# CsgoV3Stats.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/csgo/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areasCountries**](DefaultApi.md#areasCountries) | **GET** /{format}/Areas | Areas (Countries)
[**boxScore**](DefaultApi.md#boxScore) | **GET** /{format}/BoxScore/{gameid} | Box Score
[**boxScoresByDate**](DefaultApi.md#boxScoresByDate) | **GET** /{format}/BoxScores/{date} | Box Scores by Date
[**competitionFixturesLeagueDetails**](DefaultApi.md#competitionFixturesLeagueDetails) | **GET** /{format}/CompetitionDetails/{competitionid} | Competition Fixtures (League Details)
[**competitionsLeagues**](DefaultApi.md#competitionsLeagues) | **GET** /{format}/Competitions | Competitions (Leagues)
[**gamesByDate**](DefaultApi.md#gamesByDate) | **GET** /{format}/GamesByDate/{date} | Games by Date
[**membershipsActive**](DefaultApi.md#membershipsActive) | **GET** /{format}/ActiveMemberships | Memberships (Active)
[**membershipsByTeamActive**](DefaultApi.md#membershipsByTeamActive) | **GET** /{format}/MembershipsByTeam/{teamid} | Memberships by Team (Active)
[**membershipsByTeamHistorical**](DefaultApi.md#membershipsByTeamHistorical) | **GET** /{format}/HistoricalMembershipsByTeam/{teamid} | Memberships by Team (Historical)
[**membershipsHistorical**](DefaultApi.md#membershipsHistorical) | **GET** /{format}/HistoricalMemberships | Memberships (Historical)
[**player**](DefaultApi.md#player) | **GET** /{format}/Player/{playerid} | Player
[**players**](DefaultApi.md#players) | **GET** /{format}/Players | Players
[**playersByTeam**](DefaultApi.md#playersByTeam) | **GET** /{format}/PlayersByTeam/{teamid} | Players by Team
[**schedule**](DefaultApi.md#schedule) | **GET** /{format}/Schedule/{roundid} | Schedule
[**seasonTeams**](DefaultApi.md#seasonTeams) | **GET** /{format}/SeasonTeams/{seasonid} | Season Teams
[**standings**](DefaultApi.md#standings) | **GET** /{format}/Standings/{roundid} | Standings
[**teams**](DefaultApi.md#teams) | **GET** /{format}/Teams | Teams
[**venues**](DefaultApi.md#venues) | **GET** /{format}/Venues | Venues



## areasCountries

> [Area] areasCountries(format)

Areas (Countries)

Areas (Countries)

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
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

> [BoxScore] boxScore(format, gameid)

Box Score

Box Scores by Date

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let gameid = "gameid_example"; // String | Unique GameId for the desired box scores. Examples: <code>100000091</code>
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
 **gameid** | **String**| Unique GameId for the desired box scores. Examples: &lt;code&gt;100000091&lt;/code&gt; | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoresByDate

> [BoxScore] boxScoresByDate(format, date)

Box Scores by Date

Box Scores by Date

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-01-13</code>, <code>2018-06-13</code>.
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
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-01-13&lt;/code&gt;, &lt;code&gt;2018-06-13&lt;/code&gt;. | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## competitionFixturesLeagueDetails

> CompetitionDetail competitionFixturesLeagueDetails(format, competitionid)

Competition Fixtures (League Details)

Competition Fixtures (League Details)

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let competitionid = "competitionid_example"; // String | A CS:GO competition/league unique CompetitionId. Possible values include: <code>100000009</code>, etc.
apiInstance.competitionFixturesLeagueDetails(format, competitionid, (error, data, response) => {
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
 **competitionid** | **String**| A CS:GO competition/league unique CompetitionId. Possible values include: &lt;code&gt;100000009&lt;/code&gt;, etc. | 

### Return type

[**CompetitionDetail**](CompetitionDetail.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## competitionsLeagues

> [Competition] competitionsLeagues(format)

Competitions (Leagues)

Competitions (Leagues)

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
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


## gamesByDate

> [Game] gamesByDate(format, date)

Games by Date

Games by Date

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2018-01-13</code>, <code>2018-06-13</code>.
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
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-01-13&lt;/code&gt;, &lt;code&gt;2018-06-13&lt;/code&gt;. | 

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

Memberships (Active)

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
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


## membershipsByTeamActive

> [Membership] membershipsByTeamActive(format, teamid)

Memberships by Team (Active)

Memberships by Team (Active)

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let teamid = "teamid_example"; // String | Unique FantasyData Team ID.  Example:<code>100000001</code>.
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
 **teamid** | **String**| Unique FantasyData Team ID.  Example:&lt;code&gt;100000001&lt;/code&gt;. | 

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

Memberships by Team (Historical)

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let teamid = "teamid_example"; // String | Unique FantasyData Team ID.  Example:<code>100000001</code>.
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
 **teamid** | **String**| Unique FantasyData Team ID.  Example:&lt;code&gt;100000001&lt;/code&gt;. | 

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

Memberships (Historical)

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
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


## player

> Player player(format, playerid)

Player

Player

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>100000576</code>.
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
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;100000576&lt;/code&gt;. | 

### Return type

[**Player**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## players

> [Player] players(format)

Players

Players

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
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

Players by Team

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let teamid = "teamid_example"; // String | Unique FantasyData Team ID.  Example:<code>100000001</code>.
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
 **teamid** | **String**| Unique FantasyData Team ID.  Example:&lt;code&gt;100000001&lt;/code&gt;. | 

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

Schedule

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competitions and Competition Details endpoints.  Examples: <code>100000138</code>, <code>1000001412</code>, etc
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competitions and Competition Details endpoints.  Examples: &lt;code&gt;100000138&lt;/code&gt;, &lt;code&gt;1000001412&lt;/code&gt;, etc | 

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

Season Teams

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let seasonid = "seasonid_example"; // String | Unique FantasyData Season ID. SeasonIDs can be found in the Competitions and Competition Details endpoints.  Examples: <code>100000023</code>, <code>100000024</code>, etc
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
 **seasonid** | **String**| Unique FantasyData Season ID. SeasonIDs can be found in the Competitions and Competition Details endpoints.  Examples: &lt;code&gt;100000023&lt;/code&gt;, &lt;code&gt;100000024&lt;/code&gt;, etc | 

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

Schedule

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let roundid = "roundid_example"; // String | Unique FantasyData Round ID. RoundIDs can be found in the Competitions and Competition Details endpoints.  Example: <code>100000138</code>, etc
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
 **roundid** | **String**| Unique FantasyData Round ID. RoundIDs can be found in the Competitions and Competition Details endpoints.  Example: &lt;code&gt;100000138&lt;/code&gt;, etc | 

### Return type

[**[Standing]**](Standing.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams

> [Team] teams(format)

Teams

Teams

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
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


## venues

> [Venue] venues(format)

Venues

Venues

### Example

```javascript
import CsgoV3Stats from 'csgo_v3_stats';
let defaultClient = CsgoV3Stats.ApiClient.instance;
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

let apiInstance = new CsgoV3Stats.DefaultApi();
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

