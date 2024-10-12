# StorageManagementClient.ContainersApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containersCancelMigration**](ContainersApi.md#containersCancelMigration) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/operationresults/{operationId} | 
[**containersList**](ContainersApi.md#containersList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/containers | 
[**containersListDestinationShares**](ContainersApi.md#containersListDestinationShares) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/destinationshares | 
[**containersMigrate**](ContainersApi.md#containersMigrate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/migrate | 
[**containersMigrationStatus**](ContainersApi.md#containersMigrationStatus) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/operationresults/{operationId} | 



## containersCancelMigration

> MigrationResult containersCancelMigration(subscriptionId, resourceGroupName, farmId, operationId, apiVersion)



Cancel a container migration job.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let operationId = "operationId_example"; // String | Operation Id.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.containersCancelMigration(subscriptionId, resourceGroupName, farmId, operationId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **operationId** | **String**| Operation Id. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**MigrationResult**](MigrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersList

> [Container] containersList(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, intent, opts)



Returns the list of containers which can be migrated in the specified share.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let shareName = "shareName_example"; // String | Share name.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
let intent = "intent_example"; // String | The container migration intent.
let opts = {
  'maxCount': 56, // Number | The maximum number of containers.
  'startIndex': 56 // Number | The starting index the resource provider uses.
};
apiInstance.containersList(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, intent, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **shareName** | **String**| Share name. | 
 **apiVersion** | **String**| REST Api Version. | 
 **intent** | **String**| The container migration intent. | 
 **maxCount** | **Number**| The maximum number of containers. | [optional] 
 **startIndex** | **Number**| The starting index the resource provider uses. | [optional] 

### Return type

[**[Container]**](Container.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersListDestinationShares

> [ContainersListDestinationShares200ResponseInner] containersListDestinationShares(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a list of destination shares that the system considers as best candidates for migration.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let shareName = "shareName_example"; // String | Share name.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.containersListDestinationShares(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **shareName** | **String**| Share name. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**[ContainersListDestinationShares200ResponseInner]**](ContainersListDestinationShares200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersMigrate

> MigrationResult containersMigrate(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, migrationParameters)



Starts a container migration job to migrate containers to the specified destination share.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let shareName = "shareName_example"; // String | Share name.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
let migrationParameters = new StorageManagementClient.MigrationParameters(); // MigrationParameters | The parameters of container migration job.
apiInstance.containersMigrate(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, migrationParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **shareName** | **String**| Share name. | 
 **apiVersion** | **String**| REST Api Version. | 
 **migrationParameters** | [**MigrationParameters**](MigrationParameters.md)| The parameters of container migration job. | 

### Return type

[**MigrationResult**](MigrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## containersMigrationStatus

> MigrationResult containersMigrationStatus(subscriptionId, resourceGroupName, farmId, operationId, apiVersion)



Returns the status of a container migration job.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let operationId = "operationId_example"; // String | Operation Id.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.containersMigrationStatus(subscriptionId, resourceGroupName, farmId, operationId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **operationId** | **String**| Operation Id. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**MigrationResult**](MigrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

