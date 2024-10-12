# LogicManagementClient.WorkflowsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowsCreateOrUpdate**](WorkflowsApi.md#workflowsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsDelete**](WorkflowsApi.md#workflowsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsDisable**](WorkflowsApi.md#workflowsDisable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/disable | 
[**workflowsEnable**](WorkflowsApi.md#workflowsEnable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/enable | 
[**workflowsGet**](WorkflowsApi.md#workflowsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsListByResourceGroup**](WorkflowsApi.md#workflowsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows | 
[**workflowsListBySubscription**](WorkflowsApi.md#workflowsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Logic/workflows | 
[**workflowsRun**](WorkflowsApi.md#workflowsRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/run | 
[**workflowsUpdate**](WorkflowsApi.md#workflowsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName} | 
[**workflowsValidate**](WorkflowsApi.md#workflowsValidate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/validate | 



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

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


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
- **Accept**: application/json, text/json


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
  'filter': "filter_example" // String | The filter to apply on the operation.
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
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**WorkflowListResult**](WorkflowListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


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
  'filter': "filter_example" // String | The filter to apply on the operation.
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
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**WorkflowListResult**](WorkflowListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## workflowsRun

> WorkflowRun workflowsRun(subscriptionId, resourceGroupName, workflowName, apiVersion, parameters)



Runs a workflow.

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
let parameters = new LogicManagementClient.RunWorkflowParameters(); // RunWorkflowParameters | The parameters.
apiInstance.workflowsRun(subscriptionId, resourceGroupName, workflowName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**RunWorkflowParameters**](RunWorkflowParameters.md)| The parameters. | 

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


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

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## workflowsValidate

> workflowsValidate(subscriptionId, resourceGroupName, workflowName, apiVersion, workflow)



Validates a workflow.

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
apiInstance.workflowsValidate(subscriptionId, resourceGroupName, workflowName, apiVersion, workflow, (error, data, response) => {
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
 **workflow** | [**Workflow**](Workflow.md)| The workflow. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

