# TwilioRoutes.RoutesV2TrunkApi

All URIs are relative to *https://routes.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTrunks**](RoutesV2TrunkApi.md#fetchTrunks) | **GET** /v2/Trunks/{SipTrunkDomain} | 
[**updateTrunks**](RoutesV2TrunkApi.md#updateTrunks) | **POST** /v2/Trunks/{SipTrunkDomain} | 



## fetchTrunks

> RoutesV2Trunks fetchTrunks(sipTrunkDomain)



Fetch the Inbound Processing Region assigned to a SIP Trunk.

### Example

```javascript
import TwilioRoutes from 'twilio_routes';
let defaultClient = TwilioRoutes.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioRoutes.RoutesV2TrunkApi();
let sipTrunkDomain = "sipTrunkDomain_example"; // String | The absolute URL of the SIP Trunk
apiInstance.fetchTrunks(sipTrunkDomain, (error, data, response) => {
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
 **sipTrunkDomain** | **String**| The absolute URL of the SIP Trunk | 

### Return type

[**RoutesV2Trunks**](RoutesV2Trunks.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTrunks

> RoutesV2Trunks updateTrunks(sipTrunkDomain, opts)



Assign an Inbound Processing Region to a SIP Trunk

### Example

```javascript
import TwilioRoutes from 'twilio_routes';
let defaultClient = TwilioRoutes.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioRoutes.RoutesV2TrunkApi();
let sipTrunkDomain = "sipTrunkDomain_example"; // String | The absolute URL of the SIP Trunk
let opts = {
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 64 characters.
  'voiceRegion': "voiceRegion_example" // String | The Inbound Processing Region used for this SIP Trunk for voice
};
apiInstance.updateTrunks(sipTrunkDomain, opts, (error, data, response) => {
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
 **sipTrunkDomain** | **String**| The absolute URL of the SIP Trunk | 
 **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] 
 **voiceRegion** | **String**| The Inbound Processing Region used for this SIP Trunk for voice | [optional] 

### Return type

[**RoutesV2Trunks**](RoutesV2Trunks.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

