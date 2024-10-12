# SmsConversionApi

All URIs are relative to *https://api.nexmo.com/conversions*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**smsConversion**](SmsConversionApi.md#smsConversion) | **POST** /sms | Tell Nexmo if your SMS message was successful |


<a id="smsConversion"></a>
# **smsConversion**
> smsConversion(messageId, delivered, timestamp)

Tell Nexmo if your SMS message was successful

Send a Conversion API request with information about the SMS message identified by &#x60;message-id&#x60;. Nexmo uses your conversion data and internal information about &#x60;message-id&#x60; to help improve our routing of messages in the future.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/conversions");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSig
    ApiKeyAuth apiSig = (ApiKeyAuth) defaultClient.getAuthentication("apiSig");
    apiSig.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSig.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    SmsConversionApi apiInstance = new SmsConversionApi(defaultClient);
    String messageId = "00A0B0C0"; // String | The ID you receive in the response to a request. * From the Verify API - use the `event_id` in the response to Verify Check. * From the SMS API - use the `message-id` * From the Text-To-Speech API - use the `call-id` * From the Text-To-Speech-Prompt API - use the `call-id`
    Boolean delivered = true; // Boolean | Set to _true_ if your user replied to the message you sent. Otherwise, set to _false_. **Note**: for curl, use 0 and 1.
    String timestamp = "2020-01-01 12:00:00"; // String | When the user completed your call-to-action (e.g. visited your website, installed your app) in [UTC±00:00](https://en.wikipedia.org/wiki/UTC%C2%B100:00) format: _yyyy-MM-dd HH:mm:ss_. If you do not set this parameter, Nexmo uses the time it receives this request.
    try {
      apiInstance.smsConversion(messageId, delivered, timestamp);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsConversionApi#smsConversion");
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
| **messageId** | **String**| The ID you receive in the response to a request. * From the Verify API - use the &#x60;event_id&#x60; in the response to Verify Check. * From the SMS API - use the &#x60;message-id&#x60; * From the Text-To-Speech API - use the &#x60;call-id&#x60; * From the Text-To-Speech-Prompt API - use the &#x60;call-id&#x60; | |
| **delivered** | **Boolean**| Set to _true_ if your user replied to the message you sent. Otherwise, set to _false_. **Note**: for curl, use 0 and 1. | [enum: true, false, 0, 1] |
| **timestamp** | **String**| When the user completed your call-to-action (e.g. visited your website, installed your app) in [UTC±00:00](https://en.wikipedia.org/wiki/UTC%C2%B100:00) format: _yyyy-MM-dd HH:mm:ss_. If you do not set this parameter, Nexmo uses the time it receives this request. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [apiSig](../README.md#apiSig), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Wrong credentials |  -  |
| **402** | Conversion has not been enabled for your account |  -  |
| **420** | Invalid parameters |  -  |
| **423** | Invalid parameters |  -  |

