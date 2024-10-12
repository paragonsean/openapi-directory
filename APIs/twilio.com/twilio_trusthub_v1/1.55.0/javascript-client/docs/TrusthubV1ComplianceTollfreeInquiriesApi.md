# TwilioTrusthub.TrusthubV1ComplianceTollfreeInquiriesApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createComplianceTollfreeInquiry**](TrusthubV1ComplianceTollfreeInquiriesApi.md#createComplianceTollfreeInquiry) | **POST** /v1/ComplianceInquiries/Tollfree/Initialize | 



## createComplianceTollfreeInquiry

> TrusthubV1ComplianceTollfreeInquiry createComplianceTollfreeInquiry(notificationEmail, tollfreePhoneNumber, opts)



Create a new Compliance Tollfree Verification Inquiry for the authenticated account. This is necessary to start a new embedded session.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1ComplianceTollfreeInquiriesApi();
let notificationEmail = "notificationEmail_example"; // String | The email address to receive the notification about the verification result.
let tollfreePhoneNumber = "tollfreePhoneNumber_example"; // String | The Tollfree phone number to be verified
let opts = {
  'additionalInformation': "additionalInformation_example", // String | Additional information to be provided for verification.
  'businessCity': "businessCity_example", // String | The city of the business or organization using the Tollfree number.
  'businessContactEmail': "businessContactEmail_example", // String | The email address of the contact for the business or organization using the Tollfree number.
  'businessContactFirstName': "businessContactFirstName_example", // String | The first name of the contact for the business or organization using the Tollfree number.
  'businessContactLastName': "businessContactLastName_example", // String | The last name of the contact for the business or organization using the Tollfree number.
  'businessContactPhone': "businessContactPhone_example", // String | The phone number of the contact for the business or organization using the Tollfree number.
  'businessCountry': "businessCountry_example", // String | The country of the business or organization using the Tollfree number.
  'businessName': "businessName_example", // String | The name of the business or organization using the Tollfree number.
  'businessPostalCode': "businessPostalCode_example", // String | The postal code of the business or organization using the Tollfree number.
  'businessStateProvinceRegion': "businessStateProvinceRegion_example", // String | The state/province/region of the business or organization using the Tollfree number.
  'businessStreetAddress': "businessStreetAddress_example", // String | The address of the business or organization using the Tollfree number.
  'businessStreetAddress2': "businessStreetAddress2_example", // String | The address of the business or organization using the Tollfree number.
  'businessWebsite': "businessWebsite_example", // String | The website of the business or organization using the Tollfree number.
  'messageVolume': "messageVolume_example", // String | Estimate monthly volume of messages from the Tollfree Number.
  'optInImageUrls': ["null"], // [String] | Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
  'optInType': "optInType_example", // ComplianceTollfreeInquiryEnumOptInType | 
  'productionMessageSample': "productionMessageSample_example", // String | An example of message content, i.e. a sample message.
  'useCaseCategories': ["null"], // [String] | The category of the use case for the Tollfree Number. List as many are applicable..
  'useCaseSummary': "useCaseSummary_example" // String | Use this to further explain how messaging is used by the business or organization.
};
apiInstance.createComplianceTollfreeInquiry(notificationEmail, tollfreePhoneNumber, opts, (error, data, response) => {
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
 **notificationEmail** | **String**| The email address to receive the notification about the verification result. | 
 **tollfreePhoneNumber** | **String**| The Tollfree phone number to be verified | 
 **additionalInformation** | **String**| Additional information to be provided for verification. | [optional] 
 **businessCity** | **String**| The city of the business or organization using the Tollfree number. | [optional] 
 **businessContactEmail** | **String**| The email address of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactFirstName** | **String**| The first name of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactLastName** | **String**| The last name of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactPhone** | **String**| The phone number of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessCountry** | **String**| The country of the business or organization using the Tollfree number. | [optional] 
 **businessName** | **String**| The name of the business or organization using the Tollfree number. | [optional] 
 **businessPostalCode** | **String**| The postal code of the business or organization using the Tollfree number. | [optional] 
 **businessStateProvinceRegion** | **String**| The state/province/region of the business or organization using the Tollfree number. | [optional] 
 **businessStreetAddress** | **String**| The address of the business or organization using the Tollfree number. | [optional] 
 **businessStreetAddress2** | **String**| The address of the business or organization using the Tollfree number. | [optional] 
 **businessWebsite** | **String**| The website of the business or organization using the Tollfree number. | [optional] 
 **messageVolume** | **String**| Estimate monthly volume of messages from the Tollfree Number. | [optional] 
 **optInImageUrls** | [**[String]**](String.md)| Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL. | [optional] 
 **optInType** | **ComplianceTollfreeInquiryEnumOptInType**|  | [optional] 
 **productionMessageSample** | **String**| An example of message content, i.e. a sample message. | [optional] 
 **useCaseCategories** | [**[String]**](String.md)| The category of the use case for the Tollfree Number. List as many are applicable.. | [optional] 
 **useCaseSummary** | **String**| Use this to further explain how messaging is used by the business or organization. | [optional] 

### Return type

[**TrusthubV1ComplianceTollfreeInquiry**](TrusthubV1ComplianceTollfreeInquiry.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

