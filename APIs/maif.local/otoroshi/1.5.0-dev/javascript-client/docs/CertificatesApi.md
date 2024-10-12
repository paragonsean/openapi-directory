# OtoroshiAdminApi.CertificatesApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allCerts**](CertificatesApi.md#allCerts) | **GET** /api/certificates | Get all certificates
[**createCert**](CertificatesApi.md#createCert) | **POST** /api/certificates | Create one certificate
[**deleteCert**](CertificatesApi.md#deleteCert) | **DELETE** /api/certificates/{id} | Delete one certificate by id
[**oneCert**](CertificatesApi.md#oneCert) | **GET** /api/certificates/{id} | Get one certificate by id
[**patchCert**](CertificatesApi.md#patchCert) | **PATCH** /api/certificates/{id} | Update one certificate by id
[**putCert**](CertificatesApi.md#putCert) | **PUT** /api/certificates/{id} | Update one certificate by id



## allCerts

> [Certificate] allCerts()

Get all certificates

Get all certificates

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.CertificatesApi();
apiInstance.allCerts((error, data, response) => {
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

[**[Certificate]**](Certificate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createCert

> Certificate createCert(opts)

Create one certificate

Create one certificate

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.CertificatesApi();
let opts = {
  'certificate': new OtoroshiAdminApi.Certificate() // Certificate | 
};
apiInstance.createCert(opts, (error, data, response) => {
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
 **certificate** | [**Certificate**](Certificate.md)|  | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCert

> Deleted deleteCert(id)

Delete one certificate by id

Delete one certificate by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.CertificatesApi();
let id = "id_example"; // String | The certificate id
apiInstance.deleteCert(id, (error, data, response) => {
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
 **id** | **String**| The certificate id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oneCert

> Certificate oneCert(id)

Get one certificate by id

Get one certificate by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.CertificatesApi();
let id = "id_example"; // String | The auth. config id
apiInstance.oneCert(id, (error, data, response) => {
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

[**Certificate**](Certificate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchCert

> Certificate patchCert(id, opts)

Update one certificate by id

Update one certificate by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.CertificatesApi();
let id = "id_example"; // String | The certificate id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchCert(id, opts, (error, data, response) => {
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
 **id** | **String**| The certificate id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putCert

> Certificate putCert(id, opts)

Update one certificate by id

Update one certificate by id

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.CertificatesApi();
let id = "id_example"; // String | The certificate id
let opts = {
  'certificate': new OtoroshiAdminApi.Certificate() // Certificate | 
};
apiInstance.putCert(id, opts, (error, data, response) => {
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
 **id** | **String**| The certificate id | 
 **certificate** | [**Certificate**](Certificate.md)|  | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

