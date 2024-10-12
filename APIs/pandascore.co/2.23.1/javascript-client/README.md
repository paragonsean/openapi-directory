# panda_score_rest_api_for_all_videogames

PandaScoreRestApiForAllVideogames - JavaScript client for panda_score_rest_api_for_all_videogames

# Introduction

Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).

The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.

- The current endpoint is [https://api.pandascore.co](https://api.pandascore.co).
- All data is sent and received as JSON by default.
- Blank fields are included with `null` values instead of being omitted.
- All timestamps are returned in ISO-8601 format

### About this documentation

Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)

You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)

## Events hierarchy

The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.

**Leagues**

Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.  
Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._  
Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._

**Series**

A Serie represents an occurrence of a league event.  
The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._  
Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._

**Tournaments**

Tournaments groups all the matches of a serie under \"stages\" and \"groups\".  
The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._  
Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._

**Matches**

Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).  
Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._  
Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._  

**Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**  
![Structure](/doc/images/structure.png)

## Formats

&lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt;
The API currently supports the JSON format by default.

Other formats may be added depending on user needs.

## Pagination

The Pandascore API paginates all resources on the index method.

Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.

The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format

```
Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\"
```

There is also:

* A `X-Page` header field, which contains the current page.
* A `X-Per-Page` header field, which contains the current pagination length.
* A `X-Total` header field, which contains the total count of items across all pages.

## Filtering

The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).

For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:

```
GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN
```

## Range

The `range` parameter is a hash that allows filtering fields by an interval.
Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.

For example, the following is a request for all the champions with `hp` within 500 and 1000:

```
GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN
```

## Search

The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.

Note: this only works on strings.
Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.

For example, to get all the champions with a name containing `\"twi\"`:

```
$ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name'
\"Twitch\"
\"Twisted Fate\"
```

## Sorting

All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.

The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.

For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage.
Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.

## Rate limiting

Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).

With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.

Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**

# Authentication

The authentication on the Pandascore API works with access tokens.

All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.

**Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**

The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.

&lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.23.1
- Package version: 2.23.1
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install panda_score_rest_api_for_all_videogames --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your panda_score_rest_api_for_all_videogames from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var PandaScoreRestApiForAllVideogames = require('panda_score_rest_api_for_all_videogames');

var defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
var BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
var QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix['token'] = "Token"

