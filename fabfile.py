from fabric.api import local

def clean():
  local('rm -rf ./deploy')

def regen():
  clean()
  local('hyde gen')

def serve():
  regen()
  local('hyde serve')

def publish():
  regen()
  local('hyde publish -p s3')
