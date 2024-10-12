from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hook import Hook
from openapi_server.models.hook_output import HookOutput
from openapi_server import util


async def create_hook(request: web.Request, event_type, subscriber_type, actions=None, status=None, subscriber_address=None, subscriber_language=None, subscriber_name=None, subscriber_url=None) -> web.Response:
    """Creates a hook subscription

    Creates a hook subscription to notify events in Truora plataform. Subscriptions broadcast data as events occur and additional subscription instances are not required in order to refresh the information. Events are received in an array as a JWT and are decoded using the signing key returned by this endpoint. Their structure is as follows:  &#x60;&#x60;&#x60; {     \&quot;events\&quot;: [         {             \&quot;event_action\&quot;: \&quot;created\&quot;,             \&quot;event_type\&quot;: \&quot;check\&quot;,             \&quot;id\&quot;: \&quot;HKEdd28c569cf5eb74e45f0f4c092096e62c1c95ba2\&quot;,             \&quot;object\&quot;: {                 \&quot;check_id\&quot;: \&quot;CHK9c39003424c521aec8566ce59e1ddc86\&quot;,                 \&quot;country\&quot;: \&quot;CO\&quot;,                 \&quot;creation_date\&quot;: \&quot;2020-04-01T23:00:30.581232281Z\&quot;,                 \&quot;homonym_score\&quot;: 0,                 \&quot;id_score\&quot;: 0,                 \&quot;national_id\&quot;: \&quot;1151959906\&quot;,                 \&quot;previous_check\&quot;: \&quot;CHK4ec814fecd147eaae41027081d7d5caf\&quot;,                 \&quot;score\&quot;: -1,                 \&quot;status\&quot;: \&quot;not_started\&quot;,                 \&quot;type\&quot;: \&quot;person\&quot;,                 \&quot;update_date\&quot;: \&quot;2020-04-01T23:00:30.680937413Z\&quot;             },             \&quot;timestamp\&quot;: \&quot;2020-04-01T23:00:30Z\&quot;,             \&quot;version\&quot;: \&quot;1.0\&quot;         }     ],     \&quot;iat\&quot;: 1585782031,     \&quot;iss\&quot;: \&quot;Truora\&quot; } &#x60;&#x60;&#x60;  Keep in mind that the object attribute varies depending on the event_type.

    :param event_type: The entity events the client wants to subscribe
    :type event_type: str
    :param subscriber_type: A platform with an endpoint ready to process the information
    :type subscriber_type: str
    :param actions: Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
    :type actions: List[str]
    :param status: indicates whether the hook is active or not. enabled by default
    :type status: str
    :param subscriber_address: Email address where the notification is to be sent. Required if subscriber_type was set to email
    :type subscriber_address: str
    :param subscriber_language: Language for the notification to be sent
    :type subscriber_language: str
    :param subscriber_name: Name of the person to be notified
    :type subscriber_name: str
    :param subscriber_url: URL where the notification is to be sent. Required only if subscriber_type is set to web
    :type subscriber_url: str

    """
    return web.Response(status=200)


async def delet_hook(request: web.Request, hook_id) -> web.Response:
    """Deletes hook

    Deletes hook configuration.

    :param hook_id: Hook ID
    :type hook_id: str

    """
    return web.Response(status=200)


async def list_hook(request: web.Request, ) -> web.Response:
    """Lists all hooks

    Lists all the configured hooks in your account.


    """
    return web.Response(status=200)


async def update_hook(request: web.Request, hook_id, event_type, subscriber_type, actions=None, status=None, subscriber_address=None, subscriber_language=None, subscriber_name=None, subscriber_url=None) -> web.Response:
    """Updates hook

    Updates a hook configuration.

    :param hook_id: Hook ID
    :type hook_id: str
    :param event_type: The entity events the client wants to subscribe
    :type event_type: str
    :param subscriber_type: A platform with an endpoint ready to process the information
    :type subscriber_type: str
    :param actions: Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
    :type actions: List[str]
    :param status: indicates whether the hook is active or not. enabled by default
    :type status: str
    :param subscriber_address: Email address where the notification is to be sent. Required if subscriber_type was set to email
    :type subscriber_address: str
    :param subscriber_language: Language for the notification to be sent
    :type subscriber_language: str
    :param subscriber_name: Name of the person to be notified
    :type subscriber_name: str
    :param subscriber_url: URL where the notification is to be sent. Required only if subscriber_type is set to web
    :type subscriber_url: str

    """
    return web.Response(status=200)
