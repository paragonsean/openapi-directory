from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.structure_response_many import StructureResponseMany
from openapi_server.models.structure_response_one import StructureResponseOne
from openapi_server import util


async def get_single_structure_structures_entry_id_get(request: web.Request, entry_id, response_format=None, email_address=None, response_fields=None, include=None, api_hint=None) -> web.Response:
    """Get Single Structure

    

    :param entry_id: 
    :type entry_id: str
    :param response_format: The output format requested (see section Response Format). Defaults to the format string &#39;json&#39;, which specifies the standard output format described in this specification. Example: &#x60;http://example.com/v1/structures?response_format&#x3D;xml&#x60;
    :type response_format: str
    :param email_address: An email address of the user making the request. The email SHOULD be that of a person and not an automatic system. Example: &#x60;http://example.com/v1/structures?email_address&#x3D;user@example.com&#x60;
    :type email_address: str
    :param response_fields: A comma-delimited set of fields to be provided in the output. If provided, these fields MUST be returned along with the REQUIRED fields. Other OPTIONAL fields MUST NOT be returned when this parameter is present. Example: &#x60;http://example.com/v1/structures?response_fields&#x3D;last_modified,nsites&#x60;
    :type response_fields: str
    :param include: A server MAY implement the JSON API concept of returning [compound documents](https://jsonapi.org/format/1.0/#document-compound-documents) by utilizing the &#x60;include&#x60; query parameter as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-includes).  All related resource objects MUST be returned as part of an array value for the top-level &#x60;included&#x60; field, see the section JSON Response Schema: Common Fields.  The value of &#x60;include&#x60; MUST be a comma-separated list of \&quot;relationship paths\&quot;, as defined in the [JSON API](https://jsonapi.org/format/1.0/#fetching-includes). If relationship paths are not supported, or a server is unable to identify a relationship path a &#x60;400 Bad Request&#x60; response MUST be made.  The **default value** for &#x60;include&#x60; is &#x60;references&#x60;. This means &#x60;references&#x60; entries MUST always be included under the top-level field &#x60;included&#x60; as default, since a server assumes if &#x60;include&#x60; is not specified by a client in the request, it is still specified as &#x60;include&#x3D;references&#x60;. Note, if a client explicitly specifies &#x60;include&#x60; and leaves out &#x60;references&#x60;, &#x60;references&#x60; resource objects MUST NOT be included under the top-level field &#x60;included&#x60;, as per the definition of &#x60;included&#x60;, see section JSON Response Schema: Common Fields.  &gt; **Note**: A query with the parameter &#x60;include&#x60; set to the empty string means no related resource objects are to be returned under the top-level field &#x60;included&#x60;.
    :type include: str
    :param api_hint: If the client provides the parameter, the value SHOULD have the format &#x60;vMAJOR&#x60; or &#x60;vMAJOR.MINOR&#x60;, where MAJOR is a major version and MINOR is a minor version of the API. For example, if a client appends &#x60;api_hint&#x3D;v1.0&#x60; to the query string, the hint provided is for major version 1 and minor version 0.
    :type api_hint: str

    """
    return web.Response(status=200)


