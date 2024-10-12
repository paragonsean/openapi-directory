# SiteRecoveryManagementClient.ReplicationProtectionContainersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationProtectionContainersCreate**](ReplicationProtectionContainersApi.md#replicationProtectionContainersCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName} | Create a protection container.
[**replicationProtectionContainersDelete**](ReplicationProtectionContainersApi.md#replicationProtectionContainersDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/remove | Removes a protection container.
[**replicationProtectionContainersDiscoverProtectableItem**](ReplicationProtectionContainersApi.md#replicationProtectionContainersDiscoverProtectableItem) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/discoverProtectableItem | Adds a protectable item to the replication protection container.
[**replicationProtectionContainersGet**](ReplicationProtectionContainersApi.md#replicationProtectionContainersGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName} | Gets the protection container details.
[**replicationProtectionContainersList**](ReplicationProtectionContainersApi.md#replicationProtectionContainersList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionContainers | Gets the list of all protection containers in a vault.
[**replicationProtectionContainersListByReplicationFabrics**](ReplicationProtectionContainersApi.md#replicationProtectionContainersListByReplicationFabrics) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers | Gets the list of protection container for a fabric.
[**replicationProtectionContainersSwitchProtection**](ReplicationProtectionContainersApi.md#replicationProtectionContainersSwitchProtection) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/switchprotection | Switches protection from one container to another or one replication provider to another.



## replicationProtectionContainersCreate

> ProtectionContainer replicationProtectionContainersCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, creationInput)

Create a protection container.

Operation to create a protection container.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric ARM name.
let protectionContainerName = "protectionContainerName_example"; // String | Unique protection container ARM name.
let creationInput = new SiteRecoveryManagementClient.CreateProtectionContainerInput(); // CreateProtectionContainerInput | Creation input.
apiInstance.replicationProtectionContainersCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, creationInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric ARM name. | 
 **protectionContainerName** | **String**| Unique protection container ARM name. | 
 **creationInput** | [**CreateProtectionContainerInput**](CreateProtectionContainerInput.md)| Creation input. | 

### Return type

[**ProtectionContainer**](ProtectionContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectionContainersDelete

> replicationProtectionContainersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Removes a protection container.

Operation to remove a protection container.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric ARM name.
let protectionContainerName = "protectionContainerName_example"; // String | Unique protection container ARM name.
apiInstance.replicationProtectionContainersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric ARM name. | 
 **protectionContainerName** | **String**| Unique protection container ARM name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationProtectionContainersDiscoverProtectableItem

> ProtectionContainer replicationProtectionContainersDiscoverProtectableItem(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, discoverProtectableItemRequest)

Adds a protectable item to the replication protection container.

The operation to a add a protectable item to a protection container(Add physical server.)

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | The name of the fabric.
let protectionContainerName = "protectionContainerName_example"; // String | The name of the protection container.
let discoverProtectableItemRequest = new SiteRecoveryManagementClient.DiscoverProtectableItemRequest(); // DiscoverProtectableItemRequest | The request object to add a protectable item.
apiInstance.replicationProtectionContainersDiscoverProtectableItem(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, discoverProtectableItemRequest, (error, data, response) => {
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
 **fabricName** | **String**| The name of the fabric. | 
 **protectionContainerName** | **String**| The name of the protection container. | 
 **discoverProtectableItemRequest** | [**DiscoverProtectableItemRequest**](DiscoverProtectableItemRequest.md)| The request object to add a protectable item. | 

### Return type

[**ProtectionContainer**](ProtectionContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectionContainersGet

> ProtectionContainer replicationProtectionContainersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the protection container details.

Gets the details of a protection container.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
apiInstance.replicationProtectionContainersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, (error, data, response) => {
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

[**ProtectionContainer**](ProtectionContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectionContainersList

> ProtectionContainerCollection replicationProtectionContainersList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of all protection containers in a vault.

Lists the protection containers in a vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationProtectionContainersList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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

[**ProtectionContainerCollection**](ProtectionContainerCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectionContainersListByReplicationFabrics

> ProtectionContainerCollection replicationProtectionContainersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName)

Gets the list of protection container for a fabric.

Lists the protection containers in the specified fabric.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
apiInstance.replicationProtectionContainersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, (error, data, response) => {
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

### Return type

[**ProtectionContainerCollection**](ProtectionContainerCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectionContainersSwitchProtection

> ProtectionContainer replicationProtectionContainersSwitchProtection(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, switchInput)

Switches protection from one container to another or one replication provider to another.

Operation to switch protection from one container to another or one replication provider to another.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let switchInput = new SiteRecoveryManagementClient.SwitchProtectionInput(); // SwitchProtectionInput | Switch protection input.
apiInstance.replicationProtectionContainersSwitchProtection(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, switchInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **switchInput** | [**SwitchProtectionInput**](SwitchProtectionInput.md)| Switch protection input. | 

### Return type

[**ProtectionContainer**](ProtectionContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

