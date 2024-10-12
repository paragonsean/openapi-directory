# OtoroshiAdminApi.HealthApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](HealthApi.md#health) | **GET** /health | Return current Otoroshi health



## health

> OtoroshiHealth health()

Return current Otoroshi health

Import the full state of Otoroshi as a file

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';

let apiInstance = new OtoroshiAdminApi.HealthApi();
apiInstance.health((error, data, response) => {
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

[**OtoroshiHealth**](OtoroshiHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

