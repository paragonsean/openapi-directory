# SecurityCenter.IoTSecuritySolutionAnalyticsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotSecuritySolutionAnalyticsGet**](IoTSecuritySolutionAnalyticsApi.md#iotSecuritySolutionAnalyticsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default | 
[**iotSecuritySolutionAnalyticsList**](IoTSecuritySolutionAnalyticsApi.md#iotSecuritySolutionAnalyticsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels | 



## iotSecuritySolutionAnalyticsGet

> IoTSecuritySolutionAnalyticsModel iotSecuritySolutionAnalyticsGet(apiVersion, subscriptionId, resourceGroupName, solutionName)



Use this method to get IoT Security Analytics metrics.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
apiInstance.iotSecuritySolutionAnalyticsGet(apiVersion, subscriptionId, resourceGroupName, solutionName, (error, data, response) => {
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

### Return type

[**IoTSecuritySolutionAnalyticsModel**](IoTSecuritySolutionAnalyticsModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotSecuritySolutionAnalyticsList

> IoTSecuritySolutionAnalyticsModelList iotSecuritySolutionAnalyticsList(apiVersion, subscriptionId, resourceGroupName, solutionName)



Use this method to get IoT security Analytics metrics in an array.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.IoTSecuritySolutionAnalyticsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
apiInstance.iotSecuritySolutionAnalyticsList(apiVersion, subscriptionId, resourceGroupName, solutionName, (error, data, response) => {
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

### Return type

[**IoTSecuritySolutionAnalyticsModelList**](IoTSecuritySolutionAnalyticsModelList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

