# PendoFeedbackApi.TeamApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersInviteVendorUserPost_0**](TeamApi.md#usersInviteVendorUserPost_0) | **POST** /users/invite_vendor_user | Invite a VendorUser (Team member)
[**vendorUsersPost_0**](TeamApi.md#vendorUsersPost_0) | **POST** /vendor_users | Create or update a team member by their external_id



## usersInviteVendorUserPost_0

> usersInviteVendorUserPost_0(data)

Invite a VendorUser (Team member)

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.TeamApi();
let data = new PendoFeedbackApi.UsersInviteVendorUserPostRequest(); // UsersInviteVendorUserPostRequest | 
apiInstance.usersInviteVendorUserPost_0(data, (error, data, response) => {
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
 **data** | [**UsersInviteVendorUserPostRequest**](UsersInviteVendorUserPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## vendorUsersPost_0

> vendorUsersPost_0(data)

Create or update a team member by their external_id

the POST /vendor_users is very similar to the POST /users/invite_vendor_user but /vendor_users is intended for consumers to refresh team member data periodically, rather than just a one-off user creation.

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.TeamApi();
let data = new PendoFeedbackApi.VendorUsersPostRequest(); // VendorUsersPostRequest | 
apiInstance.vendorUsersPost_0(data, (error, data, response) => {
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
 **data** | [**VendorUsersPostRequest**](VendorUsersPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