async def get_structures_structures_get(request: web.Request, filter=None, response_format=None, email_address=None, response_fields=None, sort=None, page_limit=None, page_offset=None, page_number=None, page_cursor=None, page_above=None, page_below=None, include=None, api_hint=None) -> web.Response:
    """Get Structures

    

    :param filter: A filter string, in the format described in section API Filtering Format Specification of the specification.
    :type filter: str
    :param response_format: The output format requested (see section Response Format). Defaults to the format string &#39;json&#39;, which specifies the standard output format described in this specification. Example: &#x60;http://example.com/v1/structures?response_format&#x3D;xml&#x60;
    :type response_format: str
    :param email_address: An email address of the user making the request. The email SHOULD be that of a person and not an automatic system. Example: &#x60;http://example.com/v1/structures?email_address&#x3D;user@example.com&#x60;
    :type email_address: str
    :param response_fields: A comma-delimited set of fields to be provided in the output. If provided, these fields MUST be returned along with the REQUIRED fields. Other OPTIONAL fields MUST NOT be returned when this parameter is present. Example: &#x60;http://example.com/v1/structures?response_fields&#x3D;last_modified,nsites&#x60;
    :type response_fields: str
    :param sort: If supporting sortable queries, an implementation MUST use the &#x60;sort&#x60; query parameter with format as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-sorting).  An implementation MAY support multiple sort fields for a single query. If it does, it again MUST conform to the JSON API 1.0 specification.  If an implementation supports sorting for an entry listing endpoint, then the &#x60;/info/&lt;entries&gt;&#x60; endpoint MUST include, for each field name &#x60;&lt;fieldname&gt;&#x60; in its &#x60;data.properties.&lt;fieldname&gt;&#x60; response value that can be used for sorting, the key &#x60;sortable&#x60; with value &#x60;true&#x60;. If a field name under an entry listing endpoint supporting sorting cannot be used for sorting, the server MUST either leave out the &#x60;sortable&#x60; key or set it equal to &#x60;false&#x60; for the specific field name. The set of field names, with &#x60;sortable&#x60; equal to &#x60;true&#x60; are allowed to be used in the \&quot;sort fields\&quot; list according to its definition in the JSON API 1.0 specification. The field &#x60;sortable&#x60; is in addition to each property description and other OPTIONAL fields. An example is shown in the section Entry Listing Info Endpoints.
    :type sort: str
    :param page_limit: Sets a numerical limit on the number of entries returned. See [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-pagination). The API implementation MUST return no more than the number specified. It MAY return fewer. The database MAY have a maximum limit and not accept larger numbers (in which case an error code -- 403 Forbidden -- MUST be returned). The default limit value is up to the API implementation to decide. Example: &#x60;http://example.com/optimade/v1/structures?page_limit&#x3D;100&#x60;
    :type page_limit: int
    :param page_offset: RECOMMENDED for use with _offset-based_ pagination: using &#x60;page_offset&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. Example: Skip 50 structures and fetch up to 100: &#x60;/structures?page_offset&#x3D;50&amp;page_limit&#x3D;100&#x60;.
    :type page_offset: int
    :param page_number: RECOMMENDED for use with _page-based_ pagination: using &#x60;page_number&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. It is RECOMMENDED that the first page has number 1, i.e., that &#x60;page_number&#x60; is 1-based. Example: Fetch page 2 of up to 50 structures per page: &#x60;/structures?page_number&#x3D;2&amp;page_limit&#x3D;50&#x60;.
    :type page_number: int
    :param page_cursor: RECOMMENDED for use with _cursor-based_ pagination: using &#x60;page_cursor&#x60; and &#x60;page_limit&#x60; is RECOMMENDED.
    :type page_cursor: int
    :param page_above: RECOMMENDED for use with _value-based_ pagination: using &#x60;page_above&#x60;/&#x60;page_below&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. Example: Fetch up to 100 structures above sort-field value 4000 (in this example, server chooses to fetch results sorted by increasing &#x60;id&#x60;, so &#x60;page_above&#x60; value refers to an &#x60;id&#x60; value): &#x60;/structures?page_above&#x3D;4000&amp;page_limit&#x3D;100&#x60;.
    :type page_above: int
    :param page_below: RECOMMENDED for use with _value-based_ pagination: using &#x60;page_above&#x60;/&#x60;page_below&#x60; and &#x60;page_limit&#x60; is RECOMMENDED.
    :type page_below: int
    :param include: A server MAY implement the JSON API concept of returning [compound documents](https://jsonapi.org/format/1.0/#document-compound-documents) by utilizing the &#x60;include&#x60; query parameter as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-includes).  All related resource objects MUST be returned as part of an array value for the top-level &#x60;included&#x60; field, see the section JSON Response Schema: Common Fields.  The value of &#x60;include&#x60; MUST be a comma-separated list of \&quot;relationship paths\&quot;, as defined in the [JSON API](https://jsonapi.org/format/1.0/#fetching-includes). If relationship paths are not supported, or a server is unable to identify a relationship path a &#x60;400 Bad Request&#x60; response MUST be made.  The **default value** for &#x60;include&#x60; is &#x60;references&#x60;. This means &#x60;references&#x60; entries MUST always be included under the top-level field &#x60;included&#x60; as default, since a server assumes if &#x60;include&#x60; is not specified by a client in the request, it is still specified as &#x60;include&#x3D;references&#x60;. Note, if a client explicitly specifies &#x60;include&#x60; and leaves out &#x60;references&#x60;, &#x60;references&#x60; resource objects MUST NOT be included under the top-level field &#x60;included&#x60;, as per the definition of &#x60;included&#x60;, see section JSON Response Schema: Common Fields.  &gt; **Note**: A query with the parameter &#x60;include&#x60; set to the empty string means no related resource objects are to be returned under the top-level field &#x60;included&#x60;.
    :type include: str
    :param api_hint: If the client provides the parameter, the value SHOULD have the format &#x60;vMAJOR&#x60; or &#x60;vMAJOR.MINOR&#x60;, where MAJOR is a major version and MINOR is a minor version of the API. For example, if a client appends &#x60;api_hint&#x3D;v1.0&#x60; to the query string, the hint provided is for major version 1 and minor version 0.
    :type api_hint: str

    """
    return web.Response(status=200)
