# DefaultApi

All URIs are relative to *https://www.haloapi.com/stats*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**halo5Company**](DefaultApi.md#halo5Company) | **GET** /h5/companies/{companyId} | Halo 5 - Company |
| [**halo5CompanyCommendations**](DefaultApi.md#halo5CompanyCommendations) | **GET** /h5/companies/{companyId}/commendations | Halo 5 - Company Commendations |
| [**halo5LeaderboardPlayerCSR**](DefaultApi.md#halo5LeaderboardPlayerCSR) | **GET** /h5/player-leaderboards/csr/{seasonId}/{playlistId} | Halo 5 - Leaderboard - Player CSR |
| [**halo5MatchEvents**](DefaultApi.md#halo5MatchEvents) | **GET** /h5/matches/{matchId}/events | Halo 5 - Match Events |
| [**halo5MatchResultArena**](DefaultApi.md#halo5MatchResultArena) | **GET** /h5/arena/matches/{matchId} | Halo 5 - Match Result - Arena |
| [**halo5MatchResultCampaign**](DefaultApi.md#halo5MatchResultCampaign) | **GET** /h5/campaign/matches/{matchId} | Halo 5 - Match Result - Campaign |
| [**halo5MatchResultCustom**](DefaultApi.md#halo5MatchResultCustom) | **GET** /h5/custom/matches/{matchId} | Halo 5 - Match Result - Custom |
| [**halo5MatchResultCustomLocal**](DefaultApi.md#halo5MatchResultCustomLocal) | **GET** /h5/customlocal/matches/{matchId} | Halo 5 - Match Result - Custom Local |
| [**halo5MatchResultWarzone**](DefaultApi.md#halo5MatchResultWarzone) | **GET** /h5/warzone/matches/{matchId} | Halo 5 - Match Result - Warzone |
| [**halo5PCMatchResultCustom**](DefaultApi.md#halo5PCMatchResultCustom) | **GET** /h5pc/custom/matches/{matchId} | Halo 5 PC - Match Result - Custom |
| [**halo5PCPlayerMatchHistory**](DefaultApi.md#halo5PCPlayerMatchHistory) | **GET** /h5pc/players/{player}/matches | Halo 5 PC - Player Match History |
| [**halo5PCPlayerServiceRecordsCustom**](DefaultApi.md#halo5PCPlayerServiceRecordsCustom) | **GET** /h5pc/servicerecords/custom | Halo 5 PC - Player Service Records - Custom |
| [**halo5PlayerCommendations**](DefaultApi.md#halo5PlayerCommendations) | **GET** /h5/players/{player}/commendations | Halo 5 - Player Commendations |
| [**halo5PlayerMatchHistory**](DefaultApi.md#halo5PlayerMatchHistory) | **GET** /h5/players/{player}/matches | Halo 5 - Player Match History |
| [**halo5PlayerServiceRecordsArena**](DefaultApi.md#halo5PlayerServiceRecordsArena) | **GET** /h5/servicerecords/arena | Halo 5 - Player Service Records - Arena |
| [**halo5PlayerServiceRecordsCampaign**](DefaultApi.md#halo5PlayerServiceRecordsCampaign) | **GET** /h5/servicerecords/campaign | Halo 5 - Player Service Records - Campaign |
| [**halo5PlayerServiceRecordsCustom**](DefaultApi.md#halo5PlayerServiceRecordsCustom) | **GET** /h5/servicerecords/custom | Halo 5 - Player Service Records - Custom |
| [**halo5PlayerServiceRecordsCustomLocal**](DefaultApi.md#halo5PlayerServiceRecordsCustomLocal) | **GET** /h5/servicerecords/customlocal | Halo 5 - Player Service Records - Custom Local |
| [**halo5PlayerServiceRecordsWarzone**](DefaultApi.md#halo5PlayerServiceRecordsWarzone) | **GET** /h5/servicerecords/warzone | Halo 5 - Player Service Records - Warzone |
| [**haloWars2LeaderboardPlayerCSR**](DefaultApi.md#haloWars2LeaderboardPlayerCSR) | **GET** /hw2/player-leaderboards/csr/{seasonId}/{playlistId} | Halo Wars 2 - Leaderboard - Player CSR |
| [**haloWars2MatchEvents**](DefaultApi.md#haloWars2MatchEvents) | **GET** /hw2/matches/{matchId}/events | Halo Wars 2 - Match Events |
| [**haloWars2MatchResult**](DefaultApi.md#haloWars2MatchResult) | **GET** /hw2/matches/{matchId} | Halo Wars 2 - Match Result |
| [**haloWars2PlayerCampaignProgress**](DefaultApi.md#haloWars2PlayerCampaignProgress) | **GET** /hw2/players/{player}/campaign-progress | Halo Wars 2 - Player Campaign Progress |
| [**haloWars2PlayerMatchHistory**](DefaultApi.md#haloWars2PlayerMatchHistory) | **GET** /hw2/players/{player}/matches | Halo Wars 2 - Player Match History |
| [**haloWars2PlayerPlaylistRatings**](DefaultApi.md#haloWars2PlayerPlaylistRatings) | **GET** /hw2/playlist/{playlistId}/rating | Halo Wars 2 - Player Playlist Ratings |
| [**haloWars2PlayerSeasonStatsSummary**](DefaultApi.md#haloWars2PlayerSeasonStatsSummary) | **GET** /hw2/players/{player}/stats/seasons/{seasonId} | Halo Wars 2 - Player Season Stats Summary |
| [**haloWars2PlayerStatsSummary**](DefaultApi.md#haloWars2PlayerStatsSummary) | **GET** /hw2/players/{player}/stats | Halo Wars 2 - Player Stats Summary |
| [**haloWars2PlayerXPs**](DefaultApi.md#haloWars2PlayerXPs) | **GET** /hw2/xp | Halo Wars 2 - Player XPs |


<a id="halo5Company"></a>
# **halo5Company**
> halo5Company(companyId)

Halo 5 - Company

&lt;p&gt;Retrieves information about the Company. The response will contain the Company&#39;s name, status, and members.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String companyId = "companyId_example"; // String | The ID for the Company. The Company ID for a player can be retrieved from the Profile APIs via the \"Halo 5 - Player Apperance\" Endpoint.
    try {
      apiInstance.halo5Company(companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5Company");
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
| **companyId** | **String**| The ID for the Company. The Company ID for a player can be retrieved from the Profile APIs via the \&quot;Halo 5 - Player Apperance\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Company name, status, and members. |  -  |
| **404** | Specified Company was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5CompanyCommendations"></a>
# **halo5CompanyCommendations**
> halo5CompanyCommendations(companyId)

Halo 5 - Company Commendations

&lt;p&gt;Retrieves the commendation state for a Company.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String companyId = "companyId_example"; // String | The ID for the Company. The Company ID for a player can be retrieved from the Profile APIs via the \"Halo 5 - Player Apperance\" Endpoint.
    try {
      apiInstance.halo5CompanyCommendations(companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5CompanyCommendations");
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
| **companyId** | **String**| The ID for the Company. The Company ID for a player can be retrieved from the Profile APIs via the \&quot;Halo 5 - Player Apperance\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the commendation state for the Company. |  -  |
| **404** | Specified Company was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5LeaderboardPlayerCSR"></a>
# **halo5LeaderboardPlayerCSR**
> halo5LeaderboardPlayerCSR(seasonId, playlistId, count)

Halo 5 - Leaderboard - Player CSR

&lt;p&gt;Retrieves the Leaderboard for Player CSRs. The Leaderboard consists of the top Players with a CSR of 1800 or above for a given Playlist in a Season.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;March 6, 2018:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Fixed documentation typos for the names of the \&quot;Player\&quot; and \&quot;Gamertag\&quot; properties.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 31, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Clarified documentation for which players are included in the leaderboard.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Player Leaderboard\&quot; to \&quot;Halo 5 - Leaderboard Player CSR\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String seasonId = "seasonId_example"; // String | The ID for the Season.
    String playlistId = "playlistId_example"; // String | The ID for the Playlist.
    BigDecimal count = new BigDecimal(78); // BigDecimal | When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 200 is assumed.  When the value contains a non-digit or is exactly \"0\", HTTP 400 (\"Bad Request\") is returned.  When the value is greater than the allowed range [1,250], the maximum allowed value is used instead.  The \"Count\" field in the response will confirm the actual value that was used.
    try {
      apiInstance.halo5LeaderboardPlayerCSR(seasonId, playlistId, count);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5LeaderboardPlayerCSR");
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
| **seasonId** | **String**| The ID for the Season. | |
| **playlistId** | **String**| The ID for the Playlist. | |
| **count** | **BigDecimal**| When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 200 is assumed.  When the value contains a non-digit or is exactly \&quot;0\&quot;, HTTP 400 (\&quot;Bad Request\&quot;) is returned.  When the value is greater than the allowed range [1,250], the maximum allowed value is used instead.  The \&quot;Count\&quot; field in the response will confirm the actual value that was used. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Players in the Leaderboard. An empty list will be returned if no Players are in the Leaderboard. |  -  |
| **404** | The Season does not exist, or the Playlist either does not exist or is not part of the given Season. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5MatchEvents"></a>
# **halo5MatchEvents**
> halo5MatchEvents(matchId)

Halo 5 - Match Events

&lt;p&gt;Retrieves a set of Events related to the Match specified. Events are only available once the Match has completed.&lt;/p&gt; &lt;p&gt;The set of Events may grow over time as data becomes available.&lt;/p&gt; &lt;p&gt;This Endpoint does not have the accuracy guarantees of other Endpoints have, so please use with caution. This endpoint may not return Matches before December 1, 2015.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Events for Match\&quot; to \&quot;Halo 5 - Match Events\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;May 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;The Endpoint now correctly reports the \&quot;Content-Type\&quot; Response Header as \&quot;application/json\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;May 16, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented HTTP 503 Response Code.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added new types of events to the Endpoint: Impulses, Medals, Player Spawns, Round Stats, Round Ends, Weapon Drops, Weapon Pickups, and Weapon Pickup Pads.&lt;/li&gt;         &lt;li&gt;Fixed an issue that caused the API to consistently return HTTP 500&#39;s for matches where a player left and rejoined the match.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo 5 - Player Match History\" Endpoint.
    try {
      apiInstance.halo5MatchEvents(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5MatchEvents");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo 5 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Events. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5MatchResultArena"></a>
# **halo5MatchResultArena**
> halo5MatchResultArena(matchId)

Halo 5 - Match Result - Arena

&lt;p&gt;Retrieves detailed statistics for a Match with the Arena Game Mode.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 12, 2018:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Updated the documentation for \&quot;PlayerScore\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Post-Game Carnage Report: Arena\&quot; to \&quot;Halo 5 - Match Result - Arena\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;         &lt;li&gt;Updated the documentation for \&quot;GameVariantResourceId\&quot; and \&quot;MapVariantResourceId\&quot; to reference the UGC API.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;May 16, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented HTTP 503 Response Code.&lt;/li&gt;         &lt;li&gt;Added documentation for the \&quot;MatchSpeedWinAmount\&quot;, \&quot;ObjectivesCompletedAmount\&quot;, and \&quot;BoostData\&quot; fields.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added documentation for the \&quot;GameVariantResourceId\&quot;, \&quot;MapVariantResourceId\&quot;, and \&quot;PlayerScore\&quot; fields.&lt;/li&gt;         &lt;li&gt;Updated the documentation for the \&quot;MapVariantId\&quot; and \&quot;GameVariantId\&quot; fields with the recommendation of using the \&quot;MapVariantResourceId\&quot; and \&quot;GameVariantResourceId\&quot; fields, respectively.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo 5 - Player Match History\" Endpoint.
    try {
      apiInstance.halo5MatchResultArena(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5MatchResultArena");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo 5 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Result. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5MatchResultCampaign"></a>
# **halo5MatchResultCampaign**
> halo5MatchResultCampaign(matchId)

Halo 5 - Match Result - Campaign

&lt;p&gt;Retrieves detailed statistics for a Match with the Campaign Game Mode.&lt;/p&gt; &lt;p&gt;Every time a player plays a portion of a Campaign Mission, a Match will be generated whether the player finishes the Mission or not. If the \&quot;Match\&quot; ends because the Mission was completed, this will be indicated in the response.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Post-Game Carnage Report: Campaign\&quot; to \&quot;Halo 5 - Match Result - Campaign\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;May 16, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented HTTP 503 Response Code.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added documentation for the \&quot;GameVariantResourceId\&quot;, \&quot;MapVariantResourceId\&quot;, and \&quot;PlayerScore\&quot; fields.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo 5 - Player Match History\" Endpoint.
    try {
      apiInstance.halo5MatchResultCampaign(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5MatchResultCampaign");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo 5 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Result. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5MatchResultCustom"></a>
# **halo5MatchResultCustom**
> halo5MatchResultCustom(matchId)

Halo 5 - Match Result - Custom

&lt;p&gt;Retrieves detailed statistics for a Match with the Custom Game Mode. Games with the Custom Game Mode are played on Xbox Live Servers. For games played on Local Servers, use the \&quot;Halo 5 - Match Result - Custom Local\&quot; Endpoint.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 12, 2018:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Updated the documentation for \&quot;PlayerScore\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;         &lt;li&gt;Added documentation for \&quot;PresentInMatch\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Post-Game Carnage Report: Custom\&quot; to \&quot;Halo 5 - Match Result - Custom\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;         &lt;li&gt;Updated the documentation for \&quot;GameVariantResourceId\&quot; and \&quot;MapVariantResourceId\&quot; to reference the UGC API.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;May 16, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented HTTP 503 Response Code.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added documentation for the \&quot;GameVariantResourceId\&quot;, \&quot;MapVariantResourceId\&quot;, and \&quot;PlayerScore\&quot; fields.&lt;/li&gt;         &lt;li&gt;Updated the documentation for the \&quot;MapVariantId\&quot; and \&quot;GameVariantId\&quot; fields with the recommendation of using the \&quot;MapVariantResourceId\&quot; and \&quot;GameVariantResourceId\&quot; fields, respectively.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo 5 - Player Match History\" Endpoint.
    try {
      apiInstance.halo5MatchResultCustom(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5MatchResultCustom");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo 5 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Result. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5MatchResultCustomLocal"></a>
# **halo5MatchResultCustomLocal**
> halo5MatchResultCustomLocal(matchId)

Halo 5 - Match Result - Custom Local

&lt;p&gt;Retrieves detailed statistics for a Match with the Custom Local Game Mode. Games with the Custom Local Game Mode are played on Local Servers. For games played on Xbox Live Servers, use the \&quot;Halo 5 - Match Result - Custom\&quot; Endpoint.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 12, 2018:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Updated the documentation for \&quot;PlayerScore\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo 5 - Player Match History\" Endpoint.
    try {
      apiInstance.halo5MatchResultCustomLocal(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5MatchResultCustomLocal");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo 5 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Result. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5MatchResultWarzone"></a>
# **halo5MatchResultWarzone**
> halo5MatchResultWarzone(matchId)

Halo 5 - Match Result - Warzone

&lt;p&gt;Retrieves detailed statistics for a Match with the Warzone Game Mode.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Post-Game Carnage Report: Warzone\&quot; to \&quot;Halo 5 - Match Result - Warzone\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;         &lt;li&gt;Updated the documentation for \&quot;GameVariantResourceId\&quot; and \&quot;MapVariantResourceId\&quot; to reference the UGC API.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;May 16, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented HTTP 503 Response Code.&lt;/li&gt;         &lt;li&gt;Added documentation for the \&quot;MatchSpeedWinAmount\&quot;, \&quot;ObjectivesCompletedAmount\&quot;, and \&quot;BoostData\&quot; fields.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added documentation for the \&quot;GameVariantResourceId\&quot;, \&quot;MapVariantResourceId\&quot;, and \&quot;PlayerScore\&quot; fields.&lt;/li&gt;         &lt;li&gt;Updated the documentation for the \&quot;MapVariantId\&quot; and \&quot;GameVariantId\&quot; fields with the recommendation of using the \&quot;MapVariantResourceId\&quot; and \&quot;GameVariantResourceId\&quot; fields, respectively.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo 5 - Player Match History\" Endpoint.
    try {
      apiInstance.halo5MatchResultWarzone(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5MatchResultWarzone");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo 5 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Result. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PCMatchResultCustom"></a>
# **halo5PCMatchResultCustom**
> halo5PCMatchResultCustom(matchId)

Halo 5 PC - Match Result - Custom

&lt;p&gt;Retrieves detailed statistics for a Match with the Custom Game Mode. Games with the Custom Game Mode are played on Xbox Live Servers. For games played on Local Servers, use the \&quot;Halo 5 - Match Result - Custom Local\&quot; Endpoint.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 12, 2018:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Updated the documentation for \&quot;PlayerScore\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;         &lt;li&gt;Added documentation for \&quot;PresentInMatch\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Post-Game Carnage Report: Custom\&quot; to \&quot;Halo 5 - Match Result - Custom\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;         &lt;li&gt;Updated the documentation for \&quot;GameVariantResourceId\&quot; and \&quot;MapVariantResourceId\&quot; to reference the UGC API.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;May 16, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented HTTP 503 Response Code.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added documentation for the \&quot;GameVariantResourceId\&quot;, \&quot;MapVariantResourceId\&quot;, and \&quot;PlayerScore\&quot; fields.&lt;/li&gt;         &lt;li&gt;Updated the documentation for the \&quot;MapVariantId\&quot; and \&quot;GameVariantId\&quot; fields with the recommendation of using the \&quot;MapVariantResourceId\&quot; and \&quot;GameVariantResourceId\&quot; fields, respectively.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo 5 PC - Player Match History\" Endpoint.
    try {
      apiInstance.halo5PCMatchResultCustom(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PCMatchResultCustom");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo 5 PC - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Result. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PCPlayerMatchHistory"></a>
# **halo5PCPlayerMatchHistory**
> halo5PCPlayerMatchHistory(player, modes, start, count, includeTimes)

Halo 5 PC - Player Match History

&lt;p&gt;Retrieves a list of Matches that the Player has participated in and which have completed processing. If the Player is currently in a match, it is not returned in this API.&lt;/p&gt; &lt;p&gt;This endpoint will include games played on Local Servers with the Custom Local Game Mode for games that occurred or after December 22, 2017.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 1, 2019:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Enabled support for viewing the time component of the \&quot;MatchCompletedDate\&quot; via the \&quot;{include-times}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added support for the Custom Local Game mode.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Matches for Player\&quot; to \&quot;Halo 5 - Player Match History\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Clarified documentation for the \&quot;MapVariant\&quot; and \&quot;GameVariant\&quot; fields.&lt;/li&gt;         &lt;li&gt;Corrected \&quot;OwnerType\&quot; values for the \&quot;MapVariant\&quot; and \&quot;GameVariant\&quot; fields.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String player = "player_example"; // String | The Player's Gamertag.
    String modes = "modes_example"; // String | Indicates what Game Mode(s) the client is interested in getting Matches for (arena, campaign, custom, or warzone).  When the parameter is omitted or empty, Matches from all modes are returned. When a client would like to receive Matches spanning multiple Modes, separate the Modes with a comma (e.g. \"arena,custom\"). There is no significance to the order the Modes are specified in this parameter.  When an invalid Mode is specified, HTTP 400 (\"Bad Request\") is returned.  When a valid Mode is specified more than once, HTTP 400 (\"Bad Request\") is returned.
    BigDecimal start = new BigDecimal(78); // BigDecimal | When specified, this indicates the starting index (0-based) for which the batch of results will begin at. For example, \"start=0\" indicates that the first qualifying result will be returned, no items are 'skipped'. Passing \"start=10\" indicates that the result will begin with the 11th item, the first 10 will be 'skipped'.  When omitted, zero is assumed.  When the value contains a non-digit, HTTP 400 (\"Bad Request\") is returned.
    BigDecimal count = new BigDecimal(78); // BigDecimal | When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 25 is assumed.  When the value contains a non-digit or is exactly \"0\", HTTP 400 (\"Bad Request\") is returned.  When the value is greater than the allowed range [1,25], the maximum allowed value is used instead. The \"Count\" field in the response will confirm the actual value that was used.
    Boolean includeTimes = true; // Boolean | When set to \"true\", this indicates that the time component of the \"MatchCompletedDate\" field should be populated.  Otherwise, when set to \"false\" or when omitted, the time component will be set to \"00:00:00\".  When the value contains a non-boolean, HTTP 400 (\"Bad Request\") is returned.
    try {
      apiInstance.halo5PCPlayerMatchHistory(player, modes, start, count, includeTimes);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PCPlayerMatchHistory");
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
| **player** | **String**| The Player&#39;s Gamertag. | |
| **modes** | **String**| Indicates what Game Mode(s) the client is interested in getting Matches for (arena, campaign, custom, or warzone).  When the parameter is omitted or empty, Matches from all modes are returned. When a client would like to receive Matches spanning multiple Modes, separate the Modes with a comma (e.g. \&quot;arena,custom\&quot;). There is no significance to the order the Modes are specified in this parameter.  When an invalid Mode is specified, HTTP 400 (\&quot;Bad Request\&quot;) is returned.  When a valid Mode is specified more than once, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |
| **start** | **BigDecimal**| When specified, this indicates the starting index (0-based) for which the batch of results will begin at. For example, \&quot;start&#x3D;0\&quot; indicates that the first qualifying result will be returned, no items are &#39;skipped&#39;. Passing \&quot;start&#x3D;10\&quot; indicates that the result will begin with the 11th item, the first 10 will be &#39;skipped&#39;.  When omitted, zero is assumed.  When the value contains a non-digit, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |
| **count** | **BigDecimal**| When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 25 is assumed.  When the value contains a non-digit or is exactly \&quot;0\&quot;, HTTP 400 (\&quot;Bad Request\&quot;) is returned.  When the value is greater than the allowed range [1,25], the maximum allowed value is used instead. The \&quot;Count\&quot; field in the response will confirm the actual value that was used. | [optional] |
| **includeTimes** | **Boolean**| When set to \&quot;true\&quot;, this indicates that the time component of the \&quot;MatchCompletedDate\&quot; field should be populated.  Otherwise, when set to \&quot;false\&quot; or when omitted, the time component will be set to \&quot;00:00:00\&quot;.  When the value contains a non-boolean, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Player&#39;s recent Matches. An empty list will be returned if the Player has not played any Matches in the specified Game Mode(s). |  -  |
| **400** | An unsupported value was provided for a query string parameter. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PCPlayerServiceRecordsCustom"></a>
# **halo5PCPlayerServiceRecordsCustom**
> halo5PCPlayerServiceRecordsCustom(players)

Halo 5 PC - Player Service Records - Custom

&lt;p&gt;Retrieves Service Records for the Custom Game Mode for one or more players. A Service Record contains a player&#39;s lifetime statistics in the Game Mode. Games with the Custom Game Mode are played on Xbox Live Servers. For games played on Local Servers, use the \&quot;Halo 5 - Player Service Records - Custom Local\&quot; Endpoint.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Service Record: Custom\&quot; to \&quot;Halo 5 - Player Service Records - Custom\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 32 Gamertags may be specified.
    try {
      apiInstance.halo5PCPlayerServiceRecordsCustom(players);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PCPlayerServiceRecordsCustom");
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
| **players** | **String**| A comma-separated list of Gamertags. Up to 32 Gamertags may be specified. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Service Records for the requested player(s). |  -  |
| **404** | One or more Gamertags don&#39;t pass validation rules. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PlayerCommendations"></a>
# **halo5PlayerCommendations**
> halo5PlayerCommendations(player)

Halo 5 - Player Commendations

&lt;p&gt;Retrieves the commendation state for a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String player = "player_example"; // String | The Player's Gamertag.
    try {
      apiInstance.halo5PlayerCommendations(player);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerCommendations");
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
| **player** | **String**| The Player&#39;s Gamertag. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the commendation state for the Player. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PlayerMatchHistory"></a>
# **halo5PlayerMatchHistory**
> halo5PlayerMatchHistory(player, modes, start, count, includeTimes)

Halo 5 - Player Match History

&lt;p&gt;Retrieves a list of Matches that the Player has participated in and which have completed processing. If the Player is currently in a match, it is not returned in this API.&lt;/p&gt; &lt;p&gt;This endpoint will include games played on Local Servers with the Custom Local Game Mode for games that occurred or after December 22, 2017.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 1, 2019:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Enabled support for viewing the time component of the \&quot;MatchCompletedDate\&quot; via the \&quot;{include-times}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added support for the Custom Local Game mode.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Matches for Player\&quot; to \&quot;Halo 5 - Player Match History\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Clarified documentation for the \&quot;MapVariant\&quot; and \&quot;GameVariant\&quot; fields.&lt;/li&gt;         &lt;li&gt;Corrected \&quot;OwnerType\&quot; values for the \&quot;MapVariant\&quot; and \&quot;GameVariant\&quot; fields.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String player = "player_example"; // String | The Player's Gamertag.
    String modes = "modes_example"; // String | Indicates what Game Mode(s) the client is interested in getting Matches for (arena, campaign, custom, customlocal, or warzone).  When the parameter is omitted or empty, Matches from all modes are returned. When a client would like to receive Matches spanning multiple Modes, separate the Modes with a comma (e.g. \"arena,custom\"). There is no significance to the order the Modes are specified in this parameter.  When an invalid Mode is specified, HTTP 400 (\"Bad Request\") is returned.  When a valid Mode is specified more than once, HTTP 400 (\"Bad Request\") is returned.
    BigDecimal start = new BigDecimal(78); // BigDecimal | When specified, this indicates the starting index (0-based) for which the batch of results will begin at. For example, \"start=0\" indicates that the first qualifying result will be returned, no items are 'skipped'. Passing \"start=10\" indicates that the result will begin with the 11th item, the first 10 will be 'skipped'.  When omitted, zero is assumed.  When the value contains a non-digit, HTTP 400 (\"Bad Request\") is returned.
    BigDecimal count = new BigDecimal(78); // BigDecimal | When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 25 is assumed.  When the value contains a non-digit or is exactly \"0\", HTTP 400 (\"Bad Request\") is returned.  When the value is greater than the allowed range [1,25], the maximum allowed value is used instead. The \"Count\" field in the response will confirm the actual value that was used.
    Boolean includeTimes = true; // Boolean | When set to \"true\", this indicates that the time component of the \"MatchCompletedDate\" field should be populated.  Otherwise, when set to \"false\" or when omitted, the time component will be set to \"00:00:00\".  When the value contains a non-boolean, HTTP 400 (\"Bad Request\") is returned.
    try {
      apiInstance.halo5PlayerMatchHistory(player, modes, start, count, includeTimes);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerMatchHistory");
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
| **player** | **String**| The Player&#39;s Gamertag. | |
| **modes** | **String**| Indicates what Game Mode(s) the client is interested in getting Matches for (arena, campaign, custom, customlocal, or warzone).  When the parameter is omitted or empty, Matches from all modes are returned. When a client would like to receive Matches spanning multiple Modes, separate the Modes with a comma (e.g. \&quot;arena,custom\&quot;). There is no significance to the order the Modes are specified in this parameter.  When an invalid Mode is specified, HTTP 400 (\&quot;Bad Request\&quot;) is returned.  When a valid Mode is specified more than once, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |
| **start** | **BigDecimal**| When specified, this indicates the starting index (0-based) for which the batch of results will begin at. For example, \&quot;start&#x3D;0\&quot; indicates that the first qualifying result will be returned, no items are &#39;skipped&#39;. Passing \&quot;start&#x3D;10\&quot; indicates that the result will begin with the 11th item, the first 10 will be &#39;skipped&#39;.  When omitted, zero is assumed.  When the value contains a non-digit, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |
| **count** | **BigDecimal**| When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 25 is assumed.  When the value contains a non-digit or is exactly \&quot;0\&quot;, HTTP 400 (\&quot;Bad Request\&quot;) is returned.  When the value is greater than the allowed range [1,25], the maximum allowed value is used instead. The \&quot;Count\&quot; field in the response will confirm the actual value that was used. | [optional] |
| **includeTimes** | **Boolean**| When set to \&quot;true\&quot;, this indicates that the time component of the \&quot;MatchCompletedDate\&quot; field should be populated.  Otherwise, when set to \&quot;false\&quot; or when omitted, the time component will be set to \&quot;00:00:00\&quot;.  When the value contains a non-boolean, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Player&#39;s recent Matches. An empty list will be returned if the Player has not played any Matches in the specified Game Mode(s). |  -  |
| **400** | An unsupported value was provided for a query string parameter. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PlayerServiceRecordsArena"></a>
# **halo5PlayerServiceRecordsArena**
> halo5PlayerServiceRecordsArena(players, seasonId)

Halo 5 - Player Service Records - Arena

&lt;p&gt;Retrieves Service Records for the Arena Game Mode for one or more players. A Service Record contains a player&#39;s lifetime statistics in the Game Mode.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;June 29, 2018:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added support for Social (Unranked) Playlists.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Service Record: Arena\&quot; to \&quot;Halo 5 - Player Service Records - Arena\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;April 20, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added documentation for the \&quot;CsrPercentile\&quot; field.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 32 Gamertags may be specified.
    String seasonId = "seasonId_example"; // String | When specified, this indicates the Season to request the Arena Playlist Stats for. If this is not specified, the default is the current Season. Seasons are available via the Metadata API. Social (Unranked) Arena Playlist Stats can be retrieved by specifying \"NonSeasonal\".
    try {
      apiInstance.halo5PlayerServiceRecordsArena(players, seasonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerServiceRecordsArena");
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
| **players** | **String**| A comma-separated list of Gamertags. Up to 32 Gamertags may be specified. | |
| **seasonId** | **String**| When specified, this indicates the Season to request the Arena Playlist Stats for. If this is not specified, the default is the current Season. Seasons are available via the Metadata API. Social (Unranked) Arena Playlist Stats can be retrieved by specifying \&quot;NonSeasonal\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Service Records for the requested player(s). |  -  |
| **404** | One or more Gamertags don&#39;t pass validation rules. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PlayerServiceRecordsCampaign"></a>
# **halo5PlayerServiceRecordsCampaign**
> halo5PlayerServiceRecordsCampaign(players)

Halo 5 - Player Service Records - Campaign

&lt;p&gt;Retrieves Service Records for the Campaign Game Mode for one or more players. A Service Record contains a player&#39;s lifetime statistics in the Game Mode.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Service Record: Campaign\&quot; to \&quot;Halo 5 - Player Service Records - Campaign\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 32 Gamertags may be specified.
    try {
      apiInstance.halo5PlayerServiceRecordsCampaign(players);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerServiceRecordsCampaign");
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
| **players** | **String**| A comma-separated list of Gamertags. Up to 32 Gamertags may be specified. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Service Records for the requested player(s). |  -  |
| **404** | One or more Gamertags don&#39;t pass validation rules. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PlayerServiceRecordsCustom"></a>
# **halo5PlayerServiceRecordsCustom**
> halo5PlayerServiceRecordsCustom(players)

Halo 5 - Player Service Records - Custom

&lt;p&gt;Retrieves Service Records for the Custom Game Mode for one or more players. A Service Record contains a player&#39;s lifetime statistics in the Game Mode. Games with the Custom Game Mode are played on Xbox Live Servers. For games played on Local Servers, use the \&quot;Halo 5 - Player Service Records - Custom Local\&quot; Endpoint.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Service Record: Custom\&quot; to \&quot;Halo 5 - Player Service Records - Custom\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 32 Gamertags may be specified.
    try {
      apiInstance.halo5PlayerServiceRecordsCustom(players);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerServiceRecordsCustom");
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
| **players** | **String**| A comma-separated list of Gamertags. Up to 32 Gamertags may be specified. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Service Records for the requested player(s). |  -  |
| **404** | One or more Gamertags don&#39;t pass validation rules. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PlayerServiceRecordsCustomLocal"></a>
# **halo5PlayerServiceRecordsCustomLocal**
> halo5PlayerServiceRecordsCustomLocal(players)

Halo 5 - Player Service Records - Custom Local

&lt;p&gt;Retrieves Service Records for the Custom Local Game Mode for one or more players. A Service Record contains a player&#39;s lifetime statistics in the Game Mode. Games with the Custom Local Game Mode are played on Local Servers. For games played on Xbox Live Servers, use the \&quot;Halo 5 - Player Service Records - Custom\&quot; Endpoint. A player&#39;s Custom Local Service Record summarizes games played on or after December 22, 2017.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 32 Gamertags may be specified.
    try {
      apiInstance.halo5PlayerServiceRecordsCustomLocal(players);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerServiceRecordsCustomLocal");
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
| **players** | **String**| A comma-separated list of Gamertags. Up to 32 Gamertags may be specified. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Service Records for the requested player(s). |  -  |
| **404** | One or more Gamertags don&#39;t pass validation rules. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="halo5PlayerServiceRecordsWarzone"></a>
# **halo5PlayerServiceRecordsWarzone**
> halo5PlayerServiceRecordsWarzone(players)

Halo 5 - Player Service Records - Warzone

&lt;p&gt;Retrieves Service Records for the Warzone Game Mode for one or more players. A Service Record contains a player&#39;s lifetime statistics in the Game Mode.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;December 22, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Game Mode clarifications to the Endpoint description.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Service Record: Warzone\&quot; to \&quot;Halo 5 - Player Service Records - Warzone\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 32 Gamertags may be specified.
    try {
      apiInstance.halo5PlayerServiceRecordsWarzone(players);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerServiceRecordsWarzone");
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
| **players** | **String**| A comma-separated list of Gamertags. Up to 32 Gamertags may be specified. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Service Records for the requested player(s). |  -  |
| **404** | One or more Gamertags don&#39;t pass validation rules. |  -  |
| **500** | Internal Server Error |  -  |

<a id="haloWars2LeaderboardPlayerCSR"></a>
# **haloWars2LeaderboardPlayerCSR**
> haloWars2LeaderboardPlayerCSR(seasonId, playlistId, count)

Halo Wars 2 - Leaderboard - Player CSR

&lt;p&gt;Retrieves the Leaderboard for Player CSRs. The Leaderboard consists of the top Players with a CSR of 1800 or above for a given Playlist in a Season.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;March 6, 2018:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Fixed documentation typos for the names of the \&quot;Player\&quot; and \&quot;Gamertag\&quot; properties.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 31, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Clarified documentation for which players are included in the leaderboard.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String seasonId = "seasonId_example"; // String | The ID for the Season.
    String playlistId = "playlistId_example"; // String | The ID for the Playlist.
    BigDecimal count = new BigDecimal(78); // BigDecimal | When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 200 is assumed.  When the value contains a non-digit or is exactly \"0\", HTTP 400 (\"Bad Request\") is returned.  When the value is greater than the allowed range [1,250], the maximum allowed value is used instead.  The \"Count\" field in the response will confirm the actual value that was used.
    try {
      apiInstance.haloWars2LeaderboardPlayerCSR(seasonId, playlistId, count);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2LeaderboardPlayerCSR");
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
| **seasonId** | **String**| The ID for the Season. | |
| **playlistId** | **String**| The ID for the Playlist. | |
| **count** | **BigDecimal**| When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 200 is assumed.  When the value contains a non-digit or is exactly \&quot;0\&quot;, HTTP 400 (\&quot;Bad Request\&quot;) is returned.  When the value is greater than the allowed range [1,250], the maximum allowed value is used instead.  The \&quot;Count\&quot; field in the response will confirm the actual value that was used. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Players in the Leaderboard. An empty list will be returned if no Players are in the Leaderboard. |  -  |
| **404** | The Season does not exist, or the Playlist either does not exist or is not part of the given Season. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2MatchEvents"></a>
# **haloWars2MatchEvents**
> haloWars2MatchEvents(matchId)

Halo Wars 2 - Match Events

&lt;p&gt;Retrieves a set of Events related to the Match specified. Events are only available once the Match has completed. Events are not available for Matches played with the Custom Match Type.&lt;/p&gt; &lt;p&gt;The set of Events may grow over time as data becomes available.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;September 5, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented new game mode \&quot;Terminus Firefight\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo Wars 2 - Player Match History\" Endpoint.
    try {
      apiInstance.haloWars2MatchEvents(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2MatchEvents");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo Wars 2 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Events. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2MatchResult"></a>
# **haloWars2MatchResult**
> haloWars2MatchResult(matchId)

Halo Wars 2 - Match Result

&lt;p&gt;Retrieves detailed statistics for a Match. Matches can be retrieved before they are completed; however, the data for in-progress Matches is only updated every few minutes.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;September 5, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented new game mode \&quot;Terminus Firefight\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String matchId = "matchId_example"; // String | An ID that uniquely identifies a Match. Match IDs can be retrieved from the \"Halo Wars 2 - Player Match History\" Endpoint.
    try {
      apiInstance.haloWars2MatchResult(matchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2MatchResult");
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
| **matchId** | **String**| An ID that uniquely identifies a Match. Match IDs can be retrieved from the \&quot;Halo Wars 2 - Player Match History\&quot; Endpoint. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match Result. |  -  |
| **404** | The specified Match could not be found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2PlayerCampaignProgress"></a>
# **haloWars2PlayerCampaignProgress**
> haloWars2PlayerCampaignProgress(player)

Halo Wars 2 - Player Campaign Progress

&lt;p&gt;Retrieves the Campaign Progress state for a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String player = "player_example"; // String | The Player's Gamertag.
    try {
      apiInstance.haloWars2PlayerCampaignProgress(player);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2PlayerCampaignProgress");
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
| **player** | **String**| The Player&#39;s Gamertag. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Campaign Progress for the Player. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2PlayerMatchHistory"></a>
# **haloWars2PlayerMatchHistory**
> haloWars2PlayerMatchHistory(player, matchType, start, count)

Halo Wars 2 - Player Match History

&lt;p&gt;Retrieves a list of Matches that the Player has participated in. If the Player is currently in a Match, it is not returned in this API.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;September 5, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Documented new game mode \&quot;Terminus Firefight\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String player = "player_example"; // String | The Player's Gamertag.
    String matchType = "matchType_example"; // String | Indicates what Match Type the client is interested in getting Matches for (\"custom\" or \"matchmaking\").  When the parameter is omitted or empty, Matches from all Match Types are returned.  When an invalid Mode is specified, HTTP 400 (\"Bad Request\") is returned.
    BigDecimal start = new BigDecimal(78); // BigDecimal | When specified, this indicates the starting index (0-based) for which the batch of results will begin at. For example, \"start=0\" indicates that the first qualifying result will be returned, no items are 'skipped'. Passing \"start=10\" indicates that the result will begin with the 11th item, the first 10 will be 'skipped'.  When omitted, zero is assumed.  When the value contains a non-digit, HTTP 400 (\"Bad Request\") is returned.
    BigDecimal count = new BigDecimal(78); // BigDecimal | When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 25 is assumed.  When the value contains a non-digit or is exactly \"0\", HTTP 400 (\"Bad Request\") is returned.  When the value is greater than the allowed range [1,25], the maximum allowed value is used instead. The \"Count\" field in the response will confirm the actual value that was used.
    try {
      apiInstance.haloWars2PlayerMatchHistory(player, matchType, start, count);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2PlayerMatchHistory");
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
| **player** | **String**| The Player&#39;s Gamertag. | |
| **matchType** | **String**| Indicates what Match Type the client is interested in getting Matches for (\&quot;custom\&quot; or \&quot;matchmaking\&quot;).  When the parameter is omitted or empty, Matches from all Match Types are returned.  When an invalid Mode is specified, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |
| **start** | **BigDecimal**| When specified, this indicates the starting index (0-based) for which the batch of results will begin at. For example, \&quot;start&#x3D;0\&quot; indicates that the first qualifying result will be returned, no items are &#39;skipped&#39;. Passing \&quot;start&#x3D;10\&quot; indicates that the result will begin with the 11th item, the first 10 will be &#39;skipped&#39;.  When omitted, zero is assumed.  When the value contains a non-digit, HTTP 400 (\&quot;Bad Request\&quot;) is returned. | [optional] |
| **count** | **BigDecimal**| When specified, this indicates the maximum quantity of items the client would like returned in the response.  When omitted, 25 is assumed.  When the value contains a non-digit or is exactly \&quot;0\&quot;, HTTP 400 (\&quot;Bad Request\&quot;) is returned.  When the value is greater than the allowed range [1,25], the maximum allowed value is used instead. The \&quot;Count\&quot; field in the response will confirm the actual value that was used. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Match History for the Player. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2PlayerPlaylistRatings"></a>
# **haloWars2PlayerPlaylistRatings**
> haloWars2PlayerPlaylistRatings(playlistId, players)

Halo Wars 2 - Player Playlist Ratings

&lt;p&gt;Retrieves Playlist Ratings in the current season for one or more Players.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String playlistId = "playlistId_example"; // String | The ID of the Playlist to get Ratings for.
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 6 Gamertags may be specified.
    try {
      apiInstance.haloWars2PlayerPlaylistRatings(playlistId, players);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2PlayerPlaylistRatings");
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
| **playlistId** | **String**| The ID of the Playlist to get Ratings for. | |
| **players** | **String**| A comma-separated list of Gamertags. Up to 6 Gamertags may be specified. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Playlist Ratings for the Player(s). |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2PlayerSeasonStatsSummary"></a>
# **haloWars2PlayerSeasonStatsSummary**
> haloWars2PlayerSeasonStatsSummary(player, seasonId)

Halo Wars 2 - Player Season Stats Summary

&lt;p&gt;Retrieves high-level aggregations across a Season for a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;September 5, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added additional pivots of data: \&quot;CustomModeStats\&quot;, \&quot;SinglePlayerModeStats\&quot;, \&quot;MultiplayerModeStats\&quot;, \&quot;SocialModeStats\&quot;, and \&quot;RankedModeStats\&quot;.&lt;/li&gt;         &lt;li&gt;Added additional fields to the \&quot;Summary\&quot; contract: \&quot;GameMode\&quot; and \&quot;HighestObjectiveScoreByTeamSize\&quot;.&lt;/li&gt;         &lt;li&gt;Documented new game mode \&quot;Terminus Firefight\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String player = "player_example"; // String | The Player's Gamertag.
    String seasonId = "seasonId_example"; // String | A Season ID or \"current\" for the current Season. Seasons are available via the Metadata API.
    try {
      apiInstance.haloWars2PlayerSeasonStatsSummary(player, seasonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2PlayerSeasonStatsSummary");
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
| **player** | **String**| The Player&#39;s Gamertag. | |
| **seasonId** | **String**| A Season ID or \&quot;current\&quot; for the current Season. Seasons are available via the Metadata API. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Stats Summary for the Player. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2PlayerStatsSummary"></a>
# **haloWars2PlayerStatsSummary**
> haloWars2PlayerStatsSummary(player)

Halo Wars 2 - Player Stats Summary

&lt;p&gt;Retrieves high-level aggregations across the lifetime of a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;September 5, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added additional fields: \&quot;GameMode\&quot; and \&quot;HighestObjectiveScoreByTeamSize\&quot;.&lt;/li&gt;         &lt;li&gt;Documented new game mode \&quot;Terminus Firefight\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String player = "player_example"; // String | The Player's Gamertag.
    try {
      apiInstance.haloWars2PlayerStatsSummary(player);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2PlayerStatsSummary");
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
| **player** | **String**| The Player&#39;s Gamertag. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Stats Summary for the Player. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="haloWars2PlayerXPs"></a>
# **haloWars2PlayerXPs**
> haloWars2PlayerXPs(players)

Halo Wars 2 - Player XPs

&lt;p&gt;Retrieves XP and Rank information for one or more players.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/stats");
    
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
    String players = "players_example"; // String | A comma-separated list of Gamertags. Up to 6 Gamertags may be specified.
    try {
      apiInstance.haloWars2PlayerXPs(players);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#haloWars2PlayerXPs");
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
| **players** | **String**| A comma-separated list of Gamertags. Up to 6 Gamertags may be specified. | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the XPs for the Player(s). |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

