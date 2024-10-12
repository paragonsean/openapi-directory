from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def searchdocuments(request: web.Request, data_entity_name, content_type, accept, rest_range, fields=None, where=None, _schema=None, keyword=None, sort=None) -> web.Response:
    """Search documents

    Retrieves documents&#39; information, while choosing which fields will be returned and filtering documents by specific fields.    &gt; The response header &#x60;REST-Content-Range&#x60; indicates the total amount of results for that specific search. For example, it may return &#x60;resources 0-100/136108&#x60;, which indicates it has returned results from 0 to 100 of a total 136108.    Below you can see some query examples and learn more about each query parameter.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;503&#x60;.    ## Query examples    ### Simple filter    &#x60;&#x60;&#x60;  /dataentities/Client/search?email&#x3D;my@email.com  &#x60;&#x60;&#x60;    ### Complex filter    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;(firstName&#x3D;Jon OR lastName&#x3D;Smith) OR (createdIn between 2001-01-01 AND 2016-01-01)  &#x60;&#x60;&#x60;    ### Date Range    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;createdIn between 2001-01-01 AND 2016-01-01  &#x60;&#x60;&#x60;    ### Range numeric fields    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;age between 18 AND 25  &#x60;&#x60;&#x60;    ### Partial filter    &#x60;&#x60;&#x60;  /dataentities/Client/search?firstName&#x3D;*Maria*  &#x60;&#x60;&#x60;    ### Filter for null values    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;firstName is null  &#x60;&#x60;&#x60;    ### Filter for non-null values    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;firstName is not null  &#x60;&#x60;&#x60;    ### Filter for difference  &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;firstName&lt;&gt;maria  &#x60;&#x60;&#x60;    ### Filter greater than or less than  &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;number&gt;5  /dataentities/Client/search?_where&#x3D;date&lt;2001-01-01  &#x60;&#x60;&#x60;

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param rest_range: Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query.
    :type rest_range: str
    :param fields: Fields that should be returned by document. Separate fields&#39; names with commas. For example &#x60;_fields&#x3D;email,firstName,document&#x60;. You can also use &#x60;_all&#x60; to fetch all fields.
    :type fields: str
    :param where: Filter specification.
    :type where: str
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str
    :param keyword: String to search. Use quotes for a partial query. For example, &#x60;_keyword&#x3D;Maria&#x60; or &#x60;_keyword&#x3D;\&quot;Maria\&quot;&#x60;.
    :type keyword: str
    :param sort: Sets sorting mode in two parts. The first part is the name of the field you want to sort by. In the second part, use &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending.
    :type sort: str

    """
    return web.Response(status=200)
