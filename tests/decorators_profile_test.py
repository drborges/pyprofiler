from sure import expect
from mock import Mock, call

from decorators import profile

def test_profile_decorator_creates_profiling_for_target_function():
  profiler = Mock()
  profiler.start = Mock()
  profiler.stop = Mock()
  profiler.intermediate = Mock()

  @profile(profiler)
  def fn():
    profiler.intermediate()

  fn()

  expect(profiler.mock_calls[0]).to.equal(call.start('fn'))
  expect(profiler.mock_calls[1]).to.equal(call.intermediate())
  expect(profiler.mock_calls[2]).to.equal(call.stop('fn'))
  expect(profiler.mock_calls).to.have.length_of(3)

def test_profiled_function_returns_expected_value():
  @profile(profiler = Mock())
  def sum(a, b):
    return a + b

  sum_result = sum(3, 2)

  expect(sum_result).to.equal(5)
