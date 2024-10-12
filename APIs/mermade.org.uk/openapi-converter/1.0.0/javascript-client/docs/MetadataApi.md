# Swagger2OpenApiConverter.MetadataApi

All URIs are relative to *https://mermade.org.uk/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatus**](MetadataApi.md#getStatus) | **GET** /status | Get the status of the API



## getStatus

> Object getStatus()

Get the status of the API



### Example

```javascript
import Swagger2OpenApiConverter from 'swagger2_open_api_converter';

let apiInstance = new Swagger2OpenApiConverter.MetadataApi();
apiInstance.getStatus((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-yaml

