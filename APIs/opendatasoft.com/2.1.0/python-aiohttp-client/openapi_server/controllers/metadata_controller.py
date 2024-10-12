from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_metadata_templates_type200_response import GetMetadataTemplatesType200Response
from openapi_server.models.get_metadata_templates_type200_response_metadata_templates_inner import GetMetadataTemplatesType200ResponseMetadataTemplatesInner
from openapi_server.models.get_root200_response import GetRoot200Response
from openapi_server import util


async def get_metadata_template(request: web.Request, source, metadata_template_type, metadata_template_name) -> web.Response:
    """get_metadata_template

    A single metadata_template 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param metadata_template_type: 
    :type metadata_template_type: str
    :param metadata_template_name: 
    :type metadata_template_name: str

    """
    return web.Response(status=200)


async def get_metadata_templates_type(request: web.Request, source, metadata_template_type) -> web.Response:
    """get_metadata_templates_type

    List of metadata templates available for this type. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param metadata_template_type: 
    :type metadata_template_type: str

    """
    return web.Response(status=200)


async def get_metadata_templates_types(request: web.Request, source) -> web.Response:
    """get_metadata_templates_types

    List of available metadata templates types, each with their endpoints. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str

    """
    return web.Response(status=200)
