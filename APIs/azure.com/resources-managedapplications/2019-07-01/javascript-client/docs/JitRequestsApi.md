# ApplicationClient.JitRequestsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jitRequestsCreateOrUpdate**](JitRequestsApi.md#jitRequestsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/jitRequests/{jitRequestName} | 
[**jitRequestsDelete**](JitRequestsApi.md#jitRequestsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/jitRequests/{jitRequestName} | 
[**jitRequestsGet**](JitRequestsApi.md#jitRequestsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/jitRequests/{jitRequestName} | 
[**jitRequestsListByResourceGroup**](JitRequestsApi.md#jitRequestsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/jitRequests | 
[**jitRequestsListBySubscription**](JitRequestsApi.md#jitRequestsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Solutions/jitRequests | 
[**jitRequestsUpdate**](JitRequestsApi.md#jitRequestsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/jitRequests/{jitRequestName} | 



## jitRequestsCreateOrUpdate

> JitRequestDefinition jitRequestsCreateOrUpdate(resourceGroupName, jitRequestName, apiVersion, subscriptionId, parameters)



Creates or updates the JIT request.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.JitRequestsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let jitRequestName = "jitRequestName_example"; // String | The name of the JIT request.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ApplicationClient.JitRequestDefinition(); // JitRequestDefinition | Parameters supplied to the update JIT request.
apiInstance.jitRequestsCreateOrUpdate(resourceGroupName, jitRequestName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **jitRequestName** | **String**| The name of the JIT request. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**JitRequestDefinition**](JitRequestDefinition.md)| Parameters supplied to the update JIT request. | 

### Return type

[**JitRequestDefinition**](JitRequestDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jitRequestsDelete

> jitRequestsDelete(resourceGroupName, jitRequestName, apiVersion, subscriptionId)



Deletes the JIT request.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.JitRequestsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let jitRequestName = "jitRequestName_example"; // String | The name of the JIT request.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.jitRequestsDelete(resourceGroupName, jitRequestName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **jitRequestName** | **String**| The name of the JIT request. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitRequestsGet

> JitRequestDefinition jitRequestsGet(resourceGroupName, jitRequestName, apiVersion, subscriptionId)



Gets the JIT request.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.JitRequestsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let jitRequestName = "jitRequestName_example"; // String | The name of the JIT request.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.jitRequestsGet(resourceGroupName, jitRequestName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **jitRequestName** | **String**| The name of the JIT request. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**JitRequestDefinition**](JitRequestDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitRequestsListByResourceGroup

> JitRequestDefinitionListResult jitRequestsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Retrieves all JIT requests within the resource group.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.JitRequestsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.jitRequestsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**JitRequestDefinitionListResult**](JitRequestDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitRequestsListBySubscription

> JitRequestDefinitionListResult jitRequestsListBySubscription(apiVersion, subscriptionId)



Retrieves all JIT requests within the subscription.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.JitRequestsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.jitRequestsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**JitRequestDefinitionListResult**](JitRequestDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitRequestsUpdate

> JitRequestDefinition jitRequestsUpdate(resourceGroupName, jitRequestName, apiVersion, subscriptionId, parameters)



Updates the JIT request.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.JitRequestsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let jitRequestName = "jitRequestName_example"; // String | The name of the JIT request.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ApplicationClient.JitRequestPatchable(); // JitRequestPatchable | Parameters supplied to the update JIT request.
apiInstance.jitRequestsUpdate(resourceGroupName, jitRequestName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **jitRequestName** | **String**| The name of the JIT request. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**JitRequestPatchable**](JitRequestPatchable.md)| Parameters supplied to the update JIT request. | 

### Return type

[**JitRequestDefinition**](JitRequestDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

