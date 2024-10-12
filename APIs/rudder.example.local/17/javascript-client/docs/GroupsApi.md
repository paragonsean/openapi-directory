# RudderApi.GroupsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroup**](GroupsApi.md#createGroup) | **PUT** /groups | Create a group
[**createGroupCategory**](GroupsApi.md#createGroupCategory) | **PUT** /groups/categories | Create a group category
[**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /groups/{groupId} | Delete a group
[**deleteGroupCategory**](GroupsApi.md#deleteGroupCategory) | **DELETE** /groups/categories/{groupCategoryId} | Delete group category
[**getGroupCategoryDetails**](GroupsApi.md#getGroupCategoryDetails) | **GET** /groups/categories/{groupCategoryId} | Get group category details
[**getGroupTree**](GroupsApi.md#getGroupTree) | **GET** /groups/tree | Get groups tree
[**groupDetails**](GroupsApi.md#groupDetails) | **GET** /groups/{groupId} | Get group details
[**listGroups**](GroupsApi.md#listGroups) | **GET** /groups | List all groups
[**reloadGroup**](GroupsApi.md#reloadGroup) | **POST** /groups/{groupId}/reload | Reload a group
[**updateGroup**](GroupsApi.md#updateGroup) | **POST** /groups/{groupId} | Update group details
[**updateGroupCategory**](GroupsApi.md#updateGroupCategory) | **POST** /groups/categories/{groupCategoryId} | Update group category details



## createGroup

> CreateGroup200Response createGroup(opts)

Create a group

Create a new group based in provided parameters

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let opts = {
  'groupNew': new RudderApi.GroupNew() // GroupNew | 
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
 **groupNew** | [**GroupNew**](GroupNew.md)|  | [optional] 

### Return type

[**CreateGroup200Response**](CreateGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGroupCategory

> CreateGroupCategory200Response createGroupCategory(groupCategory)

Create a group category

Create a new group category

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupCategory = new RudderApi.GroupCategory(); // GroupCategory | 
apiInstance.createGroupCategory(groupCategory, (error, data, response) => {
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
 **groupCategory** | [**GroupCategory**](GroupCategory.md)|  | 

### Return type

[**CreateGroupCategory200Response**](CreateGroupCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGroup

> DeleteGroup200Response deleteGroup(groupId)

Delete a group

Update detailed information about a group

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the group
apiInstance.deleteGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| Id of the group | 

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGroupCategory

> DeleteGroupCategory200Response deleteGroupCategory(groupCategoryId)

Delete group category

Delete a group category. It must have no child groups and no children categories.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupCategoryId = "e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"; // String | 
apiInstance.deleteGroupCategory(groupCategoryId, (error, data, response) => {
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
 **groupCategoryId** | **String**|  | 

### Return type

[**DeleteGroupCategory200Response**](DeleteGroupCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupCategoryDetails

> GetGroupCategoryDetails200Response getGroupCategoryDetails(groupCategoryId)

Get group category details

Get detailed information about a group category

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupCategoryId = "e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"; // String | 
apiInstance.getGroupCategoryDetails(groupCategoryId, (error, data, response) => {
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
 **groupCategoryId** | **String**|  | 

### Return type

[**GetGroupCategoryDetails200Response**](GetGroupCategoryDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupTree

> GetGroupTree200Response getGroupTree()

Get groups tree

Get all available groups and their categories in a tree

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
apiInstance.getGroupTree((error, data, response) => {
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

[**GetGroupTree200Response**](GetGroupTree200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupDetails

> GroupDetails200Response groupDetails(groupId)

Get group details

Get detailed information about a group

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the group
apiInstance.groupDetails(groupId, (error, data, response) => {
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
 **groupId** | **String**| Id of the group | 

### Return type

[**GroupDetails200Response**](GroupDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGroups

> ListGroups200Response listGroups()

List all groups

List all groups

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
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

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadGroup

> ReloadGroup200Response reloadGroup(groupId)

Reload a group

Recompute the content of a group

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the group
apiInstance.reloadGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| Id of the group | 

### Return type

[**ReloadGroup200Response**](ReloadGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateGroup

> UpdateGroup200Response updateGroup(groupId, groupUpdate)

Update group details

Update detailed information about a group

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the group
let groupUpdate = new RudderApi.GroupUpdate(); // GroupUpdate | 
apiInstance.updateGroup(groupId, groupUpdate, (error, data, response) => {
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
 **groupId** | **String**| Id of the group | 
 **groupUpdate** | [**GroupUpdate**](GroupUpdate.md)|  | 

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGroupCategory

> UpdateGroupCategory200Response updateGroupCategory(groupCategoryId, groupCategoryUpdate)

Update group category details

Update detailed information about a group category

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.GroupsApi();
let groupCategoryId = "e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"; // String | 
let groupCategoryUpdate = new RudderApi.GroupCategoryUpdate(); // GroupCategoryUpdate | 
apiInstance.updateGroupCategory(groupCategoryId, groupCategoryUpdate, (error, data, response) => {
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
 **groupCategoryId** | **String**|  | 
 **groupCategoryUpdate** | [**GroupCategoryUpdate**](GroupCategoryUpdate.md)|  | 

### Return type

[**UpdateGroupCategory200Response**](UpdateGroupCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

