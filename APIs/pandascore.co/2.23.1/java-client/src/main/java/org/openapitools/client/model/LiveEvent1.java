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
import org.openapitools.client.model.VideogameSlug;

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
 * LiveEvent1
 * @deprecated
 */
@Deprecated
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LiveEvent1 {
  public static final String SERIALIZED_NAME_BEGIN_AT = "begin_at";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_BEGIN_AT)
  private Object beginAt;

  public static final String SERIALIZED_NAME_END_AT = "end_at";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_END_AT)
  private Object endAt;

  public static final String SERIALIZED_NAME_GAME = "game";
  @SerializedName(SERIALIZED_NAME_GAME)
  private VideogameSlug game;

  public static final String SERIALIZED_NAME_ID = "id";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "is_active";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_STREAM_URL = "stream_url";
  @SerializedName(SERIALIZED_NAME_STREAM_URL)
  private Object streamUrl;

  public static final String SERIALIZED_NAME_TOURNAMENT_ID = "tournament_id";
  @SerializedName(SERIALIZED_NAME_TOURNAMENT_ID)
  private Integer tournamentId;

  public LiveEvent1() {
  }

  @Deprecated
  public LiveEvent1 beginAt(Object beginAt) {
    this.beginAt = beginAt;
    return this;
  }

  /**
   * Get beginAt
   * @return beginAt
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Object getBeginAt() {
    return beginAt;
  }

  @Deprecated
  public void setBeginAt(Object beginAt) {
    this.beginAt = beginAt;
  }


  @Deprecated
  public LiveEvent1 endAt(Object endAt) {
    this.endAt = endAt;
    return this;
  }

  /**
   * Get endAt
   * @return endAt
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Object getEndAt() {
    return endAt;
  }

  @Deprecated
  public void setEndAt(Object endAt) {
    this.endAt = endAt;
  }


  public LiveEvent1 game(VideogameSlug game) {
    this.game = game;
    return this;
  }

  /**
   * Get game
   * @return game
   */
  @javax.annotation.Nonnull
  public VideogameSlug getGame() {
    return game;
  }

  public void setGame(VideogameSlug game) {
    this.game = game;
  }


  @Deprecated
  public LiveEvent1 id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * minimum: 1
   * @return id
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  @Deprecated
  public void setId(Integer id) {
    this.id = id;
  }


  public LiveEvent1 isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Whether event is active
   * @return isActive
   */
  @javax.annotation.Nonnull
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public LiveEvent1 streamUrl(Object streamUrl) {
    this.streamUrl = streamUrl;
    return this;
  }

  /**
   * Get streamUrl
   * @return streamUrl
   */
  @javax.annotation.Nonnull
  public Object getStreamUrl() {
    return streamUrl;
  }

  public void setStreamUrl(Object streamUrl) {
    this.streamUrl = streamUrl;
  }


  public LiveEvent1 tournamentId(Integer tournamentId) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LiveEvent1 liveEvent1 = (LiveEvent1) o;
    return Objects.equals(this.beginAt, liveEvent1.beginAt) &&
        Objects.equals(this.endAt, liveEvent1.endAt) &&
        Objects.equals(this.game, liveEvent1.game) &&
        Objects.equals(this.id, liveEvent1.id) &&
        Objects.equals(this.isActive, liveEvent1.isActive) &&
        Objects.equals(this.streamUrl, liveEvent1.streamUrl) &&
        Objects.equals(this.tournamentId, liveEvent1.tournamentId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, endAt, game, id, isActive, streamUrl, tournamentId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LiveEvent1 {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    game: ").append(toIndentedString(game)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    streamUrl: ").append(toIndentedString(streamUrl)).append("\n");
    sb.append("    tournamentId: ").append(toIndentedString(tournamentId)).append("\n");
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
    openapiFields.add("game");
    openapiFields.add("id");
    openapiFields.add("is_active");
    openapiFields.add("stream_url");
    openapiFields.add("tournament_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("begin_at");
    openapiRequiredFields.add("end_at");
    openapiRequiredFields.add("game");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("is_active");
    openapiRequiredFields.add("stream_url");
    openapiRequiredFields.add("tournament_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LiveEvent1
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LiveEvent1.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LiveEvent1 is not found in the empty JSON string", LiveEvent1.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LiveEvent1.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LiveEvent1` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : LiveEvent1.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `begin_at`
      Object.validateJsonElement(jsonObj.get("begin_at"));
      // validate the required field `end_at`
      Object.validateJsonElement(jsonObj.get("end_at"));
      // validate the required field `game`
      VideogameSlug.validateJsonElement(jsonObj.get("game"));
      // validate the required field `stream_url`
      Object.validateJsonElement(jsonObj.get("stream_url"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LiveEvent1.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LiveEvent1' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LiveEvent1> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LiveEvent1.class));

       return (TypeAdapter<T>) new TypeAdapter<LiveEvent1>() {
           @Override
           public void write(JsonWriter out, LiveEvent1 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LiveEvent1 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LiveEvent1 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LiveEvent1
   * @throws IOException if the JSON string is invalid with respect to LiveEvent1
   */
  public static LiveEvent1 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LiveEvent1.class);
  }

  /**
   * Convert an instance of LiveEvent1 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

