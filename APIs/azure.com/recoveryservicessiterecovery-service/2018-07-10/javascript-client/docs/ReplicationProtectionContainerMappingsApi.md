# SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationProtectionContainerMappingsCreate**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Create protection container mapping.
[**replicationProtectionContainerMappingsDelete**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName}/remove | Remove protection container mapping.
[**replicationProtectionContainerMappingsGet**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Gets a protection container mapping/
[**replicationProtectionContainerMappingsList**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionContainerMappings | Gets the list of all protection container mappings in a vault.
[**replicationProtectionContainerMappingsListByReplicationProtectionContainers**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsListByReplicationProtectionContainers) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings | Gets the list of protection container mappings for a protection container.
[**replicationProtectionContainerMappingsPurge**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsPurge) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Purge protection container mapping.
[**replicationProtectionContainerMappingsUpdate**](ReplicationProtectionContainerMappingsApi.md#replicationProtectionContainerMappingsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectionContainerMappings/{mappingName} | Update protection container mapping.



## replicationProtectionContainerMappingsCreate

> ProtectionContainerMapping replicationProtectionContainerMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, creationInput)

Create protection container mapping.

The operation to create a protection container mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let mappingName = "mappingName_example"; // String | Protection container mapping name.
let creationInput = new SiteRecoveryManagementClient.CreateProtectionContainerMappingInput(); // CreateProtectionContainerMappingInput | Mapping creation input.
apiInstance.replicationProtectionContainerMappingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, creationInput, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 
 **mappingName** | **String**| Protection container mapping name. | 
 **creationInput** | [**CreateProtectionContainerMappingInput**](CreateProtectionContainerMappingInput.md)| Mapping creation input. | 

### Return type

[**ProtectionContainerMapping**](ProtectionContainerMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectionContainerMappingsDelete

> replicationProtectionContainerMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, removalInput)

Remove protection container mapping.

The operation to delete or remove a protection container mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let mappingName = "mappingName_example"; // String | Protection container mapping name.
let removalInput = new SiteRecoveryManagementClient.RemoveProtectionContainerMappingInput(); // RemoveProtectionContainerMappingInput | Removal input.
apiInstance.replicationProtectionContainerMappingsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, removalInput, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 
 **mappingName** | **String**| Protection container mapping name. | 
 **removalInput** | [**RemoveProtectionContainerMappingInput**](RemoveProtectionContainerMappingInput.md)| Removal input. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## replicationProtectionContainerMappingsGet

> ProtectionContainerMapping replicationProtectionContainerMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName)

Gets a protection container mapping/

Gets the details of a protection container mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let mappingName = "mappingName_example"; // String | Protection Container mapping name.
apiInstance.replicationProtectionContainerMappingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 
 **mappingName** | **String**| Protection Container mapping name. | 

### Return type

[**ProtectionContainerMapping**](ProtectionContainerMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectionContainerMappingsList

> ProtectionContainerMappingCollection replicationProtectionContainerMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of all protection container mappings in a vault.

Lists the protection container mappings in the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationProtectionContainerMappingsList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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

[**ProtectionContainerMappingCollection**](ProtectionContainerMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectionContainerMappingsListByReplicationProtectionContainers

> ProtectionContainerMappingCollection replicationProtectionContainerMappingsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the list of protection container mappings for a protection container.

Lists the protection container mappings for a protection container.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
apiInstance.replicationProtectionContainerMappingsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 

### Return type

[**ProtectionContainerMappingCollection**](ProtectionContainerMappingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectionContainerMappingsPurge

> replicationProtectionContainerMappingsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName)

Purge protection container mapping.

The operation to purge(force delete) a protection container mapping

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let mappingName = "mappingName_example"; // String | Protection container mapping name.
apiInstance.replicationProtectionContainerMappingsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 
 **mappingName** | **String**| Protection container mapping name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationProtectionContainerMappingsUpdate

> ProtectionContainerMapping replicationProtectionContainerMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, updateInput)

Update protection container mapping.

The operation to update protection container mapping.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainerMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let mappingName = "mappingName_example"; // String | Protection container mapping name.
let updateInput = new SiteRecoveryManagementClient.UpdateProtectionContainerMappingInput(); // UpdateProtectionContainerMappingInput | Mapping update input.
apiInstance.replicationProtectionContainerMappingsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, mappingName, updateInput, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 
 **mappingName** | **String**| Protection container mapping name. | 
 **updateInput** | [**UpdateProtectionContainerMappingInput**](UpdateProtectionContainerMappingInput.md)| Mapping update input. | 

### Return type

[**ProtectionContainerMapping**](ProtectionContainerMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

