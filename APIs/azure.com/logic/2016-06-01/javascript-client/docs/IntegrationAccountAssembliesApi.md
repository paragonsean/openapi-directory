# LogicManagementClient.IntegrationAccountAssembliesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountAssembliesCreateOrUpdate**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName} | 
[**integrationAccountAssembliesDelete**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName} | 
[**integrationAccountAssembliesGet**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName} | 
[**integrationAccountAssembliesList**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies | 
[**integrationAccountAssembliesListContentCallbackUrl**](IntegrationAccountAssembliesApi.md#integrationAccountAssembliesListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName}/listContentCallbackUrl | 



## integrationAccountAssembliesCreateOrUpdate

> AssemblyDefinition integrationAccountAssembliesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion, assemblyArtifact)



Create or update an assembly for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAssembliesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
let apiVersion = "apiVersion_example"; // String | The API version.
let assemblyArtifact = new LogicManagementClient.AssemblyDefinition(); // AssemblyDefinition | The assembly artifact.
apiInstance.integrationAccountAssembliesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion, assemblyArtifact, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **assemblyArtifactName** | **String**| The assembly artifact name. | 
 **apiVersion** | **String**| The API version. | 
 **assemblyArtifact** | [**AssemblyDefinition**](AssemblyDefinition.md)| The assembly artifact. | 

### Return type

[**AssemblyDefinition**](AssemblyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationAccountAssembliesDelete

> integrationAccountAssembliesDelete(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion)



Delete an assembly for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAssembliesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountAssembliesDelete(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **assemblyArtifactName** | **String**| The assembly artifact name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## integrationAccountAssembliesGet

> AssemblyDefinition integrationAccountAssembliesGet(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion)



Get an assembly for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAssembliesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountAssembliesGet(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **assemblyArtifactName** | **String**| The assembly artifact name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**AssemblyDefinition**](AssemblyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountAssembliesList

> AssemblyCollection integrationAccountAssembliesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



List the assemblies for an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAssembliesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountAssembliesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**AssemblyCollection**](AssemblyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountAssembliesListContentCallbackUrl

> WorkflowTriggerCallbackUrl integrationAccountAssembliesListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion)



Get the content callback url for an integration account assembly.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAssembliesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let assemblyArtifactName = "assemblyArtifactName_example"; // String | The assembly artifact name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountAssembliesListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, assemblyArtifactName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **assemblyArtifactName** | **String**| The assembly artifact name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

