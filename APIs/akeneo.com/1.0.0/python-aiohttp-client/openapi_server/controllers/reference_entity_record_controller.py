from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_assets200_response_inner import PatchAssets200ResponseInner
from openapi_server.models.patch_reference_entity_records_code_request import PatchReferenceEntityRecordsCodeRequest
from openapi_server.models.patch_reference_entity_records_request_inner import PatchReferenceEntityRecordsRequestInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.reference_entity_record import ReferenceEntityRecord
from openapi_server import util


async def get_reference_entity_records(request: web.Request, reference_entity_code, search=None, channel=None, locales=None, search_after=None) -> web.Response:
    """Get the list of the records of a reference entity

    This endpoint allows you to get a list of records of a given reference entity. Records are paginated and can be filtered.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param search: Filter records of the reference entity, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-reference-entity-records\&quot;&gt;Filters&lt;/a&gt; section
    :type search: str
    :param channel: Filter attribute values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-channel\&quot;&gt;Filter attribute values by channel&lt;/a&gt; section
    :type channel: str
    :param locales: Filter attribute values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-locale\&quot;&gt;Filter attribute values by locale&lt;/a&gt; section
    :type locales: str
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str

    """
    return web.Response(status=200)


async def get_reference_entity_records_code(request: web.Request, reference_entity_code, code) -> web.Response:
    """Get a record of a given reference entity

    This endpoint allows you to get the information about a given record for a given reference entity.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_reference_entity_records(request: web.Request, reference_entity_code, body) -> web.Response:
    """Update/create several reference entity records

    This endpoint allows you to update and/or create several records of one given reference entity at once. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the record does not already exist for the given reference entity, it creates it.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchReferenceEntityRecordsRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def patch_reference_entity_records_code(request: web.Request, reference_entity_code, code, body) -> web.Response:
    """Update/create a record of a given reference entity

    This endpoint allows you to update a given record of a given renference entity. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the record does not already exist for the given reference entity, it creates it.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchReferenceEntityRecordsCodeRequest.from_dict(body)
    return web.Response(status=200)
