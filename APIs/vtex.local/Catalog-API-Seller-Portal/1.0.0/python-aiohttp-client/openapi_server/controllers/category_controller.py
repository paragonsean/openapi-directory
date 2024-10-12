from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_category_request import CreateCategoryRequest
from openapi_server.models.get_category_tree200_response import GetCategoryTree200Response
from openapi_server.models.getbyid200_response import Getbyid200Response
from openapi_server.models.roots_inner import RootsInner
from openapi_server.models.update_category_tree_request import UpdateCategoryTreeRequest
from openapi_server import util


async def create_category(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Category

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Creates a new category.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;parentId\&quot;: \&quot;567\&quot;,    \&quot;Name\&quot;: \&quot;Beauty\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;value\&quot;: {      \&quot;id\&quot;: \&quot;1\&quot;,      \&quot;name\&quot;: \&quot;Beauty\&quot;,      \&quot;isActive\&quot;: false    },    \&quot;children\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        }      }    ]  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def get_category_tree(request: web.Request, content_type, accept, depth=None) -> web.Response:
    """Get Category Tree

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about the category tree from the store.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;roots\&quot;: [          {              \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;2\&quot;,                  \&quot;name\&quot;: \&quot;Departamento Artesanato\&quot;,                  \&quot;isActive\&quot;: true              },              \&quot;children\&quot;: [                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;3\&quot;,                          \&quot;name\&quot;: \&quot;Artesanato de Barro\&quot;,                          \&quot;isActive\&quot;: false                      },                      \&quot;children\&quot;: [                          {                              \&quot;value\&quot;: {                                  \&quot;id\&quot;: \&quot;4\&quot;,                                  \&quot;name\&quot;: \&quot;Artesanato de Barro Vermelho\&quot;,                                  \&quot;isActive\&quot;: false                              },                              \&quot;children\&quot;: []                          }                      ]                  }              ]          },          {              \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;5\&quot;,                  \&quot;name\&quot;: \&quot;Perfumes\&quot;,                  \&quot;isActive\&quot;: false              },              \&quot;children\&quot;: [                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;6\&quot;,                          \&quot;name\&quot;: \&quot;Perfume Feminino\&quot;,                          \&quot;isActive\&quot;: false                      },                      \&quot;children\&quot;: []                  },                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;7\&quot;,                          \&quot;name\&quot;: \&quot;Perfume Masculino\&quot;,                          \&quot;isActive\&quot;: false,                          \&quot;displayOnMenu\&quot;: false,                          \&quot;score\&quot;: 0,                          \&quot;filterByBrand\&quot;: false,                          \&quot;isClickable\&quot;: false                      },                      \&quot;children\&quot;: []                  }              ]          }      ],      \&quot;createdAt\&quot;: \&quot;2021-08-16T20:57:13.070813Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-07-07T14:24:56.416337Z\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param depth: Category tree level.
    :type depth: int

    """
    return web.Response(status=200)


async def getbyid(request: web.Request, content_type, accept, category_id) -> web.Response:
    """Get Category by ID

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a category by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;value\&quot;: {      \&quot;id\&quot;: \&quot;1\&quot;,      \&quot;name\&quot;: \&quot;sandboxintegracao\&quot;,      \&quot;isActive\&quot;: false    },    \&quot;children\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        }      }    ]  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param category_id: Category unique identifier number.
    :type category_id: str

    """
    return web.Response(status=200)


async def update_category_tree(request: web.Request, content_type, accept, body) -> web.Response:
    """Update Category Tree

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates the existing categories in the category tree.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;roots\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Departamento Artesanato\&quot;,          \&quot;isActive\&quot;: true        },        \&quot;children\&quot;: [          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;3\&quot;,              \&quot;name\&quot;: \&quot;Artesanato de Barro\&quot;,              \&quot;isActive\&quot;: false            },            \&quot;children\&quot;: [              {                \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;4\&quot;,                  \&quot;name\&quot;: \&quot;Artesanato de Barro Vermelho\&quot;,                  \&quot;isActive\&quot;: false                },                \&quot;children\&quot;: []              }            ]          }        ]      },      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;5\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        },        \&quot;children\&quot;: [          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;6\&quot;,              \&quot;name\&quot;: \&quot;Perfume Feminino\&quot;,              \&quot;isActive\&quot;: false            },            \&quot;children\&quot;: []          },          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;7\&quot;,              \&quot;name\&quot;: \&quot;Perfume Masculino\&quot;,              \&quot;isActive\&quot;: false,              \&quot;displayOnMenu\&quot;: false,              \&quot;score\&quot;: 0,              \&quot;filterByBrand\&quot;: false,              \&quot;isClickable\&quot;: false            },            \&quot;children\&quot;: []          }        ]      }    ]  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: OK
    :type body: dict | bytes

    """
    body = UpdateCategoryTreeRequest.from_dict(body)
    return web.Response(status=200)
