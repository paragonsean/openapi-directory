# AzureMigrateHub.MachinesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**machinesEnumerateMachines**](MachinesApi.md#machinesEnumerateMachines) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/machines | Gets a list of machines in the migrate project.
[**machinesGetMachine**](MachinesApi.md#machinesGetMachine) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/machines/{machineName} | Gets a machine in the migrate project.



## machinesEnumerateMachines

> MachineCollection machinesEnumerateMachines(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts)

Gets a list of machines in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MachinesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token.
  'pageSize': 56 // Number | The number of items to be returned in a single page. This value is honored only if it is less than the 100.
};
apiInstance.machinesEnumerateMachines(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **continuationToken** | **String**| The continuation token. | [optional] 
 **pageSize** | **Number**| The number of items to be returned in a single page. This value is honored only if it is less than the 100. | [optional] 

### Return type

[**MachineCollection**](MachineCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machinesGetMachine

> Machine machinesGetMachine(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, machineName)

Gets a machine in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.MachinesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let machineName = "machineName_example"; // String | Unique name of a machine in Azure migration hub.
apiInstance.machinesGetMachine(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, machineName, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **machineName** | **String**| Unique name of a machine in Azure migration hub. | 

### Return type

[**Machine**](Machine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

