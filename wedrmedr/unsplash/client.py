# -*-coding:utf-8-*-
import falcon
from .resources import UnsplashResource, UnsplashCallback

UnsplashRes = UnsplashResource()
UnsplashCall = UnsplashCallback()

def create_app():
    app = falcon.API(middleware=[])
    app.add_route('/callback', UnsplashCall)
    app.add_route('/auth', UnsplashRes)
    return app

API = create_app()