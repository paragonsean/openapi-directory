# BlueprintClient.AssignmentApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignmentsCreateOrUpdate**](AssignmentApi.md#assignmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} | 
[**assignmentsDelete**](AssignmentApi.md#assignmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} | 
[**assignmentsGet**](AssignmentApi.md#assignmentsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} | 
[**assignmentsList**](AssignmentApi.md#assignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments | 



## assignmentsCreateOrUpdate

> Assignment assignmentsCreateOrUpdate(apiVersion, subscriptionId, assignmentName, assignment)



Create or update a Blueprint assignment.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.AssignmentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
let assignmentName = "assignmentName_example"; // String | name of the assignment.
let assignment = new BlueprintClient.Assignment(); // Assignment | assignment object to save.
apiInstance.assignmentsCreateOrUpdate(apiVersion, subscriptionId, assignmentName, assignment, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | 
 **assignmentName** | **String**| name of the assignment. | 
 **assignment** | [**Assignment**](Assignment.md)| assignment object to save. | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assignmentsDelete

> Assignment assignmentsDelete(apiVersion, subscriptionId, assignmentName)



Delete a Blueprint assignment.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.AssignmentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
let assignmentName = "assignmentName_example"; // String | name of the assignment.
apiInstance.assignmentsDelete(apiVersion, subscriptionId, assignmentName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | 
 **assignmentName** | **String**| name of the assignment. | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assignmentsGet

> Assignment assignmentsGet(apiVersion, subscriptionId, assignmentName)



Get a Blueprint assignment.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.AssignmentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
let assignmentName = "assignmentName_example"; // String | name of the assignment.
apiInstance.assignmentsGet(apiVersion, subscriptionId, assignmentName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | 
 **assignmentName** | **String**| name of the assignment. | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assignmentsList

> AssignmentList assignmentsList(apiVersion, subscriptionId)



List Blueprint assignments within a subscription.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.AssignmentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
apiInstance.assignmentsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | 

### Return type

[**AssignmentList**](AssignmentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

