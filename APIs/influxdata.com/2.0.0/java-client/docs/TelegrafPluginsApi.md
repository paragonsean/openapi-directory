# TelegrafPluginsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTelegrafPlugins**](TelegrafPluginsApi.md#getTelegrafPlugins) | **GET** /telegraf/plugins | List all Telegraf plugins |


<a id="getTelegrafPlugins"></a>
# **getTelegrafPlugins**
> TelegrafPlugins getTelegrafPlugins(zapTraceSpan, type)

List all Telegraf plugins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelegrafPluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TelegrafPluginsApi apiInstance = new TelegrafPluginsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String type = "type_example"; // String | The type of plugin desired.
    try {
      TelegrafPlugins result = apiInstance.getTelegrafPlugins(zapTraceSpan, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelegrafPluginsApi#getTelegrafPlugins");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **type** | **String**| The type of plugin desired. | [optional] |

### Return type

[**TelegrafPlugins**](TelegrafPlugins.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Telegraf plugins. |  -  |
| **0** | Unexpected error |  -  |

