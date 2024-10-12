# AuthOauth.TokensApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postOauthV1TokenCreate**](TokensApi.md#postOauthV1TokenCreate) | **POST** /oauth/v1/token | 



## postOauthV1TokenCreate

> TokenResponseIF postOauthV1TokenCreate(opts)



### Example

```javascript
import AuthOauth from 'auth_oauth';

let apiInstance = new AuthOauth.TokensApi();
let opts = {
  'clientId': "clientId_example", // String | 
  'clientSecret': "clientSecret_example", // String | 
  'code': "code_example", // String | 
  'grantType': "grantType_example", // String | 
  'redirectUri': "redirectUri_example", // String | 
  'refreshToken': "refreshToken_example" // String | 
};
apiInstance.postOauthV1TokenCreate(opts, (error, data, response) => {
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
 **clientId** | **String**|  | [optional] 
 **clientSecret** | **String**|  | [optional] 
 **code** | **String**|  | [optional] 
 **grantType** | **String**|  | [optional] 
 **redirectUri** | **String**|  | [optional] 
 **refreshToken** | **String**|  | [optional] 

### Return type

[**TokenResponseIF**](TokenResponseIF.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, */*

