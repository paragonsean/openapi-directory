# Gitlab.SessionApi

All URIs are relative to *https://gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postV3Session**](SessionApi.md#postV3Session) | **POST** /v3/session | Login to get token



## postV3Session

> UserWithPrivateToken postV3Session(postV3SessionRequest)

Login to get token

Login to get token

### Example

```javascript
import Gitlab from 'gitlab';
let defaultClient = Gitlab.ApiClient.instance;
// Configure API key authorization: private_token_query
let private_token_query = defaultClient.authentications['private_token_query'];
private_token_query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_query.apiKeyPrefix = 'Token';
// Configure API key authorization: private_token_header
let private_token_header = defaultClient.authentications['private_token_header'];
private_token_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_header.apiKeyPrefix = 'Token';

let apiInstance = new Gitlab.SessionApi();
let postV3SessionRequest = new Gitlab.PostV3SessionRequest(); // PostV3SessionRequest | 
apiInstance.postV3Session(postV3SessionRequest, (error, data, response) => {
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
 **postV3SessionRequest** | [**PostV3SessionRequest**](PostV3SessionRequest.md)|  | 

### Return type

[**UserWithPrivateToken**](UserWithPrivateToken.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

