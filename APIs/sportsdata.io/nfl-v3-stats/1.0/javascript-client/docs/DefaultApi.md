# NflV3Stats.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/nfl/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areGamesInProgress**](DefaultApi.md#areGamesInProgress) | **GET** /{format}/AreAnyGamesInProgress | Are Games In Progress
[**boxScoreByScoreidV**](DefaultApi.md#boxScoreByScoreidV) | **GET** /{format}/BoxScoreByScoreIDV3/{scoreid} | Box Score by ScoreID V3
[**boxScoreV**](DefaultApi.md#boxScoreV) | **GET** /{format}/BoxScoreV3/{season}/{week}/{hometeam} | Box Score V3
[**boxScoresDeltaV**](DefaultApi.md#boxScoresDeltaV) | **GET** /{format}/BoxScoresDeltaV3/{season}/{week}/{playerstoinclude}/{minutes} | Box Scores Delta V3
[**boxScoresVSimulation**](DefaultApi.md#boxScoresVSimulation) | **GET** /{format}/SimulatedBoxScoresV3/{numberofplays} | Box Scores V3 Simulation
[**byeWeeks**](DefaultApi.md#byeWeeks) | **GET** /{format}/Byes/{season} | Bye Weeks
[**dailyFantasyPlayers**](DefaultApi.md#dailyFantasyPlayers) | **GET** /{format}/DailyFantasyPlayers/{date} | Daily Fantasy Players
[**dailyFantasyScoring**](DefaultApi.md#dailyFantasyScoring) | **GET** /{format}/DailyFantasyPoints/{date} | Daily Fantasy Scoring
[**dfsSlatesByDate**](DefaultApi.md#dfsSlatesByDate) | **GET** /{format}/DfsSlatesByDate/{date} | DFS Slates by Date
[**dfsSlatesByWeek**](DefaultApi.md#dfsSlatesByWeek) | **GET** /{format}/DfsSlatesByWeek/{season}/{week} | DFS Slates by Week
[**fantasyDefenseGameStats**](DefaultApi.md#fantasyDefenseGameStats) | **GET** /{format}/FantasyDefenseByGame/{season}/{week} | Fantasy Defense Game Stats
[**fantasyDefenseGameStatsByTeam**](DefaultApi.md#fantasyDefenseGameStatsByTeam) | **GET** /{format}/FantasyDefenseByGameByTeam/{season}/{week}/{team} | Fantasy Defense Game Stats by Team
[**fantasyDefenseSeasonStats**](DefaultApi.md#fantasyDefenseSeasonStats) | **GET** /{format}/FantasyDefenseBySeason/{season} | Fantasy Defense Season Stats
[**fantasyDefenseSeasonStatsByTeam**](DefaultApi.md#fantasyDefenseSeasonStatsByTeam) | **GET** /{format}/FantasyDefenseBySeasonByTeam/{season}/{team} | Fantasy Defense Season Stats by Team
[**fantasyPlayerOwnershipPercentagesSeasonLong**](DefaultApi.md#fantasyPlayerOwnershipPercentagesSeasonLong) | **GET** /{format}/PlayerOwnership/{season}/{week} | Fantasy Player Ownership Percentages (Season-Long)
[**fantasyPlayersWithAdp**](DefaultApi.md#fantasyPlayersWithAdp) | **GET** /{format}/FantasyPlayers | Fantasy Players with ADP
[**gameStatsBySeasonDeprecatedUseTeamGameStatsInstead**](DefaultApi.md#gameStatsBySeasonDeprecatedUseTeamGameStatsInstead) | **GET** /{format}/GameStats/{season} | Game Stats by Season (Deprecated, use Team Game Stats instead)
[**gameStatsByWeekDeprecatedUseTeamGameStatsInstead**](DefaultApi.md#gameStatsByWeekDeprecatedUseTeamGameStatsInstead) | **GET** /{format}/GameStatsByWeek/{season}/{week} | Game Stats by Week (Deprecated, use Team Game Stats instead)
[**idpFantasyPlayersWithAdp**](DefaultApi.md#idpFantasyPlayersWithAdp) | **GET** /{format}/FantasyPlayersIDP | IDP Fantasy Players with ADP
[**injuries**](DefaultApi.md#injuries) | **GET** /{format}/Injuries/{season}/{week} | Injuries
[**injuriesByTeam**](DefaultApi.md#injuriesByTeam) | **GET** /{format}/Injuries/{season}/{week}/{team} | Injuries by Team
[**leagueLeadersBySeason**](DefaultApi.md#leagueLeadersBySeason) | **GET** /{format}/SeasonLeagueLeaders/{season}/{position}/{column} | League Leaders by Season
[**leagueLeadersByWeek**](DefaultApi.md#leagueLeadersByWeek) | **GET** /{format}/GameLeagueLeaders/{season}/{week}/{position}/{column} | League Leaders by Week
[**legacyBoxScore**](DefaultApi.md#legacyBoxScore) | **GET** /{format}/BoxScore/{season}/{week}/{hometeam} | Legacy Box Score
[**legacyBoxScores**](DefaultApi.md#legacyBoxScores) | **GET** /{format}/BoxScores/{season}/{week} | Legacy Box Scores
[**legacyBoxScoresActive**](DefaultApi.md#legacyBoxScoresActive) | **GET** /{format}/ActiveBoxScores | Legacy Box Scores Active
[**legacyBoxScoresDelta**](DefaultApi.md#legacyBoxScoresDelta) | **GET** /{format}/BoxScoresDelta/{season}/{week}/{minutes} | Legacy Box Scores Delta
[**legacyBoxScoresDeltaCurrentWeek**](DefaultApi.md#legacyBoxScoresDeltaCurrentWeek) | **GET** /{format}/RecentlyUpdatedBoxScores/{minutes} | Legacy Box Scores Delta (Current Week)
[**legacyBoxScoresFinal**](DefaultApi.md#legacyBoxScoresFinal) | **GET** /{format}/FinalBoxScores | Legacy Box Scores Final
[**legacyBoxScoresLive**](DefaultApi.md#legacyBoxScoresLive) | **GET** /{format}/LiveBoxScores | Legacy Box Scores Live
[**news**](DefaultApi.md#news) | **GET** /{format}/News | News
[**newsByDate**](DefaultApi.md#newsByDate) | **GET** /{format}/NewsByDate/{date} | News by Date
[**newsByPlayer**](DefaultApi.md#newsByPlayer) | **GET** /{format}/NewsByPlayerID/{playerid} | News by Player
[**newsByTeam**](DefaultApi.md#newsByTeam) | **GET** /{format}/NewsByTeam/{team} | News by Team
[**playerDetailsByAvailable**](DefaultApi.md#playerDetailsByAvailable) | **GET** /{format}/Players | Player Details by Available
[**playerDetailsByFreeAgents**](DefaultApi.md#playerDetailsByFreeAgents) | **GET** /{format}/FreeAgents | Player Details by Free Agents
[**playerDetailsByPlayer**](DefaultApi.md#playerDetailsByPlayer) | **GET** /{format}/Player/{playerid} | Player Details by Player
[**playerDetailsByRookieDraftYear**](DefaultApi.md#playerDetailsByRookieDraftYear) | **GET** /{format}/Rookies/{season} | Player Details by Rookie Draft Year
[**playerDetailsByTeam**](DefaultApi.md#playerDetailsByTeam) | **GET** /{format}/Players/{team} | Player Details by Team
[**playerGameLogsBySeason**](DefaultApi.md#playerGameLogsBySeason) | **GET** /{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames} | Player Game Logs By Season
[**playerGameRedZoneStats**](DefaultApi.md#playerGameRedZoneStats) | **GET** /{format}/PlayerGameRedZoneStats/{season}/{week} | Player Game Red Zone Stats
[**playerGameRedZoneStatsInsideFive**](DefaultApi.md#playerGameRedZoneStatsInsideFive) | **GET** /{format}/PlayerGameRedZoneInsideFiveStats/{season}/{week} | Player Game Red Zone Stats Inside Five
[**playerGameRedZoneStatsInsideTen**](DefaultApi.md#playerGameRedZoneStatsInsideTen) | **GET** /{format}/PlayerGameRedZoneInsideTenStats/{season}/{week} | Player Game Red Zone Stats Inside Ten
[**playerGameStatsByPlayer**](DefaultApi.md#playerGameStatsByPlayer) | **GET** /{format}/PlayerGameStatsByPlayerID/{season}/{week}/{playerid} | Player Game Stats by Player
[**playerGameStatsByTeam**](DefaultApi.md#playerGameStatsByTeam) | **GET** /{format}/PlayerGameStatsByTeam/{season}/{week}/{team} | Player Game Stats by Team
[**playerGameStatsByWeek**](DefaultApi.md#playerGameStatsByWeek) | **GET** /{format}/PlayerGameStatsByWeek/{season}/{week} | Player Game Stats by Week
[**playerGameStatsByWeekDelta**](DefaultApi.md#playerGameStatsByWeekDelta) | **GET** /{format}/PlayerGameStatsByWeekDelta/{season}/{week}/{minutes} | Player Game Stats by Week Delta
[**playerGameStatsDelta**](DefaultApi.md#playerGameStatsDelta) | **GET** /{format}/PlayerGameStatsDelta/{minutes} | Player Game Stats Delta
[**playerSeasonRedZoneStats**](DefaultApi.md#playerSeasonRedZoneStats) | **GET** /{format}/PlayerSeasonRedZoneStats/{season} | Player Season Red Zone Stats
[**playerSeasonRedZoneStatsInsideFive**](DefaultApi.md#playerSeasonRedZoneStatsInsideFive) | **GET** /{format}/PlayerSeasonRedZoneInsideFiveStats/{season} | Player Season Red Zone Stats Inside Five
[**playerSeasonRedZoneStatsInsideTen**](DefaultApi.md#playerSeasonRedZoneStatsInsideTen) | **GET** /{format}/PlayerSeasonRedZoneInsideTenStats/{season} | Player Season Red Zone Stats Inside Ten
[**playerSeasonStats**](DefaultApi.md#playerSeasonStats) | **GET** /{format}/PlayerSeasonStats/{season} | Player Season Stats
[**playerSeasonStatsByPlayer**](DefaultApi.md#playerSeasonStatsByPlayer) | **GET** /{format}/PlayerSeasonStatsByPlayerID/{season}/{playerid} | Player Season Stats by Player
[**playerSeasonStatsByTeam**](DefaultApi.md#playerSeasonStatsByTeam) | **GET** /{format}/PlayerSeasonStatsByTeam/{season}/{team} | Player Season Stats by Team
[**playerSeasonThirdDownStats**](DefaultApi.md#playerSeasonThirdDownStats) | **GET** /{format}/PlayerSeasonThirdDownStats/{season} | Player Season Third Down Stats
[**proBowlers**](DefaultApi.md#proBowlers) | **GET** /{format}/ProBowlers/{season} | Pro Bowlers
[**schedule**](DefaultApi.md#schedule) | **GET** /{format}/Schedules/{season} | Schedule
[**scoresByDate**](DefaultApi.md#scoresByDate) | **GET** /{format}/ScoresByDate/{date} | Scores by Date
[**scoresBySeason**](DefaultApi.md#scoresBySeason) | **GET** /{format}/Scores/{season} | Scores by Season 
[**scoresByWeek**](DefaultApi.md#scoresByWeek) | **GET** /{format}/ScoresByWeek/{season}/{week} | Scores by Week
[**scoresByWeekSimulation**](DefaultApi.md#scoresByWeekSimulation) | **GET** /{format}/SimulatedScores/{numberofplays} | Scores by Week Simulation
[**seasonCurrent**](DefaultApi.md#seasonCurrent) | **GET** /{format}/CurrentSeason | Season Current
[**seasonLastCompleted**](DefaultApi.md#seasonLastCompleted) | **GET** /{format}/LastCompletedSeason | Season Last Completed
[**seasonUpcoming**](DefaultApi.md#seasonUpcoming) | **GET** /{format}/UpcomingSeason | Season Upcoming
[**stadiums**](DefaultApi.md#stadiums) | **GET** /{format}/Stadiums | Stadiums
[**standings**](DefaultApi.md#standings) | **GET** /{format}/Standings/{season} | Standings
[**teamGameLogsBySeason**](DefaultApi.md#teamGameLogsBySeason) | **GET** /{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames} | Team Game Logs By Season
[**teamGameStats**](DefaultApi.md#teamGameStats) | **GET** /{format}/TeamGameStats/{season}/{week} | Team Game Stats
[**teamSeasonStats**](DefaultApi.md#teamSeasonStats) | **GET** /{format}/TeamSeasonStats/{season} | Team Season Stats
[**teamsActive**](DefaultApi.md#teamsActive) | **GET** /{format}/Teams | Teams (Active)
[**teamsAll**](DefaultApi.md#teamsAll) | **GET** /{format}/AllTeams | Teams (All)
[**teamsBySeason**](DefaultApi.md#teamsBySeason) | **GET** /{format}/Teams/{season} | Teams by Season
[**timeframes**](DefaultApi.md#timeframes) | **GET** /{format}/Timeframes/{type} | Timeframes
[**weekCurrent**](DefaultApi.md#weekCurrent) | **GET** /{format}/CurrentWeek | Week Current
[**weekLastCompleted**](DefaultApi.md#weekLastCompleted) | **GET** /{format}/LastCompletedWeek | Week Last Completed
[**weekUpcoming**](DefaultApi.md#weekUpcoming) | **GET** /{format}/UpcomingWeek | Week Upcoming



## areGamesInProgress

> Boolean areGamesInProgress(format)

Are Games In Progress

Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
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


## boxScoreByScoreidV

> BoxScoreV3 boxScoreByScoreidV(format, scoreid)

Box Score by ScoreID V3

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let scoreid = "scoreid_example"; // String | The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
apiInstance.boxScoreByScoreidV(format, scoreid, (error, data, response) => {
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
 **scoreid** | **String**| The ScoreID of the game. Possible values include: &lt;code&gt;16247&lt;/code&gt;, &lt;code&gt;16245&lt;/code&gt;, etc. | 

### Return type

[**BoxScoreV3**](BoxScoreV3.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoreV

> BoxScoreV3 boxScoreV(format, season, week, hometeam)

Box Score V3

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let hometeam = "hometeam_example"; // String | Abbreviation of a team playing in this game. Example: <code>WAS</code>.
apiInstance.boxScoreV(format, season, week, hometeam, (error, data, response) => {
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
 **hometeam** | **String**| Abbreviation of a team playing in this game. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**BoxScoreV3**](BoxScoreV3.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoresDeltaV

> [BoxScoreV3] boxScoresDeltaV(format, season, week, playerstoinclude, minutes)

Box Scores Delta V3

This method returns all box scores for a given season and week, but only returns player stats that have changed in the last X minutes. You can also filter by type of player stats to include, such as traditional fantasy players, IDP players or all players.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let playerstoinclude = "'all'"; // String | The subcategory of players to include in the returned PlayerGame records. Possible values include:<br><br> <code>all</code> Returns all players<br> <code>fantasy</code> Returns traditional fantasy players (QB, RB, WR, TE, K, DST)<br> <code>idp</code> Returns traditional fantasy players and IDP players.
let minutes = "minutes_example"; // String | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br><code>1</code>,  <code>2</code>, etc.         
apiInstance.boxScoresDeltaV(format, season, week, playerstoinclude, minutes, (error, data, response) => {
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
 **playerstoinclude** | **String**| The subcategory of players to include in the returned PlayerGame records. Possible values include:&lt;br&gt;&lt;br&gt; &lt;code&gt;all&lt;/code&gt; Returns all players&lt;br&gt; &lt;code&gt;fantasy&lt;/code&gt; Returns traditional fantasy players (QB, RB, WR, TE, K, DST)&lt;br&gt; &lt;code&gt;idp&lt;/code&gt; Returns traditional fantasy players and IDP players. | [default to &#39;all&#39;]
 **minutes** | **String**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;&lt;code&gt;1&lt;/code&gt;,  &lt;code&gt;2&lt;/code&gt;, etc.          | 

### Return type

[**[BoxScoreV3]**](BoxScoreV3.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boxScoresVSimulation

> [BoxScoreV3] boxScoresVSimulation(format, numberofplays)

Box Scores V3 Simulation

Gets simulated live box scores of NFL games, covering the Conference Championship games on January 21, 2018.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let numberofplays = "numberofplays_example"; // String | The number of plays to progress in this NFL live game simulation. Example entries are <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
apiInstance.boxScoresVSimulation(format, numberofplays, (error, data, response) => {
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
 **numberofplays** | **String**| The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. | 

### Return type

[**[BoxScoreV3]**](BoxScoreV3.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## byeWeeks

> [Bye] byeWeeks(format, season)

Bye Weeks

Get bye weeks for the teams during a specified NFL season. 

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.byeWeeks(format, season, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[Bye]**](Bye.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dailyFantasyPlayers

> [DailyFantasyPlayer] dailyFantasyPlayers(format, date)

Daily Fantasy Players

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String |            The date of the contest for which you're pulling players           <code>2014-SEP-21</code>,           <code>2014-NOV-15</code>, etc         
apiInstance.dailyFantasyPlayers(format, date, (error, data, response) => {
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
 **date** | **String**|            The date of the contest for which you&#39;re pulling players           &lt;code&gt;2014-SEP-21&lt;/code&gt;,           &lt;code&gt;2014-NOV-15&lt;/code&gt;, etc          | 

### Return type

[**[DailyFantasyPlayer]**](DailyFantasyPlayer.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dailyFantasyScoring

> [DailyFantasyScoring] dailyFantasyScoring(format, date)

Daily Fantasy Scoring

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the contest for which you're pulling players           <code>2014-SEP-21</code>,           <code>2014-NOV-15</code>, etc
apiInstance.dailyFantasyScoring(format, date, (error, data, response) => {
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
 **date** | **String**| The date of the contest for which you&#39;re pulling players           &lt;code&gt;2014-SEP-21&lt;/code&gt;,           &lt;code&gt;2014-NOV-15&lt;/code&gt;, etc | 

### Return type

[**[DailyFantasyScoring]**](DailyFantasyScoring.md)

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
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
 **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fantasyDefenseGameStats

> [FantasyDefenseGame] fantasyDefenseGameStats(format, season, week)

Fantasy Defense Game Stats

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.fantasyDefenseGameStats(format, season, week, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[FantasyDefenseGame]**](FantasyDefenseGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fantasyDefenseGameStatsByTeam

> FantasyDefenseGame fantasyDefenseGameStatsByTeam(format, season, week, team)

Fantasy Defense Game Stats by Team

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.fantasyDefenseGameStatsByTeam(format, season, week, team, (error, data, response) => {
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

[**FantasyDefenseGame**](FantasyDefenseGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fantasyDefenseSeasonStats

> [FantasyDefenseSeason] fantasyDefenseSeasonStats(format, season)

Fantasy Defense Season Stats

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.fantasyDefenseSeasonStats(format, season, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[FantasyDefenseSeason]**](FantasyDefenseSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fantasyDefenseSeasonStatsByTeam

> FantasyDefenseSeason fantasyDefenseSeasonStatsByTeam(format, season, team)

Fantasy Defense Season Stats by Team

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.fantasyDefenseSeasonStatsByTeam(format, season, team, (error, data, response) => {
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

[**FantasyDefenseSeason**](FantasyDefenseSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fantasyPlayerOwnershipPercentagesSeasonLong

> [PlayerOwnership] fantasyPlayerOwnershipPercentagesSeasonLong(format, season, week)

Fantasy Player Ownership Percentages (Season-Long)

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.fantasyPlayerOwnershipPercentagesSeasonLong(format, season, week, (error, data, response) => {
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

[**[PlayerOwnership]**](PlayerOwnership.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fantasyPlayersWithAdp

> [FantasyPlayer] fantasyPlayersWithAdp(format)

Fantasy Players with ADP

This method returns a comprehensive list of draftable fantasy football players, including QB, RB, WR, TE, K and DEF.  Players are sorted by ADP (AverageDraftPosition).

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.fantasyPlayersWithAdp(format, (error, data, response) => {
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

[**[FantasyPlayer]**](FantasyPlayer.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gameStatsBySeasonDeprecatedUseTeamGameStatsInstead

> [Game] gameStatsBySeasonDeprecatedUseTeamGameStatsInstead(format, season)

Game Stats by Season (Deprecated, use Team Game Stats instead)

Game stats for a specified season.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.gameStatsBySeasonDeprecatedUseTeamGameStatsInstead(format, season, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gameStatsByWeekDeprecatedUseTeamGameStatsInstead

> [Game] gameStatsByWeekDeprecatedUseTeamGameStatsInstead(format, season, week)

Game Stats by Week (Deprecated, use Team Game Stats instead)

Game stats for a specified season and week.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.gameStatsByWeekDeprecatedUseTeamGameStatsInstead(format, season, week, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[Game]**](Game.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idpFantasyPlayersWithAdp

> [FantasyPlayer] idpFantasyPlayersWithAdp(format)

IDP Fantasy Players with ADP

This method returns the top 300+ IDP Fantasy Players for the current or upcoming season, ordered by AverageDraftPositionIDP.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.idpFantasyPlayersWithAdp(format, (error, data, response) => {
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

[**[FantasyPlayer]**](FantasyPlayer.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuries

> [Injury] injuries(format, season, week)

Injuries

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.injuries(format, season, week, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[Injury]**](Injury.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## injuriesByTeam

> [Injury] injuriesByTeam(format, season, week, team)

Injuries by Team

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.injuriesByTeam(format, season, week, team, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[Injury]**](Injury.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## leagueLeadersBySeason

> [PlayerSeason] leagueLeadersBySeason(format, season, position, column)

League Leaders by Season

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let position = "'ALL'"; // String | Playerâ€™s position that you would like to filter by.
let column = "column_example"; // String | Response member you would like results sorted by.
apiInstance.leagueLeadersBySeason(format, season, position, column, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **position** | **String**| Playerâ€™s position that you would like to filter by. | [default to &#39;ALL&#39;]
 **column** | **String**| Response member you would like results sorted by. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## leagueLeadersByWeek

> [PlayerGame] leagueLeadersByWeek(format, season, week, position, column)

League Leaders by Week

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String |            Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.         
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let position = "'ALL'"; // String | Playerâ€™s position that you would like to filter by.
let column = "column_example"; // String | Response member you would like results sorted by.
apiInstance.leagueLeadersByWeek(format, season, week, position, column, (error, data, response) => {
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
 **format** | **String**|            Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.          | [default to &#39;XML&#39;]
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **position** | **String**| Playerâ€™s position that you would like to filter by. | [default to &#39;ALL&#39;]
 **column** | **String**| Response member you would like results sorted by. | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyBoxScore

> BoxScore legacyBoxScore(format, season, week, hometeam)

Legacy Box Score

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let hometeam = "hometeam_example"; // String | Abbreviation of the home team. Example: <code>WAS</code>.
apiInstance.legacyBoxScore(format, season, week, hometeam, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **hometeam** | **String**| Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**BoxScore**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyBoxScores

> [BoxScore] legacyBoxScores(format, season, week)

Legacy Box Scores

This method returns all box scores for a given season and week.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.legacyBoxScores(format, season, week, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyBoxScoresActive

> [BoxScore] legacyBoxScoresActive(format)

Legacy Box Scores Active

This method returns box scores for all games that are either in-progress or have been updated within the last 30 minutes.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.legacyBoxScoresActive(format, (error, data, response) => {
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

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyBoxScoresDelta

> [BoxScore] legacyBoxScoresDelta(format, season, week, minutes)

Legacy Box Scores Delta

This method returns all box scores for a given season and week, but only returns player stats that have changed in the last X minutes.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let minutes = "minutes_example"; // String | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.         
apiInstance.legacyBoxScoresDelta(format, season, week, minutes, (error, data, response) => {
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
 **minutes** | **String**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyBoxScoresDeltaCurrentWeek

> [BoxScore] legacyBoxScoresDeltaCurrentWeek(format, minutes)

Legacy Box Scores Delta (Current Week)

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let minutes = "minutes_example"; // String | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.         
apiInstance.legacyBoxScoresDeltaCurrentWeek(format, minutes, (error, data, response) => {
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
 **minutes** | **String**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyBoxScoresFinal

> [BoxScore] legacyBoxScoresFinal(format)

Legacy Box Scores Final

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.legacyBoxScoresFinal(format, (error, data, response) => {
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

[**[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyBoxScoresLive

> [BoxScore] legacyBoxScoresLive(format)

Legacy Box Scores Live

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.legacyBoxScoresLive(format, (error, data, response) => {
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

[**[BoxScore]**](BoxScore.md)

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **date** | **String**| The date of the news. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;. | 

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String |            Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.         
let playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.
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
 **format** | **String**|            Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.          | 
 **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | 

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## newsByTeam

> [News] newsByTeam(format, team)

News by Team

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.newsByTeam(format, team, (error, data, response) => {
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
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByAvailable

> [Player] playerDetailsByAvailable(format)

Player Details by Available

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.playerDetailsByAvailable(format, (error, data, response) => {
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


## playerDetailsByFreeAgents

> [Player] playerDetailsByFreeAgents(format)

Player Details by Free Agents

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.playerDetailsByFreeAgents(format, (error, data, response) => {
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

> PlayerDetail playerDetailsByPlayer(format, playerid)

Player Details by Player

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>732</code>.
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
 **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;. | 

### Return type

[**PlayerDetail**](PlayerDetail.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByRookieDraftYear

> [Player] playerDetailsByRookieDraftYear(format, season)

Player Details by Rookie Draft Year

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
apiInstance.playerDetailsByRookieDraftYear(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season.&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**[Player]**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerDetailsByTeam

> [PlayerDetail] playerDetailsByTeam(format, team)

Player Details by Team

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
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
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[PlayerDetail]**](PlayerDetail.md)

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Season to get games from. Example <code>2019POST</code>, <code>2020</code>
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>17920</code>.
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
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;17920&lt;/code&gt;. | 
 **numberofgames** | **String**| How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt; | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameRedZoneStats

> [PlayerGameRedZone] playerGameRedZoneStats(format, season, week)

Player Game Red Zone Stats

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.playerGameRedZoneStats(format, season, week, (error, data, response) => {
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

[**[PlayerGameRedZone]**](PlayerGameRedZone.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameRedZoneStatsInsideFive

> [PlayerGameRedZone] playerGameRedZoneStatsInsideFive(format, season, week)

Player Game Red Zone Stats Inside Five

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.playerGameRedZoneStatsInsideFive(format, season, week, (error, data, response) => {
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

[**[PlayerGameRedZone]**](PlayerGameRedZone.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameRedZoneStatsInsideTen

> [PlayerGameRedZone] playerGameRedZoneStatsInsideTen(format, season, week)

Player Game Red Zone Stats Inside Ten

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.playerGameRedZoneStatsInsideTen(format, season, week, (error, data, response) => {
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

[**[PlayerGameRedZone]**](PlayerGameRedZone.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsByPlayer

> PlayerGame playerGameStatsByPlayer(format, season, week, playerid)

Player Game Stats by Player

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>732</code>.
apiInstance.playerGameStatsByPlayer(format, season, week, playerid, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;. | 

### Return type

[**PlayerGame**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsByTeam

> [PlayerGame] playerGameStatsByTeam(format, season, week, team)

Player Game Stats by Team

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.playerGameStatsByTeam(format, season, week, team, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsByWeek

> [PlayerGame] playerGameStatsByWeek(format, season, week)

Player Game Stats by Week

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.playerGameStatsByWeek(format, season, week, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsByWeekDelta

> [PlayerGame] playerGameStatsByWeekDelta(format, season, week, minutes)

Player Game Stats by Week Delta

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
let minutes = "minutes_example"; // String | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.         
apiInstance.playerGameStatsByWeekDelta(format, season, week, minutes, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **minutes** | **String**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerGameStatsDelta

> [PlayerGame] playerGameStatsDelta(format, minutes)

Player Game Stats Delta

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let minutes = "minutes_example"; // String |            Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:           <code>1</code> or <code>2</code>.         
apiInstance.playerGameStatsDelta(format, minutes, (error, data, response) => {
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
 **minutes** | **String**|            Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonRedZoneStats

> [PlayerSeasonRedZone] playerSeasonRedZoneStats(format, season)

Player Season Red Zone Stats

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.playerSeasonRedZoneStats(format, season, (error, data, response) => {
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

[**[PlayerSeasonRedZone]**](PlayerSeasonRedZone.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonRedZoneStatsInsideFive

> [PlayerSeasonRedZone] playerSeasonRedZoneStatsInsideFive(format, season)

Player Season Red Zone Stats Inside Five

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.playerSeasonRedZoneStatsInsideFive(format, season, (error, data, response) => {
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

[**[PlayerSeasonRedZone]**](PlayerSeasonRedZone.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonRedZoneStatsInsideTen

> [PlayerSeasonRedZone] playerSeasonRedZoneStatsInsideTen(format, season)

Player Season Red Zone Stats Inside Ten

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.playerSeasonRedZoneStatsInsideTen(format, season, (error, data, response) => {
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

[**[PlayerSeasonRedZone]**](PlayerSeasonRedZone.md)

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonStatsByPlayer

> [PlayerSeason] playerSeasonStatsByPlayer(format, season, playerid)

Player Season Stats by Player

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>732</code>.
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playerSeasonThirdDownStats

> [PlayerSeasonThirdDown] playerSeasonThirdDownStats(format, season)

Player Season Third Down Stats

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.playerSeasonThirdDownStats(format, season, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[PlayerSeasonThirdDown]**](PlayerSeasonThirdDown.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proBowlers

> [PlayerInfo] proBowlers(format, season)

Pro Bowlers

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season <br>Examples: <code>2016</code>, <code>2017</code>
apiInstance.proBowlers(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt; | 

### Return type

[**[PlayerInfo]**](PlayerInfo.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedule

> [Schedule] schedule(format, season)

Schedule

Game schedule for a specified season.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
apiInstance.schedule(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**[Schedule]**](Schedule.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scoresByDate

> [Score] scoresByDate(format, date)

Scores by Date

Get game scores for a specified week of a season.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
apiInstance.scoresByDate(format, date, (error, data, response) => {
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
 **date** | **String**| The date of the games.&lt;br&gt;Examples: &lt;code&gt;2021-SEP-12&lt;/code&gt;, &lt;code&gt;2021-NOV-28&lt;/code&gt;. | 

### Return type

[**[Score]**](Score.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scoresBySeason

> [Score] scoresBySeason(format, season)

Scores by Season 

Game scores for a specified season.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
apiInstance.scoresBySeason(format, season, (error, data, response) => {
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
 **season** | **String**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**[Score]**](Score.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scoresByWeek

> [Score] scoresByWeek(format, season, week)

Scores by Week

Get game scores for a specified week of a season.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.scoresByWeek(format, season, week, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**[Score]**](Score.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scoresByWeekSimulation

> [Score] scoresByWeekSimulation(format, numberofplays)

Scores by Week Simulation

Gets simulated live scores of NFL games, covering the Conference Championship games on January 21, 2018.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let numberofplays = "numberofplays_example"; // String | The number of plays to progress in this NFL live game simulation. Example entries are <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
apiInstance.scoresByWeekSimulation(format, numberofplays, (error, data, response) => {
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
 **numberofplays** | **String**| The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. | 

### Return type

[**[Score]**](Score.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## seasonCurrent

> Number seasonCurrent(format)

Season Current

Year of the current NFL season. This value changes at the start of the new NFL league year. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.seasonCurrent(format, (error, data, response) => {
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

**Number**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## seasonLastCompleted

> Number seasonLastCompleted(format)

Season Last Completed

Year of the most recently completed season. this value changes immediately after the Super Bowl. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.seasonLastCompleted(format, (error, data, response) => {
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

**Number**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## seasonUpcoming

> Number seasonUpcoming(format)

Season Upcoming

Year of the current NFL season, if we are in the mid-season. If we are in the off-season, then year of the next upcoming season. This value changes immediately after the Super Bowl. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.seasonUpcoming(format, (error, data, response) => {
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

**Number**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stadiums

> [Stadium] stadiums(format)

Stadiums

This method returns all stadiums.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**[Stadium]**](Stadium.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## standings

> [Standing] standings(format, season)

Standings

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.standings(format, season, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[Standing]**](Standing.md)

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String | Season to get games from. Example <code>2019POST</code>, <code>2020</code>
let teamid = "teamid_example"; // String | Unique ID of team.  Example <code> 8 </code>
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
 **teamid** | **String**| Unique ID of team.  Example &lt;code&gt; 8 &lt;/code&gt; | 
 **numberofgames** | **String**| How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt; | 

### Return type

[**[TeamGame]**](TeamGame.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamGameStats

> [TeamGame] teamGameStats(format, season, week)

Team Game Stats

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
let week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
apiInstance.teamGameStats(format, season, week, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

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
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "'XML'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[TeamSeason]**](TeamSeason.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsActive

> [Team] teamsActive(format)

Teams (Active)

Gets all active teams.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.teamsActive(format, (error, data, response) => {
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

[**[Team]**](Team.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsAll

> [Team] teamsAll(format)

Teams (All)

Gets all teams, including pro bowl teams.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.teamsAll(format, (error, data, response) => {
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

[**[Team]**](Team.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsBySeason

> [Team] teamsBySeason(format, season)

Teams by Season

List of teams playing in a specified season.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let season = "season_example"; // String |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
apiInstance.teamsBySeason(format, season, (error, data, response) => {
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
 **season** | **String**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**[Team]**](Team.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeframes

> [Timeframe] timeframes(format, type)

Timeframes

Get detailed information about past, present, and future timeframes.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let type = "type_example"; // String | The type of timeframes to return.  Valid entries are <code>current</code> or <code>upcoming</code> or <code>completed</code> or <code>recent</code> or <code>all</code>.
apiInstance.timeframes(format, type, (error, data, response) => {
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
 **type** | **String**| The type of timeframes to return.  Valid entries are &lt;code&gt;current&lt;/code&gt; or &lt;code&gt;upcoming&lt;/code&gt; or &lt;code&gt;completed&lt;/code&gt; or &lt;code&gt;recent&lt;/code&gt; or &lt;code&gt;all&lt;/code&gt;. | 

### Return type

[**[Timeframe]**](Timeframe.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## weekCurrent

> Number weekCurrent(format)

Week Current

Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday mornings at midnight ET.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.weekCurrent(format, (error, data, response) => {
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

**Number**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## weekLastCompleted

> Number weekLastCompleted(format)

Week Last Completed

Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday mornings at midnight ET.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.weekLastCompleted(format, (error, data, response) => {
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

**Number**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## weekUpcoming

> Number weekUpcoming(format)

Week Upcoming

Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday mornings at midnight ET.

### Example

```javascript
import NflV3Stats from 'nfl_v3_stats';
let defaultClient = NflV3Stats.ApiClient.instance;
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

let apiInstance = new NflV3Stats.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.weekUpcoming(format, (error, data, response) => {
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

**Number**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

