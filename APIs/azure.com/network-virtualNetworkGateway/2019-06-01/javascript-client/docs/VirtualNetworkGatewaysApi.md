# NetworkManagementClient.VirtualNetworkGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworkGatewaysCreateOrUpdate**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} | 
[**virtualNetworkGatewaysDelete**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} | 
[**virtualNetworkGatewaysGenerateVpnProfile**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGenerateVpnProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/generatevpnprofile | 
[**virtualNetworkGatewaysGeneratevpnclientpackage**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGeneratevpnclientpackage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/generatevpnclientpackage | 
[**virtualNetworkGatewaysGet**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} | 
[**virtualNetworkGatewaysGetAdvertisedRoutes**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetAdvertisedRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getAdvertisedRoutes | 
[**virtualNetworkGatewaysGetBgpPeerStatus**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetBgpPeerStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getBgpPeerStatus | 
[**virtualNetworkGatewaysGetLearnedRoutes**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetLearnedRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getLearnedRoutes | 
[**virtualNetworkGatewaysGetVpnProfilePackageUrl**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetVpnProfilePackageUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getvpnprofilepackageurl | 
[**virtualNetworkGatewaysGetVpnclientConnectionHealth**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetVpnclientConnectionHealth) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getVpnClientConnectionHealth | 
[**virtualNetworkGatewaysGetVpnclientIpsecParameters**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetVpnclientIpsecParameters) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getvpnclientipsecparameters | 
[**virtualNetworkGatewaysList**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways | 
[**virtualNetworkGatewaysListConnections**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysListConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/connections | 
[**virtualNetworkGatewaysReset**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/reset | 
[**virtualNetworkGatewaysResetVpnClientSharedKey**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysResetVpnClientSharedKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/resetvpnclientsharedkey | 
[**virtualNetworkGatewaysSetVpnclientIpsecParameters**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysSetVpnclientIpsecParameters) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/setvpnclientipsecparameters | 
[**virtualNetworkGatewaysSupportedVpnDevices**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysSupportedVpnDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/supportedvpndevices | 
[**virtualNetworkGatewaysUpdateTags**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} | 
[**virtualNetworkGatewaysVpnDeviceConfigurationScript**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysVpnDeviceConfigurationScript) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/vpndeviceconfigurationscript | 



## virtualNetworkGatewaysCreateOrUpdate

> VirtualNetworkGateway virtualNetworkGatewaysCreateOrUpdate(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Creates or updates a virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualNetworkGateway(); // VirtualNetworkGateway | Parameters supplied to create or update virtual network gateway operation.
apiInstance.virtualNetworkGatewaysCreateOrUpdate(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md)| Parameters supplied to create or update virtual network gateway operation. | 

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewaysDelete

> virtualNetworkGatewaysDelete(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Deletes the specified virtual network gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysDelete(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualNetworkGatewaysGenerateVpnProfile

> String virtualNetworkGatewaysGenerateVpnProfile(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Generates VPN profile for P2S client of the virtual network gateway in the specified resource group. Used for IKEV2 and radius based authentication.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VpnClientParameters(); // VpnClientParameters | Parameters supplied to the generate virtual network gateway VPN client package operation.
apiInstance.virtualNetworkGatewaysGenerateVpnProfile(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VpnClientParameters**](VpnClientParameters.md)| Parameters supplied to the generate virtual network gateway VPN client package operation. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewaysGeneratevpnclientpackage

> String virtualNetworkGatewaysGeneratevpnclientpackage(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Generates VPN client package for P2S client of the virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VpnClientParameters(); // VpnClientParameters | Parameters supplied to the generate virtual network gateway VPN client package operation.
apiInstance.virtualNetworkGatewaysGeneratevpnclientpackage(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VpnClientParameters**](VpnClientParameters.md)| Parameters supplied to the generate virtual network gateway VPN client package operation. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewaysGet

> VirtualNetworkGateway virtualNetworkGatewaysGet(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets the specified virtual network gateway by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysGet(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysGetAdvertisedRoutes

> GatewayRouteListResult virtualNetworkGatewaysGetAdvertisedRoutes(resourceGroupName, virtualNetworkGatewayName, peer, apiVersion, subscriptionId)



This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let peer = "peer_example"; // String | The IP address of the peer.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysGetAdvertisedRoutes(resourceGroupName, virtualNetworkGatewayName, peer, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **peer** | **String**| The IP address of the peer. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**GatewayRouteListResult**](GatewayRouteListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysGetBgpPeerStatus

> BgpPeerStatusListResult virtualNetworkGatewaysGetBgpPeerStatus(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, opts)



The GetBgpPeerStatus operation retrieves the status of all BGP peers.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'peer': "peer_example" // String | The IP address of the peer to retrieve the status of.
};
apiInstance.virtualNetworkGatewaysGetBgpPeerStatus(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **peer** | **String**| The IP address of the peer to retrieve the status of. | [optional] 

### Return type

[**BgpPeerStatusListResult**](BgpPeerStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysGetLearnedRoutes

> GatewayRouteListResult virtualNetworkGatewaysGetLearnedRoutes(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysGetLearnedRoutes(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**GatewayRouteListResult**](GatewayRouteListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysGetVpnProfilePackageUrl

> String virtualNetworkGatewaysGetVpnProfilePackageUrl(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysGetVpnProfilePackageUrl(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysGetVpnclientConnectionHealth

> VpnClientConnectionHealthDetailListResult virtualNetworkGatewaysGetVpnclientConnectionHealth(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Get VPN client connection health detail per P2S client connection of the virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysGetVpnclientConnectionHealth(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VpnClientConnectionHealthDetailListResult**](VpnClientConnectionHealthDetailListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysGetVpnclientIpsecParameters

> VpnClientIPsecParameters virtualNetworkGatewaysGetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



The Get VpnclientIpsecParameters operation retrieves information about the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The virtual network gateway name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysGetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The virtual network gateway name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VpnClientIPsecParameters**](VpnClientIPsecParameters.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysList

> VirtualNetworkGatewayListResult virtualNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId)



Gets all virtual network gateways by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkGatewayListResult**](VirtualNetworkGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysListConnections

> VirtualNetworkGatewayListConnectionsResult virtualNetworkGatewaysListConnections(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets all the connections in a virtual network gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysListConnections(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkGatewayListConnectionsResult**](VirtualNetworkGatewayListConnectionsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysReset

> VirtualNetworkGateway virtualNetworkGatewaysReset(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, opts)



Resets the primary of the virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'gatewayVip': "gatewayVip_example" // String | Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway.
};
apiInstance.virtualNetworkGatewaysReset(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **gatewayVip** | **String**| Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway. | [optional] 

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysResetVpnClientSharedKey

> virtualNetworkGatewaysResetVpnClientSharedKey(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Resets the VPN client shared key of the virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysResetVpnClientSharedKey(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualNetworkGatewaysSetVpnclientIpsecParameters

> VpnClientIPsecParameters virtualNetworkGatewaysSetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, vpnclientIpsecParams)



The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let vpnclientIpsecParams = new NetworkManagementClient.VpnClientIPsecParameters(); // VpnClientIPsecParameters | Parameters supplied to the Begin Set vpnclient ipsec parameters of Virtual Network Gateway P2S client operation through Network resource provider.
apiInstance.virtualNetworkGatewaysSetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, vpnclientIpsecParams, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **vpnclientIpsecParams** | [**VpnClientIPsecParameters**](VpnClientIPsecParameters.md)| Parameters supplied to the Begin Set vpnclient ipsec parameters of Virtual Network Gateway P2S client operation through Network resource provider. | 

### Return type

[**VpnClientIPsecParameters**](VpnClientIPsecParameters.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewaysSupportedVpnDevices

> String virtualNetworkGatewaysSupportedVpnDevices(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets a xml format representation for supported vpn devices.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysSupportedVpnDevices(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewaysUpdateTags

> VirtualNetworkGateway virtualNetworkGatewaysUpdateTags(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Updates a virtual network gateway tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualNetworkGatewayConnectionsUpdateTagsRequest(); // VirtualNetworkGatewayConnectionsUpdateTagsRequest | Parameters supplied to update virtual network gateway tags.
apiInstance.virtualNetworkGatewaysUpdateTags(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkGatewayConnectionsUpdateTagsRequest**](VirtualNetworkGatewayConnectionsUpdateTagsRequest.md)| Parameters supplied to update virtual network gateway tags. | 

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewaysVpnDeviceConfigurationScript

> String virtualNetworkGatewaysVpnDeviceConfigurationScript(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



Gets a xml format representation for vpn device configuration script.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection for which the configuration script is generated.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VpnDeviceScriptParameters(); // VpnDeviceScriptParameters | Parameters supplied to the generate vpn device script operation.
apiInstance.virtualNetworkGatewaysVpnDeviceConfigurationScript(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection for which the configuration script is generated. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VpnDeviceScriptParameters**](VpnDeviceScriptParameters.md)| Parameters supplied to the generate vpn device script operation. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

