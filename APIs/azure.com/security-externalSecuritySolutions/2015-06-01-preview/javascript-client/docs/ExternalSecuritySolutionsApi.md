# SecurityCenter.ExternalSecuritySolutionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**externalSecuritySolutionsGet**](ExternalSecuritySolutionsApi.md#externalSecuritySolutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/ExternalSecuritySolutions/{externalSecuritySolutionsName} | 
[**externalSecuritySolutionsList**](ExternalSecuritySolutionsApi.md#externalSecuritySolutionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/externalSecuritySolutions | 
[**externalSecuritySolutionsListByHomeRegion**](ExternalSecuritySolutionsApi.md#externalSecuritySolutionsListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/ExternalSecuritySolutions | 



## externalSecuritySolutionsGet

> ExternalSecuritySolution externalSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, externalSecuritySolutionsName, apiVersion)



Gets a specific external Security Solution.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ExternalSecuritySolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let externalSecuritySolutionsName = "externalSecuritySolutionsName_example"; // String | Name of an external security solution.
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.externalSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, externalSecuritySolutionsName, apiVersion, (error, data, response) => {
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
 **externalSecuritySolutionsName** | **String**| Name of an external security solution. | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**ExternalSecuritySolution**](ExternalSecuritySolution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## externalSecuritySolutionsList

> ExternalSecuritySolutionList externalSecuritySolutionsList(apiVersion, subscriptionId)



Gets a list of external security solutions for the subscription.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ExternalSecuritySolutionsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.externalSecuritySolutionsList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**ExternalSecuritySolutionList**](ExternalSecuritySolutionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## externalSecuritySolutionsListByHomeRegion

> ExternalSecuritySolutionList externalSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets a list of external Security Solutions for the subscription and location.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ExternalSecuritySolutionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.externalSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion, (error, data, response) => {
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

[**ExternalSecuritySolutionList**](ExternalSecuritySolutionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

