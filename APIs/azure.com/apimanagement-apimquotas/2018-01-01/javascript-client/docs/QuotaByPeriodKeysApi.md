# ApiManagementClient.QuotaByPeriodKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotaByPeriodKeysGet**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}/periods/{quotaPeriodKey} | 
[**quotaByPeriodKeysUpdate**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}/periods/{quotaPeriodKey} | 



## quotaByPeriodKeysGet

> QuotaCounterContract quotaByPeriodKeysGet(subscriptionId, resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion)



Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.QuotaByPeriodKeysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
let quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.quotaByPeriodKeysGet(subscriptionId, resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion, (error, data, response) => {
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
 **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | 
 **quotaPeriodKey** | **String**| Quota period key identifier. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**QuotaCounterContract**](QuotaCounterContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotaByPeriodKeysUpdate

> quotaByPeriodKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion, subscriptionId, parameters)



Updates an existing quota counter value in the specified service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.QuotaByPeriodKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
let quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.QuotaCounterValueContractProperties(); // QuotaCounterValueContractProperties | The value of the Quota counter to be applied on the specified period.
apiInstance.quotaByPeriodKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | 
 **quotaPeriodKey** | **String**| Quota period key identifier. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**QuotaCounterValueContractProperties**](QuotaCounterValueContractProperties.md)| The value of the Quota counter to be applied on the specified period. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

