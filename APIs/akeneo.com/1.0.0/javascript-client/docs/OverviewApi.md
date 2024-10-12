# AkeneoPimRestApi.OverviewApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEndpoints**](OverviewApi.md#getEndpoints) | **GET** /api/rest/v1 | Get list of all endpoints



## getEndpoints

> GetEndpoints200Response getEndpoints()

Get list of all endpoints

This endpoint allows you to get the list of all the available endpoints. No need to be authenticated to use this endpoint.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.OverviewApi();
apiInstance.getEndpoints((error, data, response) => {
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

[**GetEndpoints200Response**](GetEndpoints200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, authentication, host, routes, code, message

