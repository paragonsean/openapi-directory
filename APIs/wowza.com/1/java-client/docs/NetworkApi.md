# NetworkApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usageNetworkStreamSourcesIndex**](NetworkApi.md#usageNetworkStreamSourcesIndex) | **GET** /usage/network/stream_sources | Fetch network usage for all stream sources |
| [**usageNetworkStreamTargetsIndex**](NetworkApi.md#usageNetworkStreamTargetsIndex) | **GET** /usage/network/stream_targets | Fetch network usage for all stream targets |
| [**usageNetworkTranscodersIndex**](NetworkApi.md#usageNetworkTranscodersIndex) | **GET** /usage/network/transcoders | Fetch network usage for all transcoders |


<a id="usageNetworkStreamSourcesIndex"></a>
# **usageNetworkStreamSourcesIndex**
> UsageNetworkStreamSources usageNetworkStreamSourcesIndex(from, to)

Fetch network usage for all stream sources

This operation shows the amount of network usage for all stream sources in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkApi;

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

    NetworkApi apiInstance = new NetworkApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
    try {
      UsageNetworkStreamSources result = apiInstance.usageNetworkStreamSourcesIndex(from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkApi#usageNetworkStreamSourcesIndex");
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

### Return type

[**UsageNetworkStreamSources**](UsageNetworkStreamSources.md)

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

<a id="usageNetworkStreamTargetsIndex"></a>
# **usageNetworkStreamTargetsIndex**
> UsageNetworkStreamTargets usageNetworkStreamTargetsIndex(from, to)

Fetch network usage for all stream targets

This operation shows the amount of network usage for all stream targets in the account cumulatively and individually. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkApi;

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

    NetworkApi apiInstance = new NetworkApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
    try {
      UsageNetworkStreamTargets result = apiInstance.usageNetworkStreamTargetsIndex(from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkApi#usageNetworkStreamTargetsIndex");
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

### Return type

[**UsageNetworkStreamTargets**](UsageNetworkStreamTargets.md)

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

<a id="usageNetworkTranscodersIndex"></a>
# **usageNetworkTranscodersIndex**
> UsageNetworkTranscoders usageNetworkTranscodersIndex(from, to, transcoderType, billingMode)

Fetch network usage for all transcoders

This operation shows the amount of network usage (egress) for all transcoders in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkApi;

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

    NetworkApi apiInstance = new NetworkApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
    String transcoderType = "transcoded"; // String | The type of transcoder. The default is <strong>transcoded</strong>.
    String billingMode = "pay_as_you_go"; // String | The billing mode for the transcoder. The default is <strong>pay_as_you_go</strong>.
    try {
      UsageNetworkTranscoders result = apiInstance.usageNetworkTranscodersIndex(from, to, transcoderType, billingMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkApi#usageNetworkTranscodersIndex");
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

[**UsageNetworkTranscoders**](UsageNetworkTranscoders.md)

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

