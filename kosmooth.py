import numpy as np
from utils import load_at2, konno_omachi_smooth


fnames = ['data/RSN763_LOMAP_GIL067.AT2', 'data/RSN763_LOMAP_GIL337.AT2']
time_series = [load_at2(fname) for fname in fnames]

# Calculate Fourier spectra
assert len(time_series[0]) == len(time_series[1])

for ts in time_series:
    ts['fourier_amps'] = np.fft.rfft(ts['accels'])

ts0 = time_series[0]
freqs = np.fft.rfftfreq(ts0['accels'].size, d=ts0['time_step'])

print(freqs)

effect_amps = np.sqrt(np.mean(
    [np.abs(ts['fourier_amps']) ** 2 for ts in time_series], axis=0))

# Smoothed spectrum
ko_bandwidth = 30
freqs_interp = np.logspace(-1, 2, num=301)

# Floating point division (from Python 3) is needed to run konno_omachi_smooth
smoothed = np.array([
    konno_omachi_smooth(freqs, effect_amps, ko_bandwidth, fc)
    for fc in freqs_interp
])

print smoothed

