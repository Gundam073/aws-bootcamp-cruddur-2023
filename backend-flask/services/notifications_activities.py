from datetime import datetime, timedelta, timezone
from opentelemetry import trace

tracer = trace.get_tracer("notification.activities")
class NotificationsActivities:
  def run():
    with tracer.start_as_current_span("notification-activities-mock-data"):
       span = trace.get_current_span()
       now = datetime.now(timezone.utc).astimezone()
       span.set_attribute("app.now", now.isoformat())
       span.set_attribute("wow.now", "?")
    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'Darth Vaders cousin',
      'message': 'Bootcamp is very very fun!',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 7,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Worf',
        'message': 'This post has no honor!',
        'likes_count': 0,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }]
    }
    ]
    for item in results:
      span.set_attribute("handle","".format(item['handle']))

    return results