# MonitorManagementClient.AlertRuleIncidentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertRuleIncidentsGet**](AlertRuleIncidentsApi.md#alertRuleIncidentsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName}/incidents/{incidentName} | 
[**alertRuleIncidentsListByAlertRule**](AlertRuleIncidentsApi.md#alertRuleIncidentsListByAlertRule) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName}/incidents | 



## alertRuleIncidentsGet

> Incident alertRuleIncidentsGet(resourceGroupName, ruleName, incidentName, apiVersion, subscriptionId)



Gets an incident associated to an alert rule

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AlertRuleIncidentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let incidentName = "incidentName_example"; // String | The name of the incident to retrieve.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.alertRuleIncidentsGet(resourceGroupName, ruleName, incidentName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **ruleName** | **String**| The name of the rule. | 
 **incidentName** | **String**| The name of the incident to retrieve. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**Incident**](Incident.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertRuleIncidentsListByAlertRule

> IncidentListResult alertRuleIncidentsListByAlertRule(resourceGroupName, ruleName, apiVersion, subscriptionId)



Gets a list of incidents associated to an alert rule

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AlertRuleIncidentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.alertRuleIncidentsListByAlertRule(resourceGroupName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**IncidentListResult**](IncidentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

