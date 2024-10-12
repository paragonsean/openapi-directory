# LogicManagementClient.WorkflowRunActionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowRunActionRepetitionsGet**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName} | 
[**workflowRunActionRepetitionsList**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions | 
[**workflowRunActionRepetitionsListExpressionTraces**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsListExpressionTraces) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/listExpressionTraces | 
[**workflowRunActionRepetitionsRequestHistoriesGet**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsRequestHistoriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/requestHistories/{requestHistoryName} | 
[**workflowRunActionRepetitionsRequestHistoriesList**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsRequestHistoriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/requestHistories | 
[**workflowRunActionRequestHistoriesGet**](WorkflowRunActionsApi.md#workflowRunActionRequestHistoriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/requestHistories/{requestHistoryName} | 
[**workflowRunActionRequestHistoriesList**](WorkflowRunActionsApi.md#workflowRunActionRequestHistoriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/requestHistories | 
[**workflowRunActionScopeRepetitionsGet**](WorkflowRunActionsApi.md#workflowRunActionScopeRepetitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/scopeRepetitions/{repetitionName} | 
[**workflowRunActionScopeRepetitionsList**](WorkflowRunActionsApi.md#workflowRunActionScopeRepetitionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/scopeRepetitions | 
[**workflowRunActionsGet**](WorkflowRunActionsApi.md#workflowRunActionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName} | 
[**workflowRunActionsList**](WorkflowRunActionsApi.md#workflowRunActionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions | 
[**workflowRunActionsListExpressionTraces**](WorkflowRunActionsApi.md#workflowRunActionsListExpressionTraces) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/listExpressionTraces | 



## workflowRunActionRepetitionsGet

> WorkflowRunActionRepetitionDefinition workflowRunActionRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



Get a workflow run action repetition.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let repetitionName = "repetitionName_example"; // String | The workflow repetition.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **repetitionName** | **String**| The workflow repetition. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowRunActionRepetitionDefinition**](WorkflowRunActionRepetitionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionRepetitionsList

> WorkflowRunActionRepetitionDefinitionCollection workflowRunActionRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



Get all of a workflow run action repetitions.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowRunActionRepetitionDefinitionCollection**](WorkflowRunActionRepetitionDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionRepetitionsListExpressionTraces

> ExpressionTraces workflowRunActionRepetitionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



Lists a workflow run expression trace.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let repetitionName = "repetitionName_example"; // String | The workflow repetition.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionRepetitionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **repetitionName** | **String**| The workflow repetition. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**ExpressionTraces**](ExpressionTraces.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionRepetitionsRequestHistoriesGet

> RequestHistory workflowRunActionRepetitionsRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, requestHistoryName, apiVersion)



Gets a workflow run repetition request history.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let repetitionName = "repetitionName_example"; // String | The workflow repetition.
let requestHistoryName = "requestHistoryName_example"; // String | The request history name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionRepetitionsRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, requestHistoryName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **repetitionName** | **String**| The workflow repetition. | 
 **requestHistoryName** | **String**| The request history name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**RequestHistory**](RequestHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionRepetitionsRequestHistoriesList

> RequestHistoryListResult workflowRunActionRepetitionsRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



List a workflow run repetition request history.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let repetitionName = "repetitionName_example"; // String | The workflow repetition.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionRepetitionsRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **repetitionName** | **String**| The workflow repetition. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**RequestHistoryListResult**](RequestHistoryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionRequestHistoriesGet

> RequestHistory workflowRunActionRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, requestHistoryName, apiVersion)



Gets a workflow run request history.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let requestHistoryName = "requestHistoryName_example"; // String | The request history name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, requestHistoryName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **requestHistoryName** | **String**| The request history name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**RequestHistory**](RequestHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionRequestHistoriesList

> RequestHistoryListResult workflowRunActionRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



List a workflow run request history.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**RequestHistoryListResult**](RequestHistoryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionScopeRepetitionsGet

> WorkflowRunActionRepetitionDefinition workflowRunActionScopeRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



Get a workflow run action scoped repetition.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let repetitionName = "repetitionName_example"; // String | The workflow repetition.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionScopeRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **repetitionName** | **String**| The workflow repetition. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowRunActionRepetitionDefinition**](WorkflowRunActionRepetitionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionScopeRepetitionsList

> WorkflowRunActionRepetitionDefinitionCollection workflowRunActionScopeRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



List the workflow run action scoped repetitions.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionScopeRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowRunActionRepetitionDefinitionCollection**](WorkflowRunActionRepetitionDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionsGet

> WorkflowRunAction workflowRunActionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



Gets a workflow run action.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowRunAction**](WorkflowRunAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionsList

> WorkflowRunActionListResult workflowRunActionsList(subscriptionId, resourceGroupName, workflowName, runName, apiVersion, opts)



Gets a list of workflow run actions.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation. Options for filters include: Status.
};
apiInstance.workflowRunActionsList(subscriptionId, resourceGroupName, workflowName, runName, apiVersion, opts, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. Options for filters include: Status. | [optional] 

### Return type

[**WorkflowRunActionListResult**](WorkflowRunActionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowRunActionsListExpressionTraces

> ExpressionTraces workflowRunActionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



Lists a workflow run expression trace.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowRunActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let runName = "runName_example"; // String | The workflow run name.
let actionName = "actionName_example"; // String | The workflow action name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowRunActionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion, (error, data, response) => {
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
 **runName** | **String**| The workflow run name. | 
 **actionName** | **String**| The workflow action name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**ExpressionTraces**](ExpressionTraces.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

