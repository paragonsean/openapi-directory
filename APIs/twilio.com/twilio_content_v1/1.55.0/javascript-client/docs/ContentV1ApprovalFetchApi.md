# TwilioContent.ContentV1ApprovalFetchApi

All URIs are relative to *https://content.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchApprovalFetch**](ContentV1ApprovalFetchApi.md#fetchApprovalFetch) | **GET** /v1/Content/{Sid}/ApprovalRequests | 



## fetchApprovalFetch

> ContentV1ContentApprovalFetch fetchApprovalFetch(sid)



Fetch a Content resource&#39;s approval status by its unique Content Sid

### Example

```javascript
import TwilioContent from 'twilio_content';
let defaultClient = TwilioContent.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioContent.ContentV1ApprovalFetchApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Content resource whose approval information to fetch.
apiInstance.fetchApprovalFetch(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Content resource whose approval information to fetch. | 

### Return type

[**ContentV1ContentApprovalFetch**](ContentV1ContentApprovalFetch.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

