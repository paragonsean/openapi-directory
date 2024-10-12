# TwilioFlex.FlexV1InsightsQuestionnairesQuestionApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#createInsightsQuestionnairesQuestion) | **POST** /v1/Insights/QualityManagement/Questions | 
[**deleteInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#deleteInsightsQuestionnairesQuestion) | **DELETE** /v1/Insights/QualityManagement/Questions/{QuestionSid} | 
[**listInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#listInsightsQuestionnairesQuestion) | **GET** /v1/Insights/QualityManagement/Questions | 
[**updateInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#updateInsightsQuestionnairesQuestion) | **POST** /v1/Insights/QualityManagement/Questions/{QuestionSid} | 



## createInsightsQuestionnairesQuestion

> FlexV1InsightsQuestionnairesQuestion createInsightsQuestionnairesQuestion(allowNa, answerSetId, categorySid, question, opts)



To create a question for a Category

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesQuestionApi();
let allowNa = true; // Boolean | The flag to enable for disable NA for answer.
let answerSetId = "answerSetId_example"; // String | The answer_set for the question.
let categorySid = "categorySid_example"; // String | The SID of the category
let question = "question_example"; // String | The question.
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'description': "description_example" // String | The description for the question.
};
apiInstance.createInsightsQuestionnairesQuestion(allowNa, answerSetId, categorySid, question, opts, (error, data, response) => {
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
 **allowNa** | **Boolean**| The flag to enable for disable NA for answer. | 
 **answerSetId** | **String**| The answer_set for the question. | 
 **categorySid** | **String**| The SID of the category | 
 **question** | **String**| The question. | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 
 **description** | **String**| The description for the question. | [optional] 

### Return type

[**FlexV1InsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteInsightsQuestionnairesQuestion

> deleteInsightsQuestionnairesQuestion(questionSid, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesQuestionApi();
let questionSid = "questionSid_example"; // String | The SID of the question
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.deleteInsightsQuestionnairesQuestion(questionSid, opts, (error, data, response) => {
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
 **questionSid** | **String**| The SID of the question | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listInsightsQuestionnairesQuestion

> ListInsightsQuestionnairesQuestionResponse listInsightsQuestionnairesQuestion(opts)



To get all the question for the given categories

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesQuestionApi();
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'categorySid': ["null"], // [String] | The list of category SIDs
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInsightsQuestionnairesQuestion(opts, (error, data, response) => {
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
 **categorySid** | [**[String]**](String.md)| The list of category SIDs | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInsightsQuestionnairesQuestionResponse**](ListInsightsQuestionnairesQuestionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInsightsQuestionnairesQuestion

> FlexV1InsightsQuestionnairesQuestion updateInsightsQuestionnairesQuestion(questionSid, allowNa, opts)



To update the question

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesQuestionApi();
let questionSid = "questionSid_example"; // String | The SID of the question
let allowNa = true; // Boolean | The flag to enable for disable NA for answer.
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'answerSetId': "answerSetId_example", // String | The answer_set for the question.
  'categorySid': "categorySid_example", // String | The SID of the category
  'description': "description_example", // String | The description for the question.
  'question': "question_example" // String | The question.
};
apiInstance.updateInsightsQuestionnairesQuestion(questionSid, allowNa, opts, (error, data, response) => {
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
 **questionSid** | **String**| The SID of the question | 
 **allowNa** | **Boolean**| The flag to enable for disable NA for answer. | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 
 **answerSetId** | **String**| The answer_set for the question. | [optional] 
 **categorySid** | **String**| The SID of the category | [optional] 
 **description** | **String**| The description for the question. | [optional] 
 **question** | **String**| The question. | [optional] 

### Return type

[**FlexV1InsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

