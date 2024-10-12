# SearchIndexClient.DocumentsProxyApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentsProxyCount**](DocumentsProxyApi.md#documentsProxyCount) | **GET** /docs/$count | 



## documentsProxyCount

> Number documentsProxyCount(apiVersion, opts)



Queries the number of documents in the Azure Search index.

### Example

```javascript
import SearchIndexClient from 'search_index_client';

let apiInstance = new SearchIndexClient.DocumentsProxyApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example" // String | The tracking ID sent with the request to help with debugging.
};
apiInstance.documentsProxyCount(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **clientRequestId** | **String**| The tracking ID sent with the request to help with debugging. | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

