# CleverCloudApi.UsersApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUsersIdApplications_1**](UsersApi.md#getUsersIdApplications_1) | **GET** /users/{id}/applications | 
[**getUsersId_0**](UsersApi.md#getUsersId_0) | **GET** /users/{id} | 
[**getUsersUserIdGitInfo_0**](UsersApi.md#getUsersUserIdGitInfo_0) | **GET** /users/{userId}/git-info | 
[**postUsers_0**](UsersApi.md#postUsers_0) | **POST** /users | 



## getUsersIdApplications_1

> [Application] getUsersIdApplications_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.UsersApi();
let id = "id_example"; // String | 
apiInstance.getUsersIdApplications_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersId_0

> User getUsersId_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.UsersApi();
let id = "id_example"; // String | 
apiInstance.getUsersId_0(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersUserIdGitInfo_0

> getUsersUserIdGitInfo_0(userId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.UsersApi();
let userId = "userId_example"; // String | 
apiInstance.getUsersUserIdGitInfo_0(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUsers_0

> postUsers_0(wannabeUser, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.UsersApi();
let wannabeUser = new CleverCloudApi.WannabeUser(); // WannabeUser | 
let opts = {
  'invitationKey': "invitationKey_example", // String | 
  'addonBetaInvitationKey': "addonBetaInvitationKey_example", // String | 
  'email': "email_example", // String | 
  'pass': "pass_example", // String | 
  'urlNext': "urlNext_example", // String | 
  'terms': "terms_example" // String | 
};
apiInstance.postUsers_0(wannabeUser, opts, (error, data, response) => {
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
 **wannabeUser** | [**WannabeUser**](WannabeUser.md)|  | 
 **invitationKey** | **String**|  | [optional] 
 **addonBetaInvitationKey** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 
 **pass** | **String**|  | [optional] 
 **urlNext** | **String**|  | [optional] 
 **terms** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

