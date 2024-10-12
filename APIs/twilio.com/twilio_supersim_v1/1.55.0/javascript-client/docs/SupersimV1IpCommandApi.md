# TwilioSupersim.SupersimV1IpCommandApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIpCommand**](SupersimV1IpCommandApi.md#createIpCommand) | **POST** /v1/IpCommands | 
[**fetchIpCommand**](SupersimV1IpCommandApi.md#fetchIpCommand) | **GET** /v1/IpCommands/{Sid} | 
[**listIpCommand**](SupersimV1IpCommandApi.md#listIpCommand) | **GET** /v1/IpCommands | 



## createIpCommand

> SupersimV1IpCommand createIpCommand(devicePort, payload, sim, opts)



Send an IP Command to a Super SIM.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1IpCommandApi();
let devicePort = 56; // Number | The device port to which the IP Command will be sent.
let payload = "payload_example"; // String | The data that will be sent to the device. The payload cannot exceed 1300 bytes. If the PayloadType is set to text, the payload is encoded in UTF-8. If PayloadType is set to binary, the payload is encoded in Base64.
let sim = "sim_example"; // String | The `sid` or `unique_name` of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the IP Command to.
let opts = {
  'callbackMethod': "callbackMethod_example", // String | The HTTP method we should use to call `callback_url`. Can be `GET` or `POST`, and the default is `POST`.
  'callbackUrl': "callbackUrl_example", // String | The URL we should call using the `callback_method` after we have sent the IP Command.
  'payloadType': "payloadType_example" // IpCommandEnumPayloadType | 
};
apiInstance.createIpCommand(devicePort, payload, sim, opts, (error, data, response) => {
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
 **devicePort** | **Number**| The device port to which the IP Command will be sent. | 
 **payload** | **String**| The data that will be sent to the device. The payload cannot exceed 1300 bytes. If the PayloadType is set to text, the payload is encoded in UTF-8. If PayloadType is set to binary, the payload is encoded in Base64. | 
 **sim** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the IP Command to. | 
 **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60;, and the default is &#x60;POST&#x60;. | [optional] 
 **callbackUrl** | **String**| The URL we should call using the &#x60;callback_method&#x60; after we have sent the IP Command. | [optional] 
 **payloadType** | **IpCommandEnumPayloadType**|  | [optional] 

### Return type

[**SupersimV1IpCommand**](SupersimV1IpCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchIpCommand

> SupersimV1IpCommand fetchIpCommand(sid)



Fetch IP Command instance from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1IpCommandApi();
let sid = "sid_example"; // String | The SID of the IP Command resource to fetch.
apiInstance.fetchIpCommand(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the IP Command resource to fetch. | 

### Return type

[**SupersimV1IpCommand**](SupersimV1IpCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIpCommand

> ListIpCommandResponse listIpCommand(opts)



Retrieve a list of IP Commands from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1IpCommandApi();
let opts = {
  'sim': "sim_example", // String | The SID or unique name of the Sim resource that IP Command was sent to or from.
  'simIccid': "simIccid_example", // String | The ICCID of the Sim resource that IP Command was sent to or from.
  'status': "status_example", // IpCommandEnumStatus | The status of the IP Command. Can be: `queued`, `sent`, `received` or `failed`. See the [IP Command Status Values](https://www.twilio.com/docs/iot/supersim/api/ipcommand-resource#status-values) for a description of each.
  'direction': "direction_example", // IpCommandEnumDirection | The direction of the IP Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listIpCommand(opts, (error, data, response) => {
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
 **sim** | **String**| The SID or unique name of the Sim resource that IP Command was sent to or from. | [optional] 
 **simIccid** | **String**| The ICCID of the Sim resource that IP Command was sent to or from. | [optional] 
 **status** | **IpCommandEnumStatus**| The status of the IP Command. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;received&#x60; or &#x60;failed&#x60;. See the [IP Command Status Values](https://www.twilio.com/docs/iot/supersim/api/ipcommand-resource#status-values) for a description of each. | [optional] 
 **direction** | **IpCommandEnumDirection**| The direction of the IP Command. Can be &#x60;to_sim&#x60; or &#x60;from_sim&#x60;. The value of &#x60;to_sim&#x60; is synonymous with the term &#x60;mobile terminated&#x60;, and &#x60;from_sim&#x60; is synonymous with the term &#x60;mobile originated&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListIpCommandResponse**](ListIpCommandResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

