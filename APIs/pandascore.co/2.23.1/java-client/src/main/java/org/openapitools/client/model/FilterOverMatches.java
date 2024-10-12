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
import org.openapitools.client.model.MatchStatus;
import org.openapitools.client.model.MatchType;
import org.openapitools.client.model.OpponentID;
import org.openapitools.client.model.TeamIDOrSlug;
import org.openapitools.client.model.VideogameIDOrSlug;

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
 * FilterOverMatches
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FilterOverMatches {
  public static final String SERIALIZED_NAME_BEGIN_AT = "begin_at";
  @SerializedName(SERIALIZED_NAME_BEGIN_AT)
  private List<OffsetDateTime> beginAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_DETAILED_STATS = "detailed_stats";
  @SerializedName(SERIALIZED_NAME_DETAILED_STATS)
  private Boolean detailedStats;

  public static final String SERIALIZED_NAME_DRAW = "draw";
  @SerializedName(SERIALIZED_NAME_DRAW)
  private Boolean draw;

  public static final String SERIALIZED_NAME_END_AT = "end_at";
  @SerializedName(SERIALIZED_NAME_END_AT)
  private List<OffsetDateTime> endAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_FINISHED = "finished";
  @SerializedName(SERIALIZED_NAME_FINISHED)
  private Boolean finished;

  public static final String SERIALIZED_NAME_FORFEIT = "forfeit";
  @SerializedName(SERIALIZED_NAME_FORFEIT)
  private Boolean forfeit;

  public static final String SERIALIZED_NAME_FUTURE = "future";
  @SerializedName(SERIALIZED_NAME_FUTURE)
  private Boolean future;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private List<Integer> id = new ArrayList<>();

  public static final String SERIALIZED_NAME_LEAGUE_ID = "league_id";
  @SerializedName(SERIALIZED_NAME_LEAGUE_ID)
  private List<Integer> leagueId = new ArrayList<>();

  public static final String SERIALIZED_NAME_MATCH_TYPE = "match_type";
  @SerializedName(SERIALIZED_NAME_MATCH_TYPE)
  private List<MatchType> matchType = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODIFIED_AT = "modified_at";
  @SerializedName(SERIALIZED_NAME_MODIFIED_AT)
  private List<OffsetDateTime> modifiedAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private List<String> name = new ArrayList<>();

  public static final String SERIALIZED_NAME_NOT_STARTED = "not_started";
  @SerializedName(SERIALIZED_NAME_NOT_STARTED)
  private Boolean notStarted;

  public static final String SERIALIZED_NAME_NUMBER_OF_GAMES = "number_of_games";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_GAMES)
  private List<Integer> numberOfGames = new ArrayList<>();

  public static final String SERIALIZED_NAME_OPPONENT_ID = "opponent_id";
  @SerializedName(SERIALIZED_NAME_OPPONENT_ID)
  private List<TeamIDOrSlug> opponentId = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAST = "past";
  @SerializedName(SERIALIZED_NAME_PAST)
  private Boolean past;

  public static final String SERIALIZED_NAME_RUNNING = "running";
  @SerializedName(SERIALIZED_NAME_RUNNING)
  private Boolean running;

  public static final String SERIALIZED_NAME_SCHEDULED_AT = "scheduled_at";
  @SerializedName(SERIALIZED_NAME_SCHEDULED_AT)
  private List<OffsetDateTime> scheduledAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERIE_ID = "serie_id";
  @SerializedName(SERIALIZED_NAME_SERIE_ID)
  private List<Integer> serieId = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private List<String> slug = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private List<MatchStatus> status = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOURNAMENT_ID = "tournament_id";
  @SerializedName(SERIALIZED_NAME_TOURNAMENT_ID)
  private List<Integer> tournamentId = new ArrayList<>();

  public static final String SERIALIZED_NAME_UNSCHEDULED = "unscheduled";
  @SerializedName(SERIALIZED_NAME_UNSCHEDULED)
  private Boolean unscheduled;

  public static final String SERIALIZED_NAME_VIDEOGAME = "videogame";
  @SerializedName(SERIALIZED_NAME_VIDEOGAME)
  private List<VideogameIDOrSlug> videogame = new ArrayList<>();

  public static final String SERIALIZED_NAME_WINNER_ID = "winner_id";
  @SerializedName(SERIALIZED_NAME_WINNER_ID)
  private List<OpponentID> winnerId = new ArrayList<>();

  public FilterOverMatches() {
  }

  public FilterOverMatches beginAt(List<OffsetDateTime> beginAt) {
    this.beginAt = beginAt;
    return this;
  }

  public FilterOverMatches addBeginAtItem(OffsetDateTime beginAtItem) {
    if (this.beginAt == null) {
      this.beginAt = new ArrayList<>();
    }
    this.beginAt.add(beginAtItem);
    return this;
  }

  /**
   * Get beginAt
   * @return beginAt
   */
  @javax.annotation.Nullable
  public List<OffsetDateTime> getBeginAt() {
    return beginAt;
  }

  public void setBeginAt(List<OffsetDateTime> beginAt) {
    this.beginAt = beginAt;
  }


  public FilterOverMatches detailedStats(Boolean detailedStats) {
    this.detailedStats = detailedStats;
    return this;
  }

  /**
   * Whether the match offers full stats
   * @return detailedStats
   */
  @javax.annotation.Nullable
  public Boolean getDetailedStats() {
    return detailedStats;
  }

  public void setDetailedStats(Boolean detailedStats) {
    this.detailedStats = detailedStats;
  }


  public FilterOverMatches draw(Boolean draw) {
    this.draw = draw;
    return this;
  }

  /**
   * Whether result of the match is a draw
   * @return draw
   */
  @javax.annotation.Nullable
  public Boolean getDraw() {
    return draw;
  }

  public void setDraw(Boolean draw) {
    this.draw = draw;
  }


  public FilterOverMatches endAt(List<OffsetDateTime> endAt) {
    this.endAt = endAt;
    return this;
  }

  public FilterOverMatches addEndAtItem(OffsetDateTime endAtItem) {
    if (this.endAt == null) {
      this.endAt = new ArrayList<>();
    }
    this.endAt.add(endAtItem);
    return this;
  }

  /**
   * Get endAt
   * @return endAt
   */
  @javax.annotation.Nullable
  public List<OffsetDateTime> getEndAt() {
    return endAt;
  }

  public void setEndAt(List<OffsetDateTime> endAt) {
    this.endAt = endAt;
  }


  public FilterOverMatches finished(Boolean finished) {
    this.finished = finished;
    return this;
  }

  /**
   * Get finished
   * @return finished
   */
  @javax.annotation.Nullable
  public Boolean getFinished() {
    return finished;
  }

  public void setFinished(Boolean finished) {
    this.finished = finished;
  }


  public FilterOverMatches forfeit(Boolean forfeit) {
    this.forfeit = forfeit;
    return this;
  }

  /**
   * Whether match was forfeited
   * @return forfeit
   */
  @javax.annotation.Nullable
  public Boolean getForfeit() {
    return forfeit;
  }

  public void setForfeit(Boolean forfeit) {
    this.forfeit = forfeit;
  }


  public FilterOverMatches future(Boolean future) {
    this.future = future;
    return this;
  }

  /**
   * Get future
   * @return future
   */
  @javax.annotation.Nullable
  public Boolean getFuture() {
    return future;
  }

  public void setFuture(Boolean future) {
    this.future = future;
  }


  public FilterOverMatches id(List<Integer> id) {
    this.id = id;
    return this;
  }

  public FilterOverMatches addIdItem(Integer idItem) {
    if (this.id == null) {
      this.id = new ArrayList<>();
    }
    this.id.add(idItem);
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public List<Integer> getId() {
    return id;
  }

  public void setId(List<Integer> id) {
    this.id = id;
  }


  public FilterOverMatches leagueId(List<Integer> leagueId) {
    this.leagueId = leagueId;
    return this;
  }

  public FilterOverMatches addLeagueIdItem(Integer leagueIdItem) {
    if (this.leagueId == null) {
      this.leagueId = new ArrayList<>();
    }
    this.leagueId.add(leagueIdItem);
    return this;
  }

  /**
   * Get leagueId
   * @return leagueId
   */
  @javax.annotation.Nullable
  public List<Integer> getLeagueId() {
    return leagueId;
  }

  public void setLeagueId(List<Integer> leagueId) {
    this.leagueId = leagueId;
  }


  public FilterOverMatches matchType(List<MatchType> matchType) {
    this.matchType = matchType;
    return this;
  }

  public FilterOverMatches addMatchTypeItem(MatchType matchTypeItem) {
    if (this.matchType == null) {
      this.matchType = new ArrayList<>();
    }
    this.matchType.add(matchTypeItem);
    return this;
  }

  /**
   * Get matchType
   * @return matchType
   */
  @javax.annotation.Nullable
  public List<MatchType> getMatchType() {
    return matchType;
  }

  public void setMatchType(List<MatchType> matchType) {
    this.matchType = matchType;
  }


  public FilterOverMatches modifiedAt(List<OffsetDateTime> modifiedAt) {
    this.modifiedAt = modifiedAt;
    return this;
  }

  public FilterOverMatches addModifiedAtItem(OffsetDateTime modifiedAtItem) {
    if (this.modifiedAt == null) {
      this.modifiedAt = new ArrayList<>();
    }
    this.modifiedAt.add(modifiedAtItem);
    return this;
  }

  /**
   * Get modifiedAt
   * @return modifiedAt
   */
  @javax.annotation.Nullable
  public List<OffsetDateTime> getModifiedAt() {
    return modifiedAt;
  }

  public void setModifiedAt(List<OffsetDateTime> modifiedAt) {
    this.modifiedAt = modifiedAt;
  }


  public FilterOverMatches name(List<String> name) {
    this.name = name;
    return this;
  }

  public FilterOverMatches addNameItem(String nameItem) {
    if (this.name == null) {
      this.name = new ArrayList<>();
    }
    this.name.add(nameItem);
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public List<String> getName() {
    return name;
  }

  public void setName(List<String> name) {
    this.name = name;
  }


  public FilterOverMatches notStarted(Boolean notStarted) {
    this.notStarted = notStarted;
    return this;
  }

  /**
   * Get notStarted
   * @return notStarted
   */
  @javax.annotation.Nullable
  public Boolean getNotStarted() {
    return notStarted;
  }

  public void setNotStarted(Boolean notStarted) {
    this.notStarted = notStarted;
  }


  public FilterOverMatches numberOfGames(List<Integer> numberOfGames) {
    this.numberOfGames = numberOfGames;
    return this;
  }

  public FilterOverMatches addNumberOfGamesItem(Integer numberOfGamesItem) {
    if (this.numberOfGames == null) {
      this.numberOfGames = new ArrayList<>();
    }
    this.numberOfGames.add(numberOfGamesItem);
    return this;
  }

  /**
   * Get numberOfGames
   * @return numberOfGames
   */
  @javax.annotation.Nullable
  public List<Integer> getNumberOfGames() {
    return numberOfGames;
  }

  public void setNumberOfGames(List<Integer> numberOfGames) {
    this.numberOfGames = numberOfGames;
  }


  public FilterOverMatches opponentId(List<TeamIDOrSlug> opponentId) {
    this.opponentId = opponentId;
    return this;
  }

  public FilterOverMatches addOpponentIdItem(TeamIDOrSlug opponentIdItem) {
    if (this.opponentId == null) {
      this.opponentId = new ArrayList<>();
    }
    this.opponentId.add(opponentIdItem);
    return this;
  }

  /**
   * Get opponentId
   * @return opponentId
   */
  @javax.annotation.Nullable
  public List<TeamIDOrSlug> getOpponentId() {
    return opponentId;
  }

  public void setOpponentId(List<TeamIDOrSlug> opponentId) {
    this.opponentId = opponentId;
  }


  public FilterOverMatches past(Boolean past) {
    this.past = past;
    return this;
  }

  /**
   * Get past
   * @return past
   */
  @javax.annotation.Nullable
  public Boolean getPast() {
    return past;
  }

  public void setPast(Boolean past) {
    this.past = past;
  }


  public FilterOverMatches running(Boolean running) {
    this.running = running;
    return this;
  }

  /**
   * Get running
   * @return running
   */
  @javax.annotation.Nullable
  public Boolean getRunning() {
    return running;
  }

  public void setRunning(Boolean running) {
    this.running = running;
  }


  public FilterOverMatches scheduledAt(List<OffsetDateTime> scheduledAt) {
    this.scheduledAt = scheduledAt;
    return this;
  }

  public FilterOverMatches addScheduledAtItem(OffsetDateTime scheduledAtItem) {
    if (this.scheduledAt == null) {
      this.scheduledAt = new ArrayList<>();
    }
    this.scheduledAt.add(scheduledAtItem);
    return this;
  }

  /**
   * Get scheduledAt
   * @return scheduledAt
   */
  @javax.annotation.Nullable
  public List<OffsetDateTime> getScheduledAt() {
    return scheduledAt;
  }

  public void setScheduledAt(List<OffsetDateTime> scheduledAt) {
    this.scheduledAt = scheduledAt;
  }


  public FilterOverMatches serieId(List<Integer> serieId) {
    this.serieId = serieId;
    return this;
  }

  public FilterOverMatches addSerieIdItem(Integer serieIdItem) {
    if (this.serieId == null) {
      this.serieId = new ArrayList<>();
    }
    this.serieId.add(serieIdItem);
    return this;
  }

  /**
   * Get serieId
   * @return serieId
   */
  @javax.annotation.Nullable
  public List<Integer> getSerieId() {
    return serieId;
  }

  public void setSerieId(List<Integer> serieId) {
    this.serieId = serieId;
  }


  public FilterOverMatches slug(List<String> slug) {
    this.slug = slug;
    return this;
  }

  public FilterOverMatches addSlugItem(String slugItem) {
    if (this.slug == null) {
      this.slug = new ArrayList<>();
    }
    this.slug.add(slugItem);
    return this;
  }

  /**
   * Get slug
   * @return slug
   */
  @javax.annotation.Nullable
  public List<String> getSlug() {
    return slug;
  }

  public void setSlug(List<String> slug) {
    this.slug = slug;
  }


  public FilterOverMatches status(List<MatchStatus> status) {
    this.status = status;
    return this;
  }

  public FilterOverMatches addStatusItem(MatchStatus statusItem) {
    if (this.status == null) {
      this.status = new ArrayList<>();
    }
    this.status.add(statusItem);
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public List<MatchStatus> getStatus() {
    return status;
  }

  public void setStatus(List<MatchStatus> status) {
    this.status = status;
  }


  public FilterOverMatches tournamentId(List<Integer> tournamentId) {
    this.tournamentId = tournamentId;
    return this;
  }

  public FilterOverMatches addTournamentIdItem(Integer tournamentIdItem) {
    if (this.tournamentId == null) {
      this.tournamentId = new ArrayList<>();
    }
    this.tournamentId.add(tournamentIdItem);
    return this;
  }

  /**
   * Get tournamentId
   * @return tournamentId
   */
  @javax.annotation.Nullable
  public List<Integer> getTournamentId() {
    return tournamentId;
  }

  public void setTournamentId(List<Integer> tournamentId) {
    this.tournamentId = tournamentId;
  }


  public FilterOverMatches unscheduled(Boolean unscheduled) {
    this.unscheduled = unscheduled;
    return this;
  }

  /**
   * Get unscheduled
   * @return unscheduled
   */
  @javax.annotation.Nullable
  public Boolean getUnscheduled() {
    return unscheduled;
  }

  public void setUnscheduled(Boolean unscheduled) {
    this.unscheduled = unscheduled;
  }


  public FilterOverMatches videogame(List<VideogameIDOrSlug> videogame) {
    this.videogame = videogame;
    return this;
  }

  public FilterOverMatches addVideogameItem(VideogameIDOrSlug videogameItem) {
    if (this.videogame == null) {
      this.videogame = new ArrayList<>();
    }
    this.videogame.add(videogameItem);
    return this;
  }

  /**
   * Get videogame
   * @return videogame
   */
  @javax.annotation.Nullable
  public List<VideogameIDOrSlug> getVideogame() {
    return videogame;
  }

  public void setVideogame(List<VideogameIDOrSlug> videogame) {
    this.videogame = videogame;
  }


  public FilterOverMatches winnerId(List<OpponentID> winnerId) {
    this.winnerId = winnerId;
    return this;
  }

  public FilterOverMatches addWinnerIdItem(OpponentID winnerIdItem) {
    if (this.winnerId == null) {
      this.winnerId = new ArrayList<>();
    }
    this.winnerId.add(winnerIdItem);
    return this;
  }

  /**
   * Get winnerId
   * @return winnerId
   */
  @javax.annotation.Nullable
  public List<OpponentID> getWinnerId() {
    return winnerId;
  }

  public void setWinnerId(List<OpponentID> winnerId) {
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
    FilterOverMatches filterOverMatches = (FilterOverMatches) o;
    return Objects.equals(this.beginAt, filterOverMatches.beginAt) &&
        Objects.equals(this.detailedStats, filterOverMatches.detailedStats) &&
        Objects.equals(this.draw, filterOverMatches.draw) &&
        Objects.equals(this.endAt, filterOverMatches.endAt) &&
        Objects.equals(this.finished, filterOverMatches.finished) &&
        Objects.equals(this.forfeit, filterOverMatches.forfeit) &&
        Objects.equals(this.future, filterOverMatches.future) &&
        Objects.equals(this.id, filterOverMatches.id) &&
        Objects.equals(this.leagueId, filterOverMatches.leagueId) &&
        Objects.equals(this.matchType, filterOverMatches.matchType) &&
        Objects.equals(this.modifiedAt, filterOverMatches.modifiedAt) &&
        Objects.equals(this.name, filterOverMatches.name) &&
        Objects.equals(this.notStarted, filterOverMatches.notStarted) &&
        Objects.equals(this.numberOfGames, filterOverMatches.numberOfGames) &&
        Objects.equals(this.opponentId, filterOverMatches.opponentId) &&
        Objects.equals(this.past, filterOverMatches.past) &&
        Objects.equals(this.running, filterOverMatches.running) &&
        Objects.equals(this.scheduledAt, filterOverMatches.scheduledAt) &&
        Objects.equals(this.serieId, filterOverMatches.serieId) &&
        Objects.equals(this.slug, filterOverMatches.slug) &&
        Objects.equals(this.status, filterOverMatches.status) &&
        Objects.equals(this.tournamentId, filterOverMatches.tournamentId) &&
        Objects.equals(this.unscheduled, filterOverMatches.unscheduled) &&
        Objects.equals(this.videogame, filterOverMatches.videogame) &&
        Objects.equals(this.winnerId, filterOverMatches.winnerId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, detailedStats, draw, endAt, finished, forfeit, future, id, leagueId, matchType, modifiedAt, name, notStarted, numberOfGames, opponentId, past, running, scheduledAt, serieId, slug, status, tournamentId, unscheduled, videogame, winnerId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FilterOverMatches {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    detailedStats: ").append(toIndentedString(detailedStats)).append("\n");
    sb.append("    draw: ").append(toIndentedString(draw)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    finished: ").append(toIndentedString(finished)).append("\n");
    sb.append("    forfeit: ").append(toIndentedString(forfeit)).append("\n");
    sb.append("    future: ").append(toIndentedString(future)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    leagueId: ").append(toIndentedString(leagueId)).append("\n");
    sb.append("    matchType: ").append(toIndentedString(matchType)).append("\n");
    sb.append("    modifiedAt: ").append(toIndentedString(modifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notStarted: ").append(toIndentedString(notStarted)).append("\n");
    sb.append("    numberOfGames: ").append(toIndentedString(numberOfGames)).append("\n");
    sb.append("    opponentId: ").append(toIndentedString(opponentId)).append("\n");
    sb.append("    past: ").append(toIndentedString(past)).append("\n");
    sb.append("    running: ").append(toIndentedString(running)).append("\n");
    sb.append("    scheduledAt: ").append(toIndentedString(scheduledAt)).append("\n");
    sb.append("    serieId: ").append(toIndentedString(serieId)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    tournamentId: ").append(toIndentedString(tournamentId)).append("\n");
    sb.append("    unscheduled: ").append(toIndentedString(unscheduled)).append("\n");
    sb.append("    videogame: ").append(toIndentedString(videogame)).append("\n");
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
    openapiFields.add("finished");
    openapiFields.add("forfeit");
    openapiFields.add("future");
    openapiFields.add("id");
    openapiFields.add("league_id");
    openapiFields.add("match_type");
    openapiFields.add("modified_at");
    openapiFields.add("name");
    openapiFields.add("not_started");
    openapiFields.add("number_of_games");
    openapiFields.add("opponent_id");
    openapiFields.add("past");
    openapiFields.add("running");
    openapiFields.add("scheduled_at");
    openapiFields.add("serie_id");
    openapiFields.add("slug");
    openapiFields.add("status");
    openapiFields.add("tournament_id");
    openapiFields.add("unscheduled");
    openapiFields.add("videogame");
    openapiFields.add("winner_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FilterOverMatches
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FilterOverMatches.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FilterOverMatches is not found in the empty JSON string", FilterOverMatches.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FilterOverMatches.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FilterOverMatches` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("begin_at") != null && !jsonObj.get("begin_at").isJsonNull() && !jsonObj.get("begin_at").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `begin_at` to be an array in the JSON string but got `%s`", jsonObj.get("begin_at").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("end_at") != null && !jsonObj.get("end_at").isJsonNull() && !jsonObj.get("end_at").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_at` to be an array in the JSON string but got `%s`", jsonObj.get("end_at").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull() && !jsonObj.get("id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be an array in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("league_id") != null && !jsonObj.get("league_id").isJsonNull() && !jsonObj.get("league_id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `league_id` to be an array in the JSON string but got `%s`", jsonObj.get("league_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("match_type") != null && !jsonObj.get("match_type").isJsonNull() && !jsonObj.get("match_type").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `match_type` to be an array in the JSON string but got `%s`", jsonObj.get("match_type").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("modified_at") != null && !jsonObj.get("modified_at").isJsonNull() && !jsonObj.get("modified_at").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified_at` to be an array in the JSON string but got `%s`", jsonObj.get("modified_at").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull() && !jsonObj.get("name").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be an array in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("number_of_games") != null && !jsonObj.get("number_of_games").isJsonNull() && !jsonObj.get("number_of_games").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `number_of_games` to be an array in the JSON string but got `%s`", jsonObj.get("number_of_games").toString()));
      }
      if (jsonObj.get("opponent_id") != null && !jsonObj.get("opponent_id").isJsonNull()) {
        JsonArray jsonArrayopponentId = jsonObj.getAsJsonArray("opponent_id");
        if (jsonArrayopponentId != null) {
          // ensure the json data is an array
          if (!jsonObj.get("opponent_id").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `opponent_id` to be an array in the JSON string but got `%s`", jsonObj.get("opponent_id").toString()));
          }

          // validate the optional field `opponent_id` (array)
          for (int i = 0; i < jsonArrayopponentId.size(); i++) {
            TeamIDOrSlug.validateJsonElement(jsonArrayopponentId.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("scheduled_at") != null && !jsonObj.get("scheduled_at").isJsonNull() && !jsonObj.get("scheduled_at").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `scheduled_at` to be an array in the JSON string but got `%s`", jsonObj.get("scheduled_at").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("serie_id") != null && !jsonObj.get("serie_id").isJsonNull() && !jsonObj.get("serie_id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `serie_id` to be an array in the JSON string but got `%s`", jsonObj.get("serie_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("slug") != null && !jsonObj.get("slug").isJsonNull() && !jsonObj.get("slug").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be an array in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull() && !jsonObj.get("status").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be an array in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tournament_id") != null && !jsonObj.get("tournament_id").isJsonNull() && !jsonObj.get("tournament_id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tournament_id` to be an array in the JSON string but got `%s`", jsonObj.get("tournament_id").toString()));
      }
      if (jsonObj.get("videogame") != null && !jsonObj.get("videogame").isJsonNull()) {
        JsonArray jsonArrayvideogame = jsonObj.getAsJsonArray("videogame");
        if (jsonArrayvideogame != null) {
          // ensure the json data is an array
          if (!jsonObj.get("videogame").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `videogame` to be an array in the JSON string but got `%s`", jsonObj.get("videogame").toString()));
          }

          // validate the optional field `videogame` (array)
          for (int i = 0; i < jsonArrayvideogame.size(); i++) {
            VideogameIDOrSlug.validateJsonElement(jsonArrayvideogame.get(i));
          };
        }
      }
      if (jsonObj.get("winner_id") != null && !jsonObj.get("winner_id").isJsonNull()) {
        JsonArray jsonArraywinnerId = jsonObj.getAsJsonArray("winner_id");
        if (jsonArraywinnerId != null) {
          // ensure the json data is an array
          if (!jsonObj.get("winner_id").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `winner_id` to be an array in the JSON string but got `%s`", jsonObj.get("winner_id").toString()));
          }

          // validate the optional field `winner_id` (array)
          for (int i = 0; i < jsonArraywinnerId.size(); i++) {
            OpponentID.validateJsonElement(jsonArraywinnerId.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FilterOverMatches.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FilterOverMatches' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FilterOverMatches> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FilterOverMatches.class));

       return (TypeAdapter<T>) new TypeAdapter<FilterOverMatches>() {
           @Override
           public void write(JsonWriter out, FilterOverMatches value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FilterOverMatches read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FilterOverMatches given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FilterOverMatches
   * @throws IOException if the JSON string is invalid with respect to FilterOverMatches
   */
  public static FilterOverMatches fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FilterOverMatches.class);
  }

  /**
   * Convert an instance of FilterOverMatches to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

