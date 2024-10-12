# ApiManagementClient.QuotaByPeriodKeysApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotaByPeriodKeysGet**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysGet) | **GET** /quotas/{quotaCounterKey}/{quotaPeriodKey} | 
[**quotaByPeriodKeysUpdate**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysUpdate) | **PATCH** /quotas/{quotaCounterKey}/{quotaPeriodKey} | 



## quotaByPeriodKeysGet

> QuotaCounterContract quotaByPeriodKeysGet(quotaCounterKey, quotaPeriodKey, apiVersion)



Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.QuotaByPeriodKeysApi();
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
let quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.quotaByPeriodKeysGet(quotaCounterKey, quotaPeriodKey, apiVersion, (error, data, response) => {
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
 **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | 
 **quotaPeriodKey** | **String**| Quota period key identifier. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**QuotaCounterContract**](QuotaCounterContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotaByPeriodKeysUpdate

> quotaByPeriodKeysUpdate(quotaCounterKey, quotaPeriodKey, apiVersion, parameters)



Updates an existing quota counter value in the specified service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.QuotaByPeriodKeysApi();
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
let quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.QuotaCounterValueContractProperties(); // QuotaCounterValueContractProperties | The value of the Quota counter to be applied on the specified period.
apiInstance.quotaByPeriodKeysUpdate(quotaCounterKey, quotaPeriodKey, apiVersion, parameters, (error, data, response) => {
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
 **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | 
 **quotaPeriodKey** | **String**| Quota period key identifier. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**QuotaCounterValueContractProperties**](QuotaCounterValueContractProperties.md)| The value of the Quota counter to be applied on the specified period. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

