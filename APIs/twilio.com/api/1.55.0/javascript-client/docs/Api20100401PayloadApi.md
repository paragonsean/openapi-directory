# TwilioApi.Api20100401PayloadApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRecordingAddOnResultPayload**](Api20100401PayloadApi.md#deleteRecordingAddOnResultPayload) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json | 
[**fetchRecordingAddOnResultPayload**](Api20100401PayloadApi.md#fetchRecordingAddOnResultPayload) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json | 
[**listRecordingAddOnResultPayload**](Api20100401PayloadApi.md#listRecordingAddOnResultPayload) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json | 



## deleteRecordingAddOnResultPayload

> deleteRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid)



Delete a payload from the result along with all associated Data

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401PayloadApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to delete.
let referenceSid = "referenceSid_example"; // String | The SID of the recording to which the AddOnResult resource that contains the payloads to delete belongs.
let addOnResultSid = "addOnResultSid_example"; // String | The SID of the AddOnResult to which the payloads to delete belongs.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to delete.
apiInstance.deleteRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to delete. | 
 **referenceSid** | **String**| The SID of the recording to which the AddOnResult resource that contains the payloads to delete belongs. | 
 **addOnResultSid** | **String**| The SID of the AddOnResult to which the payloads to delete belongs. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchRecordingAddOnResultPayload

> ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload fetchRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid)



Fetch an instance of a result payload

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401PayloadApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch.
let referenceSid = "referenceSid_example"; // String | The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs.
let addOnResultSid = "addOnResultSid_example"; // String | The SID of the AddOnResult to which the payload to fetch belongs.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
apiInstance.fetchRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch. | 
 **referenceSid** | **String**| The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs. | 
 **addOnResultSid** | **String**| The SID of the AddOnResult to which the payload to fetch belongs. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch. | 

### Return type

[**ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload**](ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecordingAddOnResultPayload

> ListRecordingAddOnResultPayloadResponse listRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, opts)



Retrieve a list of payloads belonging to the AddOnResult

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401PayloadApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read.
let referenceSid = "referenceSid_example"; // String | The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs.
let addOnResultSid = "addOnResultSid_example"; // String | The SID of the AddOnResult to which the payloads to read belongs.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRecordingAddOnResultPayload(accountSid, referenceSid, addOnResultSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read. | 
 **referenceSid** | **String**| The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs. | 
 **addOnResultSid** | **String**| The SID of the AddOnResult to which the payloads to read belongs. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRecordingAddOnResultPayloadResponse**](ListRecordingAddOnResultPayloadResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

