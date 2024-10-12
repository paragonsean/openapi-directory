# PricingV1NumberApi

All URIs are relative to *https://pricing.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchVoiceNumber**](PricingV1NumberApi.md#fetchVoiceNumber) | **GET** /v1/Voice/Numbers/{Number} |  |


<a id="fetchVoiceNumber"></a>
# **fetchVoiceNumber**
> PricingV1VoiceVoiceNumber fetchVoiceNumber(number)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingV1NumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pricing.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PricingV1NumberApi apiInstance = new PricingV1NumberApi(defaultClient);
    String number = "number_example"; // String | The phone number to fetch.
    try {
      PricingV1VoiceVoiceNumber result = apiInstance.fetchVoiceNumber(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingV1NumberApi#fetchVoiceNumber");
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
| **number** | **String**| The phone number to fetch. | |

### Return type

[**PricingV1VoiceVoiceNumber**](PricingV1VoiceVoiceNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

