# OtoroshiAdminApi.JwtVerifiersApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGlobalJwtVerifier**](JwtVerifiersApi.md#createGlobalJwtVerifier) | **POST** /api/verifiers | Create one global JWT verifiers
[**deleteGlobalJwtVerifier**](JwtVerifiersApi.md#deleteGlobalJwtVerifier) | **DELETE** /api/verifiers/{verifierId} | Delete one global JWT verifiers
[**findAllGlobalJwtVerifiers**](JwtVerifiersApi.md#findAllGlobalJwtVerifiers) | **GET** /api/verifiers | Get all global JWT verifiers
[**findGlobalJwtVerifiersById**](JwtVerifiersApi.md#findGlobalJwtVerifiersById) | **GET** /api/verifiers/{verifierId} | Get one global JWT verifiers
[**patchGlobalJwtVerifier**](JwtVerifiersApi.md#patchGlobalJwtVerifier) | **PATCH** /api/verifiers/{verifierId} | Update one global JWT verifiers
[**updateGlobalJwtVerifier**](JwtVerifiersApi.md#updateGlobalJwtVerifier) | **PUT** /api/verifiers/{verifierId} | Update one global JWT verifiers



## createGlobalJwtVerifier

> GlobalJwtVerifier createGlobalJwtVerifier(opts)

Create one global JWT verifiers

Create one global JWT verifiers

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.JwtVerifiersApi();
let opts = {
  'globalJwtVerifier': new OtoroshiAdminApi.GlobalJwtVerifier() // GlobalJwtVerifier | 
};
apiInstance.createGlobalJwtVerifier(opts, (error, data, response) => {
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
 **globalJwtVerifier** | [**GlobalJwtVerifier**](GlobalJwtVerifier.md)|  | [optional] 

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGlobalJwtVerifier

> Deleted deleteGlobalJwtVerifier(verifierId)

Delete one global JWT verifiers

Delete one global JWT verifiers

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.JwtVerifiersApi();
let verifierId = "verifierId_example"; // String | The jwt verifier id
apiInstance.deleteGlobalJwtVerifier(verifierId, (error, data, response) => {
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
 **verifierId** | **String**| The jwt verifier id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findAllGlobalJwtVerifiers

> [GlobalJwtVerifier] findAllGlobalJwtVerifiers()

Get all global JWT verifiers

Get all global JWT verifiers

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.JwtVerifiersApi();
apiInstance.findAllGlobalJwtVerifiers((error, data, response) => {
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

[**[GlobalJwtVerifier]**](GlobalJwtVerifier.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findGlobalJwtVerifiersById

> GlobalJwtVerifier findGlobalJwtVerifiersById(verifierId)

Get one global JWT verifiers

Get one global JWT verifiers

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.JwtVerifiersApi();
let verifierId = "verifierId_example"; // String | The jwt verifier id
apiInstance.findGlobalJwtVerifiersById(verifierId, (error, data, response) => {
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
 **verifierId** | **String**| The jwt verifier id | 

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchGlobalJwtVerifier

> GlobalJwtVerifier patchGlobalJwtVerifier(verifierId, opts)

Update one global JWT verifiers

Update one global JWT verifiers

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.JwtVerifiersApi();
let verifierId = "verifierId_example"; // String | The jwt verifier id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchGlobalJwtVerifier(verifierId, opts, (error, data, response) => {
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
 **verifierId** | **String**| The jwt verifier id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGlobalJwtVerifier

> GlobalJwtVerifier updateGlobalJwtVerifier(verifierId, opts)

Update one global JWT verifiers

Update one global JWT verifiers

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.JwtVerifiersApi();
let verifierId = "verifierId_example"; // String | The jwt verifier id
let opts = {
  'globalJwtVerifier': new OtoroshiAdminApi.GlobalJwtVerifier() // GlobalJwtVerifier | 
};
apiInstance.updateGlobalJwtVerifier(verifierId, opts, (error, data, response) => {
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
 **verifierId** | **String**| The jwt verifier id | 
 **globalJwtVerifier** | [**GlobalJwtVerifier**](GlobalJwtVerifier.md)|  | [optional] 

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

