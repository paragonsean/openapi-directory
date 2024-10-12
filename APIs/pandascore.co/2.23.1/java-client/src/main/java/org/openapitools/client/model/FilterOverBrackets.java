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
import java.net.URI;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.MatchStatus;
import org.openapitools.client.model.MatchType;
import org.openapitools.client.model.OpponentID;

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
 * FilterOverBrackets
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FilterOverBrackets {
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

  public static final String SERIALIZED_NAME_FORFEIT = "forfeit";
  @SerializedName(SERIALIZED_NAME_FORFEIT)
  private Boolean forfeit;

  public static final String SERIALIZED_NAME_GAME_ADVANTAGE = "game_advantage";
  @SerializedName(SERIALIZED_NAME_GAME_ADVANTAGE)
  private List<OpponentID> gameAdvantage = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private List<Integer> id = new ArrayList<>();

  public static final String SERIALIZED_NAME_LIVE_EMBED_URL = "live_embed_url";
  @SerializedName(SERIALIZED_NAME_LIVE_EMBED_URL)
  private List<URI> liveEmbedUrl = new ArrayList<>();

  public static final String SERIALIZED_NAME_MATCH_TYPE = "match_type";
  @SerializedName(SERIALIZED_NAME_MATCH_TYPE)
  private List<MatchType> matchType = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODIFIED_AT = "modified_at";
  @SerializedName(SERIALIZED_NAME_MODIFIED_AT)
  private List<OffsetDateTime> modifiedAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private List<String> name = new ArrayList<>();

  public static final String SERIALIZED_NAME_NUMBER_OF_GAMES = "number_of_games";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_GAMES)
  private List<Integer> numberOfGames = new ArrayList<>();

  public static final String SERIALIZED_NAME_OFFICIAL_STREAM_URL = "official_stream_url";
  @SerializedName(SERIALIZED_NAME_OFFICIAL_STREAM_URL)
  private List<URI> officialStreamUrl = new ArrayList<>();

  public static final String SERIALIZED_NAME_ORIGINAL_SCHEDULED_AT = "original_scheduled_at";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_SCHEDULED_AT)
  private List<OffsetDateTime> originalScheduledAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_SCHEDULED_AT = "scheduled_at";
  @SerializedName(SERIALIZED_NAME_SCHEDULED_AT)
  private List<OffsetDateTime> scheduledAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private List<String> slug = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private List<MatchStatus> status = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOURNAMENT_ID = "tournament_id";
  @SerializedName(SERIALIZED_NAME_TOURNAMENT_ID)
  private List<Integer> tournamentId = new ArrayList<>();

  public static final String SERIALIZED_NAME_WINNER_ID = "winner_id";
  @SerializedName(SERIALIZED_NAME_WINNER_ID)
  private List<OpponentID> winnerId = new ArrayList<>();

  public FilterOverBrackets() {
  }

  public FilterOverBrackets beginAt(List<OffsetDateTime> beginAt) {
    this.beginAt = beginAt;
    return this;
  }

  public FilterOverBrackets addBeginAtItem(OffsetDateTime beginAtItem) {
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


  public FilterOverBrackets detailedStats(Boolean detailedStats) {
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


  public FilterOverBrackets draw(Boolean draw) {
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


  public FilterOverBrackets endAt(List<OffsetDateTime> endAt) {
    this.endAt = endAt;
    return this;
  }

  public FilterOverBrackets addEndAtItem(OffsetDateTime endAtItem) {
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


  public FilterOverBrackets forfeit(Boolean forfeit) {
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


  public FilterOverBrackets gameAdvantage(List<OpponentID> gameAdvantage) {
    this.gameAdvantage = gameAdvantage;
    return this;
  }

  public FilterOverBrackets addGameAdvantageItem(OpponentID gameAdvantageItem) {
    if (this.gameAdvantage == null) {
      this.gameAdvantage = new ArrayList<>();
    }
    this.gameAdvantage.add(gameAdvantageItem);
    return this;
  }

  /**
   * Get gameAdvantage
   * @return gameAdvantage
   */
  @javax.annotation.Nullable
  public List<OpponentID> getGameAdvantage() {
    return gameAdvantage;
  }

  public void setGameAdvantage(List<OpponentID> gameAdvantage) {
    this.gameAdvantage = gameAdvantage;
  }


  public FilterOverBrackets id(List<Integer> id) {
    this.id = id;
    return this;
  }

  public FilterOverBrackets addIdItem(Integer idItem) {
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


  public FilterOverBrackets liveEmbedUrl(List<URI> liveEmbedUrl) {
    this.liveEmbedUrl = liveEmbedUrl;
    return this;
  }

  public FilterOverBrackets addLiveEmbedUrlItem(URI liveEmbedUrlItem) {
    if (this.liveEmbedUrl == null) {
      this.liveEmbedUrl = new ArrayList<>();
    }
    this.liveEmbedUrl.add(liveEmbedUrlItem);
    return this;
  }

  /**
   * Get liveEmbedUrl
   * @return liveEmbedUrl
   */
  @javax.annotation.Nullable
  public List<URI> getLiveEmbedUrl() {
    return liveEmbedUrl;
  }

  public void setLiveEmbedUrl(List<URI> liveEmbedUrl) {
    this.liveEmbedUrl = liveEmbedUrl;
  }


  public FilterOverBrackets matchType(List<MatchType> matchType) {
    this.matchType = matchType;
    return this;
  }

  public FilterOverBrackets addMatchTypeItem(MatchType matchTypeItem) {
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


  public FilterOverBrackets modifiedAt(List<OffsetDateTime> modifiedAt) {
    this.modifiedAt = modifiedAt;
    return this;
  }

  public FilterOverBrackets addModifiedAtItem(OffsetDateTime modifiedAtItem) {
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


  public FilterOverBrackets name(List<String> name) {
    this.name = name;
    return this;
  }

  public FilterOverBrackets addNameItem(String nameItem) {
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


  public FilterOverBrackets numberOfGames(List<Integer> numberOfGames) {
    this.numberOfGames = numberOfGames;
    return this;
  }

  public FilterOverBrackets addNumberOfGamesItem(Integer numberOfGamesItem) {
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


  public FilterOverBrackets officialStreamUrl(List<URI> officialStreamUrl) {
    this.officialStreamUrl = officialStreamUrl;
    return this;
  }

  public FilterOverBrackets addOfficialStreamUrlItem(URI officialStreamUrlItem) {
    if (this.officialStreamUrl == null) {
      this.officialStreamUrl = new ArrayList<>();
    }
    this.officialStreamUrl.add(officialStreamUrlItem);
    return this;
  }

  /**
   * Get officialStreamUrl
   * @return officialStreamUrl
   */
  @javax.annotation.Nullable
  public List<URI> getOfficialStreamUrl() {
    return officialStreamUrl;
  }

  public void setOfficialStreamUrl(List<URI> officialStreamUrl) {
    this.officialStreamUrl = officialStreamUrl;
  }


  public FilterOverBrackets originalScheduledAt(List<OffsetDateTime> originalScheduledAt) {
    this.originalScheduledAt = originalScheduledAt;
    return this;
  }

  public FilterOverBrackets addOriginalScheduledAtItem(OffsetDateTime originalScheduledAtItem) {
    if (this.originalScheduledAt == null) {
      this.originalScheduledAt = new ArrayList<>();
    }
    this.originalScheduledAt.add(originalScheduledAtItem);
    return this;
  }

  /**
   * Get originalScheduledAt
   * @return originalScheduledAt
   */
  @javax.annotation.Nullable
  public List<OffsetDateTime> getOriginalScheduledAt() {
    return originalScheduledAt;
  }

  public void setOriginalScheduledAt(List<OffsetDateTime> originalScheduledAt) {
    this.originalScheduledAt = originalScheduledAt;
  }


  public FilterOverBrackets scheduledAt(List<OffsetDateTime> scheduledAt) {
    this.scheduledAt = scheduledAt;
    return this;
  }

  public FilterOverBrackets addScheduledAtItem(OffsetDateTime scheduledAtItem) {
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


  public FilterOverBrackets slug(List<String> slug) {
    this.slug = slug;
    return this;
  }

  public FilterOverBrackets addSlugItem(String slugItem) {
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


  public FilterOverBrackets status(List<MatchStatus> status) {
    this.status = status;
    return this;
  }

  public FilterOverBrackets addStatusItem(MatchStatus statusItem) {
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


  public FilterOverBrackets tournamentId(List<Integer> tournamentId) {
    this.tournamentId = tournamentId;
    return this;
  }

  public FilterOverBrackets addTournamentIdItem(Integer tournamentIdItem) {
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


  public FilterOverBrackets winnerId(List<OpponentID> winnerId) {
    this.winnerId = winnerId;
    return this;
  }

  public FilterOverBrackets addWinnerIdItem(OpponentID winnerIdItem) {
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
    FilterOverBrackets filterOverBrackets = (FilterOverBrackets) o;
    return Objects.equals(this.beginAt, filterOverBrackets.beginAt) &&
        Objects.equals(this.detailedStats, filterOverBrackets.detailedStats) &&
        Objects.equals(this.draw, filterOverBrackets.draw) &&
        Objects.equals(this.endAt, filterOverBrackets.endAt) &&
        Objects.equals(this.forfeit, filterOverBrackets.forfeit) &&
        Objects.equals(this.gameAdvantage, filterOverBrackets.gameAdvantage) &&
        Objects.equals(this.id, filterOverBrackets.id) &&
        Objects.equals(this.liveEmbedUrl, filterOverBrackets.liveEmbedUrl) &&
        Objects.equals(this.matchType, filterOverBrackets.matchType) &&
        Objects.equals(this.modifiedAt, filterOverBrackets.modifiedAt) &&
        Objects.equals(this.name, filterOverBrackets.name) &&
        Objects.equals(this.numberOfGames, filterOverBrackets.numberOfGames) &&
        Objects.equals(this.officialStreamUrl, filterOverBrackets.officialStreamUrl) &&
        Objects.equals(this.originalScheduledAt, filterOverBrackets.originalScheduledAt) &&
        Objects.equals(this.scheduledAt, filterOverBrackets.scheduledAt) &&
        Objects.equals(this.slug, filterOverBrackets.slug) &&
        Objects.equals(this.status, filterOverBrackets.status) &&
        Objects.equals(this.tournamentId, filterOverBrackets.tournamentId) &&
        Objects.equals(this.winnerId, filterOverBrackets.winnerId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, detailedStats, draw, endAt, forfeit, gameAdvantage, id, liveEmbedUrl, matchType, modifiedAt, name, numberOfGames, officialStreamUrl, originalScheduledAt, scheduledAt, slug, status, tournamentId, winnerId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FilterOverBrackets {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    detailedStats: ").append(toIndentedString(detailedStats)).append("\n");
    sb.append("    draw: ").append(toIndentedString(draw)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    forfeit: ").append(toIndentedString(forfeit)).append("\n");
    sb.append("    gameAdvantage: ").append(toIndentedString(gameAdvantage)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    liveEmbedUrl: ").append(toIndentedString(liveEmbedUrl)).append("\n");
    sb.append("    matchType: ").append(toIndentedString(matchType)).append("\n");
    sb.append("    modifiedAt: ").append(toIndentedString(modifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    numberOfGames: ").append(toIndentedString(numberOfGames)).append("\n");
    sb.append("    officialStreamUrl: ").append(toIndentedString(officialStreamUrl)).append("\n");
    sb.append("    originalScheduledAt: ").append(toIndentedString(originalScheduledAt)).append("\n");
    sb.append("    scheduledAt: ").append(toIndentedString(scheduledAt)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    tournamentId: ").append(toIndentedString(tournamentId)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("live_embed_url");
    openapiFields.add("match_type");
    openapiFields.add("modified_at");
    openapiFields.add("name");
    openapiFields.add("number_of_games");
    openapiFields.add("official_stream_url");
    openapiFields.add("original_scheduled_at");
    openapiFields.add("scheduled_at");
    openapiFields.add("slug");
    openapiFields.add("status");
    openapiFields.add("tournament_id");
    openapiFields.add("winner_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FilterOverBrackets
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FilterOverBrackets.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FilterOverBrackets is not found in the empty JSON string", FilterOverBrackets.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FilterOverBrackets.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FilterOverBrackets` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      if (jsonObj.get("game_advantage") != null && !jsonObj.get("game_advantage").isJsonNull()) {
        JsonArray jsonArraygameAdvantage = jsonObj.getAsJsonArray("game_advantage");
        if (jsonArraygameAdvantage != null) {
          // ensure the json data is an array
          if (!jsonObj.get("game_advantage").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `game_advantage` to be an array in the JSON string but got `%s`", jsonObj.get("game_advantage").toString()));
          }

          // validate the optional field `game_advantage` (array)
          for (int i = 0; i < jsonArraygameAdvantage.size(); i++) {
            OpponentID.validateJsonElement(jsonArraygameAdvantage.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull() && !jsonObj.get("id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be an array in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("live_embed_url") != null && !jsonObj.get("live_embed_url").isJsonNull() && !jsonObj.get("live_embed_url").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `live_embed_url` to be an array in the JSON string but got `%s`", jsonObj.get("live_embed_url").toString()));
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
      // ensure the optional json data is an array if present
      if (jsonObj.get("official_stream_url") != null && !jsonObj.get("official_stream_url").isJsonNull() && !jsonObj.get("official_stream_url").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `official_stream_url` to be an array in the JSON string but got `%s`", jsonObj.get("official_stream_url").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("original_scheduled_at") != null && !jsonObj.get("original_scheduled_at").isJsonNull() && !jsonObj.get("original_scheduled_at").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `original_scheduled_at` to be an array in the JSON string but got `%s`", jsonObj.get("original_scheduled_at").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("scheduled_at") != null && !jsonObj.get("scheduled_at").isJsonNull() && !jsonObj.get("scheduled_at").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `scheduled_at` to be an array in the JSON string but got `%s`", jsonObj.get("scheduled_at").toString()));
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
       if (!FilterOverBrackets.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FilterOverBrackets' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FilterOverBrackets> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FilterOverBrackets.class));

       return (TypeAdapter<T>) new TypeAdapter<FilterOverBrackets>() {
           @Override
           public void write(JsonWriter out, FilterOverBrackets value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FilterOverBrackets read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FilterOverBrackets given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FilterOverBrackets
   * @throws IOException if the JSON string is invalid with respect to FilterOverBrackets
   */
  public static FilterOverBrackets fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FilterOverBrackets.class);
  }

  /**
   * Convert an instance of FilterOverBrackets to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

