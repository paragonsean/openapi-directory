# TwilioWireless.WirelessV1CommandApi

All URIs are relative to *https://wireless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCommand**](WirelessV1CommandApi.md#createCommand) | **POST** /v1/Commands | 
[**deleteCommand**](WirelessV1CommandApi.md#deleteCommand) | **DELETE** /v1/Commands/{Sid} | 
[**fetchCommand**](WirelessV1CommandApi.md#fetchCommand) | **GET** /v1/Commands/{Sid} | 
[**listCommand**](WirelessV1CommandApi.md#listCommand) | **GET** /v1/Commands | 



## createCommand

> WirelessV1Command createCommand(command, opts)



Send a Command to a Sim.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1CommandApi();
let command = "command_example"; // String | The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode.
let opts = {
  'callbackMethod': "callbackMethod_example", // String | The HTTP method we use to call `callback_url`. Can be: `POST` or `GET`, and the default is `POST`.
  'callbackUrl': "callbackUrl_example", // String | The URL we call using the `callback_url` when the Command has finished sending, whether the command was delivered or it failed.
  'commandMode': "commandMode_example", // CommandEnumCommandMode | 
  'deliveryReceiptRequested': true, // Boolean | Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to 'delivered' once the server has received a delivery receipt from the device. The default value is `true`.
  'includeSid': "includeSid_example", // String | Whether to include the SID of the command in the message body. Can be: `none`, `start`, or `end`, and the default behavior is `none`. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of `start` will prepend the message with the Command SID, and `end` will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included.
  'sim': "sim_example" // String | The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to send the Command to.
};
apiInstance.createCommand(command, opts, (error, data, response) => {
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
 **command** | **String**| The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode. | 
 **callbackMethod** | **String**| The HTTP method we use to call &#x60;callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;, and the default is &#x60;POST&#x60;. | [optional] 
 **callbackUrl** | **String**| The URL we call using the &#x60;callback_url&#x60; when the Command has finished sending, whether the command was delivered or it failed. | [optional] 
 **commandMode** | **CommandEnumCommandMode**|  | [optional] 
 **deliveryReceiptRequested** | **Boolean**| Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to &#39;delivered&#39; once the server has received a delivery receipt from the device. The default value is &#x60;true&#x60;. | [optional] 
 **includeSid** | **String**| Whether to include the SID of the command in the message body. Can be: &#x60;none&#x60;, &#x60;start&#x60;, or &#x60;end&#x60;, and the default behavior is &#x60;none&#x60;. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of &#x60;start&#x60; will prepend the message with the Command SID, and &#x60;end&#x60; will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included. | [optional] 
 **sim** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to send the Command to. | [optional] 

### Return type

[**WirelessV1Command**](WirelessV1Command.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCommand

> deleteCommand(sid)



Delete a Command instance from your account.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1CommandApi();
let sid = "sid_example"; // String | The SID of the Command resource to delete.
apiInstance.deleteCommand(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Command resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCommand

> WirelessV1Command fetchCommand(sid)



Fetch a Command instance from your account.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1CommandApi();
let sid = "sid_example"; // String | The SID of the Command resource to fetch.
apiInstance.fetchCommand(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Command resource to fetch. | 

### Return type

[**WirelessV1Command**](WirelessV1Command.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCommand

> ListCommandResponse listCommand(opts)



Retrieve a list of Commands from your account.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1CommandApi();
let opts = {
  'sim': "sim_example", // String | The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
  'status': "status_example", // CommandEnumStatus | The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
  'direction': "direction_example", // CommandEnumDirection | Only return Commands with this direction value.
  'transport': "transport_example", // CommandEnumTransport | Only return Commands with this transport value. Can be: `sms` or `ip`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCommand(opts, (error, data, response) => {
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
 **sim** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read. | [optional] 
 **status** | **CommandEnumStatus**| The status of the resources to read. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;delivered&#x60;, &#x60;received&#x60;, or &#x60;failed&#x60;. | [optional] 
 **direction** | **CommandEnumDirection**| Only return Commands with this direction value. | [optional] 
 **transport** | **CommandEnumTransport**| Only return Commands with this transport value. Can be: &#x60;sms&#x60; or &#x60;ip&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCommandResponse**](ListCommandResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

