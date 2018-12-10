from __future__ import division

import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numba


def load_at2(fname):
    with open(fname) as fp:
        # Skip 3 header lines
        for _ in range(3):
            next(fp)
        # Find count and timestep.
        # Ex: 'NPTS=   5093, DT=   .0100 SEC, '
        # Here a regular expression is used to find numbers in the line
        parts = re.findall(r'[.0-9]+', next(fp))
        count = int(parts[0])
        time_step = float(parts[1])
        accels = np.array([p for l in fp for p in l.split()]).astype(float)
    return {'time_step': time_step, 'accels': accels}


@numba.jit
def konno_omachi_smooth(freqs, amps, bandwidth, fc):
    # FIXME revisit this
    # Limiting calculation at 3 provides a window value of 4.9E-6 and speeds up
    # calculation
    max_ratio = 10 ** (3 / bandwidth)

    window_total = 0
    total = 0

    for i, freq in enumerate(freqs):
        if abs(freq - fc) < 1E-6:
            window = 1.
        elif (abs(freq - 0) < 1E-6) or (abs(fc - 0) < 1E-6):
            window = 0
        elif (freq / float(fc)) > max_ratio or (fc / float(freq)) > max_ratio:
            continue
        else:
            x = bandwidth * np.log10(freq / float(fc))
            window = (np.sin(x) / float(x)) ** 4

        total += window * amps[i]
        window_total += window

    return total / float(window_total)
