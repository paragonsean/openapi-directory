# AuthOauth.AccessTokensApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOauthV1AccessTokensTokenGet**](AccessTokensApi.md#getOauthV1AccessTokensTokenGet) | **GET** /oauth/v1/access-tokens/{token} | 



## getOauthV1AccessTokensTokenGet

> AccessTokenInfoResponse getOauthV1AccessTokensTokenGet(token)



### Example

```javascript
import AuthOauth from 'auth_oauth';

let apiInstance = new AuthOauth.AccessTokensApi();
let token = "token_example"; // String | 
apiInstance.getOauthV1AccessTokensTokenGet(token, (error, data, response) => {
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

[**AccessTokenInfoResponse**](AccessTokenInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

