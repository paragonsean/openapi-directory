# RankingsApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRankings**](RankingsApi.md#getRankings) | **GET** /rankings | Historical polls and rankings |


<a id="getRankings"></a>
# **getRankings**
> List&lt;RankingWeek&gt; getRankings(year, week, seasonType)

Historical polls and rankings

Poll rankings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RankingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RankingsApi apiInstance = new RankingsApi(defaultClient);
    Integer year = 56; // Integer | Year/season filter for games
    Integer week = 56; // Integer | Week filter
    String seasonType = "regular"; // String | Season type filter (regular or postseason)
    try {
      List<RankingWeek> result = apiInstance.getRankings(year, week, seasonType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RankingsApi#getRankings");
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
| **year** | **Integer**| Year/season filter for games | |
| **week** | **Integer**| Week filter | [optional] |
| **seasonType** | **String**| Season type filter (regular or postseason) | [optional] [default to regular] |

### Return type

[**List&lt;RankingWeek&gt;**](RankingWeek.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | error |  -  |

