# AzureMigrateHub.EventsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsDeleteEvent**](EventsApi.md#eventsDeleteEvent) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/migrateEvents/{eventName} | Delete the migrate event
[**eventsEnumerateEvents**](EventsApi.md#eventsEnumerateEvents) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/migrateEvents | Gets a list of events in the migrate project.
[**eventsGetEvent**](EventsApi.md#eventsGetEvent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/migrateEvents/{eventName} | Gets an event in the migrate project.



## eventsDeleteEvent

> eventsDeleteEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName)

Delete the migrate event

Delete the migrate event. Deleting non-existent migrate event is a no-operation.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.EventsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let eventName = "eventName_example"; // String | Unique name of an event within a migrate project.
apiInstance.eventsDeleteEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | 
 **migrateProjectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **eventName** | **String**| Unique name of an event within a migrate project. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventsEnumerateEvents

> EventCollection eventsEnumerateEvents(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts)

Gets a list of events in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.EventsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token.
  'pageSize': 56, // Number | The number of items to be returned in a single page. This value is honored only if it is less than the 100.
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.eventsEnumerateEvents(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**EventCollection**](EventCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsGetEvent

> MigrateEvent eventsGetEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName)

Gets an event in the migrate project.

### Example

```javascript
import AzureMigrateHub from 'azure_migrate_hub';
let defaultClient = AzureMigrateHub.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateHub.EventsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
let migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let eventName = "eventName_example"; // String | Unique name of an event within a migrate project.
apiInstance.eventsGetEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName, (error, data, response) => {
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
 **eventName** | **String**| Unique name of an event within a migrate project. | 

### Return type

[**MigrateEvent**](MigrateEvent.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

