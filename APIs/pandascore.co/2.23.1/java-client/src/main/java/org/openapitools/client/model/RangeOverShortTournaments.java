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
import org.openapitools.client.model.OpponentID;
import org.openapitools.client.model.OpponentType;

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
 * RangeOverShortTournaments
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RangeOverShortTournaments {
  public static final String SERIALIZED_NAME_BEGIN_AT = "begin_at";
  @SerializedName(SERIALIZED_NAME_BEGIN_AT)
  private List<OffsetDateTime> beginAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_END_AT = "end_at";
  @SerializedName(SERIALIZED_NAME_END_AT)
  private List<OffsetDateTime> endAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private List<Integer> id = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODIFIED_AT = "modified_at";
  @SerializedName(SERIALIZED_NAME_MODIFIED_AT)
  private List<OffsetDateTime> modifiedAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private List<String> name = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRIZEPOOL = "prizepool";
  @SerializedName(SERIALIZED_NAME_PRIZEPOOL)
  private List<String> prizepool = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERIE_ID = "serie_id";
  @SerializedName(SERIALIZED_NAME_SERIE_ID)
  private List<Integer> serieId = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private List<String> slug = new ArrayList<>();

  public static final String SERIALIZED_NAME_WINNER_ID = "winner_id";
  @SerializedName(SERIALIZED_NAME_WINNER_ID)
  private List<OpponentID> winnerId = new ArrayList<>();

  public static final String SERIALIZED_NAME_WINNER_TYPE = "winner_type";
  @SerializedName(SERIALIZED_NAME_WINNER_TYPE)
  private List<OpponentType> winnerType = new ArrayList<>();

  public RangeOverShortTournaments() {
  }

  public RangeOverShortTournaments beginAt(List<OffsetDateTime> beginAt) {
    this.beginAt = beginAt;
    return this;
  }

  public RangeOverShortTournaments addBeginAtItem(OffsetDateTime beginAtItem) {
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


  public RangeOverShortTournaments endAt(List<OffsetDateTime> endAt) {
    this.endAt = endAt;
    return this;
  }

  public RangeOverShortTournaments addEndAtItem(OffsetDateTime endAtItem) {
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


  public RangeOverShortTournaments id(List<Integer> id) {
    this.id = id;
    return this;
  }

  public RangeOverShortTournaments addIdItem(Integer idItem) {
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


  public RangeOverShortTournaments modifiedAt(List<OffsetDateTime> modifiedAt) {
    this.modifiedAt = modifiedAt;
    return this;
  }

  public RangeOverShortTournaments addModifiedAtItem(OffsetDateTime modifiedAtItem) {
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


  public RangeOverShortTournaments name(List<String> name) {
    this.name = name;
    return this;
  }

  public RangeOverShortTournaments addNameItem(String nameItem) {
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


  public RangeOverShortTournaments prizepool(List<String> prizepool) {
    this.prizepool = prizepool;
    return this;
  }

  public RangeOverShortTournaments addPrizepoolItem(String prizepoolItem) {
    if (this.prizepool == null) {
      this.prizepool = new ArrayList<>();
    }
    this.prizepool.add(prizepoolItem);
    return this;
  }

  /**
   * Get prizepool
   * @return prizepool
   */
  @javax.annotation.Nullable
  public List<String> getPrizepool() {
    return prizepool;
  }

  public void setPrizepool(List<String> prizepool) {
    this.prizepool = prizepool;
  }


  public RangeOverShortTournaments serieId(List<Integer> serieId) {
    this.serieId = serieId;
    return this;
  }

  public RangeOverShortTournaments addSerieIdItem(Integer serieIdItem) {
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


  public RangeOverShortTournaments slug(List<String> slug) {
    this.slug = slug;
    return this;
  }

  public RangeOverShortTournaments addSlugItem(String slugItem) {
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


  public RangeOverShortTournaments winnerId(List<OpponentID> winnerId) {
    this.winnerId = winnerId;
    return this;
  }

  public RangeOverShortTournaments addWinnerIdItem(OpponentID winnerIdItem) {
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


  public RangeOverShortTournaments winnerType(List<OpponentType> winnerType) {
    this.winnerType = winnerType;
    return this;
  }

  public RangeOverShortTournaments addWinnerTypeItem(OpponentType winnerTypeItem) {
    if (this.winnerType == null) {
      this.winnerType = new ArrayList<>();
    }
    this.winnerType.add(winnerTypeItem);
    return this;
  }

  /**
   * Get winnerType
   * @return winnerType
   */
  @javax.annotation.Nullable
  public List<OpponentType> getWinnerType() {
    return winnerType;
  }

  public void setWinnerType(List<OpponentType> winnerType) {
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
    RangeOverShortTournaments rangeOverShortTournaments = (RangeOverShortTournaments) o;
    return Objects.equals(this.beginAt, rangeOverShortTournaments.beginAt) &&
        Objects.equals(this.endAt, rangeOverShortTournaments.endAt) &&
        Objects.equals(this.id, rangeOverShortTournaments.id) &&
        Objects.equals(this.modifiedAt, rangeOverShortTournaments.modifiedAt) &&
        Objects.equals(this.name, rangeOverShortTournaments.name) &&
        Objects.equals(this.prizepool, rangeOverShortTournaments.prizepool) &&
        Objects.equals(this.serieId, rangeOverShortTournaments.serieId) &&
        Objects.equals(this.slug, rangeOverShortTournaments.slug) &&
        Objects.equals(this.winnerId, rangeOverShortTournaments.winnerId) &&
        Objects.equals(this.winnerType, rangeOverShortTournaments.winnerType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginAt, endAt, id, modifiedAt, name, prizepool, serieId, slug, winnerId, winnerType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RangeOverShortTournaments {\n");
    sb.append("    beginAt: ").append(toIndentedString(beginAt)).append("\n");
    sb.append("    endAt: ").append(toIndentedString(endAt)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    modifiedAt: ").append(toIndentedString(modifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    prizepool: ").append(toIndentedString(prizepool)).append("\n");
    sb.append("    serieId: ").append(toIndentedString(serieId)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("modified_at");
    openapiFields.add("name");
    openapiFields.add("prizepool");
    openapiFields.add("serie_id");
    openapiFields.add("slug");
    openapiFields.add("winner_id");
    openapiFields.add("winner_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RangeOverShortTournaments
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RangeOverShortTournaments.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RangeOverShortTournaments is not found in the empty JSON string", RangeOverShortTournaments.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RangeOverShortTournaments.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RangeOverShortTournaments` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      if (jsonObj.get("modified_at") != null && !jsonObj.get("modified_at").isJsonNull() && !jsonObj.get("modified_at").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified_at` to be an array in the JSON string but got `%s`", jsonObj.get("modified_at").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull() && !jsonObj.get("name").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be an array in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("prizepool") != null && !jsonObj.get("prizepool").isJsonNull() && !jsonObj.get("prizepool").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `prizepool` to be an array in the JSON string but got `%s`", jsonObj.get("prizepool").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("serie_id") != null && !jsonObj.get("serie_id").isJsonNull() && !jsonObj.get("serie_id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `serie_id` to be an array in the JSON string but got `%s`", jsonObj.get("serie_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("slug") != null && !jsonObj.get("slug").isJsonNull() && !jsonObj.get("slug").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be an array in the JSON string but got `%s`", jsonObj.get("slug").toString()));
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
      // ensure the optional json data is an array if present
      if (jsonObj.get("winner_type") != null && !jsonObj.get("winner_type").isJsonNull() && !jsonObj.get("winner_type").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `winner_type` to be an array in the JSON string but got `%s`", jsonObj.get("winner_type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RangeOverShortTournaments.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RangeOverShortTournaments' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RangeOverShortTournaments> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RangeOverShortTournaments.class));

       return (TypeAdapter<T>) new TypeAdapter<RangeOverShortTournaments>() {
           @Override
           public void write(JsonWriter out, RangeOverShortTournaments value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RangeOverShortTournaments read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RangeOverShortTournaments given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RangeOverShortTournaments
   * @throws IOException if the JSON string is invalid with respect to RangeOverShortTournaments
   */
  public static RangeOverShortTournaments fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RangeOverShortTournaments.class);
  }

  /**
   * Convert an instance of RangeOverShortTournaments to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

