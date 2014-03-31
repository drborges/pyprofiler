from sure import expect
from mock import Mock, call

from decorators import profile_checkpoint

def test_profile_checkpoint_decorator():
  profiler = Mock()
  profiler.start = Mock()
  profiler.intermediate = Mock()

  @profile_checkpoint(profiler, profile_id='id')
  def fn():
    profiler.intermediate()

  fn()

  expect(profiler.mock_calls[0]).to.equal(call.checkpoint('id'))
  expect(profiler.mock_calls[1]).to.equal(call.intermediate())
  expect(profiler.mock_calls).to.have.length_of(2)

def test_profiled_function_returns_expected_value():
  @profile_checkpoint(profiler = Mock(), profile_id='id')
  def sum(a, b):
    return a + b

  sum_result = sum(3, 2)

  expect(sum_result).to.equal(5)
