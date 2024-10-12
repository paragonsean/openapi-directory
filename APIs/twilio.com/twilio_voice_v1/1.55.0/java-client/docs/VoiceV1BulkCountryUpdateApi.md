# VoiceV1BulkCountryUpdateApi

All URIs are relative to *https://voice.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDialingPermissionsCountryBulkUpdate**](VoiceV1BulkCountryUpdateApi.md#createDialingPermissionsCountryBulkUpdate) | **POST** /v1/DialingPermissions/BulkCountryUpdates |  |


<a id="createDialingPermissionsCountryBulkUpdate"></a>
# **createDialingPermissionsCountryBulkUpdate**
> VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate createDialingPermissionsCountryBulkUpdate(updateRequest)



Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1BulkCountryUpdateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1BulkCountryUpdateApi apiInstance = new VoiceV1BulkCountryUpdateApi(defaultClient);
    String updateRequest = "updateRequest_example"; // String | URL encoded JSON array of update objects. example : `[ { \\\"iso_code\\\": \\\"GB\\\", \\\"low_risk_numbers_enabled\\\": \\\"true\\\", \\\"high_risk_special_numbers_enabled\\\":\\\"true\\\", \\\"high_risk_tollfraud_numbers_enabled\\\": \\\"false\\\" } ]`
    try {
      VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate result = apiInstance.createDialingPermissionsCountryBulkUpdate(updateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1BulkCountryUpdateApi#createDialingPermissionsCountryBulkUpdate");
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
| **updateRequest** | **String**| URL encoded JSON array of update objects. example : &#x60;[ { \\\&quot;iso_code\\\&quot;: \\\&quot;GB\\\&quot;, \\\&quot;low_risk_numbers_enabled\\\&quot;: \\\&quot;true\\\&quot;, \\\&quot;high_risk_special_numbers_enabled\\\&quot;:\\\&quot;true\\\&quot;, \\\&quot;high_risk_tollfraud_numbers_enabled\\\&quot;: \\\&quot;false\\\&quot; } ]&#x60; | |

### Return type

[**VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate**](VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

