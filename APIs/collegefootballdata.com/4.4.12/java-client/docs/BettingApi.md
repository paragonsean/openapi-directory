# BettingApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLines**](BettingApi.md#getLines) | **GET** /lines | Betting lines |


<a id="getLines"></a>
# **getLines**
> List&lt;GameLines&gt; getLines(gameId, year, week, seasonType, team, home, away, conference)

Betting lines

Closing betting lines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    BettingApi apiInstance = new BettingApi(defaultClient);
    Integer gameId = 56; // Integer | Game id filter
    Integer year = 56; // Integer | Year/season filter for games
    Integer week = 56; // Integer | Week filter
    String seasonType = "regular"; // String | Season type filter (regular or postseason)
    String team = "team_example"; // String | Team
    String home = "home_example"; // String | Home team filter
    String away = "away_example"; // String | Away team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    try {
      List<GameLines> result = apiInstance.getLines(gameId, year, week, seasonType, team, home, away, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BettingApi#getLines");
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
| **gameId** | **Integer**| Game id filter | [optional] |
| **year** | **Integer**| Year/season filter for games | [optional] |
| **week** | **Integer**| Week filter | [optional] |
| **seasonType** | **String**| Season type filter (regular or postseason) | [optional] [default to regular] |
| **team** | **String**| Team | [optional] |
| **home** | **String**| Home team filter | [optional] |
| **away** | **String**| Away team filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |

### Return type

[**List&lt;GameLines&gt;**](GameLines.md)

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

