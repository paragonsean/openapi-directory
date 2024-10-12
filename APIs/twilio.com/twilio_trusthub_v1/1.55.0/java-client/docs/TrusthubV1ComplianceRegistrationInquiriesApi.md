# TrusthubV1ComplianceRegistrationInquiriesApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createComplianceRegistration**](TrusthubV1ComplianceRegistrationInquiriesApi.md#createComplianceRegistration) | **POST** /v1/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize |  |


<a id="createComplianceRegistration"></a>
# **createComplianceRegistration**
> TrusthubV1ComplianceRegistration createComplianceRegistration(endUserType, phoneNumberType, acceptedNotificationReceipt, addressCity, addressCountryCode, addressPostalCode, addressStreet, addressStreetSecondary, addressSubdivision, authorizedRepresentative1DateOfBirth, authorizedRepresentative1Email, authorizedRepresentative1FirstName, authorizedRepresentative1LastName, authorizedRepresentative1Phone, businessIdentityType, businessLegalName, businessRegistrationAuthority, businessRegistrationNumber, businessWebsiteUrl, dateOfBirth, emergencyAddressCity, emergencyAddressCountryCode, emergencyAddressPostalCode, emergencyAddressStreet, emergencyAddressStreetSecondary, emergencyAddressSubdivision, _file, fileName, firstName, friendlyName, individualEmail, individualPhone, isIsvEmbed, lastName, notificationEmail, useAddressAsEmergencyAddress)



