# WeGaApi.CodeSamplesApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codeFindByElementElementGet**](CodeSamplesApi.md#codeFindByElementElementGet) | **GET** /code/findByElement/{element} | Finds code samples by XML element



## codeFindByElementElementGet

> [CodeSample] codeFindByElementElementGet(element, opts)

Finds code samples by XML element

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.CodeSamplesApi();
let element = "element_example"; // String | The XML element to search for
let opts = {
  'namespace': "'http://www.tei-c.org/ns/1.0'", // String | The element namespace. Defaults to the TEI namespace
  'docType': ["null"], // [String] | The WeGA document type
  'offset': 1, // Number | Position of first item to retrieve (starting from 1)
  'limit': 10 // Number | Number of items to retrieve (200 max)
};
apiInstance.codeFindByElementElementGet(element, opts, (error, data, response) => {
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
 **element** | **String**| The XML element to search for | 
 **namespace** | **String**| The element namespace. Defaults to the TEI namespace | [optional] [default to &#39;http://www.tei-c.org/ns/1.0&#39;]
 **docType** | [**[String]**](String.md)| The WeGA document type | [optional] 
 **offset** | **Number**| Position of first item to retrieve (starting from 1) | [optional] [default to 1]
 **limit** | **Number**| Number of items to retrieve (200 max) | [optional] [default to 10]

### Return type

[**[CodeSample]**](CodeSample.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

