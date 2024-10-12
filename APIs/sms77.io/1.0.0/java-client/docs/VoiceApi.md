# VoiceApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**voice**](VoiceApi.md#voice) | **POST** /voice |  |


<a id="voice"></a>
# **voice**
> String voice(to, text, xml, from)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VoiceApi apiInstance = new VoiceApi(defaultClient);
    String to = "to_example"; // String | Determines the receiver. Must be a valid phone number or contact from the address book.
    String text = "text_example"; // String | The text to convert to a voice message. Accepts valid XML too.
    BigDecimal xml = new BigDecimal("1"); // BigDecimal | Decides whether the parameter \"text\" is plain text or XML. The default value is 0.
    String from = "from_example"; // String | Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours.
    try {
      String result = apiInstance.voice(to, text, xml, from);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceApi#voice");
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
| **to** | **String**| Determines the receiver. Must be a valid phone number or contact from the address book. | |
| **text** | **String**| The text to convert to a voice message. Accepts valid XML too. | |
| **xml** | **BigDecimal**| Decides whether the parameter \&quot;text\&quot; is plain text or XML. The default value is 0. | [optional] [enum: 1, 0] |
| **from** | **String**| Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours. | [optional] |

### Return type

**String**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

