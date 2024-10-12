# SeaBreezeManagementClient.ReplicasApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicaGet**](ReplicasApi.md#replicaGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services/{serviceName}/replicas/{replicaName} | Gets a specific replica of a given service.
[**replicaListByServiceName**](ReplicasApi.md#replicaListByServiceName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services/{serviceName}/replicas | Gets replicas of a given service.



## replicaGet

> ServiceReplicaDescription replicaGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName, replicaName)

Gets a specific replica of a given service.

Gets the information about the specified replica of a given service of an application. The information includes the runtime properties of the replica instance.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ReplicasApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationName = "applicationName_example"; // String | The identity of the application.
let serviceName = "serviceName_example"; // String | The identity of the service.
let replicaName = "replicaName_example"; // String | The identity of the service replica.
apiInstance.replicaGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName, replicaName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationName** | **String**| The identity of the application. | 
 **serviceName** | **String**| The identity of the service. | 
 **replicaName** | **String**| The identity of the service replica. | 

### Return type

[**ServiceReplicaDescription**](ServiceReplicaDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicaListByServiceName

> ServiceReplicaList replicaListByServiceName(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName)

Gets replicas of a given service.

Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ReplicasApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationName = "applicationName_example"; // String | The identity of the application.
let serviceName = "serviceName_example"; // String | The identity of the service.
apiInstance.replicaListByServiceName(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationName** | **String**| The identity of the application. | 
 **serviceName** | **String**| The identity of the service. | 

### Return type

[**ServiceReplicaList**](ServiceReplicaList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

