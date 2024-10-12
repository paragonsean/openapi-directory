# GooglePlayGameServices.ScoresApi

All URIs are relative to *https://games.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gamesScoresGet**](ScoresApi.md#gamesScoresGet) | **GET** /games/v1/players/{playerId}/leaderboards/{leaderboardId}/scores/{timeSpan} | 
[**gamesScoresList**](ScoresApi.md#gamesScoresList) | **GET** /games/v1/leaderboards/{leaderboardId}/scores/{collection} | 
[**gamesScoresListWindow**](ScoresApi.md#gamesScoresListWindow) | **GET** /games/v1/leaderboards/{leaderboardId}/window/{collection} | 
[**gamesScoresSubmit**](ScoresApi.md#gamesScoresSubmit) | **POST** /games/v1/leaderboards/{leaderboardId}/scores | 
[**gamesScoresSubmitMultiple**](ScoresApi.md#gamesScoresSubmitMultiple) | **POST** /games/v1/leaderboards/scores | 



## gamesScoresGet

> PlayerLeaderboardScoreListResponse gamesScoresGet(playerId, leaderboardId, timeSpan, opts)



Get high scores, and optionally ranks, in leaderboards for the currently authenticated player. For a specific time span, &#x60;leaderboardId&#x60; can be set to &#x60;ALL&#x60; to retrieve data for all leaderboards in a given time span. &#x60;NOTE: You cannot ask for &#39;ALL&#39; leaderboards and &#39;ALL&#39; timeSpans in the same request; only one parameter may be set to &#39;ALL&#39;.

### Example

```javascript
import GooglePlayGameServices from 'google_play_game_services';
let defaultClient = GooglePlayGameServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayGameServices.ScoresApi();
let playerId = "playerId_example"; // String | A player ID. A value of `me` may be used in place of the authenticated player's ID.
let leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard. Can be set to 'ALL' to retrieve data for all leaderboards for this application.
let timeSpan = "timeSpan_example"; // String | The time span for the scores and ranks you're requesting.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'includeRankType': "includeRankType_example", // String | The types of ranks to return. If the parameter is omitted, no ranks will be returned.
  'language': "language_example", // String | The preferred language to use for strings returned by this method.
  'maxResults': 56, // Number | The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified `maxResults`.
  'pageToken': "pageToken_example" // String | The token returned by the previous request.
};
apiInstance.gamesScoresGet(playerId, leaderboardId, timeSpan, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playerId** | **String**| A player ID. A value of &#x60;me&#x60; may be used in place of the authenticated player&#39;s ID. | 
 **leaderboardId** | **String**| The ID of the leaderboard. Can be set to &#39;ALL&#39; to retrieve data for all leaderboards for this application. | 
 **timeSpan** | **String**| The time span for the scores and ranks you&#39;re requesting. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **includeRankType** | **String**| The types of ranks to return. If the parameter is omitted, no ranks will be returned. | [optional] 
 **language** | **String**| The preferred language to use for strings returned by this method. | [optional] 
 **maxResults** | **Number**| The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;. | [optional] 
 **pageToken** | **String**| The token returned by the previous request. | [optional] 

### Return type

[**PlayerLeaderboardScoreListResponse**](PlayerLeaderboardScoreListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesScoresList

> LeaderboardScores gamesScoresList(leaderboardId, collection, timeSpan, opts)



Lists the scores in a leaderboard, starting from the top.

### Example

```javascript
import GooglePlayGameServices from 'google_play_game_services';
let defaultClient = GooglePlayGameServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayGameServices.ScoresApi();
let leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard.
let collection = "collection_example"; // String | The collection of scores you're requesting.
let timeSpan = "timeSpan_example"; // String | Required. The time span for the scores and ranks you're requesting.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'language': "language_example", // String | The preferred language to use for strings returned by this method.
  'maxResults': 56, // Number | The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified `maxResults`.
  'pageToken': "pageToken_example" // String | The token returned by the previous request.
};
apiInstance.gamesScoresList(leaderboardId, collection, timeSpan, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboardId** | **String**| The ID of the leaderboard. | 
 **collection** | **String**| The collection of scores you&#39;re requesting. | 
 **timeSpan** | **String**| Required. The time span for the scores and ranks you&#39;re requesting. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **language** | **String**| The preferred language to use for strings returned by this method. | [optional] 
 **maxResults** | **Number**| The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;. | [optional] 
 **pageToken** | **String**| The token returned by the previous request. | [optional] 

### Return type

[**LeaderboardScores**](LeaderboardScores.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesScoresListWindow

> LeaderboardScores gamesScoresListWindow(leaderboardId, collection, timeSpan, opts)



Lists the scores in a leaderboard around (and including) a player&#39;s score.

### Example

```javascript
import GooglePlayGameServices from 'google_play_game_services';
let defaultClient = GooglePlayGameServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayGameServices.ScoresApi();
let leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard.
let collection = "collection_example"; // String | The collection of scores you're requesting.
let timeSpan = "timeSpan_example"; // String | Required. The time span for the scores and ranks you're requesting.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'language': "language_example", // String | The preferred language to use for strings returned by this method.
  'maxResults': 56, // Number | The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified `maxResults`.
  'pageToken': "pageToken_example", // String | The token returned by the previous request.
  'resultsAbove': 56, // Number | The preferred number of scores to return above the player's score. More scores may be returned if the player is at the bottom of the leaderboard; fewer may be returned if the player is at the top. Must be less than or equal to maxResults.
  'returnTopIfAbsent': true // Boolean | True if the top scores should be returned when the player is not in the leaderboard. Defaults to true.
};
apiInstance.gamesScoresListWindow(leaderboardId, collection, timeSpan, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboardId** | **String**| The ID of the leaderboard. | 
 **collection** | **String**| The collection of scores you&#39;re requesting. | 
 **timeSpan** | **String**| Required. The time span for the scores and ranks you&#39;re requesting. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **language** | **String**| The preferred language to use for strings returned by this method. | [optional] 
 **maxResults** | **Number**| The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;. | [optional] 
 **pageToken** | **String**| The token returned by the previous request. | [optional] 
 **resultsAbove** | **Number**| The preferred number of scores to return above the player&#39;s score. More scores may be returned if the player is at the bottom of the leaderboard; fewer may be returned if the player is at the top. Must be less than or equal to maxResults. | [optional] 
 **returnTopIfAbsent** | **Boolean**| True if the top scores should be returned when the player is not in the leaderboard. Defaults to true. | [optional] 

### Return type

[**LeaderboardScores**](LeaderboardScores.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesScoresSubmit

> PlayerScoreResponse gamesScoresSubmit(leaderboardId, score, opts)



Submits a score to the specified leaderboard.

### Example

```javascript
import GooglePlayGameServices from 'google_play_game_services';
let defaultClient = GooglePlayGameServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayGameServices.ScoresApi();
let leaderboardId = "leaderboardId_example"; // String | The ID of the leaderboard.
let score = "score_example"; // String | Required. The score you're submitting. The submitted score is ignored if it is worse than a previously submitted score, where worse depends on the leaderboard sort order. The meaning of the score value depends on the leaderboard format type. For fixed-point, the score represents the raw value. For time, the score represents elapsed time in milliseconds. For currency, the score represents a value in micro units.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'language': "language_example", // String | The preferred language to use for strings returned by this method.
  'scoreTag': "scoreTag_example" // String | Additional information about the score you're submitting. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986.
};
apiInstance.gamesScoresSubmit(leaderboardId, score, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboardId** | **String**| The ID of the leaderboard. | 
 **score** | **String**| Required. The score you&#39;re submitting. The submitted score is ignored if it is worse than a previously submitted score, where worse depends on the leaderboard sort order. The meaning of the score value depends on the leaderboard format type. For fixed-point, the score represents the raw value. For time, the score represents elapsed time in milliseconds. For currency, the score represents a value in micro units. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **language** | **String**| The preferred language to use for strings returned by this method. | [optional] 
 **scoreTag** | **String**| Additional information about the score you&#39;re submitting. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. | [optional] 

### Return type

[**PlayerScoreResponse**](PlayerScoreResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesScoresSubmitMultiple

> PlayerScoreListResponse gamesScoresSubmitMultiple(opts)



Submits multiple scores to leaderboards.

### Example

```javascript
import GooglePlayGameServices from 'google_play_game_services';
let defaultClient = GooglePlayGameServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayGameServices.ScoresApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'language': "language_example", // String | The preferred language to use for strings returned by this method.
  'playerScoreSubmissionList': new GooglePlayGameServices.PlayerScoreSubmissionList() // PlayerScoreSubmissionList | 
};
apiInstance.gamesScoresSubmitMultiple(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **language** | **String**| The preferred language to use for strings returned by this method. | [optional] 
 **playerScoreSubmissionList** | [**PlayerScoreSubmissionList**](PlayerScoreSubmissionList.md)|  | [optional] 

### Return type

[**PlayerScoreListResponse**](PlayerScoreListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

