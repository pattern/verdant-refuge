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

def publish():
  regen()
  local('hyde publish -p s3')
  
  # Log the most recent commit at time of publishing:
  local('rm -f last-published.txt')
  pub = "Verdant Refuge was last published: %s" % \
        datetime.now()
  local("git log --pretty=format:'Git: %s (%h, %aD)' -n 1 \
         > last-published.txt")
  local('echo "\n%s" | cat >> last-published.txt' % pub)

