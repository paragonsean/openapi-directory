# SeaBreezeManagementClient.CodePackagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codePackageGetContainerLogs**](CodePackagesApi.md#codePackageGetContainerLogs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName}/replicas/{replicaName}/codePackages/{codePackageName}/logs | Gets the logs from the container.



## codePackageGetContainerLogs

> ContainerLogs codePackageGetContainerLogs(subscriptionId, resourceGroupName, apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, opts)

Gets the logs from the container.

Gets the logs for the container of the specified code package of the service replica.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.CodePackagesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
let replicaName = "replicaName_example"; // String | Service Fabric replica name.
let codePackageName = "codePackageName_example"; // String | The name of code package of the service.
let opts = {
  'tail': 56 // Number | Number of lines to show from the end of the logs. Default is 100.
};
apiInstance.codePackageGetContainerLogs(subscriptionId, resourceGroupName, apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 
 **replicaName** | **String**| Service Fabric replica name. | 
 **codePackageName** | **String**| The name of code package of the service. | 
 **tail** | **Number**| Number of lines to show from the end of the logs. Default is 100. | [optional] 

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

