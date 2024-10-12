from typing import List, Dict
from aiohttp import web

from openapi_server.models.configuration import Configuration
from openapi_server.models.individual_update import IndividualUpdate
from openapi_server.models.interactions import Interactions
from openapi_server.models.new_update import NewUpdate
from openapi_server.models.profile import Profile
from openapi_server.models.profiles_inner import ProfilesInner
from openapi_server.models.schedules import Schedules
from openapi_server.models.shares import Shares
from openapi_server.models.shuffle import Shuffle
from openapi_server.models.success import Success
from openapi_server.models.update import Update
from openapi_server.models.updates_array import UpdatesArray
from openapi_server.models.user import User
from openapi_server import util


async def info_configurationmedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """info_configurationmedia_type_extension_get

    Returns an object with the current configuration that Buffer is using, including supported services, their icons and the varying limits of character and schedules.

    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def links_sharesmedia_type_extension_get(request: web.Request, media_type_extension, url) -> web.Response:
    """links_sharesmedia_type_extension_get

    Returns an object with a the numbers of shares a link has had using Buffer.

    :param media_type_extension: 
    :type media_type_extension: str
    :param url: URL-encoded URL of the page for which the number of shares is requested.
    :type url: str

    """
    return web.Response(status=200)


async def profiles_id_schedules_updatemedia_type_extension_post(request: web.Request, id, media_type_extension) -> web.Response:
    """profiles_id_schedules_updatemedia_type_extension_post

    \&quot;Set the posting schedules for the specified social media profile. 

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def profiles_id_schedulesmedia_type_extension_get(request: web.Request, id, media_type_extension) -> web.Response:
    """profiles_id_schedulesmedia_type_extension_get

    Returns details of the posting schedules associated with a social media profile.

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def profiles_id_updates_pendingmedia_type_extension_get(request: web.Request, id, media_type_extension, page=None, count=None, since=None, utc=None) -> web.Response:
    """profiles_id_updates_pendingmedia_type_extension_get

    \&quot;Returns an array of updates that are currently in the buffer for an individual social media profile. 

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str
    :param page: Specifies the page of status updates to receive. If not specified the first page of results will be returned.
    :type page: int
    :param count: Specifies the number of status updates to receive. If provided, must be between 1 and 100.
    :type count: int
    :param since: Specifies a unix timestamp which only status updates created after this time will be retrieved.
    :type since: str
    :param utc: If utc is set times will be returned relative to UTC rather than the users associated timezone.
    :type utc: bool

    """
    since = util.deserialize_date(since)
    return web.Response(status=200)


async def profiles_id_updates_reordermedia_type_extension_post(request: web.Request, id, media_type_extension) -> web.Response:
    """profiles_id_updates_reordermedia_type_extension_post

    Edit the order at which statuses for the specified social media profile will be sent out of the buffer. 

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def profiles_id_updates_sentmedia_type_extension_get(request: web.Request, id, media_type_extension, page=None, count=None, since=None, utc=None) -> web.Response:
    """profiles_id_updates_sentmedia_type_extension_get

    Returns an array of updates that have been sent from the buffer for an individual social media profile. 

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str
    :param page: Specifies the page of status updates to receive. If not specified the first page of results will be returned.
    :type page: int
    :param count: Specifies the number of status updates to receive. If provided, must be between 1 and 100.
    :type count: int
    :param since: Specifies a unix timestamp which only status updates created after this time will be retrieved.
    :type since: str
    :param utc: If utc is set times will be returned relative to UTC rather than the users associated timezone.
    :type utc: bool

    """
    since = util.deserialize_date(since)
    return web.Response(status=200)


async def profiles_id_updates_shufflemedia_type_extension_post(request: web.Request, id, media_type_extension) -> web.Response:
    """profiles_id_updates_shufflemedia_type_extension_post

    Randomize the order at which statuses for the specified social media profile will be sent out of the buffer. 

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def profiles_idmedia_type_extension_get(request: web.Request, media_type_extension, id) -> web.Response:
    """profiles_idmedia_type_extension_get

    Returns details of the single specified social media profile.

    :param media_type_extension: 
    :type media_type_extension: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def profilesmedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """profilesmedia_type_extension_get

    Returns an array of social media profiles connected to a users account.

    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def updates_createmedia_type_extension_post(request: web.Request, media_type_extension) -> web.Response:
    """updates_createmedia_type_extension_post

    Create one or more new status updates. 

    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def updates_id_destroymedia_type_extension_post(request: web.Request, id, media_type_extension) -> web.Response:
    """updates_id_destroymedia_type_extension_post

    Permanently delete an existing status update.

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def updates_id_interactionsmedia_type_extension_get(request: web.Request, id, media_type_extension, event, page=None, count=None) -> web.Response:
    """updates_id_interactionsmedia_type_extension_get

    Returns the detailed information on individual interactions with the social media update such as favorites, retweets and likes. 

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str
    :param event: Specifies a type of event to be retrieved, for example \&quot;retweet\&quot;, \&quot;like\&quot;, \&quot;comment\&quot;, \&quot;mention\&quot; or \&quot;reshare\&quot;. They can also be plural (e.g., \&quot;reshares\&quot;). Plurality has no effect other than visual semantics. See /info/configuration for more information on supported interaction events. 
    :type event: str
    :param page: Specifies the page of status updates to receive. If not specified the first page of results will be returned.
    :type page: int
    :param count: Specifies the number of status updates to receive. If provided, must be between 1 and 100.
    :type count: int

    """
    return web.Response(status=200)


async def updates_id_move_to_topmedia_type_extension_post(request: web.Request, id, media_type_extension) -> web.Response:
    """updates_id_move_to_topmedia_type_extension_post

    Move an existing status update to the top of the queue and recalculate times for all updates in the queue. Returns the update with its new posting time.

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def updates_id_sharemedia_type_extension_post(request: web.Request, id, media_type_extension) -> web.Response:
    """updates_id_sharemedia_type_extension_post

    Immediately shares a single pending update and recalculates times for updates remaining in the queue.

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def updates_id_updatemedia_type_extension_post(request: web.Request, id, media_type_extension) -> web.Response:
    """updates_id_updatemedia_type_extension_post

    Edit an existing, individual status update. 

    :param id: 
    :type id: str
    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def updates_idmedia_type_extension_get(request: web.Request, media_type_extension, id) -> web.Response:
    """updates_idmedia_type_extension_get

    Returns a single social media update.

    :param media_type_extension: 
    :type media_type_extension: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def usermedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """usermedia_type_extension_get

    Returns a single user.

    :param media_type_extension: 
    :type media_type_extension: str

    """
    return web.Response(status=200)
