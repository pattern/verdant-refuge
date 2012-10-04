from fabric.api import local
from datetime import datetime

def clean():
  local('rm -rf ./deploy')

def regen():
  clean()
  local('hyde gen')

def serve():
  regen()
  local('hyde serve')

def last_published():
  # CURRENTLY NOT FUNCTIONING AS INTENDED!
  # Log the most recent commit at time of publishing:
  filename = 'content/last-published.txt'
  local('rm -f %s' % filename)
  date = "Verdant Refuge was last published: %s" % datetime.now()
  local("git log --pretty=format:'Git: %s (%h, %aD)' -n 1 \
         > %s" % filename)
  local('echo "\n%s" | cat >> %s' % (date, filename))

def publish():
  regen()
  local('hyde publish -p s3')


