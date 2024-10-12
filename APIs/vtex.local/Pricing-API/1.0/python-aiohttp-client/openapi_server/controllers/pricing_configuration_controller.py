from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_pricingv2_status200_response import GetPricingv2Status200Response
from openapi_server.models.pricing_configuration import PricingConfiguration
from openapi_server import util


async def get_pricing_config(request: web.Request, content_type, accept) -> web.Response:
    """Get Pricing Configuration

    Retrieves Pricing Configuration.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;hasMigrated\&quot;: true,      \&quot;migrationStatus\&quot;: \&quot;Completed\&quot;,      \&quot;defaultMarkup\&quot;: 100,      \&quot;priceVariation\&quot;: {          \&quot;upperLimit\&quot;: null,          \&quot;lowerLimit\&quot;: null      },      \&quot;minimumMarkups\&quot;: {          \&quot;1\&quot;: 100,          \&quot;2\&quot;: 90      },      \&quot;tradePolicyConfigs\&quot;: [],      \&quot;sellersToOverride\&quot;: [],      \&quot;hasPriceInheritance\&quot;: false,      \&quot;priceInheritance\&quot;: \&quot;never\&quot;,      \&quot;hasOptionalBasePrice\&quot;: false,      \&quot;blockAccount\&quot;: false,      \&quot;blockedRoutes\&quot;: null,      \&quot;priceTableSelectionStrategy\&quot;: \&quot;first\&quot;,      \&quot;priceTableLimit\&quot;: null  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def get_pricingv2_status(request: web.Request, content_type, accept) -> web.Response:
    """Get Pricing v2 Status

    Retrieves Pricing v2 Status.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;isActive\&quot;: true,      \&quot;hasMigrated\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
