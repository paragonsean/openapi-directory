# Swagger2OpenApiConverter.ConversionApi

All URIs are relative to *https://mermade.org.uk/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert**](ConversionApi.md#convert) | **POST** /convert | Convert a Swagger 2.0 definition passed in the body to OpenAPI 3.0.x 
[**convertUrl**](ConversionApi.md#convertUrl) | **GET** /convert | Convert a Swagger 2.0 definition to OpenAPI 3.0.x from a URL



## convert

> Object convert(opts)

Convert a Swagger 2.0 definition passed in the body to OpenAPI 3.0.x 



### Example

```javascript
import Swagger2OpenApiConverter from 'swagger2_open_api_converter';

let apiInstance = new Swagger2OpenApiConverter.ConversionApi();
let opts = {
  'filename': "filename_example", // String | The file to upload and convert
  'source': "source_example", // String | The text of a Swagger 2.0 definition to convert
  'validate': "validate_example" // String | 
};
apiInstance.convert(opts, (error, data, response) => {
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
 **filename** | **String**| The file to upload and convert | [optional] 
 **source** | **String**| The text of a Swagger 2.0 definition to convert | [optional] 
 **validate** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/x-yaml


## convertUrl

> Object convertUrl(url)

Convert a Swagger 2.0 definition to OpenAPI 3.0.x from a URL



### Example

```javascript
import Swagger2OpenApiConverter from 'swagger2_open_api_converter';

let apiInstance = new Swagger2OpenApiConverter.ConversionApi();
let url = "https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/swagger.json"; // String | The URL to retrieve the OpenAPI 2.0 definition from
apiInstance.convertUrl(url, (error, data, response) => {
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
 **url** | **String**| The URL to retrieve the OpenAPI 2.0 definition from | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-yaml

