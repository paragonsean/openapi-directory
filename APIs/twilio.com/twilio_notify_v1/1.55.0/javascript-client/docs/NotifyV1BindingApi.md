# TwilioNotify.NotifyV1BindingApi

All URIs are relative to *https://notify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBinding**](NotifyV1BindingApi.md#createBinding) | **POST** /v1/Services/{ServiceSid}/Bindings | 
[**deleteBinding**](NotifyV1BindingApi.md#deleteBinding) | **DELETE** /v1/Services/{ServiceSid}/Bindings/{Sid} | 
[**fetchBinding**](NotifyV1BindingApi.md#fetchBinding) | **GET** /v1/Services/{ServiceSid}/Bindings/{Sid} | 
[**listBinding**](NotifyV1BindingApi.md#listBinding) | **GET** /v1/Services/{ServiceSid}/Bindings | 



## createBinding

> NotifyV1ServiceBinding createBinding(serviceSid, address, bindingType, identity, opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1BindingApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to create the resource under.
let address = "address_example"; // String | The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
let bindingType = "bindingType_example"; // BindingEnumBindingType | 
let identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
let opts = {
  'credentialSid': "credentialSid_example", // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only `apn`, `fcm`, and `gcm` type Bindings.
  'endpoint': "endpoint_example", // String | Deprecated.
  'notificationProtocolVersion': "notificationProtocolVersion_example", // String | The protocol version to use to send the notification. This defaults to the value of `default_xxxx_notification_protocol_version` for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is `\\\"3\\\"` for `apn`, `fcm`, and `gcm` type Bindings. The parameter is not applicable to `sms` and `facebook-messenger` type Bindings as the data format is fixed.
  'tag': ["null"] // [String] | A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags.
};
apiInstance.createBinding(serviceSid, address, bindingType, identity, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to create the resource under. | 
 **address** | **String**| The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format. | 
 **bindingType** | **BindingEnumBindingType**|  | 
 **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service. | 
 **credentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings. | [optional] 
 **endpoint** | **String**| Deprecated. | [optional] 
 **notificationProtocolVersion** | **String**| The protocol version to use to send the notification. This defaults to the value of &#x60;default_xxxx_notification_protocol_version&#x60; for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is &#x60;\\\&quot;3\\\&quot;&#x60; for &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings. The parameter is not applicable to &#x60;sms&#x60; and &#x60;facebook-messenger&#x60; type Bindings as the data format is fixed. | [optional] 
 **tag** | [**[String]**](String.md)| A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags. | [optional] 

### Return type

[**NotifyV1ServiceBinding**](NotifyV1ServiceBinding.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteBinding

> deleteBinding(serviceSid, sid)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1BindingApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to delete the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Binding resource to delete.
apiInstance.deleteBinding(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to delete the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Binding resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchBinding

> NotifyV1ServiceBinding fetchBinding(serviceSid, sid)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1BindingApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to fetch the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Binding resource to fetch.
apiInstance.fetchBinding(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to fetch the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Binding resource to fetch. | 

### Return type

[**NotifyV1ServiceBinding**](NotifyV1ServiceBinding.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBinding

> ListBindingResponse listBinding(serviceSid, opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1BindingApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to read the resource from.
let opts = {
  'startDate': new Date("2013-10-20"), // Date | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
  'endDate': new Date("2013-10-20"), // Date | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
  'identity': ["null"], // [String] | The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
  'tag': ["null"], // [String] | Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBinding(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to read the resource from. | 
 **startDate** | **Date**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **endDate** | **Date**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **identity** | [**[String]**](String.md)| The [User](https://www.twilio.com/docs/chat/rest/user-resource)&#39;s &#x60;identity&#x60; value of the resources to read. | [optional] 
 **tag** | [**[String]**](String.md)| Only list Bindings that have all of the specified Tags. The following implicit tags are available: &#x60;all&#x60;, &#x60;apn&#x60;, &#x60;fcm&#x60;, &#x60;gcm&#x60;, &#x60;sms&#x60;, &#x60;facebook-messenger&#x60;. Up to 5 tags are allowed. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBindingResponse**](ListBindingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

