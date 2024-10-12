# TwilioPreview.PreviewHostedNumbersHostedNumberOrderApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#createHostedNumbersHostedNumberOrder) | **POST** /HostedNumbers/HostedNumberOrders | 
[**deleteHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#deleteHostedNumbersHostedNumberOrder) | **DELETE** /HostedNumbers/HostedNumberOrders/{Sid} | 
[**fetchHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#fetchHostedNumbersHostedNumberOrder) | **GET** /HostedNumbers/HostedNumberOrders/{Sid} | 
[**listHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#listHostedNumbersHostedNumberOrder) | **GET** /HostedNumbers/HostedNumberOrders | 
[**updateHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrderApi.md#updateHostedNumbersHostedNumberOrder) | **POST** /HostedNumbers/HostedNumberOrders/{Sid} | 



## createHostedNumbersHostedNumberOrder

> PreviewHostedNumbersHostedNumberOrder createHostedNumbersHostedNumberOrder(phoneNumber, smsCapability, opts)



Host a phone number&#39;s capability on Twilio&#39;s platform.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersHostedNumberOrderApi();
let phoneNumber = "phoneNumber_example"; // String | The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
let smsCapability = true; // Boolean | Used to specify that the SMS capability will be hosted on Twilio's platform.
let opts = {
  'accountSid': "accountSid_example", // String | This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
  'addressSid': "addressSid_example", // String | Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
  'ccEmails': ["null"], // [String] | Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
  'email': "email_example", // String | Optional. Email of the owner of this phone number that is being hosted.
  'friendlyName': "friendlyName_example", // String | A 64 character string that is a human readable text that describes this resource.
  'smsApplicationSid': "smsApplicationSid_example", // String | Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a `SmsApplicationSid` is present, Twilio will ignore all of the SMS urls above and use those set on the application.
  'smsFallbackMethod': "smsFallbackMethod_example", // String | The HTTP method that should be used to request the SmsFallbackUrl. Must be either `GET` or `POST`. This will be copied onto the IncomingPhoneNumber resource.
  'smsFallbackUrl': "smsFallbackUrl_example", // String | A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
  'smsMethod': "smsMethod_example", // String | The HTTP method that should be used to request the SmsUrl. Must be either `GET` or `POST`.  This will be copied onto the IncomingPhoneNumber resource.
  'smsUrl': "smsUrl_example", // String | The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
  'statusCallbackUrl': "statusCallbackUrl_example", // String | Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
  'uniqueName': "uniqueName_example", // String | Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
  'verificationDocumentSid': "verificationDocumentSid_example", // String | Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
  'verificationType': "verificationType_example" // HostedNumberOrderEnumVerificationType | 
};
apiInstance.createHostedNumbersHostedNumberOrder(phoneNumber, smsCapability, opts, (error, data, response) => {
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
 **phoneNumber** | **String**| The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format | 
 **smsCapability** | **Boolean**| Used to specify that the SMS capability will be hosted on Twilio&#39;s platform. | 
 **accountSid** | **String**| This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to. | [optional] 
 **addressSid** | **String**| Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. | [optional] 
 **ccEmails** | [**[String]**](String.md)| Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to. | [optional] 
 **email** | **String**| Optional. Email of the owner of this phone number that is being hosted. | [optional] 
 **friendlyName** | **String**| A 64 character string that is a human readable text that describes this resource. | [optional] 
 **smsApplicationSid** | **String**| Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a &#x60;SmsApplicationSid&#x60; is present, Twilio will ignore all of the SMS urls above and use those set on the application. | [optional] 
 **smsFallbackMethod** | **String**| The HTTP method that should be used to request the SmsFallbackUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;. This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **smsFallbackUrl** | **String**| A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **smsMethod** | **String**| The HTTP method that should be used to request the SmsUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;.  This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **smsUrl** | **String**| The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **statusCallbackMethod** | **String**| Optional. The Status Callback Method attached to the IncomingPhoneNumber resource. | [optional] 
 **statusCallbackUrl** | **String**| Optional. The Status Callback URL attached to the IncomingPhoneNumber resource. | [optional] 
 **uniqueName** | **String**| Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] 
 **verificationDocumentSid** | **String**| Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill. | [optional] 
 **verificationType** | **HostedNumberOrderEnumVerificationType**|  | [optional] 

### Return type

[**PreviewHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteHostedNumbersHostedNumberOrder

> deleteHostedNumbersHostedNumberOrder(sid)



Cancel the HostedNumberOrder (only available when the status is in &#x60;received&#x60;).

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersHostedNumberOrderApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
apiInstance.deleteHostedNumbersHostedNumberOrder(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this HostedNumberOrder. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchHostedNumbersHostedNumberOrder

> PreviewHostedNumbersHostedNumberOrder fetchHostedNumbersHostedNumberOrder(sid)



Fetch a specific HostedNumberOrder.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersHostedNumberOrderApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
apiInstance.fetchHostedNumbersHostedNumberOrder(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this HostedNumberOrder. | 

### Return type

[**PreviewHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHostedNumbersHostedNumberOrder

> ListHostedNumbersHostedNumberOrderResponse listHostedNumbersHostedNumberOrder(opts)



Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersHostedNumberOrderApi();
let opts = {
  'status': "status_example", // HostedNumberOrderEnumStatus | The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
  'phoneNumber': "phoneNumber_example", // String | An E164 formatted phone number hosted by this HostedNumberOrder.
  'incomingPhoneNumberSid': "incomingPhoneNumberSid_example", // String | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 64 characters.
  'uniqueName': "uniqueName_example", // String | Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listHostedNumbersHostedNumberOrder(opts, (error, data, response) => {
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
 **status** | **HostedNumberOrderEnumStatus**| The Status of this HostedNumberOrder. One of &#x60;received&#x60;, &#x60;pending-verification&#x60;, &#x60;verified&#x60;, &#x60;pending-loa&#x60;, &#x60;carrier-processing&#x60;, &#x60;testing&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, or &#x60;action-required&#x60;. | [optional] 
 **phoneNumber** | **String**| An E164 formatted phone number hosted by this HostedNumberOrder. | [optional] 
 **incomingPhoneNumberSid** | **String**| A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. | [optional] 
 **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] 
 **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListHostedNumbersHostedNumberOrderResponse**](ListHostedNumbersHostedNumberOrderResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateHostedNumbersHostedNumberOrder

> PreviewHostedNumbersHostedNumberOrder updateHostedNumbersHostedNumberOrder(sid, opts)



Updates a specific HostedNumberOrder.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersHostedNumberOrderApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
let opts = {
  'callDelay': 56, // Number | The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0.
  'ccEmails': ["null"], // [String] | Optional. A list of emails that LOA document for this HostedNumberOrder will be carbon copied to.
  'email': "email_example", // String | Email of the owner of this phone number that is being hosted.
  'extension': "extension_example", // String | Digits to dial after connecting the verification call.
  'friendlyName': "friendlyName_example", // String | A 64 character string that is a human readable text that describes this resource.
  'status': "status_example", // HostedNumberOrderEnumStatus | 
  'uniqueName': "uniqueName_example", // String | Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
  'verificationCode': "verificationCode_example", // String | A verification code that is given to the user via a phone call to the phone number that is being hosted.
  'verificationDocumentSid': "verificationDocumentSid_example", // String | Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
  'verificationType': "verificationType_example" // HostedNumberOrderEnumVerificationType | 
};
apiInstance.updateHostedNumbersHostedNumberOrder(sid, opts, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this HostedNumberOrder. | 
 **callDelay** | **Number**| The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0. | [optional] 
 **ccEmails** | [**[String]**](String.md)| Optional. A list of emails that LOA document for this HostedNumberOrder will be carbon copied to. | [optional] 
 **email** | **String**| Email of the owner of this phone number that is being hosted. | [optional] 
 **extension** | **String**| Digits to dial after connecting the verification call. | [optional] 
 **friendlyName** | **String**| A 64 character string that is a human readable text that describes this resource. | [optional] 
 **status** | **HostedNumberOrderEnumStatus**|  | [optional] 
 **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] 
 **verificationCode** | **String**| A verification code that is given to the user via a phone call to the phone number that is being hosted. | [optional] 
 **verificationDocumentSid** | **String**| Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill. | [optional] 
 **verificationType** | **HostedNumberOrderEnumVerificationType**|  | [optional] 

### Return type

[**PreviewHostedNumbersHostedNumberOrder**](PreviewHostedNumbersHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

