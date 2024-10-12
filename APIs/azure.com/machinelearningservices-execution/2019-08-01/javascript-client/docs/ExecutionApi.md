# ExecutionService.ExecutionApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executionCancelRunWithUri**](ExecutionApi.md#executionCancelRunWithUri) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/runId/{runId}/cancel | Cancel a run.
[**executionStartLocalRun**](ExecutionApi.md#executionStartLocalRun) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/startlocalrun | Start a run on a local machine.
[**executionStartRun**](ExecutionApi.md#executionStartRun) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/startrun | Start a run on a remote compute target.
[**executionStartSnapshotRun**](ExecutionApi.md#executionStartSnapshotRun) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/snapshotrun | Start a run from a snapshot on a remote compute target.



## executionCancelRunWithUri

> StartRunResult executionCancelRunWithUri(subscriptionId, resourceGroupName, workspaceName, experimentName, runId)

Cancel a run.

Cancels a run within an experiment.

### Example

```javascript
import ExecutionService from 'execution_service';
let defaultClient = ExecutionService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExecutionService.ExecutionApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let experimentName = "experimentName_example"; // String | The experiment name.
let runId = "runId_example"; // String | The id of the run to cancel.
apiInstance.executionCancelRunWithUri(subscriptionId, resourceGroupName, workspaceName, experimentName, runId, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **experimentName** | **String**| The experiment name. | 
 **runId** | **String**| The id of the run to cancel. | 

### Return type

[**StartRunResult**](StartRunResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## executionStartLocalRun

> File executionStartLocalRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, opts)

Start a run on a local machine.

Starts an experiment run using the provided definition.json file to define the run.              The source code and configuration is defined in a zip archive in project.zip.

### Example

```javascript
import ExecutionService from 'execution_service';
let defaultClient = ExecutionService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExecutionService.ExecutionApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let experimentName = "experimentName_example"; // String | The experiment name.
let definition = new ExecutionService.RunDefinition(); // RunDefinition | A JSON run definition structure.
let opts = {
  'runId': "runId_example" // String | A run id. If not supplied a run id will be created automatically.
};
apiInstance.executionStartLocalRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **experimentName** | **String**| The experiment name. | 
 **definition** | [**RunDefinition**](RunDefinition.md)| A JSON run definition structure. | 
 **runId** | **String**| A run id. If not supplied a run id will be created automatically. | [optional] 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/octet-stream


## executionStartRun

> StartRunResult executionStartRun(subscriptionId, resourceGroupName, workspaceName, experimentName, runDefinitionFile, projectZipFile, opts)

Start a run on a remote compute target.

Starts an experiment run using the provided definition.json file to define the run.              The source code and configuration is defined in a zip archive in project.zip.

### Example

```javascript
import ExecutionService from 'execution_service';
let defaultClient = ExecutionService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExecutionService.ExecutionApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let experimentName = "experimentName_example"; // String | The experiment name.
let runDefinitionFile = "/path/to/file"; // File | The JSON file containing the RunDefinition
let projectZipFile = "/path/to/file"; // File | The zip archive of the project folder containing the source code to use for the run.
let opts = {
  'runId': "runId_example" // String | A run id. If not supplied a run id will be created automatically.
};
apiInstance.executionStartRun(subscriptionId, resourceGroupName, workspaceName, experimentName, runDefinitionFile, projectZipFile, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **experimentName** | **String**| The experiment name. | 
 **runDefinitionFile** | **File**| The JSON file containing the RunDefinition | 
 **projectZipFile** | **File**| The zip archive of the project folder containing the source code to use for the run. | 
 **runId** | **String**| A run id. If not supplied a run id will be created automatically. | [optional] 

### Return type

[**StartRunResult**](StartRunResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## executionStartSnapshotRun

> StartRunResult executionStartSnapshotRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, opts)

Start a run from a snapshot on a remote compute target.

Starts an experiment run on the remote compute target using the provided definition.json file to define the run.              The code for the run is retrieved using the snapshotId in definition.json.

### Example

```javascript
import ExecutionService from 'execution_service';
let defaultClient = ExecutionService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExecutionService.ExecutionApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let experimentName = "experimentName_example"; // String | The experiment name.
let definition = new ExecutionService.RunDefinition(); // RunDefinition | A JSON run definition structure.
let opts = {
  'runId': "runId_example" // String | A run id. If not supplied a run id will be created automatically.
};
apiInstance.executionStartSnapshotRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **experimentName** | **String**| The experiment name. | 
 **definition** | [**RunDefinition**](RunDefinition.md)| A JSON run definition structure. | 
 **runId** | **String**| A run id. If not supplied a run id will be created automatically. | [optional] 

### Return type

[**StartRunResult**](StartRunResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

