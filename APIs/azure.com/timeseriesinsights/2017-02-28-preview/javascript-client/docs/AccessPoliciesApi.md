# TimeSeriesInsightsClient.AccessPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accessPoliciesCreateOrUpdate**](AccessPoliciesApi.md#accessPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} | 
[**accessPoliciesDelete**](AccessPoliciesApi.md#accessPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} | 
[**accessPoliciesGet**](AccessPoliciesApi.md#accessPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} | 
[**accessPoliciesListByEnvironment**](AccessPoliciesApi.md#accessPoliciesListByEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies | 
[**accessPoliciesUpdate**](AccessPoliciesApi.md#accessPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} | 



## accessPoliciesCreateOrUpdate

> AccessPolicyResource accessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, parameters)



Create or update an access policy in the specified environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.AccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let accessPolicyName = "accessPolicyName_example"; // String | Name of the access policy.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
let parameters = new TimeSeriesInsightsClient.AccessPolicyCreateOrUpdateParameters(); // AccessPolicyCreateOrUpdateParameters | Parameters for creating an access policy.
apiInstance.accessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, parameters, (error, data, response) => {
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
 **accessPolicyName** | **String**| Name of the access policy. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 
 **parameters** | [**AccessPolicyCreateOrUpdateParameters**](AccessPolicyCreateOrUpdateParameters.md)| Parameters for creating an access policy. | 

### Return type

[**AccessPolicyResource**](AccessPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accessPoliciesDelete

> accessPoliciesDelete(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion)



Deletes the access policy with the specified name in the specified subscription, resource group, and environment

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.AccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let accessPolicyName = "accessPolicyName_example"; // String | The name of the Time Series Insights access policy associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
apiInstance.accessPoliciesDelete(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, (error, data, response) => {
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
 **accessPolicyName** | **String**| The name of the Time Series Insights access policy associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessPoliciesGet

> AccessPolicyResource accessPoliciesGet(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion)



Gets the access policy with the specified name in the specified environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.AccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let accessPolicyName = "accessPolicyName_example"; // String | The name of the Time Series Insights access policy associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
apiInstance.accessPoliciesGet(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, (error, data, response) => {
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
 **accessPolicyName** | **String**| The name of the Time Series Insights access policy associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 

### Return type

[**AccessPolicyResource**](AccessPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessPoliciesListByEnvironment

> AccessPolicyListResponse accessPoliciesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion)



Lists all the available access policies associated with the environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.AccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
apiInstance.accessPoliciesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion, (error, data, response) => {
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

[**AccessPolicyListResponse**](AccessPolicyListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessPoliciesUpdate

> AccessPolicyResource accessPoliciesUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, accessPolicyUpdateParameters)



Updates the access policy with the specified name in the specified subscription, resource group, and environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.AccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
let accessPolicyName = "accessPolicyName_example"; // String | The name of the Time Series Insights access policy associated with the specified environment.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
let accessPolicyUpdateParameters = new TimeSeriesInsightsClient.AccessPolicyUpdateParameters(); // AccessPolicyUpdateParameters | Request object that contains the updated information for the access policy.
apiInstance.accessPoliciesUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, accessPolicyUpdateParameters, (error, data, response) => {
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
 **accessPolicyName** | **String**| The name of the Time Series Insights access policy associated with the specified environment. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | 
 **accessPolicyUpdateParameters** | [**AccessPolicyUpdateParameters**](AccessPolicyUpdateParameters.md)| Request object that contains the updated information for the access policy. | 

### Return type

[**AccessPolicyResource**](AccessPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

