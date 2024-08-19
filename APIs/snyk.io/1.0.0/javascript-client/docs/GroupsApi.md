# SnykApi.GroupsApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addAMemberToAnOrganizationWithinAGroup**](GroupsApi.md#addAMemberToAnOrganizationWithinAGroup) | **POST** /group/{groupId}/org/{orgId}/members | Add a member to an organization within a group
[**deleteTagFromGroup**](GroupsApi.md#deleteTagFromGroup) | **POST** /group/{groupId}/tags/delete | Delete tag from group
[**listAllMembersInAGroup**](GroupsApi.md#listAllMembersInAGroup) | **GET** /group/{groupId}/members | List all members in a group
[**listAllOrganizationsInAGroup**](GroupsApi.md#listAllOrganizationsInAGroup) | **GET** /group/{groupId}/orgs | List all organizations in a group
[**listAllRolesInAGroup**](GroupsApi.md#listAllRolesInAGroup) | **GET** /group/{groupId}/roles | List all roles in a group
[**listAllTagsInAGroup**](GroupsApi.md#listAllTagsInAGroup) | **GET** /group/{groupId}/tags | List all tags in a group
[**updateGroupSettings**](GroupsApi.md#updateGroupSettings) | **PUT** /group/{groupId}/settings | Update group settings
[**viewGroupSettings**](GroupsApi.md#viewGroupSettings) | **GET** /group/{groupId}/settings | View group settings



## addAMemberToAnOrganizationWithinAGroup

> addAMemberToAnOrganizationWithinAGroup(groupId, orgId, opts)

Add a member to an organization within a group



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID we want to add the member to. The `API_KEY` must have access to this organization.
let opts = {
  'addAMemberToAnOrganizationWithinAGroupRequest': new SnykApi.AddAMemberToAnOrganizationWithinAGroupRequest() // AddAMemberToAnOrganizationWithinAGroupRequest | 
};
apiInstance.addAMemberToAnOrganizationWithinAGroup(groupId, orgId, opts, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | 
 **orgId** | **String**| The organization ID we want to add the member to. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **addAMemberToAnOrganizationWithinAGroupRequest** | [**AddAMemberToAnOrganizationWithinAGroupRequest**](AddAMemberToAnOrganizationWithinAGroupRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteTagFromGroup

> DeleteTagFromGroup200Response deleteTagFromGroup(groupId, opts)

Delete tag from group



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
let opts = {
  'deleteTagFromGroupRequest': new SnykApi.DeleteTagFromGroupRequest() // DeleteTagFromGroupRequest | 
};
apiInstance.deleteTagFromGroup(groupId, opts, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | 
 **deleteTagFromGroupRequest** | [**DeleteTagFromGroupRequest**](DeleteTagFromGroupRequest.md)|  | [optional] 

### Return type

[**DeleteTagFromGroup200Response**](DeleteTagFromGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## listAllMembersInAGroup

> [Object] listAllMembersInAGroup(groupId)

List all members in a group



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
apiInstance.listAllMembersInAGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listAllOrganizationsInAGroup

> listAllOrganizationsInAGroup(groupId, opts)

List all organizations in a group



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "a060a49f-636e-480f-9e14-38e773b2a97f"; // String | The group ID. The `API_KEY` must have READ access to this group and LIST organizations access in this group.
let opts = {
  'perPage': 100, // Number | The number of results to return (maximum is 100).
  'page': 1, // Number | For pagination - offset (from which to start returning results).
  'name': "my" // String | Only organizations that have a name that **starts with** this value (case insensitive) will be returned.
};
apiInstance.listAllOrganizationsInAGroup(groupId, opts, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have READ access to this group and LIST organizations access in this group. | 
 **perPage** | **Number**| The number of results to return (maximum is 100). | [optional] [default to 100]
 **page** | **Number**| For pagination - offset (from which to start returning results). | [optional] 
 **name** | **String**| Only organizations that have a name that **starts with** this value (case insensitive) will be returned. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listAllRolesInAGroup

> listAllRolesInAGroup(groupId)

List all roles in a group



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "a060a49f-636e-480f-9e14-38e773b2a97f"; // String | The group ID. The `API_KEY` must have READ access to this group.
apiInstance.listAllRolesInAGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have READ access to this group. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listAllTagsInAGroup

> ListAllTagsInAGroup200Response listAllTagsInAGroup(groupId, opts)

List all tags in a group



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The group ID. The `API_KEY` must have access admin to this group.
let opts = {
  'perPage': 10, // Number | The number of results to return (the default is 1000).
  'page': 1 // Number | The offset from which to start returning results from.
};
apiInstance.listAllTagsInAGroup(groupId, opts, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access admin to this group. | 
 **perPage** | **Number**| The number of results to return (the default is 1000). | [optional] 
 **page** | **Number**| The offset from which to start returning results from. | [optional] 

### Return type

[**ListAllTagsInAGroup200Response**](ListAllTagsInAGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## updateGroupSettings

> ViewGroupSettings200Response updateGroupSettings(groupId)

Update group settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "groupId_example"; // String | Automatically added
apiInstance.updateGroupSettings(groupId, (error, data, response) => {
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
 **groupId** | **String**| Automatically added | 

### Return type

[**ViewGroupSettings200Response**](ViewGroupSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## viewGroupSettings

> ViewGroupSettings200Response viewGroupSettings(groupId)

View group settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.GroupsApi();
let groupId = "b61bc07c-27c6-42b3-8b04-0f228ed31a67"; // String | The group ID. The `API_KEY` must have admin access to this group.
apiInstance.viewGroupSettings(groupId, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have admin access to this group. | 

### Return type

[**ViewGroupSettings200Response**](ViewGroupSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

