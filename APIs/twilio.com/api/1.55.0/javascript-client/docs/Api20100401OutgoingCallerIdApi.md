# TwilioApi.Api20100401OutgoingCallerIdApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#deleteOutgoingCallerId) | **DELETE** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json | 
[**fetchOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#fetchOutgoingCallerId) | **GET** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json | 
[**listOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#listOutgoingCallerId) | **GET** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json | 
[**updateOutgoingCallerId**](Api20100401OutgoingCallerIdApi.md#updateOutgoingCallerId) | **POST** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json | 



## deleteOutgoingCallerId

> deleteOutgoingCallerId(accountSid, sid)



Delete the caller-id specified from the account

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401OutgoingCallerIdApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to delete.
apiInstance.deleteOutgoingCallerId(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchOutgoingCallerId

> ApiV2010AccountOutgoingCallerId fetchOutgoingCallerId(accountSid, sid)



Fetch an outgoing-caller-id belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401OutgoingCallerIdApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to fetch.
apiInstance.fetchOutgoingCallerId(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to fetch. | 

### Return type

[**ApiV2010AccountOutgoingCallerId**](ApiV2010AccountOutgoingCallerId.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOutgoingCallerId

> ListOutgoingCallerIdResponse listOutgoingCallerId(accountSid, opts)



Retrieve a list of outgoing-caller-ids belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401OutgoingCallerIdApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read.
let opts = {
  'phoneNumber': "phoneNumber_example", // String | The phone number of the OutgoingCallerId resources to read.
  'friendlyName': "friendlyName_example", // String | The string that identifies the OutgoingCallerId resources to read.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listOutgoingCallerId(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read. | 
 **phoneNumber** | **String**| The phone number of the OutgoingCallerId resources to read. | [optional] 
 **friendlyName** | **String**| The string that identifies the OutgoingCallerId resources to read. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListOutgoingCallerIdResponse**](ListOutgoingCallerIdResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOutgoingCallerId

> ApiV2010AccountOutgoingCallerId updateOutgoingCallerId(accountSid, sid, opts)



Updates the caller-id

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401OutgoingCallerIdApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update.
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
};
apiInstance.updateOutgoingCallerId(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 

### Return type

[**ApiV2010AccountOutgoingCallerId**](ApiV2010AccountOutgoingCallerId.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

