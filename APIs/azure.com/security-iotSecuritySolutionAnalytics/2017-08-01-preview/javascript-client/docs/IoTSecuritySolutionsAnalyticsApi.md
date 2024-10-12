# SecurityCenter.IoTSecuritySolutionsAnalyticsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName}/dismiss | 
[**ioTSecuritySolutionsAnalyticsAggregatedAlertGet**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsAggregatedAlertGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName} | 
[**ioTSecuritySolutionsAnalyticsAggregatedAlertsList**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsAggregatedAlertsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts | 
[**ioTSecuritySolutionsAnalyticsGetAll**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsGetAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels | 
[**ioTSecuritySolutionsAnalyticsGetDefault**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsGetDefault) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default | 
[**ioTSecuritySolutionsAnalyticsRecommendationGet**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsRecommendationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations/{aggregatedRecommendationName} | 
[**ioTSecuritySolutionsAnalyticsRecommendationsList**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsRecommendationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations | 



## ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss

> ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Security Analytics of a security solution

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionsAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The solution manager name
let aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert
apiInstance.ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName, (error, data, response) => {
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
 **solutionName** | **String**| The solution manager name | 
 **aggregatedAlertName** | **String**| Identifier of the aggregated alert | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSecuritySolutionsAnalyticsAggregatedAlertGet

> IoTSecurityAggregatedAlert ioTSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Security Analytics of a security solution

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionsAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The solution manager name
let aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert
apiInstance.ioTSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName, (error, data, response) => {
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
 **solutionName** | **String**| The solution manager name | 
 **aggregatedAlertName** | **String**| Identifier of the aggregated alert | 

### Return type

[**IoTSecurityAggregatedAlert**](IoTSecurityAggregatedAlert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSecuritySolutionsAnalyticsAggregatedAlertsList

> IoTSecurityAggregatedAlertList ioTSecuritySolutionsAnalyticsAggregatedAlertsList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts)



Security Analytics of a security solution

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionsAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The solution manager name
let opts = {
  'top': 56 // Number | The number of results to retrieve.
};
apiInstance.ioTSecuritySolutionsAnalyticsAggregatedAlertsList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts, (error, data, response) => {
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
 **solutionName** | **String**| The solution manager name | 
 **top** | **Number**| The number of results to retrieve. | [optional] 

### Return type

[**IoTSecurityAggregatedAlertList**](IoTSecurityAggregatedAlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSecuritySolutionsAnalyticsGetAll

> IoTSecuritySolutionAnalyticsModelList ioTSecuritySolutionsAnalyticsGetAll(apiVersion, subscriptionId, resourceGroupName, solutionName)



Security Analytics of a security solution

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionsAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The solution manager name
apiInstance.ioTSecuritySolutionsAnalyticsGetAll(apiVersion, subscriptionId, resourceGroupName, solutionName, (error, data, response) => {
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
 **solutionName** | **String**| The solution manager name | 

### Return type

[**IoTSecuritySolutionAnalyticsModelList**](IoTSecuritySolutionAnalyticsModelList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSecuritySolutionsAnalyticsGetDefault

> IoTSecuritySolutionAnalyticsModel ioTSecuritySolutionsAnalyticsGetDefault(apiVersion, subscriptionId, resourceGroupName, solutionName)



Security Analytics of a security solution

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionsAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The solution manager name
apiInstance.ioTSecuritySolutionsAnalyticsGetDefault(apiVersion, subscriptionId, resourceGroupName, solutionName, (error, data, response) => {
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
 **solutionName** | **String**| The solution manager name | 

### Return type

[**IoTSecuritySolutionAnalyticsModel**](IoTSecuritySolutionAnalyticsModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSecuritySolutionsAnalyticsRecommendationGet

> IoTSecurityAggregatedRecommendation ioTSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName)



Security Analytics of a security solution

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionsAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The solution manager name
let aggregatedRecommendationName = "aggregatedRecommendationName_example"; // String | Identifier of the aggregated recommendation
apiInstance.ioTSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName, (error, data, response) => {
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
 **solutionName** | **String**| The solution manager name | 
 **aggregatedRecommendationName** | **String**| Identifier of the aggregated recommendation | 

### Return type

[**IoTSecurityAggregatedRecommendation**](IoTSecurityAggregatedRecommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTSecuritySolutionsAnalyticsRecommendationsList

> IoTSecurityAggregatedRecommendationList ioTSecuritySolutionsAnalyticsRecommendationsList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts)



Security Analytics of a security solution

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionsAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The solution manager name
let opts = {
  'top': 56 // Number | The number of results to retrieve.
};
apiInstance.ioTSecuritySolutionsAnalyticsRecommendationsList(apiVersion, subscriptionId, resourceGroupName, solutionName, opts, (error, data, response) => {
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
 **solutionName** | **String**| The solution manager name | 
 **top** | **Number**| The number of results to retrieve. | [optional] 

### Return type

[**IoTSecurityAggregatedRecommendationList**](IoTSecurityAggregatedRecommendationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

