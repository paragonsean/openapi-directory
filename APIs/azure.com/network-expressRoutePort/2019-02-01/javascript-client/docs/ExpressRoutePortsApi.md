# NetworkManagementClient.ExpressRoutePortsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRoutePortsCreateOrUpdate**](ExpressRoutePortsApi.md#expressRoutePortsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} | 
[**expressRoutePortsDelete**](ExpressRoutePortsApi.md#expressRoutePortsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} | 
[**expressRoutePortsGet**](ExpressRoutePortsApi.md#expressRoutePortsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} | 
[**expressRoutePortsList**](ExpressRoutePortsApi.md#expressRoutePortsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePorts | 
[**expressRoutePortsListByResourceGroup**](ExpressRoutePortsApi.md#expressRoutePortsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts | 
[**expressRoutePortsUpdateTags**](ExpressRoutePortsApi.md#expressRoutePortsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} | 



## expressRoutePortsCreateOrUpdate

> ExpressRoutePort expressRoutePortsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters)



Creates or updates the specified ExpressRoutePort resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
let parameters = new NetworkManagementClient.ExpressRoutePort(); // ExpressRoutePort | Parameters supplied to the create ExpressRoutePort operation.
apiInstance.expressRoutePortsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | 
 **parameters** | [**ExpressRoutePort**](ExpressRoutePort.md)| Parameters supplied to the create ExpressRoutePort operation. | 

### Return type

[**ExpressRoutePort**](ExpressRoutePort.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expressRoutePortsDelete

> expressRoutePortsDelete(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName)



Deletes the specified ExpressRoutePort resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
apiInstance.expressRoutePortsDelete(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expressRoutePortsGet

> ExpressRoutePort expressRoutePortsGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName)



Retrieves the requested ExpressRoutePort resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRoutePortName = "expressRoutePortName_example"; // String | The name of ExpressRoutePort.
apiInstance.expressRoutePortsGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **expressRoutePortName** | **String**| The name of ExpressRoutePort. | 

### Return type

[**ExpressRoutePort**](ExpressRoutePort.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRoutePortsList

> ExpressRoutePortListResult expressRoutePortsList(subscriptionId, apiVersion)



List all the ExpressRoutePort resources in the specified subscription

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.expressRoutePortsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**ExpressRoutePortListResult**](ExpressRoutePortListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRoutePortsListByResourceGroup

> ExpressRoutePortListResult expressRoutePortsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)



List all the ExpressRoutePort resources in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
apiInstance.expressRoutePortsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| The name of the resource group. | 

### Return type

[**ExpressRoutePortListResult**](ExpressRoutePortListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRoutePortsUpdateTags

> ExpressRoutePort expressRoutePortsUpdateTags(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters)



Update ExpressRoutePort tags

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
let parameters = new NetworkManagementClient.ExpressRoutePortsUpdateTagsRequest(); // ExpressRoutePortsUpdateTagsRequest | Parameters supplied to update ExpressRoutePort resource tags.
apiInstance.expressRoutePortsUpdateTags(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | 
 **parameters** | [**ExpressRoutePortsUpdateTagsRequest**](ExpressRoutePortsUpdateTagsRequest.md)| Parameters supplied to update ExpressRoutePort resource tags. | 

### Return type

[**ExpressRoutePort**](ExpressRoutePort.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

