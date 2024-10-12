# DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/nfl/news-rotoballer*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**premiumNews**](DefaultApi.md#premiumNews) | **GET** /{format}/RotoBallerPremiumNews | Premium News |
| [**premiumNewsByDate**](DefaultApi.md#premiumNewsByDate) | **GET** /{format}/RotoBallerPremiumNewsByDate/{date} | Premium News by Date |
| [**premiumNewsByPlayer**](DefaultApi.md#premiumNewsByPlayer) | **GET** /{format}/RotoBallerPremiumNewsByPlayerID/{playerid} | Premium News by Player |
| [**premiumNewsByTeam**](DefaultApi.md#premiumNewsByTeam) | **GET** /{format}/RotoBallerPremiumNewsByTeam/{team} | Premium News by Team |


<a id="premiumNews"></a>
# **premiumNews**
> List&lt;News&gt; premiumNews(format)

Premium News

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
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/news-rotoballer");
    
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
    String format = "xml"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    try {
      List<News> result = apiInstance.premiumNews(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#premiumNews");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to xml] [enum: xml, json] |

### Return type

[**List&lt;News&gt;**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="premiumNewsByDate"></a>
# **premiumNewsByDate**
> List&lt;News&gt; premiumNewsByDate(format, date)

Premium News by Date

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
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/news-rotoballer");
    
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
    String format = "xml"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String date = "date_example"; // String | The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
    try {
      List<News> result = apiInstance.premiumNewsByDate(format, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#premiumNewsByDate");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to xml] [enum: xml, json] |
| **date** | **String**| The date of the news. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;. | |

### Return type

[**List&lt;News&gt;**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="premiumNewsByPlayer"></a>
# **premiumNewsByPlayer**
> List&lt;News&gt; premiumNewsByPlayer(format, playerid)

Premium News by Player

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
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/news-rotoballer");
    
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
    String format = "xml"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>10000507</code>.
    try {
      List<News> result = apiInstance.premiumNewsByPlayer(format, playerid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#premiumNewsByPlayer");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to xml] [enum: xml, json] |
| **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;10000507&lt;/code&gt;. | |

### Return type

[**List&lt;News&gt;**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="premiumNewsByTeam"></a>
# **premiumNewsByTeam**
> List&lt;News&gt; premiumNewsByTeam(format, team)

Premium News by Team

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
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/news-rotoballer");
    
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
    String format = "xml"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
    try {
      List<News> result = apiInstance.premiumNewsByTeam(format, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#premiumNewsByTeam");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to xml] [enum: xml, json] |
| **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | |

### Return type

[**List&lt;News&gt;**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

