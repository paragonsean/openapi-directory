# TwilioApi.Api20100401AssignedAddOnExtensionApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchIncomingPhoneNumberAssignedAddOnExtension**](Api20100401AssignedAddOnExtensionApi.md#fetchIncomingPhoneNumberAssignedAddOnExtension) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json | 
[**listIncomingPhoneNumberAssignedAddOnExtension**](Api20100401AssignedAddOnExtensionApi.md#listIncomingPhoneNumberAssignedAddOnExtension) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json | 



## fetchIncomingPhoneNumberAssignedAddOnExtension

> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension fetchIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, sid)



Fetch an instance of an Extension for the Assigned Add-on.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AssignedAddOnExtensionApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
let resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
let assignedAddOnSid = "assignedAddOnSid_example"; // String | The SID that uniquely identifies the assigned Add-on installation.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the resource to fetch.
apiInstance.fetchIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch. | 
 **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | 
 **assignedAddOnSid** | **String**| The SID that uniquely identifies the assigned Add-on installation. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the resource to fetch. | 

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIncomingPhoneNumberAssignedAddOnExtension

> ListIncomingPhoneNumberAssignedAddOnExtensionResponse listIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, opts)



Retrieve a list of Extensions for the Assigned Add-on.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AssignedAddOnExtensionApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
let resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
let assignedAddOnSid = "assignedAddOnSid_example"; // String | The SID that uniquely identifies the assigned Add-on installation.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listIncomingPhoneNumberAssignedAddOnExtension(accountSid, resourceSid, assignedAddOnSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. | 
 **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | 
 **assignedAddOnSid** | **String**| The SID that uniquely identifies the assigned Add-on installation. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListIncomingPhoneNumberAssignedAddOnExtensionResponse**](ListIncomingPhoneNumberAssignedAddOnExtensionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

