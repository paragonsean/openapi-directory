# PlayersApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPlayerSeasonStats**](PlayersApi.md#getPlayerSeasonStats) | **GET** /stats/player/season | Player stats by season |
| [**getPlayerUsage**](PlayersApi.md#getPlayerUsage) | **GET** /player/usage | Player usage metrics broken down by season |
| [**getReturningProduction**](PlayersApi.md#getReturningProduction) | **GET** /player/returning | Team returning production metrics |
| [**getTransferPortal**](PlayersApi.md#getTransferPortal) | **GET** /player/portal | Transfer portal by season |
| [**playerSearch**](PlayersApi.md#playerSearch) | **GET** /player/search | Search for player information |


<a id="getPlayerSeasonStats"></a>
# **getPlayerSeasonStats**
> List&lt;PlayerSeasonStat&gt; getPlayerSeasonStats(year, team, conference, startWeek, endWeek, seasonType, category)

Player stats by season

Season player stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    Integer startWeek = 56; // Integer | Start week filter
    Integer endWeek = 56; // Integer | Start week filter
    String seasonType = "seasonType_example"; // String | Season type filter (regular, postseason, or both)
    String category = "category_example"; // String | Stat category filter (e.g. passing)
    try {
      List<PlayerSeasonStat> result = apiInstance.getPlayerSeasonStats(year, team, conference, startWeek, endWeek, seasonType, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#getPlayerSeasonStats");
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
| **year** | **Integer**| Year filter | |
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |
| **startWeek** | **Integer**| Start week filter | [optional] |
| **endWeek** | **Integer**| Start week filter | [optional] |
| **seasonType** | **String**| Season type filter (regular, postseason, or both) | [optional] |
| **category** | **String**| Stat category filter (e.g. passing) | [optional] |

### Return type

[**List&lt;PlayerSeasonStat&gt;**](PlayerSeasonStat.md)

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

<a id="getPlayerUsage"></a>
# **getPlayerUsage**
> List&lt;PlayerUsage&gt; getPlayerUsage(year, team, conference, position, playerId, excludeGarbageTime)

Player usage metrics broken down by season

Player usage metrics by season

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    Integer year = 2022; // Integer | Year filter
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    String position = "position_example"; // String | Position abbreviation filter
    Integer playerId = 56; // Integer | Player id filter
    Boolean excludeGarbageTime = true; // Boolean | Filter to remove garbage time plays from calculations
    try {
      List<PlayerUsage> result = apiInstance.getPlayerUsage(year, team, conference, position, playerId, excludeGarbageTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#getPlayerUsage");
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
| **year** | **Integer**| Year filter | [default to 2022] |
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |
| **position** | **String**| Position abbreviation filter | [optional] |
| **playerId** | **Integer**| Player id filter | [optional] |
| **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] |

### Return type

[**List&lt;PlayerUsage&gt;**](PlayerUsage.md)

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

<a id="getReturningProduction"></a>
# **getReturningProduction**
> List&lt;ReturningProduction&gt; getReturningProduction(year, team, conference)

Team returning production metrics

Returning production metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    try {
      List<ReturningProduction> result = apiInstance.getReturningProduction(year, team, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#getReturningProduction");
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
| **year** | **Integer**| Year filter | [optional] |
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |

### Return type

[**List&lt;ReturningProduction&gt;**](ReturningProduction.md)

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

<a id="getTransferPortal"></a>
# **getTransferPortal**
> List&lt;PortalPlayer&gt; getTransferPortal(year)

Transfer portal by season

Transfer portal by season

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    try {
      List<PortalPlayer> result = apiInstance.getTransferPortal(year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#getTransferPortal");
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
| **year** | **Integer**| Year filter | |

### Return type

[**List&lt;PortalPlayer&gt;**](PortalPlayer.md)

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

<a id="playerSearch"></a>
# **playerSearch**
> List&lt;PlayerSearchResult&gt; playerSearch(searchTerm, position, team, year)

Search for player information

Search for players

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Term to search on
    String position = "position_example"; // String | Position abbreviation filter
    String team = "team_example"; // String | Team filter
    Integer year = 56; // Integer | Year filter
    try {
      List<PlayerSearchResult> result = apiInstance.playerSearch(searchTerm, position, team, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#playerSearch");
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
| **searchTerm** | **String**| Term to search on | |
| **position** | **String**| Position abbreviation filter | [optional] |
| **team** | **String**| Team filter | [optional] |
| **year** | **Integer**| Year filter | [optional] |

### Return type

[**List&lt;PlayerSearchResult&gt;**](PlayerSearchResult.md)

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

