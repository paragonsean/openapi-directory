from typing import List, Dict
from aiohttp import web

from openapi_server.models.fax_v1_fax import FaxV1Fax
from openapi_server.models.fax_v1_fax_fax_media import FaxV1FaxFaxMedia
from openapi_server.models.list_fax_media_response import ListFaxMediaResponse
from openapi_server.models.list_fax_response import ListFaxResponse
from openapi_server import util


async def delete_fax(request: web.Request, sid) -> web.Response:
    """delete_fax

    Delete a specific fax and its associated media.

    :param sid: The Twilio-provided string that uniquely identifies the Fax resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def delete_fax_media(request: web.Request, fax_sid, sid) -> web.Response:
    """delete_fax_media

    Delete a specific fax media instance.

    :param fax_sid: The SID of the fax with the FaxMedia resource to delete.
    :type fax_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the FaxMedia resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_fax(request: web.Request, sid) -> web.Response:
    """fetch_fax

    Fetch a specific fax.

    :param sid: The Twilio-provided string that uniquely identifies the Fax resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_fax_media(request: web.Request, fax_sid, sid) -> web.Response:
    """fetch_fax_media

    Fetch a specific fax media instance.

    :param fax_sid: The SID of the fax with the FaxMedia resource to fetch.
    :type fax_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the FaxMedia resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_fax(request: web.Request, _from=None, to=None, date_created_on_or_before=None, date_created_after=None, page_size=None) -> web.Response:
    """list_fax

    Retrieve a list of all faxes.

    :param _from: Retrieve only those faxes sent from this phone number, specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.
    :type _from: str
    :param to: Retrieve only those faxes sent to this phone number, specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.
    :type to: str
    :param date_created_on_or_before: Retrieve only those faxes with a &#x60;date_created&#x60; that is before or equal to this value, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type date_created_on_or_before: str
    :param date_created_after: Retrieve only those faxes with a &#x60;date_created&#x60; that is later than this value, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :type date_created_after: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int

    """
    date_created_on_or_before = util.deserialize_datetime(date_created_on_or_before)
    date_created_after = util.deserialize_datetime(date_created_after)
    return web.Response(status=200)


async def list_fax_media(request: web.Request, fax_sid, page_size=None) -> web.Response:
    """list_fax_media

    Retrieve a list of all fax media instances for the specified fax.

    :param fax_sid: The SID of the fax with the FaxMedia resources to read.
    :type fax_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int

    """
    return web.Response(status=200)
