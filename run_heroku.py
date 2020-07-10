from Register.client_advanced import client
import os
from Register import config

if __name__ == '__main__':
  client.start()
  topics = [
        '#',
    ]
  sub_topics = list(map(lambda x: os.environ['TOPIC_BASE'] + '/' + x, topics))
  print('Subscribe to {}'.format(', '.join(sub_topics)))
  # Give a list to subscribe() to subscribe to multiple topics.
  client.subscribe(sub_topics)
  print('Subscribe to {}/unit{:d}/2'.format(config.TOPIC_BASE, int(config.UNIT)))
  client.subscribe('pbl1/unit{:d}/2'.format(int(config.UNIT)))