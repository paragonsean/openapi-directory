from typing import List, Dict
from aiohttp import web

from openapi_server.models.createnewsession_request import CreatenewsessionRequest
from openapi_server.models.editsession_request import EditsessionRequest
from openapi_server import util


async def createnewsession(request: web.Request, body) -> web.Response:
    """Create new session

    The response should contain a session cookie. Further &#x60;POST&#x60; or &#x60;PATCH&#x60; requests will edit the existing session rather than creating a new one. All parameters in the body that are not within the public namespace will be ignored. Query string items will automatically be added to the public namespace. Cookies relevant to the session manager execution are also recorded.    &gt; The sessions API uses the &#x60;vtex_session&#x60; cookie to store the data required to identify the user and the session. This cookie is stored in the user&#39;s browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment.

    :param body: 
    :type body: dict | bytes

    """
    body = CreatenewsessionRequest.from_dict(body)
    return web.Response(status=200)


async def editsession(request: web.Request, body) -> web.Response:
    """Edit session

    This works exactly the same as the POST create session, but when the request is sent with a vtex_session cookie, it retrieves the session first and then applies the changes instead of generating a new one.    As with the &#x60;POST&#x60; method, only keys inside the public namespace on the body are considered, and query parameters are automatically added to the public namespace.    &gt; The sessions API uses the &#x60;vtex_session&#x60; cookie to store the data required to identify the user and the session. This cookie is stored in the user&#39;s browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment.

    :param body: 
    :type body: dict | bytes

    """
    body = EditsessionRequest.from_dict(body)
    return web.Response(status=200)


async def get_session(request: web.Request, items) -> web.Response:
    """Get Session

    Items are the keys of the values you wish to get. It follows the format &#x60;namespace1.key1,namespace2.key2&#x60;. So if you wish to recover the data sent on the previous request, it should be &#x60;public.country,public.postalCode&#x60;.    &gt; The sessions API uses the &#x60;vtex_session&#x60; cookie to store the data required to identify the user and the session. This cookie is stored in the user&#39;s browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment.    &gt; If you want to retrieve all keys from Session Manager, you can use the wildcard operator (&#x60;*&#x60;) in your request (i.e. &#x60;?items&#x3D;*&#x60;).

    :param items: Items are the keys of the values you wish to get. It follows the format &#x60;namespace1.key1,namespace2.key2&#x60;
    :type items: str

    """
    return web.Response(status=200)
