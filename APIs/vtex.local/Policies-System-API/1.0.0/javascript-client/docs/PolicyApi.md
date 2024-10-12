# PoliciesSystemApi.PolicyApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPolicyEnginePoliciesIdPut**](PolicyApi.md#apiPolicyEnginePoliciesIdPut) | **PUT** /api/policy-engine/policies/{id} | Update Policy
[**policyCreateOrUpdate**](PolicyApi.md#policyCreateOrUpdate) | **POST** /api/policy-engine/policies/{id} | Create Policy
[**policyDelete**](PolicyApi.md#policyDelete) | **DELETE** /api/policy-engine/policies/{id} | Delete Policy by ID
[**policyEvaluate**](PolicyApi.md#policyEvaluate) | **POST** /api/policy-engine/evaluate | Evaluate Policies
[**policyGet**](PolicyApi.md#policyGet) | **GET** /api/policy-engine/policies/{id} | Get Policy by ID
[**policyList**](PolicyApi.md#policyList) | **GET** /api/policy-engine/policies | Get Policy List



## apiPolicyEnginePoliciesIdPut

> [PolicyGetResponse] apiPolicyEnginePoliciesIdPut(contentType, accept, id, policySaveRequest)

Update Policy

Updates an existing policy at your account.

### Example

```javascript
import PoliciesSystemApi from 'policies_system_api';

let apiInstance = new PoliciesSystemApi.PolicyApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let id = "'pa_test_001'"; // String | Policy ID
let policySaveRequest = new PoliciesSystemApi.PolicySaveRequest(); // PolicySaveRequest | 
apiInstance.apiPolicyEnginePoliciesIdPut(contentType, accept, id, policySaveRequest, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/json&#39;]
 **id** | **String**| Policy ID | [default to &#39;pa_test_001&#39;]
 **policySaveRequest** | [**PolicySaveRequest**](PolicySaveRequest.md)|  | 

### Return type

[**[PolicyGetResponse]**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## policyCreateOrUpdate

> [PolicyGetResponse] policyCreateOrUpdate(contentType, accept, id, opts)

Create Policy

Creates a new policy from scratch.

### Example

```javascript
import PoliciesSystemApi from 'policies_system_api';

let apiInstance = new PoliciesSystemApi.PolicyApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let id = "'pa_test_001'"; // String | Policy ID
let opts = {
  'policySaveRequest': {"description":"TesteMarcosPromotionsAlert","name":"TestAlarmBerenice","statements":[{"actions":[{"id":"SendSlackMessage","metadata":{"alertDescription":"Avoid selling products from Berenice with a discount greater than 40%.","channel":"C01NJFF35R6","relatedUsers":["URUNDC2NB"]}}],"condition":{"conditions":[{"conditions":[],"key":"brandId","operation":"stringEquals","values":["2000001"]},{"conditions":[],"key":"discountPercentage","operation":"numericGreaterThan","values":["40.00"]}],"operation":"and"},"effect":"Allow","resource":"vrn:vtex.promotions-alert:aws-us-east-1:kamila:master:/_v/promotions_alert"}]} // PolicySaveRequest | 
};
apiInstance.policyCreateOrUpdate(contentType, accept, id, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/json&#39;]
 **id** | **String**| Policy ID | [default to &#39;pa_test_001&#39;]
 **policySaveRequest** | [**PolicySaveRequest**](PolicySaveRequest.md)|  | [optional] 

### Return type

[**[PolicyGetResponse]**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## policyDelete

> policyDelete(contentType, accept, id)

Delete Policy by ID

Deletes a specific policy of the account by its ID.

### Example

```javascript
import PoliciesSystemApi from 'policies_system_api';

let apiInstance = new PoliciesSystemApi.PolicyApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let id = "'pa_test_001'"; // String | Policy ID
apiInstance.policyDelete(contentType, accept, id, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/json&#39;]
 **id** | **String**| Policy ID | [default to &#39;pa_test_001&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## policyEvaluate

> [PolicyActionGetResponse] policyEvaluate(contentType, accept, evaluatePolicyRequest)

Evaluate Policies

This endpoint consults all policies and checks the ones that satisfy the request body’s conditions.

### Example

```javascript
import PoliciesSystemApi from 'policies_system_api';

let apiInstance = new PoliciesSystemApi.PolicyApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let evaluatePolicyRequest = {"context":{"brandId":"2000001","discountPercentage":"91.00"},"resource":"vrn:vtex.promotions-alert:aws-us-east-1:kamila:master:/_v/promotions_alert"}; // EvaluatePolicyRequest | 
apiInstance.policyEvaluate(contentType, accept, evaluatePolicyRequest, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/json&#39;]
 **evaluatePolicyRequest** | [**EvaluatePolicyRequest**](EvaluatePolicyRequest.md)|  | 

### Return type

[**[PolicyActionGetResponse]**](PolicyActionGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policyGet

> [PolicyGetResponse] policyGet(contentType, accept, id)

Get Policy by ID

Retrieves general information of a policy by its ID.

### Example

```javascript
import PoliciesSystemApi from 'policies_system_api';

let apiInstance = new PoliciesSystemApi.PolicyApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let id = "'pa_test_001'"; // String | Policy ID
apiInstance.policyGet(contentType, accept, id, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/json&#39;]
 **id** | **String**| Policy ID | [default to &#39;pa_test_001&#39;]

### Return type

[**[PolicyGetResponse]**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyList

> [PolicyGetResponse] policyList(contentType, accept)

Get Policy List

Retrieves a list of all policies in the account and general information of each policy.

### Example

```javascript
import PoliciesSystemApi from 'policies_system_api';

let apiInstance = new PoliciesSystemApi.PolicyApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
apiInstance.policyList(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/json&#39;]

### Return type

[**[PolicyGetResponse]**](PolicyGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

