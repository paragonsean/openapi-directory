from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_provider_info import ServiceProviderInfo
from openapi_server.models.tnr_msg import TnrMsg
from openapi_server import util


async def capabilities(request: web.Request, ) -> web.Response:
    """capabilities

    capabilities


    """
    return web.Response(status=200)


async def search(request: web.Request, query, providers=None, search_mode=None, add_synonymy=None, timeout=None) -> web.Response:
    """search

    search

    :param query: The scientific name to search for. For example: \&quot;Bellis perennis\&quot;, \&quot;Prionus\&quot; or \&quot;Bolinus brandaris\&quot;. This is an exact search so wildcard characters are not supported.
    :type query: str
    :param providers: A list of provider id strings concatenated by comma characters. The default : \&quot;pesi,bgbm-cdm-server[col]\&quot; will be used if this parameter is not set. A list of all available provider ids can be obtained from the &#39;/capabilities&#39; service end point. Providers can be nested, that is a parent provider can have sub providers. If the id of the parent provider is supplied all subproviders will be queried. The query can also be restriced to one or more subproviders by using the following syntax: parent-id[sub-id-1,sub-id2,...]
    :type providers: str
    :param search_mode: Specifies the searchMode. Possible search modes are: scientificNameExact, scientificNameLike (begins with), vernacularNameExact, vernacularNameLike (contains), findByIdentifier. If the a provider does not support the chosen searchMode it will be skipped and the status message in the tnrClientStatus will be set to &#39;unsupported search mode&#39; in this case.
    :type search_mode: str
    :param add_synonymy: Indicates whether the synonymy of the accepted taxon should be included into the response. Turning this option on may cause an increased response time.
    :type add_synonymy: bool
    :param timeout: The maximum of milliseconds to wait for responses from any of the providers. If the timeout is exceeded the service will jut return the resonses that have been received so far. The default timeout is 0 ms (wait for ever)
    :type timeout: int

    """
    return web.Response(status=200)
