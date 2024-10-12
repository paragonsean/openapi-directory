# AzureAlertsManagementServiceResourceProvider.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionRulesCreateUpdate**](DefaultApi.md#actionRulesCreateUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Create/update an action rule
[**actionRulesDelete**](DefaultApi.md#actionRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Delete action rule
[**actionRulesGetAllResourceGroup**](DefaultApi.md#actionRulesGetAllResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules | Get all action rules created in a resource group
[**actionRulesGetAllSubscription**](DefaultApi.md#actionRulesGetAllSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/actionRules | Get all action rule in a given subscription
[**actionRulesGetByName**](DefaultApi.md#actionRulesGetByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Get action rule by name
[**actionRulesPatch**](DefaultApi.md#actionRulesPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Patch action rule
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



## actionRulesCreateUpdate

> ActionRule actionRulesCreateUpdate(subscriptionId, resourceGroup, actionRuleName, actionRule)

Create/update an action rule

Creates/Updates a specific action rule

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
let actionRuleName = "actionRuleName_example"; // String | The name of action rule that needs to be created/updated
let actionRule = new AzureAlertsManagementServiceResourceProvider.ActionRule(); // ActionRule | action rule to be created/updated
apiInstance.actionRulesCreateUpdate(subscriptionId, resourceGroup, actionRuleName, actionRule, (error, data, response) => {
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
 **resourceGroup** | **String**| Resource group name where the resource is created. | 
 **actionRuleName** | **String**| The name of action rule that needs to be created/updated | 
 **actionRule** | [**ActionRule**](ActionRule.md)| action rule to be created/updated | 

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## actionRulesDelete

> actionRulesDelete(subscriptionId, resourceGroup, actionRuleName)

Delete action rule

Deletes a given action rule

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
let actionRuleName = "actionRuleName_example"; // String | The name that needs to be deleted
apiInstance.actionRulesDelete(subscriptionId, resourceGroup, actionRuleName, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Resource group name where the resource is created. | 
 **actionRuleName** | **String**| The name that needs to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionRulesGetAllResourceGroup

> ActionRulesList actionRulesGetAllResourceGroup(subscriptionId, resourceGroup, opts)

Get all action rules created in a resource group

List all action rules of the subscription, created in given resource group and given input filters

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
let opts = {
  'targetResourceGroup': "targetResourceGroup_example", // String | filter by target resource group name
  'targetResourceType': "targetResourceType_example", // String | filter by target resource type
  'targetResource': "targetResource_example", // String | filter by target resource
  'severity': "severity_example", // String | filter by severity
  'monitorService': "monitorService_example" // String | filter by monitor service which is the source of the alert object.
};
apiInstance.actionRulesGetAllResourceGroup(subscriptionId, resourceGroup, opts, (error, data, response) => {
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
 **resourceGroup** | **String**| Resource group name where the resource is created. | 
 **targetResourceGroup** | **String**| filter by target resource group name | [optional] 
 **targetResourceType** | **String**| filter by target resource type | [optional] 
 **targetResource** | **String**| filter by target resource | [optional] 
 **severity** | **String**| filter by severity | [optional] 
 **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] 

### Return type

[**ActionRulesList**](ActionRulesList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionRulesGetAllSubscription

> ActionRulesList actionRulesGetAllSubscription(subscriptionId, opts)

Get all action rule in a given subscription

List all action rules of the subscription and given input filters

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'targetResourceGroup': "targetResourceGroup_example", // String | filter by target resource group name
  'targetResourceType': "targetResourceType_example", // String | filter by target resource type
  'targetResource': "targetResource_example", // String | filter by target resource
  'severity': "severity_example", // String | filter by severity
  'monitorService': "monitorService_example" // String | filter by monitor service which is the source of the alert object.
};
apiInstance.actionRulesGetAllSubscription(subscriptionId, opts, (error, data, response) => {
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
 **targetResourceGroup** | **String**| filter by target resource group name | [optional] 
 **targetResourceType** | **String**| filter by target resource type | [optional] 
 **targetResource** | **String**| filter by target resource | [optional] 
 **severity** | **String**| filter by severity | [optional] 
 **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] 

### Return type

[**ActionRulesList**](ActionRulesList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionRulesGetByName

> ActionRule actionRulesGetByName(subscriptionId, resourceGroup, actionRuleName)

Get action rule by name

Get a specific action rule

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
let actionRuleName = "actionRuleName_example"; // String | The name of action rule that needs to be fetched
apiInstance.actionRulesGetByName(subscriptionId, resourceGroup, actionRuleName, (error, data, response) => {
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
 **resourceGroup** | **String**| Resource group name where the resource is created. | 
 **actionRuleName** | **String**| The name of action rule that needs to be fetched | 

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionRulesPatch

> actionRulesPatch(subscriptionId, resourceGroup, actionRuleName, actionRulePatch)

Patch action rule

Update enabled flag and/or tags for the given action rule

### Example

```javascript
import AzureAlertsManagementServiceResourceProvider from 'azure_alerts_management_service_resource_provider';

let apiInstance = new AzureAlertsManagementServiceResourceProvider.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
let actionRuleName = "actionRuleName_example"; // String | The name that needs to be updated
let actionRulePatch = new AzureAlertsManagementServiceResourceProvider.PatchObject(); // PatchObject | Parameters supplied to the operation.
apiInstance.actionRulesPatch(subscriptionId, resourceGroup, actionRuleName, actionRulePatch, (error, data, response) => {
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
 **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Resource group name where the resource is created. | 
 **actionRuleName** | **String**| The name that needs to be updated | 
 **actionRulePatch** | [**PatchObject**](PatchObject.md)| Parameters supplied to the operation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


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

