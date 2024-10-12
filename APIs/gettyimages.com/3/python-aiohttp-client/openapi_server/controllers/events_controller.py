from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_detail_field_values import EventDetailFieldValues
from openapi_server import util


async def v3_events_get(request: web.Request, accept_language=None, ids=None, fields=None) -> web.Response:
    """Get metadata for multiple events

    This endpoint returns the detailed event metadata for all specified events. Getty Images news, sports and entertainment photographers and videographers cover editorially relevant events occurring around the world.  All images or video clips produced in association with  an event, are assigned the same EventID. EventIDs are part of the meta-data returned in SearchForImages Results. Only content  produced under a Getty Images brand name (Getty Images News, Getty Images Sports, Getty Images Entertainment, Film Magic, Wire Image)  will be consistently assigned an EventID. The Event framework may also be used to group similar content, such as  \&quot;Hats from the Royal Wedding\&quot; or \&quot;Odd-ballOffbeat images of the week\&quot;.   You&#39;ll need an API key and access token to use this resource. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param ids: A comma separated list of event ids.
    :type ids: List[int]
    :param fields: A comma separated list of fields to return in the response.
    :type fields: list | bytes

    """
    fields = [EventDetailFieldValues.from_dict(d) for d in fields]
    return web.Response(status=200)


async def v3_events_id_get(request: web.Request, id, accept_language=None, fields=None) -> web.Response:
    """Get metadata for a single event

    This endpoint returns the detailed event metadata for a specified event. Getty Images news, sports and entertainment  photographers and videographers cover editorially relevant events occurring around the world.   All images or video clips produced in association with an event, are assigned the same EventID.  EventIDs are part of the meta-data returned in SearchForImages Results. Only content produced under a Getty Images  brand name (Getty Images News, Getty Images Sports, Getty Images Entertainment, Film Magic, Wire Image) will be  consistently assigned an EventID. The Event framework may also be used to group similar content, such as  \&quot;Hats from the Royal Wedding\&quot; or \&quot;Odd-ballOffbeat images of the week\&quot;.   You&#39;ll need an API key and access token to use this resource. 

    :param id: An event id.
    :type id: int
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param fields: A comma separated list of fields to return in the response.
    :type fields: list | bytes

    """
    fields = [EventDetailFieldValues.from_dict(d) for d in fields]
    return web.Response(status=200)
