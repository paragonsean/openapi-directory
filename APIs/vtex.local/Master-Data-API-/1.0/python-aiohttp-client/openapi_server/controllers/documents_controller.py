from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_response import DocumentResponse
from openapi_server.models.using_fields_all import UsingFieldsAll
from openapi_server import util


async def createnewdocument(request: web.Request, content_type, accept, data_entity_name, body, _schema=None) -> web.Response:
    """Create new document

    This request allows you to create a new document corresponding to a given data entity. For example, you can create a new customer profile or address.    &gt; You can use this request to create documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to create.    ## Example use cases    ### Client profile    In order to create a new customer profile, choose the &#x60;CL&#x60; data entity and send a request similar to this:    POST  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;email\&quot;: \&quot;clark.kent@examplemail.com\&quot;,      \&quot;firstName\&quot;: \&quot;Clark\&quot;,      \&quot;lastName\&quot;: \&quot;Kent\&quot;,      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;documentType\&quot;: \&quot;CPF\&quot;,      \&quot;document\&quot;: \&quot;12345678900\&quot;      \&quot;isCorporate\&quot;: false,      \&quot;isNewsletterOptIn\&quot;: false,      \&quot;localeDefault\&quot;: \&quot;en-US\&quot;   }  &#x60;&#x60;&#x60;    ### Client address    For a new address, the data entity is &#x60;AD&#x60; and the request would look like this:    POST  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;addressName\&quot;: \&quot;My House\&quot;,      \&quot;addressType\&quot;: \&quot;residential\&quot;,      \&quot;city\&quot;: \&quot;Metropolis\&quot;,      \&quot;complement\&quot;: \&quot;\&quot;,      \&quot;country\&quot;: \&quot;USA\&quot;,      \&quot;postalCode\&quot;: \&quot;11375\&quot;,      \&quot;receiverName\&quot;: \&quot;Clark Kent\&quot;,      \&quot;reference\&quot;: null,      \&quot;state\&quot;: \&quot;MP\&quot;,      \&quot;street\&quot;: \&quot;Baker Street\&quot;,      \&quot;neighborhood\&quot;: \&quot;Upper east side\&quot;,      \&quot;number\&quot;: \&quot;21\&quot;,      \&quot;userId\&quot;: \&quot;7e03m794-a33a-11e9-84rt6-0adfa64s5a8e\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param body: 
    :type body: Dict[str, str]
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str

    """
    return web.Response(status=200)


async def createorupdatepartialdocument(request: web.Request, data_entity_name, content_type, accept, body, _schema=None) -> web.Response:
    """Create partial document

    This request allows you to partially update a document corresponding to a given data entity.    &gt; You can use this request to create documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to create a customer profile&#39;s &#x60;phone&#x60; and &#x60;isNewsletterOptIn&#x60; fields, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;isNewsletterOptIn\&quot;: false   }  &#x60;&#x60;&#x60;    ### Client address    In order to update the &#x60;receiverName&#x60; of an existing address, the data entity is &#x60;AD&#x60; and the request would look like this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;receiverName\&quot;: \&quot;Lois Lane\&quot;  }  &#x60;&#x60;&#x60;

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: JSON with the fields to be updated.
    :type body: Dict[str, str]
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str

    """
    return web.Response(status=200)


async def deletedocument(request: web.Request, data_entity_name, content_type, accept, id) -> web.Response:
    """Delete document

    It allows to delete a document.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str

    """
    return web.Response(status=200)


async def getdocument(request: web.Request, data_entity_name, content_type, accept, id) -> web.Response:
    """Get document

    Gets document by ID.    &gt; Assign the &#x60;_fields&#x60; parameter in the query string to retrieve the desired fields. If you want to return all the fields use &#x60;_fields&#x3D;_all&#x60;.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str

    """
    return web.Response(status=200)


async def updateentiredocument(request: web.Request, data_entity_name, accept, id, body, where=None, _schema=None) -> web.Response:
    """Update entire document

    Update an existing document corresponding to a given data entity. For example, you can update a customer profile or address.    &gt; You can use this request to update documents in any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to update an existing customer profile, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PUT  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;email\&quot;: \&quot;clark.kent@examplemail.com\&quot;,      \&quot;firstName\&quot;: \&quot;Clark\&quot;,      \&quot;lastName\&quot;: \&quot;Kent\&quot;,      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;documentType\&quot;: \&quot;CPF\&quot;,      \&quot;document\&quot;: \&quot;12345678900\&quot;      \&quot;isCorporate\&quot;: false,      \&quot;isNewsletterOptIn\&quot;: false,      \&quot;localeDefault\&quot;: \&quot;en-US\&quot;   }  &#x60;&#x60;&#x60;    ### Client address    To update an address, the data entity is &#x60;AD&#x60; and the request would look like this:    PUT  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;addressName\&quot;: \&quot;My House\&quot;,      \&quot;addressType\&quot;: \&quot;residential\&quot;,      \&quot;city\&quot;: \&quot;Metropolis\&quot;,      \&quot;complement\&quot;: \&quot;\&quot;,      \&quot;country\&quot;: \&quot;USA\&quot;,      \&quot;postalCode\&quot;: \&quot;11375\&quot;,      \&quot;receiverName\&quot;: \&quot;Clark Kent\&quot;,      \&quot;reference\&quot;: null,      \&quot;state\&quot;: \&quot;MP\&quot;,      \&quot;street\&quot;: \&quot;Baker Street\&quot;,      \&quot;neighborhood\&quot;: \&quot;Upper east side\&quot;,      \&quot;number\&quot;: \&quot;21\&quot;,      \&quot;userId\&quot;: \&quot;7e03m794-a33a-11e9-84rt6-0adfa64s5a8e\&quot;  }  &#x60;&#x60;&#x60;

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str
    :param body: 
    :type body: Dict[str, str]
    :param where: Filter specification.
    :type where: str
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str

    """
    return web.Response(status=200)


async def updatepartialdocument(request: web.Request, data_entity_name, accept, id, body, where=None, _schema=None) -> web.Response:
    """Update partial document

    This request allows you to partially update a document corresponding to a given data entity. For example, you can update some fields of a customer profile or address.    &gt; You can use this request to update documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to update a customer profile&#39;s &#x60;phone&#x60; and &#x60;isNewsletterOptIn&#x60; fields, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;isNewsletterOptIn\&quot;: false   }  &#x60;&#x60;&#x60;    ### Client address    In order to update the &#x60;receiverName&#x60; of an existing address, the data entity is &#x60;AD&#x60; and the request would look like this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;receiverName\&quot;: \&quot;Lois Lane\&quot;  }  &#x60;&#x60;&#x60;

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str
    :param body: 
    :type body: Dict[str, str]
    :param where: Filter specification.
    :type where: str
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str

    """
    return web.Response(status=200)
