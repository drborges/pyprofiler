from nose.tools import raises
from sure import expect
from mock import Mock, patch

from profiler import Profiler, InvalidProfileError

def create_profiler():
  datetime = Mock('datetime')
  datetime.now = Mock(side_effect = [2, 10, 12, 15])

  return Profiler(datetime)

def test_start_should_return_profiler_instance():
  profiler = Profiler()
  expect(profiler.start('profile id')).to.equal(profiler)

def test_start_should_create_inital_profile():
  profiler = Profiler()
  expect(profiler.profiles).to.be.empty

  profiler.start('profile id')
  expect('profile id').to.be.within(profiler.profiles)

@patch('profiler.datetime')
def test_start_should_record_profiling_start_time(mocked_datetime):
  mocked_datetime.now = Mock(return_value=2)

  profiler = Profiler().start('id')

  expect(profiler.profiles['id']['started']).to.equal(2)

def test_stop_should_return_profiler_instance():
  profiler = Profiler()
  expect(profiler.start('id').stop('id')).to.equal(profiler)

@patch('profiler.datetime')
def test_stop_should_record_profiling_stop_time(mocked_datetime):
  mocked_datetime.now = Mock(side_effect = [2, 10])

  profiler = Profiler().start('id').stop('id')

  expect(profiler.profiles['id']['stopped']).to.equal(10)

@patch('profiler.datetime')
def test_stop_should_record_profiling_elapsed_time(mocked_datetime):
  mocked_datetime.now = Mock(side_effect = [2, 10])

  profiler = Profiler().start('id').stop('id')

  expect(profiler.profiles['id']['elapsed']).to.equal(8)

@raises(InvalidProfileError)
def test_should_not_stop_profiling_before_starting_it():
  Profiler().stop('id')

@patch('profiler.datetime')
def test_creates_checkpoints_for_profile(mocked_datetime):
  mocked_datetime.now = Mock(side_effect = [2, 10, 12, 15])

  profiler = Profiler().start('id').checkpoint('id').checkpoint('id')

  expect(profiler.profiles['id']['checkpoints']).to.equal([
    { 'time': 10, 'elapsed': 8 },
    { 'time': 12, 'elapsed': 10 }
  ])

@raises(InvalidProfileError)
def test_profiler_should_not_create_checkpoint_before_starting_profiling():
  Profiler().checkpoint('profile id')

@raises(InvalidProfileError)
def test_profiler_should_not_create_checkpoint_for_inexistent_profile():
  Profiler().start('profile id').checkpoint('inexistent profile id')