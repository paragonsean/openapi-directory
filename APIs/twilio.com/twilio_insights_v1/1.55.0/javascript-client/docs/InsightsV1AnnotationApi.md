# TwilioInsights.InsightsV1AnnotationApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAnnotation**](InsightsV1AnnotationApi.md#fetchAnnotation) | **GET** /v1/Voice/{CallSid}/Annotation | 
[**updateAnnotation**](InsightsV1AnnotationApi.md#updateAnnotation) | **POST** /v1/Voice/{CallSid}/Annotation | 



## fetchAnnotation

> InsightsV1CallAnnotation fetchAnnotation(callSid)



Get the Annotation for a specific Call.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1AnnotationApi();
let callSid = "callSid_example"; // String | The unique SID identifier of the Call.
apiInstance.fetchAnnotation(callSid, (error, data, response) => {
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
 **callSid** | **String**| The unique SID identifier of the Call. | 

### Return type

[**InsightsV1CallAnnotation**](InsightsV1CallAnnotation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAnnotation

> InsightsV1CallAnnotation updateAnnotation(callSid, opts)



Update an Annotation for a specific Call.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1AnnotationApi();
let callSid = "callSid_example"; // String | The unique string that Twilio created to identify this Call resource. It always starts with a CA.
let opts = {
  'answeredBy': "answeredBy_example", // AnnotationEnumAnsweredBy | 
  'callScore': 56, // Number | Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
  'comment': "comment_example", // String | Specify any comments pertaining to the call. `comment` has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the `comment`.
  'connectivityIssue': "connectivityIssue_example", // AnnotationEnumConnectivityIssue | 
  'incident': "incident_example", // String | Associate this call with an incident or support ticket. The `incident` parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in `incident`.
  'qualityIssues': "qualityIssues_example", // String | Specify if the call had any subjective quality issues. Possible values, one or more of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`. Use comma separated values to indicate multiple quality issues for the same call.
  'spam': true // Boolean | A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use `true` if the call was a spam call.
};
apiInstance.updateAnnotation(callSid, opts, (error, data, response) => {
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
 **callSid** | **String**| The unique string that Twilio created to identify this Call resource. It always starts with a CA. | 
 **answeredBy** | **AnnotationEnumAnsweredBy**|  | [optional] 
 **callScore** | **Number**| Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad]. | [optional] 
 **comment** | **String**| Specify any comments pertaining to the call. &#x60;comment&#x60; has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the &#x60;comment&#x60;. | [optional] 
 **connectivityIssue** | **AnnotationEnumConnectivityIssue**|  | [optional] 
 **incident** | **String**| Associate this call with an incident or support ticket. The &#x60;incident&#x60; parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in &#x60;incident&#x60;. | [optional] 
 **qualityIssues** | **String**| Specify if the call had any subjective quality issues. Possible values, one or more of &#x60;no_quality_issue&#x60;, &#x60;low_volume&#x60;, &#x60;choppy_robotic&#x60;, &#x60;echo&#x60;, &#x60;dtmf&#x60;, &#x60;latency&#x60;, &#x60;owa&#x60;, &#x60;static_noise&#x60;. Use comma separated values to indicate multiple quality issues for the same call. | [optional] 
 **spam** | **Boolean**| A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use &#x60;true&#x60; if the call was a spam call. | [optional] 

### Return type

[**InsightsV1CallAnnotation**](InsightsV1CallAnnotation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

