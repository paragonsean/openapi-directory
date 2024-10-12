# MetricsApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGamePPA**](MetricsApi.md#getGamePPA) | **GET** /ppa/games | Team Predicated Points Added (PPA/EPA) by game |
| [**getPlayerGamePPA**](MetricsApi.md#getPlayerGamePPA) | **GET** /ppa/players/games | Player Predicated Points Added (PPA/EPA) broken down by game |
| [**getPlayerSeasonPPA**](MetricsApi.md#getPlayerSeasonPPA) | **GET** /ppa/players/season | Player Predicated Points Added (PPA/EPA) broken down by season |
| [**getPredictedPoints**](MetricsApi.md#getPredictedPoints) | **GET** /ppa/predicted | Predicted Points (i.e. Expected Points or EP) |
| [**getPregameWinProbabilities**](MetricsApi.md#getPregameWinProbabilities) | **GET** /metrics/wp/pregame | Pregame win probability data |
| [**getTeamPPA**](MetricsApi.md#getTeamPPA) | **GET** /ppa/teams | Predicted Points Added (PPA/EPA) data by team |
| [**getWinProbabilityData**](MetricsApi.md#getWinProbabilityData) | **GET** /metrics/wp | Win probability chart data |


<a id="getGamePPA"></a>
# **getGamePPA**
> List&lt;GamePPA&gt; getGamePPA(year, week, team, conference, excludeGarbageTime, seasonType)

Team Predicated Points Added (PPA/EPA) by game

Predicted Points Added (PPA) by game

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    Integer week = 56; // Integer | Week filter
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference filter
    Boolean excludeGarbageTime = true; // Boolean | Filter to remove garbage time plays from calculations
    String seasonType = "regular"; // String | Season type filter (regular or postseason)
    try {
      List<GamePPA> result = apiInstance.getGamePPA(year, week, team, conference, excludeGarbageTime, seasonType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getGamePPA");
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
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference filter | [optional] |
| **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] |
| **seasonType** | **String**| Season type filter (regular or postseason) | [optional] [default to regular] |

### Return type

[**List&lt;GamePPA&gt;**](GamePPA.md)

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

<a id="getPlayerGamePPA"></a>
# **getPlayerGamePPA**
> List&lt;PlayerGamePPA&gt; getPlayerGamePPA(year, week, team, position, playerId, threshold, excludeGarbageTime, seasonType)

Player Predicated Points Added (PPA/EPA) broken down by game

Predicted Points Added (PPA) by player game

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    Integer week = 56; // Integer | Week filter
    String team = "team_example"; // String | Team filter
    String position = "position_example"; // String | Position abbreviation filter
    Integer playerId = 56; // Integer | Player id filter
    String threshold = "threshold_example"; // String | Minimum play threshold filter
    Boolean excludeGarbageTime = true; // Boolean | Filter to remove garbage time plays from calculations
    String seasonType = "regular"; // String | Season type filter (regular or postseason)
    try {
      List<PlayerGamePPA> result = apiInstance.getPlayerGamePPA(year, week, team, position, playerId, threshold, excludeGarbageTime, seasonType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getPlayerGamePPA");
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
| **week** | **Integer**| Week filter | [optional] |
| **team** | **String**| Team filter | [optional] |
| **position** | **String**| Position abbreviation filter | [optional] |
| **playerId** | **Integer**| Player id filter | [optional] |
| **threshold** | **String**| Minimum play threshold filter | [optional] |
| **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] |
| **seasonType** | **String**| Season type filter (regular or postseason) | [optional] [default to regular] |

### Return type

[**List&lt;PlayerGamePPA&gt;**](PlayerGamePPA.md)

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

<a id="getPlayerSeasonPPA"></a>
# **getPlayerSeasonPPA**
> List&lt;PlayerSeasonPPA&gt; getPlayerSeasonPPA(year, team, conference, position, playerId, threshold, excludeGarbageTime)

Player Predicated Points Added (PPA/EPA) broken down by season

Predicted Points Added (PPA) by player season

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    String position = "position_example"; // String | Position abbreviation filter
    Integer playerId = 56; // Integer | Player id filter
    String threshold = "threshold_example"; // String | Minimum play threshold filter
    Boolean excludeGarbageTime = true; // Boolean | Filter to remove garbage time plays from calculations
    try {
      List<PlayerSeasonPPA> result = apiInstance.getPlayerSeasonPPA(year, team, conference, position, playerId, threshold, excludeGarbageTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getPlayerSeasonPPA");
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
| **position** | **String**| Position abbreviation filter | [optional] |
| **playerId** | **Integer**| Player id filter | [optional] |
| **threshold** | **String**| Minimum play threshold filter | [optional] |
| **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] |

### Return type

[**List&lt;PlayerSeasonPPA&gt;**](PlayerSeasonPPA.md)

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

<a id="getPredictedPoints"></a>
# **getPredictedPoints**
> List&lt;PredictedPoints&gt; getPredictedPoints(down, distance)

Predicted Points (i.e. Expected Points or EP)

Predicted Points

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer down = 56; // Integer | Down filter
    Integer distance = 56; // Integer | Distance filter
    try {
      List<PredictedPoints> result = apiInstance.getPredictedPoints(down, distance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getPredictedPoints");
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
| **down** | **Integer**| Down filter | |
| **distance** | **Integer**| Distance filter | |

### Return type

[**List&lt;PredictedPoints&gt;**](PredictedPoints.md)

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

<a id="getPregameWinProbabilities"></a>
# **getPregameWinProbabilities**
> List&lt;PregameWP&gt; getPregameWinProbabilities(year, week, team, seasonType)

Pregame win probability data

Pregame win probabilities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    Integer week = 56; // Integer | Week filter
    String team = "team_example"; // String | Team filter
    String seasonType = "seasonType_example"; // String | regular or postseason
    try {
      List<PregameWP> result = apiInstance.getPregameWinProbabilities(year, week, team, seasonType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getPregameWinProbabilities");
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
| **week** | **Integer**| Week filter | [optional] |
| **team** | **String**| Team filter | [optional] |
| **seasonType** | **String**| regular or postseason | [optional] |

### Return type

[**List&lt;PregameWP&gt;**](PregameWP.md)

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

<a id="getTeamPPA"></a>
# **getTeamPPA**
> List&lt;TeamPPA&gt; getTeamPPA(year, team, conference, excludeGarbageTime)

Predicted Points Added (PPA/EPA) data by team

Predicted Points Added (PPA)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer year = 56; // Integer | Year filter (required if team not specified)
    String team = "team_example"; // String | Team filter (required if year not specified)
    String conference = "conference_example"; // String | Conference filter
    Boolean excludeGarbageTime = true; // Boolean | Filter to remove garbage time plays from calculations
    try {
      List<TeamPPA> result = apiInstance.getTeamPPA(year, team, conference, excludeGarbageTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getTeamPPA");
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
| **year** | **Integer**| Year filter (required if team not specified) | [optional] |
| **team** | **String**| Team filter (required if year not specified) | [optional] |
| **conference** | **String**| Conference filter | [optional] |
| **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] |

### Return type

[**List&lt;TeamPPA&gt;**](TeamPPA.md)

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

<a id="getWinProbabilityData"></a>
# **getWinProbabilityData**
> List&lt;PlayWP&gt; getWinProbabilityData(gameId)

Win probability chart data

Win probability data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer gameId = 56; // Integer | Game id filter
    try {
      List<PlayWP> result = apiInstance.getWinProbabilityData(gameId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getWinProbabilityData");
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
| **gameId** | **Integer**| Game id filter | |

### Return type

[**List&lt;PlayWP&gt;**](PlayWP.md)

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

