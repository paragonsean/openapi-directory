# TwilioTrusthub.TrusthubV1CustomerProfilesEvaluationsApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomerProfileEvaluation**](TrusthubV1CustomerProfilesEvaluationsApi.md#createCustomerProfileEvaluation) | **POST** /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations | 
[**fetchCustomerProfileEvaluation**](TrusthubV1CustomerProfilesEvaluationsApi.md#fetchCustomerProfileEvaluation) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations/{Sid} | 
[**listCustomerProfileEvaluation**](TrusthubV1CustomerProfilesEvaluationsApi.md#listCustomerProfileEvaluation) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations | 



## createCustomerProfileEvaluation

> TrusthubV1CustomerProfileCustomerProfileEvaluation createCustomerProfileEvaluation(customerProfileSid, policySid)



Create a new Evaluation

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesEvaluationsApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let policySid = "policySid_example"; // String | The unique string of a policy that is associated to the customer_profile resource.
apiInstance.createCustomerProfileEvaluation(customerProfileSid, policySid, (error, data, response) => {
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
 **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **policySid** | **String**| The unique string of a policy that is associated to the customer_profile resource. | 

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEvaluation**](TrusthubV1CustomerProfileCustomerProfileEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchCustomerProfileEvaluation

> TrusthubV1CustomerProfileCustomerProfileEvaluation fetchCustomerProfileEvaluation(customerProfileSid, sid)



Fetch specific Evaluation Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesEvaluationsApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the customer_profile resource.
let sid = "sid_example"; // String | The unique string that identifies the Evaluation resource.
apiInstance.fetchCustomerProfileEvaluation(customerProfileSid, sid, (error, data, response) => {
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
 **customerProfileSid** | **String**| The unique string that we created to identify the customer_profile resource. | 
 **sid** | **String**| The unique string that identifies the Evaluation resource. | 

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEvaluation**](TrusthubV1CustomerProfileCustomerProfileEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomerProfileEvaluation

> ListCustomerProfileEvaluationResponse listCustomerProfileEvaluation(customerProfileSid, opts)



Retrieve a list of Evaluations associated to the customer_profile resource.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesEvaluationsApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCustomerProfileEvaluation(customerProfileSid, opts, (error, data, response) => {
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
 **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCustomerProfileEvaluationResponse**](ListCustomerProfileEvaluationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

