# VerifyV2VerificationAttemptsSummaryApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchVerificationAttemptsSummary**](VerifyV2VerificationAttemptsSummaryApi.md#fetchVerificationAttemptsSummary) | **GET** /v2/Attempts/Summary |  |


<a id="fetchVerificationAttemptsSummary"></a>
# **fetchVerificationAttemptsSummary**
> VerifyV2VerificationAttemptsSummary fetchVerificationAttemptsSummary(verifyServiceSid, dateCreatedAfter, dateCreatedBefore, country, channel, destinationPrefix)



Get a summary of how many attempts were made and how many were converted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2VerificationAttemptsSummaryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2VerificationAttemptsSummaryApi apiInstance = new VerifyV2VerificationAttemptsSummaryApi(defaultClient);
    String verifyServiceSid = "verifyServiceSid_example"; // String | Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
    OffsetDateTime dateCreatedAfter = OffsetDateTime.now(); // OffsetDateTime | Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
    OffsetDateTime dateCreatedBefore = OffsetDateTime.now(); // OffsetDateTime | Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
    String country = "country_example"; // String | Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
    VerificationAttemptsSummaryEnumChannels channel = VerificationAttemptsSummaryEnumChannels.fromValue("sms"); // VerificationAttemptsSummaryEnumChannels | Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS`, `CALL` and `WHATSAPP`
    String destinationPrefix = "destinationPrefix_example"; // String | Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.
    try {
      VerifyV2VerificationAttemptsSummary result = apiInstance.fetchVerificationAttemptsSummary(verifyServiceSid, dateCreatedAfter, dateCreatedBefore, country, channel, destinationPrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2VerificationAttemptsSummaryApi#fetchVerificationAttemptsSummary");
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
| **verifyServiceSid** | **String**| Filter used to consider only Verification Attempts of the given verify service on the summary aggregation. | [optional] |
| **dateCreatedAfter** | **OffsetDateTime**| Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] |
| **dateCreatedBefore** | **OffsetDateTime**| Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z. | [optional] |
| **country** | **String**| Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation. | [optional] |
| **channel** | **VerificationAttemptsSummaryEnumChannels**| Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are &#x60;SMS&#x60;, &#x60;CALL&#x60; and &#x60;WHATSAPP&#x60; | [optional] [enum: sms, call, email, whatsapp] |
| **destinationPrefix** | **String**| Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format. | [optional] |

### Return type

[**VerifyV2VerificationAttemptsSummary**](VerifyV2VerificationAttemptsSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

