# TimeSeriesInsightsClient.EventSourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventSourcesCreateOrUpdate**](EventSourcesApi.md#eventSourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} | 
[**eventSourcesDelete**](EventSourcesApi.md#eventSourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} | 
[**eventSourcesGet**](EventSourcesApi.md#eventSourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} | 
[**eventSourcesListByEnvironment**](EventSourcesApi.md#eventSourcesListByEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources | 
[**eventSourcesUpdate**](EventSourcesApi.md#eventSourcesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} | 



## eventSourcesCreateOrUpdate

> EventSourceResource eventSourcesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, parameters)



Create or update an event source under the specified environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EventSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let eventSourceName = "eventSourceName_example"; // String | Name of the event source.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new TimeSeriesInsightsClient.EventSourceCreateOrUpdateParameters(); // EventSourceCreateOrUpdateParameters | Parameters for creating an event source resource.
apiInstance.eventSourcesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | 
 **eventSourceName** | **String**| Name of the event source. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**EventSourceCreateOrUpdateParameters**](EventSourceCreateOrUpdateParameters.md)| Parameters for creating an event source resource. | 

### Return type

[**EventSourceResource**](EventSourceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## eventSourcesDelete

> eventSourcesDelete(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion)



Deletes the event source with the specified name in the specified subscription, resource group, and environment

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EventSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let eventSourceName = "eventSourceName_example"; // String | The name of the Time Series Insights event source associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.eventSourcesDelete(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | 
 **eventSourceName** | **String**| The name of the Time Series Insights event source associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSourcesGet

> EventSourceResource eventSourcesGet(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion)



Gets the event source with the specified name in the specified environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EventSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let eventSourceName = "eventSourceName_example"; // String | The name of the Time Series Insights event source associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.eventSourcesGet(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | 
 **eventSourceName** | **String**| The name of the Time Series Insights event source associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EventSourceResource**](EventSourceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSourcesListByEnvironment

> EventSourceListResponse eventSourcesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion)



Lists all the available event sources associated with the subscription and within the specified resource group and environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EventSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.eventSourcesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EventSourceListResponse**](EventSourceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSourcesUpdate

> EventSourceResource eventSourcesUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, eventSourceUpdateParameters)



Updates the event source with the specified name in the specified subscription, resource group, and environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EventSourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let eventSourceName = "eventSourceName_example"; // String | The name of the Time Series Insights event source associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let eventSourceUpdateParameters = new TimeSeriesInsightsClient.EventSourceUpdateParameters(); // EventSourceUpdateParameters | Request object that contains the updated information for the event source.
apiInstance.eventSourcesUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, eventSourceUpdateParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | 
 **eventSourceName** | **String**| The name of the Time Series Insights event source associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **eventSourceUpdateParameters** | [**EventSourceUpdateParameters**](EventSourceUpdateParameters.md)| Request object that contains the updated information for the event source. | 

### Return type

[**EventSourceResource**](EventSourceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

