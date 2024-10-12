# AzureMetrics.MetricsApi

All URIs are relative to *https://monitoring.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsCreate**](MetricsApi.md#metricsCreate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProvider}/{resourceTypeName}/{resourceName}/metrics | 



## metricsCreate

> AzureMetricsResult metricsCreate(contentType, contentLength, authorization, subscriptionId, resourceGroupName, resourceProvider, resourceTypeName, resourceName, body)



**Post the metric values for a resource**.

### Example

```javascript
import AzureMetrics from 'azure_metrics';

let apiInstance = new AzureMetrics.MetricsApi();
let contentType = "contentType_example"; // String | Supports application/json and application/x-ndjson
let contentLength = 56; // Number | Content length of the payload
let authorization = "authorization_example"; // String | Authorization token issue for issued for audience \"https:\\\\monitoring.azure.com\\\"
let subscriptionId = "subscriptionId_example"; // String | The azure subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The ARM resource group name
let resourceProvider = "resourceProvider_example"; // String | The ARM resource provider name
let resourceTypeName = "resourceTypeName_example"; // String | The ARM resource type name
let resourceName = "resourceName_example"; // String | The ARM resource name
let body = new AzureMetrics.AzureMetricsDocument(); // AzureMetricsDocument | The Azure metrics document json payload
apiInstance.metricsCreate(contentType, contentLength, authorization, subscriptionId, resourceGroupName, resourceProvider, resourceTypeName, resourceName, body, (error, data, response) => {
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
 **contentType** | **String**| Supports application/json and application/x-ndjson | 
 **contentLength** | **Number**| Content length of the payload | 
 **authorization** | **String**| Authorization token issue for issued for audience \&quot;https:\\\\monitoring.azure.com\\\&quot; | 
 **subscriptionId** | **String**| The azure subscription id | 
 **resourceGroupName** | **String**| The ARM resource group name | 
 **resourceProvider** | **String**| The ARM resource provider name | 
 **resourceTypeName** | **String**| The ARM resource type name | 
 **resourceName** | **String**| The ARM resource name | 
 **body** | [**AzureMetricsDocument**](AzureMetricsDocument.md)| The Azure metrics document json payload | 

### Return type

[**AzureMetricsResult**](AzureMetricsResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

