# SmsApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sms**](SmsApi.md#sms) | **POST** /sms |  |


<a id="sms"></a>
# **sms**
> Sms200Response sms(text, to, from, foreignId, label, udh, delay, debug, noReload, unicode, flash, utf8, details, returnMsgId, json, performanceTracking)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SmsApi apiInstance = new SmsApi(defaultClient);
    String text = "text_example"; // String | The actual text message to send.
    String to = "to_example"; // String | The recipient number or group name.
    String from = "from_example"; // String | Set a custom sender name.
    String foreignId = "foreignId_example"; // String | Identifier to return in callbacks.
    String label = "label_example"; // String | A custom label.
    String udh = "udh_example"; // String | A custom User Data Header.
    String delay = "delay_example"; // String | Date/Time for delayed dispatch.
    BigDecimal debug = new BigDecimal("1"); // BigDecimal | Disable message sending.
    BigDecimal noReload = new BigDecimal("1"); // BigDecimal | Enable sending of duplicated messages within 180 seconds.
    BigDecimal unicode = new BigDecimal("1"); // BigDecimal | Force unicode encoding. Reduces sms length to 70 chars.
    BigDecimal flash = new BigDecimal("1"); // BigDecimal | Send as flash.
    BigDecimal utf8 = new BigDecimal("1"); // BigDecimal | Force UTF8 encoding.
    BigDecimal details = new BigDecimal("1"); // BigDecimal | Attach message details to response.
    BigDecimal returnMsgId = new BigDecimal("1"); // BigDecimal | Attach message ID to second row in a text response.
    BigDecimal json = new BigDecimal("1"); // BigDecimal | Return a detailed JSON response.
    BigDecimal performanceTracking = new BigDecimal("1"); // BigDecimal | Enable performance tracking for found URLs.
    try {
      Sms200Response result = apiInstance.sms(text, to, from, foreignId, label, udh, delay, debug, noReload, unicode, flash, utf8, details, returnMsgId, json, performanceTracking);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#sms");
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
| **text** | **String**| The actual text message to send. | |
| **to** | **String**| The recipient number or group name. | |
| **from** | **String**| Set a custom sender name. | [optional] |
| **foreignId** | **String**| Identifier to return in callbacks. | [optional] |
| **label** | **String**| A custom label. | [optional] |
| **udh** | **String**| A custom User Data Header. | [optional] |
| **delay** | **String**| Date/Time for delayed dispatch. | [optional] |
| **debug** | **BigDecimal**| Disable message sending. | [optional] [default to 0] [enum: 1, 0] |
| **noReload** | **BigDecimal**| Enable sending of duplicated messages within 180 seconds. | [optional] [default to 0] [enum: 1, 0] |
| **unicode** | **BigDecimal**| Force unicode encoding. Reduces sms length to 70 chars. | [optional] [default to 0] [enum: 1, 0] |
| **flash** | **BigDecimal**| Send as flash. | [optional] [default to 0] [enum: 1, 0] |
| **utf8** | **BigDecimal**| Force UTF8 encoding. | [optional] [default to 0] [enum: 1, 0] |
| **details** | **BigDecimal**| Attach message details to response. | [optional] [default to 0] [enum: 1, 0] |
| **returnMsgId** | **BigDecimal**| Attach message ID to second row in a text response. | [optional] [default to 0] [enum: 1, 0] |
| **json** | **BigDecimal**| Return a detailed JSON response. | [optional] [default to 0] [enum: 1, 0] |
| **performanceTracking** | **BigDecimal**| Enable performance tracking for found URLs. | [optional] [default to 0] [enum: 1, 0] |

### Return type

[**Sms200Response**](Sms200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

