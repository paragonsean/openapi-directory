from typing import List, Dict
from aiohttp import web

from openapi_server.models.supplier_request import SupplierRequest
from openapi_server.models.supplier_response import SupplierResponse
from openapi_server import util


async def api_catalog_pvt_supplier_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Supplier

    Creates a new Supplier.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SupplierRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_supplier_supplier_id_delete(request: web.Request, content_type, accept, supplier_id) -> web.Response:
    """Delete Supplier

    Deletes an existing Supplier.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param supplier_id: Supplier&#39;s unique numerical identifier.
    :type supplier_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_supplier_supplier_id_put(request: web.Request, content_type, accept, supplier_id, body=None) -> web.Response:
    """Update Supplier

    Updates general information of an existing Supplier.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param supplier_id: Supplier&#39;s unique numerical identifier.
    :type supplier_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SupplierRequest.from_dict(body)
    return web.Response(status=200)
