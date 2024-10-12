# ApplicationClient.ApplicationDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationDefinitionsCreateOrUpdate**](ApplicationDefinitionsApi.md#applicationDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applicationDefinitions/{applicationDefinitionName} | 
[**applicationDefinitionsDelete**](ApplicationDefinitionsApi.md#applicationDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applicationDefinitions/{applicationDefinitionName} | 
[**applicationDefinitionsGet**](ApplicationDefinitionsApi.md#applicationDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applicationDefinitions/{applicationDefinitionName} | 
[**applicationDefinitionsListByResourceGroup**](ApplicationDefinitionsApi.md#applicationDefinitionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applicationDefinitions | 



## applicationDefinitionsCreateOrUpdate

> ApplicationDefinition applicationDefinitionsCreateOrUpdate(resourceGroupName, applicationDefinitionName, apiVersion, subscriptionId, parameters)



Creates a new managed application definition.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applicationDefinitionName = "applicationDefinitionName_example"; // String | The name of the managed application definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ApplicationClient.ApplicationDefinition(); // ApplicationDefinition | Parameters supplied to the create or update an managed application definition.
apiInstance.applicationDefinitionsCreateOrUpdate(resourceGroupName, applicationDefinitionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **applicationDefinitionName** | **String**| The name of the managed application definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ApplicationDefinition**](ApplicationDefinition.md)| Parameters supplied to the create or update an managed application definition. | 

### Return type

[**ApplicationDefinition**](ApplicationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationDefinitionsDelete

> applicationDefinitionsDelete(resourceGroupName, applicationDefinitionName, apiVersion, subscriptionId)



Deletes the managed application definition.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applicationDefinitionName = "applicationDefinitionName_example"; // String | The name of the managed application definition to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applicationDefinitionsDelete(resourceGroupName, applicationDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationDefinitionName** | **String**| The name of the managed application definition to delete. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationDefinitionsGet

> ApplicationDefinition applicationDefinitionsGet(resourceGroupName, applicationDefinitionName, apiVersion, subscriptionId)



Gets the managed application definition.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applicationDefinitionName = "applicationDefinitionName_example"; // String | The name of the managed application definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applicationDefinitionsGet(resourceGroupName, applicationDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationDefinitionName** | **String**| The name of the managed application definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ApplicationDefinition**](ApplicationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationDefinitionsListByResourceGroup

> ApplicationDefinitionListResult applicationDefinitionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists the managed application definitions in a resource group.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applicationDefinitionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**ApplicationDefinitionListResult**](ApplicationDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

