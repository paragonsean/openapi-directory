# PlaysApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLivePlays**](PlaysApi.md#getLivePlays) | **GET** /live/plays | Live metrics and PBP (Patreon only) |
| [**getPlayStatTypes**](PlaysApi.md#getPlayStatTypes) | **GET** /play/stat/types | Types of player play stats |
| [**getPlayStats**](PlaysApi.md#getPlayStats) | **GET** /play/stats | Play stats by play |
| [**getPlayTypes**](PlaysApi.md#getPlayTypes) | **GET** /play/types | Play types |
| [**getPlays**](PlaysApi.md#getPlays) | **GET** /plays | Play by play data |


<a id="getLivePlays"></a>
# **getLivePlays**
> LivePlayByPlay getLivePlays(id)

Live metrics and PBP (Patreon only)

Get live metrics and PBP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlaysApi apiInstance = new PlaysApi(defaultClient);
    Integer id = 56; // Integer | Game id
    try {
      LivePlayByPlay result = apiInstance.getLivePlays(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaysApi#getLivePlays");
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
| **id** | **Integer**| Game id | |

### Return type

[**LivePlayByPlay**](LivePlayByPlay.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getPlayStatTypes"></a>
# **getPlayStatTypes**
> List&lt;PlayStatType&gt; getPlayStatTypes()

Types of player play stats

Type of play stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlaysApi apiInstance = new PlaysApi(defaultClient);
    try {
      List<PlayStatType> result = apiInstance.getPlayStatTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaysApi#getPlayStatTypes");
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

[**List&lt;PlayStatType&gt;**](PlayStatType.md)

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

<a id="getPlayStats"></a>
# **getPlayStats**
> List&lt;PlayStat&gt; getPlayStats(year, week, team, gameId, athleteId, statTypeId, seasonType, conference)

Play stats by play

Gets player stats associated by play (limit 1000)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlaysApi apiInstance = new PlaysApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    Integer week = 56; // Integer | Week filter
    String team = "team_example"; // String | Team filter
    Integer gameId = 56; // Integer | gameId filter (from /games endpoint)
    Integer athleteId = 56; // Integer | athleteId filter (from /roster endpoint)
    Integer statTypeId = 56; // Integer | statTypeId filter (from /play/stat/types endpoint)
    String seasonType = "seasonType_example"; // String | regular, postseason, or both
    String conference = "conference_example"; // String | conference abbreviation filter
    try {
      List<PlayStat> result = apiInstance.getPlayStats(year, week, team, gameId, athleteId, statTypeId, seasonType, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaysApi#getPlayStats");
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
| **gameId** | **Integer**| gameId filter (from /games endpoint) | [optional] |
| **athleteId** | **Integer**| athleteId filter (from /roster endpoint) | [optional] |
| **statTypeId** | **Integer**| statTypeId filter (from /play/stat/types endpoint) | [optional] |
| **seasonType** | **String**| regular, postseason, or both | [optional] |
| **conference** | **String**| conference abbreviation filter | [optional] |

### Return type

[**List&lt;PlayStat&gt;**](PlayStat.md)

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

<a id="getPlayTypes"></a>
# **getPlayTypes**
> List&lt;PlayType&gt; getPlayTypes()

Play types

Types of plays

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlaysApi apiInstance = new PlaysApi(defaultClient);
    try {
      List<PlayType> result = apiInstance.getPlayTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaysApi#getPlayTypes");
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

[**List&lt;PlayType&gt;**](PlayType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getPlays"></a>
# **getPlays**
> List&lt;Play&gt; getPlays(year, week, seasonType, team, offense, defense, conference, offenseConference, defenseConference, playType, classification)

Play by play data

Get play data and results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PlaysApi apiInstance = new PlaysApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    Integer week = 56; // Integer | Week filter (required if team, offense, or defense, not specified)
    String seasonType = "regular"; // String | Season type filter
    String team = "team_example"; // String | Team filter
    String offense = "offense_example"; // String | Offensive team filter
    String defense = "defense_example"; // String | Defensive team filter
    String conference = "conference_example"; // String | Conference filter
    String offenseConference = "offenseConference_example"; // String | Offensive conference filter
    String defenseConference = "defenseConference_example"; // String | Defensive conference filter
    Integer playType = 56; // Integer | Play type filter
    String classification = "classification_example"; // String | Division classification filter (fbs/fcs/ii/iii)
    try {
      List<Play> result = apiInstance.getPlays(year, week, seasonType, team, offense, defense, conference, offenseConference, defenseConference, playType, classification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaysApi#getPlays");
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
| **week** | **Integer**| Week filter (required if team, offense, or defense, not specified) | |
| **seasonType** | **String**| Season type filter | [optional] [default to regular] |
| **team** | **String**| Team filter | [optional] |
| **offense** | **String**| Offensive team filter | [optional] |
| **defense** | **String**| Defensive team filter | [optional] |
| **conference** | **String**| Conference filter | [optional] |
| **offenseConference** | **String**| Offensive conference filter | [optional] |
| **defenseConference** | **String**| Defensive conference filter | [optional] |
| **playType** | **Integer**| Play type filter | [optional] |
| **classification** | **String**| Division classification filter (fbs/fcs/ii/iii) | [optional] |

### Return type

[**List&lt;Play&gt;**](Play.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

