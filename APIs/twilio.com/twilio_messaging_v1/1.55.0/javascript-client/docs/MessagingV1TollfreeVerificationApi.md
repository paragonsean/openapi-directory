# TwilioMessaging.MessagingV1TollfreeVerificationApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#createTollfreeVerification) | **POST** /v1/Tollfree/Verifications | 
[**deleteTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#deleteTollfreeVerification) | **DELETE** /v1/Tollfree/Verifications/{Sid} | 
[**fetchTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#fetchTollfreeVerification) | **GET** /v1/Tollfree/Verifications/{Sid} | 
[**listTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#listTollfreeVerification) | **GET** /v1/Tollfree/Verifications | 
[**updateTollfreeVerification**](MessagingV1TollfreeVerificationApi.md#updateTollfreeVerification) | **POST** /v1/Tollfree/Verifications/{Sid} | 



## createTollfreeVerification

> MessagingV1TollfreeVerification createTollfreeVerification(businessName, businessWebsite, messageVolume, notificationEmail, optInImageUrls, optInType, productionMessageSample, tollfreePhoneNumberSid, useCaseCategories, useCaseSummary, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1TollfreeVerificationApi();
let businessName = "businessName_example"; // String | The name of the business or organization using the Tollfree number.
let businessWebsite = "businessWebsite_example"; // String | The website of the business or organization using the Tollfree number.
let messageVolume = "messageVolume_example"; // String | Estimate monthly volume of messages from the Tollfree Number.
let notificationEmail = "notificationEmail_example"; // String | The email address to receive the notification about the verification result. .
let optInImageUrls = ["null"]; // [String] | Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
let optInType = "optInType_example"; // TollfreeVerificationEnumOptInType | 
let productionMessageSample = "productionMessageSample_example"; // String | An example of message content, i.e. a sample message.
let tollfreePhoneNumberSid = "tollfreePhoneNumberSid_example"; // String | The SID of the Phone Number associated with the Tollfree Verification.
let useCaseCategories = ["null"]; // [String] | The category of the use case for the Tollfree Number. List as many are applicable..
let useCaseSummary = "useCaseSummary_example"; // String | Use this to further explain how messaging is used by the business or organization.
let opts = {
  'additionalInformation': "additionalInformation_example", // String | Additional information to be provided for verification.
  'businessCity': "businessCity_example", // String | The city of the business or organization using the Tollfree number.
  'businessContactEmail': "businessContactEmail_example", // String | The email address of the contact for the business or organization using the Tollfree number.
  'businessContactFirstName': "businessContactFirstName_example", // String | The first name of the contact for the business or organization using the Tollfree number.
  'businessContactLastName': "businessContactLastName_example", // String | The last name of the contact for the business or organization using the Tollfree number.
  'businessContactPhone': "businessContactPhone_example", // String | The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.
  'businessCountry': "businessCountry_example", // String | The country of the business or organization using the Tollfree number.
  'businessPostalCode': "businessPostalCode_example", // String | The postal code of the business or organization using the Tollfree number.
  'businessStateProvinceRegion': "businessStateProvinceRegion_example", // String | The state/province/region of the business or organization using the Tollfree number.
  'businessStreetAddress': "businessStreetAddress_example", // String | The address of the business or organization using the Tollfree number.
  'businessStreetAddress2': "businessStreetAddress2_example", // String | The address of the business or organization using the Tollfree number.
  'customerProfileSid': "customerProfileSid_example", // String | Customer's Profile Bundle BundleSid.
  'externalReferenceId': "externalReferenceId_example" // String | An optional external reference ID supplied by customer and echoed back on status retrieval.
};
apiInstance.createTollfreeVerification(businessName, businessWebsite, messageVolume, notificationEmail, optInImageUrls, optInType, productionMessageSample, tollfreePhoneNumberSid, useCaseCategories, useCaseSummary, opts, (error, data, response) => {
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
 **businessName** | **String**| The name of the business or organization using the Tollfree number. | 
 **businessWebsite** | **String**| The website of the business or organization using the Tollfree number. | 
 **messageVolume** | **String**| Estimate monthly volume of messages from the Tollfree Number. | 
 **notificationEmail** | **String**| The email address to receive the notification about the verification result. . | 
 **optInImageUrls** | [**[String]**](String.md)| Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL. | 
 **optInType** | **TollfreeVerificationEnumOptInType**|  | 
 **productionMessageSample** | **String**| An example of message content, i.e. a sample message. | 
 **tollfreePhoneNumberSid** | **String**| The SID of the Phone Number associated with the Tollfree Verification. | 
 **useCaseCategories** | [**[String]**](String.md)| The category of the use case for the Tollfree Number. List as many are applicable.. | 
 **useCaseSummary** | **String**| Use this to further explain how messaging is used by the business or organization. | 
 **additionalInformation** | **String**| Additional information to be provided for verification. | [optional] 
 **businessCity** | **String**| The city of the business or organization using the Tollfree number. | [optional] 
 **businessContactEmail** | **String**| The email address of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactFirstName** | **String**| The first name of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactLastName** | **String**| The last name of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactPhone** | **String**| The E.164 formatted phone number of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessCountry** | **String**| The country of the business or organization using the Tollfree number. | [optional] 
 **businessPostalCode** | **String**| The postal code of the business or organization using the Tollfree number. | [optional] 
 **businessStateProvinceRegion** | **String**| The state/province/region of the business or organization using the Tollfree number. | [optional] 
 **businessStreetAddress** | **String**| The address of the business or organization using the Tollfree number. | [optional] 
 **businessStreetAddress2** | **String**| The address of the business or organization using the Tollfree number. | [optional] 
 **customerProfileSid** | **String**| Customer&#39;s Profile Bundle BundleSid. | [optional] 
 **externalReferenceId** | **String**| An optional external reference ID supplied by customer and echoed back on status retrieval. | [optional] 

### Return type

[**MessagingV1TollfreeVerification**](MessagingV1TollfreeVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTollfreeVerification

> deleteTollfreeVerification(sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1TollfreeVerificationApi();
let sid = "sid_example"; // String | The unique string to identify Tollfree Verification.
apiInstance.deleteTollfreeVerification(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string to identify Tollfree Verification. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTollfreeVerification

> MessagingV1TollfreeVerification fetchTollfreeVerification(sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1TollfreeVerificationApi();
let sid = "sid_example"; // String | The unique string to identify Tollfree Verification.
apiInstance.fetchTollfreeVerification(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string to identify Tollfree Verification. | 

### Return type

[**MessagingV1TollfreeVerification**](MessagingV1TollfreeVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTollfreeVerification

> ListTollfreeVerificationResponse listTollfreeVerification(opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1TollfreeVerificationApi();
let opts = {
  'tollfreePhoneNumberSid': "tollfreePhoneNumberSid_example", // String | The SID of the Phone Number associated with the Tollfree Verification.
  'status': "status_example", // TollfreeVerificationEnumStatus | The compliance status of the Tollfree Verification record.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTollfreeVerification(opts, (error, data, response) => {
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
 **tollfreePhoneNumberSid** | **String**| The SID of the Phone Number associated with the Tollfree Verification. | [optional] 
 **status** | **TollfreeVerificationEnumStatus**| The compliance status of the Tollfree Verification record. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTollfreeVerificationResponse**](ListTollfreeVerificationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTollfreeVerification

> MessagingV1TollfreeVerification updateTollfreeVerification(sid, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1TollfreeVerificationApi();
let sid = "sid_example"; // String | The unique string to identify Tollfree Verification.
let opts = {
  'additionalInformation': "additionalInformation_example", // String | Additional information to be provided for verification.
  'businessCity': "businessCity_example", // String | The city of the business or organization using the Tollfree number.
  'businessContactEmail': "businessContactEmail_example", // String | The email address of the contact for the business or organization using the Tollfree number.
  'businessContactFirstName': "businessContactFirstName_example", // String | The first name of the contact for the business or organization using the Tollfree number.
  'businessContactLastName': "businessContactLastName_example", // String | The last name of the contact for the business or organization using the Tollfree number.
  'businessContactPhone': "businessContactPhone_example", // String | The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.
  'businessCountry': "businessCountry_example", // String | The country of the business or organization using the Tollfree number.
  'businessName': "businessName_example", // String | The name of the business or organization using the Tollfree number.
  'businessPostalCode': "businessPostalCode_example", // String | The postal code of the business or organization using the Tollfree number.
  'businessStateProvinceRegion': "businessStateProvinceRegion_example", // String | The state/province/region of the business or organization using the Tollfree number.
  'businessStreetAddress': "businessStreetAddress_example", // String | The address of the business or organization using the Tollfree number.
  'businessStreetAddress2': "businessStreetAddress2_example", // String | The address of the business or organization using the Tollfree number.
  'businessWebsite': "businessWebsite_example", // String | The website of the business or organization using the Tollfree number.
  'editReason': "editReason_example", // String | Describe why the verification is being edited. If the verification was rejected because of a technical issue, such as the website being down, and the issue has been resolved this parameter should be set to something similar to 'Website fixed'.
  'messageVolume': "messageVolume_example", // String | Estimate monthly volume of messages from the Tollfree Number.
  'notificationEmail': "notificationEmail_example", // String | The email address to receive the notification about the verification result. .
  'optInImageUrls': ["null"], // [String] | Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
  'optInType': "optInType_example", // TollfreeVerificationEnumOptInType | 
  'productionMessageSample': "productionMessageSample_example", // String | An example of message content, i.e. a sample message.
  'useCaseCategories': ["null"], // [String] | The category of the use case for the Tollfree Number. List as many are applicable..
  'useCaseSummary': "useCaseSummary_example" // String | Use this to further explain how messaging is used by the business or organization.
};
apiInstance.updateTollfreeVerification(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string to identify Tollfree Verification. | 
 **additionalInformation** | **String**| Additional information to be provided for verification. | [optional] 
 **businessCity** | **String**| The city of the business or organization using the Tollfree number. | [optional] 
 **businessContactEmail** | **String**| The email address of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactFirstName** | **String**| The first name of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactLastName** | **String**| The last name of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessContactPhone** | **String**| The E.164 formatted phone number of the contact for the business or organization using the Tollfree number. | [optional] 
 **businessCountry** | **String**| The country of the business or organization using the Tollfree number. | [optional] 
 **businessName** | **String**| The name of the business or organization using the Tollfree number. | [optional] 
 **businessPostalCode** | **String**| The postal code of the business or organization using the Tollfree number. | [optional] 
 **businessStateProvinceRegion** | **String**| The state/province/region of the business or organization using the Tollfree number. | [optional] 
 **businessStreetAddress** | **String**| The address of the business or organization using the Tollfree number. | [optional] 
 **businessStreetAddress2** | **String**| The address of the business or organization using the Tollfree number. | [optional] 
 **businessWebsite** | **String**| The website of the business or organization using the Tollfree number. | [optional] 
 **editReason** | **String**| Describe why the verification is being edited. If the verification was rejected because of a technical issue, such as the website being down, and the issue has been resolved this parameter should be set to something similar to &#39;Website fixed&#39;. | [optional] 
 **messageVolume** | **String**| Estimate monthly volume of messages from the Tollfree Number. | [optional] 
 **notificationEmail** | **String**| The email address to receive the notification about the verification result. . | [optional] 
 **optInImageUrls** | [**[String]**](String.md)| Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL. | [optional] 
 **optInType** | **TollfreeVerificationEnumOptInType**|  | [optional] 
 **productionMessageSample** | **String**| An example of message content, i.e. a sample message. | [optional] 
 **useCaseCategories** | [**[String]**](String.md)| The category of the use case for the Tollfree Number. List as many are applicable.. | [optional] 
 **useCaseSummary** | **String**| Use this to further explain how messaging is used by the business or organization. | [optional] 

### Return type

[**MessagingV1TollfreeVerification**](MessagingV1TollfreeVerification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

