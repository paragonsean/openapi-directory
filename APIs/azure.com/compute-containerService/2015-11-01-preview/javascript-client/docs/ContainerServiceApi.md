# ContainerServiceClient.ContainerServiceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containerServiceCreateOrUpdate**](ContainerServiceApi.md#containerServiceCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/containerServices/{containerServiceName} | 
[**containerServiceDelete**](ContainerServiceApi.md#containerServiceDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/containerServices/{containerServiceName} | 
[**containerServiceGet**](ContainerServiceApi.md#containerServiceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/containerServices/{containerServiceName} | 
[**containerServiceListByResourceGroup**](ContainerServiceApi.md#containerServiceListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/containerServices | 



## containerServiceCreateOrUpdate

> ContainerService containerServiceCreateOrUpdate(resourceGroupName, containerServiceName, apiVersion, subscriptionId, parameters)



The operation to create or update a container service.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ContainerServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let containerServiceName = "containerServiceName_example"; // String | The name of the container service within the given subscription and resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ContainerServiceClient.ContainerService(); // ContainerService | Parameters supplied to the Create Container Service operation.
apiInstance.containerServiceCreateOrUpdate(resourceGroupName, containerServiceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **containerServiceName** | **String**| The name of the container service within the given subscription and resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ContainerService**](ContainerService.md)| Parameters supplied to the Create Container Service operation. | 

### Return type

[**ContainerService**](ContainerService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## containerServiceDelete

> containerServiceDelete(resourceGroupName, containerServiceName, apiVersion, subscriptionId)



The operation to delete a container service.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ContainerServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let containerServiceName = "containerServiceName_example"; // String | The name of the container service within the given subscription and resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.containerServiceDelete(resourceGroupName, containerServiceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **containerServiceName** | **String**| The name of the container service within the given subscription and resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containerServiceGet

> ContainerService containerServiceGet(resourceGroupName, containerServiceName, apiVersion, subscriptionId)



The operation to get a container service.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ContainerServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let containerServiceName = "containerServiceName_example"; // String | The name of the container service within the given subscription and resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.containerServiceGet(resourceGroupName, containerServiceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **containerServiceName** | **String**| The name of the container service within the given subscription and resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ContainerService**](ContainerService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## containerServiceListByResourceGroup

> ContainerServiceListResult containerServiceListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



The operation to list container services.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ContainerServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.containerServiceListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ContainerServiceListResult**](ContainerServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

