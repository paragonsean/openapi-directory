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
import org.openapitools.client.model.VideogameID;

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
 * FilterOverTeams
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FilterOverTeams {
  public static final String SERIALIZED_NAME_ACRONYM = "acronym";
  @SerializedName(SERIALIZED_NAME_ACRONYM)
  private List<String> acronym = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private List<Integer> id = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private List<String> location = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODIFIED_AT = "modified_at";
  @SerializedName(SERIALIZED_NAME_MODIFIED_AT)
  private List<OffsetDateTime> modifiedAt = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private List<String> name = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private List<String> slug = new ArrayList<>();

  public static final String SERIALIZED_NAME_VIDEOGAME_ID = "videogame_id";
  @SerializedName(SERIALIZED_NAME_VIDEOGAME_ID)
  private List<VideogameID> videogameId = new ArrayList<>();

  public FilterOverTeams() {
  }

  public FilterOverTeams acronym(List<String> acronym) {
    this.acronym = acronym;
    return this;
  }

  public FilterOverTeams addAcronymItem(String acronymItem) {
    if (this.acronym == null) {
      this.acronym = new ArrayList<>();
    }
    this.acronym.add(acronymItem);
    return this;
  }

  /**
   * Get acronym
   * @return acronym
   */
  @javax.annotation.Nullable
  public List<String> getAcronym() {
    return acronym;
  }

  public void setAcronym(List<String> acronym) {
    this.acronym = acronym;
  }


  public FilterOverTeams id(List<Integer> id) {
    this.id = id;
    return this;
  }

  public FilterOverTeams addIdItem(Integer idItem) {
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


  public FilterOverTeams location(List<String> location) {
    this.location = location;
    return this;
  }

  public FilterOverTeams addLocationItem(String locationItem) {
    if (this.location == null) {
      this.location = new ArrayList<>();
    }
    this.location.add(locationItem);
    return this;
  }

  /**
   * Get location
   * @return location
   */
  @javax.annotation.Nullable
  public List<String> getLocation() {
    return location;
  }

  public void setLocation(List<String> location) {
    this.location = location;
  }


  public FilterOverTeams modifiedAt(List<OffsetDateTime> modifiedAt) {
    this.modifiedAt = modifiedAt;
    return this;
  }

  public FilterOverTeams addModifiedAtItem(OffsetDateTime modifiedAtItem) {
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


  public FilterOverTeams name(List<String> name) {
    this.name = name;
    return this;
  }

  public FilterOverTeams addNameItem(String nameItem) {
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


  public FilterOverTeams slug(List<String> slug) {
    this.slug = slug;
    return this;
  }

  public FilterOverTeams addSlugItem(String slugItem) {
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


  public FilterOverTeams videogameId(List<VideogameID> videogameId) {
    this.videogameId = videogameId;
    return this;
  }

  public FilterOverTeams addVideogameIdItem(VideogameID videogameIdItem) {
    if (this.videogameId == null) {
      this.videogameId = new ArrayList<>();
    }
    this.videogameId.add(videogameIdItem);
    return this;
  }

  /**
   * Get videogameId
   * @return videogameId
   */
  @javax.annotation.Nullable
  public List<VideogameID> getVideogameId() {
    return videogameId;
  }

  public void setVideogameId(List<VideogameID> videogameId) {
    this.videogameId = videogameId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FilterOverTeams filterOverTeams = (FilterOverTeams) o;
    return Objects.equals(this.acronym, filterOverTeams.acronym) &&
        Objects.equals(this.id, filterOverTeams.id) &&
        Objects.equals(this.location, filterOverTeams.location) &&
        Objects.equals(this.modifiedAt, filterOverTeams.modifiedAt) &&
        Objects.equals(this.name, filterOverTeams.name) &&
        Objects.equals(this.slug, filterOverTeams.slug) &&
        Objects.equals(this.videogameId, filterOverTeams.videogameId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(acronym, id, location, modifiedAt, name, slug, videogameId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FilterOverTeams {\n");
    sb.append("    acronym: ").append(toIndentedString(acronym)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    modifiedAt: ").append(toIndentedString(modifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    videogameId: ").append(toIndentedString(videogameId)).append("\n");
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
    openapiFields.add("acronym");
    openapiFields.add("id");
    openapiFields.add("location");
    openapiFields.add("modified_at");
    openapiFields.add("name");
    openapiFields.add("slug");
    openapiFields.add("videogame_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FilterOverTeams
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FilterOverTeams.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FilterOverTeams is not found in the empty JSON string", FilterOverTeams.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FilterOverTeams.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FilterOverTeams` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("acronym") != null && !jsonObj.get("acronym").isJsonNull() && !jsonObj.get("acronym").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `acronym` to be an array in the JSON string but got `%s`", jsonObj.get("acronym").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull() && !jsonObj.get("id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be an array in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("location") != null && !jsonObj.get("location").isJsonNull() && !jsonObj.get("location").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `location` to be an array in the JSON string but got `%s`", jsonObj.get("location").toString()));
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
      if (jsonObj.get("slug") != null && !jsonObj.get("slug").isJsonNull() && !jsonObj.get("slug").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be an array in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("videogame_id") != null && !jsonObj.get("videogame_id").isJsonNull() && !jsonObj.get("videogame_id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `videogame_id` to be an array in the JSON string but got `%s`", jsonObj.get("videogame_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FilterOverTeams.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FilterOverTeams' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FilterOverTeams> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FilterOverTeams.class));

       return (TypeAdapter<T>) new TypeAdapter<FilterOverTeams>() {
           @Override
           public void write(JsonWriter out, FilterOverTeams value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FilterOverTeams read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FilterOverTeams given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FilterOverTeams
   * @throws IOException if the JSON string is invalid with respect to FilterOverTeams
   */
  public static FilterOverTeams fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FilterOverTeams.class);
  }

  /**
   * Convert an instance of FilterOverTeams to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

