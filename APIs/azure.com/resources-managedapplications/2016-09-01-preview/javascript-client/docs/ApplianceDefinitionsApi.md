# ManagedApplicationClient.ApplianceDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applianceDefinitionsCreateOrUpdate**](ApplianceDefinitionsApi.md#applianceDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions/{applianceDefinitionName} | 
[**applianceDefinitionsCreateOrUpdateById**](ApplianceDefinitionsApi.md#applianceDefinitionsCreateOrUpdateById) | **PUT** /{applianceDefinitionId} | 
[**applianceDefinitionsDelete**](ApplianceDefinitionsApi.md#applianceDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions/{applianceDefinitionName} | 
[**applianceDefinitionsDeleteById**](ApplianceDefinitionsApi.md#applianceDefinitionsDeleteById) | **DELETE** /{applianceDefinitionId} | 
[**applianceDefinitionsGet**](ApplianceDefinitionsApi.md#applianceDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions/{applianceDefinitionName} | 
[**applianceDefinitionsGetById**](ApplianceDefinitionsApi.md#applianceDefinitionsGetById) | **GET** /{applianceDefinitionId} | 
[**applianceDefinitionsListByResourceGroup**](ApplianceDefinitionsApi.md#applianceDefinitionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions | 



## applianceDefinitionsCreateOrUpdate

> ApplianceDefinition applianceDefinitionsCreateOrUpdate(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId, parameters)



Creates a new appliance definition.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.ApplianceDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applianceDefinitionName = "applianceDefinitionName_example"; // String | The name of the appliance definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ManagedApplicationClient.ApplianceDefinition(); // ApplianceDefinition | Parameters supplied to the create or update an appliance definition.
apiInstance.applianceDefinitionsCreateOrUpdate(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **applianceDefinitionName** | **String**| The name of the appliance definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ApplianceDefinition**](ApplianceDefinition.md)| Parameters supplied to the create or update an appliance definition. | 

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applianceDefinitionsCreateOrUpdateById

> ApplianceDefinition applianceDefinitionsCreateOrUpdateById(applianceDefinitionId, apiVersion, parameters)



Creates a new appliance definition.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.ApplianceDefinitionsApi();
let applianceDefinitionId = "applianceDefinitionId_example"; // String | The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ManagedApplicationClient.ApplianceDefinition(); // ApplianceDefinition | Parameters supplied to the create or update an appliance definition.
apiInstance.applianceDefinitionsCreateOrUpdateById(applianceDefinitionId, apiVersion, parameters, (error, data, response) => {
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
 **applianceDefinitionId** | **String**| The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**ApplianceDefinition**](ApplianceDefinition.md)| Parameters supplied to the create or update an appliance definition. | 

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applianceDefinitionsDelete

> applianceDefinitionsDelete(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId)



Deletes the appliance definition.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.ApplianceDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applianceDefinitionName = "applianceDefinitionName_example"; // String | The name of the appliance definition to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applianceDefinitionsDelete(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applianceDefinitionName** | **String**| The name of the appliance definition to delete. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applianceDefinitionsDeleteById

> applianceDefinitionsDeleteById(applianceDefinitionId, apiVersion)



Deletes the appliance definition.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.ApplianceDefinitionsApi();
let applianceDefinitionId = "applianceDefinitionId_example"; // String | The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.applianceDefinitionsDeleteById(applianceDefinitionId, apiVersion, (error, data, response) => {
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
 **applianceDefinitionId** | **String**| The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applianceDefinitionsGet

> ApplianceDefinition applianceDefinitionsGet(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId)



Gets the appliance definition.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.ApplianceDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applianceDefinitionName = "applianceDefinitionName_example"; // String | The name of the appliance definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applianceDefinitionsGet(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applianceDefinitionName** | **String**| The name of the appliance definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applianceDefinitionsGetById

> ApplianceDefinition applianceDefinitionsGetById(applianceDefinitionId, apiVersion)



Gets the appliance definition.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.ApplianceDefinitionsApi();
let applianceDefinitionId = "applianceDefinitionId_example"; // String | The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.applianceDefinitionsGetById(applianceDefinitionId, apiVersion, (error, data, response) => {
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
 **applianceDefinitionId** | **String**| The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applianceDefinitionsListByResourceGroup

> ApplianceDefinitionListResult applianceDefinitionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists the appliance definitions in a resource group.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.ApplianceDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applianceDefinitionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**ApplianceDefinitionListResult**](ApplianceDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

