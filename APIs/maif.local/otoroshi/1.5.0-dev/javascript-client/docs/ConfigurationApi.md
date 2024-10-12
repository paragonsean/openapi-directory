# OtoroshiAdminApi.ConfigurationApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalConfig**](ConfigurationApi.md#globalConfig) | **GET** /api/globalconfig | Get the full configuration of Otoroshi
[**patchGlobalConfig**](ConfigurationApi.md#patchGlobalConfig) | **PATCH** /api/globalconfig | Update the global configuration with a diff
[**putGlobalConfig**](ConfigurationApi.md#putGlobalConfig) | **PUT** /api/globalconfig | Update the global configuration



## globalConfig

> GlobalConfig globalConfig()

Get the full configuration of Otoroshi

Get the full configuration of Otoroshi

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ConfigurationApi();
apiInstance.globalConfig((error, data, response) => {
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

[**GlobalConfig**](GlobalConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchGlobalConfig

> GlobalConfig patchGlobalConfig(opts)

Update the global configuration with a diff

Update the global configuration with a diff

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ConfigurationApi();
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchGlobalConfig(opts, (error, data, response) => {
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
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**GlobalConfig**](GlobalConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putGlobalConfig

> GlobalConfig putGlobalConfig(opts)

Update the global configuration

Update the global configuration

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ConfigurationApi();
let opts = {
  'globalConfig': new OtoroshiAdminApi.GlobalConfig() // GlobalConfig | 
};
apiInstance.putGlobalConfig(opts, (error, data, response) => {
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
 **globalConfig** | [**GlobalConfig**](GlobalConfig.md)|  | [optional] 

### Return type

[**GlobalConfig**](GlobalConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

