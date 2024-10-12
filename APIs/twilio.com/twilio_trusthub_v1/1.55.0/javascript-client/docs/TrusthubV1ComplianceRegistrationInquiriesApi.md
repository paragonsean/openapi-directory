# TwilioTrusthub.TrusthubV1ComplianceRegistrationInquiriesApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createComplianceRegistration**](TrusthubV1ComplianceRegistrationInquiriesApi.md#createComplianceRegistration) | **POST** /v1/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize | 



## createComplianceRegistration

> TrusthubV1ComplianceRegistration createComplianceRegistration(endUserType, phoneNumberType, opts)



Create a new Compliance Registration Inquiry for the authenticated account. This is necessary to start a new embedded session.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1ComplianceRegistrationInquiriesApi();
let endUserType = "endUserType_example"; // ComplianceRegistrationEnumEndUserType | 
let phoneNumberType = "phoneNumberType_example"; // ComplianceRegistrationEnumPhoneNumberType | 
let opts = {
  'acceptedNotificationReceipt': true, // Boolean | The email address to receive the notification about the verification result.
  'addressCity': "addressCity_example", // String | City of the business
  'addressCountryCode': "addressCountryCode_example", // String | Country code of the business
  'addressPostalCode': "addressPostalCode_example", // String | Postal code of the business
  'addressStreet': "addressStreet_example", // String | Street address of the business
  'addressStreetSecondary': "addressStreetSecondary_example", // String | Street address of the business
  'addressSubdivision': "addressSubdivision_example", // String | State or province of the business
  'authorizedRepresentative1DateOfBirth': "authorizedRepresentative1DateOfBirth_example", // String | Birthdate of the authorized representative
  'authorizedRepresentative1Email': "authorizedRepresentative1Email_example", // String | Email address of the authorized representative
  'authorizedRepresentative1FirstName': "authorizedRepresentative1FirstName_example", // String | First name of the authorized representative
  'authorizedRepresentative1LastName': "authorizedRepresentative1LastName_example", // String | Last name of the authorized representative
  'authorizedRepresentative1Phone': "authorizedRepresentative1Phone_example", // String | Phone number of the authorized representative
  'businessIdentityType': "businessIdentityType_example", // ComplianceRegistrationEnumBusinessIdentityType | 
  'businessLegalName': "businessLegalName_example", // String | he name of the business or organization using the Tollfree number.
  'businessRegistrationAuthority': "businessRegistrationAuthority_example", // ComplianceRegistrationEnumBusinessRegistrationAuthority | 
  'businessRegistrationNumber': "businessRegistrationNumber_example", // String | Business registration number of the business
  'businessWebsiteUrl': "businessWebsiteUrl_example", // String | The URL of the business website
  'dateOfBirth': "dateOfBirth_example", // String | The date of birth of the Individual User.
  'emergencyAddressCity': "emergencyAddressCity_example", // String | City of the business
  'emergencyAddressCountryCode': "emergencyAddressCountryCode_example", // String | Country code of the business
  'emergencyAddressPostalCode': "emergencyAddressPostalCode_example", // String | Postal code of the business
  'emergencyAddressStreet': "emergencyAddressStreet_example", // String | Street address of the business
  'emergencyAddressStreetSecondary': "emergencyAddressStreetSecondary_example", // String | Street address of the business
  'emergencyAddressSubdivision': "emergencyAddressSubdivision_example", // String | State or province of the business
  'file': "file_example", // String | The verification document to upload
  'fileName': "fileName_example", // String | The name of the verification document to upload
  'firstName': "firstName_example", // String | The first name of the Individual User.
  'friendlyName': "friendlyName_example", // String | Friendly name for your business information
  'individualEmail': "individualEmail_example", // String | The email address of the Individual User.
  'individualPhone': "individualPhone_example", // String | The phone number of the Individual User.
  'isIsvEmbed': true, // Boolean | Indicates if the inquiry is being started from an ISV embedded component.
  'lastName': "lastName_example", // String | The last name of the Individual User.
  'notificationEmail': "notificationEmail_example", // String | he email address to receive the notification about the verification result.
  'useAddressAsEmergencyAddress': true // Boolean | Use the business address as the emergency address
};
apiInstance.createComplianceRegistration(endUserType, phoneNumberType, opts, (error, data, response) => {
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
 **endUserType** | **ComplianceRegistrationEnumEndUserType**|  | 
 **phoneNumberType** | **ComplianceRegistrationEnumPhoneNumberType**|  | 
 **acceptedNotificationReceipt** | **Boolean**| The email address to receive the notification about the verification result. | [optional] 
 **addressCity** | **String**| City of the business | [optional] 
 **addressCountryCode** | **String**| Country code of the business | [optional] 
 **addressPostalCode** | **String**| Postal code of the business | [optional] 
 **addressStreet** | **String**| Street address of the business | [optional] 
 **addressStreetSecondary** | **String**| Street address of the business | [optional] 
 **addressSubdivision** | **String**| State or province of the business | [optional] 
 **authorizedRepresentative1DateOfBirth** | **String**| Birthdate of the authorized representative | [optional] 
 **authorizedRepresentative1Email** | **String**| Email address of the authorized representative | [optional] 
 **authorizedRepresentative1FirstName** | **String**| First name of the authorized representative | [optional] 
 **authorizedRepresentative1LastName** | **String**| Last name of the authorized representative | [optional] 
 **authorizedRepresentative1Phone** | **String**| Phone number of the authorized representative | [optional] 
 **businessIdentityType** | **ComplianceRegistrationEnumBusinessIdentityType**|  | [optional] 
 **businessLegalName** | **String**| he name of the business or organization using the Tollfree number. | [optional] 
 **businessRegistrationAuthority** | **ComplianceRegistrationEnumBusinessRegistrationAuthority**|  | [optional] 
 **businessRegistrationNumber** | **String**| Business registration number of the business | [optional] 
 **businessWebsiteUrl** | **String**| The URL of the business website | [optional] 
 **dateOfBirth** | **String**| The date of birth of the Individual User. | [optional] 
 **emergencyAddressCity** | **String**| City of the business | [optional] 
 **emergencyAddressCountryCode** | **String**| Country code of the business | [optional] 
 **emergencyAddressPostalCode** | **String**| Postal code of the business | [optional] 
 **emergencyAddressStreet** | **String**| Street address of the business | [optional] 
 **emergencyAddressStreetSecondary** | **String**| Street address of the business | [optional] 
 **emergencyAddressSubdivision** | **String**| State or province of the business | [optional] 
 **file** | **String**| The verification document to upload | [optional] 
 **fileName** | **String**| The name of the verification document to upload | [optional] 
 **firstName** | **String**| The first name of the Individual User. | [optional] 
 **friendlyName** | **String**| Friendly name for your business information | [optional] 
 **individualEmail** | **String**| The email address of the Individual User. | [optional] 
 **individualPhone** | **String**| The phone number of the Individual User. | [optional] 
 **isIsvEmbed** | **Boolean**| Indicates if the inquiry is being started from an ISV embedded component. | [optional] 
 **lastName** | **String**| The last name of the Individual User. | [optional] 
 **notificationEmail** | **String**| he email address to receive the notification about the verification result. | [optional] 
 **useAddressAsEmergencyAddress** | **Boolean**| Use the business address as the emergency address | [optional] 

### Return type

[**TrusthubV1ComplianceRegistration**](TrusthubV1ComplianceRegistration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

