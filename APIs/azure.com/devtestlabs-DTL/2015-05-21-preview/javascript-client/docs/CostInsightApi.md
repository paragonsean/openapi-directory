# DevTestLabsClient.CostInsightApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**costInsightGetResource**](CostInsightApi.md#costInsightGetResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/costinsights/{name} | 
[**costInsightList**](CostInsightApi.md#costInsightList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/costinsights | 
[**costInsightRefreshData**](CostInsightApi.md#costInsightRefreshData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/costinsights/{name}/refreshData | 



## costInsightGetResource

> CostInsight costInsightGetResource(subscriptionId, resourceGroupName, labName, name, apiVersion)



Get cost insight.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.CostInsightApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the cost insight.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
apiInstance.costInsightGetResource(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the cost insight. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]

### Return type

[**CostInsight**](CostInsight.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## costInsightList

> ResponseWithContinuationCostInsight costInsightList(subscriptionId, resourceGroupName, labName, apiVersion, opts)



List cost insights.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.CostInsightApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'orderBy': "orderBy_example" // String | 
};
apiInstance.costInsightList(subscriptionId, resourceGroupName, labName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **orderBy** | **String**|  | [optional] 

### Return type

[**ResponseWithContinuationCostInsight**](ResponseWithContinuationCostInsight.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## costInsightRefreshData

> costInsightRefreshData(subscriptionId, resourceGroupName, labName, name, apiVersion)



Refresh Lab&#39;s Cost Insight Data. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.CostInsightApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the cost insight.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
apiInstance.costInsightRefreshData(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the cost insight. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

