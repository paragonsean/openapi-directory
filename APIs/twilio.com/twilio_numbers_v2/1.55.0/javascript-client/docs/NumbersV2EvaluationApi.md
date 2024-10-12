# TwilioNumbers.NumbersV2EvaluationApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEvaluation**](NumbersV2EvaluationApi.md#createEvaluation) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations | 
[**fetchEvaluation**](NumbersV2EvaluationApi.md#fetchEvaluation) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations/{Sid} | 
[**listEvaluation**](NumbersV2EvaluationApi.md#listEvaluation) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations | 



## createEvaluation

> NumbersV2RegulatoryComplianceBundleEvaluation createEvaluation(bundleSid)



Creates an evaluation for a bundle

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EvaluationApi();
let bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle resource.
apiInstance.createEvaluation(bundleSid, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that identifies the Bundle resource. | 

### Return type

[**NumbersV2RegulatoryComplianceBundleEvaluation**](NumbersV2RegulatoryComplianceBundleEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchEvaluation

> NumbersV2RegulatoryComplianceBundleEvaluation fetchEvaluation(bundleSid, sid)



Fetch specific Evaluation Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EvaluationApi();
let bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
let sid = "sid_example"; // String | The unique string that identifies the Evaluation resource.
apiInstance.fetchEvaluation(bundleSid, sid, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | 
 **sid** | **String**| The unique string that identifies the Evaluation resource. | 

### Return type

[**NumbersV2RegulatoryComplianceBundleEvaluation**](NumbersV2RegulatoryComplianceBundleEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEvaluation

> ListEvaluationResponse listEvaluation(bundleSid, opts)



Retrieve a list of Evaluations associated to the Bundle resource.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EvaluationApi();
let bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEvaluation(bundleSid, opts, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that identifies the Bundle resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEvaluationResponse**](ListEvaluationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

