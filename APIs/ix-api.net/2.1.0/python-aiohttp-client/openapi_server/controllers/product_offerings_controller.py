from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.product_offering import ProductOffering
from openapi_server.models.product_offering_partial import ProductOfferingPartial
from openapi_server import util


async def product_offerings_list(request: web.Request, id=None, type=None, name=None, handover_metro_area=None, handover_metro_area_network=None, service_metro_area=None, service_metro_area_network=None, service_provider=None, downgrade_allowed=None, upgrade_allowed=None, bandwidth=None, physical_port_speed=None, service_provider_region=None, service_provider_pop=None, delivery_method=None, cloud_key=None, fields=None) -> web.Response:
    """product_offerings_list

    List all (filtered) products-offerings available on the platform

    :param id: Filter by id
    :type id: List[str]
    :param type: Filter by type
    :type type: str
    :param name: Filter by name
    :type name: str
    :param handover_metro_area: Filter by handover_metro_area
    :type handover_metro_area: str
    :param handover_metro_area_network: Filter by handover_metro_area_network
    :type handover_metro_area_network: str
    :param service_metro_area: Filter by service_metro_area
    :type service_metro_area: str
    :param service_metro_area_network: Filter by service_metro_area_network
    :type service_metro_area_network: str
    :param service_provider: Filter by service_provider
    :type service_provider: str
    :param downgrade_allowed: Filter by downgrade_allowed
    :type downgrade_allowed: str
    :param upgrade_allowed: Filter by upgrade_allowed
    :type upgrade_allowed: str
    :param bandwidth: Find product offerings where bandwidth is within the range of &#x60;bandwidth_min&#x60; and &#x60;bandwidth_max&#x60;.
    :type bandwidth: int
    :param physical_port_speed: Filter by physical_port_speed
    :type physical_port_speed: int
    :param service_provider_region: Filter by service_provider_region
    :type service_provider_region: str
    :param service_provider_pop: Filter by service_provider_pop
    :type service_provider_pop: str
    :param delivery_method: Filter by delivery_method
    :type delivery_method: str
    :param cloud_key: For product offerings of type &#x60;cloud_vc&#x60;, if the &#x60;service_provider_workflow&#x60; is &#x60;provider_first&#x60; the &#x60;cloud_key&#x60; will be used for filtering the relevant offerings.
    :type cloud_key: str
    :param fields: Returned objects only have properties which are present in the list of fields. The required &#x60;type&#x60; property is *implicitly* included. The results are *deduplicated*. 
    :type fields: str

    """
    return web.Response(status=200)


async def product_offerings_read(request: web.Request, id) -> web.Response:
    """product_offerings_read

    Get a single products-offering by id.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
