# SiteRecoveryManagementClient.ReplicationNetworkMappingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationNetworkMappingsCreate**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Creates network mapping.
[**replicationNetworkMappingsDelete**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Delete network mapping.
[**replicationNetworkMappingsGet**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Gets network mapping by name.
[**replicationNetworkMappingsList**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationNetworkMappings | Gets all the network mappings under a vault.
[**replicationNetworkMappingsListByReplicationNetworks**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsListByReplicationNetworks) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings | Gets all the network mappings under a network.
[**replicationNetworkMappingsUpdate**](ReplicationNetworkMappingsApi.md#replicationNetworkMappingsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName} | Updates network mapping.



## replicationNetworkMappingsCreate

> NetworkMapping replicationNetworkMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input)

Creates network mapping.

The operation to create an ASR network mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationNetworkMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Primary fabric name.
let networkName = "networkName_example"; // String | Primary network name.
let networkMappingName = "networkMappingName_example"; // String | Network mapping name.
let input = new SiteRecoveryManagementClient.CreateNetworkMappingInput(); // CreateNetworkMappingInput | Create network mapping input.
apiInstance.replicationNetworkMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Primary fabric name. | 
 **networkName** | **String**| Primary network name. | 
 **networkMappingName** | **String**| Network mapping name. | 
 **input** | [**CreateNetworkMappingInput**](CreateNetworkMappingInput.md)| Create network mapping input. | 

### Return type

[**NetworkMapping**](NetworkMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationNetworkMappingsDelete

> replicationNetworkMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName)

Delete network mapping.

The operation to delete a network mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationNetworkMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Primary fabric name.
let networkName = "networkName_example"; // String | Primary network name.
let networkMappingName = "networkMappingName_example"; // String | ARM Resource Name for network mapping.
apiInstance.replicationNetworkMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Primary fabric name. | 
 **networkName** | **String**| Primary network name. | 
 **networkMappingName** | **String**| ARM Resource Name for network mapping. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationNetworkMappingsGet

> NetworkMapping replicationNetworkMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName)

Gets network mapping by name.

Gets the details of an ASR network mapping

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationNetworkMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Primary fabric name.
let networkName = "networkName_example"; // String | Primary network name.
let networkMappingName = "networkMappingName_example"; // String | Network mapping name.
apiInstance.replicationNetworkMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Primary fabric name. | 
 **networkName** | **String**| Primary network name. | 
 **networkMappingName** | **String**| Network mapping name. | 

### Return type

[**NetworkMapping**](NetworkMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationNetworkMappingsList

> NetworkMappingCollection replicationNetworkMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets all the network mappings under a vault.

Lists all ASR network mappings in the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationNetworkMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationNetworkMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 

### Return type

[**NetworkMappingCollection**](NetworkMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationNetworkMappingsListByReplicationNetworks

> NetworkMappingCollection replicationNetworkMappingsListByReplicationNetworks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName)

Gets all the network mappings under a network.

Lists all ASR network mappings for the specified network.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationNetworkMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Primary fabric name.
let networkName = "networkName_example"; // String | Primary network name.
apiInstance.replicationNetworkMappingsListByReplicationNetworks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Primary fabric name. | 
 **networkName** | **String**| Primary network name. | 

### Return type

[**NetworkMappingCollection**](NetworkMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationNetworkMappingsUpdate

> NetworkMapping replicationNetworkMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input)

Updates network mapping.

The operation to update an ASR network mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationNetworkMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Primary fabric name.
let networkName = "networkName_example"; // String | Primary network name.
let networkMappingName = "networkMappingName_example"; // String | Network mapping name.
let input = new SiteRecoveryManagementClient.UpdateNetworkMappingInput(); // UpdateNetworkMappingInput | Update network mapping input.
apiInstance.replicationNetworkMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, networkName, networkMappingName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Primary fabric name. | 
 **networkName** | **String**| Primary network name. | 
 **networkMappingName** | **String**| Network mapping name. | 
 **input** | [**UpdateNetworkMappingInput**](UpdateNetworkMappingInput.md)| Update network mapping input. | 

### Return type

[**NetworkMapping**](NetworkMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

