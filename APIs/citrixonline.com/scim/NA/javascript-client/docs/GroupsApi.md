# Scim.GroupsApi

All URIs are relative to *https://api.citrixonline.com/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroup**](GroupsApi.md#createGroup) | **POST** /Groups | Create Group
[**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /Groups/{groupKey} | Delete Group
[**getGroup**](GroupsApi.md#getGroup) | **GET** /Groups/{groupKey} | Get Group
[**getGroups**](GroupsApi.md#getGroups) | **GET** /Groups | Get Groups
[**replaceGroup**](GroupsApi.md#replaceGroup) | **PUT** /Groups/{groupKey} | Replace Group
[**updateGroup**](GroupsApi.md#updateGroup) | **PATCH** /Groups/{groupKey} | Update Group



## createGroup

> Group createGroup(authorization, body)

Create Group

Creates a new organization group and adds it to the user domain. Member groups and member users must be in the organization. This call requires the role ROLE_ORG_WRITE.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.GroupsApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let body = new Scim.GroupDefinition(); // GroupDefinition | The details of the group to create
apiInstance.createGroup(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **body** | [**GroupDefinition**](GroupDefinition.md)| The details of the group to create | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGroup

> deleteGroup(authorization, groupKey)

Delete Group

Deletes a group from the organization (but not from the account). The group must be in the organization. This call requires the role ROLE_ORG_WRITE.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.GroupsApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let groupKey = 789; // Number | The key of the group to query. The group must be in the organization domain
apiInstance.deleteGroup(authorization, groupKey, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **groupKey** | **Number**| The key of the group to query. The group must be in the organization domain | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGroup

> Group getGroup(authorization, groupKey)

Get Group

Queries group details in the organization domain. This call requires the role ROLE_ORG_READ.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.GroupsApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let groupKey = 789; // Number | The key of the group to query. The group must be in the organization domain
apiInstance.getGroup(authorization, groupKey, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **groupKey** | **Number**| The key of the group to query. The group must be in the organization domain | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroups

> GroupCollection getGroups(authorization, opts)

Get Groups

Queries multiple group identities in the organization domain. Filtering, sorting and pagination are available. This call requires the role ROLE_ORG_READ.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.GroupsApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let opts = {
  'filter': "filter_example" // String |  Without a filter, all groups are returned. The filter parameter must be a properly formed SCIM filter using the operator \"eq\" (equals), \"sw\" (starts with), or \"co\" (contains). The filter works for the displayName attribute. Sorting and pagination are supported. For example, GET /Groups?filter=displayName%20eq%20%22Engineering%22&sortBy=displayName&sortOrder=ascending&count=50&startIndex=51
};
apiInstance.getGroups(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **filter** | **String**|  Without a filter, all groups are returned. The filter parameter must be a properly formed SCIM filter using the operator \&quot;eq\&quot; (equals), \&quot;sw\&quot; (starts with), or \&quot;co\&quot; (contains). The filter works for the displayName attribute. Sorting and pagination are supported. For example, GET /Groups?filter&#x3D;displayName%20eq%20%22Engineering%22&amp;sortBy&#x3D;displayName&amp;sortOrder&#x3D;ascending&amp;count&#x3D;50&amp;startIndex&#x3D;51 | [optional] 

### Return type

[**GroupCollection**](GroupCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replaceGroup

> Group replaceGroup(authorization, groupKey, body)

Replace Group

Updates an existing group. The request must include the full group definition. To modify one or more values without sending the full definition, see \&quot;Update Group\&quot;. Member groups and member users must be in the organization. This call requires the role ROLE_ORG_WRITE.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.GroupsApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let groupKey = 789; // Number | The key of the group to query. The group must be in the organization domain
let body = new Scim.GroupDefinition(); // GroupDefinition | The new group definition
apiInstance.replaceGroup(authorization, groupKey, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **groupKey** | **Number**| The key of the group to query. The group must be in the organization domain | 
 **body** | [**GroupDefinition**](GroupDefinition.md)| The new group definition | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGroup

> Group updateGroup(authorization, groupKey, body)

Update Group

Updates one or more values of an existing group without sending the full definition. Member groups and member users must be in the organization. This call requires the role ROLE_ORG_WRITE.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.GroupsApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
let groupKey = 789; // Number | The key of the group to query. The group must be in the organization domain
let body = new Scim.GroupDefinition(); // GroupDefinition | The group data to update. It is allowed to update one or more values of the group definition
apiInstance.updateGroup(authorization, groupKey, body, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 
 **groupKey** | **Number**| The key of the group to query. The group must be in the organization domain | 
 **body** | [**GroupDefinition**](GroupDefinition.md)| The group data to update. It is allowed to update one or more values of the group definition | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

