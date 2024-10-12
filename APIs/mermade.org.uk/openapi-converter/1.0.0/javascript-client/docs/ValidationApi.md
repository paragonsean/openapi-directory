# Swagger2OpenApiConverter.ValidationApi

All URIs are relative to *https://mermade.org.uk/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBadge**](ValidationApi.md#getBadge) | **GET** /badge | Return a redirect to a badge svg file depending on a source definition&#39;s validity
[**validate**](ValidationApi.md#validate) | **POST** /validate | Validate an OpenAPI 3.0.x definition supplied in the body of the request
[**validateUrl**](ValidationApi.md#validateUrl) | **GET** /validate | Validate an OpenAPI 3.0.x definition



## getBadge

> getBadge(url)

Return a redirect to a badge svg file depending on a source definition&#39;s validity



### Example

```javascript
import Swagger2OpenApiConverter from 'swagger2_open_api_converter';

let apiInstance = new Swagger2OpenApiConverter.ValidationApi();
let url = "https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json"; // String | The URL to retrieve the OpenAPI 3.0.x definition from
apiInstance.getBadge(url, (error, data, response) => {
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
 **url** | **String**| The URL to retrieve the OpenAPI 3.0.x definition from | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## validate

> ValidationResult validate(opts)

Validate an OpenAPI 3.0.x definition supplied in the body of the request



### Example

```javascript
import Swagger2OpenApiConverter from 'swagger2_open_api_converter';

let apiInstance = new Swagger2OpenApiConverter.ValidationApi();
let opts = {
  'filename': "filename_example", // String | The file to upload and validate
  'source': "source_example" // String | The text of an OpenAPI 3.0.x definition to validate
};
apiInstance.validate(opts, (error, data, response) => {
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
 **filename** | **String**| The file to upload and validate | [optional] 
 **source** | **String**| The text of an OpenAPI 3.0.x definition to validate | [optional] 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/x-yaml


## validateUrl

> ValidationResult validateUrl(url)

Validate an OpenAPI 3.0.x definition



### Example

```javascript
import Swagger2OpenApiConverter from 'swagger2_open_api_converter';

let apiInstance = new Swagger2OpenApiConverter.ValidationApi();
let url = "https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json"; // String | The URL to retrieve the OpenAPI 3.0.x definition from
apiInstance.validateUrl(url, (error, data, response) => {
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
 **url** | **String**| The URL to retrieve the OpenAPI 3.0.x definition from | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-yaml

