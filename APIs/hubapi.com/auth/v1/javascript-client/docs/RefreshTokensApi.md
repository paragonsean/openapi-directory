# AuthOauth.RefreshTokensApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteOauthV1RefreshTokensTokenArchive**](RefreshTokensApi.md#deleteOauthV1RefreshTokensTokenArchive) | **DELETE** /oauth/v1/refresh-tokens/{token} | 
[**getOauthV1RefreshTokensTokenGet**](RefreshTokensApi.md#getOauthV1RefreshTokensTokenGet) | **GET** /oauth/v1/refresh-tokens/{token} | 



## deleteOauthV1RefreshTokensTokenArchive

> deleteOauthV1RefreshTokensTokenArchive(token)



### Example

```javascript
import AuthOauth from 'auth_oauth';

let apiInstance = new AuthOauth.RefreshTokensApi();
let token = "token_example"; // String | 
apiInstance.deleteOauthV1RefreshTokensTokenArchive(token, (error, data, response) => {
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
 **token** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOauthV1RefreshTokensTokenGet

> RefreshTokenInfoResponse getOauthV1RefreshTokensTokenGet(token)



### Example

```javascript
import AuthOauth from 'auth_oauth';

let apiInstance = new AuthOauth.RefreshTokensApi();
let token = "token_example"; // String | 
apiInstance.getOauthV1RefreshTokensTokenGet(token, (error, data, response) => {
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
 **token** | **String**|  | 

### Return type

[**RefreshTokenInfoResponse**](RefreshTokenInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

