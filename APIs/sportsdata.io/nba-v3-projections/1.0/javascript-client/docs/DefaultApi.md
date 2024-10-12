# NbaV3Projections.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/nba/projections*

Method | HTTP request | Description
------------- | ------------- | -------------
[**depthCharts**](DefaultApi.md#depthCharts) | **GET** /{format}/DepthCharts | Depth Charts
[**dfsSlatesByDate**](DefaultApi.md#dfsSlatesByDate) | **GET** /{format}/DfsSlatesByDate/{date} | DFS Slates by Date
[**injuredPlayers**](DefaultApi.md#injuredPlayers) | **GET** /{format}/InjuredPlayers | Injured Players
[**projectedPlayerGameStatsByDateWInjuriesDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByDateWInjuriesDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByDate/{date} | Projected Player Game Stats by Date (w/ Injuries, DFS Salaries)
[**projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByPlayer/{date}/{playerid} | Projected Player Game Stats by Player (w/ Injuries, DFS Salaries)
[**projectedPlayerSeasonStats**](DefaultApi.md#projectedPlayerSeasonStats) | **GET** /{format}/PlayerSeasonProjectionStats/{season} | Projected Player Season Stats
[**projectedPlayerSeasonStatsByPlayer**](DefaultApi.md#projectedPlayerSeasonStatsByPlayer) | **GET** /{format}/PlayerSeasonProjectionStatsByPlayer/{season}/{playerid} | Projected Player Season Stats by Player
[**projectedPlayerSeasonStatsByTeam**](DefaultApi.md#projectedPlayerSeasonStatsByTeam) | **GET** /{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team} | Projected Player Season Stats by Team
[**startingLineupsByDate**](DefaultApi.md#startingLineupsByDate) | **GET** /{format}/StartingLineupsByDate/{date} | Starting Lineups by Date



## depthCharts

> [TeamDepthChart] depthCharts(format)

Depth Charts

This endpoint provides a depth chart for each NBA team.

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.depthCharts(format, (error, data, response) => {
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

[**[TeamDepthChart]**](TeamDepthChart.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dfsSlatesByDate

> [DfsSlate] dfsSlatesByDate(format, date)

DFS Slates by Date

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
apiInstance.dfsSlatesByDate(format, date, (error, data, response) => {
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
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-DEC-01&lt;/code&gt;, &lt;code&gt;2018-FEB-15&lt;/code&gt;. | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuredPlayers

> [Player] injuredPlayers(format)

Injured Players

This endpoint provides all currently injured NBA players, along with injury details.

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
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


## projectedPlayerGameStatsByDateWInjuriesDfsSalaries

> [PlayerGameProjection] projectedPlayerGameStatsByDateWInjuriesDfsSalaries(format, date)

Projected Player Game Stats by Date (w/ Injuries, DFS Salaries)

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
apiInstance.projectedPlayerGameStatsByDateWInjuriesDfsSalaries(format, date, (error, data, response) => {
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

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries

> PlayerGameProjection projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries(format, date, playerid)

Projected Player Game Stats by Player (w/ Injuries, DFS Salaries)

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s).<br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>20000571</code>.
apiInstance.projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries(format, date, playerid, (error, data, response) => {
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
 **date** | **String**| The date of the game(s).&lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;20000571&lt;/code&gt;. | 

### Return type

[**PlayerGameProjection**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerSeasonStats

> [PlayerSeasonProjection] projectedPlayerSeasonStats(format, season)

Projected Player Season Stats

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc.
apiInstance.projectedPlayerSeasonStats(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**[PlayerSeasonProjection]**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerSeasonStatsByPlayer

> PlayerSeasonProjection projectedPlayerSeasonStatsByPlayer(format, season, playerid)

Projected Player Season Stats by Player

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>20000571</code>.
apiInstance.projectedPlayerSeasonStatsByPlayer(format, season, playerid, (error, data, response) => {
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
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;20000571&lt;/code&gt;. | 

### Return type

[**PlayerSeasonProjection**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerSeasonStatsByTeam

> [PlayerSeasonProjection] projectedPlayerSeasonStatsByTeam(format, season, team)

Projected Player Season Stats by Team

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>, etc.
let team = "team_example"; // String | The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
apiInstance.projectedPlayerSeasonStatsByTeam(format, season, team, (error, data, response) => {
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
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 
 **team** | **String**| The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;MIA&lt;/code&gt;, &lt;code&gt;PHI&lt;/code&gt;. | 

### Return type

[**[PlayerSeasonProjection]**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startingLineupsByDate

> [StartingLineups] startingLineupsByDate(format, date)

Starting Lineups by Date

This endpoint provides the projected &amp; confirmed starting lineups for NBA games on a given date.

### Example

```javascript
import NbaV3Projections from 'nba_v3_projections';
let defaultClient = NbaV3Projections.ApiClient.instance;
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

let apiInstance = new NbaV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br> Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
apiInstance.startingLineupsByDate(format, date, (error, data, response) => {
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
 **date** | **String**| The date of the game(s). &lt;br&gt; Examples: &lt;code&gt;2021-OCT-12&lt;/code&gt;, &lt;code&gt;2021-DEC-09&lt;/code&gt;. | 

### Return type

[**[StartingLineups]**](StartingLineups.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

