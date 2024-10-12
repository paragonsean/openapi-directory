from typing import List, Dict
from aiohttp import web

from openapi_server.models.getallpricetablesandrules200_response_inner import Getallpricetablesandrules200ResponseInner
from openapi_server.models.getrulesforapricetable200_response import Getrulesforapricetable200Response
from openapi_server.models.pricing_pipeline_catalog_price_table_id_put_request import PricingPipelineCatalogPriceTableIdPutRequest
from openapi_server import util


async def getallpricetablesandrules(request: web.Request, content_type, accept) -> web.Response:
    """Get all price tables and their rules

    This method will retrieve all price tables and their rules.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;tradePolicyId\&quot;: \&quot;2\&quot;,          \&quot;rules\&quot;: [              {                  \&quot;id\&quot;: 0,                  \&quot;context\&quot;: {                      \&quot;categories\&quot;: {},                      \&quot;brands\&quot;: {},                      \&quot;stockStatuses\&quot;: null,                      \&quot;internalCategories\&quot;: null,                      \&quot;markupRange\&quot;: null,                      \&quot;dateRange\&quot;: null                  },                  \&quot;percentualModifier\&quot;: 20              }          ]      },      {          \&quot;tradePolicyId\&quot;: \&quot;b2c\&quot;,          \&quot;rules\&quot;: [              {                  \&quot;id\&quot;: 0,                  \&quot;context\&quot;: {                      \&quot;categories\&quot;: {},                      \&quot;brands\&quot;: {                          \&quot;2000009\&quot;: \&quot;Whiskas\&quot;                      },                      \&quot;stockStatuses\&quot;: null,                      \&quot;internalCategories\&quot;: null,                      \&quot;markupRange\&quot;: null,                      \&quot;dateRange\&quot;: null                  },                  \&quot;percentualModifier\&quot;: 15              }          ]      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def getrulesforapricetable(request: web.Request, content_type, accept, price_table_id) -> web.Response:
    """Get rules for a price table

    This method will retrieve the rules from a specific Price Table.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;tradePolicyId\&quot;: \&quot;b2c\&quot;,      \&quot;rules\&quot;: [{          \&quot;id\&quot;: 0,          \&quot;context\&quot;: {              \&quot;categories\&quot;: {},              \&quot;brands\&quot;: {                  \&quot;2000009\&quot;: \&quot;Whiskas\&quot;              },              \&quot;stockStatuses\&quot;: null,              \&quot;internalCategories\&quot;: null,              \&quot;markupRange\&quot;: null,              \&quot;dateRange\&quot;: null          },          \&quot;percentualModifier\&quot;: 15      }]  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param price_table_id: Price Table Name.
    :type price_table_id: str

    """
    return web.Response(status=200)


async def listpricetables(request: web.Request, content_type, accept) -> web.Response:
    """List price tables

    This method will list all price tables.    ## Response body example    &#x60;&#x60;&#x60;json  [      \&quot;1\&quot;,      \&quot;2\&quot;,      \&quot;3\&quot;,      \&quot;b2c\&quot;,      \&quot;b2b\&quot;,      \&quot;gold\&quot;  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def pricing_pipeline_catalog_price_table_id_put(request: web.Request, content_type, accept, price_table_id, body=None) -> web.Response:
    """Update rules for a price table

    This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;rules\&quot;: [            {                 \&quot;id\&quot;: 1,                 \&quot;context\&quot;: {                      \&quot;categories\&quot;: {                           \&quot;Category ID\&quot;: \&quot;1\&quot;,                           \&quot;Category Name\&quot;: \&quot;Alimentação\&quot;                      },                      \&quot;brands\&quot;: {                           \&quot;Brand ID\&quot;: \&quot;2000002\&quot;,                           \&quot;Brand Name\&quot;: \&quot;Whiskas\&quot;                      },                      \&quot;markupRange\&quot;: {                           \&quot;from\&quot;: 0,                           \&quot;to\&quot;: 200                      },                      \&quot;dateRange\&quot;: {                           \&quot;from\&quot;: \&quot;2022-01-23T19:00:00.000Z\&quot;,                           \&quot;to\&quot;: \&quot;2023-10-26T00:00:00.000Z\&quot;                      }                 },                 \&quot;percentualModifier\&quot;: 0            }      ]  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param price_table_id: Price Table Name.
    :type price_table_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PricingPipelineCatalogPriceTableIdPutRequest.from_dict(body)
    return web.Response(status=200)
