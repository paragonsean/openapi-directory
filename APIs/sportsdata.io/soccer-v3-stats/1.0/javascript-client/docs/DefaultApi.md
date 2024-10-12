# SoccerV3Stats.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/soccer/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areasCountries**](DefaultApi.md#areasCountries) | **GET** /{format}/Areas | Areas (Countries)
[**boxScore**](DefaultApi.md#boxScore) | **GET** /{format}/BoxScore/{gameid} | Box Score
[**boxScoresByDate**](DefaultApi.md#boxScoresByDate) | **GET** /{format}/BoxScores/{date} | Box Scores by Date
[**boxScoresByDateByCompetition**](DefaultApi.md#boxScoresByDateByCompetition) | **GET** /{format}/BoxScoresByCompetition/{competition}/{date} | Box Scores by Date by Competition
[**boxScoresByDateDelta**](DefaultApi.md#boxScoresByDateDelta) | **GET** /{format}/BoxScoresDelta/{date}/{minutes} | Box Scores by Date Delta
[**boxScoresDeltaByDateByCompetition**](DefaultApi.md#boxScoresDeltaByDateByCompetition) | **GET** /{format}/BoxScoresDeltaByCompetition/{competition}/{date}/{minutes} | Box Scores Delta by Date by Competition
[**competitionFixturesLeagueDetails**](DefaultApi.md#competitionFixturesLeagueDetails) | **GET** /{format}/CompetitionDetails/{competition} | Competition Fixtures (League Details)
[**competitionHierarchyLeagueHierarchy**](DefaultApi.md#competitionHierarchyLeagueHierarchy) | **GET** /{format}/CompetitionHierarchy | Competition Hierarchy (League Hierarchy)
[**competitionsLeagues**](DefaultApi.md#competitionsLeagues) | **GET** /{format}/Competitions | Competitions (Leagues)
[**dfsSlatesByDate**](DefaultApi.md#dfsSlatesByDate) | **GET** /{format}/DfsSlatesByDate/{date} | Dfs Slates By Date
[**gamesByDate**](DefaultApi.md#gamesByDate) | **GET** /{format}/GamesByDate/{date} | Games by Date
[**membershipsActive**](DefaultApi.md#membershipsActive) | **GET** /{format}/ActiveMemberships | Memberships (Active)
[**membershipsByCompetitionActive**](DefaultApi.md#membershipsByCompetitionActive) | **GET** /{format}/MembershipsByCompetition/{competition} | Memberships by Competition (Active)
[**membershipsByCompetitionHistorical**](DefaultApi.md#membershipsByCompetitionHistorical) | **GET** /{format}/HistoricalMembershipsByCompetition/{competition} | Memberships by Competition (Historical)
[**membershipsByTeamActive**](DefaultApi.md#membershipsByTeamActive) | **GET** /{format}/MembershipsByTeam/{teamid} | Memberships by Team (Active)
[**membershipsByTeamHistorical**](DefaultApi.md#membershipsByTeamHistorical) | **GET** /{format}/HistoricalMembershipsByTeam/{teamid} | Memberships by Team (Historical)
[**membershipsHistorical**](DefaultApi.md#membershipsHistorical) | **GET** /{format}/HistoricalMemberships | Memberships (Historical)
[**membershipsRecentlyChanged**](DefaultApi.md#membershipsRecentlyChanged) | **GET** /{format}/RecentlyChangedMemberships/{days} | Memberships (Recently Changed)
[**player**](DefaultApi.md#player) | **GET** /{format}/Player/{playerid} | Player
[**playerGameStatsByDate**](DefaultApi.md#playerGameStatsByDate) | **GET** /{format}/PlayerGameStatsByDate/{date} | Player Game Stats by Date
[**playerGameStatsByPlayer**](DefaultApi.md#playerGameStatsByPlayer) | **GET** /{format}/PlayerGameStatsByPlayer/{date}/{playerid} | Player Game Stats by Player
[**playerSeasonStats**](DefaultApi.md#playerSeasonStats) | **GET** /{format}/PlayerSeasonStats/{roundid} | Player Season Stats
[**playerSeasonStatsByPlayer**](DefaultApi.md#playerSeasonStatsByPlayer) | **GET** /{format}/PlayerSeasonStatsByPlayer/{roundid}/{playerid} | Player Season Stats by Player
[**playerSeasonStatsByTeam**](DefaultApi.md#playerSeasonStatsByTeam) | **GET** /{format}/PlayerSeasonStatsByTeam/{roundid}/{team} | Player Season Stats by Team
[**players**](DefaultApi.md#players) | **GET** /{format}/Players | Players
[**playersByTeam**](DefaultApi.md#playersByTeam) | **GET** /{format}/PlayersByTeam/{teamid} | Players by Team
[**schedule**](DefaultApi.md#schedule) | **GET** /{format}/Schedule/{roundid} | Schedule
[**seasonTeams**](DefaultApi.md#seasonTeams) | **GET** /{format}/SeasonTeams/{seasonid} | Season Teams
[**standings**](DefaultApi.md#standings) | **GET** /{format}/Standings/{roundid} | Standings
[**teamGameStatsByDate**](DefaultApi.md#teamGameStatsByDate) | **GET** /{format}/TeamGameStatsByDate/{date} | Team Game Stats by Date
[**teamSeasonStats**](DefaultApi.md#teamSeasonStats) | **GET** /{format}/TeamSeasonStats/{roundid} | Team Season Stats
[**teams**](DefaultApi.md#teams) | **GET** /{format}/Teams | Teams
[**upcomingDfsSlatesByCompetition**](DefaultApi.md#upcomingDfsSlatesByCompetition) | **GET** /{format}/UpcomingDfsSlatesByCompetition/{competitionId} | Upcoming Dfs Slates By Competition
[**upcomingScheduleByPlayer**](DefaultApi.md#upcomingScheduleByPlayer) | **GET** /{format}/UpcomingScheduleByPlayer/{playerid} | Upcoming Schedule By Player
[**venues**](DefaultApi.md#venues) | **GET** /{format}/Venues | Venues



## areasCountries

> [Area] areasCountries(format)

Areas (Countries)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.areasCountries(format, (error, data, response) => {
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

### Return type

[**[Area]**](Area.md)

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let gameid = "gameid_example"; // String | The GameID of a Soccer game.  GameIDs can be found in the Games API.  Valid entries are <code>702</code>, <code>1274</code>, etc.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **gameid** | **String**| The GameID of a Soccer game.  GameIDs can be found in the Games API.  Valid entries are &lt;code&gt;702&lt;/code&gt;, &lt;code&gt;1274&lt;/code&gt;, etc. | 

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoresByDateByCompetition

> [BoxScore] boxScoresByDateByCompetition(format, competition, date)

Box Scores by Date by Competition

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competition = "competition_example"; // String | An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>, <code>8</code>, etc.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
apiInstance.boxScoresByDateByCompetition(format, competition, date, (error, data, response) => {
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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
let minutes = "minutes_example"; // String | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 
 **minutes** | **String**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back. Valid entries are: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt; ... &lt;code&gt;all&lt;/code&gt;. | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoresDeltaByDateByCompetition

> [BoxScore] boxScoresDeltaByDateByCompetition(format, competition, date, minutes)

Box Scores Delta by Date by Competition

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competition = "competition_example"; // String | An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>, <code>8</code>, etc.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
let minutes = "minutes_example"; // String | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
apiInstance.boxScoresDeltaByDateByCompetition(format, competition, date, minutes, (error, data, response) => {
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
 **minutes** | **String**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back. Valid entries are: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt; ... &lt;code&gt;all&lt;/code&gt;. | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## competitionFixturesLeagueDetails

> CompetitionDetail competitionFixturesLeagueDetails(format, competition)

Competition Fixtures (League Details)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competition = "competition_example"; // String | An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>, <code>8</code>, etc.
apiInstance.competitionFixturesLeagueDetails(format, competition, (error, data, response) => {
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

[**CompetitionDetail**](CompetitionDetail.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## competitionHierarchyLeagueHierarchy

> [Area] competitionHierarchyLeagueHierarchy(format)

Competition Hierarchy (League Hierarchy)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.competitionHierarchyLeagueHierarchy(format, (error, data, response) => {
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

### Return type

[**[Area]**](Area.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## competitionsLeagues

> [Competition] competitionsLeagues(format)

Competitions (Leagues)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.competitionsLeagues(format, (error, data, response) => {
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

### Return type

[**[Competition]**](Competition.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dfsSlatesByDate

> [DfsSlate] dfsSlatesByDate(format, date)

Dfs Slates By Date

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2020-02-18</code>.
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
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2020-02-18&lt;/code&gt;. | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipsActive

> [Membership] membershipsActive(format)

Memberships (Active)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.membershipsActive(format, (error, data, response) => {
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

### Return type

[**[Membership]**](Membership.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipsByCompetitionActive

> [Membership] membershipsByCompetitionActive(format, competition)

Memberships by Competition (Active)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competition = "competition_example"; // String | An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>, <code>8</code>, etc.
apiInstance.membershipsByCompetitionActive(format, competition, (error, data, response) => {
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

[**[Membership]**](Membership.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipsByCompetitionHistorical

> [Membership] membershipsByCompetitionHistorical(format, competition)

Memberships by Competition (Historical)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competition = "competition_example"; // String | An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>, <code>8</code>, etc.
apiInstance.membershipsByCompetitionHistorical(format, competition, (error, data, response) => {
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

[**[Membership]**](Membership.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipsByTeamActive

> [Membership] membershipsByTeamActive(format, teamid)

Memberships by Team (Active)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let teamid = "teamid_example"; // String | Unique FantasyData Team ID.  Example:<code>516</code>.
apiInstance.membershipsByTeamActive(format, teamid, (error, data, response) => {
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
 **teamid** | **String**| Unique FantasyData Team ID.  Example:&lt;code&gt;516&lt;/code&gt;. | 

### Return type

[**[Membership]**](Membership.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipsByTeamHistorical

> [Membership] membershipsByTeamHistorical(format, teamid)

Memberships by Team (Historical)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let teamid = "teamid_example"; // String | Unique FantasyData Team ID.  Example:<code>516</code>.
apiInstance.membershipsByTeamHistorical(format, teamid, (error, data, response) => {
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
 **teamid** | **String**| Unique FantasyData Team ID.  Example:&lt;code&gt;516&lt;/code&gt;. | 

### Return type

[**[Membership]**](Membership.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipsHistorical

> [Membership] membershipsHistorical(format)

Memberships (Historical)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.membershipsHistorical(format, (error, data, response) => {
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

### Return type

[**[Membership]**](Membership.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipsRecentlyChanged

> [Membership] membershipsRecentlyChanged(format, days)

Memberships (Recently Changed)

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let days = "days_example"; // String | The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>, <code>2</code> ... <code>30</code>
apiInstance.membershipsRecentlyChanged(format, days, (error, data, response) => {
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
 **days** | **String**| The number of days since memberships were updated. For example, if you pass &lt;code&gt;3&lt;/code&gt;, you&#39;ll receive all memberships that have been updated in the past 3 days. Valid entries are: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt; ... &lt;code&gt;30&lt;/code&gt; | 

### Return type

[**[Membership]**](Membership.md)

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>90026231</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;. | 

### Return type

[**Player**](Player.md)

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsByPlayer

> [PlayerGame] playerGameStatsByPlayer(format, date, playerid)

Player Game Stats by Player

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>90026231</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;. | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStats

> [PlayerSeason] playerSeasonStats(format, roundid)

Player Season Stats

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
apiInstance.playerSeasonStats(format, roundid, (error, data, response) => {
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStatsByPlayer

> [PlayerSeason] playerSeasonStatsByPlayer(format, roundid, playerid)

Player Season Stats by Player

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>90026231</code>.
apiInstance.playerSeasonStatsByPlayer(format, roundid, playerid, (error, data, response) => {
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStatsByTeam

> [PlayerSeason] playerSeasonStatsByTeam(format, roundid, team)

Player Season Stats by Team

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
let team = "team_example"; // String | Unique FantasyData Team ID.  Example:<code>516</code>.
apiInstance.playerSeasonStatsByTeam(format, roundid, team, (error, data, response) => {
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc | 
 **team** | **String**| Unique FantasyData Team ID.  Example:&lt;code&gt;516&lt;/code&gt;. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playersByTeam

> [Player] playersByTeam(format, teamid)

Players by Team

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let teamid = "teamid_example"; // String | Unique FantasyData Team ID.  Example:<code>516</code>.
apiInstance.playersByTeam(format, teamid, (error, data, response) => {
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
 **teamid** | **String**| Unique FantasyData Team ID.  Example:&lt;code&gt;516&lt;/code&gt;. | 

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedule

> [Game] schedule(format, roundid)

Schedule

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
apiInstance.schedule(format, roundid, (error, data, response) => {
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## seasonTeams

> [SeasonTeam] seasonTeams(format, seasonid)

Season Teams

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let seasonid = "seasonid_example"; // String | Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
apiInstance.seasonTeams(format, seasonid, (error, data, response) => {
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
 **seasonid** | **String**| Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc | 

### Return type

[**[SeasonTeam]**](SeasonTeam.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## standings

> [Standing] standings(format, roundid)

Standings

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
apiInstance.standings(format, roundid, (error, data, response) => {
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc | 

### Return type

[**[Standing]**](Standing.md)

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 

### Return type

[**[TeamGame]**](TeamGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamSeasonStats

> [TeamSeason] teamSeasonStats(format, roundid)

Team Season Stats

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
apiInstance.teamSeasonStats(format, roundid, (error, data, response) => {
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc | 

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]

### Return type

[**[Team]**](Team.md)

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
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competitionId = "competitionId_example"; // String | The id of the competition. <br>Examples: <code>3</code>
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
 **competitionId** | **String**| The id of the competition. &lt;br&gt;Examples: &lt;code&gt;3&lt;/code&gt; | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## upcomingScheduleByPlayer

> [Game] upcomingScheduleByPlayer(format, playerid)

Upcoming Schedule By Player

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>90026231</code>.
apiInstance.upcomingScheduleByPlayer(format, playerid, (error, data, response) => {
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
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;. | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## venues

> [Venue] venues(format)

Venues

### Example

```javascript
import SoccerV3Stats from 'soccer_v3_stats';
let defaultClient = SoccerV3Stats.ApiClient.instance;
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

let apiInstance = new SoccerV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.venues(format, (error, data, response) => {
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

### Return type

[**[Venue]**](Venue.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

