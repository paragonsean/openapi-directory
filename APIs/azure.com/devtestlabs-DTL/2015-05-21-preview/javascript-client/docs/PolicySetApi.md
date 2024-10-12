# DevTestLabsClient.PolicySetApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policySetEvaluatePolicies**](PolicySetApi.md#policySetEvaluatePolicies) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{name}/evaluatePolicies | 



## policySetEvaluatePolicies

> EvaluatePoliciesResponse policySetEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest)



Evaluates Lab Policy.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.PolicySetApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the policy set.
let apiVersion = "'2015-05-21-preview'"; // String | Client API version.
let evaluatePoliciesRequest = new DevTestLabsClient.EvaluatePoliciesRequest(); // EvaluatePoliciesRequest | 
apiInstance.policySetEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the policy set. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2015-05-21-preview&#39;]
 **evaluatePoliciesRequest** | [**EvaluatePoliciesRequest**](EvaluatePoliciesRequest.md)|  | 

### Return type

[**EvaluatePoliciesResponse**](EvaluatePoliciesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

