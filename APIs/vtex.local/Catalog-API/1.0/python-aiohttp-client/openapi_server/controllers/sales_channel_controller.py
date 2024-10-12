from typing import List, Dict
from aiohttp import web

from openapi_server.models.sales_channelby_id200_response import SalesChannelbyId200Response
from openapi_server import util


async def sales_channel_list(request: web.Request, content_type, accept) -> web.Response:
    """Get Sales Channel List

    Retrieves a list with details about the store&#39;s sales channels.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1,          \&quot;Name\&quot;: \&quot;Loja Principal\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;ProductClusterId\&quot;: null,          \&quot;CountryCode\&quot;: \&quot;BRA\&quot;,          \&quot;CultureInfo\&quot;: \&quot;pt-BR\&quot;,          \&quot;TimeZone\&quot;: \&quot;E. South America Standard Time\&quot;,          \&quot;CurrencyCode\&quot;: \&quot;BRL\&quot;,          \&quot;CurrencySymbol\&quot;: \&quot;R$\&quot;,          \&quot;CurrencyLocale\&quot;: 1046,          \&quot;CurrencyFormatInfo\&quot;: {              \&quot;CurrencyDecimalDigits\&quot;: 1,              \&quot;CurrencyDecimalSeparator\&quot;: \&quot;,\&quot;,              \&quot;CurrencyGroupSeparator\&quot;: \&quot;.\&quot;,              \&quot;CurrencyGroupSize\&quot;: 3,              \&quot;StartsWithCurrencySymbol\&quot;: true          },          \&quot;Origin\&quot;: null,          \&quot;Position\&quot;: 2,          \&quot;ConditionRule\&quot;: null,          \&quot;CurrencyDecimalDigits\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def sales_channelby_id(request: web.Request, content_type, accept, sales_channel_id) -> web.Response:
    """Get Sales Channel by ID

    Retrieves a specific sales channel by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Loja Principal\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ProductClusterId\&quot;: null,      \&quot;CountryCode\&quot;: \&quot;BRA\&quot;,      \&quot;CultureInfo\&quot;: \&quot;pt-BR\&quot;,      \&quot;TimeZone\&quot;: \&quot;E. South America Standard Time\&quot;,      \&quot;CurrencyCode\&quot;: \&quot;BRL\&quot;,      \&quot;CurrencySymbol\&quot;: \&quot;R$\&quot;,      \&quot;CurrencyLocale\&quot;: 1046,      \&quot;CurrencyFormatInfo\&quot;: {          \&quot;CurrencyDecimalDigits\&quot;: 1,          \&quot;CurrencyDecimalSeparator\&quot;: \&quot;,\&quot;,          \&quot;CurrencyGroupSeparator\&quot;: \&quot;.\&quot;,          \&quot;CurrencyGroupSize\&quot;: 3,          \&quot;StartsWithCurrencySymbol\&quot;: true      },      \&quot;Origin\&quot;: null,      \&quot;Position\&quot;: 2,      \&quot;ConditionRule\&quot;: null,      \&quot;CurrencyDecimalDigits\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sales_channel_id: 
    :type sales_channel_id: str

    """
    return web.Response(status=200)
