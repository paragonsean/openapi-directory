# TwilioNumbers.NumbersV2RegulationApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchRegulation**](NumbersV2RegulationApi.md#fetchRegulation) | **GET** /v2/RegulatoryCompliance/Regulations/{Sid} | 
[**listRegulation**](NumbersV2RegulationApi.md#listRegulation) | **GET** /v2/RegulatoryCompliance/Regulations | 



## fetchRegulation

> NumbersV2RegulatoryComplianceRegulation fetchRegulation(sid)



Fetch specific Regulation Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2RegulationApi();
let sid = "sid_example"; // String | The unique string that identifies the Regulation resource.
apiInstance.fetchRegulation(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that identifies the Regulation resource. | 

### Return type

[**NumbersV2RegulatoryComplianceRegulation**](NumbersV2RegulatoryComplianceRegulation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRegulation

> ListRegulationResponse listRegulation(opts)



Retrieve a list of all Regulations.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2RegulationApi();
let opts = {
  'endUserType': "endUserType_example", // RegulationEnumEndUserType | The type of End User the regulation requires - can be `individual` or `business`.
  'isoCountry': "isoCountry_example", // String | The ISO country code of the phone number's country.
  'numberType': "numberType_example", // String | The type of phone number that the regulatory requiremnt is restricting.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRegulation(opts, (error, data, response) => {
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
 **endUserType** | **RegulationEnumEndUserType**| The type of End User the regulation requires - can be &#x60;individual&#x60; or &#x60;business&#x60;. | [optional] 
 **isoCountry** | **String**| The ISO country code of the phone number&#39;s country. | [optional] 
 **numberType** | **String**| The type of phone number that the regulatory requiremnt is restricting. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRegulationResponse**](ListRegulationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

