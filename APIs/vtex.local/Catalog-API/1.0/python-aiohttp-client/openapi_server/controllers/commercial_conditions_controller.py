from typing import List, Dict
from aiohttp import web

from openapi_server.models.array_with_information_of_all_the_commercial_conditions_inner import ArrayWithInformationOfAllTheCommercialConditionsInner
from openapi_server.models.get_commercial_conditions200_response import GetCommercialConditions200Response
from openapi_server import util


async def get_all_commercial_conditions(request: web.Request, content_type, accept) -> web.Response:
    """Get all commercial conditions

    Lists all commercial conditions on the store.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1,          \&quot;Name\&quot;: \&quot;Padrão\&quot;,          \&quot;IsDefault\&quot;: true      },      {          \&quot;Id\&quot;: 2,          \&quot;Name\&quot;: \&quot;Teste Fast\&quot;,          \&quot;IsDefault\&quot;: false      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def get_commercial_conditions(request: web.Request, content_type, accept, commercial_condition_id) -> web.Response:
    """Get commercial condition

    Retrieves information of a commercial condition by its ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Padrão\&quot;,      \&quot;IsDefault\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param commercial_condition_id: Commercial condition unique numerical identifier.
    :type commercial_condition_id: int

    """
    return web.Response(status=200)
