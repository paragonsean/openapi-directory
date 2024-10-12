# BotifyApi.UserApi

All URIs are relative to *https://api.botify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserProjects**](UserApi.md#getUserProjects) | **GET** /projects/{username} | List all active projects for the user



## getUserProjects

> GetUserProjects200Response getUserProjects(username, opts)

List all active projects for the user

List all active projects for the user

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.UserApi();
let username = "username_example"; // String | User's identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getUserProjects(username, opts, (error, data, response) => {
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
 **username** | **String**| User&#39;s identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetUserProjects200Response**](GetUserProjects200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

