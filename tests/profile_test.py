from nose.tools import raises
from sure import expect
from mock import Mock, patch

from profiler import Profile, Checkpoint, InvalidProfileError

@patch('profiler.datetime')
def test_creates_checkpoints_for_profile(mocked_datetime):
  mocked_datetime.now = Mock(side_effect = [10, 12])

  profile = Profile('importd')
  profile.started_at = 2
  profile.checkpoint()
  profile.checkpoint()

  expect([c.__dict__ for c in profile.checkpoints]).to.equal([
    Checkpoint(time=10, elapsed_time=8).__dict__,
    Checkpoint(time=12, elapsed_time=10).__dict__
  ])