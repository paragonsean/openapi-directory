# OptimadeApi.StructuresApi

All URIs are relative to *http://optimade.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSingleStructureStructuresEntryIdGet**](StructuresApi.md#getSingleStructureStructuresEntryIdGet) | **GET** /structures/{entry_id} | Get Single Structure
[**getStructuresStructuresGet**](StructuresApi.md#getStructuresStructuresGet) | **GET** /structures | Get Structures



## getSingleStructureStructuresEntryIdGet

> StructureResponseOne getSingleStructureStructuresEntryIdGet(entryId, opts)

Get Single Structure

### Example

```javascript
import OptimadeApi from 'optimade_api';

let apiInstance = new OptimadeApi.StructuresApi();
let entryId = "entryId_example"; // String | 
let opts = {
  'responseFormat': "'json'", // String | The output format requested (see section Response Format). Defaults to the format string 'json', which specifies the standard output format described in this specification. Example: `http://example.com/v1/structures?response_format=xml`
  'emailAddress': "''", // String | An email address of the user making the request. The email SHOULD be that of a person and not an automatic system. Example: `http://example.com/v1/structures?email_address=user@example.com`
  'responseFields': "''", // String | A comma-delimited set of fields to be provided in the output. If provided, these fields MUST be returned along with the REQUIRED fields. Other OPTIONAL fields MUST NOT be returned when this parameter is present. Example: `http://example.com/v1/structures?response_fields=last_modified,nsites`
  'include': "'references'", // String | A server MAY implement the JSON API concept of returning [compound documents](https://jsonapi.org/format/1.0/#document-compound-documents) by utilizing the `include` query parameter as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-includes).  All related resource objects MUST be returned as part of an array value for the top-level `included` field, see the section JSON Response Schema: Common Fields.  The value of `include` MUST be a comma-separated list of \"relationship paths\", as defined in the [JSON API](https://jsonapi.org/format/1.0/#fetching-includes). If relationship paths are not supported, or a server is unable to identify a relationship path a `400 Bad Request` response MUST be made.  The **default value** for `include` is `references`. This means `references` entries MUST always be included under the top-level field `included` as default, since a server assumes if `include` is not specified by a client in the request, it is still specified as `include=references`. Note, if a client explicitly specifies `include` and leaves out `references`, `references` resource objects MUST NOT be included under the top-level field `included`, as per the definition of `included`, see section JSON Response Schema: Common Fields.  > **Note**: A query with the parameter `include` set to the empty string means no related resource objects are to be returned under the top-level field `included`.
  'apiHint': "''" // String | If the client provides the parameter, the value SHOULD have the format `vMAJOR` or `vMAJOR.MINOR`, where MAJOR is a major version and MINOR is a minor version of the API. For example, if a client appends `api_hint=v1.0` to the query string, the hint provided is for major version 1 and minor version 0.
};
apiInstance.getSingleStructureStructuresEntryIdGet(entryId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entryId** | **String**|  | 
 **responseFormat** | **String**| The output format requested (see section Response Format). Defaults to the format string &#39;json&#39;, which specifies the standard output format described in this specification. Example: &#x60;http://example.com/v1/structures?response_format&#x3D;xml&#x60; | [optional] [default to &#39;json&#39;]
 **emailAddress** | **String**| An email address of the user making the request. The email SHOULD be that of a person and not an automatic system. Example: &#x60;http://example.com/v1/structures?email_address&#x3D;user@example.com&#x60; | [optional] [default to &#39;&#39;]
 **responseFields** | **String**| A comma-delimited set of fields to be provided in the output. If provided, these fields MUST be returned along with the REQUIRED fields. Other OPTIONAL fields MUST NOT be returned when this parameter is present. Example: &#x60;http://example.com/v1/structures?response_fields&#x3D;last_modified,nsites&#x60; | [optional] [default to &#39;&#39;]
 **include** | **String**| A server MAY implement the JSON API concept of returning [compound documents](https://jsonapi.org/format/1.0/#document-compound-documents) by utilizing the &#x60;include&#x60; query parameter as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-includes).  All related resource objects MUST be returned as part of an array value for the top-level &#x60;included&#x60; field, see the section JSON Response Schema: Common Fields.  The value of &#x60;include&#x60; MUST be a comma-separated list of \&quot;relationship paths\&quot;, as defined in the [JSON API](https://jsonapi.org/format/1.0/#fetching-includes). If relationship paths are not supported, or a server is unable to identify a relationship path a &#x60;400 Bad Request&#x60; response MUST be made.  The **default value** for &#x60;include&#x60; is &#x60;references&#x60;. This means &#x60;references&#x60; entries MUST always be included under the top-level field &#x60;included&#x60; as default, since a server assumes if &#x60;include&#x60; is not specified by a client in the request, it is still specified as &#x60;include&#x3D;references&#x60;. Note, if a client explicitly specifies &#x60;include&#x60; and leaves out &#x60;references&#x60;, &#x60;references&#x60; resource objects MUST NOT be included under the top-level field &#x60;included&#x60;, as per the definition of &#x60;included&#x60;, see section JSON Response Schema: Common Fields.  &gt; **Note**: A query with the parameter &#x60;include&#x60; set to the empty string means no related resource objects are to be returned under the top-level field &#x60;included&#x60;. | [optional] [default to &#39;references&#39;]
 **apiHint** | **String**| If the client provides the parameter, the value SHOULD have the format &#x60;vMAJOR&#x60; or &#x60;vMAJOR.MINOR&#x60;, where MAJOR is a major version and MINOR is a minor version of the API. For example, if a client appends &#x60;api_hint&#x3D;v1.0&#x60; to the query string, the hint provided is for major version 1 and minor version 0. | [optional] [default to &#39;&#39;]

### Return type

[**StructureResponseOne**](StructureResponseOne.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStructuresStructuresGet

> StructureResponseMany getStructuresStructuresGet(opts)

Get Structures

### Example

```javascript
import OptimadeApi from 'optimade_api';

let apiInstance = new OptimadeApi.StructuresApi();
let opts = {
  'filter': "''", // String | A filter string, in the format described in section API Filtering Format Specification of the specification.
  'responseFormat': "'json'", // String | The output format requested (see section Response Format). Defaults to the format string 'json', which specifies the standard output format described in this specification. Example: `http://example.com/v1/structures?response_format=xml`
  'emailAddress': "''", // String | An email address of the user making the request. The email SHOULD be that of a person and not an automatic system. Example: `http://example.com/v1/structures?email_address=user@example.com`
  'responseFields': "''", // String | A comma-delimited set of fields to be provided in the output. If provided, these fields MUST be returned along with the REQUIRED fields. Other OPTIONAL fields MUST NOT be returned when this parameter is present. Example: `http://example.com/v1/structures?response_fields=last_modified,nsites`
  'sort': "''", // String | If supporting sortable queries, an implementation MUST use the `sort` query parameter with format as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-sorting).  An implementation MAY support multiple sort fields for a single query. If it does, it again MUST conform to the JSON API 1.0 specification.  If an implementation supports sorting for an entry listing endpoint, then the `/info/<entries>` endpoint MUST include, for each field name `<fieldname>` in its `data.properties.<fieldname>` response value that can be used for sorting, the key `sortable` with value `true`. If a field name under an entry listing endpoint supporting sorting cannot be used for sorting, the server MUST either leave out the `sortable` key or set it equal to `false` for the specific field name. The set of field names, with `sortable` equal to `true` are allowed to be used in the \"sort fields\" list according to its definition in the JSON API 1.0 specification. The field `sortable` is in addition to each property description and other OPTIONAL fields. An example is shown in the section Entry Listing Info Endpoints.
  'pageLimit': 20, // Number | Sets a numerical limit on the number of entries returned. See [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-pagination). The API implementation MUST return no more than the number specified. It MAY return fewer. The database MAY have a maximum limit and not accept larger numbers (in which case an error code -- 403 Forbidden -- MUST be returned). The default limit value is up to the API implementation to decide. Example: `http://example.com/optimade/v1/structures?page_limit=100`
  'pageOffset': 0, // Number | RECOMMENDED for use with _offset-based_ pagination: using `page_offset` and `page_limit` is RECOMMENDED. Example: Skip 50 structures and fetch up to 100: `/structures?page_offset=50&page_limit=100`.
  'pageNumber': 0, // Number | RECOMMENDED for use with _page-based_ pagination: using `page_number` and `page_limit` is RECOMMENDED. It is RECOMMENDED that the first page has number 1, i.e., that `page_number` is 1-based. Example: Fetch page 2 of up to 50 structures per page: `/structures?page_number=2&page_limit=50`.
  'pageCursor': 0, // Number | RECOMMENDED for use with _cursor-based_ pagination: using `page_cursor` and `page_limit` is RECOMMENDED.
  'pageAbove': 0, // Number | RECOMMENDED for use with _value-based_ pagination: using `page_above`/`page_below` and `page_limit` is RECOMMENDED. Example: Fetch up to 100 structures above sort-field value 4000 (in this example, server chooses to fetch results sorted by increasing `id`, so `page_above` value refers to an `id` value): `/structures?page_above=4000&page_limit=100`.
  'pageBelow': 0, // Number | RECOMMENDED for use with _value-based_ pagination: using `page_above`/`page_below` and `page_limit` is RECOMMENDED.
  'include': "'references'", // String | A server MAY implement the JSON API concept of returning [compound documents](https://jsonapi.org/format/1.0/#document-compound-documents) by utilizing the `include` query parameter as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-includes).  All related resource objects MUST be returned as part of an array value for the top-level `included` field, see the section JSON Response Schema: Common Fields.  The value of `include` MUST be a comma-separated list of \"relationship paths\", as defined in the [JSON API](https://jsonapi.org/format/1.0/#fetching-includes). If relationship paths are not supported, or a server is unable to identify a relationship path a `400 Bad Request` response MUST be made.  The **default value** for `include` is `references`. This means `references` entries MUST always be included under the top-level field `included` as default, since a server assumes if `include` is not specified by a client in the request, it is still specified as `include=references`. Note, if a client explicitly specifies `include` and leaves out `references`, `references` resource objects MUST NOT be included under the top-level field `included`, as per the definition of `included`, see section JSON Response Schema: Common Fields.  > **Note**: A query with the parameter `include` set to the empty string means no related resource objects are to be returned under the top-level field `included`.
  'apiHint': "''" // String | If the client provides the parameter, the value SHOULD have the format `vMAJOR` or `vMAJOR.MINOR`, where MAJOR is a major version and MINOR is a minor version of the API. For example, if a client appends `api_hint=v1.0` to the query string, the hint provided is for major version 1 and minor version 0.
};
apiInstance.getStructuresStructuresGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **String**| A filter string, in the format described in section API Filtering Format Specification of the specification. | [optional] [default to &#39;&#39;]
 **responseFormat** | **String**| The output format requested (see section Response Format). Defaults to the format string &#39;json&#39;, which specifies the standard output format described in this specification. Example: &#x60;http://example.com/v1/structures?response_format&#x3D;xml&#x60; | [optional] [default to &#39;json&#39;]
 **emailAddress** | **String**| An email address of the user making the request. The email SHOULD be that of a person and not an automatic system. Example: &#x60;http://example.com/v1/structures?email_address&#x3D;user@example.com&#x60; | [optional] [default to &#39;&#39;]
 **responseFields** | **String**| A comma-delimited set of fields to be provided in the output. If provided, these fields MUST be returned along with the REQUIRED fields. Other OPTIONAL fields MUST NOT be returned when this parameter is present. Example: &#x60;http://example.com/v1/structures?response_fields&#x3D;last_modified,nsites&#x60; | [optional] [default to &#39;&#39;]
 **sort** | **String**| If supporting sortable queries, an implementation MUST use the &#x60;sort&#x60; query parameter with format as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-sorting).  An implementation MAY support multiple sort fields for a single query. If it does, it again MUST conform to the JSON API 1.0 specification.  If an implementation supports sorting for an entry listing endpoint, then the &#x60;/info/&lt;entries&gt;&#x60; endpoint MUST include, for each field name &#x60;&lt;fieldname&gt;&#x60; in its &#x60;data.properties.&lt;fieldname&gt;&#x60; response value that can be used for sorting, the key &#x60;sortable&#x60; with value &#x60;true&#x60;. If a field name under an entry listing endpoint supporting sorting cannot be used for sorting, the server MUST either leave out the &#x60;sortable&#x60; key or set it equal to &#x60;false&#x60; for the specific field name. The set of field names, with &#x60;sortable&#x60; equal to &#x60;true&#x60; are allowed to be used in the \&quot;sort fields\&quot; list according to its definition in the JSON API 1.0 specification. The field &#x60;sortable&#x60; is in addition to each property description and other OPTIONAL fields. An example is shown in the section Entry Listing Info Endpoints. | [optional] [default to &#39;&#39;]
 **pageLimit** | **Number**| Sets a numerical limit on the number of entries returned. See [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-pagination). The API implementation MUST return no more than the number specified. It MAY return fewer. The database MAY have a maximum limit and not accept larger numbers (in which case an error code -- 403 Forbidden -- MUST be returned). The default limit value is up to the API implementation to decide. Example: &#x60;http://example.com/optimade/v1/structures?page_limit&#x3D;100&#x60; | [optional] [default to 20]
 **pageOffset** | **Number**| RECOMMENDED for use with _offset-based_ pagination: using &#x60;page_offset&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. Example: Skip 50 structures and fetch up to 100: &#x60;/structures?page_offset&#x3D;50&amp;page_limit&#x3D;100&#x60;. | [optional] [default to 0]
 **pageNumber** | **Number**| RECOMMENDED for use with _page-based_ pagination: using &#x60;page_number&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. It is RECOMMENDED that the first page has number 1, i.e., that &#x60;page_number&#x60; is 1-based. Example: Fetch page 2 of up to 50 structures per page: &#x60;/structures?page_number&#x3D;2&amp;page_limit&#x3D;50&#x60;. | [optional] [default to 0]
 **pageCursor** | **Number**| RECOMMENDED for use with _cursor-based_ pagination: using &#x60;page_cursor&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. | [optional] [default to 0]
 **pageAbove** | **Number**| RECOMMENDED for use with _value-based_ pagination: using &#x60;page_above&#x60;/&#x60;page_below&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. Example: Fetch up to 100 structures above sort-field value 4000 (in this example, server chooses to fetch results sorted by increasing &#x60;id&#x60;, so &#x60;page_above&#x60; value refers to an &#x60;id&#x60; value): &#x60;/structures?page_above&#x3D;4000&amp;page_limit&#x3D;100&#x60;. | [optional] [default to 0]
 **pageBelow** | **Number**| RECOMMENDED for use with _value-based_ pagination: using &#x60;page_above&#x60;/&#x60;page_below&#x60; and &#x60;page_limit&#x60; is RECOMMENDED. | [optional] [default to 0]
 **include** | **String**| A server MAY implement the JSON API concept of returning [compound documents](https://jsonapi.org/format/1.0/#document-compound-documents) by utilizing the &#x60;include&#x60; query parameter as specified by [JSON API 1.0](https://jsonapi.org/format/1.0/#fetching-includes).  All related resource objects MUST be returned as part of an array value for the top-level &#x60;included&#x60; field, see the section JSON Response Schema: Common Fields.  The value of &#x60;include&#x60; MUST be a comma-separated list of \&quot;relationship paths\&quot;, as defined in the [JSON API](https://jsonapi.org/format/1.0/#fetching-includes). If relationship paths are not supported, or a server is unable to identify a relationship path a &#x60;400 Bad Request&#x60; response MUST be made.  The **default value** for &#x60;include&#x60; is &#x60;references&#x60;. This means &#x60;references&#x60; entries MUST always be included under the top-level field &#x60;included&#x60; as default, since a server assumes if &#x60;include&#x60; is not specified by a client in the request, it is still specified as &#x60;include&#x3D;references&#x60;. Note, if a client explicitly specifies &#x60;include&#x60; and leaves out &#x60;references&#x60;, &#x60;references&#x60; resource objects MUST NOT be included under the top-level field &#x60;included&#x60;, as per the definition of &#x60;included&#x60;, see section JSON Response Schema: Common Fields.  &gt; **Note**: A query with the parameter &#x60;include&#x60; set to the empty string means no related resource objects are to be returned under the top-level field &#x60;included&#x60;. | [optional] [default to &#39;references&#39;]
 **apiHint** | **String**| If the client provides the parameter, the value SHOULD have the format &#x60;vMAJOR&#x60; or &#x60;vMAJOR.MINOR&#x60;, where MAJOR is a major version and MINOR is a minor version of the API. For example, if a client appends &#x60;api_hint&#x3D;v1.0&#x60; to the query string, the hint provided is for major version 1 and minor version 0. | [optional] [default to &#39;&#39;]

### Return type

[**StructureResponseMany**](StructureResponseMany.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

