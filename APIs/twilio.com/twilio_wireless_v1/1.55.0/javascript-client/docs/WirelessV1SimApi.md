# TwilioWireless.WirelessV1SimApi

All URIs are relative to *https://wireless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSim**](WirelessV1SimApi.md#deleteSim) | **DELETE** /v1/Sims/{Sid} | 
[**fetchSim**](WirelessV1SimApi.md#fetchSim) | **GET** /v1/Sims/{Sid} | 
[**listSim**](WirelessV1SimApi.md#listSim) | **GET** /v1/Sims | 
[**updateSim**](WirelessV1SimApi.md#updateSim) | **POST** /v1/Sims/{Sid} | 



## deleteSim

> deleteSim(sid)



Delete a Sim resource on your Account.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1SimApi();
let sid = "sid_example"; // String | The SID or the `unique_name` of the Sim resource to delete.
apiInstance.deleteSim(sid, (error, data, response) => {
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
 **sid** | **String**| The SID or the &#x60;unique_name&#x60; of the Sim resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSim

> WirelessV1Sim fetchSim(sid)



Fetch a Sim resource on your Account.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1SimApi();
let sid = "sid_example"; // String | The SID or the `unique_name` of the Sim resource to fetch.
apiInstance.fetchSim(sid, (error, data, response) => {
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
 **sid** | **String**| The SID or the &#x60;unique_name&#x60; of the Sim resource to fetch. | 

### Return type

[**WirelessV1Sim**](WirelessV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSim

> ListSimResponse listSim(opts)



Retrieve a list of Sim resources on your Account.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1SimApi();
let opts = {
  'status': "status_example", // SimEnumStatus | Only return Sim resources with this status.
  'iccid': "iccid_example", // String | Only return Sim resources with this ICCID. This will return a list with a maximum size of 1.
  'ratePlan': "ratePlan_example", // String | The SID or unique name of a [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource). Only return Sim resources assigned to this RatePlan resource.
  'eId': "eId_example", // String | Deprecated.
  'simRegistrationCode': "simRegistrationCode_example", // String | Only return Sim resources with this registration code. This will return a list with a maximum size of 1.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSim(opts, (error, data, response) => {
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
 **status** | **SimEnumStatus**| Only return Sim resources with this status. | [optional] 
 **iccid** | **String**| Only return Sim resources with this ICCID. This will return a list with a maximum size of 1. | [optional] 
 **ratePlan** | **String**| The SID or unique name of a [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource). Only return Sim resources assigned to this RatePlan resource. | [optional] 
 **eId** | **String**| Deprecated. | [optional] 
 **simRegistrationCode** | **String**| Only return Sim resources with this registration code. This will return a list with a maximum size of 1. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSimResponse**](ListSimResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSim

> WirelessV1Sim updateSim(sid, opts)



Updates the given properties of a Sim resource on your Account.

### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1SimApi();
let sid = "sid_example"; // String | The SID or the `unique_name` of the Sim resource to update.
let opts = {
  'accountSid': "accountSid_example", // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a [Subaccount](https://www.twilio.com/docs/iam/api/subaccounts) of the requesting Account. Only valid when the Sim resource's status is `new`. For more information, see the [Move SIMs between Subaccounts documentation](https://www.twilio.com/docs/iot/wireless/api/sim-resource#move-sims-between-subaccounts).
  'callbackMethod': "callbackMethod_example", // String | The HTTP method we should use to call `callback_url`. Can be: `POST` or `GET`. The default is `POST`.
  'callbackUrl': "callbackUrl_example", // String | The URL we should call using the `callback_url` when the SIM has finished updating. When the SIM transitions from `new` to `ready` or from any status to `deactivated`, we call this URL when the status changes to an intermediate status (`ready` or `deactivated`) and again when the status changes to its final status (`active` or `canceled`).
  'commandsCallbackMethod': "commandsCallbackMethod_example", // String | The HTTP method we should use to call `commands_callback_url`. Can be: `POST` or `GET`. The default is `POST`.
  'commandsCallbackUrl': "commandsCallbackUrl_example", // String | The URL we should call using the `commands_callback_method` when the SIM sends a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). Your server should respond with an HTTP status code in the 200 range; any response body is ignored.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the Sim resource. It does not need to be unique.
  'ratePlan': "ratePlan_example", // String | The SID or unique name of the [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource) to which the Sim resource should be assigned.
  'resetStatus': "resetStatus_example", // SimEnumResetStatus | 
  'smsFallbackMethod': "smsFallbackMethod_example", // String | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`. Default is `POST`.
  'smsFallbackUrl': "smsFallbackUrl_example", // String | The URL we should call using the `sms_fallback_method` when an error occurs while retrieving or executing the TwiML requested from `sms_url`.
  'smsMethod': "smsMethod_example", // String | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`. Default is `POST`.
  'smsUrl': "smsUrl_example", // String | The URL we should call using the `sms_method` when the SIM-connected device sends an SMS message that is not a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource).
  'status': "status_example", // SimEnumStatus | 
  'uniqueName': "uniqueName_example", // String | An application-defined string that uniquely identifies the resource. It can be used in place of the `sid` in the URL path to address the resource.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | Deprecated.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | Deprecated.
  'voiceMethod': "voiceMethod_example", // String | Deprecated.
  'voiceUrl': "voiceUrl_example" // String | Deprecated.
};
apiInstance.updateSim(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID or the &#x60;unique_name&#x60; of the Sim resource to update. | 
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a [Subaccount](https://www.twilio.com/docs/iam/api/subaccounts) of the requesting Account. Only valid when the Sim resource&#39;s status is &#x60;new&#x60;. For more information, see the [Move SIMs between Subaccounts documentation](https://www.twilio.com/docs/iot/wireless/api/sim-resource#move-sims-between-subaccounts). | [optional] 
 **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;. The default is &#x60;POST&#x60;. | [optional] 
 **callbackUrl** | **String**| The URL we should call using the &#x60;callback_url&#x60; when the SIM has finished updating. When the SIM transitions from &#x60;new&#x60; to &#x60;ready&#x60; or from any status to &#x60;deactivated&#x60;, we call this URL when the status changes to an intermediate status (&#x60;ready&#x60; or &#x60;deactivated&#x60;) and again when the status changes to its final status (&#x60;active&#x60; or &#x60;canceled&#x60;). | [optional] 
 **commandsCallbackMethod** | **String**| The HTTP method we should use to call &#x60;commands_callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;. The default is &#x60;POST&#x60;. | [optional] 
 **commandsCallbackUrl** | **String**| The URL we should call using the &#x60;commands_callback_method&#x60; when the SIM sends a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). Your server should respond with an HTTP status code in the 200 range; any response body is ignored. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the Sim resource. It does not need to be unique. | [optional] 
 **ratePlan** | **String**| The SID or unique name of the [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource) to which the Sim resource should be assigned. | [optional] 
 **resetStatus** | **SimEnumResetStatus**|  | [optional] 
 **smsFallbackMethod** | **String**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. | [optional] 
 **smsFallbackUrl** | **String**| The URL we should call using the &#x60;sms_fallback_method&#x60; when an error occurs while retrieving or executing the TwiML requested from &#x60;sms_url&#x60;. | [optional] 
 **smsMethod** | **String**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. | [optional] 
 **smsUrl** | **String**| The URL we should call using the &#x60;sms_method&#x60; when the SIM-connected device sends an SMS message that is not a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). | [optional] 
 **status** | **SimEnumStatus**|  | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the &#x60;sid&#x60; in the URL path to address the resource. | [optional] 
 **voiceFallbackMethod** | **String**| Deprecated. | [optional] 
 **voiceFallbackUrl** | **String**| Deprecated. | [optional] 
 **voiceMethod** | **String**| Deprecated. | [optional] 
 **voiceUrl** | **String**| Deprecated. | [optional] 

### Return type

[**WirelessV1Sim**](WirelessV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

