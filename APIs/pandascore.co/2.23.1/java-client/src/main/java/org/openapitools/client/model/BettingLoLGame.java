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
import java.util.Arrays;
import org.openapitools.client.model.BettingGameTeams1;
import org.openapitools.client.model.GameStatus;
import org.openapitools.client.model.GameWinner;

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
 * BettingLoLGame
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BettingLoLGame {
  public static final String SERIALIZED_NAME_BEGIN_AT = "begin_at";
  @SerializedName(SERIALIZED_NAME_BEGIN_AT)
  private Object beginAt;

  public static final String SERIALIZED_NAME_COMPLETE = "complete";
  @SerializedName(SERIALIZED_NAME_COMPLETE)
  private Boolean complete;

  public static final String SERIALIZED_NAME_DETAILED_STATS = "detailed_stats";
  @SerializedName(SERIALIZED_NAME_DETAILED_STATS)
  private Boolean detailedStats;

  public static final String SERIALIZED_NAME_END_AT = "end_at";
  @SerializedName(SERIALIZED_NAME_END_AT)
  private Object endAt;

  public static final String SERIALIZED_NAME_FINISHED = "finished";
  @SerializedName(SERIALIZED_NAME_FINISHED)
  private Boolean finished;

  public static final String SERIALIZED_NAME_FORFEIT = "forfeit";
  @SerializedName(SERIALIZED_NAME_FORFEIT)
  private Boolean forfeit;

  public static final String SERIALIZED_NAME_GAME_TEAMS = "game_teams";
  @SerializedName(SERIALIZED_NAME_GAME_TEAMS)
  private BettingGameTeams1 gameTeams;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LENGTH = "length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private Object length;

  public static final String SERIALIZED_NAME_MATCH_ID = "match_id";
  @SerializedName(SERIALIZED_NAME_MATCH_ID)
  private Integer matchId;

  public static final String SERIALIZED_NAME_POSITION = "position";
  @SerializedName(SERIALIZED_NAME_POSITION)
  private Integer position;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private GameStatus status;

  public static final String SERIALIZED_NAME_VIDEO_URL = "video_url";
  @SerializedName(SERIALIZED_NAME_VIDEO_URL)
  private Object videoUrl;

  public static final String SERIALIZED_NAME_WINNER = "winner";
  @SerializedName(SERIALIZED_NAME_WINNER)
  private GameWinner winner;

  public static final String SERIALIZED_NAME_WINNER_TYPE = "winner_type";
  @SerializedName(SERIALIZED_NAME_WINNER_TYPE)
  private Object winnerType;

  public BettingLoLGame() {
  }

  public BettingLoLGame beginAt(Object beginAt) {
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


  public BettingLoLGame complete(Boolean complete) {
    this.complete = complete;
    return this;
  }

  /**
   * Whether game data are complete and won&#39;t change
   * @return complete
   */
  @javax.annotation.Nonnull
  public Boolean getComplete() {
    return complete;
  }

  public void setComplete(Boolean complete) {
    this.complete = complete;
  }


  public BettingLoLGame detailedStats(Boolean detailedStats) {
    this.detailedStats = detailedStats;
    return this;
  }

  /**
   * Whether the game offers full stats
   * @return detailedStats
   */
  @javax.annotation.Nonnull
  public Boolean getDetailedStats() {
    return detailedStats;
  }

  public void setDetailedStats(Boolean detailedStats) {
    this.detailedStats = detailedStats;
  }


  public BettingLoLGame endAt(Object endAt) {
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


  public BettingLoLGame finished(Boolean finished) {
    this.finished = finished;
    return this;
  }

  /**
   * Whether game is finished
   * @return finished
   */
  @javax.annotation.Nonnull
  public Boolean getFinished() {
    return finished;
  }

  public void setFinished(Boolean finished) {
    this.finished = finished;
  }


  public BettingLoLGame forfeit(Boolean forfeit) {
    this.forfeit = forfeit;
    return this;
  }

  /**
   * Whether game is forfeit
   * @return forfeit
   */
  @javax.annotation.Nonnull
  public Boolean getForfeit() {
    return forfeit;
  }

  public void setForfeit(Boolean forfeit) {
    this.forfeit = forfeit;
  }


  public BettingLoLGame gameTeams(BettingGameTeams1 gameTeams) {
    this.gameTeams = gameTeams;
    return this;
  }

  /**
   * Get gameTeams
   * @return gameTeams
   */
  @javax.annotation.Nonnull
  public BettingGameTeams1 getGameTeams() {
    return gameTeams;
  }

  public void setGameTeams(BettingGameTeams1 gameTeams) {
    this.gameTeams = gameTeams;
  }


  public BettingLoLGame id(Integer id) {
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


  public BettingLoLGame length(Object length) {
    this.length = length;
    return this;
  }

  /**
   * Get length
   * @return length
   */
  @javax.annotation.Nonnull
  public Object getLength() {
    return length;
  }

  public void setLength(Object length) {
    this.length = length;
  }


  public BettingLoLGame matchId(Integer matchId) {
    this.matchId = matchId;
    return this;
  }

  /**
   * Get matchId
   * minimum: 1
   * @return matchId
   */
  @javax.annotation.Nonnull
  public Integer getMatchId() {
    return matchId;
  }

  public void setMatchId(Integer matchId) {
    this.matchId = matchId;
  }


  public BettingLoLGame position(Integer position) {
    this.position = position;
    return this;
  }

  /**
   * Get position
   * minimum: 1
   * @return position
   */
  @javax.annotation.Nonnull
  public Integer getPosition() {
    return position;
  }

  public void setPosition(Integer position) {
    this.position = position;
  }


  public BettingLoLGame status(GameStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public GameStatus getStatus() {
    return status;
  }

  public void setStatus(GameStatus status) {
    this.status = status;
  }


  public BettingLoLGame videoUrl(Object videoUrl) {
    this.videoUrl = videoUrl;
    return this;
  }

  /**
   * Get videoUrl
   * @return videoUrl
   */
  @javax.annotation.Nonnull
  public Object getVideoUrl() {
    return videoUrl;
  }

  public void setVideoUrl(Object videoUrl) {
    this.videoUrl = videoUrl;
  }


  public BettingLoLGame winner(GameWinner winner) {
    this.winner = winner;
    return this;
  }

  /**
   * Get winner
   * @return winner
   */
  @javax.annotation.Nonnull
  public GameWinner getWinner() {
    return winner;
  }

  public void setWinner(GameWinner winner) {
    this.winner = winner;
  }


  public BettingLoLGame winnerType(Object winnerType) {
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
    BettingLoLGame bettingLoLGame = (BettingLoLGame) o;
    return Objects.equals(this.beginAt, bettingLoLGame.beginAt) &&
        Objects.equals(this.complete, bettingLoLGame.complete) &&
        Objects.equals(this.detailedStats, bettingLoLGame.detailedStats) &&
        Objects.equals(this.endAt, bettingLoLGame.endAt) &&
        Objects.equals(this.finished, bettingLoLGame.finished) &&
        Objects.equals(this.forfeit, bettingLoLGame.forfeit) &&
        Objects.equals(this.gameTeams, bettingLoLGame.gameTeams) &&
        Objects.equals(this.id, bettingLoLGame.id) &&
        Objects.equals(this.length, bettingLoLGame.length) &&
        Objects.equals(this.matchId, bettingLoLGame.matchId) &&
        Objects.equals(this.position, bettingLoLGame.position) &&
        Objects.equals(this.status, bettingLoLGame.status) &&
        Objects.equals(this.videoUrl, bettingLoLGame.videoUrl) &&
        Objects.equals(this.winner, bettingLoLGame.winner) &&
        Objects.equals(this.winnerType, bettingLoLGame.winnerType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, complete, detailedStats, endAt, finished, forfeit, gameTeams, id, length, matchId, position, status, videoUrl, winner, winnerType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BettingLoLGame {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    complete: ").append(toIndentedString(complete)).append("\n");
    sb.append("    detailedStats: ").append(toIndentedString(detailedStats)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    finished: ").append(toIndentedString(finished)).append("\n");
    sb.append("    forfeit: ").append(toIndentedString(forfeit)).append("\n");
    sb.append("    gameTeams: ").append(toIndentedString(gameTeams)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    matchId: ").append(toIndentedString(matchId)).append("\n");
    sb.append("    position: ").append(toIndentedString(position)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    videoUrl: ").append(toIndentedString(videoUrl)).append("\n");
    sb.append("    winner: ").append(toIndentedString(winner)).append("\n");
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
    openapiFields.add("complete");
    openapiFields.add("detailed_stats");
    openapiFields.add("end_at");
    openapiFields.add("finished");
    openapiFields.add("forfeit");
    openapiFields.add("game_teams");
    openapiFields.add("id");
    openapiFields.add("length");
    openapiFields.add("match_id");
    openapiFields.add("position");
    openapiFields.add("status");
    openapiFields.add("video_url");
    openapiFields.add("winner");
    openapiFields.add("winner_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("begin_at");
    openapiRequiredFields.add("complete");
    openapiRequiredFields.add("detailed_stats");
    openapiRequiredFields.add("end_at");
    openapiRequiredFields.add("finished");
    openapiRequiredFields.add("forfeit");
    openapiRequiredFields.add("game_teams");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("length");
    openapiRequiredFields.add("match_id");
    openapiRequiredFields.add("position");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("video_url");
    openapiRequiredFields.add("winner");
    openapiRequiredFields.add("winner_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BettingLoLGame
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BettingLoLGame.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BettingLoLGame is not found in the empty JSON string", BettingLoLGame.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BettingLoLGame.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BettingLoLGame` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BettingLoLGame.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `begin_at`
      Object.validateJsonElement(jsonObj.get("begin_at"));
      // validate the required field `end_at`
      Object.validateJsonElement(jsonObj.get("end_at"));
      // validate the required field `game_teams`
      BettingGameTeams1.validateJsonElement(jsonObj.get("game_teams"));
      // validate the required field `length`
      Object.validateJsonElement(jsonObj.get("length"));
      // validate the required field `status`
      GameStatus.validateJsonElement(jsonObj.get("status"));
      // validate the required field `video_url`
      Object.validateJsonElement(jsonObj.get("video_url"));
      // validate the required field `winner`
      GameWinner.validateJsonElement(jsonObj.get("winner"));
      // validate the required field `winner_type`
      Object.validateJsonElement(jsonObj.get("winner_type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BettingLoLGame.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BettingLoLGame' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BettingLoLGame> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BettingLoLGame.class));

       return (TypeAdapter<T>) new TypeAdapter<BettingLoLGame>() {
           @Override
           public void write(JsonWriter out, BettingLoLGame value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BettingLoLGame read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BettingLoLGame given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BettingLoLGame
   * @throws IOException if the JSON string is invalid with respect to BettingLoLGame
   */
  public static BettingLoLGame fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BettingLoLGame.class);
  }

  /**
   * Convert an instance of BettingLoLGame to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

