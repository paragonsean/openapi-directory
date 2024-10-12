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
import org.openapitools.client.model.BaseMatch;
import org.openapitools.client.model.BaseSerie;
import org.openapitools.client.model.BaseTeam;
import org.openapitools.client.model.CurrentVideogame;
import org.openapitools.client.model.OpponentID1;
import org.openapitools.client.model.TournamentRosterItem;

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
 * Tournament
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Tournament {
  public static final String SERIALIZED_NAME_BEGIN_AT = "begin_at";
  @SerializedName(SERIALIZED_NAME_BEGIN_AT)
  private Object beginAt;

  public static final String SERIALIZED_NAME_END_AT = "end_at";
  @SerializedName(SERIALIZED_NAME_END_AT)
  private Object endAt;

  public static final String SERIALIZED_NAME_EXPECTED_ROSTER = "expected_roster";
  @SerializedName(SERIALIZED_NAME_EXPECTED_ROSTER)
  private List<TournamentRosterItem> expectedRoster = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LEAGUE = "league";
  @SerializedName(SERIALIZED_NAME_LEAGUE)
  private BaseLeague league;

  public static final String SERIALIZED_NAME_LEAGUE_ID = "league_id";
  @SerializedName(SERIALIZED_NAME_LEAGUE_ID)
  private Integer leagueId;

  public static final String SERIALIZED_NAME_LIVE_SUPPORTED = "live_supported";
  @SerializedName(SERIALIZED_NAME_LIVE_SUPPORTED)
  private Boolean liveSupported;

  public static final String SERIALIZED_NAME_MATCHES = "matches";
  @SerializedName(SERIALIZED_NAME_MATCHES)
  private List<BaseMatch> matches = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODIFIED_AT = "modified_at";
  @SerializedName(SERIALIZED_NAME_MODIFIED_AT)
  private OffsetDateTime modifiedAt;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PRIZEPOOL = "prizepool";
  @SerializedName(SERIALIZED_NAME_PRIZEPOOL)
  private Object prizepool;

  public static final String SERIALIZED_NAME_SERIE = "serie";
  @SerializedName(SERIALIZED_NAME_SERIE)
  private BaseSerie serie;

  public static final String SERIALIZED_NAME_SERIE_ID = "serie_id";
  @SerializedName(SERIALIZED_NAME_SERIE_ID)
  private Integer serieId;

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private String slug;

  public static final String SERIALIZED_NAME_TEAMS = "teams";
  @SerializedName(SERIALIZED_NAME_TEAMS)
  private List<BaseTeam> teams = new ArrayList<>();

  public static final String SERIALIZED_NAME_VIDEOGAME = "videogame";
  @SerializedName(SERIALIZED_NAME_VIDEOGAME)
  private CurrentVideogame videogame;

  public static final String SERIALIZED_NAME_WINNER_ID = "winner_id";
  @SerializedName(SERIALIZED_NAME_WINNER_ID)
  private OpponentID1 winnerId;

  public static final String SERIALIZED_NAME_WINNER_TYPE = "winner_type";
  @SerializedName(SERIALIZED_NAME_WINNER_TYPE)
  private Object winnerType;

  public Tournament() {
  }

  public Tournament beginAt(Object beginAt) {
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


  public Tournament endAt(Object endAt) {
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


  public Tournament expectedRoster(List<TournamentRosterItem> expectedRoster) {
    this.expectedRoster = expectedRoster;
    return this;
  }

  public Tournament addExpectedRosterItem(TournamentRosterItem expectedRosterItem) {
    if (this.expectedRoster == null) {
      this.expectedRoster = new ArrayList<>();
    }
    this.expectedRoster.add(expectedRosterItem);
    return this;
  }

  /**
   * Get expectedRoster
   * @return expectedRoster
   */
  @javax.annotation.Nonnull
  public List<TournamentRosterItem> getExpectedRoster() {
    return expectedRoster;
  }

  public void setExpectedRoster(List<TournamentRosterItem> expectedRoster) {
    this.expectedRoster = expectedRoster;
  }


  public Tournament id(Integer id) {
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


  public Tournament league(BaseLeague league) {
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


  public Tournament leagueId(Integer leagueId) {
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


  public Tournament liveSupported(Boolean liveSupported) {
    this.liveSupported = liveSupported;
    return this;
  }

  /**
   * Whether live is supported
   * @return liveSupported
   */
  @javax.annotation.Nonnull
  public Boolean getLiveSupported() {
    return liveSupported;
  }

  public void setLiveSupported(Boolean liveSupported) {
    this.liveSupported = liveSupported;
  }


  public Tournament matches(List<BaseMatch> matches) {
    this.matches = matches;
    return this;
  }

  public Tournament addMatchesItem(BaseMatch matchesItem) {
    if (this.matches == null) {
      this.matches = new ArrayList<>();
    }
    this.matches.add(matchesItem);
    return this;
  }

  /**
   * Get matches
   * @return matches
   */
  @javax.annotation.Nonnull
  public List<BaseMatch> getMatches() {
    return matches;
  }

  public void setMatches(List<BaseMatch> matches) {
    this.matches = matches;
  }


  public Tournament modifiedAt(OffsetDateTime modifiedAt) {
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


  public Tournament name(String name) {
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


  public Tournament prizepool(Object prizepool) {
    this.prizepool = prizepool;
    return this;
  }

  /**
   * Get prizepool
   * @return prizepool
   */
  @javax.annotation.Nonnull
  public Object getPrizepool() {
    return prizepool;
  }

  public void setPrizepool(Object prizepool) {
    this.prizepool = prizepool;
  }


  public Tournament serie(BaseSerie serie) {
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


  public Tournament serieId(Integer serieId) {
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


  public Tournament slug(String slug) {
    this.slug = slug;
    return this;
  }

  /**
   * Get slug
   * @return slug
   */
  @javax.annotation.Nonnull
  public String getSlug() {
    return slug;
  }

  public void setSlug(String slug) {
    this.slug = slug;
  }


  public Tournament teams(List<BaseTeam> teams) {
    this.teams = teams;
    return this;
  }

  public Tournament addTeamsItem(BaseTeam teamsItem) {
    if (this.teams == null) {
      this.teams = new ArrayList<>();
    }
    this.teams.add(teamsItem);
    return this;
  }

  /**
   * Get teams
   * @return teams
   */
  @javax.annotation.Nonnull
  public List<BaseTeam> getTeams() {
    return teams;
  }

  public void setTeams(List<BaseTeam> teams) {
    this.teams = teams;
  }


  public Tournament videogame(CurrentVideogame videogame) {
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


  public Tournament winnerId(OpponentID1 winnerId) {
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


  public Tournament winnerType(Object winnerType) {
    this.winnerType = winnerType;
    return this;
  }

  /**
   * Get winnerType
   * @return winnerType
   */
  @javax.annotation.Nonnull
  public Object getWinnerType() {
    return winnerType;
  }

  public void setWinnerType(Object winnerType) {
    this.winnerType = winnerType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Tournament tournament = (Tournament) o;
    return Objects.equals(this.beginAt, tournament.beginAt) &&
        Objects.equals(this.endAt, tournament.endAt) &&
        Objects.equals(this.expectedRoster, tournament.expectedRoster) &&
        Objects.equals(this.id, tournament.id) &&
        Objects.equals(this.league, tournament.league) &&
        Objects.equals(this.leagueId, tournament.leagueId) &&
        Objects.equals(this.liveSupported, tournament.liveSupported) &&
        Objects.equals(this.matches, tournament.matches) &&
        Objects.equals(this.modifiedAt, tournament.modifiedAt) &&
        Objects.equals(this.name, tournament.name) &&
        Objects.equals(this.prizepool, tournament.prizepool) &&
        Objects.equals(this.serie, tournament.serie) &&
        Objects.equals(this.serieId, tournament.serieId) &&
        Objects.equals(this.slug, tournament.slug) &&
        Objects.equals(this.teams, tournament.teams) &&
        Objects.equals(this.videogame, tournament.videogame) &&
        Objects.equals(this.winnerId, tournament.winnerId) &&
        Objects.equals(this.winnerType, tournament.winnerType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, endAt, expectedRoster, id, league, leagueId, liveSupported, matches, modifiedAt, name, prizepool, serie, serieId, slug, teams, videogame, winnerId, winnerType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Tournament {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    expectedRoster: ").append(toIndentedString(expectedRoster)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    league: ").append(toIndentedString(league)).append("\n");
    sb.append("    leagueId: ").append(toIndentedString(leagueId)).append("\n");
    sb.append("    liveSupported: ").append(toIndentedString(liveSupported)).append("\n");
    sb.append("    matches: ").append(toIndentedString(matches)).append("\n");
    sb.append("    modifiedAt: ").append(toIndentedString(modifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    prizepool: ").append(toIndentedString(prizepool)).append("\n");
    sb.append("    serie: ").append(toIndentedString(serie)).append("\n");
    sb.append("    serieId: ").append(toIndentedString(serieId)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    teams: ").append(toIndentedString(teams)).append("\n");
    sb.append("    videogame: ").append(toIndentedString(videogame)).append("\n");
    sb.append("    winnerId: ").append(toIndentedString(winnerId)).append("\n");
    sb.append("    winnerType: ").append(toIndentedString(winnerType)).append("\n");
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
    openapiFields.add("end_at");
    openapiFields.add("expected_roster");
    openapiFields.add("id");
    openapiFields.add("league");
    openapiFields.add("league_id");
    openapiFields.add("live_supported");
    openapiFields.add("matches");
    openapiFields.add("modified_at");
    openapiFields.add("name");
    openapiFields.add("prizepool");
    openapiFields.add("serie");
    openapiFields.add("serie_id");
    openapiFields.add("slug");
    openapiFields.add("teams");
    openapiFields.add("videogame");
    openapiFields.add("winner_id");
    openapiFields.add("winner_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("begin_at");
    openapiRequiredFields.add("end_at");
    openapiRequiredFields.add("expected_roster");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("league");
    openapiRequiredFields.add("league_id");
    openapiRequiredFields.add("live_supported");
    openapiRequiredFields.add("matches");
    openapiRequiredFields.add("modified_at");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("prizepool");
    openapiRequiredFields.add("serie");
    openapiRequiredFields.add("serie_id");
    openapiRequiredFields.add("slug");
    openapiRequiredFields.add("teams");
    openapiRequiredFields.add("videogame");
    openapiRequiredFields.add("winner_id");
    openapiRequiredFields.add("winner_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Tournament
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Tournament.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Tournament is not found in the empty JSON string", Tournament.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Tournament.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Tournament` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Tournament.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `begin_at`
      Object.validateJsonElement(jsonObj.get("begin_at"));
      // validate the required field `end_at`
      Object.validateJsonElement(jsonObj.get("end_at"));
      // ensure the json data is an array
      if (!jsonObj.get("expected_roster").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `expected_roster` to be an array in the JSON string but got `%s`", jsonObj.get("expected_roster").toString()));
      }

      JsonArray jsonArrayexpectedRoster = jsonObj.getAsJsonArray("expected_roster");
      // validate the required field `expected_roster` (array)
      for (int i = 0; i < jsonArrayexpectedRoster.size(); i++) {
        TournamentRosterItem.validateJsonElement(jsonArrayexpectedRoster.get(i));
      };
      // validate the required field `league`
      BaseLeague.validateJsonElement(jsonObj.get("league"));
      // ensure the json data is an array
      if (!jsonObj.get("matches").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `matches` to be an array in the JSON string but got `%s`", jsonObj.get("matches").toString()));
      }

      JsonArray jsonArraymatches = jsonObj.getAsJsonArray("matches");
      // validate the required field `matches` (array)
      for (int i = 0; i < jsonArraymatches.size(); i++) {
        BaseMatch.validateJsonElement(jsonArraymatches.get(i));
      };
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the required field `prizepool`
      Object.validateJsonElement(jsonObj.get("prizepool"));
      // validate the required field `serie`
      BaseSerie.validateJsonElement(jsonObj.get("serie"));
      if (!jsonObj.get("slug").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be a primitive type in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("teams").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `teams` to be an array in the JSON string but got `%s`", jsonObj.get("teams").toString()));
      }

      JsonArray jsonArrayteams = jsonObj.getAsJsonArray("teams");
      // validate the required field `teams` (array)
      for (int i = 0; i < jsonArrayteams.size(); i++) {
        BaseTeam.validateJsonElement(jsonArrayteams.get(i));
      };
      // validate the required field `videogame`
      CurrentVideogame.validateJsonElement(jsonObj.get("videogame"));
      // validate the required field `videogame`
      CurrentVideogame.validateJsonElement(jsonObj.get("videogame"));
      // validate the required field `winner_id`
      OpponentID1.validateJsonElement(jsonObj.get("winner_id"));
      // validate the required field `winner_type`
      Object.validateJsonElement(jsonObj.get("winner_type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Tournament.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Tournament' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Tournament> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Tournament.class));

       return (TypeAdapter<T>) new TypeAdapter<Tournament>() {
           @Override
           public void write(JsonWriter out, Tournament value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Tournament read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Tournament given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Tournament
   * @throws IOException if the JSON string is invalid with respect to Tournament
   */
  public static Tournament fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Tournament.class);
  }

  /**
   * Convert an instance of Tournament to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

