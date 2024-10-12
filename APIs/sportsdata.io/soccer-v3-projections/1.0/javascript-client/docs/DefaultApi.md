# SoccerV3Projections.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/soccer/projections*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dfsSlatesByDate**](DefaultApi.md#dfsSlatesByDate) | **GET** /{format}/DfsSlatesByDate/{date} | Dfs Slates By Date
[**injuredPlayersByCompetition**](DefaultApi.md#injuredPlayersByCompetition) | **GET** /{format}/InjuredPlayers/{competition} | Injured Players By Competition
[**projectedPlayerGameStatsByCompetitionWDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByCompetitionWDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByCompetition/{competition}/{date} | Projected Player Game Stats by Competition (w/ DFS Salaries)
[**projectedPlayerGameStatsByDateWDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByDateWDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByDate/{date} | Projected Player Game Stats by Date (w/ DFS Salaries)
[**projectedPlayerGameStatsByPlayerWDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByPlayerWDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByPlayer/{date}/{playerid} | Projected Player Game Stats by Player (w/ DFS Salaries)
[**upcomingDfsSlatesByCompetition**](DefaultApi.md#upcomingDfsSlatesByCompetition) | **GET** /{format}/UpcomingDfsSlatesByCompetition/{competitionId} | Upcoming Dfs Slates By Competition



## dfsSlatesByDate

> [DfsSlate] dfsSlatesByDate(format, date)

Dfs Slates By Date

### Example

```javascript
import SoccerV3Projections from 'soccer_v3_projections';
let defaultClient = SoccerV3Projections.ApiClient.instance;
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

let apiInstance = new SoccerV3Projections.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2020-02-18</code> 
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2020-02-18&lt;/code&gt;  | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuredPlayersByCompetition

> [Player] injuredPlayersByCompetition(format, competition)

Injured Players By Competition

This endpoint provides all currently injured soccer players by competition, along with injury details.

### Example

```javascript
import SoccerV3Projections from 'soccer_v3_projections';
let defaultClient = SoccerV3Projections.ApiClient.instance;
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

let apiInstance = new SoccerV3Projections.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competition = "competition_example"; // String | An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>, <code>8</code>, etc.
apiInstance.injuredPlayersByCompetition(format, competition, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **competition** | **String**| An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: &lt;code&gt;EPL&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;MLS&lt;/code&gt;, &lt;code&gt;8&lt;/code&gt;, etc. | 

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByCompetitionWDfsSalaries

> [PlayerGameProjection] projectedPlayerGameStatsByCompetitionWDfsSalaries(format, competition, date)

Projected Player Game Stats by Competition (w/ DFS Salaries)

### Example

```javascript
import SoccerV3Projections from 'soccer_v3_projections';
let defaultClient = SoccerV3Projections.ApiClient.instance;
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

let apiInstance = new SoccerV3Projections.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competition = "competition_example"; // String | An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>, <code>8</code>, etc.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
apiInstance.projectedPlayerGameStatsByCompetitionWDfsSalaries(format, competition, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **competition** | **String**| An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: &lt;code&gt;EPL&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;MLS&lt;/code&gt;, &lt;code&gt;8&lt;/code&gt;, etc. | 
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByDateWDfsSalaries

> [PlayerGameProjection] projectedPlayerGameStatsByDateWDfsSalaries(format, date)

Projected Player Game Stats by Date (w/ DFS Salaries)

### Example

```javascript
import SoccerV3Projections from 'soccer_v3_projections';
let defaultClient = SoccerV3Projections.ApiClient.instance;
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

let apiInstance = new SoccerV3Projections.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
apiInstance.projectedPlayerGameStatsByDateWDfsSalaries(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByPlayerWDfsSalaries

> [PlayerGameProjection] projectedPlayerGameStatsByPlayerWDfsSalaries(format, date, playerid)

Projected Player Game Stats by Player (w/ DFS Salaries)

### Example

```javascript
import SoccerV3Projections from 'soccer_v3_projections';
let defaultClient = SoccerV3Projections.ApiClient.instance;
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

let apiInstance = new SoccerV3Projections.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>90026231</code>.
apiInstance.projectedPlayerGameStatsByPlayerWDfsSalaries(format, date, playerid, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;. | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## upcomingDfsSlatesByCompetition

> [DfsSlate] upcomingDfsSlatesByCompetition(format, competitionId)

Upcoming Dfs Slates By Competition

### Example

```javascript
import SoccerV3Projections from 'soccer_v3_projections';
let defaultClient = SoccerV3Projections.ApiClient.instance;
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

let apiInstance = new SoccerV3Projections.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competitionId = "competitionId_example"; // String | The Competition Id. <br>Examples: <code>3</code>
apiInstance.upcomingDfsSlatesByCompetition(format, competitionId, (error, data, response) => {
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
 **competitionId** | **String**| The Competition Id. &lt;br&gt;Examples: &lt;code&gt;3&lt;/code&gt; | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

