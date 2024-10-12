# ProcessingTimeApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usageTimeTranscodersIndex**](ProcessingTimeApi.md#usageTimeTranscodersIndex) | **GET** /usage/time/transcoders | Fetch stream processing time |


<a id="usageTimeTranscodersIndex"></a>
# **usageTimeTranscodersIndex**
> UsageTimeTranscoders usageTimeTranscodersIndex(from, to, transcoderType, billingMode)

Fetch stream processing time

This operation shows the amount of stream processing time used by all transcoders in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    ProcessingTimeApi apiInstance = new ProcessingTimeApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
    String transcoderType = "transcoded"; // String | The type of transcoder. The default is <strong>transcoded</strong>.
    String billingMode = "pay_as_you_go"; // String | The billing mode for the transcoder. The default is <strong>pay_as_you_go</strong>.
    try {
      UsageTimeTranscoders result = apiInstance.usageTimeTranscodersIndex(from, to, transcoderType, billingMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingTimeApi#usageTimeTranscodersIndex");
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
| **from** | **OffsetDateTime**| The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date. | [optional] |
| **to** | **OffsetDateTime**| The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day. | [optional] |
| **transcoderType** | **String**| The type of transcoder. The default is &lt;strong&gt;transcoded&lt;/strong&gt;. | [optional] [enum: transcoded, passthrough] |
| **billingMode** | **String**| The billing mode for the transcoder. The default is &lt;strong&gt;pay_as_you_go&lt;/strong&gt;. | [optional] [enum: pay_as_you_go, twentyfour_seven] |

### Return type

[**UsageTimeTranscoders**](UsageTimeTranscoders.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unauthorized |  -  |

