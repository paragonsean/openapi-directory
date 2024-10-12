# TwilioNumbers.NumbersV2SupportingDocumentTypeApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchSupportingDocumentType**](NumbersV2SupportingDocumentTypeApi.md#fetchSupportingDocumentType) | **GET** /v2/RegulatoryCompliance/SupportingDocumentTypes/{Sid} | 
[**listSupportingDocumentType**](NumbersV2SupportingDocumentTypeApi.md#listSupportingDocumentType) | **GET** /v2/RegulatoryCompliance/SupportingDocumentTypes | 



## fetchSupportingDocumentType

> NumbersV2RegulatoryComplianceSupportingDocumentType fetchSupportingDocumentType(sid)



Fetch a specific Supporting Document Type Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2SupportingDocumentTypeApi();
let sid = "sid_example"; // String | The unique string that identifies the Supporting Document Type resource.
apiInstance.fetchSupportingDocumentType(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that identifies the Supporting Document Type resource. | 

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocumentType**](NumbersV2RegulatoryComplianceSupportingDocumentType.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSupportingDocumentType

> ListSupportingDocumentTypeResponse listSupportingDocumentType(opts)



Retrieve a list of all Supporting Document Types.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2SupportingDocumentTypeApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSupportingDocumentType(opts, (error, data, response) => {
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

[**ListSupportingDocumentTypeResponse**](ListSupportingDocumentTypeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

