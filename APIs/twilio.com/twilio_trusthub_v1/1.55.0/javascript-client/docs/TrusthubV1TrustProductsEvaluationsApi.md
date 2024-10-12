# TwilioTrusthub.TrusthubV1TrustProductsEvaluationsApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTrustProductEvaluation**](TrusthubV1TrustProductsEvaluationsApi.md#createTrustProductEvaluation) | **POST** /v1/TrustProducts/{TrustProductSid}/Evaluations | 
[**fetchTrustProductEvaluation**](TrusthubV1TrustProductsEvaluationsApi.md#fetchTrustProductEvaluation) | **GET** /v1/TrustProducts/{TrustProductSid}/Evaluations/{Sid} | 
[**listTrustProductEvaluation**](TrusthubV1TrustProductsEvaluationsApi.md#listTrustProductEvaluation) | **GET** /v1/TrustProducts/{TrustProductSid}/Evaluations | 



## createTrustProductEvaluation

> TrusthubV1TrustProductTrustProductEvaluation createTrustProductEvaluation(trustProductSid, policySid)



Create a new Evaluation

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsEvaluationsApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the trust_product resource.
let policySid = "policySid_example"; // String | The unique string of a policy that is associated to the customer_profile resource.
apiInstance.createTrustProductEvaluation(trustProductSid, policySid, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the trust_product resource. | 
 **policySid** | **String**| The unique string of a policy that is associated to the customer_profile resource. | 

### Return type

[**TrusthubV1TrustProductTrustProductEvaluation**](TrusthubV1TrustProductTrustProductEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchTrustProductEvaluation

> TrusthubV1TrustProductTrustProductEvaluation fetchTrustProductEvaluation(trustProductSid, sid)



Fetch specific Evaluation Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsEvaluationsApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the trust_product resource.
let sid = "sid_example"; // String | The unique string that identifies the Evaluation resource.
apiInstance.fetchTrustProductEvaluation(trustProductSid, sid, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the trust_product resource. | 
 **sid** | **String**| The unique string that identifies the Evaluation resource. | 

### Return type

[**TrusthubV1TrustProductTrustProductEvaluation**](TrusthubV1TrustProductTrustProductEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTrustProductEvaluation

> ListTrustProductEvaluationResponse listTrustProductEvaluation(trustProductSid, opts)



Retrieve a list of Evaluations associated to the trust_product resource.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsEvaluationsApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the trust_product resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTrustProductEvaluation(trustProductSid, opts, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the trust_product resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTrustProductEvaluationResponse**](ListTrustProductEvaluationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

