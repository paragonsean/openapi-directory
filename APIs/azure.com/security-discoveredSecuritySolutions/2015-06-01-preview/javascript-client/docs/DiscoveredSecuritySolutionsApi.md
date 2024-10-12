# SecurityCenter.DiscoveredSecuritySolutionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discoveredSecuritySolutionsGet**](DiscoveredSecuritySolutionsApi.md#discoveredSecuritySolutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/discoveredSecuritySolutions/{discoveredSecuritySolutionName} | 
[**discoveredSecuritySolutionsList**](DiscoveredSecuritySolutionsApi.md#discoveredSecuritySolutionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/discoveredSecuritySolutions | 
[**discoveredSecuritySolutionsListByHomeRegion**](DiscoveredSecuritySolutionsApi.md#discoveredSecuritySolutionsListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/discoveredSecuritySolutions | 



## discoveredSecuritySolutionsGet

> DiscoveredSecuritySolution discoveredSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, discoveredSecuritySolutionName, apiVersion)



Gets a specific discovered Security Solution.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.DiscoveredSecuritySolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let discoveredSecuritySolutionName = "discoveredSecuritySolutionName_example"; // String | Name of a discovered security solution.
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.discoveredSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, discoveredSecuritySolutionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **discoveredSecuritySolutionName** | **String**| Name of a discovered security solution. | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**DiscoveredSecuritySolution**](DiscoveredSecuritySolution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## discoveredSecuritySolutionsList

> DiscoveredSecuritySolutionList discoveredSecuritySolutionsList(subscriptionId, apiVersion)



Gets a list of discovered Security Solutions for the subscription.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.DiscoveredSecuritySolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.discoveredSecuritySolutionsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**DiscoveredSecuritySolutionList**](DiscoveredSecuritySolutionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## discoveredSecuritySolutionsListByHomeRegion

> DiscoveredSecuritySolutionList discoveredSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets a list of discovered Security Solutions for the subscription and location.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.DiscoveredSecuritySolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.discoveredSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**DiscoveredSecuritySolutionList**](DiscoveredSecuritySolutionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

