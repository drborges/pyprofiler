from sure import expect
from mock import Mock
from datetime import datetime

from profiler import Profile
from text_formatter import TextFormatter

def test_formatter_type_should_be_txt():
  expect(TextFormatter().type()).to.equal('txt')

def test_should_format_profiles_as_plain_text():
  start = datetime(year=2014, month=3, day=25, hour=2, minute=30, second=15, microsecond=399999)
  stop = datetime(year=2014, month=3, day=25, hour=2, minute=33, second=20, microsecond=399999)

  formatted_profiles = TextFormatter().format({
    'id1': Profile('id1', started_at = start, stopped_at = stop, elapsed_time = stop - start),
    'id2': Profile('id2', started_at = start, stopped_at = stop, elapsed_time = stop - start)
  })

  expect(formatted_profiles).to.equal(
    "id2 took 0:03:05 [started at: 2:30:15.4, finished at: 2:33:20.4]" +
    "\nid1 took 0:03:05 [started at: 2:30:15.4, finished at: 2:33:20.4]"
  )