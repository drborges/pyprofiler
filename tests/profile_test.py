from nose.tools import raises
from sure import expect
from mock import Mock, patch

from profiler import Profile, InvalidProfileError

@patch('profiler.datetime')
def test_creates_checkpoints_for_profile(mocked_datetime):
  mocked_datetime.now = Mock(side_effect = [10, 12])

  profile = Profile('id')
  profile.started_at = 2
  profile.checkpoint()
  profile.checkpoint()

  expect(profile._checkpoints).to.equal([
    { 'time': 10, 'elapsed': 8 },
    { 'time': 12, 'elapsed': 10 }
  ])