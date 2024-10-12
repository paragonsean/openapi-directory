# TwilioTrusthub.TrusthubV1ComplianceInquiriesApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createComplianceInquiry**](TrusthubV1ComplianceInquiriesApi.md#createComplianceInquiry) | **POST** /v1/ComplianceInquiries/Customers/Initialize | 
[**updateComplianceInquiry**](TrusthubV1ComplianceInquiriesApi.md#updateComplianceInquiry) | **POST** /v1/ComplianceInquiries/Customers/{CustomerId}/Initialize | 



## createComplianceInquiry

> TrusthubV1ComplianceInquiry createComplianceInquiry(primaryProfileSid, opts)



Create a new Compliance Inquiry for the authenticated account. This is necessary to start a new embedded session.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1ComplianceInquiriesApi();
let primaryProfileSid = "primaryProfileSid_example"; // String | The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile.
let opts = {
  'notificationEmail': "notificationEmail_example" // String | The email address that approval status updates will be sent to. If not specified, the email address associated with your primary customer profile will be used.
};
apiInstance.createComplianceInquiry(primaryProfileSid, opts, (error, data, response) => {
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
 **primaryProfileSid** | **String**| The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile. | 
 **notificationEmail** | **String**| The email address that approval status updates will be sent to. If not specified, the email address associated with your primary customer profile will be used. | [optional] 

### Return type

[**TrusthubV1ComplianceInquiry**](TrusthubV1ComplianceInquiry.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateComplianceInquiry

> TrusthubV1ComplianceInquiry updateComplianceInquiry(customerId, primaryProfileSid)



Resume a specific Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry for editing.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1ComplianceInquiriesApi();
let customerId = "customerId_example"; // String | The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call.
let primaryProfileSid = "primaryProfileSid_example"; // String | The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile.
apiInstance.updateComplianceInquiry(customerId, primaryProfileSid, (error, data, response) => {
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
 **customerId** | **String**| The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call. | 
 **primaryProfileSid** | **String**| The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile. | 

### Return type

[**TrusthubV1ComplianceInquiry**](TrusthubV1ComplianceInquiry.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

