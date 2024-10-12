# BlueprintClient.AssignmentOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignmentOperationsGet**](AssignmentOperationsApi.md#assignmentOperationsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName}/assignmentOperations/{assignmentOperationName} | 
[**assignmentOperationsList**](AssignmentOperationsApi.md#assignmentOperationsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName}/assignmentOperations | 



## assignmentOperationsGet

> AssignmentOperation assignmentOperationsGet(apiVersion, scope, assignmentName, assignmentOperationName)



Get a blueprint assignment operation.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.AssignmentOperationsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
let assignmentOperationName = "assignmentOperationName_example"; // String | Name of the blueprint assignment operation.
apiInstance.assignmentOperationsGet(apiVersion, scope, assignmentName, assignmentOperationName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | 
 **assignmentName** | **String**| Name of the blueprint assignment. | 
 **assignmentOperationName** | **String**| Name of the blueprint assignment operation. | 

### Return type

[**AssignmentOperation**](AssignmentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assignmentOperationsList

> AssignmentOperationList assignmentOperationsList(apiVersion, scope, assignmentName)



List operations for given blueprint assignment within a subscription.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.AssignmentOperationsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
apiInstance.assignmentOperationsList(apiVersion, scope, assignmentName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | 
 **assignmentName** | **String**| Name of the blueprint assignment. | 

### Return type

[**AssignmentOperationList**](AssignmentOperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

