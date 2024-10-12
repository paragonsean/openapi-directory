# AzureLogAnalytics.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryExecute**](DefaultApi.md#queryExecute) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/query | Execute an Analytics query
[**queryGet**](DefaultApi.md#queryGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/query | Execute an Analytics query



## queryExecute

> QueryResults queryExecute(subscriptionId, resourceGroupName, workspaceName, apiVersion, body)

Execute an Analytics query

Executes an Analytics query for data. [Here](https://dev.loganalytics.io/documentation/Using-the-API) is an example for using POST with an Analytics query.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics workspace.
let apiVersion = "'2017-10-01'"; // String | Client API version.
let body = new AzureLogAnalytics.QueryBody(); // QueryBody | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
apiInstance.queryExecute(subscriptionId, resourceGroupName, workspaceName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **workspaceName** | **String**| Name of the Log Analytics workspace. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2017-10-01&#39;]
 **body** | [**QueryBody**](QueryBody.md)| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | 

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryGet

> QueryResults queryGet(subscriptionId, resourceGroupName, workspaceName, query, apiVersion, opts)

Execute an Analytics query

Executes an Analytics query for data

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let workspaceName = "workspaceName_example"; // String | Name of the Log Analytics workspace.
let query = "query_example"; // String | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
let apiVersion = "'2017-10-01'"; // String | Client API version.
let opts = {
  'timespan': "timespan_example" // String | Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression.
};
apiInstance.queryGet(subscriptionId, resourceGroupName, workspaceName, query, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **workspaceName** | **String**| Name of the Log Analytics workspace. | 
 **query** | **String**| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2017-10-01&#39;]
 **timespan** | **String**| Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. | [optional] 

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

