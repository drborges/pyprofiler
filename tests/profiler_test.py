from sure import expect
from mock import Mock

from profiler import Profiler

def create_profiler():
  datetime = Mock('datetime')
  datetime.now = Mock(side_effect = [2, 10, 12, 15])

  return Profiler(datetime)

def test_start_should_return_profiler_instance():
  profiler = create_profiler()
  expect(profiler.start('profile id')).to.equal(profiler)

def test_start_should_create_inital_profile():
  profiler = create_profiler()
  expect(profiler.profiles).to.be.empty

  profiler.start('profile id')
  expect('profile id').to.be.within(profiler.profiles)

def test_start_should_record_profiling_start_time():
  profiler = create_profiler().start('id')
  print profiler.datetime.now()
  expect(profiler.profiles['id']['started']).to.equal(2)

def test_stop_should_return_profiler_instance():
  profiler = create_profiler()
  expect(profiler.start('id').stop('id')).to.equal(profiler)

def test_stop_should_record_profiling_stop_time():
  profiler = create_profiler().start('id').stop('id')
  expect(profiler.profiles['id']['stopped']).to.equal(10)

def test_stop_should_record_profiling_elapsed_time():
  profiler = create_profiler().start('id').stop('id')
  expect(profiler.profiles['id']['elapsed']).to.equal(8)

def test_profiler_api_should_be_chainable():
  profiler = create_profiler().start('id1').start('id2').stop('id1').stop('id2')

  expect('id1').to.be.within(profiler.profiles)
  expect('id2').to.be.within(profiler.profiles)

  expect(profiler.profiles['id1']).to.equal({
    'started': 2,
    'stopped': 12,
    'elapsed': 10
  })

  expect(profiler.profiles['id2']).to.equal({
    'started': 10,
    'stopped': 15,
    'elapsed': 5
  })