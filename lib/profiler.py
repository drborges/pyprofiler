class Profiler:

  def __init__(self, datetime):
    self.profiles = {}
    self.datetime = datetime

  def start(self, id):
    self.profiles[id] = { 'started': self.datetime.now() }
    return self

  def stop(self, id):
    profile = self.profiles[id]
    profile['stopped'] = self.datetime.now()
    profile['elapsed'] = profile['stopped'] - profile['started']
    return self