from mock import Mock
from sure import expect
from nose.tools import raises
from datetime import datetime

from profiler import Profiler, Profile, Checkpoint
from json_formatter import JsonFormatter, UnexpectedValueError

def test_should_report_as_json():
  start = datetime(year=2014, month=3, day=25, hour=2, minute=30, second=15, microsecond=399999)
  stop = datetime(year=2014, month=3, day=25, hour=2, minute=33, second=20, microsecond=399999)
  elapsed_time = stop - start

  checkpoints = [Checkpoint(start, elapsed_time), Checkpoint(start, elapsed_time)]
  profile1 = Profile(started_at = start, stopped_at = stop, elapsed_time = elapsed_time)
  profile2 = Profile(started_at = start, stopped_at = stop, elapsed_time = elapsed_time)
  profile2.checkpoints = checkpoints

  formatted_profiles = JsonFormatter().format({ 'id1': profile1, 'id2': profile2 })

  expect(formatted_profiles).to.equal('{"id1": {"checkpoints": [], "elapsed_time": "0:03:05", "started_at": "2:30:15.4", "stopped_at": "2:33:20.4"}, "id2": {"checkpoints": [{"elapsed_time": "0:03:05", "time": "2:30:15.4"}, {"elapsed_time": "0:03:05", "time": "2:30:15.4"}], "elapsed_time": "0:03:05", "started_at": "2:30:15.4", "stopped_at": "2:33:20.4"}}')

@raises(UnexpectedValueError)
def test_invalid_field_value():
  JsonFormatter().format({ 'field': object() })
