# GraphRbacManagementClient.GroupApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsAddMember**](GroupApi.md#groupsAddMember) | **POST** /{tenantID}/groups/{groupObjectId}/$links/members | 
[**groupsCreate**](GroupApi.md#groupsCreate) | **POST** /{tenantID}/groups | 
[**groupsDelete**](GroupApi.md#groupsDelete) | **DELETE** /{tenantID}/groups/{objectId} | 
[**groupsGet**](GroupApi.md#groupsGet) | **GET** /{tenantID}/groups/{objectId} | 
[**groupsGetGroupMembers**](GroupApi.md#groupsGetGroupMembers) | **GET** /{tenantID}/groups/{objectId}/members | 
[**groupsGetMemberGroups**](GroupApi.md#groupsGetMemberGroups) | **POST** /{tenantID}/groups/{objectId}/getMemberGroups | 
[**groupsIsMemberOf**](GroupApi.md#groupsIsMemberOf) | **POST** /{tenantID}/isMemberOf | 
[**groupsList**](GroupApi.md#groupsList) | **GET** /{tenantID}/groups | 
[**groupsRemoveMember**](GroupApi.md#groupsRemoveMember) | **DELETE** /{tenantID}/groups/{groupObjectId}/$links/members/{memberObjectId} | 



## groupsAddMember

> groupsAddMember(groupObjectId, apiVersion, tenantID, groupAddMemberParameters)



Add a member to a group.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let groupObjectId = "groupObjectId_example"; // String | The object ID of the group to which to add the member.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let groupAddMemberParameters = new GraphRbacManagementClient.GroupAddMemberParameters(); // GroupAddMemberParameters | The URL of the member object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
apiInstance.groupsAddMember(groupObjectId, apiVersion, tenantID, groupAddMemberParameters, (error, data, response) => {
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
 **groupObjectId** | **String**| The object ID of the group to which to add the member. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **groupAddMemberParameters** | [**GroupAddMemberParameters**](GroupAddMemberParameters.md)| The URL of the member object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## groupsCreate

> ADGroup groupsCreate(apiVersion, tenantID, groupCreateParameters)



Create a group in the directory.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let groupCreateParameters = new GraphRbacManagementClient.GroupCreateParameters(); // GroupCreateParameters | The parameters for the group to create.
apiInstance.groupsCreate(apiVersion, tenantID, groupCreateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **groupCreateParameters** | [**GroupCreateParameters**](GroupCreateParameters.md)| The parameters for the group to create. | 

### Return type

[**ADGroup**](ADGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## groupsDelete

> groupsDelete(objectId, apiVersion, tenantID)



Delete a group from the directory.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let objectId = "objectId_example"; // String | The object ID of the group to delete.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.groupsDelete(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the group to delete. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsGet

> ADGroup groupsGet(objectId, apiVersion, tenantID)



Gets group information from the directory.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let objectId = "objectId_example"; // String | The object ID of the user for which to get group information.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.groupsGet(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the user for which to get group information. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**ADGroup**](ADGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsGetGroupMembers

> DirectoryObjectListResult groupsGetGroupMembers(objectId, apiVersion, tenantID)



Gets the members of a group.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let objectId = "objectId_example"; // String | The object ID of the group whose members should be retrieved.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.groupsGetGroupMembers(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the group whose members should be retrieved. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**DirectoryObjectListResult**](DirectoryObjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsGetMemberGroups

> GroupGetMemberGroupsResult groupsGetMemberGroups(objectId, apiVersion, tenantID, groupGetMemberGroupsParameters)



Gets a collection of object IDs of groups of which the specified group is a member.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let objectId = "objectId_example"; // String | The object ID of the group for which to get group membership.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let groupGetMemberGroupsParameters = new GraphRbacManagementClient.GroupGetMemberGroupsParameters(); // GroupGetMemberGroupsParameters | Group filtering parameters.
apiInstance.groupsGetMemberGroups(objectId, apiVersion, tenantID, groupGetMemberGroupsParameters, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the group for which to get group membership. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **groupGetMemberGroupsParameters** | [**GroupGetMemberGroupsParameters**](GroupGetMemberGroupsParameters.md)| Group filtering parameters. | 

### Return type

[**GroupGetMemberGroupsResult**](GroupGetMemberGroupsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## groupsIsMemberOf

> CheckGroupMembershipResult groupsIsMemberOf(apiVersion, tenantID, checkGroupMembershipParameters)



Checks whether the specified user, group, contact, or service principal is a direct or transitive member of the specified group.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let checkGroupMembershipParameters = new GraphRbacManagementClient.CheckGroupMembershipParameters(); // CheckGroupMembershipParameters | The check group membership parameters.
apiInstance.groupsIsMemberOf(apiVersion, tenantID, checkGroupMembershipParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **checkGroupMembershipParameters** | [**CheckGroupMembershipParameters**](CheckGroupMembershipParameters.md)| The check group membership parameters. | 

### Return type

[**CheckGroupMembershipResult**](CheckGroupMembershipResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## groupsList

> GroupListResult groupsList(apiVersion, tenantID, opts)



Gets list of groups for the current tenant.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let opts = {
  'filter': "filter_example" // String | The filter to apply to the operation.
};
apiInstance.groupsList(apiVersion, tenantID, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **filter** | **String**| The filter to apply to the operation. | [optional] 

### Return type

[**GroupListResult**](GroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsRemoveMember

> groupsRemoveMember(groupObjectId, memberObjectId, apiVersion, tenantID)



Remove a member from a group.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupApi();
let groupObjectId = "groupObjectId_example"; // String | The object ID of the group from which to remove the member.
let memberObjectId = "memberObjectId_example"; // String | Member object id
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.groupsRemoveMember(groupObjectId, memberObjectId, apiVersion, tenantID, (error, data, response) => {
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
 **groupObjectId** | **String**| The object ID of the group from which to remove the member. | 
 **memberObjectId** | **String**| Member object id | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

