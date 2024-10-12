# SiteRecoveryManagementClient.ReplicationStorageClassificationMappingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationStorageClassificationMappingsCreate**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName} | Create storage classification mapping.
[**replicationStorageClassificationMappingsDelete**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName} | Delete a storage classification mapping.
[**replicationStorageClassificationMappingsGet**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings/{storageClassificationMappingName} | Gets the details of a storage classification mapping.
[**replicationStorageClassificationMappingsList**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationStorageClassificationMappings | Gets the list of storage classification mappings objects under a vault.
[**replicationStorageClassificationMappingsListByReplicationStorageClassifications**](ReplicationStorageClassificationMappingsApi.md#replicationStorageClassificationMappingsListByReplicationStorageClassifications) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationStorageClassifications/{storageClassificationName}/replicationStorageClassificationMappings | Gets the list of storage classification mappings objects under a storage.



## replicationStorageClassificationMappingsCreate

> StorageClassificationMapping replicationStorageClassificationMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName, pairingInput)

Create storage classification mapping.

The operation to create a storage classification mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationStorageClassificationMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
let storageClassificationMappingName = "storageClassificationMappingName_example"; // String | Storage classification mapping name.
let pairingInput = new SiteRecoveryManagementClient.StorageClassificationMappingInput(); // StorageClassificationMappingInput | Pairing input.
apiInstance.replicationStorageClassificationMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName, pairingInput, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name. | 
 **storageClassificationName** | **String**| Storage classification name. | 
 **storageClassificationMappingName** | **String**| Storage classification mapping name. | 
 **pairingInput** | [**StorageClassificationMappingInput**](StorageClassificationMappingInput.md)| Pairing input. | 

### Return type

[**StorageClassificationMapping**](StorageClassificationMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationStorageClassificationMappingsDelete

> replicationStorageClassificationMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName)

Delete a storage classification mapping.

The operation to delete a storage classification mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationStorageClassificationMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
let storageClassificationMappingName = "storageClassificationMappingName_example"; // String | Storage classification mapping name.
apiInstance.replicationStorageClassificationMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name. | 
 **storageClassificationName** | **String**| Storage classification name. | 
 **storageClassificationMappingName** | **String**| Storage classification mapping name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationStorageClassificationMappingsGet

> StorageClassificationMapping replicationStorageClassificationMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName)

Gets the details of a storage classification mapping.

Gets the details of the specified storage classification mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationStorageClassificationMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
let storageClassificationMappingName = "storageClassificationMappingName_example"; // String | Storage classification mapping name.
apiInstance.replicationStorageClassificationMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, storageClassificationMappingName, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name. | 
 **storageClassificationName** | **String**| Storage classification name. | 
 **storageClassificationMappingName** | **String**| Storage classification mapping name. | 

### Return type

[**StorageClassificationMapping**](StorageClassificationMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationStorageClassificationMappingsList

> StorageClassificationMappingCollection replicationStorageClassificationMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of storage classification mappings objects under a vault.

Lists the storage classification mappings in the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationStorageClassificationMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationStorageClassificationMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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

[**StorageClassificationMappingCollection**](StorageClassificationMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationStorageClassificationMappingsListByReplicationStorageClassifications

> StorageClassificationMappingCollection replicationStorageClassificationMappingsListByReplicationStorageClassifications(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName)

Gets the list of storage classification mappings objects under a storage.

Lists the storage classification mappings for the fabric.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationStorageClassificationMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let storageClassificationName = "storageClassificationName_example"; // String | Storage classification name.
apiInstance.replicationStorageClassificationMappingsListByReplicationStorageClassifications(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, storageClassificationName, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name. | 
 **storageClassificationName** | **String**| Storage classification name. | 

### Return type

[**StorageClassificationMappingCollection**](StorageClassificationMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

