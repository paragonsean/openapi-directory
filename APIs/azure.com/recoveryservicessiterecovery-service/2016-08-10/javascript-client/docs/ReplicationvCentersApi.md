# SiteRecoveryManagementClient.ReplicationvCentersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationvCentersCreate**](ReplicationvCentersApi.md#replicationvCentersCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vCenterName} | Add vCenter.
[**replicationvCentersDelete**](ReplicationvCentersApi.md#replicationvCentersDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vCenterName} | Remove vCenter operation.
[**replicationvCentersGet**](ReplicationvCentersApi.md#replicationvCentersGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vCenterName} | Gets the details of a vCenter.
[**replicationvCentersList**](ReplicationvCentersApi.md#replicationvCentersList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationvCenters | Gets the list of vCenter registered under the vault.
[**replicationvCentersListByReplicationFabrics**](ReplicationvCentersApi.md#replicationvCentersListByReplicationFabrics) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters | Gets the list of vCenter registered under a fabric.
[**replicationvCentersUpdate**](ReplicationvCentersApi.md#replicationvCentersUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationvCenters/{vCenterName} | Update vCenter operation.



## replicationvCentersCreate

> VCenter replicationvCentersCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName, addVCenterRequest)

Add vCenter.

The operation to create a vCenter object..

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationvCentersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let vCenterName = "vCenterName_example"; // String | vCenter name.
let addVCenterRequest = new SiteRecoveryManagementClient.AddVCenterRequest(); // AddVCenterRequest | The input to the add vCenter operation.
apiInstance.replicationvCentersCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName, addVCenterRequest, (error, data, response) => {
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
 **vCenterName** | **String**| vCenter name. | 
 **addVCenterRequest** | [**AddVCenterRequest**](AddVCenterRequest.md)| The input to the add vCenter operation. | 

### Return type

[**VCenter**](VCenter.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationvCentersDelete

> replicationvCentersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName)

Remove vCenter operation.

The operation to remove(unregister) a registered vCenter server from the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationvCentersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let vCenterName = "vCenterName_example"; // String | vCenter name.
apiInstance.replicationvCentersDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName, (error, data, response) => {
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
 **vCenterName** | **String**| vCenter name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationvCentersGet

> VCenter replicationvCentersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName)

Gets the details of a vCenter.

Gets the details of a registered vCenter server(Add vCenter server.)

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationvCentersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let vCenterName = "vCenterName_example"; // String | vCenter name.
apiInstance.replicationvCentersGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName, (error, data, response) => {
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
 **vCenterName** | **String**| vCenter name. | 

### Return type

[**VCenter**](VCenter.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationvCentersList

> VCenterCollection replicationvCentersList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of vCenter registered under the vault.

Lists the vCenter servers registered in the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationvCentersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationvCentersList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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

[**VCenterCollection**](VCenterCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationvCentersListByReplicationFabrics

> VCenterCollection replicationvCentersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName)

Gets the list of vCenter registered under a fabric.

Lists the vCenter servers registered in a fabric.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationvCentersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
apiInstance.replicationvCentersListByReplicationFabrics(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, (error, data, response) => {
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

[**VCenterCollection**](VCenterCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationvCentersUpdate

> VCenter replicationvCentersUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName, updateVCenterRequest)

Update vCenter operation.

The operation to update a registered vCenter.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationvCentersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let vCenterName = "vCenterName_example"; // String | vCenter name
let updateVCenterRequest = new SiteRecoveryManagementClient.UpdateVCenterRequest(); // UpdateVCenterRequest | The input to the update vCenter operation.
apiInstance.replicationvCentersUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, vCenterName, updateVCenterRequest, (error, data, response) => {
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
 **vCenterName** | **String**| vCenter name | 
 **updateVCenterRequest** | [**UpdateVCenterRequest**](UpdateVCenterRequest.md)| The input to the update vCenter operation. | 

### Return type

[**VCenter**](VCenter.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

