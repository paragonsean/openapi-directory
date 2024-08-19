# SearchManagementClient.AdminKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminKeysList**](AdminKeysApi.md#adminKeysList) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{serviceName}/listAdminKeys | 



## adminKeysList

> AdminKeyResult adminKeysList(resourceGroupName, serviceName, apiVersion, subscriptionId)



Returns the primary and secondary API keys for the given Azure Search service.

### Example

```javascript
import SearchManagementClient from 'search_management_client';
let defaultClient = SearchManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchManagementClient.AdminKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the current subscription.
let serviceName = "serviceName_example"; // String | The name of the Search service for which to list admin keys.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.adminKeysList(resourceGroupName, serviceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group within the current subscription. | 
 **serviceName** | **String**| The name of the Search service for which to list admin keys. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AdminKeyResult**](AdminKeyResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

