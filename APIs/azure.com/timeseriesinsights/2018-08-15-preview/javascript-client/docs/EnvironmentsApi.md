# TimeSeriesInsightsClient.EnvironmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environmentsCreateOrUpdate**](EnvironmentsApi.md#environmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} | 
[**environmentsDelete**](EnvironmentsApi.md#environmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} | 
[**environmentsGet**](EnvironmentsApi.md#environmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} | 
[**environmentsListByResourceGroup**](EnvironmentsApi.md#environmentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments | 
[**environmentsListBySubscription**](EnvironmentsApi.md#environmentsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.TimeSeriesInsights/environments | 
[**environmentsUpdate**](EnvironmentsApi.md#environmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} | 



## environmentsCreateOrUpdate

> EnvironmentResource environmentsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, parameters)



Create or update an environment in the specified subscription and resource group.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | Name of the environment
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new TimeSeriesInsightsClient.EnvironmentCreateOrUpdateParameters(); // EnvironmentCreateOrUpdateParameters | Parameters for creating an environment resource.
apiInstance.environmentsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, parameters, (error, data, response) => {
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
 **environmentName** | **String**| Name of the environment | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**EnvironmentCreateOrUpdateParameters**](EnvironmentCreateOrUpdateParameters.md)| Parameters for creating an environment resource. | 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## environmentsDelete

> environmentsDelete(subscriptionId, resourceGroupName, environmentName, apiVersion)



Deletes the environment with the specified name in the specified subscription and resource group.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.environmentsDelete(subscriptionId, resourceGroupName, environmentName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsGet

> EnvironmentResource environmentsGet(subscriptionId, resourceGroupName, environmentName, apiVersion, opts)



Gets the environment with the specified name in the specified subscription and resource group.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'expand': "expand_example" // String | Setting $expand=status will include the status of the internal services of the environment in the Time Series Insights service.
};
apiInstance.environmentsGet(subscriptionId, resourceGroupName, environmentName, apiVersion, opts, (error, data, response) => {
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
 **expand** | **String**| Setting $expand&#x3D;status will include the status of the internal services of the environment in the Time Series Insights service. | [optional] 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsListByResourceGroup

> EnvironmentListResponse environmentsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the available environments associated with the subscription and within the specified resource group.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.environmentsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EnvironmentListResponse**](EnvironmentListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsListBySubscription

> EnvironmentListResponse environmentsListBySubscription(subscriptionId, apiVersion)



Lists all the available environments within a subscription, irrespective of the resource groups.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.environmentsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EnvironmentListResponse**](EnvironmentListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsUpdate

> EnvironmentResource environmentsUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, standardEnvironmentUpdateParameters)



Updates the environment with the specified name in the specified subscription and resource group.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let standardEnvironmentUpdateParameters = new TimeSeriesInsightsClient.StandardEnvironmentUpdateParameters(); // StandardEnvironmentUpdateParameters | Request object that contains the updated information for the environment.
apiInstance.environmentsUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, standardEnvironmentUpdateParameters, (error, data, response) => {
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
 **standardEnvironmentUpdateParameters** | [**StandardEnvironmentUpdateParameters**](StandardEnvironmentUpdateParameters.md)| Request object that contains the updated information for the environment. | 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

