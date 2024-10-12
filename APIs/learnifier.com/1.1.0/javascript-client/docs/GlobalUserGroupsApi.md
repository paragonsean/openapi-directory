# Learnifier.GlobalUserGroupsApi

All URIs are relative to *http://learnifier.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalusergroupsGet**](GlobalUserGroupsApi.md#globalusergroupsGet) | **GET** /globalusergroups | List Global User Groups.
[**globalusergroupsGroupidMembersGet**](GlobalUserGroupsApi.md#globalusergroupsGroupidMembersGet) | **GET** /globalusergroups/{groupid}/members | List of all users in group.



## globalusergroupsGet

> [GlobalUserGroup] globalusergroupsGet()

List Global User Groups.

Returns a list of Global User Groups. Global User Groups are set up for the realm, and will generate groups that can be used on the client level. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.GlobalUserGroupsApi();
apiInstance.globalusergroupsGet((error, data, response) => {
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

[**[GlobalUserGroup]**](GlobalUserGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## globalusergroupsGroupidMembersGet

> [User] globalusergroupsGroupidMembersGet(groupid)

List of all users in group.

Returns a list of all members in User Groups that are based on the Global Group with this groupid. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.GlobalUserGroupsApi();
let groupid = 789; // Number | ID of group
apiInstance.globalusergroupsGroupidMembersGet(groupid, (error, data, response) => {
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
 **groupid** | **Number**| ID of group | 

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

