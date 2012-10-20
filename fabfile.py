from fabric.api import local, lcd, env
from datetime import datetime

env.now = datetime.today()

def clean():
  local('rm -rf ./deploy')

def regen():
  clean()
  local('hyde gen')

def serve():
  regen()
  local('hyde serve')

def article(slug):
  """Create a new article with slug=slug. Uses the template article
     located in ./content/writing/article-template.
     
     Args:
         slug (str): the slug for the article
  """
  base = 'content/writing/{year}/{slug}' \
         .format(year=env.now.year, slug=slug)
  local('mkdir -p {base}'.format(base=base))
  with lcd(base):
    local('cp ../../article-template/index.html index.html')
    f = open('{base}/index.html'.format(base=base), 'r+')
    text = f.read()
    text = text.replace('#created', 'created')
    text = text.format(date=env.now.strftime("%B %d, %Y"),
                timestamp=env.now.isoformat())
    f.seek(0)
    f.write(text)
    f.truncate()
    f.close()

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


