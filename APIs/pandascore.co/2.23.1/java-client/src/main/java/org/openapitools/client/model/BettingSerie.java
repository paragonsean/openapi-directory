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
import java.util.Arrays;
import org.openapitools.client.model.CurrentVideogame;
import org.openapitools.client.model.OpponentID1;

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
 * BettingSerie
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BettingSerie {
  public static final String SERIALIZED_NAME_BEGIN_AT = "begin_at";
  @SerializedName(SERIALIZED_NAME_BEGIN_AT)
  private Object beginAt;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private Object description;

  public static final String SERIALIZED_NAME_END_AT = "end_at";
  @SerializedName(SERIALIZED_NAME_END_AT)
  private Object endAt;

  public static final String SERIALIZED_NAME_FULL_NAME = "full_name";
  @SerializedName(SERIALIZED_NAME_FULL_NAME)
  private String fullName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LEAGUE_ID = "league_id";
  @SerializedName(SERIALIZED_NAME_LEAGUE_ID)
  private Integer leagueId;

  public static final String SERIALIZED_NAME_LEAGUE_IMAGE_URL = "league_image_url";
  @SerializedName(SERIALIZED_NAME_LEAGUE_IMAGE_URL)
  private Object leagueImageUrl;

  public static final String SERIALIZED_NAME_LEAGUE_NAME = "league_name";
  @SerializedName(SERIALIZED_NAME_LEAGUE_NAME)
  private String leagueName;

  public static final String SERIALIZED_NAME_MODIFIED_AT = "modified_at";
  @SerializedName(SERIALIZED_NAME_MODIFIED_AT)
  private OffsetDateTime modifiedAt;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private Object name;

  public static final String SERIALIZED_NAME_SEASON = "season";
  @SerializedName(SERIALIZED_NAME_SEASON)
  private Object season;

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private String slug;

  public static final String SERIALIZED_NAME_TIER = "tier";
  @SerializedName(SERIALIZED_NAME_TIER)
  private Object tier;

  public static final String SERIALIZED_NAME_VIDEOGAME = "videogame";
  @SerializedName(SERIALIZED_NAME_VIDEOGAME)
  private CurrentVideogame videogame;

  public static final String SERIALIZED_NAME_WINNER_ID = "winner_id";
  @SerializedName(SERIALIZED_NAME_WINNER_ID)
  private OpponentID1 winnerId;

  public static final String SERIALIZED_NAME_WINNER_TYPE = "winner_type";
  @SerializedName(SERIALIZED_NAME_WINNER_TYPE)
  private Object winnerType;

  public static final String SERIALIZED_NAME_YEAR = "year";
  @SerializedName(SERIALIZED_NAME_YEAR)
  private Integer year;

  public BettingSerie() {
  }

  public BettingSerie beginAt(Object beginAt) {
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


  public BettingSerie description(Object description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nonnull
  public Object getDescription() {
    return description;
  }

  public void setDescription(Object description) {
    this.description = description;
  }


  public BettingSerie endAt(Object endAt) {
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


  public BettingSerie fullName(String fullName) {
    this.fullName = fullName;
    return this;
  }

  /**
   * Get fullName
   * @return fullName
   */
  @javax.annotation.Nonnull
  public String getFullName() {
    return fullName;
  }

  public void setFullName(String fullName) {
    this.fullName = fullName;
  }


  public BettingSerie id(Integer id) {
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


  public BettingSerie leagueId(Integer leagueId) {
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


  public BettingSerie leagueImageUrl(Object leagueImageUrl) {
    this.leagueImageUrl = leagueImageUrl;
    return this;
  }

  /**
   * Get leagueImageUrl
   * @return leagueImageUrl
   */
  @javax.annotation.Nonnull
  public Object getLeagueImageUrl() {
    return leagueImageUrl;
  }

  public void setLeagueImageUrl(Object leagueImageUrl) {
    this.leagueImageUrl = leagueImageUrl;
  }


  public BettingSerie leagueName(String leagueName) {
    this.leagueName = leagueName;
    return this;
  }

  /**
   * Get leagueName
   * @return leagueName
   */
  @javax.annotation.Nonnull
  public String getLeagueName() {
    return leagueName;
  }

  public void setLeagueName(String leagueName) {
    this.leagueName = leagueName;
  }


  public BettingSerie modifiedAt(OffsetDateTime modifiedAt) {
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


  public BettingSerie name(Object name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public Object getName() {
    return name;
  }

  public void setName(Object name) {
    this.name = name;
  }


  public BettingSerie season(Object season) {
    this.season = season;
    return this;
  }

  /**
   * Get season
   * @return season
   */
  @javax.annotation.Nonnull
  public Object getSeason() {
    return season;
  }

  public void setSeason(Object season) {
    this.season = season;
  }


  public BettingSerie slug(String slug) {
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


  public BettingSerie tier(Object tier) {
    this.tier = tier;
    return this;
  }

  /**
   * Get tier
   * @return tier
   */
  @javax.annotation.Nonnull
  public Object getTier() {
    return tier;
  }

  public void setTier(Object tier) {
    this.tier = tier;
  }


  public BettingSerie videogame(CurrentVideogame videogame) {
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


  public BettingSerie winnerId(OpponentID1 winnerId) {
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


  public BettingSerie winnerType(Object winnerType) {
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


  public BettingSerie year(Integer year) {
    this.year = year;
    return this;
  }

  /**
   * Get year
   * minimum: 2012
   * @return year
   */
  @javax.annotation.Nonnull
  public Integer getYear() {
    return year;
  }

  public void setYear(Integer year) {
    this.year = year;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BettingSerie bettingSerie = (BettingSerie) o;
    return Objects.equals(this.beginAt, bettingSerie.beginAt) &&
        Objects.equals(this.description, bettingSerie.description) &&
        Objects.equals(this.endAt, bettingSerie.endAt) &&
        Objects.equals(this.fullName, bettingSerie.fullName) &&
        Objects.equals(this.id, bettingSerie.id) &&
        Objects.equals(this.leagueId, bettingSerie.leagueId) &&
        Objects.equals(this.leagueImageUrl, bettingSerie.leagueImageUrl) &&
        Objects.equals(this.leagueName, bettingSerie.leagueName) &&
        Objects.equals(this.modifiedAt, bettingSerie.modifiedAt) &&
        Objects.equals(this.name, bettingSerie.name) &&
        Objects.equals(this.season, bettingSerie.season) &&
        Objects.equals(this.slug, bettingSerie.slug) &&
        Objects.equals(this.tier, bettingSerie.tier) &&
        Objects.equals(this.videogame, bettingSerie.videogame) &&
        Objects.equals(this.winnerId, bettingSerie.winnerId) &&
        Objects.equals(this.winnerType, bettingSerie.winnerType) &&
        Objects.equals(this.year, bettingSerie.year);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, description, endAt, fullName, id, leagueId, leagueImageUrl, leagueName, modifiedAt, name, season, slug, tier, videogame, winnerId, winnerType, year);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BettingSerie {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    fullName: ").append(toIndentedString(fullName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    leagueId: ").append(toIndentedString(leagueId)).append("\n");
    sb.append("    leagueImageUrl: ").append(toIndentedString(leagueImageUrl)).append("\n");
    sb.append("    leagueName: ").append(toIndentedString(leagueName)).append("\n");
    sb.append("    modifiedAt: ").append(toIndentedString(modifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    season: ").append(toIndentedString(season)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    tier: ").append(toIndentedString(tier)).append("\n");
    sb.append("    videogame: ").append(toIndentedString(videogame)).append("\n");
    sb.append("    winnerId: ").append(toIndentedString(winnerId)).append("\n");
    sb.append("    winnerType: ").append(toIndentedString(winnerType)).append("\n");
    sb.append("    year: ").append(toIndentedString(year)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("end_at");
    openapiFields.add("full_name");
    openapiFields.add("id");
    openapiFields.add("league_id");
    openapiFields.add("league_image_url");
    openapiFields.add("league_name");
    openapiFields.add("modified_at");
    openapiFields.add("name");
    openapiFields.add("season");
    openapiFields.add("slug");
    openapiFields.add("tier");
    openapiFields.add("videogame");
    openapiFields.add("winner_id");
    openapiFields.add("winner_type");
    openapiFields.add("year");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("begin_at");
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("end_at");
    openapiRequiredFields.add("full_name");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("league_id");
    openapiRequiredFields.add("league_image_url");
    openapiRequiredFields.add("league_name");
    openapiRequiredFields.add("modified_at");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("season");
    openapiRequiredFields.add("slug");
    openapiRequiredFields.add("tier");
    openapiRequiredFields.add("videogame");
    openapiRequiredFields.add("winner_id");
    openapiRequiredFields.add("winner_type");
    openapiRequiredFields.add("year");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BettingSerie
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BettingSerie.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BettingSerie is not found in the empty JSON string", BettingSerie.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BettingSerie.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BettingSerie` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BettingSerie.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `begin_at`
      Object.validateJsonElement(jsonObj.get("begin_at"));
      // validate the required field `description`
      Object.validateJsonElement(jsonObj.get("description"));
      // validate the required field `end_at`
      Object.validateJsonElement(jsonObj.get("end_at"));
      if (!jsonObj.get("full_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `full_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("full_name").toString()));
      }
      // validate the required field `league_image_url`
      Object.validateJsonElement(jsonObj.get("league_image_url"));
      if (!jsonObj.get("league_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `league_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("league_name").toString()));
      }
      // validate the required field `name`
      Object.validateJsonElement(jsonObj.get("name"));
      // validate the required field `season`
      Object.validateJsonElement(jsonObj.get("season"));
      if (!jsonObj.get("slug").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be a primitive type in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
      // validate the required field `tier`
      Object.validateJsonElement(jsonObj.get("tier"));
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
       if (!BettingSerie.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BettingSerie' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BettingSerie> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BettingSerie.class));

       return (TypeAdapter<T>) new TypeAdapter<BettingSerie>() {
           @Override
           public void write(JsonWriter out, BettingSerie value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BettingSerie read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BettingSerie given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BettingSerie
   * @throws IOException if the JSON string is invalid with respect to BettingSerie
   */
  public static BettingSerie fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BettingSerie.class);
  }

  /**
   * Convert an instance of BettingSerie to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

