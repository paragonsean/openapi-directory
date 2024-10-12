# SnykApi.OrganizationsApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createANewOrganization**](OrganizationsApi.md#createANewOrganization) | **POST** /org | Create a new organization
[**deletePendingUserProvision**](OrganizationsApi.md#deletePendingUserProvision) | **DELETE** /org/{orgId}/provision | Delete pending user provision
[**inviteUsers**](OrganizationsApi.md#inviteUsers) | **POST** /org/{orgId}/invite | Invite users
[**listAllTheOrganizationsAUserBelongsTo**](OrganizationsApi.md#listAllTheOrganizationsAUserBelongsTo) | **GET** /orgs | List all the organizations a user belongs to
[**listMembers**](OrganizationsApi.md#listMembers) | **GET** /org/{orgId}/members | List Members
[**listPendingUserProvisions**](OrganizationsApi.md#listPendingUserProvisions) | **GET** /org/{orgId}/provision | List pending user provisions
[**orgOrgIdNotificationSettingsGet**](OrganizationsApi.md#orgOrgIdNotificationSettingsGet) | **GET** /org/{orgId}/notification-settings | Get organization notification settings
[**provisionAUserToTheOrganization**](OrganizationsApi.md#provisionAUserToTheOrganization) | **POST** /org/{orgId}/provision | Provision a user to the organization
[**removeAMemberFromTheOrganization**](OrganizationsApi.md#removeAMemberFromTheOrganization) | **DELETE** /org/{orgId}/members/{userId} | Remove a member from the organization
[**removeOrganization**](OrganizationsApi.md#removeOrganization) | **DELETE** /org/{orgId} | Remove organization
[**setNotificationSettings**](OrganizationsApi.md#setNotificationSettings) | **PUT** /org/{orgId}/notification-settings | Set notification settings
[**updateAMemberInTheOrganization**](OrganizationsApi.md#updateAMemberInTheOrganization) | **PUT** /org/{orgId}/members/{userId} | Update a member in the organization
[**updateAMembersRoleInTheOrganization**](OrganizationsApi.md#updateAMembersRoleInTheOrganization) | **PUT** /org/{orgId}/members/update/{userId} | Update a member&#39;s role in the organization
[**updateOrganizationSettings**](OrganizationsApi.md#updateOrganizationSettings) | **PUT** /org/{orgId}/settings | Update organization settings
[**viewOrganizationSettings**](OrganizationsApi.md#viewOrganizationSettings) | **GET** /org/{orgId}/settings | View organization settings



## createANewOrganization

> createANewOrganization(opts)

Create a new organization



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let opts = {
  'createANewOrganizationRequest': new SnykApi.CreateANewOrganizationRequest() // CreateANewOrganizationRequest | 
};
apiInstance.createANewOrganization(opts, (error, data, response) => {
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
 **createANewOrganizationRequest** | [**CreateANewOrganizationRequest**](CreateANewOrganizationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8, application/json, charset=utf-8


## deletePendingUserProvision

> DeletePendingUserProvision200Response deletePendingUserProvision(orgId)

Delete pending user provision



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID.
apiInstance.deletePendingUserProvision(orgId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. | 

### Return type

[**DeletePendingUserProvision200Response**](DeletePendingUserProvision200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## inviteUsers

> inviteUsers(orgId, opts)

Invite users



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let opts = {
  'inviteUsersRequest': new SnykApi.InviteUsersRequest() // InviteUsersRequest | 
};
apiInstance.inviteUsers(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **inviteUsersRequest** | [**InviteUsersRequest**](InviteUsersRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listAllTheOrganizationsAUserBelongsTo

> listAllTheOrganizationsAUserBelongsTo()

List all the organizations a user belongs to



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
apiInstance.listAllTheOrganizationsAUserBelongsTo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listMembers

> [Object] listMembers(orgId, opts)

List Members



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID.
let opts = {
  'includeGroupAdmins': true // Boolean | Include group administrators who also have access to this organization.
};
apiInstance.listMembers(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. | 
 **includeGroupAdmins** | **Boolean**| Include group administrators who also have access to this organization. | [optional] [default to false]

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listPendingUserProvisions

> [Object] listPendingUserProvisions(orgId)

List pending user provisions



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID.
apiInstance.listPendingUserProvisions(orgId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. | 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## orgOrgIdNotificationSettingsGet

> OrgOrgIdNotificationSettingsGet200Response orgOrgIdNotificationSettingsGet(orgId)

Get organization notification settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
apiInstance.orgOrgIdNotificationSettingsGet(orgId, (error, data, response) => {
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


## provisionAUserToTheOrganization

> ProvisionAUserToTheOrganization200Response provisionAUserToTheOrganization(orgId, opts)

Provision a user to the organization



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID. The `API_KEY` must not exceed the permissions being granted to the provisioned user.
let opts = {
  'provisionAUserToTheOrganizationRequest': new SnykApi.ProvisionAUserToTheOrganizationRequest() // ProvisionAUserToTheOrganizationRequest | 
};
apiInstance.provisionAUserToTheOrganization(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must not exceed the permissions being granted to the provisioned user. | 
 **provisionAUserToTheOrganizationRequest** | [**ProvisionAUserToTheOrganizationRequest**](ProvisionAUserToTheOrganizationRequest.md)|  | [optional] 

### Return type

[**ProvisionAUserToTheOrganization200Response**](ProvisionAUserToTheOrganization200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## removeAMemberFromTheOrganization

> removeAMemberFromTheOrganization(orgId, userId)

Remove a member from the organization



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must admin have access to this organization.
let userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The user ID we want to remove.
apiInstance.removeAMemberFromTheOrganization(orgId, userId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must admin have access to this organization. | 
 **userId** | **String**| The user ID we want to remove. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeOrganization

> removeOrganization(orgId)

Remove organization



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have permission to delete the provided organization. Currently this operation is only supported for organizations without any projects.
apiInstance.removeOrganization(orgId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have permission to delete the provided organization. Currently this operation is only supported for organizations without any projects. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setNotificationSettings

> OrgOrgIdNotificationSettingsGet200Response setNotificationSettings(orgId, opts)

Set notification settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "orgId_example"; // String | Automatically added
let opts = {
  'setNotificationSettingsRequest': new SnykApi.SetNotificationSettingsRequest() // SetNotificationSettingsRequest | 
};
apiInstance.setNotificationSettings(orgId, opts, (error, data, response) => {
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


## updateAMemberInTheOrganization

> updateAMemberInTheOrganization(orgId, userId, opts)

Update a member in the organization



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The user ID.
let opts = {
  'updateAMemberInTheOrganizationRequest': new SnykApi.UpdateAMemberInTheOrganizationRequest() // UpdateAMemberInTheOrganizationRequest | 
};
apiInstance.updateAMemberInTheOrganization(orgId, userId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **userId** | **String**| The user ID. | 
 **updateAMemberInTheOrganizationRequest** | [**UpdateAMemberInTheOrganizationRequest**](UpdateAMemberInTheOrganizationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateAMembersRoleInTheOrganization

> updateAMembersRoleInTheOrganization(orgId, userId, opts)

Update a member&#39;s role in the organization



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The user ID.
let opts = {
  'updateAMemberSRoleInTheOrganizationRequest': new SnykApi.UpdateAMemberSRoleInTheOrganizationRequest() // UpdateAMemberSRoleInTheOrganizationRequest | 
};
apiInstance.updateAMembersRoleInTheOrganization(orgId, userId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **userId** | **String**| The user ID. | 
 **updateAMemberSRoleInTheOrganizationRequest** | [**UpdateAMemberSRoleInTheOrganizationRequest**](UpdateAMemberSRoleInTheOrganizationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationSettings

> ViewOrganizationSettings200Response updateOrganizationSettings(orgId, opts)

Update organization settings

Settings that are not provided will not be modified.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let opts = {
  'updateOrganizationSettingsRequest': new SnykApi.UpdateOrganizationSettingsRequest() // UpdateOrganizationSettingsRequest | 
};
apiInstance.updateOrganizationSettings(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **updateOrganizationSettingsRequest** | [**UpdateOrganizationSettingsRequest**](UpdateOrganizationSettingsRequest.md)|  | [optional] 

### Return type

[**ViewOrganizationSettings200Response**](ViewOrganizationSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## viewOrganizationSettings

> ViewOrganizationSettings200Response viewOrganizationSettings(orgId)

View organization settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.OrganizationsApi();
let orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID. The `API_KEY` must have access to this organization.
apiInstance.viewOrganizationSettings(orgId, (error, data, response) => {
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

[**ViewOrganizationSettings200Response**](ViewOrganizationSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

