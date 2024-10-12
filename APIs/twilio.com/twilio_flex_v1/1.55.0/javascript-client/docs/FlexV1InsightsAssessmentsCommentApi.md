# TwilioFlex.FlexV1InsightsAssessmentsCommentApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInsightsAssessmentsComment**](FlexV1InsightsAssessmentsCommentApi.md#createInsightsAssessmentsComment) | **POST** /v1/Insights/QualityManagement/Assessments/Comments | 
[**listInsightsAssessmentsComment**](FlexV1InsightsAssessmentsCommentApi.md#listInsightsAssessmentsComment) | **GET** /v1/Insights/QualityManagement/Assessments/Comments | 



## createInsightsAssessmentsComment

> FlexV1InsightsAssessmentsComment createInsightsAssessmentsComment(agentId, categoryId, categoryName, comment, offset, segmentId, opts)



To create a comment assessment for a conversation

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsAssessmentsCommentApi();
let agentId = "agentId_example"; // String | The id of the agent.
let categoryId = "categoryId_example"; // String | The ID of the category
let categoryName = "categoryName_example"; // String | The name of the category
let comment = "comment_example"; // String | The Assessment comment.
let offset = 3.4; // Number | The offset
let segmentId = "segmentId_example"; // String | The id of the segment.
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.createInsightsAssessmentsComment(agentId, categoryId, categoryName, comment, offset, segmentId, opts, (error, data, response) => {
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
 **agentId** | **String**| The id of the agent. | 
 **categoryId** | **String**| The ID of the category | 
 **categoryName** | **String**| The name of the category | 
 **comment** | **String**| The Assessment comment. | 
 **offset** | **Number**| The offset | 
 **segmentId** | **String**| The id of the segment. | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

[**FlexV1InsightsAssessmentsComment**](FlexV1InsightsAssessmentsComment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## listInsightsAssessmentsComment

> ListInsightsAssessmentsCommentResponse listInsightsAssessmentsComment(opts)



To create a comment assessment for a conversation

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsAssessmentsCommentApi();
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'segmentId': "segmentId_example", // String | The id of the segment.
  'agentId': "agentId_example", // String | The id of the agent.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInsightsAssessmentsComment(opts, (error, data, response) => {
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
 **agentId** | **String**| The id of the agent. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInsightsAssessmentsCommentResponse**](ListInsightsAssessmentsCommentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

