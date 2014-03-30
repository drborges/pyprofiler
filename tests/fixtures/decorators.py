class mock_dep:
  def __init__(self, mock_fn):
    self.mock_fn = mock_fn

  def __call__(self, fn):
    # function wrapper has to follow nose testMatch naming
    # conventions so that the test can be picked up by the
    # nose test discovering mechanism
    def test_wrapper(*args):
      return fn(self.mock_fn())

    return test_wrapper