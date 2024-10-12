# SnykApi.UsersApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMyDetails**](UsersApi.md#getMyDetails) | **GET** /user/me | Get My Details
[**getOrganizationNotificationSettings**](UsersApi.md#getOrganizationNotificationSettings) | **GET** /user/me/notification-settings/org/{orgId} | Get organization notification settings
[**getProjectNotificationSettings**](UsersApi.md#getProjectNotificationSettings) | **GET** /user/me/notification-settings/org/{orgId}/project/{projectId} | Get project notification settings
[**getUserDetails**](UsersApi.md#getUserDetails) | **GET** /user/{userId} | Get User Details
[**modifyOrganizationNotificationSettings**](UsersApi.md#modifyOrganizationNotificationSettings) | **PUT** /user/me/notification-settings/org/{orgId} | Modify organization notification settings
[**modifyProjectNotificationSettings**](UsersApi.md#modifyProjectNotificationSettings) | **PUT** /user/me/notification-settings/org/{orgId}/project/{projectId} | Modify project notification settings



## getMyDetails

> GetMyDetails200Response getMyDetails()

Get My Details



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.UsersApi();
apiInstance.getMyDetails((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMyDetails200Response**](GetMyDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getOrganizationNotificationSettings

> OrgOrgIdNotificationSettingsGet200Response getOrganizationNotificationSettings(orgId)

Get organization notification settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.UsersApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
apiInstance.getOrganizationNotificationSettings(orgId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 

### Return type

[**OrgOrgIdNotificationSettingsGet200Response**](OrgOrgIdNotificationSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getProjectNotificationSettings

> OrgOrgIdNotificationSettingsGet200Response getProjectNotificationSettings(orgId, projectId)

Get project notification settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.UsersApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return notification settings for.
apiInstance.getProjectNotificationSettings(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to return notification settings for. | 

### Return type

[**OrgOrgIdNotificationSettingsGet200Response**](OrgOrgIdNotificationSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getUserDetails

> GetUserDetails200Response getUserDetails(userId)

Get User Details



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.UsersApi();
let userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The users ID. The `API_KEY` must have admin access to at least one group or organization where the requested user is a member and must have the `api` entitlement on their preferred organization.
apiInstance.getUserDetails(userId, (error, data, response) => {
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
 **userId** | **String**| The users ID. The &#x60;API_KEY&#x60; must have admin access to at least one group or organization where the requested user is a member and must have the &#x60;api&#x60; entitlement on their preferred organization. | 

### Return type

[**GetUserDetails200Response**](GetUserDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## modifyOrganizationNotificationSettings

> OrgOrgIdNotificationSettingsGet200Response modifyOrganizationNotificationSettings(orgId, opts)

Modify organization notification settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.UsersApi();
let orgId = "orgId_example"; // String | Automatically added
let opts = {
  'setNotificationSettingsRequest': new SnykApi.SetNotificationSettingsRequest() // SetNotificationSettingsRequest | 
};
apiInstance.modifyOrganizationNotificationSettings(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **setNotificationSettingsRequest** | [**SetNotificationSettingsRequest**](SetNotificationSettingsRequest.md)|  | [optional] 

### Return type

[**OrgOrgIdNotificationSettingsGet200Response**](OrgOrgIdNotificationSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## modifyProjectNotificationSettings

> modifyProjectNotificationSettings(orgId, projectId, opts)

Modify project notification settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.UsersApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
let opts = {
  'modifyProjectNotificationSettingsRequest': new SnykApi.ModifyProjectNotificationSettingsRequest() // ModifyProjectNotificationSettingsRequest | 
};
apiInstance.modifyProjectNotificationSettings(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 
 **modifyProjectNotificationSettingsRequest** | [**ModifyProjectNotificationSettingsRequest**](ModifyProjectNotificationSettingsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

