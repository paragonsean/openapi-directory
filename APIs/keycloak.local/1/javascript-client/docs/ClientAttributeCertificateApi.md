# KeycloakAdminRestApi.ClientAttributeCertificateApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientsIdCertificatesAttrDownloadPost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrDownloadPost) | **POST** /{realm}/clients/{id}/certificates/{attr}/download | Get a keystore file for the client, containing private key and public certificate
[**realmClientsIdCertificatesAttrGenerateAndDownloadPost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrGenerateAndDownloadPost) | **POST** /{realm}/clients/{id}/certificates/{attr}/generate-and-download | Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.
[**realmClientsIdCertificatesAttrGeneratePost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrGeneratePost) | **POST** /{realm}/clients/{id}/certificates/{attr}/generate | Generate a new certificate with new key pair
[**realmClientsIdCertificatesAttrGet**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrGet) | **GET** /{realm}/clients/{id}/certificates/{attr} | Get key info
[**realmClientsIdCertificatesAttrUploadCertificatePost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrUploadCertificatePost) | **POST** /{realm}/clients/{id}/certificates/{attr}/upload-certificate | Upload only certificate, not private key
[**realmClientsIdCertificatesAttrUploadPost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrUploadPost) | **POST** /{realm}/clients/{id}/certificates/{attr}/upload | Upload certificate and eventually private key



## realmClientsIdCertificatesAttrDownloadPost

> Blob realmClientsIdCertificatesAttrDownloadPost(realm, id, attr, keyStoreConfig)

Get a keystore file for the client, containing private key and public certificate

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientAttributeCertificateApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let attr = "attr_example"; // String | 
let keyStoreConfig = new KeycloakAdminRestApi.KeyStoreConfig(); // KeyStoreConfig | Keystore configuration as JSON
apiInstance.realmClientsIdCertificatesAttrDownloadPost(realm, id, attr, keyStoreConfig, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**| id of client (not client-id) | 
 **attr** | **String**|  | 
 **keyStoreConfig** | [**KeyStoreConfig**](KeyStoreConfig.md)| Keystore configuration as JSON | 

### Return type

**Blob**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## realmClientsIdCertificatesAttrGenerateAndDownloadPost

> Blob realmClientsIdCertificatesAttrGenerateAndDownloadPost(realm, id, attr, keyStoreConfig)

Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientAttributeCertificateApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let attr = "attr_example"; // String | 
let keyStoreConfig = new KeycloakAdminRestApi.KeyStoreConfig(); // KeyStoreConfig | Keystore configuration as JSON
apiInstance.realmClientsIdCertificatesAttrGenerateAndDownloadPost(realm, id, attr, keyStoreConfig, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**| id of client (not client-id) | 
 **attr** | **String**|  | 
 **keyStoreConfig** | [**KeyStoreConfig**](KeyStoreConfig.md)| Keystore configuration as JSON | 

### Return type

**Blob**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## realmClientsIdCertificatesAttrGeneratePost

> CertificateRepresentation realmClientsIdCertificatesAttrGeneratePost(realm, id, attr)

Generate a new certificate with new key pair

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientAttributeCertificateApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let attr = "attr_example"; // String | 
apiInstance.realmClientsIdCertificatesAttrGeneratePost(realm, id, attr, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**| id of client (not client-id) | 
 **attr** | **String**|  | 

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdCertificatesAttrGet

> CertificateRepresentation realmClientsIdCertificatesAttrGet(realm, id, attr)

Get key info

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientAttributeCertificateApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let attr = "attr_example"; // String | 
apiInstance.realmClientsIdCertificatesAttrGet(realm, id, attr, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**| id of client (not client-id) | 
 **attr** | **String**|  | 

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdCertificatesAttrUploadCertificatePost

> CertificateRepresentation realmClientsIdCertificatesAttrUploadCertificatePost(realm, id, attr)

Upload only certificate, not private key

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientAttributeCertificateApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let attr = "attr_example"; // String | 
apiInstance.realmClientsIdCertificatesAttrUploadCertificatePost(realm, id, attr, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**| id of client (not client-id) | 
 **attr** | **String**|  | 

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdCertificatesAttrUploadPost

> CertificateRepresentation realmClientsIdCertificatesAttrUploadPost(realm, id, attr)

Upload certificate and eventually private key

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientAttributeCertificateApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let attr = "attr_example"; // String | 
apiInstance.realmClientsIdCertificatesAttrUploadPost(realm, id, attr, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **id** | **String**| id of client (not client-id) | 
 **attr** | **String**|  | 

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

