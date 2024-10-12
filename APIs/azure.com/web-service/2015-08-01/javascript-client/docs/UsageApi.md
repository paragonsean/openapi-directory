# WebSiteManagementClient.UsageApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usageGetUsage**](UsageApi.md#usageGetUsage) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web.Admin/environments/{environmentName}/usage | Returns usage records for specified subscription and resource groups



## usageGetUsage

> Object usageGetUsage(resourceGroupName, environmentName, lastId, batchSize, subscriptionId, apiVersion)

Returns usage records for specified subscription and resource groups

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.UsageApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let environmentName = "environmentName_example"; // String | Environment name
let lastId = "lastId_example"; // String | Last marker that was returned from the batch
let batchSize = 56; // Number | size of the batch to be returned.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.usageGetUsage(resourceGroupName, environmentName, lastId, batchSize, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **environmentName** | **String**| Environment name | 
 **lastId** | **String**| Last marker that was returned from the batch | 
 **batchSize** | **Number**| size of the batch to be returned. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

