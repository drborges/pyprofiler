from datetime import datetime

class Checkpoint(object):

  def __init__(self, time, elapsed_time):
    self.time = time
    self.elapsed_time = elapsed_time

class Profile(object):

  def __init__(self, started_at = None, stopped_at = None, elapsed_time = None):
    self.started_at = started_at
    self.stopped_at = stopped_at
    self.elapsed_time = elapsed_time
    self.checkpoints = []

  def checkpoint(self):
    current_time = datetime.now()
    elapsed_time = current_time - self.started_at
    self.checkpoints.append(Checkpoint(current_time, elapsed_time))

class Profiler:

  def __init__(self):
    self.profiles = {}

  def start(self, profile_id):
    profile = Profile(profile_id)
    profile.started_at = datetime.now()
    self.profiles[profile_id] = profile

    return self

  def stop(self, profile_id):
    if profile_id not in self.profiles:
      raise InvalidProfileError(profile_id)

    profile = self.profiles[profile_id]
    profile.stopped_at = datetime.now()
    profile.elapsed_time = profile.stopped_at - profile.started_at
    return self

  def checkpoint(self, profile_id):
    if profile_id not in self.profiles:
      raise InvalidProfileError(profile_id)

    self.profiles[profile_id].checkpoint()

class InvalidProfileError(Exception):
  def __init__(self, profile_id):
    self.profile_id = profile_id

  def __str__(self):
    return 'Invalid profile id: ' + self.profile_id