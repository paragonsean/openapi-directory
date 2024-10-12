/*
 * Pims
 *  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  <div class=\"info\"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   <ul>     <li>Base path: `https://demo.pims.io/api`</li>     <li>Username: `demo`</li>     <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>   </ul> </div>  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">  <div style=\"display: inline-block; width:100%;\">   <strong>So when you read in the doc:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"object\"</span>: {   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>  } }</code></pre>  </div>  <div style=\"display: inline-block; width:100%;\">   <strong>... you'll get in the Real World®:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"_embedded\"</span>: {   <span class=\"token string\">\"object\"</span>: {    <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,    <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,    <span class=\"token string\">\"_links\"</span>: {     <span class=\"token string\">\"self\"</span>: {      <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>     }    }   }  }  <span class=\"token string\">\"_links\"</span>: {   <span class=\"token string\">\"self\"</span>: {    <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>   }  } }</code></pre>  </div> </div>  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.  The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON: ```json {  \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",     \"title\": \"Not Found\",  \"status\": 404,     \"detail\": \"Entity not found\" } ```  ## Versioning The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: ```json {  \"_links\": {   \"self\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=1\"   },   \"first\": {    \"href\": \"https://demo.pims.io/api/v1/events\"   },   \"last\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=14\"   },   \"next\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=2\"   }  },  \"_embedded\": {    ... // data content goes here  },  \"page_count\": 14,  \"page_size\": 25,  \"total_items\": 331,  \"page\": 1 } ```  ## Filtering and sorting Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>): - Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)     2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)     3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@pims.io
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.VenuesEntityType;

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
 * VenuesEntity
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:11.901875-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VenuesEntity {
  public static final String SERIALIZED_NAME_ALTERNATIVE_LABELS = "alternative_labels";
  @SerializedName(SERIALIZED_NAME_ALTERNATIVE_LABELS)
  private List<String> alternativeLabels = new ArrayList<>();

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COUNTRY_CODE = "country_code";
  @SerializedName(SERIALIZED_NAME_COUNTRY_CODE)
  private String countryCode;

  public static final String SERIALIZED_NAME_CREATION_TIMESTAMP = "creation_timestamp";
  @SerializedName(SERIALIZED_NAME_CREATION_TIMESTAMP)
  private Long creationTimestamp;

  public static final String SERIALIZED_NAME_FIRST_ADDRESS = "first_address";
  @SerializedName(SERIALIZED_NAME_FIRST_ADDRESS)
  private String firstAddress;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_LAST_UPDATE_TIMESTAMP = "last_update_timestamp";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE_TIMESTAMP)
  private Long lastUpdateTimestamp;

  public static final String SERIALIZED_NAME_MAJOR_CITY = "major_city";
  @SerializedName(SERIALIZED_NAME_MAJOR_CITY)
  private String majorCity;

  public static final String SERIALIZED_NAME_SECOND_ADDRESS = "second_address";
  @SerializedName(SERIALIZED_NAME_SECOND_ADDRESS)
  private String secondAddress;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private VenuesEntityType type;

  public static final String SERIALIZED_NAME_ZIP_CODE = "zip_code";
  @SerializedName(SERIALIZED_NAME_ZIP_CODE)
  private String zipCode;

  public VenuesEntity() {
  }

  public VenuesEntity alternativeLabels(List<String> alternativeLabels) {
    this.alternativeLabels = alternativeLabels;
    return this;
  }

  public VenuesEntity addAlternativeLabelsItem(String alternativeLabelsItem) {
    if (this.alternativeLabels == null) {
      this.alternativeLabels = new ArrayList<>();
    }
    this.alternativeLabels.add(alternativeLabelsItem);
    return this;
  }

  /**
   * Array of alternative/old names of the venue.
   * @return alternativeLabels
   */
  @javax.annotation.Nullable
  public List<String> getAlternativeLabels() {
    return alternativeLabels;
  }

  public void setAlternativeLabels(List<String> alternativeLabels) {
    this.alternativeLabels = alternativeLabels;
  }


  public VenuesEntity city(String city) {
    this.city = city;
    return this;
  }

  /**
   * City in which the venue is.
   * @return city
   */
  @javax.annotation.Nonnull
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public VenuesEntity countryCode(String countryCode) {
    this.countryCode = countryCode;
    return this;
  }

  /**
   * Country in which the venue is (&lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3&#39;&gt;ISO 3166-1 alpha-3 code&lt;/a&gt;).
   * @return countryCode
   */
  @javax.annotation.Nonnull
  public String getCountryCode() {
    return countryCode;
  }

  public void setCountryCode(String countryCode) {
    this.countryCode = countryCode;
  }


  public VenuesEntity creationTimestamp(Long creationTimestamp) {
    this.creationTimestamp = creationTimestamp;
    return this;
  }

  /**
   * Timestamp for when the venue was created in the customer&#39;s database.
   * @return creationTimestamp
   */
  @javax.annotation.Nonnull
  public Long getCreationTimestamp() {
    return creationTimestamp;
  }

  public void setCreationTimestamp(Long creationTimestamp) {
    this.creationTimestamp = creationTimestamp;
  }


  public VenuesEntity firstAddress(String firstAddress) {
    this.firstAddress = firstAddress;
    return this;
  }

  /**
   * First address field of the venue.
   * @return firstAddress
   */
  @javax.annotation.Nullable
  public String getFirstAddress() {
    return firstAddress;
  }

  public void setFirstAddress(String firstAddress) {
    this.firstAddress = firstAddress;
  }


  public VenuesEntity id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Unique ID of the venue.
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public VenuesEntity label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Name of the venue.
   * @return label
   */
  @javax.annotation.Nonnull
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public VenuesEntity lastUpdateTimestamp(Long lastUpdateTimestamp) {
    this.lastUpdateTimestamp = lastUpdateTimestamp;
    return this;
  }

  /**
   * Timestamp for when the venue was last updated in the customer&#39;s database.
   * @return lastUpdateTimestamp
   */
  @javax.annotation.Nonnull
  public Long getLastUpdateTimestamp() {
    return lastUpdateTimestamp;
  }

  public void setLastUpdateTimestamp(Long lastUpdateTimestamp) {
    this.lastUpdateTimestamp = lastUpdateTimestamp;
  }


  public VenuesEntity majorCity(String majorCity) {
    this.majorCity = majorCity;
    return this;
  }

  /**
   * Major city or metropolitan area the venue belongs to.
   * @return majorCity
   */
  @javax.annotation.Nullable
  public String getMajorCity() {
    return majorCity;
  }

  public void setMajorCity(String majorCity) {
    this.majorCity = majorCity;
  }


  public VenuesEntity secondAddress(String secondAddress) {
    this.secondAddress = secondAddress;
    return this;
  }

  /**
   * Second address field of the venue.
   * @return secondAddress
   */
  @javax.annotation.Nullable
  public String getSecondAddress() {
    return secondAddress;
  }

  public void setSecondAddress(String secondAddress) {
    this.secondAddress = secondAddress;
  }


  public VenuesEntity type(VenuesEntityType type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nonnull
  public VenuesEntityType getType() {
    return type;
  }

  public void setType(VenuesEntityType type) {
    this.type = type;
  }


  public VenuesEntity zipCode(String zipCode) {
    this.zipCode = zipCode;
    return this;
  }

  /**
   * ZIP code of the venue.
   * @return zipCode
   */
  @javax.annotation.Nullable
  public String getZipCode() {
    return zipCode;
  }

  public void setZipCode(String zipCode) {
    this.zipCode = zipCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VenuesEntity venuesEntity = (VenuesEntity) o;
    return Objects.equals(this.alternativeLabels, venuesEntity.alternativeLabels) &&
        Objects.equals(this.city, venuesEntity.city) &&
        Objects.equals(this.countryCode, venuesEntity.countryCode) &&
        Objects.equals(this.creationTimestamp, venuesEntity.creationTimestamp) &&
        Objects.equals(this.firstAddress, venuesEntity.firstAddress) &&
        Objects.equals(this.id, venuesEntity.id) &&
        Objects.equals(this.label, venuesEntity.label) &&
        Objects.equals(this.lastUpdateTimestamp, venuesEntity.lastUpdateTimestamp) &&
        Objects.equals(this.majorCity, venuesEntity.majorCity) &&
        Objects.equals(this.secondAddress, venuesEntity.secondAddress) &&
        Objects.equals(this.type, venuesEntity.type) &&
        Objects.equals(this.zipCode, venuesEntity.zipCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alternativeLabels, city, countryCode, creationTimestamp, firstAddress, id, label, lastUpdateTimestamp, majorCity, secondAddress, type, zipCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VenuesEntity {\n");
    sb.append("    alternativeLabels: ").append(toIndentedString(alternativeLabels)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    countryCode: ").append(toIndentedString(countryCode)).append("\n");
    sb.append("    creationTimestamp: ").append(toIndentedString(creationTimestamp)).append("\n");
    sb.append("    firstAddress: ").append(toIndentedString(firstAddress)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    lastUpdateTimestamp: ").append(toIndentedString(lastUpdateTimestamp)).append("\n");
    sb.append("    majorCity: ").append(toIndentedString(majorCity)).append("\n");
    sb.append("    secondAddress: ").append(toIndentedString(secondAddress)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    zipCode: ").append(toIndentedString(zipCode)).append("\n");
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
    openapiFields.add("alternative_labels");
    openapiFields.add("city");
    openapiFields.add("country_code");
    openapiFields.add("creation_timestamp");
    openapiFields.add("first_address");
    openapiFields.add("id");
    openapiFields.add("label");
    openapiFields.add("last_update_timestamp");
    openapiFields.add("major_city");
    openapiFields.add("second_address");
    openapiFields.add("type");
    openapiFields.add("zip_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("city");
    openapiRequiredFields.add("country_code");
    openapiRequiredFields.add("creation_timestamp");
    openapiRequiredFields.add("first_address");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("label");
    openapiRequiredFields.add("last_update_timestamp");
    openapiRequiredFields.add("major_city");
    openapiRequiredFields.add("second_address");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("zip_code");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VenuesEntity
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VenuesEntity.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VenuesEntity is not found in the empty JSON string", VenuesEntity.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VenuesEntity.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VenuesEntity` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : VenuesEntity.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("alternative_labels") != null && !jsonObj.get("alternative_labels").isJsonNull() && !jsonObj.get("alternative_labels").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `alternative_labels` to be an array in the JSON string but got `%s`", jsonObj.get("alternative_labels").toString()));
      }
      if (!jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if (!jsonObj.get("country_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country_code").toString()));
      }
      if ((jsonObj.get("first_address") != null && !jsonObj.get("first_address").isJsonNull()) && !jsonObj.get("first_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_address").toString()));
      }
      if (!jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      if ((jsonObj.get("major_city") != null && !jsonObj.get("major_city").isJsonNull()) && !jsonObj.get("major_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `major_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("major_city").toString()));
      }
      if ((jsonObj.get("second_address") != null && !jsonObj.get("second_address").isJsonNull()) && !jsonObj.get("second_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `second_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("second_address").toString()));
      }
      // validate the required field `type`
      VenuesEntityType.validateJsonElement(jsonObj.get("type"));
      if ((jsonObj.get("zip_code") != null && !jsonObj.get("zip_code").isJsonNull()) && !jsonObj.get("zip_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `zip_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("zip_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VenuesEntity.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VenuesEntity' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VenuesEntity> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VenuesEntity.class));

       return (TypeAdapter<T>) new TypeAdapter<VenuesEntity>() {
           @Override
           public void write(JsonWriter out, VenuesEntity value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VenuesEntity read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VenuesEntity given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VenuesEntity
   * @throws IOException if the JSON string is invalid with respect to VenuesEntity
   */
  public static VenuesEntity fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VenuesEntity.class);
  }

  /**
   * Convert an instance of VenuesEntity to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

