# KeyVaultManagementClient.PrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateEndpointConnectionsDelete**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsGet**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsPut**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName} | 



## privateEndpointConnectionsDelete

> PrivateEndpointConnection privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion)



Deletes the specified private endpoint connection associated with the key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
let vaultName = "vaultName_example"; // String | The name of the key vault.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Name of the private endpoint connection associated with the key vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | 
 **vaultName** | **String**| The name of the key vault. | 
 **privateEndpointConnectionName** | **String**| Name of the private endpoint connection associated with the key vault. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsGet

> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion)



Gets the specified private endpoint connection associated with the key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
let vaultName = "vaultName_example"; // String | The name of the key vault.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Name of the private endpoint connection associated with the key vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | 
 **vaultName** | **String**| The name of the key vault. | 
 **privateEndpointConnectionName** | **String**| Name of the private endpoint connection associated with the key vault. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsPut

> PrivateEndpointConnection privateEndpointConnectionsPut(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion, properties)



Updates the specified private endpoint connection associated with the key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
let vaultName = "vaultName_example"; // String | The name of the key vault.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Name of the private endpoint connection associated with the key vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let properties = new KeyVaultManagementClient.PrivateEndpointConnection(); // PrivateEndpointConnection | The intended state of private endpoint connection.
apiInstance.privateEndpointConnectionsPut(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion, properties, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | 
 **vaultName** | **String**| The name of the key vault. | 
 **privateEndpointConnectionName** | **String**| Name of the private endpoint connection associated with the key vault. | 
 **apiVersion** | **String**| Client Api Version. | 
 **properties** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| The intended state of private endpoint connection. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

