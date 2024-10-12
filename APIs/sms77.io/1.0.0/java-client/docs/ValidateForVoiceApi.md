# ValidateForVoiceApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**validateForVoice**](ValidateForVoiceApi.md#validateForVoice) | **POST** /validate_for_voice |  |


<a id="validateForVoice"></a>
# **validateForVoice**
> ValidateForVoice200Response validateForVoice(number, paramCallback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidateForVoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ValidateForVoiceApi apiInstance = new ValidateForVoiceApi(defaultClient);
    String number = "number_example"; // String | Determines the recipient. Can only be a number, not a contact from your address book.
    URI paramCallback = new URI(); // URI | The callback URL which gets queried right after validation.
    try {
      ValidateForVoice200Response result = apiInstance.validateForVoice(number, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidateForVoiceApi#validateForVoice");
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
| **number** | **String**| Determines the recipient. Can only be a number, not a contact from your address book. | |
| **paramCallback** | **URI**| The callback URL which gets queried right after validation. | [optional] |

### Return type

[**ValidateForVoice200Response**](ValidateForVoice200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

