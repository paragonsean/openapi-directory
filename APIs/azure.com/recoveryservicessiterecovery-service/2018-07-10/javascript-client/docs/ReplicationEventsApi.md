# SiteRecoveryManagementClient.ReplicationEventsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationEventsGet**](ReplicationEventsApi.md#replicationEventsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationEvents/{eventName} | Get the details of an Azure Site recovery event.
[**replicationEventsList**](ReplicationEventsApi.md#replicationEventsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationEvents | Gets the list of Azure Site Recovery events.



## replicationEventsGet

> Event replicationEventsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, eventName)

Get the details of an Azure Site recovery event.

The operation to get the details of an Azure Site recovery event.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationEventsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let eventName = "eventName_example"; // String | The name of the Azure Site Recovery event.
apiInstance.replicationEventsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, eventName, (error, data, response) => {
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
 **eventName** | **String**| The name of the Azure Site Recovery event. | 

### Return type

[**Event**](Event.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationEventsList

> EventCollection replicationEventsList(apiVersion, resourceName, resourceGroupName, subscriptionId, opts)

Gets the list of Azure Site Recovery events.

Gets the list of Azure Site Recovery events for the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationEventsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let opts = {
  'filter': "filter_example" // String | OData filter options.
};
apiInstance.replicationEventsList(apiVersion, resourceName, resourceGroupName, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| OData filter options. | [optional] 

### Return type

[**EventCollection**](EventCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

