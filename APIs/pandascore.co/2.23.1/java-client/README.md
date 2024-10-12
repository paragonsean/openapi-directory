# openapi-java-client

PandaScore REST API for All Videogames
- API version: 2.23.1
  - Build date: 2024-10-12T09:58:25.859268-04:00[America/New_York]
  - Generator version: 7.9.0


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



*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2.23.1</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2.23.1"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2.23.1.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    List<String> type = Arrays.asList(); // List<String> | Filter by result type(s)
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Filter out older results
    List<VideogameIDOrSlug> videogame = Arrays.asList(); // List<VideogameIDOrSlug> | Filter by videogame(s)
    try {
      List<NonDeletionIncident> result = apiInstance.getAdditions(page, perPage, type, since, videogame);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#getAdditions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.pandascore.co*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IncidentsApi* | [**getAdditions**](docs/IncidentsApi.md#getAdditions) | **GET** /additions | List additions
*IncidentsApi* | [**getChanges**](docs/IncidentsApi.md#getChanges) | **GET** /changes | List changes
*IncidentsApi* | [**getDeletions**](docs/IncidentsApi.md#getDeletions) | **GET** /deletions | List deletions
*IncidentsApi* | [**getIncidents**](docs/IncidentsApi.md#getIncidents) | **GET** /incidents | List changes, additions and deletions
*LeaguesApi* | [**getLeagues**](docs/LeaguesApi.md#getLeagues) | **GET** /leagues | List leagues
*LeaguesApi* | [**getLeaguesLeagueIdOrSlug**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlug) | **GET** /leagues/{league_id_or_slug} | Get a league
*LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatches**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatches) | **GET** /leagues/{league_id_or_slug}/matches | Get matches for a league
*LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatchesPast**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesPast) | **GET** /leagues/{league_id_or_slug}/matches/past | Get past matches for league
*LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatchesRunning**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesRunning) | **GET** /leagues/{league_id_or_slug}/matches/running | Get running matches for league
*LeaguesApi* | [**getLeaguesLeagueIdOrSlugMatchesUpcoming**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesUpcoming) | **GET** /leagues/{league_id_or_slug}/matches/upcoming | Get upcoming matches for league
*LeaguesApi* | [**getLeaguesLeagueIdOrSlugSeries**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugSeries) | **GET** /leagues/{league_id_or_slug}/series | List series of a league
*LeaguesApi* | [**getLeaguesLeagueIdOrSlugTournaments**](docs/LeaguesApi.md#getLeaguesLeagueIdOrSlugTournaments) | **GET** /leagues/{league_id_or_slug}/tournaments | Get tournaments for a league
*LivesApi* | [**getLives_0**](docs/LivesApi.md#getLives_0) | **GET** /lives | List lives matches
*MatchesApi* | [**getLives**](docs/MatchesApi.md#getLives) | **GET** /lives | List lives matches
*MatchesApi* | [**getMatches**](docs/MatchesApi.md#getMatches) | **GET** /matches | List matches
*MatchesApi* | [**getMatchesMatchIdOrSlug**](docs/MatchesApi.md#getMatchesMatchIdOrSlug) | **GET** /matches/{match_id_or_slug} | Get a match
*MatchesApi* | [**getMatchesMatchIdOrSlugOpponents**](docs/MatchesApi.md#getMatchesMatchIdOrSlugOpponents) | **GET** /matches/{match_id_or_slug}/opponents | Get match&#39;s opponents
*MatchesApi* | [**getMatchesPast**](docs/MatchesApi.md#getMatchesPast) | **GET** /matches/past | Get past matches
*MatchesApi* | [**getMatchesRunning**](docs/MatchesApi.md#getMatchesRunning) | **GET** /matches/running | Get running matches
*MatchesApi* | [**getMatchesUpcoming**](docs/MatchesApi.md#getMatchesUpcoming) | **GET** /matches/upcoming | Get upcoming matches
*PlayersApi* | [**getPlayers**](docs/PlayersApi.md#getPlayers) | **GET** /players | List players
*PlayersApi* | [**getPlayersPlayerIdOrSlug**](docs/PlayersApi.md#getPlayersPlayerIdOrSlug) | **GET** /players/{player_id_or_slug} | Get a player
*PlayersApi* | [**getPlayersPlayerIdOrSlugMatches**](docs/PlayersApi.md#getPlayersPlayerIdOrSlugMatches) | **GET** /players/{player_id_or_slug}/matches | Get matches for a player
*SeriesApi* | [**getSeries**](docs/SeriesApi.md#getSeries) | **GET** /series | List series
*SeriesApi* | [**getSeriesPast**](docs/SeriesApi.md#getSeriesPast) | **GET** /series/past | Get past series
*SeriesApi* | [**getSeriesRunning**](docs/SeriesApi.md#getSeriesRunning) | **GET** /series/running | Get running series
*SeriesApi* | [**getSeriesSerieIdOrSlug**](docs/SeriesApi.md#getSeriesSerieIdOrSlug) | **GET** /series/{serie_id_or_slug} | Get a serie
*SeriesApi* | [**getSeriesSerieIdOrSlugMatches**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatches) | **GET** /series/{serie_id_or_slug}/matches | Get matches for a serie
*SeriesApi* | [**getSeriesSerieIdOrSlugMatchesPast**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatchesPast) | **GET** /series/{serie_id_or_slug}/matches/past | Get past matches for serie
*SeriesApi* | [**getSeriesSerieIdOrSlugMatchesRunning**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatchesRunning) | **GET** /series/{serie_id_or_slug}/matches/running | Get running matches for serie
*SeriesApi* | [**getSeriesSerieIdOrSlugMatchesUpcoming**](docs/SeriesApi.md#getSeriesSerieIdOrSlugMatchesUpcoming) | **GET** /series/{serie_id_or_slug}/matches/upcoming | Get upcoming matches for serie
*SeriesApi* | [**getSeriesSerieIdOrSlugPlayers**](docs/SeriesApi.md#getSeriesSerieIdOrSlugPlayers) | **GET** /series/{serie_id_or_slug}/players | Get players for a serie
*SeriesApi* | [**getSeriesSerieIdOrSlugTournaments**](docs/SeriesApi.md#getSeriesSerieIdOrSlugTournaments) | **GET** /series/{serie_id_or_slug}/tournaments | Get tournaments for a serie
*SeriesApi* | [**getSeriesUpcoming**](docs/SeriesApi.md#getSeriesUpcoming) | **GET** /series/upcoming | Get upcoming series
*TeamsApi* | [**getTeams**](docs/TeamsApi.md#getTeams) | **GET** /teams | List teams
*TeamsApi* | [**getTeamsTeamIdOrSlug**](docs/TeamsApi.md#getTeamsTeamIdOrSlug) | **GET** /teams/{team_id_or_slug} | Get a team
*TeamsApi* | [**getTeamsTeamIdOrSlugLeagues**](docs/TeamsApi.md#getTeamsTeamIdOrSlugLeagues) | **GET** /teams/{team_id_or_slug}/leagues | Get leagues for a team
*TeamsApi* | [**getTeamsTeamIdOrSlugMatches**](docs/TeamsApi.md#getTeamsTeamIdOrSlugMatches) | **GET** /teams/{team_id_or_slug}/matches | Get matches for team
*TeamsApi* | [**getTeamsTeamIdOrSlugSeries**](docs/TeamsApi.md#getTeamsTeamIdOrSlugSeries) | **GET** /teams/{team_id_or_slug}/series | Get series for a team
*TeamsApi* | [**getTeamsTeamIdOrSlugTournaments**](docs/TeamsApi.md#getTeamsTeamIdOrSlugTournaments) | **GET** /teams/{team_id_or_slug}/tournaments | Get tournaments for a team
*TournamentsApi* | [**getTournaments**](docs/TournamentsApi.md#getTournaments) | **GET** /tournaments | List tournaments
*TournamentsApi* | [**getTournamentsPast**](docs/TournamentsApi.md#getTournamentsPast) | **GET** /tournaments/past | Get past tournaments
*TournamentsApi* | [**getTournamentsRunning**](docs/TournamentsApi.md#getTournamentsRunning) | **GET** /tournaments/running | Get running tournaments
*TournamentsApi* | [**getTournamentsTournamentIdOrSlug**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlug) | **GET** /tournaments/{tournament_id_or_slug} | Get a tournament
*TournamentsApi* | [**getTournamentsTournamentIdOrSlugBrackets**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugBrackets) | **GET** /tournaments/{tournament_id_or_slug}/brackets | Get a tournament&#39;s brackets
*TournamentsApi* | [**getTournamentsTournamentIdOrSlugMatches**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugMatches) | **GET** /tournaments/{tournament_id_or_slug}/matches | Get matches for tournament
*TournamentsApi* | [**getTournamentsTournamentIdOrSlugPlayers**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugPlayers) | **GET** /tournaments/{tournament_id_or_slug}/players | Get players for a tournament
*TournamentsApi* | [**getTournamentsTournamentIdOrSlugRosters**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugRosters) | **GET** /tournaments/{tournament_id_or_slug}/rosters | Get rosters for a tournament
*TournamentsApi* | [**getTournamentsTournamentIdOrSlugStandings**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugStandings) | **GET** /tournaments/{tournament_id_or_slug}/standings | Get tournament standings
*TournamentsApi* | [**getTournamentsTournamentIdOrSlugTeams**](docs/TournamentsApi.md#getTournamentsTournamentIdOrSlugTeams) | **GET** /tournaments/{tournament_id_or_slug}/teams | Get teams for a tournament
*TournamentsApi* | [**getTournamentsUpcoming**](docs/TournamentsApi.md#getTournamentsUpcoming) | **GET** /tournaments/upcoming | Get upcoming tournaments
*VideogamesApi* | [**getVideogames**](docs/VideogamesApi.md#getVideogames) | **GET** /videogames | List videogames
*VideogamesApi* | [**getVideogamesVideogameIdOrSlug**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlug) | **GET** /videogames/{videogame_id_or_slug} | Get a videogame
*VideogamesApi* | [**getVideogamesVideogameIdOrSlugLeagues**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugLeagues) | **GET** /videogames/{videogame_id_or_slug}/leagues | 
*VideogamesApi* | [**getVideogamesVideogameIdOrSlugSeries**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugSeries) | **GET** /videogames/{videogame_id_or_slug}/series | List series for a videogame
*VideogamesApi* | [**getVideogamesVideogameIdOrSlugTournaments**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugTournaments) | **GET** /videogames/{videogame_id_or_slug}/tournaments | Get tournaments for a videogame
*VideogamesApi* | [**getVideogamesVideogameIdOrSlugVersions**](docs/VideogamesApi.md#getVideogamesVideogameIdOrSlugVersions) | **GET** /videogames/{videogame_id_or_slug}/versions | List videogame versions


## Documentation for Models

 - [BaseLeague](docs/BaseLeague.md)
 - [BaseMatch](docs/BaseMatch.md)
 - [BaseOpponent](docs/BaseOpponent.md)
 - [BaseOpponent1](docs/BaseOpponent1.md)
 - [BasePlayer](docs/BasePlayer.md)
 - [BaseSerie](docs/BaseSerie.md)
 - [BaseTeam](docs/BaseTeam.md)
 - [BaseTeam1](docs/BaseTeam1.md)
 - [BaseTournament](docs/BaseTournament.md)
 - [BettingBaseTournament](docs/BettingBaseTournament.md)
 - [BettingCSGOGame](docs/BettingCSGOGame.md)
 - [BettingCSGOGameRoundTeam](docs/BettingCSGOGameRoundTeam.md)
 - [BettingDota2Game](docs/BettingDota2Game.md)
 - [BettingGame](docs/BettingGame.md)
 - [BettingGameRoundTeams](docs/BettingGameRoundTeams.md)
 - [BettingGameRoundTeams1](docs/BettingGameRoundTeams1.md)
 - [BettingGameTeams](docs/BettingGameTeams.md)
 - [BettingGameTeams1](docs/BettingGameTeams1.md)
 - [BettingGroup](docs/BettingGroup.md)
 - [BettingGroup1](docs/BettingGroup1.md)
 - [BettingLeague](docs/BettingLeague.md)
 - [BettingLeague1](docs/BettingLeague1.md)
 - [BettingLeagueVideogame](docs/BettingLeagueVideogame.md)
 - [BettingLoLGame](docs/BettingLoLGame.md)
 - [BettingLoLGameTeam](docs/BettingLoLGameTeam.md)
 - [BettingMatch](docs/BettingMatch.md)
 - [BettingMatchStatus](docs/BettingMatchStatus.md)
 - [BettingMetadata](docs/BettingMetadata.md)
 - [BettingOwGame](docs/BettingOwGame.md)
 - [BettingPUBGGame](docs/BettingPUBGGame.md)
 - [BettingSerie](docs/BettingSerie.md)
 - [BettingSerie1](docs/BettingSerie1.md)
 - [BettingTournament](docs/BettingTournament.md)
 - [Blueprint](docs/Blueprint.md)
 - [Blueprint1](docs/Blueprint1.md)
 - [Bracket](docs/Bracket.md)
 - [BracketStanding](docs/BracketStanding.md)
 - [CSGOMap](docs/CSGOMap.md)
 - [CSGOMap1](docs/CSGOMap1.md)
 - [CSGOOutcome](docs/CSGOOutcome.md)
 - [CSGOWeaponIDOrSlug](docs/CSGOWeaponIDOrSlug.md)
 - [CurrentVideogame](docs/CurrentVideogame.md)
 - [DeletionIncident](docs/DeletionIncident.md)
 - [DeletionIncidentChangeType](docs/DeletionIncidentChangeType.md)
 - [DeletionObject](docs/DeletionObject.md)
 - [Dota2AbilityIDOrSlug](docs/Dota2AbilityIDOrSlug.md)
 - [Dota2HeroIDOrSlug](docs/Dota2HeroIDOrSlug.md)
 - [Dota2ItemIDOrSlug](docs/Dota2ItemIDOrSlug.md)
 - [Esport](docs/Esport.md)
 - [EsportCSGO](docs/EsportCSGO.md)
 - [EsportCodmw](docs/EsportCodmw.md)
 - [EsportDota2](docs/EsportDota2.md)
 - [EsportFifa](docs/EsportFifa.md)
 - [EsportFortnite](docs/EsportFortnite.md)
 - [EsportLoL](docs/EsportLoL.md)
 - [EsportOverwatch](docs/EsportOverwatch.md)
 - [EsportPUBG](docs/EsportPUBG.md)
 - [EsportR6siege](docs/EsportR6siege.md)
 - [EsportRocketLeague](docs/EsportRocketLeague.md)
 - [EsportValorant](docs/EsportValorant.md)
 - [FilterOverBrackets](docs/FilterOverBrackets.md)
 - [FilterOverLeagues](docs/FilterOverLeagues.md)
 - [FilterOverMatches](docs/FilterOverMatches.md)
 - [FilterOverPlayers](docs/FilterOverPlayers.md)
 - [FilterOverSeries](docs/FilterOverSeries.md)
 - [FilterOverShortTournaments](docs/FilterOverShortTournaments.md)
 - [FilterOverShortVideogameVersions](docs/FilterOverShortVideogameVersions.md)
 - [FilterOverTeams](docs/FilterOverTeams.md)
 - [Game](docs/Game.md)
 - [GameID](docs/GameID.md)
 - [GameStatus](docs/GameStatus.md)
 - [GameWinner](docs/GameWinner.md)
 - [GetAdditions400Response](docs/GetAdditions400Response.md)
 - [GetAdditionsPageParameter](docs/GetAdditionsPageParameter.md)
 - [GetAdditionsPageParameterOneOf](docs/GetAdditionsPageParameterOneOf.md)
 - [GroupStanding](docs/GroupStanding.md)
 - [Incident](docs/Incident.md)
 - [IncidentChangeType](docs/IncidentChangeType.md)
 - [IncidentDeletionReason](docs/IncidentDeletionReason.md)
 - [IncidentDeletionReasonDeleted](docs/IncidentDeletionReasonDeleted.md)
 - [IncidentID](docs/IncidentID.md)
 - [IncidentOfTypeLeague](docs/IncidentOfTypeLeague.md)
 - [IncidentOfTypeMatch](docs/IncidentOfTypeMatch.md)
 - [IncidentOfTypePlayer](docs/IncidentOfTypePlayer.md)
 - [IncidentOfTypeSerie](docs/IncidentOfTypeSerie.md)
 - [IncidentOfTypeTeam](docs/IncidentOfTypeTeam.md)
 - [IncidentOfTypeTournament](docs/IncidentOfTypeTournament.md)
 - [IncidentType](docs/IncidentType.md)
 - [League](docs/League.md)
 - [LeagueIDOrSlug](docs/LeagueIDOrSlug.md)
 - [LeagueVideogame](docs/LeagueVideogame.md)
 - [LeagueVideogameCSGO](docs/LeagueVideogameCSGO.md)
 - [LeagueVideogameCodmw](docs/LeagueVideogameCodmw.md)
 - [LeagueVideogameDota2](docs/LeagueVideogameDota2.md)
 - [LeagueVideogameFifa](docs/LeagueVideogameFifa.md)
 - [LeagueVideogameFortnite](docs/LeagueVideogameFortnite.md)
 - [LeagueVideogameLoL](docs/LeagueVideogameLoL.md)
 - [LeagueVideogameOverwatch](docs/LeagueVideogameOverwatch.md)
 - [LeagueVideogamePUBG](docs/LeagueVideogamePUBG.md)
 - [LeagueVideogameR6siege](docs/LeagueVideogameR6siege.md)
 - [LeagueVideogameRocketLeague](docs/LeagueVideogameRocketLeague.md)
 - [LeagueVideogameValorant](docs/LeagueVideogameValorant.md)
 - [Live](docs/Live.md)
 - [LiveEndpoint](docs/LiveEndpoint.md)
 - [LiveEvent](docs/LiveEvent.md)
 - [LiveEvent1](docs/LiveEvent1.md)
 - [LiveType](docs/LiveType.md)
 - [LoLTeamColor](docs/LoLTeamColor.md)
 - [Market](docs/Market.md)
 - [MarketSelection](docs/MarketSelection.md)
 - [MarketStatus](docs/MarketStatus.md)
 - [Match](docs/Match.md)
 - [MatchIDOrSlug](docs/MatchIDOrSlug.md)
 - [MatchLive](docs/MatchLive.md)
 - [MatchLocalizedStream](docs/MatchLocalizedStream.md)
 - [MatchLocalizedStreams](docs/MatchLocalizedStreams.md)
 - [MatchMarketGame](docs/MatchMarketGame.md)
 - [MatchMarkets](docs/MatchMarkets.md)
 - [MatchOpponentBasePlayer](docs/MatchOpponentBasePlayer.md)
 - [MatchOpponentsObject](docs/MatchOpponentsObject.md)
 - [MatchPlayerOpponentsObject](docs/MatchPlayerOpponentsObject.md)
 - [MatchPlayerResult](docs/MatchPlayerResult.md)
 - [MatchResult](docs/MatchResult.md)
 - [MatchStatus](docs/MatchStatus.md)
 - [MatchTeamOpponentsObject](docs/MatchTeamOpponentsObject.md)
 - [MatchTeamResult](docs/MatchTeamResult.md)
 - [MatchType](docs/MatchType.md)
 - [NonDeletionIncident](docs/NonDeletionIncident.md)
 - [Opponent](docs/Opponent.md)
 - [OpponentID](docs/OpponentID.md)
 - [OpponentID1](docs/OpponentID1.md)
 - [OpponentType](docs/OpponentType.md)
 - [OpponentTypePlayer](docs/OpponentTypePlayer.md)
 - [OpponentTypeTeam](docs/OpponentTypeTeam.md)
 - [OwHeroIDOrSlug](docs/OwHeroIDOrSlug.md)
 - [OwMapIDOrSlug](docs/OwMapIDOrSlug.md)
 - [Player](docs/Player.md)
 - [PlayerIDOrSlug](docs/PlayerIDOrSlug.md)
 - [PreviousMatch](docs/PreviousMatch.md)
 - [PreviousMatchType](docs/PreviousMatchType.md)
 - [RangeOverBrackets](docs/RangeOverBrackets.md)
 - [RangeOverLeagues](docs/RangeOverLeagues.md)
 - [RangeOverMatches](docs/RangeOverMatches.md)
 - [RangeOverPlayers](docs/RangeOverPlayers.md)
 - [RangeOverSeries](docs/RangeOverSeries.md)
 - [RangeOverShortTournaments](docs/RangeOverShortTournaments.md)
 - [RangeOverShortVideogameVersions](docs/RangeOverShortVideogameVersions.md)
 - [RangeOverTeams](docs/RangeOverTeams.md)
 - [SearchOverBrackets](docs/SearchOverBrackets.md)
 - [SearchOverLeagues](docs/SearchOverLeagues.md)
 - [SearchOverMatches](docs/SearchOverMatches.md)
 - [SearchOverPlayers](docs/SearchOverPlayers.md)
 - [SearchOverSeries](docs/SearchOverSeries.md)
 - [SearchOverShortTournaments](docs/SearchOverShortTournaments.md)
 - [SearchOverShortVideogameVersions](docs/SearchOverShortVideogameVersions.md)
 - [SearchOverTeams](docs/SearchOverTeams.md)
 - [SelectionResult](docs/SelectionResult.md)
 - [Serie](docs/Serie.md)
 - [SerieIDOrSlug](docs/SerieIDOrSlug.md)
 - [ShortTournament](docs/ShortTournament.md)
 - [ShortVideogameVersion](docs/ShortVideogameVersion.md)
 - [ShortVideogameVersion1](docs/ShortVideogameVersion1.md)
 - [Standing](docs/Standing.md)
 - [Stream](docs/Stream.md)
 - [StreamLanguage](docs/StreamLanguage.md)
 - [Team](docs/Team.md)
 - [TeamIDOrSlug](docs/TeamIDOrSlug.md)
 - [Tournament](docs/Tournament.md)
 - [TournamentIDOrSlug](docs/TournamentIDOrSlug.md)
 - [TournamentPlayerRosters](docs/TournamentPlayerRosters.md)
 - [TournamentRosterItem](docs/TournamentRosterItem.md)
 - [TournamentRosters](docs/TournamentRosters.md)
 - [TournamentTeamRosters](docs/TournamentTeamRosters.md)
 - [Videogame](docs/Videogame.md)
 - [VideogameCSGO](docs/VideogameCSGO.md)
 - [VideogameCodmw](docs/VideogameCodmw.md)
 - [VideogameDota2](docs/VideogameDota2.md)
 - [VideogameFifa](docs/VideogameFifa.md)
 - [VideogameID](docs/VideogameID.md)
 - [VideogameIDOrSlug](docs/VideogameIDOrSlug.md)
 - [VideogameLeague](docs/VideogameLeague.md)
 - [VideogameLoL](docs/VideogameLoL.md)
 - [VideogameOverwatch](docs/VideogameOverwatch.md)
 - [VideogamePUBG](docs/VideogamePUBG.md)
 - [VideogameR6siege](docs/VideogameR6siege.md)
 - [VideogameRocketLeague](docs/VideogameRocketLeague.md)
 - [VideogameSlug](docs/VideogameSlug.md)
 - [VideogameTitle](docs/VideogameTitle.md)
 - [VideogameTitle1](docs/VideogameTitle1.md)
 - [VideogameValorant](docs/VideogameValorant.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="BearerToken"></a>
### BearerToken

- **Type**: HTTP Bearer Token authentication

<a id="QueryToken"></a>
### QueryToken

- **Type**: API key
- **API key parameter name**: token
- **Location**: URL query string


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



