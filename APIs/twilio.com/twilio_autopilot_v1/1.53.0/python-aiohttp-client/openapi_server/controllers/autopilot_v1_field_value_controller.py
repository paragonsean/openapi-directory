from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_field_type_field_value import AutopilotV1AssistantFieldTypeFieldValue
from openapi_server.models.list_field_value_response import ListFieldValueResponse
from openapi_server import util


async def create_field_value(request: web.Request, assistant_sid, field_type_sid, language, value, synonym_of=None) -> web.Response:
    """create_field_value

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the new resource.
    :type assistant_sid: str
    :param field_type_sid: The SID of the Field Type associated with the Field Value.
    :type field_type_sid: str
    :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: &#x60;en-US&#x60;
    :type language: str
    :param value: The Field Value data.
    :type value: str
    :param synonym_of: The string value that indicates which word the field value is a synonym of.
    :type synonym_of: str

    """
    return web.Response(status=200)


async def delete_field_value(request: web.Request, assistant_sid, field_type_sid, sid) -> web.Response:
    """delete_field_value

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to delete.
    :type assistant_sid: str
    :param field_type_sid: The SID of the Field Type associated with the Field Value to delete.
    :type field_type_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the FieldValue resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_field_value(request: web.Request, assistant_sid, field_type_sid, sid) -> web.Response:
    """fetch_field_value

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resource to fetch.
    :type assistant_sid: str
    :param field_type_sid: The SID of the Field Type associated with the Field Value to fetch.
    :type field_type_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the FieldValue resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_field_value(request: web.Request, assistant_sid, field_type_sid, language=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_field_value

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to read.
    :type assistant_sid: str
    :param field_type_sid: The SID of the Field Type associated with the Field Value to read.
    :type field_type_sid: str
    :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: &#x60;en-US&#x60;
    :type language: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
