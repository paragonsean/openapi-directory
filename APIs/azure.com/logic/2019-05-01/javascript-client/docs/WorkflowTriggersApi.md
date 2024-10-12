# LogicManagementClient.WorkflowTriggersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowTriggersGet**](WorkflowTriggersApi.md#workflowTriggersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName} | 
[**workflowTriggersGetSchemaJson**](WorkflowTriggersApi.md#workflowTriggersGetSchemaJson) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/schemas/json | 
[**workflowTriggersList**](WorkflowTriggersApi.md#workflowTriggersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers | 
[**workflowTriggersListCallbackUrl**](WorkflowTriggersApi.md#workflowTriggersListCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/listCallbackUrl | 
[**workflowTriggersReset**](WorkflowTriggersApi.md#workflowTriggersReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/reset | 
[**workflowTriggersRun**](WorkflowTriggersApi.md#workflowTriggersRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/run | 
[**workflowTriggersSetState**](WorkflowTriggersApi.md#workflowTriggersSetState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/setState | 
[**workflowVersionTriggersListCallbackUrl**](WorkflowTriggersApi.md#workflowVersionTriggersListCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/versions/{versionId}/triggers/{triggerName}/listCallbackUrl | 



## workflowTriggersGet

> WorkflowTrigger workflowTriggersGet(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Gets a workflow trigger.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowTriggersGet(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowTrigger**](WorkflowTrigger.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowTriggersGetSchemaJson

> JsonSchema workflowTriggersGetSchemaJson(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Get the trigger schema as JSON.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowTriggersGetSchemaJson(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**JsonSchema**](JsonSchema.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowTriggersList

> WorkflowTriggerListResult workflowTriggersList(subscriptionId, resourceGroupName, workflowName, apiVersion, opts)



Gets a list of workflow triggers.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.workflowTriggersList(subscriptionId, resourceGroupName, workflowName, apiVersion, opts, (error, data, response) => {
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
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**WorkflowTriggerListResult**](WorkflowTriggerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowTriggersListCallbackUrl

> WorkflowTriggerCallbackUrl workflowTriggersListCallbackUrl(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Get the callback URL for a workflow trigger.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowTriggersListCallbackUrl(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowTriggersReset

> workflowTriggersReset(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Resets a workflow trigger.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowTriggersReset(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowTriggersRun

> Object workflowTriggersRun(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Runs a workflow trigger.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowTriggersRun(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowTriggersSetState

> workflowTriggersSetState(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, setState)



Sets the state of a workflow trigger.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
let setState = new LogicManagementClient.SetTriggerStateActionDefinition(); // SetTriggerStateActionDefinition | The workflow trigger state.
apiInstance.workflowTriggersSetState(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, setState, (error, data, response) => {
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
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 
 **setState** | [**SetTriggerStateActionDefinition**](SetTriggerStateActionDefinition.md)| The workflow trigger state. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workflowVersionTriggersListCallbackUrl

> WorkflowTriggerCallbackUrl workflowVersionTriggersListCallbackUrl(subscriptionId, resourceGroupName, workflowName, versionId, triggerName, apiVersion, opts)



Get the callback url for a trigger of a workflow version.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let versionId = "versionId_example"; // String | The workflow versionId.
let triggerName = "triggerName_example"; // String | The workflow trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'parameters': new LogicManagementClient.GetCallbackUrlParameters() // GetCallbackUrlParameters | The callback URL parameters.
};
apiInstance.workflowVersionTriggersListCallbackUrl(subscriptionId, resourceGroupName, workflowName, versionId, triggerName, apiVersion, opts, (error, data, response) => {
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
 **versionId** | **String**| The workflow versionId. | 
 **triggerName** | **String**| The workflow trigger name. | 
 **apiVersion** | **String**| The API version. | 
 **parameters** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)| The callback URL parameters. | [optional] 

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

