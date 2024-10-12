# SeaBreezeManagementClient.ServiceReplicasApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceReplicaGet**](ServiceReplicasApi.md#serviceReplicaGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName}/replicas/{replicaName} | Gets the given replica of the service of an application.
[**serviceReplicaList**](ServiceReplicasApi.md#serviceReplicaList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName}/replicas | Gets replicas of a given service.



## serviceReplicaGet

> ServiceReplicaDescription serviceReplicaGet(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName, replicaName)

Gets the given replica of the service of an application.

Gets the information about the service replica with the given name. The information include the description and other properties of the service replica.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ServiceReplicasApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
let replicaName = "replicaName_example"; // String | Service Fabric replica name.
apiInstance.serviceReplicaGet(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName, replicaName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 
 **replicaName** | **String**| Service Fabric replica name. | 

### Return type

[**ServiceReplicaDescription**](ServiceReplicaDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceReplicaList

> ServiceReplicaDescriptionList serviceReplicaList(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName)

Gets replicas of a given service.

Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ServiceReplicasApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
apiInstance.serviceReplicaList(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 

### Return type

[**ServiceReplicaDescriptionList**](ServiceReplicaDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

