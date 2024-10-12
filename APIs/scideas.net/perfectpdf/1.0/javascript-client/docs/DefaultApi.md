# PerfectpdfApi.DefaultApi

All URIs are relative to *https://services.scideas.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perfectpdfApiPost**](DefaultApi.md#perfectpdfApiPost) | **POST** /perfectpdf/api | Returns PDF document.



## perfectpdfApiPost

> InlineResponse200 perfectpdfApiPost(perfectpdfApiBody)

Returns PDF document.

### Example

```javascript
import PerfectpdfApi from 'perfectpdf_api';

let apiInstance = new PerfectpdfApi.DefaultApi();
let perfectpdfApiBody = new PerfectpdfApi.PerfectpdfApiBody(); // PerfectpdfApiBody | 
apiInstance.perfectpdfApiPost(perfectpdfApiBody, (error, data, response) => {
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
 **perfectpdfApiBody** | [**PerfectpdfApiBody**](PerfectpdfApiBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/html

