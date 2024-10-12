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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * RangeOverPlayers
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RangeOverPlayers {
  public static final String SERIALIZED_NAME_BIRTH_YEAR = "birth_year";
  @SerializedName(SERIALIZED_NAME_BIRTH_YEAR)
  private List<BigDecimal> birthYear = new ArrayList<>();

  public static final String SERIALIZED_NAME_BIRTHDAY = "birthday";
  @SerializedName(SERIALIZED_NAME_BIRTHDAY)
  private List<String> birthday = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private List<String> firstName = new ArrayList<>();

  public static final String SERIALIZED_NAME_HOMETOWN = "hometown";
  @SerializedName(SERIALIZED_NAME_HOMETOWN)
  private List<String> hometown = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private List<Integer> id = new ArrayList<>();

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private List<String> lastName = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private List<String> name = new ArrayList<>();

  public static final String SERIALIZED_NAME_NATIONALITY = "nationality";
  @SerializedName(SERIALIZED_NAME_NATIONALITY)
  private List<String> nationality = new ArrayList<>();

  public static final String SERIALIZED_NAME_ROLE = "role";
  @SerializedName(SERIALIZED_NAME_ROLE)
  private List<String> role = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private List<String> slug = new ArrayList<>();

  public RangeOverPlayers() {
  }

  public RangeOverPlayers birthYear(List<BigDecimal> birthYear) {
    this.birthYear = birthYear;
    return this;
  }

  public RangeOverPlayers addBirthYearItem(BigDecimal birthYearItem) {
    if (this.birthYear == null) {
      this.birthYear = new ArrayList<>();
    }
    this.birthYear.add(birthYearItem);
    return this;
  }

  /**
   * Get birthYear
   * @return birthYear
   */
  @javax.annotation.Nullable
  public List<BigDecimal> getBirthYear() {
    return birthYear;
  }

  public void setBirthYear(List<BigDecimal> birthYear) {
    this.birthYear = birthYear;
  }


  public RangeOverPlayers birthday(List<String> birthday) {
    this.birthday = birthday;
    return this;
  }

  public RangeOverPlayers addBirthdayItem(String birthdayItem) {
    if (this.birthday == null) {
      this.birthday = new ArrayList<>();
    }
    this.birthday.add(birthdayItem);
    return this;
  }

  /**
   * Get birthday
   * @return birthday
   */
  @javax.annotation.Nullable
  public List<String> getBirthday() {
    return birthday;
  }

  public void setBirthday(List<String> birthday) {
    this.birthday = birthday;
  }


  public RangeOverPlayers firstName(List<String> firstName) {
    this.firstName = firstName;
    return this;
  }

  public RangeOverPlayers addFirstNameItem(String firstNameItem) {
    if (this.firstName == null) {
      this.firstName = new ArrayList<>();
    }
    this.firstName.add(firstNameItem);
    return this;
  }

  /**
   * Get firstName
   * @return firstName
   */
  @javax.annotation.Nullable
  public List<String> getFirstName() {
    return firstName;
  }

  public void setFirstName(List<String> firstName) {
    this.firstName = firstName;
  }


  public RangeOverPlayers hometown(List<String> hometown) {
    this.hometown = hometown;
    return this;
  }

  public RangeOverPlayers addHometownItem(String hometownItem) {
    if (this.hometown == null) {
      this.hometown = new ArrayList<>();
    }
    this.hometown.add(hometownItem);
    return this;
  }

  /**
   * Get hometown
   * @return hometown
   */
  @javax.annotation.Nullable
  public List<String> getHometown() {
    return hometown;
  }

  public void setHometown(List<String> hometown) {
    this.hometown = hometown;
  }


  public RangeOverPlayers id(List<Integer> id) {
    this.id = id;
    return this;
  }

  public RangeOverPlayers addIdItem(Integer idItem) {
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


  public RangeOverPlayers lastName(List<String> lastName) {
    this.lastName = lastName;
    return this;
  }

  public RangeOverPlayers addLastNameItem(String lastNameItem) {
    if (this.lastName == null) {
      this.lastName = new ArrayList<>();
    }
    this.lastName.add(lastNameItem);
    return this;
  }

  /**
   * Get lastName
   * @return lastName
   */
  @javax.annotation.Nullable
  public List<String> getLastName() {
    return lastName;
  }

  public void setLastName(List<String> lastName) {
    this.lastName = lastName;
  }


  public RangeOverPlayers name(List<String> name) {
    this.name = name;
    return this;
  }

  public RangeOverPlayers addNameItem(String nameItem) {
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


  public RangeOverPlayers nationality(List<String> nationality) {
    this.nationality = nationality;
    return this;
  }

  public RangeOverPlayers addNationalityItem(String nationalityItem) {
    if (this.nationality == null) {
      this.nationality = new ArrayList<>();
    }
    this.nationality.add(nationalityItem);
    return this;
  }

  /**
   * Get nationality
   * @return nationality
   */
  @javax.annotation.Nullable
  public List<String> getNationality() {
    return nationality;
  }

  public void setNationality(List<String> nationality) {
    this.nationality = nationality;
  }


  public RangeOverPlayers role(List<String> role) {
    this.role = role;
    return this;
  }

  public RangeOverPlayers addRoleItem(String roleItem) {
    if (this.role == null) {
      this.role = new ArrayList<>();
    }
    this.role.add(roleItem);
    return this;
  }

  /**
   * Get role
   * @return role
   */
  @javax.annotation.Nullable
  public List<String> getRole() {
    return role;
  }

  public void setRole(List<String> role) {
    this.role = role;
  }


  public RangeOverPlayers slug(List<String> slug) {
    this.slug = slug;
    return this;
  }

  public RangeOverPlayers addSlugItem(String slugItem) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RangeOverPlayers rangeOverPlayers = (RangeOverPlayers) o;
    return Objects.equals(this.birthYear, rangeOverPlayers.birthYear) &&
        Objects.equals(this.birthday, rangeOverPlayers.birthday) &&
        Objects.equals(this.firstName, rangeOverPlayers.firstName) &&
        Objects.equals(this.hometown, rangeOverPlayers.hometown) &&
        Objects.equals(this.id, rangeOverPlayers.id) &&
        Objects.equals(this.lastName, rangeOverPlayers.lastName) &&
        Objects.equals(this.name, rangeOverPlayers.name) &&
        Objects.equals(this.nationality, rangeOverPlayers.nationality) &&
        Objects.equals(this.role, rangeOverPlayers.role) &&
        Objects.equals(this.slug, rangeOverPlayers.slug);
  }

  @Override
  public int hashCode() {
    return Objects.hash(birthYear, birthday, firstName, hometown, id, lastName, name, nationality, role, slug);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RangeOverPlayers {\n");
    sb.append("    birthYear: ").append(toIndentedString(birthYear)).append("\n");
    sb.append("    birthday: ").append(toIndentedString(birthday)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    hometown: ").append(toIndentedString(hometown)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nationality: ").append(toIndentedString(nationality)).append("\n");
    sb.append("    role: ").append(toIndentedString(role)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
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
    openapiFields.add("birth_year");
    openapiFields.add("birthday");
    openapiFields.add("first_name");
    openapiFields.add("hometown");
    openapiFields.add("id");
    openapiFields.add("last_name");
    openapiFields.add("name");
    openapiFields.add("nationality");
    openapiFields.add("role");
    openapiFields.add("slug");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RangeOverPlayers
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RangeOverPlayers.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RangeOverPlayers is not found in the empty JSON string", RangeOverPlayers.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RangeOverPlayers.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RangeOverPlayers` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("birth_year") != null && !jsonObj.get("birth_year").isJsonNull() && !jsonObj.get("birth_year").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `birth_year` to be an array in the JSON string but got `%s`", jsonObj.get("birth_year").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("birthday") != null && !jsonObj.get("birthday").isJsonNull() && !jsonObj.get("birthday").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `birthday` to be an array in the JSON string but got `%s`", jsonObj.get("birthday").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull() && !jsonObj.get("first_name").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be an array in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("hometown") != null && !jsonObj.get("hometown").isJsonNull() && !jsonObj.get("hometown").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `hometown` to be an array in the JSON string but got `%s`", jsonObj.get("hometown").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull() && !jsonObj.get("id").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be an array in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull() && !jsonObj.get("last_name").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be an array in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull() && !jsonObj.get("name").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be an array in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("nationality") != null && !jsonObj.get("nationality").isJsonNull() && !jsonObj.get("nationality").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `nationality` to be an array in the JSON string but got `%s`", jsonObj.get("nationality").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("role") != null && !jsonObj.get("role").isJsonNull() && !jsonObj.get("role").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `role` to be an array in the JSON string but got `%s`", jsonObj.get("role").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("slug") != null && !jsonObj.get("slug").isJsonNull() && !jsonObj.get("slug").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be an array in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RangeOverPlayers.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RangeOverPlayers' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RangeOverPlayers> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RangeOverPlayers.class));

       return (TypeAdapter<T>) new TypeAdapter<RangeOverPlayers>() {
           @Override
           public void write(JsonWriter out, RangeOverPlayers value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RangeOverPlayers read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RangeOverPlayers given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RangeOverPlayers
   * @throws IOException if the JSON string is invalid with respect to RangeOverPlayers
   */
  public static RangeOverPlayers fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RangeOverPlayers.class);
  }

  /**
   * Convert an instance of RangeOverPlayers to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

