# OtoroshiAdminApi.ValidationAuthoritiesApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createClientValidator**](ValidationAuthoritiesApi.md#createClientValidator) | **POST** /api/client-validators | Create one validation authorities
[**deleteClientValidator**](ValidationAuthoritiesApi.md#deleteClientValidator) | **DELETE** /api/client-validators/{id} | Delete one validation authorities by id
[**findAllClientValidators**](ValidationAuthoritiesApi.md#findAllClientValidators) | **GET** /api/client-validators | Get all validation authoritiess
[**findClientValidatorById**](ValidationAuthoritiesApi.md#findClientValidatorById) | **GET** /api/client-validators/{id} | Get one validation authorities by id
[**patchClientValidator**](ValidationAuthoritiesApi.md#patchClientValidator) | **PATCH** /api/client-validators/{id} | Update one validation authorities by id
[**updateClientValidator**](ValidationAuthoritiesApi.md#updateClientValidator) | **PUT** /api/client-validators/{id} | Update one validation authorities by id



## createClientValidator

> ValidationAuthority createClientValidator(opts)

Create one validation authorities

Create one validation authorities

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ValidationAuthoritiesApi();
let opts = {
  'validationAuthority': new OtoroshiAdminApi.ValidationAuthority() // ValidationAuthority | 
};
apiInstance.createClientValidator(opts, (error, data, response) => {
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
 **validationAuthority** | [**ValidationAuthority**](ValidationAuthority.md)|  | [optional] 

### Return type

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteClientValidator

> Deleted deleteClientValidator(id)

Delete one validation authorities by id

Delete one validation authorities by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ValidationAuthoritiesApi();
let id = "id_example"; // String | The validation authorities id
apiInstance.deleteClientValidator(id, (error, data, response) => {
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
 **id** | **String**| The validation authorities id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findAllClientValidators

> [ValidationAuthority] findAllClientValidators()

Get all validation authoritiess

Get all validation authoritiess

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ValidationAuthoritiesApi();
apiInstance.findAllClientValidators((error, data, response) => {
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

[**[ValidationAuthority]**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findClientValidatorById

> ValidationAuthority findClientValidatorById(id)

Get one validation authorities by id

Get one validation authorities by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ValidationAuthoritiesApi();
let id = "id_example"; // String | The auth. config id
apiInstance.findClientValidatorById(id, (error, data, response) => {
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

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchClientValidator

> ValidationAuthority patchClientValidator(id, opts)

Update one validation authorities by id

Update one validation authorities by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ValidationAuthoritiesApi();
let id = "id_example"; // String | The validation authorities id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchClientValidator(id, opts, (error, data, response) => {
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
 **id** | **String**| The validation authorities id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateClientValidator

> ValidationAuthority updateClientValidator(id, opts)

Update one validation authorities by id

Update one validation authorities by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ValidationAuthoritiesApi();
let id = "id_example"; // String | The validation authorities id
let opts = {
  'validationAuthority': new OtoroshiAdminApi.ValidationAuthority() // ValidationAuthority | 
};
apiInstance.updateClientValidator(id, opts, (error, data, response) => {
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
 **id** | **String**| The validation authorities id | 
 **validationAuthority** | [**ValidationAuthority**](ValidationAuthority.md)|  | [optional] 

### Return type

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

