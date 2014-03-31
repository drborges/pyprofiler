class profile(object):
  def __init__(self, profiler):
    self.profiler = profiler

  def __call__(self, fn):
    def wrapper(*args):
      self.profiler.start(fn.__name__)
      result = fn(*args)
      self.profiler.stop(fn.__name__)

      return result

    return wrapper

class profile_start(object):
  def __init__(self, profiler):
    self.profiler = profiler

  def __call__(self, fn):
    def wrapper(*args):
      self.profiler.start(fn.__name__)
      result = fn(*args)

      return result

    return wrapper

class profile_stop(object):
  def __init__(self, profiler):
    self.profiler = profiler

  def __call__(self, fn):
    def wrapper(*args):
      result = fn(*args)
      self.profiler.stop(fn.__name__)

      return result

    return wrapper

class profile_checkpoint(object):
  def __init__(self, profiler, profile_id):
    self.profiler = profiler
    self.profile_id = profile_id

  def __call__(self, fn):
    def wrapper(*args):
      self.profiler.checkpoint(self.profile_id)
      result = fn(*args)

      return result

    return wrapper
