# NetworkManagementClient.LocalNetworkGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**localNetworkGatewaysCreateOrUpdate**](LocalNetworkGatewaysApi.md#localNetworkGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} | 
[**localNetworkGatewaysDelete**](LocalNetworkGatewaysApi.md#localNetworkGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} | 
[**localNetworkGatewaysGet**](LocalNetworkGatewaysApi.md#localNetworkGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} | 
[**localNetworkGatewaysList**](LocalNetworkGatewaysApi.md#localNetworkGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways | 



## localNetworkGatewaysCreateOrUpdate

> LocalNetworkGateway localNetworkGatewaysCreateOrUpdate(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters)



The Put LocalNetworkGateway operation creates/updates a local network gateway in the specified resource group through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.LocalNetworkGateway(); // LocalNetworkGateway | Parameters supplied to the Begin Create or update Local Network Gateway operation through Network resource provider.
apiInstance.localNetworkGatewaysCreateOrUpdate(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **localNetworkGatewayName** | **String**| The name of the local network gateway. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**LocalNetworkGateway**](LocalNetworkGateway.md)| Parameters supplied to the Begin Create or update Local Network Gateway operation through Network resource provider. | 

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## localNetworkGatewaysDelete

> localNetworkGatewaysDelete(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId)



The Delete LocalNetworkGateway operation deletes the specified local network Gateway through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.localNetworkGatewaysDelete(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **localNetworkGatewayName** | **String**| The name of the local network gateway. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## localNetworkGatewaysGet

> LocalNetworkGateway localNetworkGatewaysGet(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId)



The Get LocalNetworkGateway operation retrieves information about the specified local network gateway through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.localNetworkGatewaysGet(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **localNetworkGatewayName** | **String**| The name of the local network gateway. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## localNetworkGatewaysList

> LocalNetworkGatewayListResult localNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId)



The List LocalNetworkGateways operation retrieves all the local network gateways stored.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.localNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LocalNetworkGatewayListResult**](LocalNetworkGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

