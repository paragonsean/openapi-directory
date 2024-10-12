# DiscourseApiDocumentation.GroupsApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addGroupMembers**](GroupsApi.md#addGroupMembers) | **PUT** /groups/{id}/members.json | Add group members
[**createGroup**](GroupsApi.md#createGroup) | **POST** /admin/groups.json | Create a group
[**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /admin/groups/{id}.json | Delete a group
[**getGroup**](GroupsApi.md#getGroup) | **GET** /groups/{id}.json | Get a group
[**listGroupMembers**](GroupsApi.md#listGroupMembers) | **GET** /groups/{id}/members.json | List group members
[**listGroups**](GroupsApi.md#listGroups) | **GET** /groups.json | List groups
[**removeGroupMembers**](GroupsApi.md#removeGroupMembers) | **DELETE** /groups/{id}/members.json | Remove group members
[**updateGroup**](GroupsApi.md#updateGroup) | **PUT** /groups/{id}.json | Update a group



## addGroupMembers

> AddGroupMembers200Response addGroupMembers(id, opts)

Add group members

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
let id = 56; // Number | 
let opts = {
  'addGroupMembersRequest': new DiscourseApiDocumentation.AddGroupMembersRequest() // AddGroupMembersRequest | 
};
apiInstance.addGroupMembers(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **addGroupMembersRequest** | [**AddGroupMembersRequest**](AddGroupMembersRequest.md)|  | [optional] 

### Return type

[**AddGroupMembers200Response**](AddGroupMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGroup

> CreateGroup200Response createGroup(opts)

Create a group

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
let opts = {
  'createGroupRequest': new DiscourseApiDocumentation.CreateGroupRequest() // CreateGroupRequest | 
};
apiInstance.createGroup(opts, (error, data, response) => {
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
 **createGroupRequest** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | [optional] 

### Return type

[**CreateGroup200Response**](CreateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGroup

> DeleteGroup200Response deleteGroup(id)

Delete a group

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
let id = 56; // Number | 
apiInstance.deleteGroup(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroup

> GetGroup200Response getGroup(id)

Get a group

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
let id = "name"; // String | Use group name instead of id
apiInstance.getGroup(id, (error, data, response) => {
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
 **id** | **String**| Use group name instead of id | 

### Return type

[**GetGroup200Response**](GetGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGroupMembers

> ListGroupMembers200Response listGroupMembers(id)

List group members

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
let id = "name"; // String | Use group name instead of id
apiInstance.listGroupMembers(id, (error, data, response) => {
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
 **id** | **String**| Use group name instead of id | 

### Return type

[**ListGroupMembers200Response**](ListGroupMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGroups

> ListGroups200Response listGroups()

List groups

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
apiInstance.listGroups((error, data, response) => {
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

[**ListGroups200Response**](ListGroups200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeGroupMembers

> RemoveGroupMembers200Response removeGroupMembers(id, opts)

Remove group members

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
let id = 56; // Number | 
let opts = {
  'addGroupMembersRequest': new DiscourseApiDocumentation.AddGroupMembersRequest() // AddGroupMembersRequest | 
};
apiInstance.removeGroupMembers(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **addGroupMembersRequest** | [**AddGroupMembersRequest**](AddGroupMembersRequest.md)|  | [optional] 

### Return type

[**RemoveGroupMembers200Response**](RemoveGroupMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGroup

> UpdateGroup200Response updateGroup(id, opts)

Update a group

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.GroupsApi();
let id = 56; // Number | 
let opts = {
  'updateGroupRequest': new DiscourseApiDocumentation.UpdateGroupRequest() // UpdateGroupRequest | 
};
apiInstance.updateGroup(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **updateGroupRequest** | [**UpdateGroupRequest**](UpdateGroupRequest.md)|  | [optional] 

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

