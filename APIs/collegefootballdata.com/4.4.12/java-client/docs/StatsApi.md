# StatsApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAdvancedTeamGameStats**](StatsApi.md#getAdvancedTeamGameStats) | **GET** /stats/game/advanced | Advanced team metrics by game |
| [**getAdvancedTeamSeasonStats**](StatsApi.md#getAdvancedTeamSeasonStats) | **GET** /stats/season/advanced | Advanced team metrics by season |
| [**getStatCategories**](StatsApi.md#getStatCategories) | **GET** /stats/categories | Team stat categories |
| [**getTeamSeasonStats**](StatsApi.md#getTeamSeasonStats) | **GET** /stats/season | Team statistics by season |


<a id="getAdvancedTeamGameStats"></a>
# **getAdvancedTeamGameStats**
> List&lt;AdvancedGameStat&gt; getAdvancedTeamGameStats(year, week, team, opponent, excludeGarbageTime, seasonType)

Advanced team metrics by game

Advanced team game stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    StatsApi apiInstance = new StatsApi(defaultClient);
    Integer year = 56; // Integer | Year filter (required if no team specified)
    Integer week = 56; // Integer | Week filter
    String team = "team_example"; // String | Team filter (required if no year specified)
    String opponent = "opponent_example"; // String | Opponent filter
    Boolean excludeGarbageTime = true; // Boolean | Filter to remove garbage time plays from calculations
    String seasonType = "seasonType_example"; // String | Season type filter (regular, postseason, or both)
    try {
      List<AdvancedGameStat> result = apiInstance.getAdvancedTeamGameStats(year, week, team, opponent, excludeGarbageTime, seasonType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#getAdvancedTeamGameStats");
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
| **year** | **Integer**| Year filter (required if no team specified) | [optional] |
| **week** | **Integer**| Week filter | [optional] |
| **team** | **String**| Team filter (required if no year specified) | [optional] |
| **opponent** | **String**| Opponent filter | [optional] |
| **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] |
| **seasonType** | **String**| Season type filter (regular, postseason, or both) | [optional] |

### Return type

[**List&lt;AdvancedGameStat&gt;**](AdvancedGameStat.md)

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

<a id="getAdvancedTeamSeasonStats"></a>
# **getAdvancedTeamSeasonStats**
> List&lt;AdvancedSeasonStat&gt; getAdvancedTeamSeasonStats(year, team, excludeGarbageTime, startWeek, endWeek)

Advanced team metrics by season

Advanced team season stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    StatsApi apiInstance = new StatsApi(defaultClient);
    Integer year = 56; // Integer | Year filter (required if no team specified)
    String team = "team_example"; // String | Team filter (required if no year specified)
    Boolean excludeGarbageTime = true; // Boolean | Filter to remove garbage time plays from calculations
    Integer startWeek = 56; // Integer | Starting week filter
    Integer endWeek = 56; // Integer | Starting week filter
    try {
      List<AdvancedSeasonStat> result = apiInstance.getAdvancedTeamSeasonStats(year, team, excludeGarbageTime, startWeek, endWeek);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#getAdvancedTeamSeasonStats");
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
| **year** | **Integer**| Year filter (required if no team specified) | [optional] |
| **team** | **String**| Team filter (required if no year specified) | [optional] |
| **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] |
| **startWeek** | **Integer**| Starting week filter | [optional] |
| **endWeek** | **Integer**| Starting week filter | [optional] |

### Return type

[**List&lt;AdvancedSeasonStat&gt;**](AdvancedSeasonStat.md)

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

<a id="getStatCategories"></a>
# **getStatCategories**
> List&lt;String&gt; getStatCategories()

Team stat categories

Stat category list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    StatsApi apiInstance = new StatsApi(defaultClient);
    try {
      List<String> result = apiInstance.getStatCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#getStatCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getTeamSeasonStats"></a>
# **getTeamSeasonStats**
> List&lt;TeamSeasonStat&gt; getTeamSeasonStats(year, team, conference, startWeek, endWeek)

Team statistics by season

Team season stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    StatsApi apiInstance = new StatsApi(defaultClient);
    Integer year = 56; // Integer | Year filter (required if no team specified)
    String team = "team_example"; // String | Team filter (required if no year specified)
    String conference = "conference_example"; // String | Conference abbreviation filter
    Integer startWeek = 56; // Integer | Starting week filter
    Integer endWeek = 56; // Integer | Starting week filter
    try {
      List<TeamSeasonStat> result = apiInstance.getTeamSeasonStats(year, team, conference, startWeek, endWeek);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#getTeamSeasonStats");
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
| **year** | **Integer**| Year filter (required if no team specified) | [optional] |
| **team** | **String**| Team filter (required if no year specified) | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |
| **startWeek** | **Integer**| Starting week filter | [optional] |
| **endWeek** | **Integer**| Starting week filter | [optional] |

### Return type

[**List&lt;TeamSeasonStat&gt;**](TeamSeasonStat.md)

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

