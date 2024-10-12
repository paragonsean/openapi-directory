/*
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BaseLeague;
import org.openapitools.client.model.BaseOpponent1;
import org.openapitools.client.model.BaseSerie;
import org.openapitools.client.model.BaseTournament;
import org.openapitools.client.model.CurrentVideogame;
import org.openapitools.client.model.Game;
import org.openapitools.client.model.MatchLive;
import org.openapitools.client.model.MatchLocalizedStreams;
import org.openapitools.client.model.MatchResult;
import org.openapitools.client.model.MatchStatus;
import org.openapitools.client.model.MatchType;
import org.openapitools.client.model.Opponent;
import org.openapitools.client.model.OpponentID1;
import org.openapitools.client.model.ShortVideogameVersion1;
import org.openapitools.client.model.Stream;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * Match
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Match {
  public static final String SERIALIZED_NAME_BEGIN_AT = "begin_at";
  @SerializedName(SERIALIZED_NAME_BEGIN_AT)
  private Object beginAt;

  public static final String SERIALIZED_NAME_DETAILED_STATS = "detailed_stats";
  @SerializedName(SERIALIZED_NAME_DETAILED_STATS)
  private Boolean detailedStats;

  public static final String SERIALIZED_NAME_DRAW = "draw";
  @SerializedName(SERIALIZED_NAME_DRAW)
  private Boolean draw;

  public static final String SERIALIZED_NAME_END_AT = "end_at";
  @SerializedName(SERIALIZED_NAME_END_AT)
  private Object endAt;

  public static final String SERIALIZED_NAME_FORFEIT = "forfeit";
  @SerializedName(SERIALIZED_NAME_FORFEIT)
  private Boolean forfeit;

  public static final String SERIALIZED_NAME_GAME_ADVANTAGE = "game_advantage";
  @SerializedName(SERIALIZED_NAME_GAME_ADVANTAGE)
  private OpponentID1 gameAdvantage;

  public static final String SERIALIZED_NAME_GAMES = "games";
  @SerializedName(SERIALIZED_NAME_GAMES)
  private List<Game> games = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LEAGUE = "league";
  @SerializedName(SERIALIZED_NAME_LEAGUE)
  private BaseLeague league;

  public static final String SERIALIZED_NAME_LEAGUE_ID = "league_id";
  @SerializedName(SERIALIZED_NAME_LEAGUE_ID)
  private Integer leagueId;

  public static final String SERIALIZED_NAME_LIVE = "live";
  @SerializedName(SERIALIZED_NAME_LIVE)
  private MatchLive live;

  public static final String SERIALIZED_NAME_LIVE_EMBED_URL = "live_embed_url";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_LIVE_EMBED_URL)
  private Object liveEmbedUrl;

  public static final String SERIALIZED_NAME_MATCH_TYPE = "match_type";
  @SerializedName(SERIALIZED_NAME_MATCH_TYPE)
  private MatchType matchType;

  public static final String SERIALIZED_NAME_MODIFIED_AT = "modified_at";
  @SerializedName(SERIALIZED_NAME_MODIFIED_AT)
  private OffsetDateTime modifiedAt;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NUMBER_OF_GAMES = "number_of_games";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_GAMES)
  private Integer numberOfGames;

  public static final String SERIALIZED_NAME_OFFICIAL_STREAM_URL = "official_stream_url";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_OFFICIAL_STREAM_URL)
  private Object officialStreamUrl;

  public static final String SERIALIZED_NAME_OPPONENTS = "opponents";
  @SerializedName(SERIALIZED_NAME_OPPONENTS)
  private List<Opponent> opponents = new ArrayList<>();

  public static final String SERIALIZED_NAME_ORIGINAL_SCHEDULED_AT = "original_scheduled_at";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_SCHEDULED_AT)
  private Object originalScheduledAt;

  public static final String SERIALIZED_NAME_RESCHEDULED = "rescheduled";
  @SerializedName(SERIALIZED_NAME_RESCHEDULED)
  private Object rescheduled;

  public static final String SERIALIZED_NAME_RESULTS = "results";
  @SerializedName(SERIALIZED_NAME_RESULTS)
  private List<MatchResult> results = new ArrayList<>();

  public static final String SERIALIZED_NAME_SCHEDULED_AT = "scheduled_at";
  @SerializedName(SERIALIZED_NAME_SCHEDULED_AT)
  private Object scheduledAt;

  public static final String SERIALIZED_NAME_SERIE = "serie";
  @SerializedName(SERIALIZED_NAME_SERIE)
  private BaseSerie serie;

  public static final String SERIALIZED_NAME_SERIE_ID = "serie_id";
  @SerializedName(SERIALIZED_NAME_SERIE_ID)
  private Integer serieId;

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private Object slug;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private MatchStatus status;

  public static final String SERIALIZED_NAME_STREAMS = "streams";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_STREAMS)
  private MatchLocalizedStreams streams;

  public static final String SERIALIZED_NAME_STREAMS_LIST = "streams_list";
  @SerializedName(SERIALIZED_NAME_STREAMS_LIST)
  private List<Stream> streamsList = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOURNAMENT = "tournament";
  @SerializedName(SERIALIZED_NAME_TOURNAMENT)
  private BaseTournament tournament;

  public static final String SERIALIZED_NAME_TOURNAMENT_ID = "tournament_id";
  @SerializedName(SERIALIZED_NAME_TOURNAMENT_ID)
  private Integer tournamentId;

  public static final String SERIALIZED_NAME_VIDEOGAME = "videogame";
  @SerializedName(SERIALIZED_NAME_VIDEOGAME)
  private CurrentVideogame videogame;

  public static final String SERIALIZED_NAME_VIDEOGAME_VERSION = "videogame_version";
  @SerializedName(SERIALIZED_NAME_VIDEOGAME_VERSION)
  private ShortVideogameVersion1 videogameVersion;

  public static final String SERIALIZED_NAME_WINNER = "winner";
  @SerializedName(SERIALIZED_NAME_WINNER)
  private BaseOpponent1 winner;

  public static final String SERIALIZED_NAME_WINNER_ID = "winner_id";
  @SerializedName(SERIALIZED_NAME_WINNER_ID)
  private OpponentID1 winnerId;

  public Match() {
  }

  public Match beginAt(Object beginAt) {
    this.beginAt = beginAt;
    return this;
  }

  /**
   * Get beginAt
   * @return beginAt
   */
  @javax.annotation.Nonnull
  public Object getBeginAt() {
    return beginAt;
  }

  public void setBeginAt(Object beginAt) {
    this.beginAt = beginAt;
  }


  public Match detailedStats(Boolean detailedStats) {
    this.detailedStats = detailedStats;
    return this;
  }

  /**
   * Whether the match offers full stats
   * @return detailedStats
   */
  @javax.annotation.Nonnull
  public Boolean getDetailedStats() {
    return detailedStats;
  }

  public void setDetailedStats(Boolean detailedStats) {
    this.detailedStats = detailedStats;
  }


  public Match draw(Boolean draw) {
    this.draw = draw;
    return this;
  }

  /**
   * Whether result of the match is a draw
   * @return draw
   */
  @javax.annotation.Nonnull
  public Boolean getDraw() {
    return draw;
  }

  public void setDraw(Boolean draw) {
    this.draw = draw;
  }


  public Match endAt(Object endAt) {
    this.endAt = endAt;
    return this;
  }

  /**
   * Get endAt
   * @return endAt
   */
  @javax.annotation.Nonnull
  public Object getEndAt() {
    return endAt;
  }

  public void setEndAt(Object endAt) {
    this.endAt = endAt;
  }


  public Match forfeit(Boolean forfeit) {
    this.forfeit = forfeit;
    return this;
  }

  /**
   * Whether match was forfeited
   * @return forfeit
   */
  @javax.annotation.Nonnull
  public Boolean getForfeit() {
    return forfeit;
  }

  public void setForfeit(Boolean forfeit) {
    this.forfeit = forfeit;
  }


  public Match gameAdvantage(OpponentID1 gameAdvantage) {
    this.gameAdvantage = gameAdvantage;
    return this;
  }

  /**
   * Get gameAdvantage
   * @return gameAdvantage
   */
  @javax.annotation.Nonnull
  public OpponentID1 getGameAdvantage() {
    return gameAdvantage;
  }

  public void setGameAdvantage(OpponentID1 gameAdvantage) {
    this.gameAdvantage = gameAdvantage;
  }


  public Match games(List<Game> games) {
    this.games = games;
    return this;
  }

  public Match addGamesItem(Game gamesItem) {
    if (this.games == null) {
      this.games = new ArrayList<>();
    }
    this.games.add(gamesItem);
    return this;
  }

  /**
   * Get games
   * @return games
   */
  @javax.annotation.Nonnull
  public List<Game> getGames() {
    return games;
  }

  public void setGames(List<Game> games) {
    this.games = games;
  }


  public Match id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * minimum: 1
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public Match league(BaseLeague league) {
    this.league = league;
    return this;
  }

  /**
   * Get league
   * @return league
   */
  @javax.annotation.Nonnull
  public BaseLeague getLeague() {
    return league;
  }

  public void setLeague(BaseLeague league) {
    this.league = league;
  }


  public Match leagueId(Integer leagueId) {
    this.leagueId = leagueId;
    return this;
  }

  /**
   * Get leagueId
   * minimum: 1
   * @return leagueId
   */
  @javax.annotation.Nonnull
  public Integer getLeagueId() {
    return leagueId;
  }

  public void setLeagueId(Integer leagueId) {
    this.leagueId = leagueId;
  }


  public Match live(MatchLive live) {
    this.live = live;
    return this;
  }

  /**
   * Get live
   * @return live
   */
  @javax.annotation.Nonnull
  public MatchLive getLive() {
    return live;
  }

  public void setLive(MatchLive live) {
    this.live = live;
  }


  @Deprecated
  public Match liveEmbedUrl(Object liveEmbedUrl) {
    this.liveEmbedUrl = liveEmbedUrl;
    return this;
  }

  /**
   * Get liveEmbedUrl
   * @return liveEmbedUrl
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Object getLiveEmbedUrl() {
    return liveEmbedUrl;
  }

  @Deprecated
  public void setLiveEmbedUrl(Object liveEmbedUrl) {
    this.liveEmbedUrl = liveEmbedUrl;
  }


  public Match matchType(MatchType matchType) {
    this.matchType = matchType;
    return this;
  }

  /**
   * Get matchType
   * @return matchType
   */
  @javax.annotation.Nonnull
  public MatchType getMatchType() {
    return matchType;
  }

  public void setMatchType(MatchType matchType) {
    this.matchType = matchType;
  }


  public Match modifiedAt(OffsetDateTime modifiedAt) {
    this.modifiedAt = modifiedAt;
    return this;
  }

  /**
   * Get modifiedAt
   * @return modifiedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getModifiedAt() {
    return modifiedAt;
  }

  public void setModifiedAt(OffsetDateTime modifiedAt) {
    this.modifiedAt = modifiedAt;
  }


  public Match name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Match numberOfGames(Integer numberOfGames) {
    this.numberOfGames = numberOfGames;
    return this;
  }

  /**
   * Number of games
   * minimum: 0
   * @return numberOfGames
   */
  @javax.annotation.Nonnull
  public Integer getNumberOfGames() {
    return numberOfGames;
  }

  public void setNumberOfGames(Integer numberOfGames) {
    this.numberOfGames = numberOfGames;
  }


  @Deprecated
  public Match officialStreamUrl(Object officialStreamUrl) {
    this.officialStreamUrl = officialStreamUrl;
    return this;
  }

  /**
   * Get officialStreamUrl
   * @return officialStreamUrl
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Object getOfficialStreamUrl() {
    return officialStreamUrl;
  }

  @Deprecated
  public void setOfficialStreamUrl(Object officialStreamUrl) {
    this.officialStreamUrl = officialStreamUrl;
  }


  public Match opponents(List<Opponent> opponents) {
    this.opponents = opponents;
    return this;
  }

  public Match addOpponentsItem(Opponent opponentsItem) {
    if (this.opponents == null) {
      this.opponents = new ArrayList<>();
    }
    this.opponents.add(opponentsItem);
    return this;
  }

  /**
   * Get opponents
   * @return opponents
   */
  @javax.annotation.Nonnull
  public List<Opponent> getOpponents() {
    return opponents;
  }

  public void setOpponents(List<Opponent> opponents) {
    this.opponents = opponents;
  }


  public Match originalScheduledAt(Object originalScheduledAt) {
    this.originalScheduledAt = originalScheduledAt;
    return this;
  }

  /**
   * Get originalScheduledAt
   * @return originalScheduledAt
   */
  @javax.annotation.Nonnull
  public Object getOriginalScheduledAt() {
    return originalScheduledAt;
  }

  public void setOriginalScheduledAt(Object originalScheduledAt) {
    this.originalScheduledAt = originalScheduledAt;
  }


  public Match rescheduled(Object rescheduled) {
    this.rescheduled = rescheduled;
    return this;
  }

  /**
   * Get rescheduled
   * @return rescheduled
   */
  @javax.annotation.Nonnull
  public Object getRescheduled() {
    return rescheduled;
  }

  public void setRescheduled(Object rescheduled) {
    this.rescheduled = rescheduled;
  }


  public Match results(List<MatchResult> results) {
    this.results = results;
    return this;
  }

  public Match addResultsItem(MatchResult resultsItem) {
    if (this.results == null) {
      this.results = new ArrayList<>();
    }
    this.results.add(resultsItem);
    return this;
  }

  /**
   * Get results
   * @return results
   */
  @javax.annotation.Nonnull
  public List<MatchResult> getResults() {
    return results;
  }

  public void setResults(List<MatchResult> results) {
    this.results = results;
  }


  public Match scheduledAt(Object scheduledAt) {
    this.scheduledAt = scheduledAt;
    return this;
  }

  /**
   * Get scheduledAt
   * @return scheduledAt
   */
  @javax.annotation.Nonnull
  public Object getScheduledAt() {
    return scheduledAt;
  }

  public void setScheduledAt(Object scheduledAt) {
    this.scheduledAt = scheduledAt;
  }


  public Match serie(BaseSerie serie) {
    this.serie = serie;
    return this;
  }

  /**
   * Get serie
   * @return serie
   */
  @javax.annotation.Nonnull
  public BaseSerie getSerie() {
    return serie;
  }

  public void setSerie(BaseSerie serie) {
    this.serie = serie;
  }


  public Match serieId(Integer serieId) {
    this.serieId = serieId;
    return this;
  }

  /**
   * Get serieId
   * minimum: 1
   * @return serieId
   */
  @javax.annotation.Nonnull
  public Integer getSerieId() {
    return serieId;
  }

  public void setSerieId(Integer serieId) {
    this.serieId = serieId;
  }


  public Match slug(Object slug) {
    this.slug = slug;
    return this;
  }

  /**
   * Get slug
   * @return slug
   */
  @javax.annotation.Nonnull
  public Object getSlug() {
    return slug;
  }

  public void setSlug(Object slug) {
    this.slug = slug;
  }


  public Match status(MatchStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public MatchStatus getStatus() {
    return status;
  }

  public void setStatus(MatchStatus status) {
    this.status = status;
  }


  @Deprecated
  public Match streams(MatchLocalizedStreams streams) {
    this.streams = streams;
    return this;
  }

  /**
   * Get streams
   * @return streams
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public MatchLocalizedStreams getStreams() {
    return streams;
  }

  @Deprecated
  public void setStreams(MatchLocalizedStreams streams) {
    this.streams = streams;
  }


  public Match streamsList(List<Stream> streamsList) {
    this.streamsList = streamsList;
    return this;
  }

  public Match addStreamsListItem(Stream streamsListItem) {
    if (this.streamsList == null) {
      this.streamsList = new ArrayList<>();
    }
    this.streamsList.add(streamsListItem);
    return this;
  }

  /**
   * Get streamsList
   * @return streamsList
   */
  @javax.annotation.Nonnull
  public List<Stream> getStreamsList() {
    return streamsList;
  }

  public void setStreamsList(List<Stream> streamsList) {
    this.streamsList = streamsList;
  }


  public Match tournament(BaseTournament tournament) {
    this.tournament = tournament;
    return this;
  }

  /**
   * Get tournament
   * @return tournament
   */
  @javax.annotation.Nonnull
  public BaseTournament getTournament() {
    return tournament;
  }

  public void setTournament(BaseTournament tournament) {
    this.tournament = tournament;
  }


  public Match tournamentId(Integer tournamentId) {
    this.tournamentId = tournamentId;
    return this;
  }

  /**
   * Get tournamentId
   * minimum: 1
   * @return tournamentId
   */
  @javax.annotation.Nonnull
  public Integer getTournamentId() {
    return tournamentId;
  }

  public void setTournamentId(Integer tournamentId) {
    this.tournamentId = tournamentId;
  }


  public Match videogame(CurrentVideogame videogame) {
    this.videogame = videogame;
    return this;
  }

  /**
   * Get videogame
   * @return videogame
   */
  @javax.annotation.Nonnull
  public CurrentVideogame getVideogame() {
    return videogame;
  }

  public void setVideogame(CurrentVideogame videogame) {
    this.videogame = videogame;
  }


  public Match videogameVersion(ShortVideogameVersion1 videogameVersion) {
    this.videogameVersion = videogameVersion;
    return this;
  }

  /**
   * Get videogameVersion
   * @return videogameVersion
   */
  @javax.annotation.Nonnull
  public ShortVideogameVersion1 getVideogameVersion() {
    return videogameVersion;
  }

  public void setVideogameVersion(ShortVideogameVersion1 videogameVersion) {
    this.videogameVersion = videogameVersion;
  }


  public Match winner(BaseOpponent1 winner) {
    this.winner = winner;
    return this;
  }

  /**
   * Get winner
   * @return winner
   */
  @javax.annotation.Nonnull
  public BaseOpponent1 getWinner() {
    return winner;
  }

  public void setWinner(BaseOpponent1 winner) {
    this.winner = winner;
  }


  public Match winnerId(OpponentID1 winnerId) {
    this.winnerId = winnerId;
    return this;
  }

  /**
   * Get winnerId
   * @return winnerId
   */
  @javax.annotation.Nonnull
  public OpponentID1 getWinnerId() {
    return winnerId;
  }

  public void setWinnerId(OpponentID1 winnerId) {
    this.winnerId = winnerId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Match match = (Match) o;
    return Objects.equals(this.beginAt, match.beginAt) &&
        Objects.equals(this.detailedStats, match.detailedStats) &&
        Objects.equals(this.draw, match.draw) &&
        Objects.equals(this.endAt, match.endAt) &&
        Objects.equals(this.forfeit, match.forfeit) &&
        Objects.equals(this.gameAdvantage, match.gameAdvantage) &&
        Objects.equals(this.games, match.games) &&
        Objects.equals(this.id, match.id) &&
        Objects.equals(this.league, match.league) &&
        Objects.equals(this.leagueId, match.leagueId) &&
        Objects.equals(this.live, match.live) &&
        Objects.equals(this.liveEmbedUrl, match.liveEmbedUrl) &&
        Objects.equals(this.matchType, match.matchType) &&
        Objects.equals(this.modifiedAt, match.modifiedAt) &&
        Objects.equals(this.name, match.name) &&
        Objects.equals(this.numberOfGames, match.numberOfGames) &&
        Objects.equals(this.officialStreamUrl, match.officialStreamUrl) &&
        Objects.equals(this.opponents, match.opponents) &&
        Objects.equals(this.originalScheduledAt, match.originalScheduledAt) &&
        Objects.equals(this.rescheduled, match.rescheduled) &&
        Objects.equals(this.results, match.results) &&
        Objects.equals(this.scheduledAt, match.scheduledAt) &&
        Objects.equals(this.serie, match.serie) &&
        Objects.equals(this.serieId, match.serieId) &&
        Objects.equals(this.slug, match.slug) &&
        Objects.equals(this.status, match.status) &&
        Objects.equals(this.streams, match.streams) &&
        Objects.equals(this.streamsList, match.streamsList) &&
        Objects.equals(this.tournament, match.tournament) &&
        Objects.equals(this.tournamentId, match.tournamentId) &&
        Objects.equals(this.videogame, match.videogame) &&
        Objects.equals(this.videogameVersion, match.videogameVersion) &&
        Objects.equals(this.winner, match.winner) &&
        Objects.equals(this.winnerId, match.winnerId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, detailedStats, draw, endAt, forfeit, gameAdvantage, games, id, league, leagueId, live, liveEmbedUrl, matchType, modifiedAt, name, numberOfGames, officialStreamUrl, opponents, originalScheduledAt, rescheduled, results, scheduledAt, serie, serieId, slug, status, streams, streamsList, tournament, tournamentId, videogame, videogameVersion, winner, winnerId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Match {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    detailedStats: ").append(toIndentedString(detailedStats)).append("\n");
    sb.append("    draw: ").append(toIndentedString(draw)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    forfeit: ").append(toIndentedString(forfeit)).append("\n");
    sb.append("    gameAdvantage: ").append(toIndentedString(gameAdvantage)).append("\n");
    sb.append("    games: ").append(toIndentedString(games)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    league: ").append(toIndentedString(league)).append("\n");
    sb.append("    leagueId: ").append(toIndentedString(leagueId)).append("\n");
    sb.append("    live: ").append(toIndentedString(live)).append("\n");
    sb.append("    liveEmbedUrl: ").append(toIndentedString(liveEmbedUrl)).append("\n");
    sb.append("    matchType: ").append(toIndentedString(matchType)).append("\n");
    sb.append("    modifiedAt: ").append(toIndentedString(modifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    numberOfGames: ").append(toIndentedString(numberOfGames)).append("\n");
    sb.append("    officialStreamUrl: ").append(toIndentedString(officialStreamUrl)).append("\n");
    sb.append("    opponents: ").append(toIndentedString(opponents)).append("\n");
    sb.append("    originalScheduledAt: ").append(toIndentedString(originalScheduledAt)).append("\n");
    sb.append("    rescheduled: ").append(toIndentedString(rescheduled)).append("\n");
    sb.append("    results: ").append(toIndentedString(results)).append("\n");
    sb.append("    scheduledAt: ").append(toIndentedString(scheduledAt)).append("\n");
    sb.append("    serie: ").append(toIndentedString(serie)).append("\n");
    sb.append("    serieId: ").append(toIndentedString(serieId)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    streams: ").append(toIndentedString(streams)).append("\n");
    sb.append("    streamsList: ").append(toIndentedString(streamsList)).append("\n");
    sb.append("    tournament: ").append(toIndentedString(tournament)).append("\n");
    sb.append("    tournamentId: ").append(toIndentedString(tournamentId)).append("\n");
    sb.append("    videogame: ").append(toIndentedString(videogame)).append("\n");
    sb.append("    videogameVersion: ").append(toIndentedString(videogameVersion)).append("\n");
    sb.append("    winner: ").append(toIndentedString(winner)).append("\n");
    sb.append("    winnerId: ").append(toIndentedString(winnerId)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("begin_at");
    openapiFields.add("detailed_stats");
    openapiFields.add("draw");
    openapiFields.add("end_at");
    openapiFields.add("forfeit");
    openapiFields.add("game_advantage");
    openapiFields.add("games");
    openapiFields.add("id");
    openapiFields.add("league");
    openapiFields.add("league_id");
    openapiFields.add("live");
    openapiFields.add("live_embed_url");
    openapiFields.add("match_type");
    openapiFields.add("modified_at");
    openapiFields.add("name");
    openapiFields.add("number_of_games");
    openapiFields.add("official_stream_url");
    openapiFields.add("opponents");
    openapiFields.add("original_scheduled_at");
    openapiFields.add("rescheduled");
    openapiFields.add("results");
    openapiFields.add("scheduled_at");
    openapiFields.add("serie");
    openapiFields.add("serie_id");
    openapiFields.add("slug");
    openapiFields.add("status");
    openapiFields.add("streams");
    openapiFields.add("streams_list");
    openapiFields.add("tournament");
    openapiFields.add("tournament_id");
    openapiFields.add("videogame");
    openapiFields.add("videogame_version");
    openapiFields.add("winner");
    openapiFields.add("winner_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("begin_at");
    openapiRequiredFields.add("detailed_stats");
    openapiRequiredFields.add("draw");
    openapiRequiredFields.add("end_at");
    openapiRequiredFields.add("forfeit");
    openapiRequiredFields.add("game_advantage");
    openapiRequiredFields.add("games");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("league");
    openapiRequiredFields.add("league_id");
    openapiRequiredFields.add("live");
    openapiRequiredFields.add("live_embed_url");
    openapiRequiredFields.add("match_type");
    openapiRequiredFields.add("modified_at");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("number_of_games");
    openapiRequiredFields.add("official_stream_url");
    openapiRequiredFields.add("opponents");
    openapiRequiredFields.add("original_scheduled_at");
    openapiRequiredFields.add("rescheduled");
    openapiRequiredFields.add("results");
    openapiRequiredFields.add("scheduled_at");
    openapiRequiredFields.add("serie");
    openapiRequiredFields.add("serie_id");
    openapiRequiredFields.add("slug");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("streams");
    openapiRequiredFields.add("streams_list");
    openapiRequiredFields.add("tournament");
    openapiRequiredFields.add("tournament_id");
    openapiRequiredFields.add("videogame");
    openapiRequiredFields.add("videogame_version");
    openapiRequiredFields.add("winner");
    openapiRequiredFields.add("winner_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Match
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Match.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Match is not found in the empty JSON string", Match.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Match.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Match` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Match.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `begin_at`
      Object.validateJsonElement(jsonObj.get("begin_at"));
      // validate the required field `end_at`
      Object.validateJsonElement(jsonObj.get("end_at"));
      // validate the required field `game_advantage`
      OpponentID1.validateJsonElement(jsonObj.get("game_advantage"));
      // ensure the json data is an array
      if (!jsonObj.get("games").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `games` to be an array in the JSON string but got `%s`", jsonObj.get("games").toString()));
      }

      JsonArray jsonArraygames = jsonObj.getAsJsonArray("games");
      // validate the required field `games` (array)
      for (int i = 0; i < jsonArraygames.size(); i++) {
        Game.validateJsonElement(jsonArraygames.get(i));
      };
      // validate the required field `league`
      BaseLeague.validateJsonElement(jsonObj.get("league"));
      // validate the required field `live`
      MatchLive.validateJsonElement(jsonObj.get("live"));
      // validate the required field `live_embed_url`
      Object.validateJsonElement(jsonObj.get("live_embed_url"));
      // validate the required field `match_type`
      MatchType.validateJsonElement(jsonObj.get("match_type"));
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the required field `official_stream_url`
      Object.validateJsonElement(jsonObj.get("official_stream_url"));
      // ensure the json data is an array
      if (!jsonObj.get("opponents").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `opponents` to be an array in the JSON string but got `%s`", jsonObj.get("opponents").toString()));
      }

      JsonArray jsonArrayopponents = jsonObj.getAsJsonArray("opponents");
      // validate the required field `opponents` (array)
      for (int i = 0; i < jsonArrayopponents.size(); i++) {
        Opponent.validateJsonElement(jsonArrayopponents.get(i));
      };
      // validate the required field `original_scheduled_at`
      Object.validateJsonElement(jsonObj.get("original_scheduled_at"));
      // validate the required field `rescheduled`
      Object.validateJsonElement(jsonObj.get("rescheduled"));
      // ensure the json data is an array
      if (!jsonObj.get("results").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `results` to be an array in the JSON string but got `%s`", jsonObj.get("results").toString()));
      }

      JsonArray jsonArrayresults = jsonObj.getAsJsonArray("results");
      // validate the required field `results` (array)
      for (int i = 0; i < jsonArrayresults.size(); i++) {
        MatchResult.validateJsonElement(jsonArrayresults.get(i));
      };
      // validate the required field `scheduled_at`
      Object.validateJsonElement(jsonObj.get("scheduled_at"));
      // validate the required field `serie`
      BaseSerie.validateJsonElement(jsonObj.get("serie"));
      // validate the required field `slug`
      Object.validateJsonElement(jsonObj.get("slug"));
      // validate the required field `status`
      MatchStatus.validateJsonElement(jsonObj.get("status"));
      // validate the required field `streams`
      MatchLocalizedStreams.validateJsonElement(jsonObj.get("streams"));
      // ensure the json data is an array
      if (!jsonObj.get("streams_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `streams_list` to be an array in the JSON string but got `%s`", jsonObj.get("streams_list").toString()));
      }

      JsonArray jsonArraystreamsList = jsonObj.getAsJsonArray("streams_list");
      // validate the required field `streams_list` (array)
      for (int i = 0; i < jsonArraystreamsList.size(); i++) {
        Stream.validateJsonElement(jsonArraystreamsList.get(i));
      };
      // validate the required field `tournament`
      BaseTournament.validateJsonElement(jsonObj.get("tournament"));
      // validate the required field `videogame`
      CurrentVideogame.validateJsonElement(jsonObj.get("videogame"));
      // validate the required field `videogame`
      CurrentVideogame.validateJsonElement(jsonObj.get("videogame"));
      // validate the required field `videogame_version`
      ShortVideogameVersion1.validateJsonElement(jsonObj.get("videogame_version"));
      // validate the required field `winner`
      BaseOpponent1.validateJsonElement(jsonObj.get("winner"));
      // validate the required field `winner_id`
      OpponentID1.validateJsonElement(jsonObj.get("winner_id"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Match.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Match' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Match> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Match.class));

       return (TypeAdapter<T>) new TypeAdapter<Match>() {
           @Override
           public void write(JsonWriter out, Match value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Match read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Match given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Match
   * @throws IOException if the JSON string is invalid with respect to Match
   */
  public static Match fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Match.class);
  }

  /**
   * Convert an instance of Match to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

