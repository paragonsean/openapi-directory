# CfbV3Scores.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/cfb/scores*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areGamesInProgress**](DefaultApi.md#areGamesInProgress) | **GET** /{format}/AreAnyGamesInProgress | Are Games In Progress
[**conferenceHierarchyWithTeams**](DefaultApi.md#conferenceHierarchyWithTeams) | **GET** /{format}/LeagueHierarchy | Conference Hierarchy (with Teams)
[**currentSeason**](DefaultApi.md#currentSeason) | **GET** /{format}/CurrentSeason | Current Season
[**currentSeasonDetails**](DefaultApi.md#currentSeasonDetails) | **GET** /{format}/CurrentSeasonDetails | Current Season Details
[**currentSeasontype**](DefaultApi.md#currentSeasontype) | **GET** /{format}/CurrentSeasonType | Current SeasonType
[**currentWeek**](DefaultApi.md#currentWeek) | **GET** /{format}/CurrentWeek | Current Week
[**gamesByDate**](DefaultApi.md#gamesByDate) | **GET** /{format}/GamesByDate/{date} | Games by Date
[**gamesByWeek**](DefaultApi.md#gamesByWeek) | **GET** /{format}/GamesByWeek/{season}/{week} | Games by Week
[**gamesByWeekBasic**](DefaultApi.md#gamesByWeekBasic) | **GET** /{format}/ScoresBasic/{season}/{week} | Games by Week (Basic)
[**injuredPlayers**](DefaultApi.md#injuredPlayers) | **GET** /{format}/InjuredPlayers | Injured Players
[**playerDetailsByActive**](DefaultApi.md#playerDetailsByActive) | **GET** /{format}/Players | Player Details By Active
[**playerDetailsByPlayer**](DefaultApi.md#playerDetailsByPlayer) | **GET** /{format}/Player/{playerid} | Player Details By Player
[**playerDetailsByTeam**](DefaultApi.md#playerDetailsByTeam) | **GET** /{format}/Players/{team} | Player Details by Team
[**playersByTeamBasic**](DefaultApi.md#playersByTeamBasic) | **GET** /{format}/PlayersBasic/{team} | Players by Team (Basic)
[**schedules**](DefaultApi.md#schedules) | **GET** /{format}/Games/{season} | Schedules
[**schedulesBasic**](DefaultApi.md#schedulesBasic) | **GET** /{format}/SchedulesBasic/{season} | Schedules (Basic)
[**stadiums**](DefaultApi.md#stadiums) | **GET** /{format}/Stadiums | Stadiums
[**teamGameLogsBySeason**](DefaultApi.md#teamGameLogsBySeason) | **GET** /{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames} | Team Game Logs By Season
[**teamGameStatsByWeek**](DefaultApi.md#teamGameStatsByWeek) | **GET** /{format}/TeamGameStatsByWeek/{season}/{week} | Team Game Stats by Week
[**teamSeasonStatsStandings**](DefaultApi.md#teamSeasonStatsStandings) | **GET** /{format}/TeamSeasonStats/{season} | Team Season Stats &amp; Standings
[**teams**](DefaultApi.md#teams) | **GET** /{format}/Teams | Teams
[**teamsBasic**](DefaultApi.md#teamsBasic) | **GET** /{format}/TeamsBasic | Teams (Basic)



## areGamesInProgress

> Boolean areGamesInProgress(format)

Are Games In Progress

Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

**Boolean**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conferenceHierarchyWithTeams

> [Conference] conferenceHierarchyWithTeams(format)

Conference Hierarchy (with Teams)

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
apiInstance.conferenceHierarchyWithTeams(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Conference]**](Conference.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentSeason

> Number currentSeason(format)

Current Season

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

**Number**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentSeasonDetails

> Season currentSeasonDetails(format)

Current Season Details

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
apiInstance.currentSeasonDetails(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**Season**](Season.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentSeasontype

> String currentSeasontype(format)

Current SeasonType

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
apiInstance.currentSeasontype(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

**String**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentWeek

> Number currentWeek(format)

Current Week

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
apiInstance.currentWeek(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

**Number**

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
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
let date = "date_example"; // String |            The date of the game(s).           <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.         
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **date** | **String**|            The date of the game(s).           &lt;br&gt;Examples: &lt;code&gt;2016-SEP-01&lt;/code&gt;, &lt;code&gt;2017-SEP-10&lt;/code&gt;.          | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesByWeek

> [Game] gamesByWeek(format, season, week)

Games by Week

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
let season = "season_example"; // String |            Year of the season.           <br>Examples: <code>2015</code>, <code>2016</code>, etc.         
let week = "week_example"; // String |            The week of the game(s).           <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.         
apiInstance.gamesByWeek(format, season, week, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**|            Year of the season.           &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;, etc.          | 
 **week** | **String**|            The week of the game(s).           &lt;br&gt;Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc.          | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesByWeekBasic

> Object gamesByWeekBasic(format, season, week)

Games by Week (Basic)

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
let season = "season_example"; // String |            Year of the season.           <br>Examples: <code>2015</code>, <code>2016</code>, etc.         
let week = "week_example"; // String |            The week of the game(s).           <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.         
apiInstance.gamesByWeekBasic(format, season, week, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**|            Year of the season.           &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;, etc.          | 
 **week** | **String**|            The week of the game(s).           &lt;br&gt;Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc.          | 

### Return type

**Object**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuredPlayers

> [Player] injuredPlayers(format)

Injured Players

This endpoint provides all currently injured college football players, along with injury details.

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByActive

> [Player] playerDetailsByActive(format)

Player Details By Active

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByPlayer

> [Player] playerDetailsByPlayer(format, playerid)

Player Details By Player

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String |            Unique FantasyData Player ID.           Example:<code>50002016</code>.         
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **playerid** | **String**|            Unique FantasyData Player ID.           Example:&lt;code&gt;50002016&lt;/code&gt;.          | 

### Return type

[**[Player]**](Player.md)

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
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let team = "team_example"; // String |            The abbreviation of the requested team.           <br>Examples: <code>SF</code>, <code>NYY</code>.         
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **team** | **String**|            The abbreviation of the requested team.           &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.          | 

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playersByTeamBasic

> [PlayerBasic] playersByTeamBasic(format, team)

Players by Team (Basic)

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let team = "team_example"; // String |            The abbreviation of the requested team.           <br>Examples: <code>SF</code>, <code>NYY</code>.         
apiInstance.playersByTeamBasic(format, team, (error, data, response) => {
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
 **team** | **String**|            The abbreviation of the requested team.           &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.          | 

### Return type

[**[PlayerBasic]**](PlayerBasic.md)

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
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesBasic

> [ScheduleBasic] schedulesBasic(format, season)

Schedules (Basic)

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
apiInstance.schedulesBasic(format, season, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**[ScheduleBasic]**](ScheduleBasic.md)

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
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

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
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;         | 
 **teamid** | **String**| Unique ID of team.  Example &lt;code&gt; 1 &lt;/code&gt; | 
 **numberofgames** | **String**| How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt; | 

### Return type

[**[TeamGame]**](TeamGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamGameStatsByWeek

> [TeamGame] teamGameStatsByWeek(format, season, week)

Team Game Stats by Week

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
let season = "season_example"; // String |            Year of the season.           <br>Examples: <code>2015</code>, <code>2016</code>, etc.         
let week = "week_example"; // String |            The week of the game(s).           <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.         
apiInstance.teamGameStatsByWeek(format, season, week, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**|            Year of the season.           &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;, etc.          | 
 **week** | **String**|            The week of the game(s).           &lt;br&gt;Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc.          | 

### Return type

[**[TeamGame]**](TeamGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamSeasonStatsStandings

> [TeamSeason] teamSeasonStatsStandings(format, season)

Team Season Stats &amp; Standings

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2017</code>, <code>2017POST</code>, <code>2018</code>.
apiInstance.teamSeasonStatsStandings(format, season, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2017POST&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;. | 

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
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[Team]**](Team.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsBasic

> [TeamBasic] teamsBasic(format)

Teams (Basic)

### Example

```javascript
import CfbV3Scores from 'cfb_v3_scores';
let defaultClient = CfbV3Scores.ApiClient.instance;
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

let apiInstance = new CfbV3Scores.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>xml</code> or <code>json</code>.
apiInstance.teamsBasic(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;. | [default to &#39;XML&#39;]

### Return type

[**[TeamBasic]**](TeamBasic.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

