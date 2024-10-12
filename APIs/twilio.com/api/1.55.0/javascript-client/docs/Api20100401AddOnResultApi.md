# TwilioApi.Api20100401AddOnResultApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRecordingAddOnResult**](Api20100401AddOnResultApi.md#deleteRecordingAddOnResult) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json | 
[**fetchRecordingAddOnResult**](Api20100401AddOnResultApi.md#fetchRecordingAddOnResult) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json | 
[**listRecordingAddOnResult**](Api20100401AddOnResultApi.md#listRecordingAddOnResult) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults.json | 



## deleteRecordingAddOnResult

> deleteRecordingAddOnResult(accountSid, referenceSid, sid)



Delete a result and purge all associated Payloads

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddOnResultApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to delete.
let referenceSid = "referenceSid_example"; // String | The SID of the recording to which the result to delete belongs.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete.
apiInstance.deleteRecordingAddOnResult(accountSid, referenceSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to delete. | 
 **referenceSid** | **String**| The SID of the recording to which the result to delete belongs. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchRecordingAddOnResult

> ApiV2010AccountRecordingRecordingAddOnResult fetchRecordingAddOnResult(accountSid, referenceSid, sid)



Fetch an instance of an AddOnResult

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddOnResultApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource to fetch.
let referenceSid = "referenceSid_example"; // String | The SID of the recording to which the result to fetch belongs.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
apiInstance.fetchRecordingAddOnResult(accountSid, referenceSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource to fetch. | 
 **referenceSid** | **String**| The SID of the recording to which the result to fetch belongs. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch. | 

### Return type

[**ApiV2010AccountRecordingRecordingAddOnResult**](ApiV2010AccountRecordingRecordingAddOnResult.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecordingAddOnResult

> ListRecordingAddOnResultResponse listRecordingAddOnResult(accountSid, referenceSid, opts)



Retrieve a list of results belonging to the recording

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddOnResultApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to read.
let referenceSid = "referenceSid_example"; // String | The SID of the recording to which the result to read belongs.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRecordingAddOnResult(accountSid, referenceSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to read. | 
 **referenceSid** | **String**| The SID of the recording to which the result to read belongs. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRecordingAddOnResultResponse**](ListRecordingAddOnResultResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

