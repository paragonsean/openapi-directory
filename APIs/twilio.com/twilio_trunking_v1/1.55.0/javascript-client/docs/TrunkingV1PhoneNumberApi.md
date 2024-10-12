# TwilioTrunking.TrunkingV1PhoneNumberApi

All URIs are relative to *https://trunking.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPhoneNumber**](TrunkingV1PhoneNumberApi.md#createPhoneNumber) | **POST** /v1/Trunks/{TrunkSid}/PhoneNumbers | 
[**deletePhoneNumber**](TrunkingV1PhoneNumberApi.md#deletePhoneNumber) | **DELETE** /v1/Trunks/{TrunkSid}/PhoneNumbers/{Sid} | 
[**fetchPhoneNumber**](TrunkingV1PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v1/Trunks/{TrunkSid}/PhoneNumbers/{Sid} | 
[**listPhoneNumber**](TrunkingV1PhoneNumberApi.md#listPhoneNumber) | **GET** /v1/Trunks/{TrunkSid}/PhoneNumbers | 



## createPhoneNumber

> TrunkingV1TrunkPhoneNumber createPhoneNumber(trunkSid, phoneNumberSid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1PhoneNumberApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the phone number with.
let phoneNumberSid = "phoneNumberSid_example"; // String | The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk.
apiInstance.createPhoneNumber(trunkSid, phoneNumberSid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk to associate the phone number with. | 
 **phoneNumberSid** | **String**| The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk. | 

### Return type

[**TrunkingV1TrunkPhoneNumber**](TrunkingV1TrunkPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deletePhoneNumber

> deletePhoneNumber(trunkSid, sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1PhoneNumberApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the PhoneNumber resource.
let sid = "sid_example"; // String | The unique string that we created to identify the PhoneNumber resource to delete.
apiInstance.deletePhoneNumber(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to delete the PhoneNumber resource. | 
 **sid** | **String**| The unique string that we created to identify the PhoneNumber resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchPhoneNumber

> TrunkingV1TrunkPhoneNumber fetchPhoneNumber(trunkSid, sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1PhoneNumberApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the PhoneNumber resource.
let sid = "sid_example"; // String | The unique string that we created to identify the PhoneNumber resource to fetch.
apiInstance.fetchPhoneNumber(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to fetch the PhoneNumber resource. | 
 **sid** | **String**| The unique string that we created to identify the PhoneNumber resource to fetch. | 

### Return type

[**TrunkingV1TrunkPhoneNumber**](TrunkingV1TrunkPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPhoneNumber

> ListPhoneNumberResponse listPhoneNumber(trunkSid, opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1PhoneNumberApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the PhoneNumber resources.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listPhoneNumber(trunkSid, opts, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to read the PhoneNumber resources. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListPhoneNumberResponse**](ListPhoneNumberResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

