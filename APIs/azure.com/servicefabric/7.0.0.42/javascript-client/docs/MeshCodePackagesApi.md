# ServiceFabricClientApis.MeshCodePackagesApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshCodePackageGetContainerLogs**](MeshCodePackagesApi.md#meshCodePackageGetContainerLogs) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas/{replicaName}/CodePackages/{codePackageName}/Logs | Gets the logs from the container.



## meshCodePackageGetContainerLogs

> ContainerLogs meshCodePackageGetContainerLogs(apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, opts)

Gets the logs from the container.

Gets the logs for the container of the specified code package of the service replica.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshCodePackagesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
let replicaName = "replicaName_example"; // String | Service Fabric replica name.
let codePackageName = "codePackageName_example"; // String | The name of code package of the service.
let opts = {
  'tail': "tail_example" // String | Number of lines to show from the end of the logs. Default is 100. 'all' to show the complete logs.
};
apiInstance.meshCodePackageGetContainerLogs(apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 
 **replicaName** | **String**| Service Fabric replica name. | 
 **codePackageName** | **String**| The name of code package of the service. | 
 **tail** | **String**| Number of lines to show from the end of the logs. Default is 100. &#39;all&#39; to show the complete logs. | [optional] 

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

