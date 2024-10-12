# ApimaticApiTransformer.DefaultApi

All URIs are relative to *https://apimatic.io/api/transform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convertAPI**](DefaultApi.md#convertAPI) | **POST** /transform | Transform API Descriptions from/to various formats



## convertAPI

> Object convertAPI(format, opts)

Transform API Descriptions from/to various formats

Transform API Descriptions from/to various formats e.g., Swagger, API Blueprint, RAML, WADL, Google Discovery, I/O Docs.  ### INPUTS * API Blueprint * Swagger 1.0 - 1.2 * Swagger 2.0 JSON * Swagger 2.0 YAML * WADL - W3C 2009 * Google Discovery * RAML 0.8 * I/O Docs - Mashery * HAR 1.2 * Postman Collection 1.0 - 2.0 * APIMATIC Format * Mashape  ### OUTPUTS * API Blueprint * Swagger 1.2 * Swagger 2.0 JSON * Swagger 2.0 YAML * WADL - W3C 2009 * RAML 0.8 - 1.0 * APIMATIC Format

### Example

```javascript
import ApimaticApiTransformer from 'apimatic_api_transformer';

let apiInstance = new ApimaticApiTransformer.DefaultApi();
let format = "format_example"; // String | 
let opts = {
  'url': "url_example" // String | 
};
apiInstance.convertAPI(format, opts, (error, data, response) => {
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
 **format** | **String**|  | 
 **url** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/x-yaml

