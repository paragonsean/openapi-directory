# CbbV3Stats.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/cbb/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areGamesInProgress**](DefaultApi.md#areGamesInProgress) | **GET** /{format}/AreAnyGamesInProgress | Are Games In Progress
[**boxScore**](DefaultApi.md#boxScore) | **GET** /{format}/BoxScore/{gameid} | Box Score
[**boxScoresByDate**](DefaultApi.md#boxScoresByDate) | **GET** /{format}/BoxScores/{date} | Box Scores by Date
[**boxScoresByDateDelta**](DefaultApi.md#boxScoresByDateDelta) | **GET** /{format}/BoxScoresDelta/{date}/{minutes} | Box Scores by Date Delta
[**currentSeason**](DefaultApi.md#currentSeason) | **GET** /{format}/CurrentSeason | Current Season
[**gamesByDate**](DefaultApi.md#gamesByDate) | **GET** /{format}/GamesByDate/{date} | Games by Date
[**injuredPlayers**](DefaultApi.md#injuredPlayers) | **GET** /{format}/InjuredPlayers | Injured Players
[**leagueHierarchy**](DefaultApi.md#leagueHierarchy) | **GET** /{format}/LeagueHierarchy | League Hierarchy
[**playerDetailsByActive**](DefaultApi.md#playerDetailsByActive) | **GET** /{format}/Players | Player Details by Active
[**playerDetailsByPlayer**](DefaultApi.md#playerDetailsByPlayer) | **GET** /{format}/Player/{playerid} | Player Details by Player
[**playerDetailsByTeam**](DefaultApi.md#playerDetailsByTeam) | **GET** /{format}/Players/{team} | Player Details by Team
[**playerGameLogsBySeason**](DefaultApi.md#playerGameLogsBySeason) | **GET** /{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames} | Player Game Logs By Season
[**playerGameStatsByDate**](DefaultApi.md#playerGameStatsByDate) | **GET** /{format}/PlayerGameStatsByDate/{date} | Player Game Stats by Date
[**playerGameStatsByPlayer**](DefaultApi.md#playerGameStatsByPlayer) | **GET** /{format}/PlayerGameStatsByPlayer/{date}/{playerid} | Player Game Stats by Player
[**playerSeasonStats**](DefaultApi.md#playerSeasonStats) | **GET** /{format}/PlayerSeasonStats/{season} | Player Season Stats
[**playerSeasonStatsByPlayer**](DefaultApi.md#playerSeasonStatsByPlayer) | **GET** /{format}/PlayerSeasonStatsByPlayer/{season}/{playerid} | Player Season Stats By Player
[**playerSeasonStatsByTeam**](DefaultApi.md#playerSeasonStatsByTeam) | **GET** /{format}/PlayerSeasonStatsByTeam/{season}/{team} | Player Season Stats by Team
[**projectedPlayerGameStatsByDate**](DefaultApi.md#projectedPlayerGameStatsByDate) | **GET** /{format}/PlayerGameProjectionStatsByDate/{date} | Projected Player Game Stats by Date
[**projectedPlayerGameStatsByPlayer**](DefaultApi.md#projectedPlayerGameStatsByPlayer) | **GET** /{format}/PlayerGameProjectionStatsByPlayer/{date}/{playerid} | Projected Player Game Stats by Player
[**schedules**](DefaultApi.md#schedules) | **GET** /{format}/Games/{season} | Schedules
[**stadiums**](DefaultApi.md#stadiums) | **GET** /{format}/Stadiums | Stadiums
[**teamGameLogsBySeason**](DefaultApi.md#teamGameLogsBySeason) | **GET** /{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames} | Team Game Logs By Season
[**teamGameStatsByDate**](DefaultApi.md#teamGameStatsByDate) | **GET** /{format}/TeamGameStatsByDate/{date} | Team Game Stats by Date
[**teamSeasonStats**](DefaultApi.md#teamSeasonStats) | **GET** /{format}/TeamSeasonStats/{season} | Team Season Stats
[**teams**](DefaultApi.md#teams) | **GET** /{format}/teams | Teams
[**tournamentHierarchy**](DefaultApi.md#tournamentHierarchy) | **GET** /{format}/Tournament/{season} | Tournament Hierarchy



## areGamesInProgress

> Boolean areGamesInProgress(format)

Are Games In Progress

Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.areGamesInProgress(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

**Boolean**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScore

> BoxScore boxScore(format, gameid)

Box Score

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let gameid = "gameid_example"; // String | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>14620</code> or <code>16905</code>
apiInstance.boxScore(format, gameid, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **gameid** | **String**| The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are &lt;code&gt;14620&lt;/code&gt; or &lt;code&gt;16905&lt;/code&gt; | 

### Return type

[**BoxScore**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoresByDate

> [BoxScore] boxScoresByDate(format, date)

Box Scores by Date

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
apiInstance.boxScoresByDate(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoresByDateDelta

> [BoxScore] boxScoresByDateDelta(format, date, minutes)

Box Scores by Date Delta

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
let minutes = "minutes_example"; // String | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are: <code>1</code> or <code>2</code>.
apiInstance.boxScoresByDateDelta(format, date, minutes, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 
 **minutes** | **String**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are: &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;. | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentSeason

> Season currentSeason(format)

Current Season

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.currentSeason(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**Season**](Season.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesByDate

> [Game] gamesByDate(format, date)

Games by Date

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
apiInstance.gamesByDate(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuredPlayers

> [Player] injuredPlayers(format)

Injured Players

This endpoint provides all currently injured college basketball players, along with injury details.

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.injuredPlayers(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## leagueHierarchy

> [Conference] leagueHierarchy(format)

League Hierarchy

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.leagueHierarchy(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Conference]**](Conference.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByActive

> [Player] playerDetailsByActive(format)

Player Details by Active

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.playerDetailsByActive(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByPlayer

> Player playerDetailsByPlayer(format, playerid)

Player Details by Player

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>60003802</code>.
apiInstance.playerDetailsByPlayer(format, playerid, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;. | 

### Return type

[**Player**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByTeam

> [Player] playerDetailsByTeam(format, team)

Player Details by Team

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let team = "team_example"; // String | The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
apiInstance.playerDetailsByTeam(format, team, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **team** | **String**| The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;. | 

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameLogsBySeason

> [PlayerGame] playerGameLogsBySeason(format, season, playerid, numberofgames)

Player Game Logs By Season

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Season to get games from. Example <code>2019POST</code>, <code>2020</code>
let playerid = "playerid_example"; // String | Unique FantasyData Player ID.Example:<code>60008094</code>.
let numberofgames = "numberofgames_example"; // String | How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
apiInstance.playerGameLogsBySeason(format, season, playerid, numberofgames, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **String**| Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt; | 
 **playerid** | **String**| Unique FantasyData Player ID.Example:&lt;code&gt;60008094&lt;/code&gt;. | 
 **numberofgames** | **String**| How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt; | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsByDate

> [PlayerGame] playerGameStatsByDate(format, date)

Player Game Stats by Date

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
apiInstance.playerGameStatsByDate(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsByPlayer

> PlayerGame playerGameStatsByPlayer(format, date, playerid)

Player Game Stats by Player

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>60003802</code>.
apiInstance.playerGameStatsByPlayer(format, date, playerid, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;. | 

### Return type

[**PlayerGame**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStats

> [PlayerSeason] playerSeasonStats(format, season)

Player Season Stats

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>.
apiInstance.playerSeasonStats(format, season, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStatsByPlayer

> PlayerSeason playerSeasonStatsByPlayer(format, season, playerid)

Player Season Stats By Player

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>60003802</code>.
apiInstance.playerSeasonStatsByPlayer(format, season, playerid, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;. | 

### Return type

[**PlayerSeason**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStatsByTeam

> [PlayerSeason] playerSeasonStatsByTeam(format, season, team)

Player Season Stats by Team

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>.
let team = "team_example"; // String | The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
apiInstance.playerSeasonStatsByTeam(format, season, team, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;. | 
 **team** | **String**| The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByDate

> [PlayerGameProjection] projectedPlayerGameStatsByDate(format, date)

Projected Player Game Stats by Date

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
apiInstance.projectedPlayerGameStatsByDate(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByPlayer

> PlayerGameProjection projectedPlayerGameStatsByPlayer(format, date, playerid)

Projected Player Game Stats by Player

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>60003802</code>.
apiInstance.projectedPlayerGameStatsByPlayer(format, date, playerid, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;. | 

### Return type

[**PlayerGameProjection**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedules

> [Game] schedules(format, season)

Schedules

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
apiInstance.schedules(format, season, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stadiums

> [Stadium] stadiums(format)

Stadiums

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.stadiums(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Stadium]**](Stadium.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamGameLogsBySeason

> [TeamGame] teamGameLogsBySeason(format, season, teamid, numberofgames)

Team Game Logs By Season

Game by game log of total team statistics.

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Season to get games from. Example <code>2019POST</code>, <code>2020</code>
let teamid = "teamid_example"; // String | Unique ID of team.  Example <code> 1 </code>
let numberofgames = "numberofgames_example"; // String | How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
apiInstance.teamGameLogsBySeason(format, season, teamid, numberofgames, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **String**| Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt; | 
 **teamid** | **String**| Unique ID of team.  Example &lt;code&gt; 1 &lt;/code&gt; | 
 **numberofgames** | **String**| How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt; | 

### Return type

[**[TeamGame]**](TeamGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamGameStatsByDate

> [TeamGame] teamGameStatsByDate(format, date)

Team Game Stats by Date

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
apiInstance.teamGameStatsByDate(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;. | 

### Return type

[**[TeamGame]**](TeamGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamSeasonStats

> [TeamSeason] teamSeasonStats(format, season)

Team Season Stats

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>.
apiInstance.teamSeasonStats(format, season, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;. | 

### Return type

[**[TeamSeason]**](TeamSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams

> [Team] teams(format)

Teams

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.teams(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Team]**](Team.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tournamentHierarchy

> Tournament tournamentHierarchy(format, season)

Tournament Hierarchy

### Example

```javascript
import CbbV3Stats from 'cbb_v3_stats';
let defaultClient = CbbV3Stats.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new CbbV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>.
apiInstance.tournamentHierarchy(format, season, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;. | 

### Return type

[**Tournament**](Tournament.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

