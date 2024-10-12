# SecurityCenter.AggregatedRecommendationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotSecuritySolutionsAnalyticsRecommendationGet**](AggregatedRecommendationApi.md#iotSecuritySolutionsAnalyticsRecommendationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations/{aggregatedRecommendationName} | 
[**iotSecuritySolutionsAnalyticsRecommendationList**](AggregatedRecommendationApi.md#iotSecuritySolutionsAnalyticsRecommendationList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations | 



## iotSecuritySolutionsAnalyticsRecommendationGet

> IoTSecurityAggregatedRecommendation iotSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName)



Use this method to get the aggregated security analytics recommendation of yours IoT Security solution. This aggregation is performed by recommendation name.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AggregatedRecommendationApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
let aggregatedRecommendationName = "aggregatedRecommendationName_example"; // String | Name of the recommendation aggregated for this query.
apiInstance.iotSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName, (error, data, response) => {
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
 **aggregatedRecommendationName** | **String**| Name of the recommendation aggregated for this query. | 

### Return type

[**IoTSecurityAggregatedRecommendation**](IoTSecurityAggregatedRecommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotSecuritySolutionsAnalyticsRecommendationList

> IoTSecurityAggregatedRecommendationList iotSecuritySolutionsAnalyticsRecommendationList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts)



Use this method to get the list of aggregated security analytics recommendations of yours IoT Security solution.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AggregatedRecommendationApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
let opts = {
  'top': 56 // Number | Number of results to retrieve.
};
apiInstance.iotSecuritySolutionsAnalyticsRecommendationList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts, (error, data, response) => {
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

[**IoTSecurityAggregatedRecommendationList**](IoTSecurityAggregatedRecommendationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

