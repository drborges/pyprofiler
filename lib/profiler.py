from datetime import datetime

class Profile:

  def __init__(self, id):
    self._id = id
    self._checkpoints = []

  def checkpoint(self):
    current_time = datetime.now()
    self._checkpoints.append({
      'time': current_time,
      'elapsed': current_time - self.started_at
    })

  @property
  def started_at(self, value):
    self._started_at = value
    return self

  @property
  def stopped_at(self, value):
    self._stopped_at = value
    return self

  @property
  def elapsed_time(self, value):
    self._elapsed_time = value
    return self

class Profiler:

  def __init__(self):
    self.profiles = {}

  def start(self, profile_id):
    self.profiles[profile_id] = { 'started': datetime.now() }
    return self

  def stop(self, profile_id):
    if profile_id not in self.profiles:
      raise InvalidProfileError(profile_id)

    profile = self.profiles[profile_id]
    profile['stopped'] = datetime.now()
    profile['elapsed'] = profile['stopped'] - profile['started']
    return self

  def checkpoint(self, profile_id):
    if profile_id not in self.profiles:
      raise InvalidProfileError(profile_id)

    current_time = datetime.now()

    profile = self.profiles[profile_id]
    if 'checkpoints' not in profile:
      profile['checkpoints'] = []

    profile['checkpoints'].append({
      'time': current_time,
      'elapsed': current_time - profile['started']
    })

    return self

class InvalidProfileError(Exception):
  def __init__(self, profile_id):
    self.profile_id = profile_id

  def __str__(self):
    return 'Invalid profile id: ' + self.profile_id