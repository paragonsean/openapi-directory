# ServiceFabricClientApis.RepairManagementApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelRepairTask**](RepairManagementApi.md#cancelRepairTask) | **POST** /$/CancelRepairTask | Requests the cancellation of the given repair task.
[**createRepairTask**](RepairManagementApi.md#createRepairTask) | **POST** /$/CreateRepairTask | Creates a new repair task.
[**deleteRepairTask**](RepairManagementApi.md#deleteRepairTask) | **POST** /$/DeleteRepairTask | Deletes a completed repair task.
[**forceApproveRepairTask**](RepairManagementApi.md#forceApproveRepairTask) | **POST** /$/ForceApproveRepairTask | Forces the approval of the given repair task.
[**getRepairTaskList**](RepairManagementApi.md#getRepairTaskList) | **GET** /$/GetRepairTaskList | Gets a list of repair tasks matching the given filters.
[**updateRepairExecutionState**](RepairManagementApi.md#updateRepairExecutionState) | **POST** /$/UpdateRepairExecutionState | Updates the execution state of a repair task.
[**updateRepairTaskHealthPolicy**](RepairManagementApi.md#updateRepairTaskHealthPolicy) | **POST** /$/UpdateRepairTaskHealthPolicy | Updates the health policy of the given repair task.



## cancelRepairTask

> RepairTaskUpdateInfo cancelRepairTask(apiVersion, repairTaskCancelDescription)

Requests the cancellation of the given repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.RepairManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let repairTaskCancelDescription = new ServiceFabricClientApis.RepairTaskCancelDescription(); // RepairTaskCancelDescription | Describes the repair task to be cancelled.
apiInstance.cancelRepairTask(apiVersion, repairTaskCancelDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **repairTaskCancelDescription** | [**RepairTaskCancelDescription**](RepairTaskCancelDescription.md)| Describes the repair task to be cancelled. | 

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createRepairTask

> RepairTaskUpdateInfo createRepairTask(apiVersion, repairTask)

Creates a new repair task.

For clusters that have the Repair Manager Service configured, this API provides a way to create repair tasks that run automatically or manually. For repair tasks that run automatically, an appropriate repair executor must be running for each repair action to run automatically. These are currently only available in specially-configured Azure Cloud Services.  To create a manual repair task, provide the set of impacted node names and the expected impact. When the state of the created repair task changes to approved, you can safely perform repair actions on those nodes.  This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.RepairManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let repairTask = new ServiceFabricClientApis.RepairTask(); // RepairTask | Describes the repair task to be created or updated.
apiInstance.createRepairTask(apiVersion, repairTask, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **repairTask** | [**RepairTask**](RepairTask.md)| Describes the repair task to be created or updated. | 

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRepairTask

> deleteRepairTask(apiVersion, repairTaskDeleteDescription)

Deletes a completed repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.RepairManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let repairTaskDeleteDescription = new ServiceFabricClientApis.RepairTaskDeleteDescription(); // RepairTaskDeleteDescription | Describes the repair task to be deleted.
apiInstance.deleteRepairTask(apiVersion, repairTaskDeleteDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **repairTaskDeleteDescription** | [**RepairTaskDeleteDescription**](RepairTaskDeleteDescription.md)| Describes the repair task to be deleted. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forceApproveRepairTask

> RepairTaskUpdateInfo forceApproveRepairTask(apiVersion, repairTaskApproveDescription)

Forces the approval of the given repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.RepairManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let repairTaskApproveDescription = new ServiceFabricClientApis.RepairTaskApproveDescription(); // RepairTaskApproveDescription | Describes the repair task to be approved.
apiInstance.forceApproveRepairTask(apiVersion, repairTaskApproveDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **repairTaskApproveDescription** | [**RepairTaskApproveDescription**](RepairTaskApproveDescription.md)| Describes the repair task to be approved. | 

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepairTaskList

> [RepairTask] getRepairTaskList(apiVersion, opts)

Gets a list of repair tasks matching the given filters.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.RepairManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let opts = {
  'taskIdFilter': "taskIdFilter_example", // String | The repair task ID prefix to be matched.
  'stateFilter': 56, // Number | A bitwise-OR of the following values, specifying which task states should be included in the result list.  - 1 - Created - 2 - Claimed - 4 - Preparing - 8 - Approved - 16 - Executing - 32 - Restoring - 64 - Completed
  'executorFilter': "executorFilter_example" // String | The name of the repair executor whose claimed tasks should be included in the list.
};
apiInstance.getRepairTaskList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **taskIdFilter** | **String**| The repair task ID prefix to be matched. | [optional] 
 **stateFilter** | **Number**| A bitwise-OR of the following values, specifying which task states should be included in the result list.  - 1 - Created - 2 - Claimed - 4 - Preparing - 8 - Approved - 16 - Executing - 32 - Restoring - 64 - Completed | [optional] 
 **executorFilter** | **String**| The name of the repair executor whose claimed tasks should be included in the list. | [optional] 

### Return type

[**[RepairTask]**](RepairTask.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRepairExecutionState

> RepairTaskUpdateInfo updateRepairExecutionState(apiVersion, repairTask)

Updates the execution state of a repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.RepairManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let repairTask = new ServiceFabricClientApis.RepairTask(); // RepairTask | Describes the repair task to be created or updated.
apiInstance.updateRepairExecutionState(apiVersion, repairTask, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **repairTask** | [**RepairTask**](RepairTask.md)| Describes the repair task to be created or updated. | 

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRepairTaskHealthPolicy

> RepairTaskUpdateInfo updateRepairTaskHealthPolicy(apiVersion, repairTaskUpdateHealthPolicyDescription)

Updates the health policy of the given repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.RepairManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let repairTaskUpdateHealthPolicyDescription = new ServiceFabricClientApis.RepairTaskUpdateHealthPolicyDescription(); // RepairTaskUpdateHealthPolicyDescription | Describes the repair task healthy policy to be updated.
apiInstance.updateRepairTaskHealthPolicy(apiVersion, repairTaskUpdateHealthPolicyDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **repairTaskUpdateHealthPolicyDescription** | [**RepairTaskUpdateHealthPolicyDescription**](RepairTaskUpdateHealthPolicyDescription.md)| Describes the repair task healthy policy to be updated. | 

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

