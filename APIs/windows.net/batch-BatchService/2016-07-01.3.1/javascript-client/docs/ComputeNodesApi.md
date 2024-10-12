# BatchService.ComputeNodesApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeNodeAddUser**](ComputeNodesApi.md#computeNodeAddUser) | **POST** /pools/{poolId}/nodes/{nodeId}/users | Adds a user account to the specified compute node.
[**computeNodeDeleteUser**](ComputeNodesApi.md#computeNodeDeleteUser) | **DELETE** /pools/{poolId}/nodes/{nodeId}/users/{userName} | Deletes a user account from the specified compute node.
[**computeNodeDisableScheduling**](ComputeNodesApi.md#computeNodeDisableScheduling) | **POST** /pools/{poolId}/nodes/{nodeId}/disablescheduling | Disables task scheduling on the specified compute node.
[**computeNodeEnableScheduling**](ComputeNodesApi.md#computeNodeEnableScheduling) | **POST** /pools/{poolId}/nodes/{nodeId}/enablescheduling | Enables task scheduling on the specified compute node.
[**computeNodeGet**](ComputeNodesApi.md#computeNodeGet) | **GET** /pools/{poolId}/nodes/{nodeId} | Gets information about the specified compute node.
[**computeNodeGetRemoteDesktop**](ComputeNodesApi.md#computeNodeGetRemoteDesktop) | **GET** /pools/{poolId}/nodes/{nodeId}/rdp | Gets the Remote Desktop Protocol file for the specified compute node.
[**computeNodeGetRemoteLoginSettings**](ComputeNodesApi.md#computeNodeGetRemoteLoginSettings) | **GET** /pools/{poolId}/nodes/{nodeId}/remoteloginsettings | Gets the settings required for remote login to a compute node.
[**computeNodeList**](ComputeNodesApi.md#computeNodeList) | **GET** /pools/{poolId}/nodes | Lists the compute nodes in the specified pool.
[**computeNodeReboot**](ComputeNodesApi.md#computeNodeReboot) | **POST** /pools/{poolId}/nodes/{nodeId}/reboot | Restarts the specified compute node.
[**computeNodeReimage**](ComputeNodesApi.md#computeNodeReimage) | **POST** /pools/{poolId}/nodes/{nodeId}/reimage | Reinstalls the operating system on the specified compute node.
[**computeNodeUpdateUser**](ComputeNodesApi.md#computeNodeUpdateUser) | **PUT** /pools/{poolId}/nodes/{nodeId}/users/{userName} | Updates the password or expiration time of a user account on the specified compute node.
[**poolRemoveNodes**](ComputeNodesApi.md#poolRemoveNodes) | **POST** /pools/{poolId}/removenodes | Removes compute nodes from the specified pool.



## computeNodeAddUser

> computeNodeAddUser(poolId, nodeId, apiVersion, user, opts)

Adds a user account to the specified compute node.

You can add a user account to a node only when it is in the idle or running state.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the machine on which you want to create a user account.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let user = new BatchService.ComputeNodeUser(); // ComputeNodeUser | The user account to be created.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeAddUser(poolId, nodeId, apiVersion, user, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the machine on which you want to create a user account. | 
 **apiVersion** | **String**| Client API Version. | 
 **user** | [**ComputeNodeUser**](ComputeNodeUser.md)| The user account to be created. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## computeNodeDeleteUser

> computeNodeDeleteUser(poolId, nodeId, userName, apiVersion, opts)

Deletes a user account from the specified compute node.

You can delete a user account to a node only when it is in the idle or running state.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the machine on which you want to delete a user account.
let userName = "userName_example"; // String | The name of the user account to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeDeleteUser(poolId, nodeId, userName, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the machine on which you want to delete a user account. | 
 **userName** | **String**| The name of the user account to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## computeNodeDisableScheduling

> computeNodeDisableScheduling(poolId, nodeId, apiVersion, opts)

Disables task scheduling on the specified compute node.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node on which you want to disable task scheduling.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'nodeDisableSchedulingParameter': new BatchService.NodeDisableSchedulingParameter() // NodeDisableSchedulingParameter | The parameters for the request.
};
apiInstance.computeNodeDisableScheduling(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node on which you want to disable task scheduling. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **nodeDisableSchedulingParameter** | [**NodeDisableSchedulingParameter**](NodeDisableSchedulingParameter.md)| The parameters for the request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## computeNodeEnableScheduling

> computeNodeEnableScheduling(poolId, nodeId, apiVersion, opts)

Enables task scheduling on the specified compute node.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node on which you want to enable task scheduling.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeEnableScheduling(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node on which you want to enable task scheduling. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## computeNodeGet

> ComputeNode computeNodeGet(poolId, nodeId, apiVersion, opts)

Gets information about the specified compute node.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node that you want to get information about.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | An OData $select clause.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeGet(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node that you want to get information about. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| An OData $select clause. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**ComputeNode**](ComputeNode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## computeNodeGetRemoteDesktop

> File computeNodeGetRemoteDesktop(poolId, nodeId, apiVersion, opts)

Gets the Remote Desktop Protocol file for the specified compute node.

Before you can access a node by using the RDP file, you must create a user account on the node. This API can only be invoked on pools created with the cloud service configuration property.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node for which you want to get the Remote Desktop Protocol file.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeGetRemoteDesktop(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node for which you want to get the Remote Desktop Protocol file. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## computeNodeGetRemoteLoginSettings

> ComputeNodeGetRemoteLoginSettingsResult computeNodeGetRemoteLoginSettings(poolId, nodeId, apiVersion, opts)

Gets the settings required for remote login to a compute node.

Before you can remotely login to a node using the remote login settings, you must create a user account on the node. This API can be invoked only on pools created with the virtual machine configuration property.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node for which to obtain the remote login settings.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeGetRemoteLoginSettings(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node for which to obtain the remote login settings. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**ComputeNodeGetRemoteLoginSettingsResult**](ComputeNodeGetRemoteLoginSettingsResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## computeNodeList

> ComputeNodeListResult computeNodeList(poolId, apiVersion, opts)

Lists the compute nodes in the specified pool.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool from which you want to list nodes.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause..
  'select': "select_example", // String | An OData $select clause.
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 nodes can be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeList(poolId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool from which you want to list nodes. | 
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause.. | [optional] 
 **select** | **String**| An OData $select clause. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 nodes can be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**ComputeNodeListResult**](ComputeNodeListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## computeNodeReboot

> computeNodeReboot(poolId, nodeId, apiVersion, opts)

Restarts the specified compute node.

You can restart a node only if it is in an idle or running state.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node that you want to restart.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'nodeRebootParameter': new BatchService.NodeRebootParameter() // NodeRebootParameter | The parameters for the request.
};
apiInstance.computeNodeReboot(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node that you want to restart. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **nodeRebootParameter** | [**NodeRebootParameter**](NodeRebootParameter.md)| The parameters for the request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## computeNodeReimage

> computeNodeReimage(poolId, nodeId, apiVersion, opts)

Reinstalls the operating system on the specified compute node.

You can reinstall the operating system on a node only if it is in an idle or running state. This API can be invoked only on pools created with the cloud service configuration property.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node that you want to restart.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'nodeReimageParameter': new BatchService.NodeReimageParameter() // NodeReimageParameter | The parameters for the request.
};
apiInstance.computeNodeReimage(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node that you want to restart. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **nodeReimageParameter** | [**NodeReimageParameter**](NodeReimageParameter.md)| The parameters for the request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## computeNodeUpdateUser

> computeNodeUpdateUser(poolId, nodeId, userName, apiVersion, nodeUpdateUserParameter, opts)

Updates the password or expiration time of a user account on the specified compute node.

This operation replaces of all the updatable properties of the account. For example, if the expiryTime element is not specified, the current value is replaced with the default value, not left unmodified. You can update a user account on a node only when it is in the idle or running state.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the machine on which you want to update a user account.
let userName = "userName_example"; // String | The name of the user account to update.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let nodeUpdateUserParameter = new BatchService.NodeUpdateUserParameter(); // NodeUpdateUserParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.computeNodeUpdateUser(poolId, nodeId, userName, apiVersion, nodeUpdateUserParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the machine on which you want to update a user account. | 
 **userName** | **String**| The name of the user account to update. | 
 **apiVersion** | **String**| Client API Version. | 
 **nodeUpdateUserParameter** | [**NodeUpdateUserParameter**](NodeUpdateUserParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## poolRemoveNodes

> poolRemoveNodes(poolId, apiVersion, nodeRemoveParameter, opts)

Removes compute nodes from the specified pool.

This operation can only run when the allocation state of the pool is steady. When this operation runs, the allocation state changes from steady to resizing.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.ComputeNodesApi();
let poolId = "poolId_example"; // String | The ID of the pool from which you want to remove nodes.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let nodeRemoveParameter = new BatchService.NodeRemoveParameter(); // NodeRemoveParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.poolRemoveNodes(poolId, apiVersion, nodeRemoveParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool from which you want to remove nodes. | 
 **apiVersion** | **String**| Client API Version. | 
 **nodeRemoveParameter** | [**NodeRemoveParameter**](NodeRemoveParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json

