# ControlApiV1.KeysApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppIdKeysGet**](KeysApi.md#appsAppIdKeysGet) | **GET** /apps/{app_id}/keys | Lists app keys
[**appsAppIdKeysKeyIdPatch**](KeysApi.md#appsAppIdKeysKeyIdPatch) | **PATCH** /apps/{app_id}/keys/{key_id} | Updates a key
[**appsAppIdKeysKeyIdRevokePost**](KeysApi.md#appsAppIdKeysKeyIdRevokePost) | **POST** /apps/{app_id}/keys/{key_id}/revoke | Revokes a key
[**appsAppIdKeysPost**](KeysApi.md#appsAppIdKeysPost) | **POST** /apps/{app_id}/keys | Creates a key



## appsAppIdKeysGet

> [KeyResponse] appsAppIdKeysGet(appId)

Lists app keys

Lists the API keys associated with the application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.KeysApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsAppIdKeysGet(appId, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 

### Return type

[**[KeyResponse]**](KeyResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdKeysKeyIdPatch

> KeyResponse appsAppIdKeysKeyIdPatch(appId, keyId, opts)

Updates a key

Update the API key with the specified key ID, for the application with the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.KeysApi();
let appId = "appId_example"; // String | The application ID.
let keyId = "keyId_example"; // String | The API key ID.
let opts = {
  'keyPatch': new ControlApiV1.KeyPatch() // KeyPatch | 
};
apiInstance.appsAppIdKeysKeyIdPatch(appId, keyId, opts, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **keyId** | **String**| The API key ID. | 
 **keyPatch** | [**KeyPatch**](KeyPatch.md)|  | [optional] 

### Return type

[**KeyResponse**](KeyResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsAppIdKeysKeyIdRevokePost

> appsAppIdKeysKeyIdRevokePost(appId, keyId)

Revokes a key

Revokes the API key with the specified ID, with the Application ID. This deletes the key.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.KeysApi();
let appId = "appId_example"; // String | The application ID.
let keyId = "keyId_example"; // String | The key ID.
apiInstance.appsAppIdKeysKeyIdRevokePost(appId, keyId, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **keyId** | **String**| The key ID. | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdKeysPost

> KeyResponse appsAppIdKeysPost(appId, opts)

Creates a key

Creates an API key for the application specified.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.KeysApi();
let appId = "appId_example"; // String | The application ID.
let opts = {
  'keyPost': new ControlApiV1.KeyPost() // KeyPost | 
};
apiInstance.appsAppIdKeysPost(appId, opts, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **keyPost** | [**KeyPost**](KeyPost.md)|  | [optional] 

### Return type

[**KeyResponse**](KeyResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

