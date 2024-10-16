/*
 * CORE API v2
 * <p style=\"text-align: justify;\">You can use the CORE API to access the      resources harvested and enriched by CORE. If you encounter any problems with the API, please <a href=\"/contact\">report them to us</a>.</p>  <h2>Overview</h2> <p style=\"text-align: justify;\">The API is organised by resource type. The resources are <b>articles</b>,      <b>journals</b> and <b>repositories</b> and are represented using JSON data format. Furthermore,      each resource has a list of methods. The API also provides two global methods for accessing all resources at once.</p>  <h2>Response format</h2> <p style=\"text-align: justify;\">Response for each query contains two fields: <b>status</b> and <b>data</b>.     In case of an error status, the data field is empty. The data field contains a single object     in case the request is for a specific identifier (e.g. CORE ID, CORE repository ID, etc.), or       contains a list of objects, for example for search queries. In case of batch requests, the response     is an array of objects, each of which contains its own <b>status</b> and <b>data</b> fields.     For search queries the response contains an additional field <b>totalHits</b>, which is the      total number of items which match the search criteria.</p>  <h2>Search query syntax</h2>  <p style=\"text-align: justify\">Complex search queries can be used in all of the API search methods.     The query can be a simple string or it can be built using terms and operators described in Elasticsearch     <a href=\"http://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-query-string-query.html#query-string-syntax\">documentation</a>.     The usable field names are <strong>title</strong>, <strong>description</strong>, <strong>fullText</strong>,      <strong>authors</strong>, <strong>publisher</strong>, <strong>repositories.id</strong>, <strong>repositories.name</strong>,      <strong>doi</strong>, <strong>oai</strong>, <strong>identifiers</strong> (which is a list of article identifiers including OAI, URL, etc.), <strong>language.name</strong>      and <strong>year</strong>. Some example queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>title:psychology and language.name:English</p></li>     <li><p>repositories.id:86 AND year:2014</p></li>     <li><p>identifiers:\"oai:aura.abdn.ac.uk:2164/3837\" OR identifiers:\"oai:aura.abdn.ac.uk:2164/3843\"</p></li>     <li><p>doi:\"10.1186/1471-2458-6-309\"</p></li> </ul>  <h3>Retrieving the latest Articles</h3> <p style=\"text-align: justify\">     You can retrieve the harvested items since specific dates using the following queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>repositoryDocument.metadataUpdated:>2017-02-10</p></li>     <li><p>repositoryDocument.metadataUpdated:>2017-03-01 AND repositoryDocument.metadataUpdated:<2017-03-31</p></li>     </ul>  <h2>Sort order</h2>  <p style=\"text-align: justify;\">For search queries, the results are ordered by relevance score. For batch      requests, the results are retrieved in the order of the requests.</p>  <h2>Parameters</h2> <p style=\"text-align: justify;\">The API methods allow different parameters to be passed. Additionally, there is an API key parameter which is common to all API methods. For all API methods      the API key can be provided either as a query parameter or in the request header. If the API key      is not provided, the API will return HTTP 401 error. You can register for an API key <a href=\"/services#api\">here</a>.</p>  <h2>API methods</h2>
 *
 * The version of the OpenAPI document: 2.0
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
 * RepositoryLocation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:44.717365-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RepositoryLocation {
  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_COUNTRY_CODE = "countryCode";
  @SerializedName(SERIALIZED_NAME_COUNTRY_CODE)
  private String countryCode;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LATITUDE = "latitude";
  @SerializedName(SERIALIZED_NAME_LATITUDE)
  private Integer latitude;

  public static final String SERIALIZED_NAME_LONGITUDE = "longitude";
  @SerializedName(SERIALIZED_NAME_LONGITUDE)
  private Integer longitude;

  public static final String SERIALIZED_NAME_REPOSITORY_NAME = "repositoryName";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_NAME)
  private String repositoryName;

  public RepositoryLocation() {
  }

  public RepositoryLocation country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Country name
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public RepositoryLocation countryCode(String countryCode) {
    this.countryCode = countryCode;
    return this;
  }

  /**
   * Two letter country code
   * @return countryCode
   */
  @javax.annotation.Nullable
  public String getCountryCode() {
    return countryCode;
  }

  public void setCountryCode(String countryCode) {
    this.countryCode = countryCode;
  }


  public RepositoryLocation id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * CORE repository ID
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public RepositoryLocation latitude(Integer latitude) {
    this.latitude = latitude;
    return this;
  }

  /**
   * Get latitude
   * @return latitude
   */
  @javax.annotation.Nullable
  public Integer getLatitude() {
    return latitude;
  }

  public void setLatitude(Integer latitude) {
    this.latitude = latitude;
  }


  public RepositoryLocation longitude(Integer longitude) {
    this.longitude = longitude;
    return this;
  }

  /**
   * Get longitude
   * @return longitude
   */
  @javax.annotation.Nullable
  public Integer getLongitude() {
    return longitude;
  }

  public void setLongitude(Integer longitude) {
    this.longitude = longitude;
  }


  public RepositoryLocation repositoryName(String repositoryName) {
    this.repositoryName = repositoryName;
    return this;
  }

  /**
   * Repository name
   * @return repositoryName
   */
  @javax.annotation.Nullable
  public String getRepositoryName() {
    return repositoryName;
  }

  public void setRepositoryName(String repositoryName) {
    this.repositoryName = repositoryName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RepositoryLocation repositoryLocation = (RepositoryLocation) o;
    return Objects.equals(this.country, repositoryLocation.country) &&
        Objects.equals(this.countryCode, repositoryLocation.countryCode) &&
        Objects.equals(this.id, repositoryLocation.id) &&
        Objects.equals(this.latitude, repositoryLocation.latitude) &&
        Objects.equals(this.longitude, repositoryLocation.longitude) &&
        Objects.equals(this.repositoryName, repositoryLocation.repositoryName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(country, countryCode, id, latitude, longitude, repositoryName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RepositoryLocation {\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    countryCode: ").append(toIndentedString(countryCode)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    latitude: ").append(toIndentedString(latitude)).append("\n");
    sb.append("    longitude: ").append(toIndentedString(longitude)).append("\n");
    sb.append("    repositoryName: ").append(toIndentedString(repositoryName)).append("\n");
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
    openapiFields.add("country");
    openapiFields.add("countryCode");
    openapiFields.add("id");
    openapiFields.add("latitude");
    openapiFields.add("longitude");
    openapiFields.add("repositoryName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RepositoryLocation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RepositoryLocation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RepositoryLocation is not found in the empty JSON string", RepositoryLocation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RepositoryLocation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RepositoryLocation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if ((jsonObj.get("countryCode") != null && !jsonObj.get("countryCode").isJsonNull()) && !jsonObj.get("countryCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `countryCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("countryCode").toString()));
      }
      if ((jsonObj.get("repositoryName") != null && !jsonObj.get("repositoryName").isJsonNull()) && !jsonObj.get("repositoryName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `repositoryName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("repositoryName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RepositoryLocation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RepositoryLocation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RepositoryLocation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RepositoryLocation.class));

       return (TypeAdapter<T>) new TypeAdapter<RepositoryLocation>() {
           @Override
           public void write(JsonWriter out, RepositoryLocation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RepositoryLocation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RepositoryLocation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RepositoryLocation
   * @throws IOException if the JSON string is invalid with respect to RepositoryLocation
   */
  public static RepositoryLocation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RepositoryLocation.class);
  }

  /**
   * Convert an instance of RepositoryLocation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

