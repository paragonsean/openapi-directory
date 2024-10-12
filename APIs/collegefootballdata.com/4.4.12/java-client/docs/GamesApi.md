# GamesApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAdvancedBoxScore**](GamesApi.md#getAdvancedBoxScore) | **GET** /game/box/advanced | Advanced box scores |
| [**getCalendar**](GamesApi.md#getCalendar) | **GET** /calendar | Season calendar |
| [**getGameMedia**](GamesApi.md#getGameMedia) | **GET** /games/media | Game media information and schedules |
| [**getGameWeather**](GamesApi.md#getGameWeather) | **GET** /games/weather | Game weather information (Patreon only) |
| [**getGames**](GamesApi.md#getGames) | **GET** /games | Games and results |
| [**getPlayerGameStats**](GamesApi.md#getPlayerGameStats) | **GET** /games/players | Player game stats |
| [**getScoreboard**](GamesApi.md#getScoreboard) | **GET** /scoreboard | Live game results (Patreon only) |
| [**getTeamGameStats**](GamesApi.md#getTeamGameStats) | **GET** /games/teams | Team game stats |
| [**getTeamRecords**](GamesApi.md#getTeamRecords) | **GET** /records | Team records |


<a id="getAdvancedBoxScore"></a>
# **getAdvancedBoxScore**
> BoxScore getAdvancedBoxScore(gameId)

Advanced box scores

Get advanced box score data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer gameId = 56; // Integer | Game id parameters
    try {
      BoxScore result = apiInstance.getAdvancedBoxScore(gameId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getAdvancedBoxScore");
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
| **gameId** | **Integer**| Game id parameters | |

### Return type

[**BoxScore**](BoxScore.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getCalendar"></a>
# **getCalendar**
> List&lt;Week&gt; getCalendar(year)

Season calendar

Get calendar of weeks by season

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    try {
      List<Week> result = apiInstance.getCalendar(year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getCalendar");
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

[**List&lt;Week&gt;**](Week.md)

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

<a id="getGameMedia"></a>
# **getGameMedia**
> List&lt;GameMedia&gt; getGameMedia(year, week, seasonType, team, conference, mediaType, classification)

Game media information and schedules

Game media information (TV, radio, etc)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    Integer week = 56; // Integer | Week filter
    String seasonType = "seasonType_example"; // String | Season type filter (regular, postseason, or both)
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference filter
    String mediaType = "mediaType_example"; // String | Media type filter (tv, radio, web, ppv, or mobile)
    String classification = "classification_example"; // String | Division classification filter (fbs/fcs/ii/iii)
    try {
      List<GameMedia> result = apiInstance.getGameMedia(year, week, seasonType, team, conference, mediaType, classification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getGameMedia");
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
| **week** | **Integer**| Week filter | [optional] |
| **seasonType** | **String**| Season type filter (regular, postseason, or both) | [optional] |
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference filter | [optional] |
| **mediaType** | **String**| Media type filter (tv, radio, web, ppv, or mobile) | [optional] |
| **classification** | **String**| Division classification filter (fbs/fcs/ii/iii) | [optional] |

### Return type

[**List&lt;GameMedia&gt;**](GameMedia.md)

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

<a id="getGameWeather"></a>
# **getGameWeather**
> List&lt;GameWeather&gt; getGameWeather(gameId, year, week, seasonType, team, conference, classification)

Game weather information (Patreon only)

Weather information for the hour of kickoff

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer gameId = 56; // Integer | Game id filter (required if no year)
    Integer year = 56; // Integer | Year filter (required if no game id)
    Integer week = 56; // Integer | Week filter
    String seasonType = "seasonType_example"; // String | Season type filter (regular, postseason, or both)
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference filter
    String classification = "classification_example"; // String | Division classification filter (fbs/fcs/ii/iii)
    try {
      List<GameWeather> result = apiInstance.getGameWeather(gameId, year, week, seasonType, team, conference, classification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getGameWeather");
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
| **gameId** | **Integer**| Game id filter (required if no year) | [optional] |
| **year** | **Integer**| Year filter (required if no game id) | [optional] |
| **week** | **Integer**| Week filter | [optional] |
| **seasonType** | **String**| Season type filter (regular, postseason, or both) | [optional] |
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference filter | [optional] |
| **classification** | **String**| Division classification filter (fbs/fcs/ii/iii) | [optional] |

### Return type

[**List&lt;GameWeather&gt;**](GameWeather.md)

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

<a id="getGames"></a>
# **getGames**
> List&lt;Game&gt; getGames(year, week, seasonType, team, home, away, conference, division, id)

Games and results

Get game results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer year = 56; // Integer | Year/season filter for games
    Integer week = 56; // Integer | Week filter
    String seasonType = "regular"; // String | Season type filter (regular or postseason)
    String team = "team_example"; // String | Team
    String home = "home_example"; // String | Home team filter
    String away = "away_example"; // String | Away team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    String division = "division_example"; // String | Division classification filter (fbs/fcs/ii/iii)
    Integer id = 56; // Integer | id filter for querying a single game
    try {
      List<Game> result = apiInstance.getGames(year, week, seasonType, team, home, away, conference, division, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getGames");
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
| **team** | **String**| Team | [optional] |
| **home** | **String**| Home team filter | [optional] |
| **away** | **String**| Away team filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |
| **division** | **String**| Division classification filter (fbs/fcs/ii/iii) | [optional] |
| **id** | **Integer**| id filter for querying a single game | [optional] |

### Return type

[**List&lt;Game&gt;**](Game.md)

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

<a id="getPlayerGameStats"></a>
# **getPlayerGameStats**
> List&lt;PlayerGame&gt; getPlayerGameStats(year, week, seasonType, team, conference, category, gameId)

Player game stats

Player stats broken down by game

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer year = 56; // Integer | Year/season filter for games
    Integer week = 56; // Integer | Week filter
    String seasonType = "regular"; // String | Season type filter (regular or postseason)
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    String category = "category_example"; // String | Category filter (e.g defensive)
    Integer gameId = 56; // Integer | Game id filter
    try {
      List<PlayerGame> result = apiInstance.getPlayerGameStats(year, week, seasonType, team, conference, category, gameId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getPlayerGameStats");
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
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |
| **category** | **String**| Category filter (e.g defensive) | [optional] |
| **gameId** | **Integer**| Game id filter | [optional] |

### Return type

[**List&lt;PlayerGame&gt;**](PlayerGame.md)

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

<a id="getScoreboard"></a>
# **getScoreboard**
> List&lt;ScoreboardGame&gt; getScoreboard(classification, conference)

Live game results (Patreon only)

Get live game results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    String classification = "classification_example"; // String | Classification filter (fbs, fcs, ii, or iii). Defaults to fbs.
    String conference = "conference_example"; // String | Conference abbreviation filter.
    try {
      List<ScoreboardGame> result = apiInstance.getScoreboard(classification, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getScoreboard");
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
| **classification** | **String**| Classification filter (fbs, fcs, ii, or iii). Defaults to fbs. | [optional] |
| **conference** | **String**| Conference abbreviation filter. | [optional] |

### Return type

[**List&lt;ScoreboardGame&gt;**](ScoreboardGame.md)

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

<a id="getTeamGameStats"></a>
# **getTeamGameStats**
> List&lt;TeamGame&gt; getTeamGameStats(year, week, seasonType, team, conference, gameId, classification)

Team game stats

Team stats broken down by game

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer year = 56; // Integer | Year/season filter for games
    Integer week = 56; // Integer | Week filter
    String seasonType = "regular"; // String | Season type filter (regular or postseason)
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    Integer gameId = 56; // Integer | Game id filter
    String classification = "classification_example"; // String | Division classification filter (fbs/fcs/ii/iii)
    try {
      List<TeamGame> result = apiInstance.getTeamGameStats(year, week, seasonType, team, conference, gameId, classification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getTeamGameStats");
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
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |
| **gameId** | **Integer**| Game id filter | [optional] |
| **classification** | **String**| Division classification filter (fbs/fcs/ii/iii) | [optional] |

### Return type

[**List&lt;TeamGame&gt;**](TeamGame.md)

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

<a id="getTeamRecords"></a>
# **getTeamRecords**
> List&lt;TeamRecord&gt; getTeamRecords(year, team, conference)

Team records

Get team records by year

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GamesApi apiInstance = new GamesApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference filter
    try {
      List<TeamRecord> result = apiInstance.getTeamRecords(year, team, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#getTeamRecords");
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
| **conference** | **String**| Conference filter | [optional] |

### Return type

[**List&lt;TeamRecord&gt;**](TeamRecord.md)

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

