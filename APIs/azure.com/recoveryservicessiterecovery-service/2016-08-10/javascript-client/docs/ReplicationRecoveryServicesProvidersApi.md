# SiteRecoveryManagementClient.ReplicationRecoveryServicesProvidersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationRecoveryServicesProvidersDelete**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName}/remove | Deletes provider from fabric. Note: Deleting provider for any fabric other than SingleHost is unsupported. To maintain backward compatibility for released clients the object \&quot;deleteRspInput\&quot; is used (if the object is empty we assume that it is old client and continue the old behavior).
[**replicationRecoveryServicesProvidersGet**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName} | Gets the details of a recovery services provider.
[**replicationRecoveryServicesProvidersList**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryServicesProviders | Gets the list of registered recovery services providers in the vault. This is a view only api.
[**replicationRecoveryServicesProvidersListByReplicationFabrics**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersListByReplicationFabrics) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders | Gets the list of registered recovery services providers for the fabric.
[**replicationRecoveryServicesProvidersPurge**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersPurge) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName} | Purges recovery service provider from fabric
[**replicationRecoveryServicesProvidersRefreshProvider**](ReplicationRecoveryServicesProvidersApi.md#replicationRecoveryServicesProvidersRefreshProvider) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationRecoveryServicesProviders/{providerName}/refreshProvider | Refresh details from the recovery services provider.



## replicationRecoveryServicesProvidersDelete

> replicationRecoveryServicesProvidersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Deletes provider from fabric. Note: Deleting provider for any fabric other than SingleHost is unsupported. To maintain backward compatibility for released clients the object \&quot;deleteRspInput\&quot; is used (if the object is empty we assume that it is old client and continue the old behavior).

The operation to removes/delete(unregister) a recovery services provider from the vault

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryServicesProvidersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let providerName = "providerName_example"; // String | Recovery services provider name.
apiInstance.replicationRecoveryServicesProvidersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName, (error, data, response) => {
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
 **providerName** | **String**| Recovery services provider name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationRecoveryServicesProvidersGet

> RecoveryServicesProvider replicationRecoveryServicesProvidersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Gets the details of a recovery services provider.

Gets the details of registered recovery services provider.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryServicesProvidersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let providerName = "providerName_example"; // String | Recovery services provider name
apiInstance.replicationRecoveryServicesProvidersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName, (error, data, response) => {
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
 **providerName** | **String**| Recovery services provider name | 

### Return type

[**RecoveryServicesProvider**](RecoveryServicesProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationRecoveryServicesProvidersList

> RecoveryServicesProviderCollection replicationRecoveryServicesProvidersList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of registered recovery services providers in the vault. This is a view only api.

Lists the registered recovery services providers in the vault

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryServicesProvidersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationRecoveryServicesProvidersList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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

[**RecoveryServicesProviderCollection**](RecoveryServicesProviderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationRecoveryServicesProvidersListByReplicationFabrics

> RecoveryServicesProviderCollection replicationRecoveryServicesProvidersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName)

Gets the list of registered recovery services providers for the fabric.

Lists the registered recovery services providers for the specified fabric.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryServicesProvidersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name
apiInstance.replicationRecoveryServicesProvidersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name | 

### Return type

[**RecoveryServicesProviderCollection**](RecoveryServicesProviderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationRecoveryServicesProvidersPurge

> replicationRecoveryServicesProvidersPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Purges recovery service provider from fabric

The operation to purge(force delete) a recovery services provider from the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryServicesProvidersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let providerName = "providerName_example"; // String | Recovery services provider name.
apiInstance.replicationRecoveryServicesProvidersPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName, (error, data, response) => {
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
 **providerName** | **String**| Recovery services provider name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationRecoveryServicesProvidersRefreshProvider

> RecoveryServicesProvider replicationRecoveryServicesProvidersRefreshProvider(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName)

Refresh details from the recovery services provider.

The operation to refresh the information from the recovery services provider.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryServicesProvidersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let providerName = "providerName_example"; // String | Recovery services provider name.
apiInstance.replicationRecoveryServicesProvidersRefreshProvider(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, providerName, (error, data, response) => {
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
 **providerName** | **String**| Recovery services provider name. | 

### Return type

[**RecoveryServicesProvider**](RecoveryServicesProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

