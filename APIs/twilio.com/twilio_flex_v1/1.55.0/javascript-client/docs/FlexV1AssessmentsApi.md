# TwilioFlex.FlexV1AssessmentsApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInsightsAssessments**](FlexV1AssessmentsApi.md#createInsightsAssessments) | **POST** /v1/Insights/QualityManagement/Assessments | 
[**listInsightsAssessments**](FlexV1AssessmentsApi.md#listInsightsAssessments) | **GET** /v1/Insights/QualityManagement/Assessments | 
[**updateInsightsAssessments**](FlexV1AssessmentsApi.md#updateInsightsAssessments) | **POST** /v1/Insights/QualityManagement/Assessments/{AssessmentSid} | 



## createInsightsAssessments

> FlexV1InsightsAssessments createInsightsAssessments(agentId, answerId, answerText, categoryName, categorySid, metricId, metricName, offset, questionnaireSid, segmentId, opts)



Add assessments against conversation to dynamo db. Used in assessments screen by user. Users can select the questionnaire and pick up answers for each and every question.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1AssessmentsApi();
let agentId = "agentId_example"; // String | The id of the Agent
let answerId = "answerId_example"; // String | The id of the answer selected by user
let answerText = "answerText_example"; // String | The answer text selected by user
let categoryName = "categoryName_example"; // String | The name of the category
let categorySid = "categorySid_example"; // String | The SID of the category 
let metricId = "metricId_example"; // String | The question SID selected for assessment
let metricName = "metricName_example"; // String | The question name of the assessment
let offset = 3.4; // Number | The offset of the conversation.
let questionnaireSid = "questionnaireSid_example"; // String | Questionnaire SID of the associated question
let segmentId = "segmentId_example"; // String | Segment Id of the conversation
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.createInsightsAssessments(agentId, answerId, answerText, categoryName, categorySid, metricId, metricName, offset, questionnaireSid, segmentId, opts, (error, data, response) => {
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
 **agentId** | **String**| The id of the Agent | 
 **answerId** | **String**| The id of the answer selected by user | 
 **answerText** | **String**| The answer text selected by user | 
 **categoryName** | **String**| The name of the category | 
 **categorySid** | **String**| The SID of the category  | 
 **metricId** | **String**| The question SID selected for assessment | 
 **metricName** | **String**| The question name of the assessment | 
 **offset** | **Number**| The offset of the conversation. | 
 **questionnaireSid** | **String**| Questionnaire SID of the associated question | 
 **segmentId** | **String**| Segment Id of the conversation | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

[**FlexV1InsightsAssessments**](FlexV1InsightsAssessments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## listInsightsAssessments

> ListInsightsAssessmentsResponse listInsightsAssessments(opts)



Get assessments done for a conversation by logged in user

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1AssessmentsApi();
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'segmentId': "segmentId_example", // String | The id of the segment.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInsightsAssessments(opts, (error, data, response) => {
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
 **authorization** | **String**| The Authorization HTTP request header | [optional] 
 **segmentId** | **String**| The id of the segment. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInsightsAssessmentsResponse**](ListInsightsAssessmentsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInsightsAssessments

> FlexV1InsightsAssessments updateInsightsAssessments(assessmentSid, answerId, answerText, offset, opts)



Update a specific Assessment assessed earlier

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1AssessmentsApi();
let assessmentSid = "assessmentSid_example"; // String | The SID of the assessment to be modified
let answerId = "answerId_example"; // String | The id of the answer selected by user
let answerText = "answerText_example"; // String | The answer text selected by user
let offset = 3.4; // Number | The offset of the conversation
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.updateInsightsAssessments(assessmentSid, answerId, answerText, offset, opts, (error, data, response) => {
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
 **assessmentSid** | **String**| The SID of the assessment to be modified | 
 **answerId** | **String**| The id of the answer selected by user | 
 **answerText** | **String**| The answer text selected by user | 
 **offset** | **Number**| The offset of the conversation | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

[**FlexV1InsightsAssessments**](FlexV1InsightsAssessments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

