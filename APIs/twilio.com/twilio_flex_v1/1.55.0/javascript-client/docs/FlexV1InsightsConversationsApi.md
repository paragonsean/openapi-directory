# TwilioFlex.FlexV1InsightsConversationsApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listInsightsConversations**](FlexV1InsightsConversationsApi.md#listInsightsConversations) | **GET** /v1/Insights/Conversations | 



## listInsightsConversations

> ListInsightsConversationsResponse listInsightsConversations(opts)



To get conversation with segment id

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsConversationsApi();
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'segmentId': "segmentId_example", // String | Unique Id of the segment for which conversation details needs to be fetched
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInsightsConversations(opts, (error, data, response) => {
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
 **segmentId** | **String**| Unique Id of the segment for which conversation details needs to be fetched | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInsightsConversationsResponse**](ListInsightsConversationsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

