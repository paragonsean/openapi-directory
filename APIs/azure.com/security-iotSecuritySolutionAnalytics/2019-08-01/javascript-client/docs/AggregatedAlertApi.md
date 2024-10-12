# SecurityCenter.AggregatedAlertApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotSecuritySolutionsAnalyticsAggregatedAlertDismiss**](AggregatedAlertApi.md#iotSecuritySolutionsAnalyticsAggregatedAlertDismiss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName}/dismiss | 
[**iotSecuritySolutionsAnalyticsAggregatedAlertGet**](AggregatedAlertApi.md#iotSecuritySolutionsAnalyticsAggregatedAlertGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName} | 
[**iotSecuritySolutionsAnalyticsAggregatedAlertList**](AggregatedAlertApi.md#iotSecuritySolutionsAnalyticsAggregatedAlertList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts | 



## iotSecuritySolutionsAnalyticsAggregatedAlertDismiss

> iotSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Use this method to dismiss an aggregated IoT Security Solution Alert.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AggregatedAlertApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
let aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert.
apiInstance.iotSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **solutionName** | **String**| The name of the IoT Security solution. | 
 **aggregatedAlertName** | **String**| Identifier of the aggregated alert. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotSecuritySolutionsAnalyticsAggregatedAlertGet

> IoTSecurityAggregatedAlert iotSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Use this method to get a single the aggregated alert of yours IoT Security solution. This aggregation is performed by alert name.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AggregatedAlertApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
let aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert.
apiInstance.iotSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **solutionName** | **String**| The name of the IoT Security solution. | 
 **aggregatedAlertName** | **String**| Identifier of the aggregated alert. | 

### Return type

[**IoTSecurityAggregatedAlert**](IoTSecurityAggregatedAlert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotSecuritySolutionsAnalyticsAggregatedAlertList

> IoTSecurityAggregatedAlertList iotSecuritySolutionsAnalyticsAggregatedAlertList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts)



Use this method to get the aggregated alert list of yours IoT Security solution.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AggregatedAlertApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
let opts = {
  'top': 56 // Number | Number of results to retrieve.
};
apiInstance.iotSecuritySolutionsAnalyticsAggregatedAlertList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **solutionName** | **String**| The name of the IoT Security solution. | 
 **top** | **Number**| Number of results to retrieve. | [optional] 

### Return type

[**IoTSecurityAggregatedAlertList**](IoTSecurityAggregatedAlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

