# ApiManagementClient.QuotaByCounterKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotaByCounterKeysListByService**](QuotaByCounterKeysApi.md#quotaByCounterKeysListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey} | 
[**quotaByCounterKeysUpdate**](QuotaByCounterKeysApi.md#quotaByCounterKeysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey} | 



## quotaByCounterKeysListByService

> QuotaCounterCollection quotaByCounterKeysListByService(subscriptionId, resourceGroupName, serviceName, quotaCounterKey, apiVersion)



Lists a collection of current quota counter periods associated with the counter-key configured in the policy on the specified service instance. The api does not support paging yet.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.QuotaByCounterKeysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.quotaByCounterKeysListByService(subscriptionId, resourceGroupName, serviceName, quotaCounterKey, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **quotaCounterKey** | **String**| Quota counter key identifier. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**QuotaCounterCollection**](QuotaCounterCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotaByCounterKeysUpdate

> quotaByCounterKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, apiVersion, subscriptionId, parameters)



Updates all the quota counter values specified with the existing quota counter key to a value in the specified service instance. This should be used for reset of the quota counter values.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.QuotaByCounterKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.QuotaCounterValueContract(); // QuotaCounterValueContract | The value of the quota counter to be applied to all quota counter periods.
apiInstance.quotaByCounterKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **quotaCounterKey** | **String**| Quota counter key identifier. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**QuotaCounterValueContract**](QuotaCounterValueContract.md)| The value of the quota counter to be applied to all quota counter periods. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

