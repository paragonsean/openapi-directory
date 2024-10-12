# ManagedServicesClient.RegistrationAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registrationAssignmentsCreateOrUpdate**](RegistrationAssignmentsApi.md#registrationAssignmentsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registrationAssignmentId} | 
[**registrationAssignmentsDelete**](RegistrationAssignmentsApi.md#registrationAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registrationAssignmentId} | 
[**registrationAssignmentsGet**](RegistrationAssignmentsApi.md#registrationAssignmentsGet) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registrationAssignmentId} | 
[**registrationAssignmentsList**](RegistrationAssignmentsApi.md#registrationAssignmentsList) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments | 



## registrationAssignmentsCreateOrUpdate

> RegistrationAssignment registrationAssignmentsCreateOrUpdate(scope, registrationAssignmentId, apiVersion, requestBody)



Creates or updates a registration assignment.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationAssignmentsApi();
let scope = "scope_example"; // String | Scope of the resource.
let registrationAssignmentId = "registrationAssignmentId_example"; // String | Guid of the registration assignment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let requestBody = new ManagedServicesClient.RegistrationAssignment(); // RegistrationAssignment | The parameters required to create new registration assignment.
apiInstance.registrationAssignmentsCreateOrUpdate(scope, registrationAssignmentId, apiVersion, requestBody, (error, data, response) => {
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
 **scope** | **String**| Scope of the resource. | 
 **registrationAssignmentId** | **String**| Guid of the registration assignment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **requestBody** | [**RegistrationAssignment**](RegistrationAssignment.md)| The parameters required to create new registration assignment. | 

### Return type

[**RegistrationAssignment**](RegistrationAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registrationAssignmentsDelete

> registrationAssignmentsDelete(scope, registrationAssignmentId, apiVersion)



Deletes the specified registration assignment.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationAssignmentsApi();
let scope = "scope_example"; // String | Scope of the resource.
let registrationAssignmentId = "registrationAssignmentId_example"; // String | Guid of the registration assignment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.registrationAssignmentsDelete(scope, registrationAssignmentId, apiVersion, (error, data, response) => {
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
 **scope** | **String**| Scope of the resource. | 
 **registrationAssignmentId** | **String**| Guid of the registration assignment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationAssignmentsGet

> RegistrationAssignment registrationAssignmentsGet(scope, registrationAssignmentId, apiVersion, opts)



Gets the details of specified registration assignment.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationAssignmentsApi();
let scope = "scope_example"; // String | Scope of the resource.
let registrationAssignmentId = "registrationAssignmentId_example"; // String | Guid of the registration assignment.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'expandRegistrationDefinition': true // Boolean | Tells whether to return registration definition details also along with registration assignment details.
};
apiInstance.registrationAssignmentsGet(scope, registrationAssignmentId, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| Scope of the resource. | 
 **registrationAssignmentId** | **String**| Guid of the registration assignment. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **expandRegistrationDefinition** | **Boolean**| Tells whether to return registration definition details also along with registration assignment details. | [optional] 

### Return type

[**RegistrationAssignment**](RegistrationAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationAssignmentsList

> RegistrationAssignmentList registrationAssignmentsList(scope, apiVersion, opts)



Gets a list of the registration assignments.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationAssignmentsApi();
let scope = "scope_example"; // String | Scope of the resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'expandRegistrationDefinition': true // Boolean | Tells whether to return registration definition details also along with registration assignment details.
};
apiInstance.registrationAssignmentsList(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| Scope of the resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **expandRegistrationDefinition** | **Boolean**| Tells whether to return registration definition details also along with registration assignment details. | [optional] 

### Return type

[**RegistrationAssignmentList**](RegistrationAssignmentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

