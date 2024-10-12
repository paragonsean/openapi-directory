# TwilioNumbers.NumbersV2HostedNumberOrderApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#createHostedNumberOrder) | **POST** /v2/HostedNumber/Orders | 
[**deleteHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#deleteHostedNumberOrder) | **DELETE** /v2/HostedNumber/Orders/{Sid} | 
[**fetchHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#fetchHostedNumberOrder) | **GET** /v2/HostedNumber/Orders/{Sid} | 
[**listHostedNumberOrder**](NumbersV2HostedNumberOrderApi.md#listHostedNumberOrder) | **GET** /v2/HostedNumber/Orders | 



## createHostedNumberOrder

> NumbersV2HostedNumberOrder createHostedNumberOrder(addressSid, contactPhoneNumber, email, phoneNumber, opts)



Host a phone number&#39;s capability on Twilio&#39;s platform.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2HostedNumberOrderApi();
let addressSid = "addressSid_example"; // String | Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
let contactPhoneNumber = "contactPhoneNumber_example"; // String | The contact phone number of the person authorized to sign the Authorization Document.
let email = "email_example"; // String | Optional. Email of the owner of this phone number that is being hosted.
let phoneNumber = "phoneNumber_example"; // String | The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
let opts = {
  'accountSid': "accountSid_example", // String | This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
  'ccEmails': ["null"], // [String] | Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
  'contactTitle': "contactTitle_example", // String | The title of the person authorized to sign the Authorization Document for this phone number.
  'friendlyName': "friendlyName_example", // String | A 128 character string that is a human readable text that describes this resource.
  'smsApplicationSid': "smsApplicationSid_example", // String | Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a `SmsApplicationSid` is present, Twilio will ignore all of the SMS urls above and use those set on the application.
  'smsCapability': true, // Boolean | Used to specify that the SMS capability will be hosted on Twilio's platform.
  'smsFallbackMethod': "smsFallbackMethod_example", // String | The HTTP method that should be used to request the SmsFallbackUrl. Must be either `GET` or `POST`. This will be copied onto the IncomingPhoneNumber resource.
  'smsFallbackUrl': "smsFallbackUrl_example", // String | A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
  'smsMethod': "smsMethod_example", // String | The HTTP method that should be used to request the SmsUrl. Must be either `GET` or `POST`.  This will be copied onto the IncomingPhoneNumber resource.
  'smsUrl': "smsUrl_example", // String | The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
  'statusCallbackUrl': "statusCallbackUrl_example" // String | Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
};
apiInstance.createHostedNumberOrder(addressSid, contactPhoneNumber, email, phoneNumber, opts, (error, data, response) => {
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
 **addressSid** | **String**| Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number. | 
 **contactPhoneNumber** | **String**| The contact phone number of the person authorized to sign the Authorization Document. | 
 **email** | **String**| Optional. Email of the owner of this phone number that is being hosted. | 
 **phoneNumber** | **String**| The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format | 
 **accountSid** | **String**| This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to. | [optional] 
 **ccEmails** | [**[String]**](String.md)| Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to. | [optional] 
 **contactTitle** | **String**| The title of the person authorized to sign the Authorization Document for this phone number. | [optional] 
 **friendlyName** | **String**| A 128 character string that is a human readable text that describes this resource. | [optional] 
 **smsApplicationSid** | **String**| Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a &#x60;SmsApplicationSid&#x60; is present, Twilio will ignore all of the SMS urls above and use those set on the application. | [optional] 
 **smsCapability** | **Boolean**| Used to specify that the SMS capability will be hosted on Twilio&#39;s platform. | [optional] 
 **smsFallbackMethod** | **String**| The HTTP method that should be used to request the SmsFallbackUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;. This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **smsFallbackUrl** | **String**| A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **smsMethod** | **String**| The HTTP method that should be used to request the SmsUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;.  This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **smsUrl** | **String**| The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource. | [optional] 
 **statusCallbackMethod** | **String**| Optional. The Status Callback Method attached to the IncomingPhoneNumber resource. | [optional] 
 **statusCallbackUrl** | **String**| Optional. The Status Callback URL attached to the IncomingPhoneNumber resource. | [optional] 

### Return type

[**NumbersV2HostedNumberOrder**](NumbersV2HostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteHostedNumberOrder

> deleteHostedNumberOrder(sid)



Cancel the HostedNumberOrder (only available when the status is in &#x60;received&#x60;).

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2HostedNumberOrderApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
apiInstance.deleteHostedNumberOrder(sid, (error, data, response) => {
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


## fetchHostedNumberOrder

> NumbersV2HostedNumberOrder fetchHostedNumberOrder(sid)



Fetch a specific HostedNumberOrder.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2HostedNumberOrderApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this HostedNumberOrder.
apiInstance.fetchHostedNumberOrder(sid, (error, data, response) => {
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

[**NumbersV2HostedNumberOrder**](NumbersV2HostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHostedNumberOrder

> ListHostedNumberOrderResponse listHostedNumberOrder(opts)



Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2HostedNumberOrderApi();
let opts = {
  'status': "status_example", // HostedNumberOrderEnumStatus | The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
  'smsCapability': true, // Boolean | Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
  'phoneNumber': "phoneNumber_example", // String | An E164 formatted phone number hosted by this HostedNumberOrder.
  'incomingPhoneNumberSid': "incomingPhoneNumberSid_example", // String | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 128 characters.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listHostedNumberOrder(opts, (error, data, response) => {
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
 **smsCapability** | **Boolean**| Whether the SMS capability will be hosted on our platform. Can be &#x60;true&#x60; of &#x60;false&#x60;. | [optional] 
 **phoneNumber** | **String**| An E164 formatted phone number hosted by this HostedNumberOrder. | [optional] 
 **incomingPhoneNumberSid** | **String**| A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. | [optional] 
 **friendlyName** | **String**| A human readable description of this resource, up to 128 characters. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListHostedNumberOrderResponse**](ListHostedNumberOrderResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

