# ScoresApi

All URIs are relative to *https://games.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gamesScoresGet**](ScoresApi.md#gamesScoresGet) | **GET** /games/v1/players/{playerId}/leaderboards/{leaderboardId}/scores/{timeSpan} |  |
| [**gamesScoresList**](ScoresApi.md#gamesScoresList) | **GET** /games/v1/leaderboards/{leaderboardId}/scores/{collection} |  |
| [**gamesScoresListWindow**](ScoresApi.md#gamesScoresListWindow) | **GET** /games/v1/leaderboards/{leaderboardId}/window/{collection} |  |
| [**gamesScoresSubmit**](ScoresApi.md#gamesScoresSubmit) | **POST** /games/v1/leaderboards/{leaderboardId}/scores |  |
| [**gamesScoresSubmitMultiple**](ScoresApi.md#gamesScoresSubmitMultiple) | **POST** /games/v1/leaderboards/scores |  |


<a id="gamesScoresGet"></a>
# **gamesScoresGet**
> PlayerLeaderboardScoreListResponse gamesScoresGet(playerId, leaderboardId, timeSpan, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeRankType, language, maxResults, pageToken)



Get high scores, and optionally ranks, in leaderboards for the currently authenticated player. For a specific time span, &#x60;leaderboardId&#x60; can be set to &#x60;ALL&#x60; to retrieve data for all leaderboards in a given time span. &#x60;NOTE: You cannot ask for &#39;ALL&#39; leaderboards and &#39;ALL&#39; timeSpans in the same request; only one parameter may be set to &#39;ALL&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://games.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoresApi apiInstance = new ScoresApi(defaultClient);
    String playerId = "playerId_example"; // String | A player ID. A value of `me` may be used in place of the authenticated player's ID.
    String leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard. Can be set to 'ALL' to retrieve data for all leaderboards for this application.
    String timeSpan = "ALL"; // String | The time span for the scores and ranks you're requesting.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String includeRankType = "ALL"; // String | The types of ranks to return. If the parameter is omitted, no ranks will be returned.
    String language = "language_example"; // String | The preferred language to use for strings returned by this method.
    Integer maxResults = 56; // Integer | The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified `maxResults`.
    String pageToken = "pageToken_example"; // String | The token returned by the previous request.
    try {
      PlayerLeaderboardScoreListResponse result = apiInstance.gamesScoresGet(playerId, leaderboardId, timeSpan, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeRankType, language, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoresApi#gamesScoresGet");
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
| **playerId** | **String**| A player ID. A value of &#x60;me&#x60; may be used in place of the authenticated player&#39;s ID. | |
| **leaderboardId** | **String**| The ID of the leaderboard. Can be set to &#39;ALL&#39; to retrieve data for all leaderboards for this application. | |
| **timeSpan** | **String**| The time span for the scores and ranks you&#39;re requesting. | [enum: ALL, ALL_TIME, WEEKLY, DAILY] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **includeRankType** | **String**| The types of ranks to return. If the parameter is omitted, no ranks will be returned. | [optional] [enum: ALL, PUBLIC, SOCIAL, FRIENDS] |
| **language** | **String**| The preferred language to use for strings returned by this method. | [optional] |
| **maxResults** | **Integer**| The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;. | [optional] |
| **pageToken** | **String**| The token returned by the previous request. | [optional] |

### Return type

[**PlayerLeaderboardScoreListResponse**](PlayerLeaderboardScoreListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="gamesScoresList"></a>
# **gamesScoresList**
> LeaderboardScores gamesScoresList(leaderboardId, collection, timeSpan, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, maxResults, pageToken)



Lists the scores in a leaderboard, starting from the top.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://games.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoresApi apiInstance = new ScoresApi(defaultClient);
    String leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard.
    String collection = "PUBLIC"; // String | The collection of scores you're requesting.
    String timeSpan = "ALL_TIME"; // String | Required. The time span for the scores and ranks you're requesting.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String language = "language_example"; // String | The preferred language to use for strings returned by this method.
    Integer maxResults = 56; // Integer | The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified `maxResults`.
    String pageToken = "pageToken_example"; // String | The token returned by the previous request.
    try {
      LeaderboardScores result = apiInstance.gamesScoresList(leaderboardId, collection, timeSpan, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoresApi#gamesScoresList");
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
| **leaderboardId** | **String**| The ID of the leaderboard. | |
| **collection** | **String**| The collection of scores you&#39;re requesting. | [enum: PUBLIC, SOCIAL, FRIENDS] |
| **timeSpan** | **String**| Required. The time span for the scores and ranks you&#39;re requesting. | [enum: ALL_TIME, WEEKLY, DAILY] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **language** | **String**| The preferred language to use for strings returned by this method. | [optional] |
| **maxResults** | **Integer**| The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;. | [optional] |
| **pageToken** | **String**| The token returned by the previous request. | [optional] |

### Return type

[**LeaderboardScores**](LeaderboardScores.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="gamesScoresListWindow"></a>
# **gamesScoresListWindow**
> LeaderboardScores gamesScoresListWindow(leaderboardId, collection, timeSpan, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, maxResults, pageToken, resultsAbove, returnTopIfAbsent)



Lists the scores in a leaderboard around (and including) a player&#39;s score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://games.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoresApi apiInstance = new ScoresApi(defaultClient);
    String leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard.
    String collection = "PUBLIC"; // String | The collection of scores you're requesting.
    String timeSpan = "ALL_TIME"; // String | Required. The time span for the scores and ranks you're requesting.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String language = "language_example"; // String | The preferred language to use for strings returned by this method.
    Integer maxResults = 56; // Integer | The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified `maxResults`.
    String pageToken = "pageToken_example"; // String | The token returned by the previous request.
    Integer resultsAbove = 56; // Integer | The preferred number of scores to return above the player's score. More scores may be returned if the player is at the bottom of the leaderboard; fewer may be returned if the player is at the top. Must be less than or equal to maxResults.
    Boolean returnTopIfAbsent = true; // Boolean | True if the top scores should be returned when the player is not in the leaderboard. Defaults to true.
    try {
      LeaderboardScores result = apiInstance.gamesScoresListWindow(leaderboardId, collection, timeSpan, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, maxResults, pageToken, resultsAbove, returnTopIfAbsent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoresApi#gamesScoresListWindow");
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
| **leaderboardId** | **String**| The ID of the leaderboard. | |
| **collection** | **String**| The collection of scores you&#39;re requesting. | [enum: PUBLIC, SOCIAL, FRIENDS] |
| **timeSpan** | **String**| Required. The time span for the scores and ranks you&#39;re requesting. | [enum: ALL_TIME, WEEKLY, DAILY] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **language** | **String**| The preferred language to use for strings returned by this method. | [optional] |
| **maxResults** | **Integer**| The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;. | [optional] |
| **pageToken** | **String**| The token returned by the previous request. | [optional] |
| **resultsAbove** | **Integer**| The preferred number of scores to return above the player&#39;s score. More scores may be returned if the player is at the bottom of the leaderboard; fewer may be returned if the player is at the top. Must be less than or equal to maxResults. | [optional] |
| **returnTopIfAbsent** | **Boolean**| True if the top scores should be returned when the player is not in the leaderboard. Defaults to true. | [optional] |

### Return type

[**LeaderboardScores**](LeaderboardScores.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="gamesScoresSubmit"></a>
# **gamesScoresSubmit**
> PlayerScoreResponse gamesScoresSubmit(leaderboardId, score, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, scoreTag)



Submits a score to the specified leaderboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://games.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoresApi apiInstance = new ScoresApi(defaultClient);
    String leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard.
    String score = "score_example"; // String | Required. The score you're submitting. The submitted score is ignored if it is worse than a previously submitted score, where worse depends on the leaderboard sort order. The meaning of the score value depends on the leaderboard format type. For fixed-point, the score represents the raw value. For time, the score represents elapsed time in milliseconds. For currency, the score represents a value in micro units.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String language = "language_example"; // String | The preferred language to use for strings returned by this method.
    String scoreTag = "scoreTag_example"; // String | Additional information about the score you're submitting. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986.
    try {
      PlayerScoreResponse result = apiInstance.gamesScoresSubmit(leaderboardId, score, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, scoreTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoresApi#gamesScoresSubmit");
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
| **leaderboardId** | **String**| The ID of the leaderboard. | |
| **score** | **String**| Required. The score you&#39;re submitting. The submitted score is ignored if it is worse than a previously submitted score, where worse depends on the leaderboard sort order. The meaning of the score value depends on the leaderboard format type. For fixed-point, the score represents the raw value. For time, the score represents elapsed time in milliseconds. For currency, the score represents a value in micro units. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **language** | **String**| The preferred language to use for strings returned by this method. | [optional] |
| **scoreTag** | **String**| Additional information about the score you&#39;re submitting. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. | [optional] |

### Return type

[**PlayerScoreResponse**](PlayerScoreResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="gamesScoresSubmitMultiple"></a>
# **gamesScoresSubmitMultiple**
> PlayerScoreListResponse gamesScoresSubmitMultiple($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, playerScoreSubmissionList)



Submits multiple scores to leaderboards.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://games.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoresApi apiInstance = new ScoresApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String language = "language_example"; // String | The preferred language to use for strings returned by this method.
    PlayerScoreSubmissionList playerScoreSubmissionList = new PlayerScoreSubmissionList(); // PlayerScoreSubmissionList | 
    try {
      PlayerScoreListResponse result = apiInstance.gamesScoresSubmitMultiple($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, language, playerScoreSubmissionList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoresApi#gamesScoresSubmitMultiple");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **language** | **String**| The preferred language to use for strings returned by this method. | [optional] |
| **playerScoreSubmissionList** | [**PlayerScoreSubmissionList**](PlayerScoreSubmissionList.md)|  | [optional] |

### Return type

[**PlayerScoreListResponse**](PlayerScoreListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

