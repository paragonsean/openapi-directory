# NetworkManagementClient.VirtualNetworkGatewayConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworkGatewayConnectionsCreateOrUpdate**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName} | 
[**virtualNetworkGatewayConnectionsDelete**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName} | 
[**virtualNetworkGatewayConnectionsGet**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName} | 
[**virtualNetworkGatewayConnectionsGetSharedKey**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsGetSharedKey) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey | 
[**virtualNetworkGatewayConnectionsList**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections | 
[**virtualNetworkGatewayConnectionsResetSharedKey**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsResetSharedKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey/reset | 
[**virtualNetworkGatewayConnectionsSetSharedKey**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsSetSharedKey) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey | 
[**virtualNetworkGatewayConnectionsStartPacketCapture**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsStartPacketCapture) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/startPacketCapture | 
[**virtualNetworkGatewayConnectionsStopPacketCapture**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsStopPacketCapture) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/stopPacketCapture | 
[**virtualNetworkGatewayConnectionsUpdateTags**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName} | 



## virtualNetworkGatewayConnectionsCreateOrUpdate

> VirtualNetworkGatewayConnection virtualNetworkGatewayConnectionsCreateOrUpdate(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



Creates or updates a virtual network gateway connection in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualNetworkGatewayConnection(); // VirtualNetworkGatewayConnection | Parameters supplied to the create or update virtual network gateway connection operation.
apiInstance.virtualNetworkGatewayConnectionsCreateOrUpdate(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkGatewayConnection**](VirtualNetworkGatewayConnection.md)| Parameters supplied to the create or update virtual network gateway connection operation. | 

### Return type

[**VirtualNetworkGatewayConnection**](VirtualNetworkGatewayConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewayConnectionsDelete

> virtualNetworkGatewayConnectionsDelete(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId)



Deletes the specified virtual network Gateway connection.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewayConnectionsDelete(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualNetworkGatewayConnectionsGet

> VirtualNetworkGatewayConnection virtualNetworkGatewayConnectionsGet(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId)



Gets the specified virtual network gateway connection by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewayConnectionsGet(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkGatewayConnection**](VirtualNetworkGatewayConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewayConnectionsGetSharedKey

> ConnectionSharedKey virtualNetworkGatewayConnectionsGetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId)



The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the specified virtual network gateway connection shared key through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The virtual network gateway connection shared key name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewayConnectionsGetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The virtual network gateway connection shared key name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ConnectionSharedKey**](ConnectionSharedKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewayConnectionsList

> VirtualNetworkGatewayConnectionListResult virtualNetworkGatewayConnectionsList(resourceGroupName, apiVersion, subscriptionId)



The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewayConnectionsList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualNetworkGatewayConnectionListResult**](VirtualNetworkGatewayConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkGatewayConnectionsResetSharedKey

> ConnectionResetSharedKey virtualNetworkGatewayConnectionsResetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The virtual network gateway connection reset shared key Name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ConnectionResetSharedKey(); // ConnectionResetSharedKey | Parameters supplied to the begin reset virtual network gateway connection shared key operation through network resource provider.
apiInstance.virtualNetworkGatewayConnectionsResetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The virtual network gateway connection reset shared key Name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ConnectionResetSharedKey**](ConnectionResetSharedKey.md)| Parameters supplied to the begin reset virtual network gateway connection shared key operation through network resource provider. | 

### Return type

[**ConnectionResetSharedKey**](ConnectionResetSharedKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewayConnectionsSetSharedKey

> ConnectionSharedKey virtualNetworkGatewayConnectionsSetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The virtual network gateway connection name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ConnectionSharedKey(); // ConnectionSharedKey | Parameters supplied to the Begin Set Virtual Network Gateway connection Shared key operation throughNetwork resource provider.
apiInstance.virtualNetworkGatewayConnectionsSetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The virtual network gateway connection name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ConnectionSharedKey**](ConnectionSharedKey.md)| Parameters supplied to the Begin Set Virtual Network Gateway connection Shared key operation throughNetwork resource provider. | 

### Return type

[**ConnectionSharedKey**](ConnectionSharedKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewayConnectionsStartPacketCapture

> String virtualNetworkGatewayConnectionsStartPacketCapture(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, opts)



Starts packet capture on virtual network gateway connection in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'parameters': new NetworkManagementClient.VpnPacketCaptureStartParameters() // VpnPacketCaptureStartParameters | Virtual network gateway packet capture parameters supplied to start packet capture on gateway connection.
};
apiInstance.virtualNetworkGatewayConnectionsStartPacketCapture(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VpnPacketCaptureStartParameters**](VpnPacketCaptureStartParameters.md)| Virtual network gateway packet capture parameters supplied to start packet capture on gateway connection. | [optional] 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewayConnectionsStopPacketCapture

> String virtualNetworkGatewayConnectionsStopPacketCapture(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



Stops packet capture on virtual network gateway connection in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway Connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VpnPacketCaptureStopParameters(); // VpnPacketCaptureStopParameters | Virtual network gateway packet capture parameters supplied to stop packet capture on gateway connection.
apiInstance.virtualNetworkGatewayConnectionsStopPacketCapture(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway Connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VpnPacketCaptureStopParameters**](VpnPacketCaptureStopParameters.md)| Virtual network gateway packet capture parameters supplied to stop packet capture on gateway connection. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkGatewayConnectionsUpdateTags

> VirtualNetworkGatewayConnection virtualNetworkGatewayConnectionsUpdateTags(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



Updates a virtual network gateway connection tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewayConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualNetworkGatewayConnectionsUpdateTagsRequest(); // VirtualNetworkGatewayConnectionsUpdateTagsRequest | Parameters supplied to update virtual network gateway connection tags.
apiInstance.virtualNetworkGatewayConnectionsUpdateTags(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkGatewayConnectionsUpdateTagsRequest**](VirtualNetworkGatewayConnectionsUpdateTagsRequest.md)| Parameters supplied to update virtual network gateway connection tags. | 

### Return type

[**VirtualNetworkGatewayConnection**](VirtualNetworkGatewayConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

