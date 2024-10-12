# ApiManagementClient.QuotaByCounterKeysApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotaByCounterKeysList**](QuotaByCounterKeysApi.md#quotaByCounterKeysList) | **GET** /quotas/{quotaCounterKey} | 
[**quotaByCounterKeysUpdate**](QuotaByCounterKeysApi.md#quotaByCounterKeysUpdate) | **PATCH** /quotas/{quotaCounterKey} | 



## quotaByCounterKeysList

> QuotaCounterCollection quotaByCounterKeysList(quotaCounterKey, apiVersion)



Lists a collection of current quota counter periods associated with the counter-key configured in the policy on the specified service instance. The api does not support paging yet.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.QuotaByCounterKeysApi();
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.quotaByCounterKeysList(quotaCounterKey, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**QuotaCounterCollection**](QuotaCounterCollection.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotaByCounterKeysUpdate

> quotaByCounterKeysUpdate(quotaCounterKey, apiVersion, parameters)



Updates all the quota counter values specified with the existing quota counter key to a value in the specified service instance. This should be used for reset of the quota counter values.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.QuotaByCounterKeysApi();
let quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.QuotaCounterValueContractProperties(); // QuotaCounterValueContractProperties | The value of the quota counter to be applied to all quota counter periods.
apiInstance.quotaByCounterKeysUpdate(quotaCounterKey, apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**QuotaCounterValueContractProperties**](QuotaCounterValueContractProperties.md)| The value of the quota counter to be applied to all quota counter periods. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

