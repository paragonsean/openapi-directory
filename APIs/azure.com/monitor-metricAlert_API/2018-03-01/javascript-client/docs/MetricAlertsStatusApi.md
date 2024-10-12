# MonitorManagementClient.MetricAlertsStatusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricAlertsStatusList**](MetricAlertsStatusApi.md#metricAlertsStatusList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}/status | 
[**metricAlertsStatusListByName**](MetricAlertsStatusApi.md#metricAlertsStatusListByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}/status/{statusName} | 



## metricAlertsStatusList

> MetricAlertStatusCollection metricAlertsStatusList(subscriptionId, resourceGroupName, ruleName, apiVersion)



Retrieve an alert rule status.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsStatusApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metricAlertsStatusList(subscriptionId, resourceGroupName, ruleName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**MetricAlertStatusCollection**](MetricAlertStatusCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metricAlertsStatusListByName

> MetricAlertStatusCollection metricAlertsStatusListByName(subscriptionId, resourceGroupName, ruleName, statusName, apiVersion)



Retrieve an alert rule status.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsStatusApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let statusName = "statusName_example"; // String | The name of the status.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metricAlertsStatusListByName(subscriptionId, resourceGroupName, ruleName, statusName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **ruleName** | **String**| The name of the rule. | 
 **statusName** | **String**| The name of the status. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**MetricAlertStatusCollection**](MetricAlertStatusCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

