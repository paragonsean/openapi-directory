# LogicManagementClient.WorkflowsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowsCreateOrUpdate**](WorkflowsApi.md#workflowsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsDelete**](WorkflowsApi.md#workflowsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsDisable**](WorkflowsApi.md#workflowsDisable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/disable | 
[**workflowsEnable**](WorkflowsApi.md#workflowsEnable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/enable | 
[**workflowsGenerateUpgradedDefinition**](WorkflowsApi.md#workflowsGenerateUpgradedDefinition) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/generateUpgradedDefinition | 
[**workflowsGet**](WorkflowsApi.md#workflowsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsListByResourceGroup**](WorkflowsApi.md#workflowsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows | 
[**workflowsListBySubscription**](WorkflowsApi.md#workflowsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Logic/workflows | 
[**workflowsListCallbackUrl**](WorkflowsApi.md#workflowsListCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/listCallbackUrl | 
[**workflowsListSwagger**](WorkflowsApi.md#workflowsListSwagger) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/listSwagger | 
[**workflowsMove**](WorkflowsApi.md#workflowsMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/move | 
[**workflowsRegenerateAccessKey**](WorkflowsApi.md#workflowsRegenerateAccessKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/regenerateAccessKey | 
[**workflowsUpdate**](WorkflowsApi.md#workflowsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsValidate**](WorkflowsApi.md#workflowsValidate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/locations/{location}/workflows/{workflowName}/validate | 
[**workflowsValidateWorkflow**](WorkflowsApi.md#workflowsValidateWorkflow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/validate | 



## workflowsCreateOrUpdate

> Workflow workflowsCreateOrUpdate(subscriptionId, resourceGroupName, workflowName, apiVersion, workflow)



Creates or updates a workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let workflow = new LogicManagementClient.Workflow(); // Workflow | The workflow.
apiInstance.workflowsCreateOrUpdate(subscriptionId, resourceGroupName, workflowName, apiVersion, workflow, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **workflow** | [**Workflow**](Workflow.md)| The workflow. | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workflowsDelete

> workflowsDelete(subscriptionId, resourceGroupName, workflowName, apiVersion)



Deletes a workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowsDelete(subscriptionId, resourceGroupName, workflowName, apiVersion, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workflowsDisable

> workflowsDisable(subscriptionId, resourceGroupName, workflowName, apiVersion)



Disables a workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowsDisable(subscriptionId, resourceGroupName, workflowName, apiVersion, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workflowsEnable

> workflowsEnable(subscriptionId, resourceGroupName, workflowName, apiVersion)



Enables a workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowsEnable(subscriptionId, resourceGroupName, workflowName, apiVersion, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workflowsGenerateUpgradedDefinition

> Object workflowsGenerateUpgradedDefinition(subscriptionId, resourceGroupName, workflowName, apiVersion, parameters)



Generates the upgraded definition for a workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let parameters = new LogicManagementClient.GenerateUpgradedDefinitionParameters(); // GenerateUpgradedDefinitionParameters | Parameters for generating an upgraded definition.
apiInstance.workflowsGenerateUpgradedDefinition(subscriptionId, resourceGroupName, workflowName, apiVersion, parameters, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **parameters** | [**GenerateUpgradedDefinitionParameters**](GenerateUpgradedDefinitionParameters.md)| Parameters for generating an upgraded definition. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workflowsGet

> Workflow workflowsGet(subscriptionId, resourceGroupName, workflowName, apiVersion)



Gets a workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowsGet(subscriptionId, resourceGroupName, workflowName, apiVersion, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowsListByResourceGroup

> WorkflowListResult workflowsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Gets a list of workflows by resource group.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.
};
apiInstance.workflowsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId. | [optional] 

### Return type

[**WorkflowListResult**](WorkflowListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowsListBySubscription

> WorkflowListResult workflowsListBySubscription(subscriptionId, apiVersion, opts)



Gets a list of workflows by subscription.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.
};
apiInstance.workflowsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId. | [optional] 

### Return type

[**WorkflowListResult**](WorkflowListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowsListCallbackUrl

> WorkflowTriggerCallbackUrl workflowsListCallbackUrl(subscriptionId, resourceGroupName, workflowName, apiVersion, listCallbackUrl)



Get the workflow callback Url.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let listCallbackUrl = new LogicManagementClient.GetCallbackUrlParameters(); // GetCallbackUrlParameters | Which callback url to list.
apiInstance.workflowsListCallbackUrl(subscriptionId, resourceGroupName, workflowName, apiVersion, listCallbackUrl, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **listCallbackUrl** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)| Which callback url to list. | 

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workflowsListSwagger

> Object workflowsListSwagger(subscriptionId, resourceGroupName, workflowName, apiVersion)



Gets an OpenAPI definition for the workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowsListSwagger(subscriptionId, resourceGroupName, workflowName, apiVersion, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowsMove

> workflowsMove(subscriptionId, resourceGroupName, workflowName, apiVersion, move)



Moves an existing workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let move = new LogicManagementClient.Workflow(); // Workflow | The workflow to move.
apiInstance.workflowsMove(subscriptionId, resourceGroupName, workflowName, apiVersion, move, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **move** | [**Workflow**](Workflow.md)| The workflow to move. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## workflowsRegenerateAccessKey

> workflowsRegenerateAccessKey(subscriptionId, resourceGroupName, workflowName, apiVersion, keyType)



Regenerates the callback URL access key for request triggers.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let keyType = new LogicManagementClient.RegenerateActionParameter(); // RegenerateActionParameter | The access key type.
apiInstance.workflowsRegenerateAccessKey(subscriptionId, resourceGroupName, workflowName, apiVersion, keyType, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **keyType** | [**RegenerateActionParameter**](RegenerateActionParameter.md)| The access key type. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## workflowsUpdate

> Workflow workflowsUpdate(subscriptionId, resourceGroupName, workflowName, apiVersion, workflow)



Updates a workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let workflow = new LogicManagementClient.Workflow(); // Workflow | The workflow.
apiInstance.workflowsUpdate(subscriptionId, resourceGroupName, workflowName, apiVersion, workflow, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **workflow** | [**Workflow**](Workflow.md)| The workflow. | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workflowsValidate

> workflowsValidate(subscriptionId, resourceGroupName, location, workflowName, apiVersion, workflow)



Validates the workflow definition.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let location = "location_example"; // String | The workflow location.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let workflow = new LogicManagementClient.Workflow(); // Workflow | The workflow definition.
apiInstance.workflowsValidate(subscriptionId, resourceGroupName, location, workflowName, apiVersion, workflow, (error, data, response) => {
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
 **location** | **String**| The workflow location. | 
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **workflow** | [**Workflow**](Workflow.md)| The workflow definition. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## workflowsValidateWorkflow

> workflowsValidateWorkflow(subscriptionId, resourceGroupName, workflowName, apiVersion, validate)



Validates the workflow.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let validate = new LogicManagementClient.Workflow(); // Workflow | The workflow.
apiInstance.workflowsValidateWorkflow(subscriptionId, resourceGroupName, workflowName, apiVersion, validate, (error, data, response) => {
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
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **validate** | [**Workflow**](Workflow.md)| The workflow. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

