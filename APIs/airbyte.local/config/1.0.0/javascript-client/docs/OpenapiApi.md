# AirbyteConfigurationApi.OpenapiApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOpenApiSpec**](OpenapiApi.md#getOpenApiSpec) | **GET** /v1/openapi | Returns the openapi specification



## getOpenApiSpec

> File getOpenApiSpec()

Returns the openapi specification

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.OpenapiApi();
apiInstance.getOpenApiSpec((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

