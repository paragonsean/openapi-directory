# MonitorManagementClient.MetricAlertsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricAlertsCreateOrUpdate**](MetricAlertsApi.md#metricAlertsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} | 
[**metricAlertsDelete**](MetricAlertsApi.md#metricAlertsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} | 
[**metricAlertsGet**](MetricAlertsApi.md#metricAlertsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} | 
[**metricAlertsListByResourceGroup**](MetricAlertsApi.md#metricAlertsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts | 
[**metricAlertsListBySubscription**](MetricAlertsApi.md#metricAlertsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Insights/metricAlerts | 
[**metricAlertsUpdate**](MetricAlertsApi.md#metricAlertsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} | 



## metricAlertsCreateOrUpdate

> MetricAlertResource metricAlertsCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Create or update an metric alert definition.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new MonitorManagementClient.MetricAlertResource(); // MetricAlertResource | The parameters of the rule to create or update.
apiInstance.metricAlertsCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**MetricAlertResource**](MetricAlertResource.md)| The parameters of the rule to create or update. | 

### Return type

[**MetricAlertResource**](MetricAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## metricAlertsDelete

> metricAlertsDelete(subscriptionId, resourceGroupName, ruleName, apiVersion)



Delete an alert rule definition.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metricAlertsDelete(subscriptionId, resourceGroupName, ruleName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## metricAlertsGet

> MetricAlertResource metricAlertsGet(subscriptionId, resourceGroupName, ruleName, apiVersion)



Retrieve an alert rule definition.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metricAlertsGet(subscriptionId, resourceGroupName, ruleName, apiVersion, (error, data, response) => {
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

[**MetricAlertResource**](MetricAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metricAlertsListByResourceGroup

> MetricAlertResourceCollection metricAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Retrieve alert rule definitions in a resource group.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metricAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**MetricAlertResourceCollection**](MetricAlertResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metricAlertsListBySubscription

> MetricAlertResourceCollection metricAlertsListBySubscription(subscriptionId, apiVersion)



Retrieve alert rule definitions in a subscription.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.metricAlertsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**MetricAlertResourceCollection**](MetricAlertResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metricAlertsUpdate

> MetricAlertResource metricAlertsUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Update an metric alert definition.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricAlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new MonitorManagementClient.MetricAlertResourcePatch(); // MetricAlertResourcePatch | The parameters of the rule to update.
apiInstance.metricAlertsUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**MetricAlertResourcePatch**](MetricAlertResourcePatch.md)| The parameters of the rule to update. | 

### Return type

[**MetricAlertResource**](MetricAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

