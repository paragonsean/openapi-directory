# ForemApiV1.ProfileImagesApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProfileImage**](ProfileImagesApi.md#getProfileImage) | **GET** /api/profile_images/{username} | A Users or organizations profile image



## getProfileImage

> [ProfileImage] getProfileImage(username)

A Users or organizations profile image

This endpoint allows the client to retrieve a user or organization profile image information by its         corresponding username.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.ProfileImagesApi();
let username = "janedoe"; // String | The parameter is the username of the user or the username of the organization.
apiInstance.getProfileImage(username, (error, data, response) => {
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
 **username** | **String**| The parameter is the username of the user or the username of the organization. | 

### Return type

[**[ProfileImage]**](ProfileImage.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

