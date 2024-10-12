# TwilioNumbers.NumbersV2EndUserTypeApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchEndUserType**](NumbersV2EndUserTypeApi.md#fetchEndUserType) | **GET** /v2/RegulatoryCompliance/EndUserTypes/{Sid} | 
[**listEndUserType**](NumbersV2EndUserTypeApi.md#listEndUserType) | **GET** /v2/RegulatoryCompliance/EndUserTypes | 



## fetchEndUserType

> NumbersV2RegulatoryComplianceEndUserType fetchEndUserType(sid)



Fetch a specific End-User Type Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EndUserTypeApi();
let sid = "sid_example"; // String | The unique string that identifies the End-User Type resource.
apiInstance.fetchEndUserType(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that identifies the End-User Type resource. | 

### Return type

[**NumbersV2RegulatoryComplianceEndUserType**](NumbersV2RegulatoryComplianceEndUserType.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEndUserType

> ListEndUserTypeResponse listEndUserType(opts)



Retrieve a list of all End-User Types.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2EndUserTypeApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEndUserType(opts, (error, data, response) => {
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

[**ListEndUserTypeResponse**](ListEndUserTypeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

