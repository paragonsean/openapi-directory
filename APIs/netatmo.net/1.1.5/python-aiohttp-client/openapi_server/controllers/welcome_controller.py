from typing import List, Dict
from aiohttp import web

from openapi_server.models.na_welcome_event_response import NAWelcomeEventResponse
from openapi_server.models.na_welcome_home_data_response import NAWelcomeHomeDataResponse
from openapi_server.models.na_welcome_persons_away_response import NAWelcomePersonsAwayResponse
from openapi_server.models.na_welcome_persons_home_response import NAWelcomePersonsHomeResponse
from openapi_server.models.na_welcome_webhook_response import NAWelcomeWebhookResponse
from openapi_server import util


async def addwebhook(request: web.Request, url, app_type) -> web.Response:
    """addwebhook

    Links a callback url to a user. 

    :param url: Your webhook callback url
    :type url: str
    :param app_type: Webhooks are only available for Welcome, enter app_camera.
    :type app_type: str

    """
    return web.Response(status=200)


async def dropwebhook(request: web.Request, app_type) -> web.Response:
    """dropwebhook

    Dissociates a webhook from a user. 

    :param app_type: For Welcome, use app_camera
    :type app_type: str

    """
    return web.Response(status=200)


async def getcamerapicture(request: web.Request, image_id, key) -> web.Response:
    """getcamerapicture

    Returns the snapshot associated to an event. 

    :param image_id: id of the image (can be retrieved as &#39;id&#39; in &#39;face&#39; in Gethomedata, or as &#39;id&#39; in &#39;snapshot&#39; in Getnextevents, Getlasteventof and Geteventsuntil)
    :type image_id: str
    :param key: Security key to access snapshots.
    :type key: str

    """
    return web.Response(status=200)


async def geteventsuntil(request: web.Request, home_id, event_id) -> web.Response:
    """geteventsuntil

    Returns the snapshot associated to an event. 

    :param home_id: ID of the Home you&#39;re interested in
    :type home_id: str
    :param event_id: Your request will retrieve all the events until this one
    :type event_id: str

    """
    return web.Response(status=200)


async def gethomedata(request: web.Request, home_id=None, size=None) -> web.Response:
    """gethomedata

    Returns information about users homes and cameras. 

    :param home_id: Specify if you&#39;re looking for the events of a specific Home.
    :type home_id: str
    :param size: Number of events to retrieve. Default is &#x60;30&#x60;.
    :type size: int

    """
    return web.Response(status=200)


async def getlasteventof(request: web.Request, home_id, person_id, offset=None) -> web.Response:
    """getlasteventof

    Returns most recent events. 

    :param home_id: ID of the Home you&#39;re interested in
    :type home_id: str
    :param person_id: Your request will retrieve all events of the given home until the most recent event of the given person
    :type person_id: str
    :param offset: Number of events to retrieve. Default is 30.
    :type offset: int

    """
    return web.Response(status=200)


async def getnextevents(request: web.Request, home_id, event_id, size=None) -> web.Response:
    """getnextevents

    Returns previous events. 

    :param home_id: ID of the Home you&#39;re interested in
    :type home_id: str
    :param event_id: Your request will retrieve events occured before this one
    :type event_id: str
    :param size: Number of events to retrieve. Default is 30.
    :type size: int

    """
    return web.Response(status=200)


async def setpersonsaway(request: web.Request, home_id, person_id=None) -> web.Response:
    """setpersonsaway

    Sets a person as &#39;Away&#39; or the Home as &#39;Empty&#39;. The event will be added to the user’s timeline. 

    :param home_id: ID of the Home you&#39;re interested in
    :type home_id: str
    :param person_id: If a person_id is specified, that person will be set as &#39;Away&#39;. If no person_id is specified, the Home will be set as &#39;Empty&#39;.
    :type person_id: str

    """
    return web.Response(status=200)


async def setpersonshome(request: web.Request, home_id, person_ids) -> web.Response:
    """setpersonshome

    Sets a person as &#39;At home&#39;. 

    :param home_id: ID of the Home you&#39;re interested in
    :type home_id: str
    :param person_ids: List of persons IDs
    :type person_ids: str

    """
    return web.Response(status=200)
