# SvixApi.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthApiV1HealthGet**](HealthApi.md#healthApiV1HealthGet) | **GET** /api/v1/health/ | Health



## healthApiV1HealthGet

> healthApiV1HealthGet(opts)

Health

Verify the API server is up and running.

### Example

```javascript
import SvixApi from 'svix_api';

let apiInstance = new SvixApi.HealthApi();
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.healthApiV1HealthGet(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

