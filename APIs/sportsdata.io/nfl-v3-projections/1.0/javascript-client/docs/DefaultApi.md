# NflV3Projections.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/nfl/projections*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dfsSlateOwnershipProjectionsBySlateid**](DefaultApi.md#dfsSlateOwnershipProjectionsBySlateid) | **GET** /{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId} | DFS Slate Ownership Projections by SlateID
[**dfsSlatesByDate**](DefaultApi.md#dfsSlatesByDate) | **GET** /{format}/DfsSlatesByDate/{date} | DFS Slates by Date
[**dfsSlatesByWeek**](DefaultApi.md#dfsSlatesByWeek) | **GET** /{format}/DfsSlatesByWeek/{season}/{week} | DFS Slates by Week
[**idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries**](DefaultApi.md#idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries) | **GET** /{format}/IdpPlayerGameProjectionStatsByPlayerID/{season}/{week}/{playerid} | IDP Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)
[**idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries**](DefaultApi.md#idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries) | **GET** /{format}/IdpPlayerGameProjectionStatsByTeam/{season}/{week}/{team} | IDP Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)
[**idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries**](DefaultApi.md#idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries) | **GET** /{format}/IdpPlayerGameProjectionStatsByWeek/{season}/{week} | IDP Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)
[**injuredPlayers**](DefaultApi.md#injuredPlayers) | **GET** /{format}/InjuredPlayers | Injured Players
[**projectedFantasyDefenseGameStatsWDfsSalaries**](DefaultApi.md#projectedFantasyDefenseGameStatsWDfsSalaries) | **GET** /{format}/FantasyDefenseProjectionsByGame/{season}/{week} | Projected Fantasy Defense Game Stats (w/ DFS Salaries)
[**projectedFantasyDefenseSeasonStatsWAdp**](DefaultApi.md#projectedFantasyDefenseSeasonStatsWAdp) | **GET** /{format}/FantasyDefenseProjectionsBySeason/{season} | Projected Fantasy Defense Season Stats (w/ ADP)
[**projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByPlayerID/{season}/{week}/{playerid} | Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)
[**projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByTeam/{season}/{week}/{team} | Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)
[**projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByWeek/{season}/{week} | Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)
[**projectedPlayerSeasonStatsByPlayerWAdp**](DefaultApi.md#projectedPlayerSeasonStatsByPlayerWAdp) | **GET** /{format}/PlayerSeasonProjectionStatsByPlayerID/{season}/{playerid} | Projected Player Season Stats by Player (w/ ADP)
[**projectedPlayerSeasonStatsByTeamWAdp**](DefaultApi.md#projectedPlayerSeasonStatsByTeamWAdp) | **GET** /{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team} | Projected Player Season Stats by Team (w/ ADP)
[**projectedPlayerSeasonStatsWAdp**](DefaultApi.md#projectedPlayerSeasonStatsWAdp) | **GET** /{format}/PlayerSeasonProjectionStats/{season} | Projected Player Season Stats (w/ ADP)
[**upcomingDfsSlateOwnershipProjections**](DefaultApi.md#upcomingDfsSlateOwnershipProjections) | **GET** /{format}/UpcomingDfsSlateOwnershipProjections | Upcoming DFS Slate Ownership Projections



## dfsSlateOwnershipProjectionsBySlateid

> DfsSlateWithOwnershipProjection dfsSlateOwnershipProjectionsBySlateid(format, slateId)

DFS Slate Ownership Projections by SlateID

Slate Ownership Projections for a specific slate. Projections are for GPP format ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let slateId = "slateId_example"; // String | SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty SlateOwnershipProjections if this slate was not projected
apiInstance.dfsSlateOwnershipProjectionsBySlateid(format, slateId, (error, data, response) => {
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
 **slateId** | **String**| SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty SlateOwnershipProjections if this slate was not projected | 

### Return type

[**DfsSlateWithOwnershipProjection**](DfsSlateWithOwnershipProjection.md)

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
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the slates. <br>Examples: <code>2017-SEP-25</code>, <code>2017-10-31</code>.
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
 **date** | **String**| The date of the slates. &lt;br&gt;Examples: &lt;code&gt;2017-SEP-25&lt;/code&gt;, &lt;code&gt;2017-10-31&lt;/code&gt;. | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dfsSlatesByWeek

> [DfsSlate] dfsSlatesByWeek(format, season, week)

DFS Slates by Week

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>
apiInstance.dfsSlatesByWeek(format, season, week, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt; | 
 **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt; | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries

> PlayerGameProjection idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid)

IDP Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.
apiInstance.idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | 

### Return type

[**PlayerGameProjection**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries

> [PlayerGameProjection] idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team)

IDP Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries

> [PlayerGameProjection] idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week)

IDP Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuredPlayers

> [Player] injuredPlayers(format)

Injured Players

This endpoint provides all currently injured NFL players, along with injury details.

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
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


## projectedFantasyDefenseGameStatsWDfsSalaries

> [FantasyDefenseGameProjection] projectedFantasyDefenseGameStatsWDfsSalaries(format, season, week)

Projected Fantasy Defense Game Stats (w/ DFS Salaries)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.projectedFantasyDefenseGameStatsWDfsSalaries(format, season, week, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[FantasyDefenseGameProjection]**](FantasyDefenseGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedFantasyDefenseSeasonStatsWAdp

> [FantasyDefenseSeasonProjection] projectedFantasyDefenseSeasonStatsWAdp(format, season)

Projected Fantasy Defense Season Stats (w/ ADP)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.projectedFantasyDefenseSeasonStatsWAdp(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[FantasyDefenseSeasonProjection]**](FantasyDefenseSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries

> PlayerGameProjection projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid)

Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.
apiInstance.projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | 

### Return type

[**PlayerGameProjection**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries

> [PlayerGameProjection] projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team)

Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries

> [PlayerGameProjection] projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week)

Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerSeasonStatsByPlayerWAdp

> PlayerSeasonProjection projectedPlayerSeasonStatsByPlayerWAdp(format, season, playerid)

Projected Player Season Stats by Player (w/ ADP)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.
apiInstance.projectedPlayerSeasonStatsByPlayerWAdp(format, season, playerid, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | 

### Return type

[**PlayerSeasonProjection**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerSeasonStatsByTeamWAdp

> [PlayerSeasonProjection] projectedPlayerSeasonStatsByTeamWAdp(format, season, team)

Projected Player Season Stats by Team (w/ ADP)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.projectedPlayerSeasonStatsByTeamWAdp(format, season, team, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[PlayerSeasonProjection]**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerSeasonStatsWAdp

> [PlayerSeasonProjection] projectedPlayerSeasonStatsWAdp(format, season)

Projected Player Season Stats (w/ ADP)

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.projectedPlayerSeasonStatsWAdp(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[PlayerSeasonProjection]**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## upcomingDfsSlateOwnershipProjections

> [DfsSlateWithOwnershipProjection] upcomingDfsSlateOwnershipProjections(format)

Upcoming DFS Slate Ownership Projections

Grabs DFS Slates which have not yet started for which we have DFS Ownership projections. 

### Example

```javascript
import NflV3Projections from 'nfl_v3_projections';
let defaultClient = NflV3Projections.ApiClient.instance;
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

let apiInstance = new NflV3Projections.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.upcomingDfsSlateOwnershipProjections(format, (error, data, response) => {
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

[**[DfsSlateWithOwnershipProjection]**](DfsSlateWithOwnershipProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

