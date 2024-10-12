from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.delete_characters_character_id_mail_labels_label_id_unprocessable_entity import DeleteCharactersCharacterIdMailLabelsLabelIdUnprocessableEntity
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_mail200_ok import GetCharactersCharacterIdMail200Ok
from openapi_server.models.get_characters_character_id_mail_labels_ok import GetCharactersCharacterIdMailLabelsOk
from openapi_server.models.get_characters_character_id_mail_lists200_ok import GetCharactersCharacterIdMailLists200Ok
from openapi_server.models.get_characters_character_id_mail_mail_id_not_found import GetCharactersCharacterIdMailMailIdNotFound
from openapi_server.models.get_characters_character_id_mail_mail_id_ok import GetCharactersCharacterIdMailMailIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_mail_error520 import PostCharactersCharacterIdMailError520
from openapi_server.models.post_characters_character_id_mail_labels_label import PostCharactersCharacterIdMailLabelsLabel
from openapi_server.models.post_characters_character_id_mail_mail import PostCharactersCharacterIdMailMail
from openapi_server.models.put_characters_character_id_mail_mail_id_contents import PutCharactersCharacterIdMailMailIdContents
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def delete_characters_character_id_mail_labels_label_id(request: web.Request, character_id, label_id, datasource=None, token=None) -> web.Response:
    """Delete a mail label

    Delete a mail label  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/labels/{label_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/labels/{label_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/labels/{label_id}/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param label_id: An EVE label id
    :type label_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def delete_characters_character_id_mail_mail_id(request: web.Request, character_id, mail_id, datasource=None, token=None) -> web.Response:
    """Delete a mail

    Delete a mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/{mail_id}/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param mail_id: An EVE mail ID
    :type mail_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_mail(request: web.Request, character_id, datasource=None, if_none_match=None, labels=None, last_mail_id=None, token=None) -> web.Response:
    """Return mail headers

    Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/&#x60;  --- This route is cached for up to 30 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param labels: Fetch only mails that match one or more of the given labels
    :type labels: List[int]
    :param last_mail_id: List only mail with an ID lower than the given ID, if present
    :type last_mail_id: int
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_mail_labels(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get mail labels and unread counts

    Return a list of the users mail labels, unread counts for each label and a total unread count.  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/labels/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/mail/labels/&#x60;  --- This route is cached for up to 30 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_mail_lists(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Return mailing list subscriptions

    Return all mailing lists that the character is subscribed to  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/lists/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/lists/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/lists/&#x60;  --- This route is cached for up to 120 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_mail_mail_id(request: web.Request, character_id, mail_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Return a mail

    Return the contents of an EVE mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/{mail_id}/&#x60;  --- This route is cached for up to 30 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param mail_id: An EVE mail ID
    :type mail_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_characters_character_id_mail(request: web.Request, character_id, mail, datasource=None, token=None) -> web.Response:
    """Send a new mail

    Create and send a new mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param mail: The mail to send
    :type mail: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    mail = PostCharactersCharacterIdMailMail.from_dict(mail)
    return web.Response(status=200)


async def post_characters_character_id_mail_labels(request: web.Request, character_id, label, datasource=None, token=None) -> web.Response:
    """Create a mail label

    Create a mail label  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/labels/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/labels/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/mail/labels/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param label: Label to create
    :type label: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    label = PostCharactersCharacterIdMailLabelsLabel.from_dict(label)
    return web.Response(status=200)


async def put_characters_character_id_mail_mail_id(request: web.Request, character_id, mail_id, contents, datasource=None, token=None) -> web.Response:
    """Update metadata about a mail

    Update metadata about a mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/{mail_id}/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param mail_id: An EVE mail ID
    :type mail_id: int
    :param contents: Data used to update the mail
    :type contents: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    contents = PutCharactersCharacterIdMailMailIdContents.from_dict(contents)
    return web.Response(status=200)
