# TimeSeriesInsightsClient.ReferenceDataSetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**referenceDataSetsCreateOrUpdate**](ReferenceDataSetsApi.md#referenceDataSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} | 
[**referenceDataSetsDelete**](ReferenceDataSetsApi.md#referenceDataSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} | 
[**referenceDataSetsGet**](ReferenceDataSetsApi.md#referenceDataSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} | 
[**referenceDataSetsListByEnvironment**](ReferenceDataSetsApi.md#referenceDataSetsListByEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets | 
[**referenceDataSetsUpdate**](ReferenceDataSetsApi.md#referenceDataSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} | 



## referenceDataSetsCreateOrUpdate

> ReferenceDataSetResource referenceDataSetsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, parameters)



Create or update a reference data set in the specified environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.ReferenceDataSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let referenceDataSetName = "referenceDataSetName_example"; // String | Name of the reference data set.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
let parameters = new TimeSeriesInsightsClient.ReferenceDataSetCreateOrUpdateParameters(); // ReferenceDataSetCreateOrUpdateParameters | Parameters for creating a reference data set.
apiInstance.referenceDataSetsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, parameters, (error, data, response) => {
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
 **referenceDataSetName** | **String**| Name of the reference data set. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 
 **parameters** | [**ReferenceDataSetCreateOrUpdateParameters**](ReferenceDataSetCreateOrUpdateParameters.md)| Parameters for creating a reference data set. | 

### Return type

[**ReferenceDataSetResource**](ReferenceDataSetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## referenceDataSetsDelete

> referenceDataSetsDelete(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion)



Deletes the reference data set with the specified name in the specified subscription, resource group, and environment

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.ReferenceDataSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let referenceDataSetName = "referenceDataSetName_example"; // String | The name of the Time Series Insights reference data set associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
apiInstance.referenceDataSetsDelete(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, (error, data, response) => {
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
 **referenceDataSetName** | **String**| The name of the Time Series Insights reference data set associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referenceDataSetsGet

> ReferenceDataSetResource referenceDataSetsGet(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion)



Gets the reference data set with the specified name in the specified environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.ReferenceDataSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let referenceDataSetName = "referenceDataSetName_example"; // String | The name of the Time Series Insights reference data set associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
apiInstance.referenceDataSetsGet(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, (error, data, response) => {
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
 **referenceDataSetName** | **String**| The name of the Time Series Insights reference data set associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 

### Return type

[**ReferenceDataSetResource**](ReferenceDataSetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referenceDataSetsListByEnvironment

> ReferenceDataSetListResponse referenceDataSetsListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion)



Lists all the available reference data sets associated with the subscription and within the specified resource group and environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.ReferenceDataSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
apiInstance.referenceDataSetsListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 

### Return type

[**ReferenceDataSetListResponse**](ReferenceDataSetListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referenceDataSetsUpdate

> ReferenceDataSetResource referenceDataSetsUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, referenceDataSetUpdateParameters)



Updates the reference data set with the specified name in the specified subscription, resource group, and environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.ReferenceDataSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let referenceDataSetName = "referenceDataSetName_example"; // String | The name of the Time Series Insights reference data set associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
let referenceDataSetUpdateParameters = new TimeSeriesInsightsClient.ReferenceDataSetUpdateParameters(); // ReferenceDataSetUpdateParameters | Request object that contains the updated information for the reference data set.
apiInstance.referenceDataSetsUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, referenceDataSetUpdateParameters, (error, data, response) => {
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
 **referenceDataSetName** | **String**| The name of the Time Series Insights reference data set associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 
 **referenceDataSetUpdateParameters** | [**ReferenceDataSetUpdateParameters**](ReferenceDataSetUpdateParameters.md)| Request object that contains the updated information for the reference data set. | 

### Return type

[**ReferenceDataSetResource**](ReferenceDataSetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

