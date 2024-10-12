# SearchIndexClient.DocumentsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentsCount**](DocumentsApi.md#documentsCount) | **GET** /docs/$count | 



## documentsCount

> Number documentsCount(apiVersion, opts)



Queries the number of documents in the Azure Search index.

### Example

```javascript
import SearchIndexClient from 'search_index_client';

let apiInstance = new SearchIndexClient.DocumentsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example" // String | Tracking ID sent with the request to help with debugging.
};
apiInstance.documentsCount(apiVersion, opts, (error, data, response) => {
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
 **clientRequestId** | **String**| Tracking ID sent with the request to help with debugging. | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

