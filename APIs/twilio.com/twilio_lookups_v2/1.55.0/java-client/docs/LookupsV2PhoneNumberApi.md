# LookupsV2PhoneNumberApi

All URIs are relative to *https://lookups.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchPhoneNumber**](LookupsV2PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v2/PhoneNumbers/{PhoneNumber} |  |


<a id="fetchPhoneNumber"></a>
# **fetchPhoneNumber**
> LookupsV2PhoneNumber fetchPhoneNumber(phoneNumber, fields, countryCode, firstName, lastName, addressLine1, addressLine2, city, state, postalCode, addressCountryCode, nationalId, dateOfBirth, lastVerifiedDate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupsV2PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lookups.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    LookupsV2PhoneNumberApi apiInstance = new LookupsV2PhoneNumberApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
    String fields = "fields_example"; // String | A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap, call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number, sms_pumping_risk, phone_number_quality_score.
    String countryCode = "countryCode_example"; // String | The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
    String firstName = "firstName_example"; // String | User’s first name. This query parameter is only used (optionally) for identity_match package requests.
    String lastName = "lastName_example"; // String | User’s last name. This query parameter is only used (optionally) for identity_match package requests.
    String addressLine1 = "addressLine1_example"; // String | User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
    String addressLine2 = "addressLine2_example"; // String | User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
    String city = "city_example"; // String | User’s city. This query parameter is only used (optionally) for identity_match package requests.
    String state = "state_example"; // String | User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
    String postalCode = "postalCode_example"; // String | User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
    String addressCountryCode = "addressCountryCode_example"; // String | User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
    String nationalId = "nationalId_example"; // String | User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
    String dateOfBirth = "dateOfBirth_example"; // String | User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.
    String lastVerifiedDate = "lastVerifiedDate_example"; // String | The date you obtained consent to call or text the end-user of the phone number or a date on which you are reasonably certain that the end-user could still be reached at that number. This query parameter is only used (optionally) for reassigned_number package requests.
    try {
      LookupsV2PhoneNumber result = apiInstance.fetchPhoneNumber(phoneNumber, fields, countryCode, firstName, lastName, addressLine1, addressLine2, city, state, postalCode, addressCountryCode, nationalId, dateOfBirth, lastVerifiedDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupsV2PhoneNumberApi#fetchPhoneNumber");
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
| **phoneNumber** | **String**| The phone number to lookup in E.164 or national format. Default country code is +1 (North America). | |
| **fields** | **String**| A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap, call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number, sms_pumping_risk, phone_number_quality_score. | [optional] |
| **countryCode** | **String**| The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format. | [optional] |
| **firstName** | **String**| User’s first name. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **lastName** | **String**| User’s last name. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **addressLine1** | **String**| User’s first address line. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **addressLine2** | **String**| User’s second address line. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **city** | **String**| User’s city. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **state** | **String**| User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **postalCode** | **String**| User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **addressCountryCode** | **String**| User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **nationalId** | **String**| User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **dateOfBirth** | **String**| User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests. | [optional] |
| **lastVerifiedDate** | **String**| The date you obtained consent to call or text the end-user of the phone number or a date on which you are reasonably certain that the end-user could still be reached at that number. This query parameter is only used (optionally) for reassigned_number package requests. | [optional] |

### Return type

[**LookupsV2PhoneNumber**](LookupsV2PhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

