# TwilioTrunking.TrunkingV1TrunkApi

All URIs are relative to *https://trunking.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTrunk**](TrunkingV1TrunkApi.md#createTrunk) | **POST** /v1/Trunks | 
[**deleteTrunk**](TrunkingV1TrunkApi.md#deleteTrunk) | **DELETE** /v1/Trunks/{Sid} | 
[**fetchTrunk**](TrunkingV1TrunkApi.md#fetchTrunk) | **GET** /v1/Trunks/{Sid} | 
[**listTrunk**](TrunkingV1TrunkApi.md#listTrunk) | **GET** /v1/Trunks | 
[**updateTrunk**](TrunkingV1TrunkApi.md#updateTrunk) | **POST** /v1/Trunks/{Sid} | 



## createTrunk

> TrunkingV1Trunk createTrunk(opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1TrunkApi();
let opts = {
  'cnamLookupEnabled': true, // Boolean | Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
  'disasterRecoveryMethod': "disasterRecoveryMethod_example", // String | The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
  'disasterRecoveryUrl': "disasterRecoveryUrl_example", // String | The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
  'domainName': "domainName_example", // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'secure': true, // Boolean | Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
  'transferCallerId': "transferCallerId_example", // TrunkEnumTransferCallerId | 
  'transferMode': "transferMode_example" // TrunkEnumTransferSetting | 
};
apiInstance.createTrunk(opts, (error, data, response) => {
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
 **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] 
 **disasterRecoveryMethod** | **String**| The HTTP method we should use to call the &#x60;disaster_recovery_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **disasterRecoveryUrl** | **String**| The URL we should call using the &#x60;disaster_recovery_method&#x60; if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information. | [optional] 
 **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and &#x60;-&#x60; and must end with &#x60;pstn.twilio.com&#x60;. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **secure** | **Boolean**| Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information. | [optional] 
 **transferCallerId** | **TrunkEnumTransferCallerId**|  | [optional] 
 **transferMode** | **TrunkEnumTransferSetting**|  | [optional] 

### Return type

[**TrunkingV1Trunk**](TrunkingV1Trunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTrunk

> deleteTrunk(sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1TrunkApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Trunk resource to delete.
apiInstance.deleteTrunk(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Trunk resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTrunk

> TrunkingV1Trunk fetchTrunk(sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1TrunkApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Trunk resource to fetch.
apiInstance.fetchTrunk(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Trunk resource to fetch. | 

### Return type

[**TrunkingV1Trunk**](TrunkingV1Trunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTrunk

> ListTrunkResponse listTrunk(opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1TrunkApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTrunk(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTrunkResponse**](ListTrunkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTrunk

> TrunkingV1Trunk updateTrunk(sid, opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1TrunkApi();
let sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to update.
let opts = {
  'cnamLookupEnabled': true, // Boolean | Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
  'disasterRecoveryMethod': "disasterRecoveryMethod_example", // String | The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
  'disasterRecoveryUrl': "disasterRecoveryUrl_example", // String | The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
  'domainName': "domainName_example", // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'secure': true, // Boolean | Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
  'transferCallerId': "transferCallerId_example", // TrunkEnumTransferCallerId | 
  'transferMode': "transferMode_example" // TrunkEnumTransferSetting | 
};
apiInstance.updateTrunk(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to update. | 
 **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] 
 **disasterRecoveryMethod** | **String**| The HTTP method we should use to call the &#x60;disaster_recovery_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **disasterRecoveryUrl** | **String**| The URL we should call using the &#x60;disaster_recovery_method&#x60; if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information. | [optional] 
 **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and &#x60;-&#x60; and must end with &#x60;pstn.twilio.com&#x60;. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **secure** | **Boolean**| Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information. | [optional] 
 **transferCallerId** | **TrunkEnumTransferCallerId**|  | [optional] 
 **transferMode** | **TrunkEnumTransferSetting**|  | [optional] 

### Return type

[**TrunkingV1Trunk**](TrunkingV1Trunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

