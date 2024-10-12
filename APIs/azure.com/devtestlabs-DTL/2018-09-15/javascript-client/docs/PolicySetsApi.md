# DevTestLabsClient.PolicySetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policySetsEvaluatePolicies**](PolicySetsApi.md#policySetsEvaluatePolicies) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{name}/evaluatePolicies | 



## policySetsEvaluatePolicies

> EvaluatePoliciesResponse policySetsEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest)



Evaluates lab policy.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.PolicySetsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the policy set.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let evaluatePoliciesRequest = new DevTestLabsClient.EvaluatePoliciesRequest(); // EvaluatePoliciesRequest | Request body for evaluating a policy set.
apiInstance.policySetsEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **evaluatePoliciesRequest** | [**EvaluatePoliciesRequest**](EvaluatePoliciesRequest.md)| Request body for evaluating a policy set. | 

### Return type

[**EvaluatePoliciesResponse**](EvaluatePoliciesResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

