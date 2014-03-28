from sure import expect
from mock import Mock, call

from decorators import profile_start

def test_profile_start_decorator_starts_profiling_for_target_function():
  profiler = Mock()
  profiler.start = Mock()
  profiler.intermediate = Mock()

  @profile_start(profiler)
  def fn():
    profiler.intermediate()

  fn()

  expect(profiler.mock_calls[0]).to.equal(call.start('fn'))
  expect(profiler.mock_calls[1]).to.equal(call.intermediate())
  expect(profiler.mock_calls).to.have.length_of(2)

def test_profiled_function_returns_expected_value():
  @profile_start(profiler = Mock())
  def sum(a, b):
    return a + b

  sum_result = sum(3, 2)

  expect(sum_result).to.equal(5)
