# ApicurioRegistryApiV2.GroupsApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroup**](GroupsApi.md#createGroup) | **POST** /groups | Create a new group
[**deleteGroupById**](GroupsApi.md#deleteGroupById) | **DELETE** /groups/{groupId} | Delete a group by the specified ID.
[**getGroupById**](GroupsApi.md#getGroupById) | **GET** /groups/{groupId} | Get a group by the specified ID.
[**listGroups**](GroupsApi.md#listGroups) | **GET** /groups | List groups



## createGroup

> GroupMetaData createGroup(createGroupMetaData)

Create a new group

Creates a new group.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) * The group already exist (HTTP error &#x60;409&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.GroupsApi();
let createGroupMetaData = new ApicurioRegistryApiV2.CreateGroupMetaData(); // CreateGroupMetaData | 
apiInstance.createGroup(createGroupMetaData, (error, data, response) => {
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
 **createGroupMetaData** | [**CreateGroupMetaData**](CreateGroupMetaData.md)|  | 

### Return type

[**GroupMetaData**](GroupMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGroupById

> deleteGroupById(groupId)

Delete a group by the specified ID.

Deletes a group by identifier.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) * The group does not exist (HTTP error &#x60;404&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.GroupsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
apiInstance.deleteGroupById(groupId, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupById

> GroupMetaData getGroupById(groupId)

Get a group by the specified ID.

Returns a group using the specified id.  This operation can fail for the following reasons:  * No group exists with the specified ID (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.GroupsApi();
let groupId = "groupId_example"; // String | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
apiInstance.getGroupById(groupId, (error, data, response) => {
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
 **groupId** | **String**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. | 

### Return type

[**GroupMetaData**](GroupMetaData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGroups

> GroupSearchResults listGroups(opts)

List groups

Returns a list of all groups.  This list is paged.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.GroupsApi();
let opts = {
  'limit': 56, // Number | The number of groups to return.  Defaults to 20.
  'offset': 56, // Number | The number of groups to skip before starting the result set.  Defaults to 0.
  'order': new ApicurioRegistryApiV2.SortOrder(), // SortOrder | Sort order, ascending (`asc`) or descending (`desc`).
  'orderby': new ApicurioRegistryApiV2.SortBy() // SortBy | The field to sort by.  Can be one of:  * `name` * `createdOn` 
};
apiInstance.listGroups(opts, (error, data, response) => {
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
 **limit** | **Number**| The number of groups to return.  Defaults to 20. | [optional] 
 **offset** | **Number**| The number of groups to skip before starting the result set.  Defaults to 0. | [optional] 
 **order** | [**SortOrder**](.md)| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] 
 **orderby** | [**SortBy**](.md)| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] 

### Return type

[**GroupSearchResults**](GroupSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

