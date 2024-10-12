# AzureAlertsManagementServiceResourceProvider.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsChangeState**](DefaultApi.md#alertsChangeState) | **POST** /{scope}/providers/Microsoft.AlertsManagement/alerts/{alertId}/changestate | 
[**alertsGetAll**](DefaultApi.md#alertsGetAll) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alerts | 
[**alertsGetById**](DefaultApi.md#alertsGetById) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alerts/{alertId} | Get a specific alert.
[**alertsGetHistory**](DefaultApi.md#alertsGetHistory) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alerts/{alertId}/history | 
[**alertsGetSummary**](DefaultApi.md#alertsGetSummary) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alertsSummary | 
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.AlertsManagement/operations | 
[**smartGroupsChangeState**](DefaultApi.md#smartGroupsChangeState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState | 
[**smartGroupsGetAll**](DefaultApi.md#smartGroupsGetAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups | Get all Smart Groups within a specified subscription
[**smartGroupsGetById**](DefaultApi.md#smartGroupsGetById) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId} | Get information related to a specific Smart Group.
[**smartGroupsGetHistory**](DefaultApi.md#smartGroupsGetHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history | 



## alertsChangeState

> Alert alertsChangeState(scope, alertId, apiVersion, newState)



Change the state of an alert.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let scope = "scope_example"; // String | scope here is resourceId for which alert is created.
let alertId = "alertId_example"; // String | Unique ID of an alert instance.
let apiVersion = "apiVersion_example"; // String | API version.
let newState = "newState_example"; // String | New state of the alert.
apiInstance.alertsChangeState(scope, alertId, apiVersion, newState, (error, data, response) => {
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
 **scope** | **String**| scope here is resourceId for which alert is created. | 
 **alertId** | **String**| Unique ID of an alert instance. | 
 **apiVersion** | **String**| API version. | 
 **newState** | **String**| New state of the alert. | 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetAll

> AlertsList alertsGetAll(scope, apiVersion, opts)



List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime. 

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let scope = "scope_example"; // String | scope here is resourceId for which alert is created.
let apiVersion = "apiVersion_example"; // String | API version.
let opts = {
  'targetResource': "targetResource_example", // String | Filter by target resource( which is full ARM ID) Default value is select all.
  'targetResourceType': "targetResourceType_example", // String | Filter by target resource type. Default value is select all.
  'targetResourceGroup': "targetResourceGroup_example", // String | Filter by target resource group name. Default value is select all.
  'monitorService': "monitorService_example", // String | Filter by monitor service which generates the alert instance. Default value is select all.
  'monitorCondition': "monitorCondition_example", // String | Filter by monitor condition which is either 'Fired' or 'Resolved'. Default value is to select all.
  'severity': "severity_example", // String | Filter by severity.  Default value is select all.
  'alertState': "alertState_example", // String | Filter by state of the alert instance. Default value is to select all.
  'alertRule': "alertRule_example", // String | Filter by specific alert rule.  Default value is to select all.
  'smartGroupId': "smartGroupId_example", // String | Filter the alerts list by the Smart Group Id. Default value is none.
  'includeContext': true, // Boolean | Include context which has contextual data specific to the monitor service. Default value is false'
  'includeEgressConfig': true, // Boolean | Include egress config which would be used for displaying the content in portal.  Default value is 'false'.
  'pageCount': 56, // Number | Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \"includeContent\"  filter is selected, maximum value allowed is 25. Default value is 25.
  'sortBy': "sortBy_example", // String | Sort the query results by input field,  Default value is 'lastModifiedDateTime'.
  'sortOrder': "sortOrder_example", // String | Sort the query results order in either ascending or descending.  Default value is 'desc' for time fields and 'asc' for others.
  'select': "select_example", // String | This filter allows to selection of the fields(comma separated) which would  be part of the essential section. This would allow to project only the  required fields rather than getting entire content.  Default is to fetch all the fields in the essentials section.
  'timeRange': "timeRange_example", // String | Filter by time range by below listed values. Default value is 1 day.
  'customTimeRange': "customTimeRange_example" // String | Filter by custom time range in the format <start-time>/<end-time>  where time is in (ISO-8601 format)'. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none.
};
apiInstance.alertsGetAll(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| scope here is resourceId for which alert is created. | 
 **apiVersion** | **String**| API version. | 
 **targetResource** | **String**| Filter by target resource( which is full ARM ID) Default value is select all. | [optional] 
 **targetResourceType** | **String**| Filter by target resource type. Default value is select all. | [optional] 
 **targetResourceGroup** | **String**| Filter by target resource group name. Default value is select all. | [optional] 
 **monitorService** | **String**| Filter by monitor service which generates the alert instance. Default value is select all. | [optional] 
 **monitorCondition** | **String**| Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all. | [optional] 
 **severity** | **String**| Filter by severity.  Default value is select all. | [optional] 
 **alertState** | **String**| Filter by state of the alert instance. Default value is to select all. | [optional] 
 **alertRule** | **String**| Filter by specific alert rule.  Default value is to select all. | [optional] 
 **smartGroupId** | **String**| Filter the alerts list by the Smart Group Id. Default value is none. | [optional] 
 **includeContext** | **Boolean**| Include context which has contextual data specific to the monitor service. Default value is false&#39; | [optional] 
 **includeEgressConfig** | **Boolean**| Include egress config which would be used for displaying the content in portal.  Default value is &#39;false&#39;. | [optional] 
 **pageCount** | **Number**| Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \&quot;includeContent\&quot;  filter is selected, maximum value allowed is 25. Default value is 25. | [optional] 
 **sortBy** | **String**| Sort the query results by input field,  Default value is &#39;lastModifiedDateTime&#39;. | [optional] 
 **sortOrder** | **String**| Sort the query results order in either ascending or descending.  Default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] 
 **select** | **String**| This filter allows to selection of the fields(comma separated) which would  be part of the essential section. This would allow to project only the  required fields rather than getting entire content.  Default is to fetch all the fields in the essentials section. | [optional] 
 **timeRange** | **String**| Filter by time range by below listed values. Default value is 1 day. | [optional] 
 **customTimeRange** | **String**| Filter by custom time range in the format &lt;start-time&gt;/&lt;end-time&gt;  where time is in (ISO-8601 format)&#39;. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none. | [optional] 

### Return type

[**AlertsList**](AlertsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetById

> Alert alertsGetById(scope, alertId, apiVersion)

Get a specific alert.

Get information related to a specific alert

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let scope = "scope_example"; // String | scope here is resourceId for which alert is created.
let alertId = "alertId_example"; // String | Unique ID of an alert instance.
let apiVersion = "apiVersion_example"; // String | API version.
apiInstance.alertsGetById(scope, alertId, apiVersion, (error, data, response) => {
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
 **scope** | **String**| scope here is resourceId for which alert is created. | 
 **alertId** | **String**| Unique ID of an alert instance. | 
 **apiVersion** | **String**| API version. | 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetHistory

> AlertModification alertsGetHistory(scope, alertId, apiVersion)



Get the history of an alert, which captures any monitor condition changes (Fired/Resolved) and alert state changes (New/Acknowledged/Closed).

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let scope = "scope_example"; // String | scope here is resourceId for which alert is created.
let alertId = "alertId_example"; // String | Unique ID of an alert instance.
let apiVersion = "apiVersion_example"; // String | API version.
apiInstance.alertsGetHistory(scope, alertId, apiVersion, (error, data, response) => {
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
 **scope** | **String**| scope here is resourceId for which alert is created. | 
 **alertId** | **String**| Unique ID of an alert instance. | 
 **apiVersion** | **String**| API version. | 

### Return type

[**AlertModification**](AlertModification.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetSummary

> AlertsSummary alertsGetSummary(scope, groupby, apiVersion, opts)



Get a summarized count of your alerts grouped by various parameters (e.g. grouping by &#39;Severity&#39; returns the count of alerts for each severity).

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let scope = "scope_example"; // String | scope here is resourceId for which alert is created.
let groupby = "groupby_example"; // String | This parameter allows the result set to be grouped by input fields. For example, groupby=severity,alertstate.
let apiVersion = "apiVersion_example"; // String | API version.
let opts = {
  'includeSmartGroupsCount': true, // Boolean | Include count of the SmartGroups as part of the summary. Default value is 'false'.
  'targetResource': "targetResource_example", // String | Filter by target resource( which is full ARM ID) Default value is select all.
  'targetResourceType': "targetResourceType_example", // String | Filter by target resource type. Default value is select all.
  'targetResourceGroup': "targetResourceGroup_example", // String | Filter by target resource group name. Default value is select all.
  'monitorService': "monitorService_example", // String | Filter by monitor service which generates the alert instance. Default value is select all.
  'monitorCondition': "monitorCondition_example", // String | Filter by monitor condition which is either 'Fired' or 'Resolved'. Default value is to select all.
  'severity': "severity_example", // String | Filter by severity.  Default value is select all.
  'alertState': "alertState_example", // String | Filter by state of the alert instance. Default value is to select all.
  'alertRule': "alertRule_example", // String | Filter by specific alert rule.  Default value is to select all.
  'timeRange': "timeRange_example", // String | Filter by time range by below listed values. Default value is 1 day.
  'customTimeRange': "customTimeRange_example" // String | Filter by custom time range in the format <start-time>/<end-time>  where time is in (ISO-8601 format)'. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none.
};
apiInstance.alertsGetSummary(scope, groupby, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| scope here is resourceId for which alert is created. | 
 **groupby** | **String**| This parameter allows the result set to be grouped by input fields. For example, groupby&#x3D;severity,alertstate. | 
 **apiVersion** | **String**| API version. | 
 **includeSmartGroupsCount** | **Boolean**| Include count of the SmartGroups as part of the summary. Default value is &#39;false&#39;. | [optional] 
 **targetResource** | **String**| Filter by target resource( which is full ARM ID) Default value is select all. | [optional] 
 **targetResourceType** | **String**| Filter by target resource type. Default value is select all. | [optional] 
 **targetResourceGroup** | **String**| Filter by target resource group name. Default value is select all. | [optional] 
 **monitorService** | **String**| Filter by monitor service which generates the alert instance. Default value is select all. | [optional] 
 **monitorCondition** | **String**| Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all. | [optional] 
 **severity** | **String**| Filter by severity.  Default value is select all. | [optional] 
 **alertState** | **String**| Filter by state of the alert instance. Default value is to select all. | [optional] 
 **alertRule** | **String**| Filter by specific alert rule.  Default value is to select all. | [optional] 
 **timeRange** | **String**| Filter by time range by below listed values. Default value is 1 day. | [optional] 
 **customTimeRange** | **String**| Filter by custom time range in the format &lt;start-time&gt;/&lt;end-time&gt;  where time is in (ISO-8601 format)&#39;. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none. | [optional] 

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
let apiVersion = "apiVersion_example"; // String | API version.
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
 **apiVersion** | **String**| API version. | 

### Return type

[**OperationsList**](OperationsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsChangeState

> SmartGroup smartGroupsChangeState(subscriptionId, smartGroupId, apiVersion, newState)



Change the state of a Smart Group.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let smartGroupId = "smartGroupId_example"; // String | Smart group unique id. 
let apiVersion = "apiVersion_example"; // String | API version.
let newState = "newState_example"; // String | New state of the alert.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **smartGroupId** | **String**| Smart group unique id.  | 
 **apiVersion** | **String**| API version. | 
 **newState** | **String**| New state of the alert. | 

### Return type

[**SmartGroup**](SmartGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsGetAll

> SmartGroupsList smartGroupsGetAll(subscriptionId, apiVersion, opts)

Get all Smart Groups within a specified subscription

List all the Smart Groups within a specified subscription. 

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | API version.
let opts = {
  'targetResource': "targetResource_example", // String | Filter by target resource( which is full ARM ID) Default value is select all.
  'targetResourceGroup': "targetResourceGroup_example", // String | Filter by target resource group name. Default value is select all.
  'targetResourceType': "targetResourceType_example", // String | Filter by target resource type. Default value is select all.
  'monitorService': "monitorService_example", // String | Filter by monitor service which generates the alert instance. Default value is select all.
  'monitorCondition': "monitorCondition_example", // String | Filter by monitor condition which is either 'Fired' or 'Resolved'. Default value is to select all.
  'severity': "severity_example", // String | Filter by severity.  Default value is select all.
  'smartGroupState': "smartGroupState_example", // String | Filter by state of the smart group. Default value is to select all.
  'timeRange': "timeRange_example", // String | Filter by time range by below listed values. Default value is 1 day.
  'pageCount': 56, // Number | Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \"includeContent\"  filter is selected, maximum value allowed is 25. Default value is 25.
  'sortBy': "sortBy_example", // String | Sort the query results by input field. Default value is sort by 'lastModifiedDateTime'.
  'sortOrder': "sortOrder_example" // String | Sort the query results order in either ascending or descending.  Default value is 'desc' for time fields and 'asc' for others.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| API version. | 
 **targetResource** | **String**| Filter by target resource( which is full ARM ID) Default value is select all. | [optional] 
 **targetResourceGroup** | **String**| Filter by target resource group name. Default value is select all. | [optional] 
 **targetResourceType** | **String**| Filter by target resource type. Default value is select all. | [optional] 
 **monitorService** | **String**| Filter by monitor service which generates the alert instance. Default value is select all. | [optional] 
 **monitorCondition** | **String**| Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all. | [optional] 
 **severity** | **String**| Filter by severity.  Default value is select all. | [optional] 
 **smartGroupState** | **String**| Filter by state of the smart group. Default value is to select all. | [optional] 
 **timeRange** | **String**| Filter by time range by below listed values. Default value is 1 day. | [optional] 
 **pageCount** | **Number**| Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \&quot;includeContent\&quot;  filter is selected, maximum value allowed is 25. Default value is 25. | [optional] 
 **sortBy** | **String**| Sort the query results by input field. Default value is sort by &#39;lastModifiedDateTime&#39;. | [optional] 
 **sortOrder** | **String**| Sort the query results order in either ascending or descending.  Default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] 

### Return type

[**SmartGroupsList**](SmartGroupsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsGetById

> SmartGroup smartGroupsGetById(subscriptionId, smartGroupId, apiVersion)

Get information related to a specific Smart Group.

Get information related to a specific Smart Group.

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let smartGroupId = "smartGroupId_example"; // String | Smart group unique id. 
let apiVersion = "apiVersion_example"; // String | API version.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **smartGroupId** | **String**| Smart group unique id.  | 
 **apiVersion** | **String**| API version. | 

### Return type

[**SmartGroup**](SmartGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## smartGroupsGetHistory

> SmartGroupModification smartGroupsGetHistory(subscriptionId, smartGroupId, apiVersion)



Get the history a smart group, which captures any Smart Group state changes (New/Acknowledged/Closed) .

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let smartGroupId = "smartGroupId_example"; // String | Smart group unique id. 
let apiVersion = "apiVersion_example"; // String | API version.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **smartGroupId** | **String**| Smart group unique id.  | 
 **apiVersion** | **String**| API version. | 

### Return type

[**SmartGroupModification**](SmartGroupModification.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

