# MuxApi.URLSigningKeysApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUrlSigningKey**](URLSigningKeysApi.md#createUrlSigningKey) | **POST** /video/v1/signing-keys | Create a URL signing key
[**deleteUrlSigningKey**](URLSigningKeysApi.md#deleteUrlSigningKey) | **DELETE** /video/v1/signing-keys/{SIGNING_KEY_ID} | Delete a URL signing key
[**getUrlSigningKey**](URLSigningKeysApi.md#getUrlSigningKey) | **GET** /video/v1/signing-keys/{SIGNING_KEY_ID} | Retrieve a URL signing key
[**listUrlSigningKeys**](URLSigningKeysApi.md#listUrlSigningKeys) | **GET** /video/v1/signing-keys | List URL signing keys



## createUrlSigningKey

> SigningKeyResponse createUrlSigningKey()

Create a URL signing key

This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Creates a new signing key pair. When creating a new signing key, the API will generate a 2048-bit RSA key-pair and return the private key and a generated key-id; the public key will be stored at Mux to validate signed tokens.  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.URLSigningKeysApi();
apiInstance.createUrlSigningKey((error, data, response) => {
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


## deleteUrlSigningKey

> deleteUrlSigningKey(SIGNING_KEY_ID)

Delete a URL signing key

This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Deletes an existing signing key. Use with caution, as this will invalidate any existing signatures and no URLs can be signed using the key again.  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.URLSigningKeysApi();
let SIGNING_KEY_ID = "SIGNING_KEY_ID_example"; // String | The ID of the signing key.
apiInstance.deleteUrlSigningKey(SIGNING_KEY_ID, (error, data, response) => {
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


## getUrlSigningKey

> SigningKeyResponse getUrlSigningKey(SIGNING_KEY_ID)

Retrieve a URL signing key

This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Retrieves the details of a URL signing key that has previously been created. Supply the unique signing key ID that was returned from your previous request, and Mux will return the corresponding signing key information. **The private key is not returned in this response.**  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.URLSigningKeysApi();
let SIGNING_KEY_ID = "SIGNING_KEY_ID_example"; // String | The ID of the signing key.
apiInstance.getUrlSigningKey(SIGNING_KEY_ID, (error, data, response) => {
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


## listUrlSigningKeys

> ListSigningKeysResponse listUrlSigningKeys(opts)

List URL signing keys

This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Returns a list of URL signing keys.  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.URLSigningKeysApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1 // Number | Offset by this many pages, of the size of `limit`
};
apiInstance.listUrlSigningKeys(opts, (error, data, response) => {
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

