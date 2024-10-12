# PricingV2NumberApi

All URIs are relative to *https://pricing.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTrunkingNumber**](PricingV2NumberApi.md#fetchTrunkingNumber) | **GET** /v2/Trunking/Numbers/{DestinationNumber} |  |
| [**fetchVoiceNumber**](PricingV2NumberApi.md#fetchVoiceNumber) | **GET** /v2/Voice/Numbers/{DestinationNumber} |  |


<a id="fetchTrunkingNumber"></a>
# **fetchTrunkingNumber**
> PricingV2TrunkingNumber fetchTrunkingNumber(destinationNumber, originationNumber)



Fetch pricing information for a specific destination and, optionally, origination phone number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingV2NumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pricing.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PricingV2NumberApi apiInstance = new PricingV2NumberApi(defaultClient);
    String destinationNumber = "destinationNumber_example"; // String | The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    String originationNumber = "originationNumber_example"; // String | The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    try {
      PricingV2TrunkingNumber result = apiInstance.fetchTrunkingNumber(destinationNumber, originationNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingV2NumberApi#fetchTrunkingNumber");
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
| **destinationNumber** | **String**| The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | |
| **originationNumber** | **String**| The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | [optional] |

### Return type

[**PricingV2TrunkingNumber**](PricingV2TrunkingNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchVoiceNumber"></a>
# **fetchVoiceNumber**
> PricingV2VoiceVoiceNumber fetchVoiceNumber(destinationNumber, originationNumber)



Fetch pricing information for a specific destination and, optionally, origination phone number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingV2NumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pricing.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PricingV2NumberApi apiInstance = new PricingV2NumberApi(defaultClient);
    String destinationNumber = "destinationNumber_example"; // String | The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    String originationNumber = "originationNumber_example"; // String | The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    try {
      PricingV2VoiceVoiceNumber result = apiInstance.fetchVoiceNumber(destinationNumber, originationNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingV2NumberApi#fetchVoiceNumber");
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
| **destinationNumber** | **String**| The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | |
| **originationNumber** | **String**| The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number. | [optional] |

### Return type

[**PricingV2VoiceVoiceNumber**](PricingV2VoiceVoiceNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

