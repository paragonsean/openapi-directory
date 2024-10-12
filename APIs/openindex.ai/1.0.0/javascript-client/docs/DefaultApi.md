# OpenIndexRetrievalPluginApi.DefaultApi

All URIs are relative to */sub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryQueryPost**](DefaultApi.md#queryQueryPost) | **POST** /query | Query



## queryQueryPost

> QueryResponse queryQueryPost(queryRequest)

Query

Accepts search query objects array each with query and optional filter. Break down complex questions into sub-questions. Refine results by criteria, e.g. time / source, don&#39;t do this often. Split queries if ResponseTooLargeError occurs.

### Example

```javascript
import OpenIndexRetrievalPluginApi from 'open_index_retrieval_plugin_api';
let defaultClient = OpenIndexRetrievalPluginApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OpenIndexRetrievalPluginApi.DefaultApi();
let queryRequest = new OpenIndexRetrievalPluginApi.QueryRequest(); // QueryRequest | 
apiInstance.queryQueryPost(queryRequest, (error, data, response) => {
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
 **queryRequest** | [**QueryRequest**](QueryRequest.md)|  | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

