# TwilioStudio.StudioV1EngagementContextApi

All URIs are relative to *https://studio.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchEngagementContext**](StudioV1EngagementContextApi.md#fetchEngagementContext) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Context | 



## fetchEngagementContext

> StudioV1FlowEngagementEngagementContext fetchEngagementContext(flowSid, engagementSid)



Retrieve the most recent context for an Engagement.

### Example

```javascript
import TwilioStudio from 'twilio_studio';
let defaultClient = TwilioStudio.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioStudio.StudioV1EngagementContextApi();
let flowSid = "flowSid_example"; // String | The SID of the Flow.
let engagementSid = "engagementSid_example"; // String | The SID of the Engagement.
apiInstance.fetchEngagementContext(flowSid, engagementSid, (error, data, response) => {
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
 **flowSid** | **String**| The SID of the Flow. | 
 **engagementSid** | **String**| The SID of the Engagement. | 

### Return type

[**StudioV1FlowEngagementEngagementContext**](StudioV1FlowEngagementEngagementContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

