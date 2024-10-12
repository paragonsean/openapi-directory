# GolfV2.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/golf/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentSeason**](DefaultApi.md#currentSeason) | **GET** /{format}/CurrentSeason | Current Season
[**dfsSlates**](DefaultApi.md#dfsSlates) | **GET** /{format}/DfsSlatesByTournament/{tournamentid} | DFS Slates
[**injuries**](DefaultApi.md#injuries) | **GET** /{format}/Injuries | Injuries
[**injuriesHistorical**](DefaultApi.md#injuriesHistorical) | **GET** /{format}/InjuriesByHistorical | Injuries (Historical)
[**leaderboard**](DefaultApi.md#leaderboard) | **GET** /{format}/Leaderboard/{tournamentid} | Leaderboard
[**news**](DefaultApi.md#news) | **GET** /{format}/News | News
[**newsByDate**](DefaultApi.md#newsByDate) | **GET** /{format}/NewsByDate/{date} | News by Date
[**newsByPlayer**](DefaultApi.md#newsByPlayer) | **GET** /{format}/NewsByPlayerID/{playerid} | News by Player
[**player**](DefaultApi.md#player) | **GET** /{format}/Player/{playerid} | Player
[**playerSeasonStatsWWorldGolfRankings**](DefaultApi.md#playerSeasonStatsWWorldGolfRankings) | **GET** /{format}/PlayerSeasonStats/{season} | Player Season Stats (w/ World Golf Rankings)
[**playerTournamentProjectedStatsWDraftkingsSalaries**](DefaultApi.md#playerTournamentProjectedStatsWDraftkingsSalaries) | **GET** /{format}/PlayerTournamentProjectionStats/{tournamentid} | Player Tournament Projected Stats (w/ DraftKings Salaries)
[**playerTournamentStatsByPlayer**](DefaultApi.md#playerTournamentStatsByPlayer) | **GET** /{format}/PlayerTournamentStatsByPlayer/{tournamentid}/{playerid} | Player Tournament Stats By Player
[**players**](DefaultApi.md#players) | **GET** /{format}/Players | Players
[**schedule**](DefaultApi.md#schedule) | **GET** /{format}/Tournaments | Schedule
[**scheduleBySeason**](DefaultApi.md#scheduleBySeason) | **GET** /{format}/Tournaments/{season} | Schedule by Season



## currentSeason

> Season currentSeason(format)

Current Season

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
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


## dfsSlates

> [DfsSlate] dfsSlates(format, tournamentid)

DFS Slates

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let tournamentid = "tournamentid_example"; // String | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>58</code>, <code>61</code>, etc.
apiInstance.dfsSlates(format, tournamentid, (error, data, response) => {
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
 **tournamentid** | **String**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc. | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuries

> [Injury] injuries(format)

Injuries

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.injuries(format, (error, data, response) => {
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

[**[Injury]**](Injury.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuriesHistorical

> [Injury] injuriesHistorical(format)

Injuries (Historical)

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.injuriesHistorical(format, (error, data, response) => {
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

[**[Injury]**](Injury.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## leaderboard

> Leaderboard leaderboard(format, tournamentid)

Leaderboard

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let tournamentid = "tournamentid_example"; // String | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>58</code>, <code>61</code>, etc.
apiInstance.leaderboard(format, tournamentid, (error, data, response) => {
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
 **tournamentid** | **String**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc. | 

### Return type

[**Leaderboard**](Leaderboard.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## news

> [News] news(format)

News

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.news(format, (error, data, response) => {
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

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## newsByDate

> [News] newsByDate(format, date)

News by Date

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
apiInstance.newsByDate(format, date, (error, data, response) => {
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
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;. | 

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## newsByPlayer

> [News] newsByPlayer(format, playerid)

News by Player

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>40000019</code>.
apiInstance.newsByPlayer(format, playerid, (error, data, response) => {
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
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;. | 

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## player

> Player player(format, playerid)

Player

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>40000019</code>.
apiInstance.player(format, playerid, (error, data, response) => {
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
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;. | 

### Return type

[**Player**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStatsWWorldGolfRankings

> [PlayerSeason] playerSeasonStatsWWorldGolfRankings(format, season)

Player Season Stats (w/ World Golf Rankings)

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
apiInstance.playerSeasonStatsWWorldGolfRankings(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season. &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt;. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerTournamentProjectedStatsWDraftkingsSalaries

> [PlayerTournamentProjection] playerTournamentProjectedStatsWDraftkingsSalaries(format, tournamentid)

Player Tournament Projected Stats (w/ DraftKings Salaries)

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let tournamentid = "tournamentid_example"; // String | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
apiInstance.playerTournamentProjectedStatsWDraftkingsSalaries(format, tournamentid, (error, data, response) => {
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
 **tournamentid** | **String**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;78&lt;/code&gt;, &lt;code&gt;79&lt;/code&gt;, &lt;code&gt;80&lt;/code&gt;, etc. | 

### Return type

[**[PlayerTournamentProjection]**](PlayerTournamentProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerTournamentStatsByPlayer

> PlayerTournament playerTournamentStatsByPlayer(format, tournamentid, playerid)

Player Tournament Stats By Player

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let tournamentid = "tournamentid_example"; // String | The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are <code>58</code>, <code>61</code>, etc.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>40000019</code>.
apiInstance.playerTournamentStatsByPlayer(format, tournamentid, playerid, (error, data, response) => {
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
 **tournamentid** | **String**| The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;. | 

### Return type

[**PlayerTournament**](PlayerTournament.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## players

> [Player] players(format)

Players

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.players(format, (error, data, response) => {
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


## schedule

> [Tournament] schedule(format)

Schedule

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.schedule(format, (error, data, response) => {
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

[**[Tournament]**](Tournament.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scheduleBySeason

> [Tournament] scheduleBySeason(format, season)

Schedule by Season

### Example

```javascript
import GolfV2 from 'golf_v2';
let defaultClient = GolfV2.ApiClient.instance;
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

let apiInstance = new GolfV2.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
apiInstance.scheduleBySeason(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season. &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt;. | 

### Return type

[**[Tournament]**](Tournament.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

