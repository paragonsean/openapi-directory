# AzureAlertsManagementServiceResourceProvider.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsChangeState**](DefaultApi.md#alertsChangeState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId}/changestate | 
[**alertsGetAll**](DefaultApi.md#alertsGetAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts | 
[**alertsGetById**](DefaultApi.md#alertsGetById) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId} | Get a specific alert.
[**alertsGetHistory**](DefaultApi.md#alertsGetHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId}/history | 
[**alertsGetSummary**](DefaultApi.md#alertsGetSummary) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alertsSummary | 
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.AlertsManagement/operations | 
[**smartGroupsChangeState**](DefaultApi.md#smartGroupsChangeState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState | 
[**smartGroupsGetAll**](DefaultApi.md#smartGroupsGetAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups | Get all smartGroups within the subscription
[**smartGroupsGetById**](DefaultApi.md#smartGroupsGetById) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId} | Get information of smart alerts group.
[**smartGroupsGetHistory**](DefaultApi.md#smartGroupsGetHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history | 



## alertsChangeState

> Alert alertsChangeState(subscriptionId, alertId, apiVersion, newState)



Change the state of the alert.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let alertId = "alertId_example"; // String | Unique ID of an alert object.
let apiVersion = "apiVersion_example"; // String | client API version
let newState = "newState_example"; // String | filter by state
apiInstance.alertsChangeState(subscriptionId, alertId, apiVersion, newState, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **alertId** | **String**| Unique ID of an alert object. | 
 **apiVersion** | **String**| client API version | 
 **newState** | **String**| filter by state | 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetAll

> AlertsList alertsGetAll(subscriptionId, apiVersion, opts)



List all the existing alerts, where the results can be selective by passing multiple filter parameters including time range and sorted on specific fields. 

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | client API version
let opts = {
  'targetResource': "targetResource_example", // String | filter by target resource
  'targetResourceGroup': "targetResourceGroup_example", // String | filter by target resource group name
  'targetResourceType': "targetResourceType_example", // String | filter by target resource type
  'monitorService': "monitorService_example", // String | filter by monitor service which is the source of the alert object.
  'monitorCondition': "monitorCondition_example", // String | filter by monitor condition which is the state of the alert at monitor service
  'severity': "severity_example", // String | filter by severity
  'alertState': "alertState_example", // String | filter by state
  'smartGroupId': "smartGroupId_example", // String | filter by smart Group Id
  'includePayload': true, // Boolean | include payload field content, default value is 'false'.
  'pageCount': 56, // Number | number of items per page, default value is '25'.
  'sortBy': "sortBy_example", // String | sort the query results by input field, default value is 'lastModifiedDateTime'.
  'sortOrder': "sortOrder_example", // String | sort the query results order in either ascending or descending, default value is 'desc' for time fields and 'asc' for others.
  'timeRange': "timeRange_example" // String | filter by time range, default value is 1 day
};
apiInstance.alertsGetAll(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| client API version | 
 **targetResource** | **String**| filter by target resource | [optional] 
 **targetResourceGroup** | **String**| filter by target resource group name | [optional] 
 **targetResourceType** | **String**| filter by target resource type | [optional] 
 **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] 
 **monitorCondition** | **String**| filter by monitor condition which is the state of the alert at monitor service | [optional] 
 **severity** | **String**| filter by severity | [optional] 
 **alertState** | **String**| filter by state | [optional] 
 **smartGroupId** | **String**| filter by smart Group Id | [optional] 
 **includePayload** | **Boolean**| include payload field content, default value is &#39;false&#39;. | [optional] 
 **pageCount** | **Number**| number of items per page, default value is &#39;25&#39;. | [optional] 
 **sortBy** | **String**| sort the query results by input field, default value is &#39;lastModifiedDateTime&#39;. | [optional] 
 **sortOrder** | **String**| sort the query results order in either ascending or descending, default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] 
 **timeRange** | **String**| filter by time range, default value is 1 day | [optional] 

### Return type

[**AlertsList**](AlertsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetById

> Alert alertsGetById(subscriptionId, alertId, apiVersion)

Get a specific alert.

Get information related to a specific alert

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let alertId = "alertId_example"; // String | Unique ID of an alert object.
let apiVersion = "apiVersion_example"; // String | client API version
apiInstance.alertsGetById(subscriptionId, alertId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **alertId** | **String**| Unique ID of an alert object. | 
 **apiVersion** | **String**| client API version | 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetHistory

> AlertModification alertsGetHistory(subscriptionId, alertId, apiVersion)



Get the history of the changes of an alert.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let alertId = "alertId_example"; // String | Unique ID of an alert object.
let apiVersion = "apiVersion_example"; // String | client API version
apiInstance.alertsGetHistory(subscriptionId, alertId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **alertId** | **String**| Unique ID of an alert object. | 
 **apiVersion** | **String**| client API version | 

### Return type

[**AlertModification**](AlertModification.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetSummary

> AlertsSummary alertsGetSummary(subscriptionId, apiVersion, opts)



Summary of alerts with the count each severity.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | client API version
let opts = {
  'targetResourceGroup': "targetResourceGroup_example", // String | filter by target resource group name
  'timeRange': "timeRange_example" // String | filter by time range, default value is 1 day
};
apiInstance.alertsGetSummary(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| client API version | 
 **targetResourceGroup** | **String**| filter by target resource group name | [optional] 
 **timeRange** | **String**| filter by time range, default value is 1 day | [optional] 

### Return type

[**AlertsSummary**](AlertsSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationsList

> OperationsList operationsList(apiVersion)



List all operations available through Azure Alerts Management Resource Provider.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | client API version
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| client API version | 

### Return type

[**OperationsList**](OperationsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsChangeState

> SmartGroup smartGroupsChangeState(subscriptionId, smartGroupId, apiVersion, newState)



Change the state from unresolved to resolved and all the alerts within the smart group will also be resolved.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let smartGroupId = "smartGroupId_example"; // String | Smart Group Id
let apiVersion = "apiVersion_example"; // String | client API version
let newState = "newState_example"; // String | filter by state
apiInstance.smartGroupsChangeState(subscriptionId, smartGroupId, apiVersion, newState, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **smartGroupId** | **String**| Smart Group Id | 
 **apiVersion** | **String**| client API version | 
 **newState** | **String**| filter by state | 

### Return type

[**SmartGroup**](SmartGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsGetAll

> SmartGroupsList smartGroupsGetAll(subscriptionId, apiVersion, opts)

Get all smartGroups within the subscription

List all the smartGroups within the specified subscription. 

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | client API version
let opts = {
  'targetResource': "targetResource_example", // String | filter by target resource
  'targetResourceGroup': "targetResourceGroup_example", // String | filter by target resource group name
  'targetResourceType': "targetResourceType_example", // String | filter by target resource type
  'monitorService': "monitorService_example", // String | filter by monitor service which is the source of the alert object.
  'monitorCondition': "monitorCondition_example", // String | filter by monitor condition which is the state of the alert at monitor service
  'severity': "severity_example", // String | filter by severity
  'smartGroupState': "smartGroupState_example", // String | filter by state
  'timeRange': "timeRange_example", // String | filter by time range, default value is 1 day
  'pageCount': 56, // Number | number of items per page, default value is '25'.
  'sortBy': "sortBy_example", // String | sort the query results by input field, default value is 'lastModifiedDateTime'.
  'sortOrder': "sortOrder_example" // String | sort the query results order in either ascending or descending, default value is 'desc' for time fields and 'asc' for others.
};
apiInstance.smartGroupsGetAll(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| client API version | 
 **targetResource** | **String**| filter by target resource | [optional] 
 **targetResourceGroup** | **String**| filter by target resource group name | [optional] 
 **targetResourceType** | **String**| filter by target resource type | [optional] 
 **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] 
 **monitorCondition** | **String**| filter by monitor condition which is the state of the alert at monitor service | [optional] 
 **severity** | **String**| filter by severity | [optional] 
 **smartGroupState** | **String**| filter by state | [optional] 
 **timeRange** | **String**| filter by time range, default value is 1 day | [optional] 
 **pageCount** | **Number**| number of items per page, default value is &#39;25&#39;. | [optional] 
 **sortBy** | **String**| sort the query results by input field, default value is &#39;lastModifiedDateTime&#39;. | [optional] 
 **sortOrder** | **String**| sort the query results order in either ascending or descending, default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] 

### Return type

[**SmartGroupsList**](SmartGroupsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsGetById

> SmartGroup smartGroupsGetById(subscriptionId, smartGroupId, apiVersion)

Get information of smart alerts group.

Get details of smart group.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let smartGroupId = "smartGroupId_example"; // String | Smart Group Id
let apiVersion = "apiVersion_example"; // String | client API version
apiInstance.smartGroupsGetById(subscriptionId, smartGroupId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **smartGroupId** | **String**| Smart Group Id | 
 **apiVersion** | **String**| client API version | 

### Return type

[**SmartGroup**](SmartGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsGetHistory

> SmartGroupModification smartGroupsGetHistory(subscriptionId, smartGroupId, apiVersion)



Get the history of the changes of smart group.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let smartGroupId = "smartGroupId_example"; // String | Smart Group Id
let apiVersion = "apiVersion_example"; // String | client API version
apiInstance.smartGroupsGetHistory(subscriptionId, smartGroupId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **smartGroupId** | **String**| Smart Group Id | 
 **apiVersion** | **String**| client API version | 

### Return type

[**SmartGroupModification**](SmartGroupModification.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

