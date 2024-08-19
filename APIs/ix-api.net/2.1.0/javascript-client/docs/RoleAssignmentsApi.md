# IxApi.RoleAssignmentsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roleAssignmentsCreate**](RoleAssignmentsApi.md#roleAssignmentsCreate) | **POST** /role-assignments | 
[**roleAssignmentsDestroy**](RoleAssignmentsApi.md#roleAssignmentsDestroy) | **DELETE** /role-assignments/{assignment_id} | 
[**roleAssignmentsList**](RoleAssignmentsApi.md#roleAssignmentsList) | **GET** /role-assignments | 
[**roleAssignmentsRead**](RoleAssignmentsApi.md#roleAssignmentsRead) | **GET** /role-assignments/{assignment_id} | 



## roleAssignmentsCreate

> RoleAssignment roleAssignmentsCreate(opts)



Assign a &#x60;Role&#x60; to a &#x60;Contact&#x60;.  The contact needs to have all fields filled, which the role requires. If this is not the case a &#x60;400&#x60; &#x60;UnableToFulfill&#x60; will be returned.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.RoleAssignmentsApi();
let opts = {
  'roleAssignmentRequest': new IxApi.RoleAssignmentRequest() // RoleAssignmentRequest | A role assignment request
};
apiInstance.roleAssignmentsCreate(opts, (error, data, response) => {
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
 **roleAssignmentRequest** | [**RoleAssignmentRequest**](RoleAssignmentRequest.md)| A role assignment request | [optional] 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## roleAssignmentsDestroy

> RoleAssignment roleAssignmentsDestroy(assignmentId)



Remove a role assignment from a contact.  If the contact is still in use with a given role required, this will yield an &#x60;UnableToFulfill&#x60; error.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.RoleAssignmentsApi();
let assignmentId = "assignmentId_example"; // String | Get by assignment_id
apiInstance.roleAssignmentsDestroy(assignmentId, (error, data, response) => {
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
 **assignmentId** | **String**| Get by assignment_id | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## roleAssignmentsList

> [RoleAssignment] roleAssignmentsList(opts)



List all role assignments for a contact.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.RoleAssignmentsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'contact': "contact_example", // String | Filter by contact
  'role': "role_example" // String | Filter by role
};
apiInstance.roleAssignmentsList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **contact** | **String**| Filter by contact | [optional] 
 **role** | **String**| Filter by role | [optional] 

### Return type

[**[RoleAssignment]**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## roleAssignmentsRead

> RoleAssignment roleAssignmentsRead(assignmentId)



Get a role assignment for a contact.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.RoleAssignmentsApi();
let assignmentId = "assignmentId_example"; // String | Get by assignment_id
apiInstance.roleAssignmentsRead(assignmentId, (error, data, response) => {
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
 **assignmentId** | **String**| Get by assignment_id | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

