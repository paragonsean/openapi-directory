# NetworkResourceProviderClient.SubnetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subnetsCreateOrUpdate**](SubnetsApi.md#subnetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualnetworks/{virtualNetworkName}/subnets/{subnetName} | 
[**subnetsDelete**](SubnetsApi.md#subnetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualnetworks/{virtualNetworkName}/subnets/{subnetName} | 
[**subnetsGet**](SubnetsApi.md#subnetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualnetworks/{virtualNetworkName}/subnets/{subnetName} | 
[**subnetsList**](SubnetsApi.md#subnetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualnetworks/{virtualNetworkName}/subnets | 



## subnetsCreateOrUpdate

> Subnet subnetsCreateOrUpdate(resourceGroupName, virtualNetworkName, subnetName, apiVersion, subscriptionId, subnetParameters)



The Put Subnet operation creates/updates a subnet in the specified virtual network

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.SubnetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let subnetName = "subnetName_example"; // String | The name of the subnet.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let subnetParameters = new NetworkResourceProviderClient.Subnet(); // Subnet | Parameters supplied to the create/update Subnet operation
apiInstance.subnetsCreateOrUpdate(resourceGroupName, virtualNetworkName, subnetName, apiVersion, subscriptionId, subnetParameters, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **subnetName** | **String**| The name of the subnet. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **subnetParameters** | [**Subnet**](Subnet.md)| Parameters supplied to the create/update Subnet operation | 

### Return type

[**Subnet**](Subnet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## subnetsDelete

> subnetsDelete(resourceGroupName, virtualNetworkName, subnetName, apiVersion, subscriptionId)



The delete subnet operation deletes the specified subnet.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.SubnetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let subnetName = "subnetName_example"; // String | The name of the subnet.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.subnetsDelete(resourceGroupName, virtualNetworkName, subnetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **subnetName** | **String**| The name of the subnet. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## subnetsGet

> Subnet subnetsGet(resourceGroupName, virtualNetworkName, subnetName, apiVersion, subscriptionId)



The Get subnet operation retrieves information about the specified subnet.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.SubnetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let subnetName = "subnetName_example"; // String | The name of the subnet.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.subnetsGet(resourceGroupName, virtualNetworkName, subnetName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **subnetName** | **String**| The name of the subnet. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Subnet**](Subnet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## subnetsList

> SubnetListResult subnetsList(resourceGroupName, virtualNetworkName, apiVersion, subscriptionId)



The List subnets operation retrieves all the subnets in a virtual network.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.SubnetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.subnetsList(resourceGroupName, virtualNetworkName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SubnetListResult**](SubnetListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

