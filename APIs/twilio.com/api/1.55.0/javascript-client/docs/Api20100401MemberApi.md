# TwilioApi.Api20100401MemberApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchMember**](Api20100401MemberApi.md#fetchMember) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json | 
[**listMember**](Api20100401MemberApi.md#listMember) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json | 
[**updateMember**](Api20100401MemberApi.md#updateMember) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json | 



## fetchMember

> ApiV2010AccountQueueMember fetchMember(accountSid, queueSid, callSid)



Fetch a specific member from the queue

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MemberApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to fetch.
let queueSid = "queueSid_example"; // String | The SID of the Queue in which to find the members to fetch.
let callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to fetch.
apiInstance.fetchMember(accountSid, queueSid, callSid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to fetch. | 
 **queueSid** | **String**| The SID of the Queue in which to find the members to fetch. | 
 **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to fetch. | 

### Return type

[**ApiV2010AccountQueueMember**](ApiV2010AccountQueueMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMember

> ListMemberResponse listMember(accountSid, queueSid, opts)



Retrieve the members of the queue

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MemberApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to read.
let queueSid = "queueSid_example"; // String | The SID of the Queue in which to find the members
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMember(accountSid, queueSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to read. | 
 **queueSid** | **String**| The SID of the Queue in which to find the members | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMemberResponse**](ListMemberResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMember

> ApiV2010AccountQueueMember updateMember(accountSid, queueSid, callSid, url, opts)



Dequeue a member from a queue and have the member&#39;s call begin executing the TwiML document at that URL

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MemberApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to update.
let queueSid = "queueSid_example"; // String | The SID of the Queue in which to find the members to update.
let callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update.
let url = "url_example"; // String | The absolute URL of the Queue resource.
let opts = {
  'method': "method_example" // String | How to pass the update request data. Can be `GET` or `POST` and the default is `POST`. `POST` sends the data as encoded form data and `GET` sends the data as query parameters.
};
apiInstance.updateMember(accountSid, queueSid, callSid, url, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to update. | 
 **queueSid** | **String**| The SID of the Queue in which to find the members to update. | 
 **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update. | 
 **url** | **String**| The absolute URL of the Queue resource. | 
 **method** | **String**| How to pass the update request data. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. &#x60;POST&#x60; sends the data as encoded form data and &#x60;GET&#x60; sends the data as query parameters. | [optional] 

### Return type

[**ApiV2010AccountQueueMember**](ApiV2010AccountQueueMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

