import falcon
import traceback
import requests
import json
from falcon.util.uri import parse_query_string
from falcon import HTTPFound
from .config import CONFIG
from .weather import get_conditions

class SessionCache(object):
    def __init__(self):
        self.cache = dict()

    def set(self, key, obj):
        self.cache[key] = obj
    def unset(self, key):
        if key in self.cache:
            del self.cache[key]
    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None

CACHE = SessionCache()

class UnsplashCallback(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        args = parse_query_string(req.query_string)
        image_urls = {}
        try:
            # request access token
            code = args.get('code')
            url = '{0}?{1}={2}&{3}={4}&{5}={6}&{7}={8}&{9}={10}'.format(
                CONFIG['access_token_url'],
                'client_id', CONFIG['access_key'],
                'client_secret', CONFIG['secret_key'],
                'redirect_uri', 'http://localhost:8000/callback',
                'code', code,
                'grant_type', 'authorization_code')
            q = requests.post(url)

            # Save access token
            access_token = q.json().get('access_token', None)
            CACHE.set('access_token', access_token)

            # TODO: Use proper query string
            url = '{0}?{1}={2}&{3}={4}'.format(
                CONFIG['random_photo_url'], 
                'query', list(get_conditions())[0],
                'orientation', 'landscape')
            q = requests.get(url, headers={'Authorization': 'Bearer {0}'.format(access_token)})
            print(q.status_code)
            print(q.content)
            print(q.json()['urls'])
            if q.status_code == 200:
                image_urls = q.json()['urls']
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(image_urls)
        except Exception as exc:
            traceback.print_exc()

class UnsplashResource(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        url = '{0}?{1}={2}&{3}={4}&{5}={6}&{7}={8}'.format(
        CONFIG['auth_url'],
        'client_id', CONFIG['access_key'],
        'redirect_uri', 'http://localhost:8000/callback',
        'response_type', 'code',
        'scope', 'public+read_photos')
        #q = requests.get(CONFIG['auth_url'])
        raise HTTPFound(url)