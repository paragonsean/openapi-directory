# DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/mlb/pbp*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**playByPlay**](DefaultApi.md#playByPlay) | **GET** /{format}/PlayByPlay/{gameid} | Play By Play |
| [**playByPlayDelta**](DefaultApi.md#playByPlayDelta) | **GET** /{format}/PlayByPlayDelta/{date}/{minutes} | Play By Play Delta |


<a id="playByPlay"></a>
# **playByPlay**
> PlayByPlay playByPlay(format, gameid)

Play By Play

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/mlb/pbp");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String gameid = "gameid_example"; // String | The GameID of an MLB game.  GameIDs can be found in the Games API.  Valid entries are <code>14620</code> or <code>16905</code>
    try {
      PlayByPlay result = apiInstance.playByPlay(format, gameid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#playByPlay");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **gameid** | **String**| The GameID of an MLB game.  GameIDs can be found in the Games API.  Valid entries are &lt;code&gt;14620&lt;/code&gt; or &lt;code&gt;16905&lt;/code&gt; | |

### Return type

[**PlayByPlay**](PlayByPlay.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="playByPlayDelta"></a>
# **playByPlayDelta**
> List&lt;PlayByPlay&gt; playByPlayDelta(format, date, minutes)

Play By Play Delta

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/mlb/pbp");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
    String minutes = "minutes_example"; // String | Only returns plays that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
    try {
      List<PlayByPlay> result = apiInstance.playByPlayDelta(format, date, minutes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#playByPlayDelta");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;. | |
| **minutes** | **String**| Only returns plays that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt; ... &lt;code&gt;all&lt;/code&gt;. | |

### Return type

[**List&lt;PlayByPlay&gt;**](PlayByPlay.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