var api = new PandaScoreRestApiForAllVideogames.IncidentsApi()
var opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // {GetAdditionsPageParameter} Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5, // {Number} Equivalent to `page[size]`
  'type': ["null"], // {[String]} Filter by result type(s)
  'since': new Date("2013-10-20T19:20:30+01:00"), // {Date} Filter out older results
  'videogame': [new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug()] // {[VideogameIDOrSlug]} Filter by videogame(s)
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getAdditions(opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.pandascore.co*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PandaScoreRestApiForAllVideogames.IncidentsApi* | [**getAdditions**](docs/IncidentsApi.md#getAdditions) | **GET** /additions | List additions
*PandaScoreRestApiForAllVideogames.IncidentsApi* | [**getChanges**](docs/IncidentsApi.md#getChanges) | **GET** /changes | List changes
*PandaScoreRestApiForAllVideogames.IncidentsApi* | [**getDeletions**](docs/IncidentsApi.md#getDeletions) | **GET** /deletions | List deletions
*PandaScoreRestApiForAllVideogames.IncidentsApi* | [**getIncidents**](docs/IncidentsApi.md#getIncidents) | **GET** /incidents | List changes, additions and deletions
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeagues**](docs/LeaguesApi.md#getLeagues) | **GET** /leagues | List leagues
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeaguesLeagueIdOrSlug**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlug) | **GET** /leagues/{league_id_or_slug} | Get a league
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatches**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatches) | **GET** /leagues/{league_id_or_slug}/matches | Get matches for a league
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatchesPast**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesPast) | **GET** /leagues/{league_id_or_slug}/matches/past | Get past matches for league
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatchesRunning**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesRunning) | **GET** /leagues/{league_id_or_slug}/matches/running | Get running matches for league
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatchesUpcoming**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesUpcoming) | **GET** /leagues/{league_id_or_slug}/matches/upcoming | Get upcoming matches for league
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeaguesLeagueIdOrSlugSeries**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugSeries) | **GET** /leagues/{league_id_or_slug}/series | List series of a league
*PandaScoreRestApiForAllVideogames.LeaguesApi* | [**getLeaguesLeagueIdOrSlugTournaments**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugTournaments) | **GET** /leagues/{league_id_or_slug}/tournaments | Get tournaments for a league
*PandaScoreRestApiForAllVideogames.LivesApi* | [**getLives_0**](docs/LivesApi.md#getLives_0) | **GET** /lives | List lives matches
*PandaScoreRestApiForAllVideogames.MatchesApi* | [**getLives**](docs/MatchesApi.md#getLives) | **GET** /lives | List lives matches
*PandaScoreRestApiForAllVideogames.MatchesApi* | [**getMatches**](docs/MatchesApi.md#getMatches) | **GET** /matches | List matches
*PandaScoreRestApiForAllVideogames.MatchesApi* | [**getMatchesMatchIdOrSlug**](docs/MatchesApi.md#getMatchesMatchIdOrSlug) | **GET** /matches/{match_id_or_slug} | Get a match
*PandaScoreRestApiForAllVideogames.MatchesApi* | [**getMatchesMatchIdOrSlugOpponents**](docs/MatchesApi.md#getMatchesMatchIdOrSlugOpponents) | **GET** /matches/{match_id_or_slug}/opponents | Get match&#39;s opponents
*PandaScoreRestApiForAllVideogames.MatchesApi* | [**getMatchesPast**](docs/MatchesApi.md#getMatchesPast) | **GET** /matches/past | Get past matches
*PandaScoreRestApiForAllVideogames.MatchesApi* | [**getMatchesRunning**](docs/MatchesApi.md#getMatchesRunning) | **GET** /matches/running | Get running matches
*PandaScoreRestApiForAllVideogames.MatchesApi* | [**getMatchesUpcoming**](docs/MatchesApi.md#getMatchesUpcoming) | **GET** /matches/upcoming | Get upcoming matches
*PandaScoreRestApiForAllVideogames.PlayersApi* | [**getPlayers**](docs/PlayersApi.md#getPlayers) | **GET** /players | List players
*PandaScoreRestApiForAllVideogames.PlayersApi* | [**getPlayersPlayerIdOrSlug**](docs/PlayersApi.md#getPlayersPlayerIdOrSlug) | **GET** /players/{player_id_or_slug} | Get a player
*PandaScoreRestApiForAllVideogames.PlayersApi* | [**getPlayersPlayerIdOrSlugMatches**](docs/PlayersApi.md#getPlayersPlayerIdOrSlugMatches) | **GET** /players/{player_id_or_slug}/matches | Get matches for a player
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeries**](docs/SeriesApi.md#getSeries) | **GET** /series | List series
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesPast**](docs/SeriesApi.md#getSeriesPast) | **GET** /series/past | Get past series
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesRunning**](docs/SeriesApi.md#getSeriesRunning) | **GET** /series/running | Get running series
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesSerieIdOrSlug**](docs/SeriesApi.md#getSeriesSerieIdOrSlug) | **GET** /series/{serie_id_or_slug} | Get a serie
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesSerieIdOrSlugMatches**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatches) | **GET** /series/{serie_id_or_slug}/matches | Get matches for a serie
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesSerieIdOrSlugMatchesPast**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatchesPast) | **GET** /series/{serie_id_or_slug}/matches/past | Get past matches for serie
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesSerieIdOrSlugMatchesRunning**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatchesRunning) | **GET** /series/{serie_id_or_slug}/matches/running | Get running matches for serie
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesSerieIdOrSlugMatchesUpcoming**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatchesUpcoming) | **GET** /series/{serie_id_or_slug}/matches/upcoming | Get upcoming matches for serie
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesSerieIdOrSlugPlayers**](docs/SeriesApi.md#getSeriesSerieIdOrSlugPlayers) | **GET** /series/{serie_id_or_slug}/players | Get players for a serie
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesSerieIdOrSlugTournaments**](docs/SeriesApi.md#getSeriesSerieIdOrSlugTournaments) | **GET** /series/{serie_id_or_slug}/tournaments | Get tournaments for a serie
*PandaScoreRestApiForAllVideogames.SeriesApi* | [**getSeriesUpcoming**](docs/SeriesApi.md#getSeriesUpcoming) | **GET** /series/upcoming | Get upcoming series
*PandaScoreRestApiForAllVideogames.TeamsApi* | [**getTeams**](docs/TeamsApi.md#getTeams) | **GET** /teams | List teams
*PandaScoreRestApiForAllVideogames.TeamsApi* | [**getTeamsTeamIdOrSlug**](docs/TeamsApi.md#getTeamsTeamIdOrSlug) | **GET** /teams/{team_id_or_slug} | Get a team
*PandaScoreRestApiForAllVideogames.TeamsApi* | [**getTeamsTeamIdOrSlugLeagues**](docs/TeamsApi.md#getTeamsTeamIdOrSlugLeagues) | **GET** /teams/{team_id_or_slug}/leagues | Get leagues for a team
*PandaScoreRestApiForAllVideogames.TeamsApi* | [**getTeamsTeamIdOrSlugMatches**](docs/TeamsApi.md#getTeamsTeamIdOrSlugMatches) | **GET** /teams/{team_id_or_slug}/matches | Get matches for team
*PandaScoreRestApiForAllVideogames.TeamsApi* | [**getTeamsTeamIdOrSlugSeries**](docs/TeamsApi.md#getTeamsTeamIdOrSlugSeries) | **GET** /teams/{team_id_or_slug}/series | Get series for a team
*PandaScoreRestApiForAllVideogames.TeamsApi* | [**getTeamsTeamIdOrSlugTournaments**](docs/TeamsApi.md#getTeamsTeamIdOrSlugTournaments) | **GET** /teams/{team_id_or_slug}/tournaments | Get tournaments for a team
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournaments**](docs/TournamentsApi.md#getTournaments) | **GET** /tournaments | List tournaments
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsPast**](docs/TournamentsApi.md#getTournamentsPast) | **GET** /tournaments/past | Get past tournaments
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsRunning**](docs/TournamentsApi.md#getTournamentsRunning) | **GET** /tournaments/running | Get running tournaments
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsTournamentIdOrSlug**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlug) | **GET** /tournaments/{tournament_id_or_slug} | Get a tournament
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsTournamentIdOrSlugBrackets**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugBrackets) | **GET** /tournaments/{tournament_id_or_slug}/brackets | Get a tournament&#39;s brackets
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsTournamentIdOrSlugMatches**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugMatches) | **GET** /tournaments/{tournament_id_or_slug}/matches | Get matches for tournament
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsTournamentIdOrSlugPlayers**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugPlayers) | **GET** /tournaments/{tournament_id_or_slug}/players | Get players for a tournament
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsTournamentIdOrSlugRosters**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugRosters) | **GET** /tournaments/{tournament_id_or_slug}/rosters | Get rosters for a tournament
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsTournamentIdOrSlugStandings**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugStandings) | **GET** /tournaments/{tournament_id_or_slug}/standings | Get tournament standings
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsTournamentIdOrSlugTeams**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugTeams) | **GET** /tournaments/{tournament_id_or_slug}/teams | Get teams for a tournament
*PandaScoreRestApiForAllVideogames.TournamentsApi* | [**getTournamentsUpcoming**](docs/TournamentsApi.md#getTournamentsUpcoming) | **GET** /tournaments/upcoming | Get upcoming tournaments
*PandaScoreRestApiForAllVideogames.VideogamesApi* | [**getVideogames**](docs/VideogamesApi.md#getVideogames) | **GET** /videogames | List videogames
*PandaScoreRestApiForAllVideogames.VideogamesApi* | [**getVideogamesVideogameIdOrSlug**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlug) | **GET** /videogames/{videogame_id_or_slug} | Get a videogame
*PandaScoreRestApiForAllVideogames.VideogamesApi* | [**getVideogamesVideogameIdOrSlugLeagues**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugLeagues) | **GET** /videogames/{videogame_id_or_slug}/leagues | 
*PandaScoreRestApiForAllVideogames.VideogamesApi* | [**getVideogamesVideogameIdOrSlugSeries**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugSeries) | **GET** /videogames/{videogame_id_or_slug}/series | List series for a videogame
*PandaScoreRestApiForAllVideogames.VideogamesApi* | [**getVideogamesVideogameIdOrSlugTournaments**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugTournaments) | **GET** /videogames/{videogame_id_or_slug}/tournaments | Get tournaments for a videogame
*PandaScoreRestApiForAllVideogames.VideogamesApi* | [**getVideogamesVideogameIdOrSlugVersions**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugVersions) | **GET** /videogames/{videogame_id_or_slug}/versions | List videogame versions


## Documentation for Models

 - [PandaScoreRestApiForAllVideogames.BaseLeague](docs/BaseLeague.md)
 - [PandaScoreRestApiForAllVideogames.BaseMatch](docs/BaseMatch.md)
 - [PandaScoreRestApiForAllVideogames.BaseOpponent](docs/BaseOpponent.md)
 - [PandaScoreRestApiForAllVideogames.BaseOpponent1](docs/BaseOpponent1.md)
 - [PandaScoreRestApiForAllVideogames.BasePlayer](docs/BasePlayer.md)
 - [PandaScoreRestApiForAllVideogames.BaseSerie](docs/BaseSerie.md)
 - [PandaScoreRestApiForAllVideogames.BaseTeam](docs/BaseTeam.md)
 - [PandaScoreRestApiForAllVideogames.BaseTeam1](docs/BaseTeam1.md)
 - [PandaScoreRestApiForAllVideogames.BaseTournament](docs/BaseTournament.md)
 - [PandaScoreRestApiForAllVideogames.BettingBaseTournament](docs/BettingBaseTournament.md)
 - [PandaScoreRestApiForAllVideogames.BettingCSGOGame](docs/BettingCSGOGame.md)
 - [PandaScoreRestApiForAllVideogames.BettingCSGOGameRoundTeam](docs/BettingCSGOGameRoundTeam.md)
 - [PandaScoreRestApiForAllVideogames.BettingDota2Game](docs/BettingDota2Game.md)
 - [PandaScoreRestApiForAllVideogames.BettingGame](docs/BettingGame.md)
 - [PandaScoreRestApiForAllVideogames.BettingGameRoundTeams](docs/BettingGameRoundTeams.md)
 - [PandaScoreRestApiForAllVideogames.BettingGameRoundTeams1](docs/BettingGameRoundTeams1.md)
 - [PandaScoreRestApiForAllVideogames.BettingGameTeams](docs/BettingGameTeams.md)
 - [PandaScoreRestApiForAllVideogames.BettingGameTeams1](docs/BettingGameTeams1.md)
 - [PandaScoreRestApiForAllVideogames.BettingGroup](docs/BettingGroup.md)
 - [PandaScoreRestApiForAllVideogames.BettingGroup1](docs/BettingGroup1.md)
 - [PandaScoreRestApiForAllVideogames.BettingLeague](docs/BettingLeague.md)
 - [PandaScoreRestApiForAllVideogames.BettingLeague1](docs/BettingLeague1.md)
 - [PandaScoreRestApiForAllVideogames.BettingLeagueVideogame](docs/BettingLeagueVideogame.md)
 - [PandaScoreRestApiForAllVideogames.BettingLoLGame](docs/BettingLoLGame.md)
 - [PandaScoreRestApiForAllVideogames.BettingLoLGameTeam](docs/BettingLoLGameTeam.md)
 - [PandaScoreRestApiForAllVideogames.BettingMatch](docs/BettingMatch.md)
 - [PandaScoreRestApiForAllVideogames.BettingMatchStatus](docs/BettingMatchStatus.md)
 - [PandaScoreRestApiForAllVideogames.BettingMetadata](docs/BettingMetadata.md)
 - [PandaScoreRestApiForAllVideogames.BettingOwGame](docs/BettingOwGame.md)
 - [PandaScoreRestApiForAllVideogames.BettingPUBGGame](docs/BettingPUBGGame.md)
 - [PandaScoreRestApiForAllVideogames.BettingSerie](docs/BettingSerie.md)
 - [PandaScoreRestApiForAllVideogames.BettingSerie1](docs/BettingSerie1.md)
 - [PandaScoreRestApiForAllVideogames.BettingTournament](docs/BettingTournament.md)
 - [PandaScoreRestApiForAllVideogames.Blueprint](docs/Blueprint.md)
 - [PandaScoreRestApiForAllVideogames.Blueprint1](docs/Blueprint1.md)
 - [PandaScoreRestApiForAllVideogames.Bracket](docs/Bracket.md)
 - [PandaScoreRestApiForAllVideogames.BracketStanding](docs/BracketStanding.md)
 - [PandaScoreRestApiForAllVideogames.CSGOMap](docs/CSGOMap.md)
 - [PandaScoreRestApiForAllVideogames.CSGOMap1](docs/CSGOMap1.md)
 - [PandaScoreRestApiForAllVideogames.CSGOOutcome](docs/CSGOOutcome.md)
 - [PandaScoreRestApiForAllVideogames.CSGOWeaponIDOrSlug](docs/CSGOWeaponIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.CurrentVideogame](docs/CurrentVideogame.md)
 - [PandaScoreRestApiForAllVideogames.DeletionIncident](docs/DeletionIncident.md)
 - [PandaScoreRestApiForAllVideogames.DeletionIncidentChangeType](docs/DeletionIncidentChangeType.md)
 - [PandaScoreRestApiForAllVideogames.DeletionObject](docs/DeletionObject.md)
 - [PandaScoreRestApiForAllVideogames.Dota2AbilityIDOrSlug](docs/Dota2AbilityIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.Dota2HeroIDOrSlug](docs/Dota2HeroIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.Dota2ItemIDOrSlug](docs/Dota2ItemIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.Esport](docs/Esport.md)
 - [PandaScoreRestApiForAllVideogames.EsportCSGO](docs/EsportCSGO.md)
 - [PandaScoreRestApiForAllVideogames.EsportCodmw](docs/EsportCodmw.md)
 - [PandaScoreRestApiForAllVideogames.EsportDota2](docs/EsportDota2.md)
 - [PandaScoreRestApiForAllVideogames.EsportFifa](docs/EsportFifa.md)
 - [PandaScoreRestApiForAllVideogames.EsportFortnite](docs/EsportFortnite.md)
 - [PandaScoreRestApiForAllVideogames.EsportLoL](docs/EsportLoL.md)
 - [PandaScoreRestApiForAllVideogames.EsportOverwatch](docs/EsportOverwatch.md)
 - [PandaScoreRestApiForAllVideogames.EsportPUBG](docs/EsportPUBG.md)
 - [PandaScoreRestApiForAllVideogames.EsportR6siege](docs/EsportR6siege.md)
 - [PandaScoreRestApiForAllVideogames.EsportRocketLeague](docs/EsportRocketLeague.md)
 - [PandaScoreRestApiForAllVideogames.EsportValorant](docs/EsportValorant.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverBrackets](docs/FilterOverBrackets.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverLeagues](docs/FilterOverLeagues.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverMatches](docs/FilterOverMatches.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverPlayers](docs/FilterOverPlayers.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverSeries](docs/FilterOverSeries.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverShortTournaments](docs/FilterOverShortTournaments.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverShortVideogameVersions](docs/FilterOverShortVideogameVersions.md)
 - [PandaScoreRestApiForAllVideogames.FilterOverTeams](docs/FilterOverTeams.md)
 - [PandaScoreRestApiForAllVideogames.Game](docs/Game.md)
 - [PandaScoreRestApiForAllVideogames.GameID](docs/GameID.md)
 - [PandaScoreRestApiForAllVideogames.GameStatus](docs/GameStatus.md)
 - [PandaScoreRestApiForAllVideogames.GameWinner](docs/GameWinner.md)
 - [PandaScoreRestApiForAllVideogames.GetAdditions400Response](docs/GetAdditions400Response.md)
 - [PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter](docs/GetAdditionsPageParameter.md)
 - [PandaScoreRestApiForAllVideogames.GetAdditionsPageParameterOneOf](docs/GetAdditionsPageParameterOneOf.md)
 - [PandaScoreRestApiForAllVideogames.GroupStanding](docs/GroupStanding.md)
 - [PandaScoreRestApiForAllVideogames.Incident](docs/Incident.md)
 - [PandaScoreRestApiForAllVideogames.IncidentChangeType](docs/IncidentChangeType.md)
 - [PandaScoreRestApiForAllVideogames.IncidentDeletionReason](docs/IncidentDeletionReason.md)
 - [PandaScoreRestApiForAllVideogames.IncidentDeletionReasonDeleted](docs/IncidentDeletionReasonDeleted.md)
 - [PandaScoreRestApiForAllVideogames.IncidentID](docs/IncidentID.md)
 - [PandaScoreRestApiForAllVideogames.IncidentOfTypeLeague](docs/IncidentOfTypeLeague.md)
 - [PandaScoreRestApiForAllVideogames.IncidentOfTypeMatch](docs/IncidentOfTypeMatch.md)
 - [PandaScoreRestApiForAllVideogames.IncidentOfTypePlayer](docs/IncidentOfTypePlayer.md)
 - [PandaScoreRestApiForAllVideogames.IncidentOfTypeSerie](docs/IncidentOfTypeSerie.md)
 - [PandaScoreRestApiForAllVideogames.IncidentOfTypeTeam](docs/IncidentOfTypeTeam.md)
 - [PandaScoreRestApiForAllVideogames.IncidentOfTypeTournament](docs/IncidentOfTypeTournament.md)
 - [PandaScoreRestApiForAllVideogames.IncidentType](docs/IncidentType.md)
 - [PandaScoreRestApiForAllVideogames.League](docs/League.md)
 - [PandaScoreRestApiForAllVideogames.LeagueIDOrSlug](docs/LeagueIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogame](docs/LeagueVideogame.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameCSGO](docs/LeagueVideogameCSGO.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameCodmw](docs/LeagueVideogameCodmw.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameDota2](docs/LeagueVideogameDota2.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameFifa](docs/LeagueVideogameFifa.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameFortnite](docs/LeagueVideogameFortnite.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameLoL](docs/LeagueVideogameLoL.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameOverwatch](docs/LeagueVideogameOverwatch.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogamePUBG](docs/LeagueVideogamePUBG.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameR6siege](docs/LeagueVideogameR6siege.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameRocketLeague](docs/LeagueVideogameRocketLeague.md)
 - [PandaScoreRestApiForAllVideogames.LeagueVideogameValorant](docs/LeagueVideogameValorant.md)
 - [PandaScoreRestApiForAllVideogames.Live](docs/Live.md)
 - [PandaScoreRestApiForAllVideogames.LiveEndpoint](docs/LiveEndpoint.md)
 - [PandaScoreRestApiForAllVideogames.LiveEvent](docs/LiveEvent.md)
 - [PandaScoreRestApiForAllVideogames.LiveEvent1](docs/LiveEvent1.md)
 - [PandaScoreRestApiForAllVideogames.LiveType](docs/LiveType.md)
 - [PandaScoreRestApiForAllVideogames.LoLTeamColor](docs/LoLTeamColor.md)
 - [PandaScoreRestApiForAllVideogames.Market](docs/Market.md)
 - [PandaScoreRestApiForAllVideogames.MarketSelection](docs/MarketSelection.md)
 - [PandaScoreRestApiForAllVideogames.MarketStatus](docs/MarketStatus.md)
 - [PandaScoreRestApiForAllVideogames.Match](docs/Match.md)
 - [PandaScoreRestApiForAllVideogames.MatchIDOrSlug](docs/MatchIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.MatchLive](docs/MatchLive.md)
 - [PandaScoreRestApiForAllVideogames.MatchLocalizedStream](docs/MatchLocalizedStream.md)
 - [PandaScoreRestApiForAllVideogames.MatchLocalizedStreams](docs/MatchLocalizedStreams.md)
 - [PandaScoreRestApiForAllVideogames.MatchMarketGame](docs/MatchMarketGame.md)
 - [PandaScoreRestApiForAllVideogames.MatchMarkets](docs/MatchMarkets.md)
 - [PandaScoreRestApiForAllVideogames.MatchOpponentBasePlayer](docs/MatchOpponentBasePlayer.md)
 - [PandaScoreRestApiForAllVideogames.MatchOpponentsObject](docs/MatchOpponentsObject.md)
 - [PandaScoreRestApiForAllVideogames.MatchPlayerOpponentsObject](docs/MatchPlayerOpponentsObject.md)
 - [PandaScoreRestApiForAllVideogames.MatchPlayerResult](docs/MatchPlayerResult.md)
 - [PandaScoreRestApiForAllVideogames.MatchResult](docs/MatchResult.md)
 - [PandaScoreRestApiForAllVideogames.MatchStatus](docs/MatchStatus.md)
 - [PandaScoreRestApiForAllVideogames.MatchTeamOpponentsObject](docs/MatchTeamOpponentsObject.md)
 - [PandaScoreRestApiForAllVideogames.MatchTeamResult](docs/MatchTeamResult.md)
 - [PandaScoreRestApiForAllVideogames.MatchType](docs/MatchType.md)
 - [PandaScoreRestApiForAllVideogames.NonDeletionIncident](docs/NonDeletionIncident.md)
 - [PandaScoreRestApiForAllVideogames.Opponent](docs/Opponent.md)
 - [PandaScoreRestApiForAllVideogames.OpponentID](docs/OpponentID.md)
 - [PandaScoreRestApiForAllVideogames.OpponentID1](docs/OpponentID1.md)
 - [PandaScoreRestApiForAllVideogames.OpponentType](docs/OpponentType.md)
 - [PandaScoreRestApiForAllVideogames.OpponentTypePlayer](docs/OpponentTypePlayer.md)
 - [PandaScoreRestApiForAllVideogames.OpponentTypeTeam](docs/OpponentTypeTeam.md)
 - [PandaScoreRestApiForAllVideogames.OwHeroIDOrSlug](docs/OwHeroIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.OwMapIDOrSlug](docs/OwMapIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.Player](docs/Player.md)
 - [PandaScoreRestApiForAllVideogames.PlayerIDOrSlug](docs/PlayerIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.PreviousMatch](docs/PreviousMatch.md)
 - [PandaScoreRestApiForAllVideogames.PreviousMatchType](docs/PreviousMatchType.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverBrackets](docs/RangeOverBrackets.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverLeagues](docs/RangeOverLeagues.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverMatches](docs/RangeOverMatches.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverPlayers](docs/RangeOverPlayers.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverSeries](docs/RangeOverSeries.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverShortTournaments](docs/RangeOverShortTournaments.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverShortVideogameVersions](docs/RangeOverShortVideogameVersions.md)
 - [PandaScoreRestApiForAllVideogames.RangeOverTeams](docs/RangeOverTeams.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverBrackets](docs/SearchOverBrackets.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverLeagues](docs/SearchOverLeagues.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverMatches](docs/SearchOverMatches.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverPlayers](docs/SearchOverPlayers.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverSeries](docs/SearchOverSeries.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverShortTournaments](docs/SearchOverShortTournaments.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverShortVideogameVersions](docs/SearchOverShortVideogameVersions.md)
 - [PandaScoreRestApiForAllVideogames.SearchOverTeams](docs/SearchOverTeams.md)
 - [PandaScoreRestApiForAllVideogames.SelectionResult](docs/SelectionResult.md)
 - [PandaScoreRestApiForAllVideogames.Serie](docs/Serie.md)
 - [PandaScoreRestApiForAllVideogames.SerieIDOrSlug](docs/SerieIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.ShortTournament](docs/ShortTournament.md)
 - [PandaScoreRestApiForAllVideogames.ShortVideogameVersion](docs/ShortVideogameVersion.md)
 - [PandaScoreRestApiForAllVideogames.ShortVideogameVersion1](docs/ShortVideogameVersion1.md)
 - [PandaScoreRestApiForAllVideogames.Standing](docs/Standing.md)
 - [PandaScoreRestApiForAllVideogames.Stream](docs/Stream.md)
 - [PandaScoreRestApiForAllVideogames.StreamLanguage](docs/StreamLanguage.md)
 - [PandaScoreRestApiForAllVideogames.Team](docs/Team.md)
 - [PandaScoreRestApiForAllVideogames.TeamIDOrSlug](docs/TeamIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.Tournament](docs/Tournament.md)
 - [PandaScoreRestApiForAllVideogames.TournamentIDOrSlug](docs/TournamentIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.TournamentPlayerRosters](docs/TournamentPlayerRosters.md)
 - [PandaScoreRestApiForAllVideogames.TournamentRosterItem](docs/TournamentRosterItem.md)
 - [PandaScoreRestApiForAllVideogames.TournamentRosters](docs/TournamentRosters.md)
 - [PandaScoreRestApiForAllVideogames.TournamentTeamRosters](docs/TournamentTeamRosters.md)
 - [PandaScoreRestApiForAllVideogames.Videogame](docs/Videogame.md)
 - [PandaScoreRestApiForAllVideogames.VideogameCSGO](docs/VideogameCSGO.md)
 - [PandaScoreRestApiForAllVideogames.VideogameCodmw](docs/VideogameCodmw.md)
 - [PandaScoreRestApiForAllVideogames.VideogameDota2](docs/VideogameDota2.md)
 - [PandaScoreRestApiForAllVideogames.VideogameFifa](docs/VideogameFifa.md)
 - [PandaScoreRestApiForAllVideogames.VideogameID](docs/VideogameID.md)
 - [PandaScoreRestApiForAllVideogames.VideogameIDOrSlug](docs/VideogameIDOrSlug.md)
 - [PandaScoreRestApiForAllVideogames.VideogameLeague](docs/VideogameLeague.md)
 - [PandaScoreRestApiForAllVideogames.VideogameLoL](docs/VideogameLoL.md)
 - [PandaScoreRestApiForAllVideogames.VideogameOverwatch](docs/VideogameOverwatch.md)
 - [PandaScoreRestApiForAllVideogames.VideogamePUBG](docs/VideogamePUBG.md)
 - [PandaScoreRestApiForAllVideogames.VideogameR6siege](docs/VideogameR6siege.md)
 - [PandaScoreRestApiForAllVideogames.VideogameRocketLeague](docs/VideogameRocketLeague.md)
 - [PandaScoreRestApiForAllVideogames.VideogameSlug](docs/VideogameSlug.md)
 - [PandaScoreRestApiForAllVideogames.VideogameTitle](docs/VideogameTitle.md)
 - [PandaScoreRestApiForAllVideogames.VideogameTitle1](docs/VideogameTitle1.md)
 - [PandaScoreRestApiForAllVideogames.VideogameValorant](docs/VideogameValorant.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### BearerToken

- **Type**: Bearer authentication

### QueryToken


- **Type**: API key
- **API key parameter name**: token
- **Location**: URL query string

