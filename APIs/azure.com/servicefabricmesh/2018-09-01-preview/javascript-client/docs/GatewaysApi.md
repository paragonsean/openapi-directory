# SeaBreezeManagementClient.GatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gatewayCreate**](GatewaysApi.md#gatewayCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/gateways/{gatewayResourceName} | Creates or updates a gateway resource.
[**gatewayDelete**](GatewaysApi.md#gatewayDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/gateways/{gatewayResourceName} | Deletes the gateway resource.
[**gatewayGet**](GatewaysApi.md#gatewayGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/gateways/{gatewayResourceName} | Gets the gateway resource with the given name.
[**gatewayListByResourceGroup**](GatewaysApi.md#gatewayListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/gateways | Gets all the gateway resources in a given resource group.
[**gatewayListBySubscription**](GatewaysApi.md#gatewayListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabricMesh/gateways | Gets all the gateway resources in a given subscription.



## gatewayCreate

> GatewayResourceDescription gatewayCreate(subscriptionId, apiVersion, resourceGroupName, gatewayResourceName, gatewayResourceDescription)

Creates or updates a gateway resource.

Creates a gateway resource with the specified name, description and properties. If a gateway resource with the same name exists, then it is updated with the specified description and properties. Use gateway resources to create a gateway for public connectivity for services within your application.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.GatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
let gatewayResourceDescription = new SeaBreezeManagementClient.GatewayResourceDescription(); // GatewayResourceDescription | Description for creating a Gateway resource.
apiInstance.gatewayCreate(subscriptionId, apiVersion, resourceGroupName, gatewayResourceName, gatewayResourceDescription, (error, data, response) => {
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
 **gatewayResourceName** | **String**| The identity of the gateway. | 
 **gatewayResourceDescription** | [**GatewayResourceDescription**](GatewayResourceDescription.md)| Description for creating a Gateway resource. | 

### Return type

[**GatewayResourceDescription**](GatewayResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gatewayDelete

> gatewayDelete(subscriptionId, apiVersion, resourceGroupName, gatewayResourceName)

Deletes the gateway resource.

Deletes the gateway resource identified by the name.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.GatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
apiInstance.gatewayDelete(subscriptionId, apiVersion, resourceGroupName, gatewayResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **gatewayResourceName** | **String**| The identity of the gateway. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gatewayGet

> GatewayResourceDescription gatewayGet(subscriptionId, apiVersion, resourceGroupName, gatewayResourceName)

Gets the gateway resource with the given name.

Gets the information about the gateway resource with the given name. The information include the description and other properties of the gateway.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.GatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
apiInstance.gatewayGet(subscriptionId, apiVersion, resourceGroupName, gatewayResourceName, (error, data, response) => {
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
 **gatewayResourceName** | **String**| The identity of the gateway. | 

### Return type

[**GatewayResourceDescription**](GatewayResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gatewayListByResourceGroup

> GatewayResourceDescriptionList gatewayListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Gets all the gateway resources in a given resource group.

Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.GatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
apiInstance.gatewayListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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

### Return type

[**GatewayResourceDescriptionList**](GatewayResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gatewayListBySubscription

> GatewayResourceDescriptionList gatewayListBySubscription(subscriptionId, apiVersion)

Gets all the gateway resources in a given subscription.

Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the gateway.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.GatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
apiInstance.gatewayListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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

### Return type

[**GatewayResourceDescriptionList**](GatewayResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

