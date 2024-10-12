from typing import List, Dict
from aiohttp import web

from openapi_server.models.counter import Counter
from openapi_server.models.get_service200_response import GetService200Response
from openapi_server.models.metadata import Metadata
from openapi_server.models.operation_override_dto import OperationOverrideDTO
from openapi_server.models.service import Service
from openapi_server import util


async def delete_service(request: web.Request, id) -> web.Response:
    """Delete Service

    Delete a Service

    :param id: Unique identifier of Service to managed
    :type id: str

    """
    return web.Response(status=200)


async def export_snapshot(request: web.Request, service_ids) -> web.Response:
    """Export a snapshot

    Export a repostiory snapshot with requested services

    :param service_ids: List of service identifiers to export
    :type service_ids: List[str]

    """
    return web.Response(status=200)


async def get_service(request: web.Request, id, messages=None) -> web.Response:
    """Get Service

    

    :param id: Unique identifier of Service to managed
    :type id: str
    :param messages: Whether to include details on services messages into result. Default is false
    :type messages: bool

    """
    return web.Response(status=200)


async def get_services(request: web.Request, page=None, size=None) -> web.Response:
    """Get Services and APIs

    

    :param page: Page of Services to retrieve (starts at and defaults to 0)
    :type page: int
    :param size: Size of a page. Maximum number of Services to include in a response (defaults to 20)
    :type size: int

    """
    return web.Response(status=200)


async def get_services_counter(request: web.Request, ) -> web.Response:
    """Get the Services counter

    


    """
    return web.Response(status=200)


async def get_services_labels(request: web.Request, ) -> web.Response:
    """Get the already used labels for Services

    


    """
    return web.Response(status=200)


async def import_snapshot(request: web.Request, file) -> web.Response:
    """Import a snapshot

    Import a repository snapshot previsouly exported into Microcks

    :param file: The repository snapshot file
    :type file: str

    """
    return web.Response(status=200)


async def override_service_operation(request: web.Request, id, operation_name, body) -> web.Response:
    """Override Service Operation

    

    :param id: Unique identifier of Service to managed
    :type id: str
    :param operation_name: Name of operation to update
    :type operation_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = OperationOverrideDTO.from_dict(body)
    return web.Response(status=200)


async def search_services(request: web.Request, query_map) -> web.Response:
    """Search for Services and APIs

    

    :param query_map: Map of criterion. Key can be simply &#39;name&#39; with value as the searched string. You can also search by label using keys like &#39;labels.x&#39; where &#39;x&#39; is the label and value the label value
    :type query_map: Dict[str, str]

    """
    return web.Response(status=200)


async def update_service_metadata(request: web.Request, id, body) -> web.Response:
    """Update Service Metadata

    

    :param id: Unique identifier of Service to managed
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Metadata.from_dict(body)
    return web.Response(status=200)
