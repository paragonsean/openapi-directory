# MasterDataApiV2.ScrollApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scrolldocuments**](ScrollApi.md#scrolldocuments) | **GET** /api/dataentities/{dataEntityName}/scroll | Scroll documents



## scrolldocuments

> scrolldocuments(dataEntityName, contentType, accept, rESTRange, opts)

Scroll documents

In the first request, the &#x60;X-VTEX-MD-TOKEN&#x60; token will be returned in the header. This token must be passed to the next request in the query string &#x60;_token&#x60; parameter. The token has a timeout of 10 minutes, which refreshes after each request.    After the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;429&#x60;.    ## Request examples    First request:  &#x60;&#x60;&#x60;  /dataentities/Client/scroll?isCluster&#x3D;true&amp;_size&#x3D;250&amp;_fields&#x3D;email,firstName  &#x60;&#x60;&#x60;    Retrieve the token in the header &#x60;X-VTEX-MD-TOKEN&#x60; from the first request&#39;s response and use it to make the next requests.    Subsequent requests:  &#x60;&#x60;&#x60;  /dataentities/Client/scroll?_token&#x3D;{tokenValueExample}  &#x60;&#x60;&#x60;

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.ScrollApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let rESTRange = "resources=0-10"; // String | Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query.
let opts = {
  'token': "'{tokenValueExample}'", // String | Value of the header `X-VTEX-MD-TOKEN` returned in your first request. Send its value in this query string in the subsequent requests. The token has a timeout of 10 minutes, which refreshes after each new request.
  'fields': "'email,firstName,document'", // String | Fields that should be returned by document. Separate fields' names with commas. For example `_fields=email,firstName,document`. You can also use `_all` to fetch all fields.
  'where': "firstName is not null.", // String | Filter specification.
  'schema': "schema", // String | Name of the schema the document to be created needs to be compliant with.
  'keyword': "String to search", // String | String to search. Use quotes for a partial query. For example, `_keyword=Maria` or `_keyword=\"Maria\"`.
  'sort': "'firstName ASC'" // String | Sets sorting mode in two parts. The first part is the name of the field you want to sort by. In the second part, use `ASC` for ascending or `DESC` for descending.
};
apiInstance.scrolldocuments(dataEntityName, contentType, accept, rESTRange, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **rESTRange** | **String**| Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query. | 
 **token** | **String**| Value of the header &#x60;X-VTEX-MD-TOKEN&#x60; returned in your first request. Send its value in this query string in the subsequent requests. The token has a timeout of 10 minutes, which refreshes after each new request. | [optional] [default to &#39;{tokenValueExample}&#39;]
 **fields** | **String**| Fields that should be returned by document. Separate fields&#39; names with commas. For example &#x60;_fields&#x3D;email,firstName,document&#x60;. You can also use &#x60;_all&#x60; to fetch all fields. | [optional] [default to &#39;email,firstName,document&#39;]
 **where** | **String**| Filter specification. | [optional] 
 **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] 
 **keyword** | **String**| String to search. Use quotes for a partial query. For example, &#x60;_keyword&#x3D;Maria&#x60; or &#x60;_keyword&#x3D;\&quot;Maria\&quot;&#x60;. | [optional] 
 **sort** | **String**| Sets sorting mode in two parts. The first part is the name of the field you want to sort by. In the second part, use &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending. | [optional] [default to &#39;firstName ASC&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

