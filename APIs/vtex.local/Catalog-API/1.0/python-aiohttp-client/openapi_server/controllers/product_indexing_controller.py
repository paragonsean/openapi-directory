from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def indexed_info(request: web.Request, content_type, accept, product_id) -> web.Response:
    """Get Product Indexed Information

    Retrieve details of a Product&#39;s Indexed Information in XML format.   ## Response body example    &#x60;&#x60;&#x60;xml  \&quot;  &lt;?xml version&#x3D;\\\&quot;1.0\\\&quot; encoding&#x3D;\\\&quot;UTF-8\\\&quot;?&gt;\\n  &lt;response&gt;\\n      &lt;lst name&#x3D;\\\&quot;responseHeader\\\&quot;&gt;          &lt;bool name&#x3D;\\\&quot;zkConnected\\\&quot;&gt;true&lt;/bool&gt;          &lt;int name&#x3D;\\\&quot;status\\\&quot;&gt;0&lt;/int&gt;          &lt;int name&#x3D;\\\&quot;QTime\\\&quot;&gt;2&lt;/int&gt;          &lt;lst name&#x3D;\\\&quot;params\\\&quot;&gt;              &lt;str name&#x3D;\\\&quot;fl\\\&quot;&gt;*&lt;/str&gt;              &lt;arr name&#x3D;\\\&quot;fq\\\&quot;&gt;                  &lt;str&gt;instanceId:394dbdc8-b1f4-4dea-adfa-1ec104f3bfe1&lt;/str&gt;                  &lt;str&gt;productId:1&lt;/str&gt;              &lt;/arr&gt;          &lt;/lst&gt;      &lt;/lst&gt;      &lt;result name&#x3D;\\\&quot;response\\\&quot; numFound&#x3D;\\\&quot;0\\\&quot; start&#x3D;\\\&quot;0\\\&quot; maxScore&#x3D;\\\&quot;0.0\\\&quot;&gt;&lt;/result&gt;      &lt;lst name&#x3D;\\\&quot;facet_counts\\\&quot;&gt;          &lt;lst name&#x3D;\\\&quot;facet_queries\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_fields\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_ranges\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_intervals\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_heatmaps\\\&quot;/&gt;&lt;/lst&gt;\\n  &lt;/response&gt;\\n\&quot;  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: str

    """
    return web.Response(status=200)
