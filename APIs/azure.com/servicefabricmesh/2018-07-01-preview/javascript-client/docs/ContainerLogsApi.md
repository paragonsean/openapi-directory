# SeaBreezeManagementClient.ContainerLogsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codePackageGetContainerLog**](ContainerLogsApi.md#codePackageGetContainerLog) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services/{serviceName}/replicas/{replicaName}/codePackages/{codePackageName}/logs | Gets the logs for the container.



## codePackageGetContainerLog

> ContainerLogs codePackageGetContainerLog(subscriptionId, resourceGroupName, apiVersion, applicationName, serviceName, replicaName, codePackageName, opts)

Gets the logs for the container.

Get the logs for the container of a given code package of an application.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ContainerLogsApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let applicationName = "applicationName_example"; // String | The identity of the application.
let serviceName = "serviceName_example"; // String | The identity of the service.
let replicaName = "replicaName_example"; // String | The identity of the service replica.
let codePackageName = "codePackageName_example"; // String | The name of the code package.
let opts = {
  'tail': 56 // Number | Number of lines to show from the end of the logs. Default is 100.
};
apiInstance.codePackageGetContainerLog(subscriptionId, resourceGroupName, apiVersion, applicationName, serviceName, replicaName, codePackageName, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **resourceGroupName** | **String**| Azure resource group name | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **applicationName** | **String**| The identity of the application. | 
 **serviceName** | **String**| The identity of the service. | 
 **replicaName** | **String**| The identity of the service replica. | 
 **codePackageName** | **String**| The name of the code package. | 
 **tail** | **Number**| Number of lines to show from the end of the logs. Default is 100. | [optional] 

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

