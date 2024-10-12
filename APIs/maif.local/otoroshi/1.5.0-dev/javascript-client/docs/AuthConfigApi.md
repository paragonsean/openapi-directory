# OtoroshiAdminApi.AuthConfigApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGlobalAuthModule**](AuthConfigApi.md#createGlobalAuthModule) | **POST** /api/auths | Create one global auth. module config
[**deleteGlobalAuthModule**](AuthConfigApi.md#deleteGlobalAuthModule) | **DELETE** /api/auths/{id} | Delete one global auth. module config
[**findAllGlobalAuthModules**](AuthConfigApi.md#findAllGlobalAuthModules) | **GET** /api/auths | Get all global auth. module configs
[**findGlobalAuthModuleById**](AuthConfigApi.md#findGlobalAuthModuleById) | **GET** /api/auths/{id} | Get one global auth. module configs
[**patchGlobalAuthModule**](AuthConfigApi.md#patchGlobalAuthModule) | **PATCH** /api/auths/{id} | Update one global auth. module config
[**updateGlobalAuthModule**](AuthConfigApi.md#updateGlobalAuthModule) | **PUT** /api/auths/{id} | Update one global auth. module config



## createGlobalAuthModule

> FindAllGlobalAuthModules200ResponseInner createGlobalAuthModule(opts)

Create one global auth. module config

Create one global auth. module config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.AuthConfigApi();
let opts = {
  'findAllGlobalAuthModules200ResponseInner': new OtoroshiAdminApi.FindAllGlobalAuthModules200ResponseInner() // FindAllGlobalAuthModules200ResponseInner | 
};
apiInstance.createGlobalAuthModule(opts, (error, data, response) => {
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
 **findAllGlobalAuthModules200ResponseInner** | [**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)|  | [optional] 

### Return type

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGlobalAuthModule

> Deleted deleteGlobalAuthModule(id)

Delete one global auth. module config

Delete one global auth. module config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.AuthConfigApi();
let id = "id_example"; // String | The auth. config id id
apiInstance.deleteGlobalAuthModule(id, (error, data, response) => {
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
 **id** | **String**| The auth. config id id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findAllGlobalAuthModules

> [FindAllGlobalAuthModules200ResponseInner] findAllGlobalAuthModules()

Get all global auth. module configs

Get all global auth. module configs

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.AuthConfigApi();
apiInstance.findAllGlobalAuthModules((error, data, response) => {
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

[**[FindAllGlobalAuthModules200ResponseInner]**](FindAllGlobalAuthModules200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findGlobalAuthModuleById

> FindAllGlobalAuthModules200ResponseInner findGlobalAuthModuleById(id)

Get one global auth. module configs

Get one global auth. module configs

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.AuthConfigApi();
let id = "id_example"; // String | The auth. config id
apiInstance.findGlobalAuthModuleById(id, (error, data, response) => {
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
 **id** | **String**| The auth. config id | 

### Return type

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchGlobalAuthModule

> FindAllGlobalAuthModules200ResponseInner patchGlobalAuthModule(id, opts)

Update one global auth. module config

Update one global auth. module config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.AuthConfigApi();
let id = "id_example"; // String | The auth. config id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchGlobalAuthModule(id, opts, (error, data, response) => {
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
 **id** | **String**| The auth. config id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGlobalAuthModule

> FindAllGlobalAuthModules200ResponseInner updateGlobalAuthModule(id, opts)

Update one global auth. module config

Update one global auth. module config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.AuthConfigApi();
let id = "id_example"; // String | The auth. config id
let opts = {
  'findAllGlobalAuthModules200ResponseInner': new OtoroshiAdminApi.FindAllGlobalAuthModules200ResponseInner() // FindAllGlobalAuthModules200ResponseInner | 
};
apiInstance.updateGlobalAuthModule(id, opts, (error, data, response) => {
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
 **id** | **String**| The auth. config id | 
 **findAllGlobalAuthModules200ResponseInner** | [**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)|  | [optional] 

### Return type

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

