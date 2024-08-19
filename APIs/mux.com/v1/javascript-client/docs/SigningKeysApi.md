# MuxApi.SigningKeysApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSigningKey**](SigningKeysApi.md#createSigningKey) | **POST** /system/v1/signing-keys | Create a signing key
[**deleteSigningKey**](SigningKeysApi.md#deleteSigningKey) | **DELETE** /system/v1/signing-keys/{SIGNING_KEY_ID} | Delete a signing key
[**getSigningKey**](SigningKeysApi.md#getSigningKey) | **GET** /system/v1/signing-keys/{SIGNING_KEY_ID} | Retrieve a signing key
[**listSigningKeys**](SigningKeysApi.md#listSigningKeys) | **GET** /system/v1/signing-keys | List signing keys



## createSigningKey

> SigningKeyResponse createSigningKey()

Create a signing key

Creates a new signing key pair. When creating a new signing key, the API will generate a 2048-bit RSA key-pair and return the private key and a generated key-id; the public key will be stored at Mux to validate signed tokens.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SigningKeysApi();
apiInstance.createSigningKey((error, data, response) => {
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

[**SigningKeyResponse**](SigningKeyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSigningKey

> deleteSigningKey(SIGNING_KEY_ID)

Delete a signing key

Deletes an existing signing key. Use with caution, as this will invalidate any existing signatures and no JWTs can be signed using the key again.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SigningKeysApi();
let SIGNING_KEY_ID = "SIGNING_KEY_ID_example"; // String | The ID of the signing key.
apiInstance.deleteSigningKey(SIGNING_KEY_ID, (error, data, response) => {
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
 **SIGNING_KEY_ID** | **String**| The ID of the signing key. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSigningKey

> SigningKeyResponse getSigningKey(SIGNING_KEY_ID)

Retrieve a signing key

Retrieves the details of a signing key that has previously been created. Supply the unique signing key ID that was returned from your previous request, and Mux will return the corresponding signing key information. **The private key is not returned in this response.** 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SigningKeysApi();
let SIGNING_KEY_ID = "SIGNING_KEY_ID_example"; // String | The ID of the signing key.
apiInstance.getSigningKey(SIGNING_KEY_ID, (error, data, response) => {
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
 **SIGNING_KEY_ID** | **String**| The ID of the signing key. | 

### Return type

[**SigningKeyResponse**](SigningKeyResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSigningKeys

> ListSigningKeysResponse listSigningKeys(opts)

List signing keys

Returns a list of signing keys.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SigningKeysApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1 // Number | Offset by this many pages, of the size of `limit`
};
apiInstance.listSigningKeys(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListSigningKeysResponse**](ListSigningKeysResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

