# TwilioVoice.VoiceV1ConnectionPolicyTargetApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#createConnectionPolicyTarget) | **POST** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets | 
[**deleteConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#deleteConnectionPolicyTarget) | **DELETE** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid} | 
[**fetchConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#fetchConnectionPolicyTarget) | **GET** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid} | 
[**listConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#listConnectionPolicyTarget) | **GET** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets | 
[**updateConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#updateConnectionPolicyTarget) | **POST** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid} | 



## createConnectionPolicyTarget

> VoiceV1ConnectionPolicyConnectionPolicyTarget createConnectionPolicyTarget(connectionPolicySid, target, opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyTargetApi();
let connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
let target = "target_example"; // String | The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
let opts = {
  'enabled': true, // Boolean | Whether the Target is enabled. The default is `true`.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
  'priority': 56, // Number | The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
  'weight': 56 // Number | The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
};
apiInstance.createConnectionPolicyTarget(connectionPolicySid, target, opts, (error, data, response) => {
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
 **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | 
 **target** | **String**| The SIP address you want Twilio to route your calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported. | 
 **enabled** | **Boolean**| Whether the Target is enabled. The default is &#x60;true&#x60;. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 
 **priority** | **Number**| The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target. | [optional] 
 **weight** | **Number**| The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority. | [optional] 

### Return type

[**VoiceV1ConnectionPolicyConnectionPolicyTarget**](VoiceV1ConnectionPolicyConnectionPolicyTarget.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteConnectionPolicyTarget

> deleteConnectionPolicyTarget(connectionPolicySid, sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyTargetApi();
let connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
let sid = "sid_example"; // String | The unique string that we created to identify the Target resource to delete.
apiInstance.deleteConnectionPolicyTarget(connectionPolicySid, sid, (error, data, response) => {
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
 **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | 
 **sid** | **String**| The unique string that we created to identify the Target resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConnectionPolicyTarget

> VoiceV1ConnectionPolicyConnectionPolicyTarget fetchConnectionPolicyTarget(connectionPolicySid, sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyTargetApi();
let connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
let sid = "sid_example"; // String | The unique string that we created to identify the Target resource to fetch.
apiInstance.fetchConnectionPolicyTarget(connectionPolicySid, sid, (error, data, response) => {
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
 **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | 
 **sid** | **String**| The unique string that we created to identify the Target resource to fetch. | 

### Return type

[**VoiceV1ConnectionPolicyConnectionPolicyTarget**](VoiceV1ConnectionPolicyConnectionPolicyTarget.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConnectionPolicyTarget

> ListConnectionPolicyTargetResponse listConnectionPolicyTarget(connectionPolicySid, opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyTargetApi();
let connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy from which to read the Targets.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConnectionPolicyTarget(connectionPolicySid, opts, (error, data, response) => {
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
 **connectionPolicySid** | **String**| The SID of the Connection Policy from which to read the Targets. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConnectionPolicyTargetResponse**](ListConnectionPolicyTargetResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConnectionPolicyTarget

> VoiceV1ConnectionPolicyConnectionPolicyTarget updateConnectionPolicyTarget(connectionPolicySid, sid, opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyTargetApi();
let connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
let sid = "sid_example"; // String | The unique string that we created to identify the Target resource to update.
let opts = {
  'enabled': true, // Boolean | Whether the Target is enabled.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
  'priority': 56, // Number | The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
  'target': "target_example", // String | The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
  'weight': 56 // Number | The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
};
apiInstance.updateConnectionPolicyTarget(connectionPolicySid, sid, opts, (error, data, response) => {
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
 **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | 
 **sid** | **String**| The unique string that we created to identify the Target resource to update. | 
 **enabled** | **Boolean**| Whether the Target is enabled. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 
 **priority** | **Number**| The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target. | [optional] 
 **target** | **String**| The SIP address you want Twilio to route your calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported. | [optional] 
 **weight** | **Number**| The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority. | [optional] 

### Return type

[**VoiceV1ConnectionPolicyConnectionPolicyTarget**](VoiceV1ConnectionPolicyConnectionPolicyTarget.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

