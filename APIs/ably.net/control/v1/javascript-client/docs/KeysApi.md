# ApiV1.KeysApi

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

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.KeysApi();
let appId = "appId_example"; // String | 
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
 **appId** | **String**|  | 

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

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.KeysApi();
let appId = "appId_example"; // String | 
let keyId = "keyId_example"; // String | 
let opts = {
  'keyPatch': new ApiV1.KeyPatch() // KeyPatch | 
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
 **appId** | **String**|  | 
 **keyId** | **String**|  | 
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

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.KeysApi();
let appId = "appId_example"; // String | 
let keyId = "keyId_example"; // String | 
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
 **appId** | **String**|  | 
 **keyId** | **String**|  | 

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

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.KeysApi();
let appId = "appId_example"; // String | 
let opts = {
  'keyPost': new ApiV1.KeyPost() // KeyPost | 
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
 **appId** | **String**|  | 
 **keyPost** | [**KeyPost**](KeyPost.md)|  | [optional] 

### Return type

[**KeyResponse**](KeyResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

