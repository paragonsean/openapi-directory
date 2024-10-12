# GraphRbacManagementClient.UserApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersCreate**](UserApi.md#usersCreate) | **POST** /{tenantID}/users | 
[**usersDelete**](UserApi.md#usersDelete) | **DELETE** /{tenantID}/users/{upnOrObjectId} | 
[**usersGet**](UserApi.md#usersGet) | **GET** /{tenantID}/users/{upnOrObjectId} | 
[**usersGetMemberGroups**](UserApi.md#usersGetMemberGroups) | **POST** /{tenantID}/users/{objectId}/getMemberGroups | 
[**usersList**](UserApi.md#usersList) | **GET** /{tenantID}/users | 
[**usersUpdate**](UserApi.md#usersUpdate) | **PATCH** /{tenantID}/users/{upnOrObjectId} | 



## usersCreate

> User usersCreate(apiVersion, tenantID, userCreateParameters)



Create a new user.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.UserApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let userCreateParameters = new GraphRbacManagementClient.UserCreateParameters(); // UserCreateParameters | Parameters to create a user.
apiInstance.usersCreate(apiVersion, tenantID, userCreateParameters, (error, data, response) => {
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
 **userCreateParameters** | [**UserCreateParameters**](UserCreateParameters.md)| Parameters to create a user. | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## usersDelete

> usersDelete(upnOrObjectId, apiVersion, tenantID)



Delete a user.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.UserApi();
let upnOrObjectId = "upnOrObjectId_example"; // String | The object ID or principal name of the user to delete.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.usersDelete(upnOrObjectId, apiVersion, tenantID, (error, data, response) => {
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
 **upnOrObjectId** | **String**| The object ID or principal name of the user to delete. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## usersGet

> User usersGet(upnOrObjectId, apiVersion, tenantID)



Gets user information from the directory.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.UserApi();
let upnOrObjectId = "upnOrObjectId_example"; // String | The object ID or principal name of the user for which to get information.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.usersGet(upnOrObjectId, apiVersion, tenantID, (error, data, response) => {
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
 **upnOrObjectId** | **String**| The object ID or principal name of the user for which to get information. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## usersGetMemberGroups

> UserGetMemberGroupsResult usersGetMemberGroups(objectId, apiVersion, tenantID, userGetMemberGroupsParameters)



Gets a collection that contains the object IDs of the groups of which the user is a member.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.UserApi();
let objectId = "objectId_example"; // String | The object ID of the user for which to get group membership.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let userGetMemberGroupsParameters = new GraphRbacManagementClient.UserGetMemberGroupsParameters(); // UserGetMemberGroupsParameters | User filtering parameters.
apiInstance.usersGetMemberGroups(objectId, apiVersion, tenantID, userGetMemberGroupsParameters, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the user for which to get group membership. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **userGetMemberGroupsParameters** | [**UserGetMemberGroupsParameters**](UserGetMemberGroupsParameters.md)| User filtering parameters. | 

### Return type

[**UserGetMemberGroupsResult**](UserGetMemberGroupsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## usersList

> UserListResult usersList(apiVersion, tenantID, opts)



Gets list of users for the current tenant.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.UserApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let opts = {
  'filter': "filter_example", // String | The filter to apply to the operation.
  'expand': "expand_example", // String | The expand value for the operation result.
  'top': 100 // Number | (Optional) Set the maximum number of results per response.
};
apiInstance.usersList(apiVersion, tenantID, opts, (error, data, response) => {
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
 **expand** | **String**| The expand value for the operation result. | [optional] 
 **top** | **Number**| (Optional) Set the maximum number of results per response. | [optional] [default to 100]

### Return type

[**UserListResult**](UserListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## usersUpdate

> usersUpdate(upnOrObjectId, apiVersion, tenantID, userUpdateParameters)



Updates a user.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.UserApi();
let upnOrObjectId = "upnOrObjectId_example"; // String | The object ID or principal name of the user to update.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let userUpdateParameters = new GraphRbacManagementClient.UserUpdateParameters(); // UserUpdateParameters | Parameters to update an existing user.
apiInstance.usersUpdate(upnOrObjectId, apiVersion, tenantID, userUpdateParameters, (error, data, response) => {
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
 **upnOrObjectId** | **String**| The object ID or principal name of the user to update. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **userUpdateParameters** | [**UserUpdateParameters**](UserUpdateParameters.md)| Parameters to update an existing user. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

