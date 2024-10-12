# WeGaApi.SearchApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchEntityGet**](SearchApi.md#searchEntityGet) | **GET** /search/entity | Search for a WeGA entity



## searchEntityGet

> [Document] searchEntityGet(opts)

Search for a WeGA entity

This endpoint returns the search results for an entity&#39;s name or title. 

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.SearchApi();
let opts = {
  'docType': ["null"], // [String] | The WeGA document type
  'q': "q_example", // String | The query string
  'offset': 1, // Number | Position of first item to retrieve (starting from 1)
  'limit': 10 // Number | Number of items to retrieve (200 max)
};
apiInstance.searchEntityGet(opts, (error, data, response) => {
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
 **docType** | [**[String]**](String.md)| The WeGA document type | [optional] 
 **q** | **String**| The query string | [optional] 
 **offset** | **Number**| Position of first item to retrieve (starting from 1) | [optional] [default to 1]
 **limit** | **Number**| Number of items to retrieve (200 max) | [optional] [default to 10]

### Return type

[**[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

