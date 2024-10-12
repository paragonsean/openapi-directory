# Mailscript.KeysApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addKey**](KeysApi.md#addKey) | **POST** /addresses/{address}/keys | Add address key
[**deleteKey**](KeysApi.md#deleteKey) | **DELETE** /addresses/{address}/keys/{key} | Delete address key
[**getAllKeys**](KeysApi.md#getAllKeys) | **GET** /addresses/{address}/keys | List address keys
[**getKey**](KeysApi.md#getKey) | **GET** /addresses/{address}/keys/{key} | Get address key
[**updateKey**](KeysApi.md#updateKey) | **PUT** /addresses/{address}/keys/{key} | Update an address key



## addKey

> AddKeyResponse addKey(address, addKeyRequest)

Add address key

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.KeysApi();
let address = "address_example"; // String | ID of address
let addKeyRequest = new Mailscript.AddKeyRequest(); // AddKeyRequest | Key body
apiInstance.addKey(address, addKeyRequest, (error, data, response) => {
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
 **address** | **String**| ID of address | 
 **addKeyRequest** | [**AddKeyRequest**](AddKeyRequest.md)| Key body | 

### Return type

[**AddKeyResponse**](AddKeyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteKey

> deleteKey(address, key)

Delete address key

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.KeysApi();
let address = "address_example"; // String | ID of address
let key = "key_example"; // String | ID of key
apiInstance.deleteKey(address, key, (error, data, response) => {
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
 **address** | **String**| ID of address | 
 **key** | **String**| ID of key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllKeys

> GetAllKeysResponse getAllKeys(address)

List address keys

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.KeysApi();
let address = "address_example"; // String | ID of address
apiInstance.getAllKeys(address, (error, data, response) => {
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
 **address** | **String**| ID of address | 

### Return type

[**GetAllKeysResponse**](GetAllKeysResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKey

> Key getKey(address, key)

Get address key

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.KeysApi();
let address = "address_example"; // String | ID of address
let key = "key_example"; // String | ID of key
apiInstance.getKey(address, key, (error, data, response) => {
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
 **address** | **String**| ID of address | 
 **key** | **String**| ID of key | 

### Return type

[**Key**](Key.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateKey

> Key updateKey(address, key, updateKeyRequest)

Update an address key

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.KeysApi();
let address = "address_example"; // String | ID of address
let key = "key_example"; // String | ID of key
let updateKeyRequest = new Mailscript.UpdateKeyRequest(); // UpdateKeyRequest | Key body
apiInstance.updateKey(address, key, updateKeyRequest, (error, data, response) => {
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
 **address** | **String**| ID of address | 
 **key** | **String**| ID of key | 
 **updateKeyRequest** | [**UpdateKeyRequest**](UpdateKeyRequest.md)| Key body | 

### Return type

[**Key**](Key.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