Create a new Compliance Registration Inquiry for the authenticated account. This is necessary to start a new embedded session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1ComplianceRegistrationInquiriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1ComplianceRegistrationInquiriesApi apiInstance = new TrusthubV1ComplianceRegistrationInquiriesApi(defaultClient);
    ComplianceRegistrationEnumEndUserType endUserType = ComplianceRegistrationEnumEndUserType.fromValue("Individual"); // ComplianceRegistrationEnumEndUserType | 
    ComplianceRegistrationEnumPhoneNumberType phoneNumberType = ComplianceRegistrationEnumPhoneNumberType.fromValue("local"); // ComplianceRegistrationEnumPhoneNumberType | 
    Boolean acceptedNotificationReceipt = true; // Boolean | The email address to receive the notification about the verification result.
    String addressCity = "addressCity_example"; // String | City of the business
    String addressCountryCode = "addressCountryCode_example"; // String | Country code of the business
    String addressPostalCode = "addressPostalCode_example"; // String | Postal code of the business
    String addressStreet = "addressStreet_example"; // String | Street address of the business
    String addressStreetSecondary = "addressStreetSecondary_example"; // String | Street address of the business
    String addressSubdivision = "addressSubdivision_example"; // String | State or province of the business
    String authorizedRepresentative1DateOfBirth = "authorizedRepresentative1DateOfBirth_example"; // String | Birthdate of the authorized representative
    String authorizedRepresentative1Email = "authorizedRepresentative1Email_example"; // String | Email address of the authorized representative
    String authorizedRepresentative1FirstName = "authorizedRepresentative1FirstName_example"; // String | First name of the authorized representative
    String authorizedRepresentative1LastName = "authorizedRepresentative1LastName_example"; // String | Last name of the authorized representative
    String authorizedRepresentative1Phone = "authorizedRepresentative1Phone_example"; // String | Phone number of the authorized representative
    ComplianceRegistrationEnumBusinessIdentityType businessIdentityType = ComplianceRegistrationEnumBusinessIdentityType.fromValue("direct_customer"); // ComplianceRegistrationEnumBusinessIdentityType | 
    String businessLegalName = "businessLegalName_example"; // String | he name of the business or organization using the Tollfree number.
    ComplianceRegistrationEnumBusinessRegistrationAuthority businessRegistrationAuthority = ComplianceRegistrationEnumBusinessRegistrationAuthority.fromValue("UK:CRN"); // ComplianceRegistrationEnumBusinessRegistrationAuthority | 
    String businessRegistrationNumber = "businessRegistrationNumber_example"; // String | Business registration number of the business
    String businessWebsiteUrl = "businessWebsiteUrl_example"; // String | The URL of the business website
    String dateOfBirth = "dateOfBirth_example"; // String | The date of birth of the Individual User.
    String emergencyAddressCity = "emergencyAddressCity_example"; // String | City of the business
    String emergencyAddressCountryCode = "emergencyAddressCountryCode_example"; // String | Country code of the business
    String emergencyAddressPostalCode = "emergencyAddressPostalCode_example"; // String | Postal code of the business
    String emergencyAddressStreet = "emergencyAddressStreet_example"; // String | Street address of the business
    String emergencyAddressStreetSecondary = "emergencyAddressStreetSecondary_example"; // String | Street address of the business
    String emergencyAddressSubdivision = "emergencyAddressSubdivision_example"; // String | State or province of the business
    String _file = "_file_example"; // String | The verification document to upload
    String fileName = "fileName_example"; // String | The name of the verification document to upload
    String firstName = "firstName_example"; // String | The first name of the Individual User.
    String friendlyName = "friendlyName_example"; // String | Friendly name for your business information
    String individualEmail = "individualEmail_example"; // String | The email address of the Individual User.
    String individualPhone = "individualPhone_example"; // String | The phone number of the Individual User.
    Boolean isIsvEmbed = true; // Boolean | Indicates if the inquiry is being started from an ISV embedded component.
    String lastName = "lastName_example"; // String | The last name of the Individual User.
    String notificationEmail = "notificationEmail_example"; // String | he email address to receive the notification about the verification result.
    Boolean useAddressAsEmergencyAddress = true; // Boolean | Use the business address as the emergency address
    try {
      TrusthubV1ComplianceRegistration result = apiInstance.createComplianceRegistration(endUserType, phoneNumberType, acceptedNotificationReceipt, addressCity, addressCountryCode, addressPostalCode, addressStreet, addressStreetSecondary, addressSubdivision, authorizedRepresentative1DateOfBirth, authorizedRepresentative1Email, authorizedRepresentative1FirstName, authorizedRepresentative1LastName, authorizedRepresentative1Phone, businessIdentityType, businessLegalName, businessRegistrationAuthority, businessRegistrationNumber, businessWebsiteUrl, dateOfBirth, emergencyAddressCity, emergencyAddressCountryCode, emergencyAddressPostalCode, emergencyAddressStreet, emergencyAddressStreetSecondary, emergencyAddressSubdivision, _file, fileName, firstName, friendlyName, individualEmail, individualPhone, isIsvEmbed, lastName, notificationEmail, useAddressAsEmergencyAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1ComplianceRegistrationInquiriesApi#createComplianceRegistration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **endUserType** | **ComplianceRegistrationEnumEndUserType**|  | [enum: Individual, Business] |
| **phoneNumberType** | **ComplianceRegistrationEnumPhoneNumberType**|  | [enum: local, national, mobile, toll-free] |
| **acceptedNotificationReceipt** | **Boolean**| The email address to receive the notification about the verification result. | [optional] |
| **addressCity** | **String**| City of the business | [optional] |
| **addressCountryCode** | **String**| Country code of the business | [optional] |
| **addressPostalCode** | **String**| Postal code of the business | [optional] |
| **addressStreet** | **String**| Street address of the business | [optional] |
| **addressStreetSecondary** | **String**| Street address of the business | [optional] |
| **addressSubdivision** | **String**| State or province of the business | [optional] |
| **authorizedRepresentative1DateOfBirth** | **String**| Birthdate of the authorized representative | [optional] |
| **authorizedRepresentative1Email** | **String**| Email address of the authorized representative | [optional] |
| **authorizedRepresentative1FirstName** | **String**| First name of the authorized representative | [optional] |
| **authorizedRepresentative1LastName** | **String**| Last name of the authorized representative | [optional] |
| **authorizedRepresentative1Phone** | **String**| Phone number of the authorized representative | [optional] |
| **businessIdentityType** | **ComplianceRegistrationEnumBusinessIdentityType**|  | [optional] [enum: direct_customer, isv_reseller_or_partner, unknown] |
| **businessLegalName** | **String**| he name of the business or organization using the Tollfree number. | [optional] |
| **businessRegistrationAuthority** | **ComplianceRegistrationEnumBusinessRegistrationAuthority**|  | [optional] [enum: UK:CRN, US:EIN, CA:CBN, AU:ACN, Other] |
| **businessRegistrationNumber** | **String**| Business registration number of the business | [optional] |
| **businessWebsiteUrl** | **String**| The URL of the business website | [optional] |
| **dateOfBirth** | **String**| The date of birth of the Individual User. | [optional] |
| **emergencyAddressCity** | **String**| City of the business | [optional] |
| **emergencyAddressCountryCode** | **String**| Country code of the business | [optional] |
| **emergencyAddressPostalCode** | **String**| Postal code of the business | [optional] |
| **emergencyAddressStreet** | **String**| Street address of the business | [optional] |
| **emergencyAddressStreetSecondary** | **String**| Street address of the business | [optional] |
| **emergencyAddressSubdivision** | **String**| State or province of the business | [optional] |
| **_file** | **String**| The verification document to upload | [optional] |
| **fileName** | **String**| The name of the verification document to upload | [optional] |
| **firstName** | **String**| The first name of the Individual User. | [optional] |
| **friendlyName** | **String**| Friendly name for your business information | [optional] |
| **individualEmail** | **String**| The email address of the Individual User. | [optional] |
| **individualPhone** | **String**| The phone number of the Individual User. | [optional] |
| **isIsvEmbed** | **Boolean**| Indicates if the inquiry is being started from an ISV embedded component. | [optional] |
| **lastName** | **String**| The last name of the Individual User. | [optional] |
| **notificationEmail** | **String**| he email address to receive the notification about the verification result. | [optional] |
| **useAddressAsEmergencyAddress** | **Boolean**| Use the business address as the emergency address | [optional] |

### Return type

[**TrusthubV1ComplianceRegistration**](TrusthubV1ComplianceRegistration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

