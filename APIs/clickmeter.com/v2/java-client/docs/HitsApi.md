# HitsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hitsGetHits**](HitsApi.md#hitsGetHits) | **GET** /hits | Retrieve the list of events related to this account. |


<a id="hitsGetHits"></a>
# **hitsGetHits**
> ApiCoreDtoClickStreamHitListPage hitsGetHits(timeframe, limit, offset, fromDay, toDay, filter)

Retrieve the list of events related to this account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    HitsApi apiInstance = new HitsApi(defaultClient);
    String timeframe = "yesterday"; // String | Timeframe of the request. See list at $timeframeList
    Integer limit = 56; // Integer | Limit results to this number
    String offset = "offset_example"; // String | Offset where to start from (it's the lastKey field in the response object)
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String filter = "spiders"; // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
    try {
      ApiCoreDtoClickStreamHitListPage result = apiInstance.hitsGetHits(timeframe, limit, offset, fromDay, toDay, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HitsApi#hitsGetHits");
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
| **timeframe** | **String**| Timeframe of the request. See list at $timeframeList | [enum: yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, custom] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **offset** | **String**| Offset where to start from (it&#39;s the lastKey field in the response object) | [optional] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **filter** | **String**| Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;) | [optional] [enum: spiders, uniques, nonuniques, conversions] |

### Return type

[**ApiCoreDtoClickStreamHitListPage**](ApiCoreDtoClickStreamHitListPage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

