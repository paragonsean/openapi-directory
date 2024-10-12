# OtoroshiAdminApi.TemplatesApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**initiateApiKey**](TemplatesApi.md#initiateApiKey) | **GET** /new/apikey | Get a template of an Otoroshi Api Key
[**initiateService**](TemplatesApi.md#initiateService) | **GET** /new/service | Get a template of an Otoroshi service descriptor
[**initiateServiceGroup**](TemplatesApi.md#initiateServiceGroup) | **GET** /new/group | Get a template of an Otoroshi service group



## initiateApiKey

> ApiKey initiateApiKey()

Get a template of an Otoroshi Api Key

Get a template of an Otoroshi Api Key. The generated entity is not persisted

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.TemplatesApi();
apiInstance.initiateApiKey((error, data, response) => {
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

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## initiateService

> Service initiateService()

Get a template of an Otoroshi service descriptor

Get a template of an Otoroshi service descriptor. The generated entity is not persisted

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.TemplatesApi();
apiInstance.initiateService((error, data, response) => {
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

[**Service**](Service.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## initiateServiceGroup

> Group initiateServiceGroup()

Get a template of an Otoroshi service group

Get a template of an Otoroshi service group. The generated entity is not persisted

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.TemplatesApi();
apiInstance.initiateServiceGroup((error, data, response) => {
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

[**Group**](Group.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

