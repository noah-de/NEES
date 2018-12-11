from nose.tools import raises
from utils import load_at2


@raises(IOError)
def test_load_at2_with_bad_paths():
    load_at2('bad/path')
