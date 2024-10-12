# TrusthubV1ComplianceTollfreeInquiriesApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createComplianceTollfreeInquiry**](TrusthubV1ComplianceTollfreeInquiriesApi.md#createComplianceTollfreeInquiry) | **POST** /v1/ComplianceInquiries/Tollfree/Initialize |  |


<a id="createComplianceTollfreeInquiry"></a>
# **createComplianceTollfreeInquiry**
> TrusthubV1ComplianceTollfreeInquiry createComplianceTollfreeInquiry(notificationEmail, tollfreePhoneNumber, additionalInformation, businessCity, businessContactEmail, businessContactFirstName, businessContactLastName, businessContactPhone, businessCountry, businessName, businessPostalCode, businessStateProvinceRegion, businessStreetAddress, businessStreetAddress2, businessWebsite, messageVolume, optInImageUrls, optInType, productionMessageSample, useCaseCategories, useCaseSummary)



Create a new Compliance Tollfree Verification Inquiry for the authenticated account. This is necessary to start a new embedded session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1ComplianceTollfreeInquiriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1ComplianceTollfreeInquiriesApi apiInstance = new TrusthubV1ComplianceTollfreeInquiriesApi(defaultClient);
    String notificationEmail = "notificationEmail_example"; // String | The email address to receive the notification about the verification result.
    String tollfreePhoneNumber = "tollfreePhoneNumber_example"; // String | The Tollfree phone number to be verified
    String additionalInformation = "additionalInformation_example"; // String | Additional information to be provided for verification.
    String businessCity = "businessCity_example"; // String | The city of the business or organization using the Tollfree number.
    String businessContactEmail = "businessContactEmail_example"; // String | The email address of the contact for the business or organization using the Tollfree number.
    String businessContactFirstName = "businessContactFirstName_example"; // String | The first name of the contact for the business or organization using the Tollfree number.
    String businessContactLastName = "businessContactLastName_example"; // String | The last name of the contact for the business or organization using the Tollfree number.
    String businessContactPhone = "businessContactPhone_example"; // String | The phone number of the contact for the business or organization using the Tollfree number.
    String businessCountry = "businessCountry_example"; // String | The country of the business or organization using the Tollfree number.
    String businessName = "businessName_example"; // String | The name of the business or organization using the Tollfree number.
    String businessPostalCode = "businessPostalCode_example"; // String | The postal code of the business or organization using the Tollfree number.
    String businessStateProvinceRegion = "businessStateProvinceRegion_example"; // String | The state/province/region of the business or organization using the Tollfree number.
    String businessStreetAddress = "businessStreetAddress_example"; // String | The address of the business or organization using the Tollfree number.
    String businessStreetAddress2 = "businessStreetAddress2_example"; // String | The address of the business or organization using the Tollfree number.
    String businessWebsite = "businessWebsite_example"; // String | The website of the business or organization using the Tollfree number.
    String messageVolume = "messageVolume_example"; // String | Estimate monthly volume of messages from the Tollfree Number.
    List<String> optInImageUrls = Arrays.asList(); // List<String> | Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    ComplianceTollfreeInquiryEnumOptInType optInType = ComplianceTollfreeInquiryEnumOptInType.fromValue("VERBAL"); // ComplianceTollfreeInquiryEnumOptInType | 
    String productionMessageSample = "productionMessageSample_example"; // String | An example of message content, i.e. a sample message.
    List<String> useCaseCategories = Arrays.asList(); // List<String> | The category of the use case for the Tollfree Number. List as many are applicable..
    String useCaseSummary = "useCaseSummary_example"; // String | Use this to further explain how messaging is used by the business or organization.
    try {
      TrusthubV1ComplianceTollfreeInquiry result = apiInstance.createComplianceTollfreeInquiry(notificationEmail, tollfreePhoneNumber, additionalInformation, businessCity, businessContactEmail, businessContactFirstName, businessContactLastName, businessContactPhone, businessCountry, businessName, businessPostalCode, businessStateProvinceRegion, businessStreetAddress, businessStreetAddress2, businessWebsite, messageVolume, optInImageUrls, optInType, productionMessageSample, useCaseCategories, useCaseSummary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1ComplianceTollfreeInquiriesApi#createComplianceTollfreeInquiry");
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
| **notificationEmail** | **String**| The email address to receive the notification about the verification result. | |
| **tollfreePhoneNumber** | **String**| The Tollfree phone number to be verified | |
| **additionalInformation** | **String**| Additional information to be provided for verification. | [optional] |
| **businessCity** | **String**| The city of the business or organization using the Tollfree number. | [optional] |
| **businessContactEmail** | **String**| The email address of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactFirstName** | **String**| The first name of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactLastName** | **String**| The last name of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessContactPhone** | **String**| The phone number of the contact for the business or organization using the Tollfree number. | [optional] |
| **businessCountry** | **String**| The country of the business or organization using the Tollfree number. | [optional] |
| **businessName** | **String**| The name of the business or organization using the Tollfree number. | [optional] |
| **businessPostalCode** | **String**| The postal code of the business or organization using the Tollfree number. | [optional] |
| **businessStateProvinceRegion** | **String**| The state/province/region of the business or organization using the Tollfree number. | [optional] |
| **businessStreetAddress** | **String**| The address of the business or organization using the Tollfree number. | [optional] |
| **businessStreetAddress2** | **String**| The address of the business or organization using the Tollfree number. | [optional] |
| **businessWebsite** | **String**| The website of the business or organization using the Tollfree number. | [optional] |
| **messageVolume** | **String**| Estimate monthly volume of messages from the Tollfree Number. | [optional] |
| **optInImageUrls** | [**List&lt;String&gt;**](String.md)| Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL. | [optional] |
| **optInType** | **ComplianceTollfreeInquiryEnumOptInType**|  | [optional] [enum: VERBAL, WEB_FORM, PAPER_FORM, VIA_TEXT, MOBILE_QR_CODE] |
| **productionMessageSample** | **String**| An example of message content, i.e. a sample message. | [optional] |
| **useCaseCategories** | [**List&lt;String&gt;**](String.md)| The category of the use case for the Tollfree Number. List as many are applicable.. | [optional] |
| **useCaseSummary** | **String**| Use this to further explain how messaging is used by the business or organization. | [optional] |

### Return type

[**TrusthubV1ComplianceTollfreeInquiry**](TrusthubV1ComplianceTollfreeInquiry.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

