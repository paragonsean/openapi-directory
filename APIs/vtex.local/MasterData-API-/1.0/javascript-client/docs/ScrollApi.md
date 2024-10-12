# MasterDataApiV1.ScrollApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scrolldocuments**](ScrollApi.md#scrolldocuments) | **GET** /api/dataentities/{acronym}/scroll | Scroll documents



## scrolldocuments

> scrolldocuments(contentType, accept, acronym)

Scroll documents

Scrolls through documents according to the query parameter filters.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;429&#x60;.    Use all the features of &#x60;search&#x60; API to perform filters.    In the first request, the &#x60;X-VTEX-MD-TOKEN&#x60; token will be obtained in the header. This token must be passed to the next request in the query string &#x60;_token&#x60; parameter. The token has a timeout of 10 minutes, which refreshes after each request.    **ATTENTION:** To inform the number of documents per request, use the query string parameter &#x60;_size&#x60;, which has the maximum value of 1000.    After the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.    ### First request example:  &#x60;&#x60;&#x60;  /dataentities/CL/scroll?isCluster&#x3D;true&amp;_size&#x3D;250&amp;_fields&#x3D;email,firstName  &#x60;&#x60;&#x60;    After the first request, retrieve the token in the header &#x60;X-VTEX-MD-TOKEN&#x60; and make the next requests.    ### Example of subsequent requests:  &#x60;&#x60;&#x60;  /dataentities/CL/scroll?_token&#x3D;tokenvalueexample  &#x60;&#x60;&#x60;

### Example

```javascript
import MasterDataApiV1 from 'master_data_api_v1';
let defaultClient = MasterDataApiV1.ApiClient.instance;
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

let apiInstance = new MasterDataApiV1.ScrollApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Identifies the kind of data
apiInstance.scrolldocuments(contentType, accept, acronym, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **acronym** | **String**| Identifies the kind of data | [default to &#39;{{acronym}}&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

