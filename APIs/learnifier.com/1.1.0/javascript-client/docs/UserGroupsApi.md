# Learnifier.UserGroupsApi

All URIs are relative to *http://learnifier.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgunitsOrgidUsergroupsGet**](UserGroupsApi.md#orgunitsOrgidUsergroupsGet) | **GET** /orgunits/{orgid}/usergroups | List User Groups.
[**orgunitsOrgidUsergroupsGroupidGet**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidGet) | **GET** /orgunits/{orgid}/usergroups/{groupid} | Get user group
[**orgunitsOrgidUsergroupsGroupidMembersGet**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidMembersGet) | **GET** /orgunits/{orgid}/usergroups/{groupid}/members | List of all users in group.
[**orgunitsOrgidUsergroupsGroupidMembersPost**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidMembersPost) | **POST** /orgunits/{orgid}/usergroups/{groupid}/members | Add user group member.
[**orgunitsOrgidUsergroupsGroupidMembersUuidDelete**](UserGroupsApi.md#orgunitsOrgidUsergroupsGroupidMembersUuidDelete) | **DELETE** /orgunits/{orgid}/usergroups/{groupid}/members/{uuid} | Remove user group member.
[**orgunitsOrgidUsergroupsPost**](UserGroupsApi.md#orgunitsOrgidUsergroupsPost) | **POST** /orgunits/{orgid}/usergroups | Create a User Group.



## orgunitsOrgidUsergroupsGet

> [UserGroup] orgunitsOrgidUsergroupsGet(orgid)

List User Groups.

Returns a list of User Groups for the org unit. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UserGroupsApi();
let orgid = 789; // Number | ID of organization
apiInstance.orgunitsOrgidUsergroupsGet(orgid, (error, data, response) => {
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
 **orgid** | **Number**| ID of organization | 

### Return type

[**[UserGroup]**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidUsergroupsGroupidGet

> UserGroup orgunitsOrgidUsergroupsGroupidGet(orgid, groupid)

Get user group

Returns single User Group. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UserGroupsApi();
let orgid = 789; // Number | ID of organization
let groupid = 789; // Number | ID of group
apiInstance.orgunitsOrgidUsergroupsGroupidGet(orgid, groupid, (error, data, response) => {
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
 **orgid** | **Number**| ID of organization | 
 **groupid** | **Number**| ID of group | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidUsergroupsGroupidMembersGet

> [User] orgunitsOrgidUsergroupsGroupidMembersGet(orgid, groupid)

List of all users in group.

Returns a list of all members in User Groups that are based on the Global Group with this groupid. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UserGroupsApi();
let orgid = 789; // Number | ID of organization
let groupid = 789; // Number | ID of group
apiInstance.orgunitsOrgidUsergroupsGroupidMembersGet(orgid, groupid, (error, data, response) => {
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
 **orgid** | **Number**| ID of organization | 
 **groupid** | **Number**| ID of group | 

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidUsergroupsGroupidMembersPost

> UserId orgunitsOrgidUsergroupsGroupidMembersPost(orgid, groupid, body)

Add user group member.

Adds a user to user group. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UserGroupsApi();
let orgid = 789; // Number | ID of organization
let groupid = 789; // Number | ID of group
let body = new Learnifier.AddUserGroupMember(); // AddUserGroupMember | 
apiInstance.orgunitsOrgidUsergroupsGroupidMembersPost(orgid, groupid, body, (error, data, response) => {
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
 **orgid** | **Number**| ID of organization | 
 **groupid** | **Number**| ID of group | 
 **body** | [**AddUserGroupMember**](AddUserGroupMember.md)|  | 

### Return type

[**UserId**](UserId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidUsergroupsGroupidMembersUuidDelete

> orgunitsOrgidUsergroupsGroupidMembersUuidDelete(orgid, groupid, uuid)

Remove user group member.

Removes a user from a user group. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UserGroupsApi();
let orgid = 789; // Number | ID of organization
let groupid = 789; // Number | ID of group
let uuid = "uuid_example"; // String | UUID of user to remove from group.
apiInstance.orgunitsOrgidUsergroupsGroupidMembersUuidDelete(orgid, groupid, uuid, (error, data, response) => {
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
 **orgid** | **Number**| ID of organization | 
 **groupid** | **Number**| ID of group | 
 **uuid** | **String**| UUID of user to remove from group. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidUsergroupsPost

> [GroupId] orgunitsOrgidUsergroupsPost(orgid, body)

Create a User Group.

Create a User Group. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.UserGroupsApi();
let orgid = 789; // Number | ID of organization
let body = new Learnifier.AddUserGroup(); // AddUserGroup | 
apiInstance.orgunitsOrgidUsergroupsPost(orgid, body, (error, data, response) => {
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
 **orgid** | **Number**| ID of organization | 
 **body** | [**AddUserGroup**](AddUserGroup.md)|  | 

### Return type

[**[GroupId]**](GroupId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

