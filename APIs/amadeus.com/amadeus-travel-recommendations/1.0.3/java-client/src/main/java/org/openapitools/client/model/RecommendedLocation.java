/*
 * Travel Recommendations API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.3
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
import java.util.Arrays;
import org.openapitools.client.model.GeoCode;

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
 * Similar Location
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:02.835999-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RecommendedLocation {
  public static final String SERIALIZED_NAME_GEO_CODE = "geoCode";
  @SerializedName(SERIALIZED_NAME_GEO_CODE)
  private GeoCode geoCode;

  public static final String SERIALIZED_NAME_IATA_CODE = "iataCode";
  @SerializedName(SERIALIZED_NAME_IATA_CODE)
  private String iataCode;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SUBTYPE = "subtype";
  @SerializedName(SERIALIZED_NAME_SUBTYPE)
  private String subtype;

  public static final String SERIALIZED_NAME_RELEVANCE = "relevance";
  @SerializedName(SERIALIZED_NAME_RELEVANCE)
  private BigDecimal relevance;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public RecommendedLocation() {
  }

  public RecommendedLocation geoCode(GeoCode geoCode) {
    this.geoCode = geoCode;
    return this;
  }

  /**
   * Get geoCode
   * @return geoCode
   */
  @javax.annotation.Nullable
  public GeoCode getGeoCode() {
    return geoCode;
  }

  public void setGeoCode(GeoCode geoCode) {
    this.geoCode = geoCode;
  }


  public RecommendedLocation iataCode(String iataCode) {
    this.iataCode = iataCode;
    return this;
  }

  /**
   * IATA location code
   * @return iataCode
   */
  @javax.annotation.Nullable
  public String getIataCode() {
    return iataCode;
  }

  public void setIataCode(String iataCode) {
    this.iataCode = iataCode;
  }


  public RecommendedLocation name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Label associated to the location (e.g. Eiffel Tower, Madison Square)
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public RecommendedLocation subtype(String subtype) {
    this.subtype = subtype;
    return this;
  }

  /**
   * Location sub-type (e.g. airport, port, rail-station, restaurant, atm...)
   * @return subtype
   */
  @javax.annotation.Nullable
  public String getSubtype() {
    return subtype;
  }

  public void setSubtype(String subtype) {
    this.subtype = subtype;
  }


  public RecommendedLocation relevance(BigDecimal relevance) {
    this.relevance = relevance;
    return this;
  }

  /**
   * percentage of similarity.  0 for not similar to 1 for exactly the same
   * @return relevance
   */
  @javax.annotation.Nullable
  public BigDecimal getRelevance() {
    return relevance;
  }

  public void setRelevance(BigDecimal relevance) {
    this.relevance = relevance;
  }


  public RecommendedLocation type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Ressource type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RecommendedLocation recommendedLocation = (RecommendedLocation) o;
    return Objects.equals(this.geoCode, recommendedLocation.geoCode) &&
        Objects.equals(this.iataCode, recommendedLocation.iataCode) &&
        Objects.equals(this.name, recommendedLocation.name) &&
        Objects.equals(this.subtype, recommendedLocation.subtype) &&
        Objects.equals(this.relevance, recommendedLocation.relevance) &&
        Objects.equals(this.type, recommendedLocation.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(geoCode, iataCode, name, subtype, relevance, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RecommendedLocation {\n");
    sb.append("    geoCode: ").append(toIndentedString(geoCode)).append("\n");
    sb.append("    iataCode: ").append(toIndentedString(iataCode)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    subtype: ").append(toIndentedString(subtype)).append("\n");
    sb.append("    relevance: ").append(toIndentedString(relevance)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("geoCode");
    openapiFields.add("iataCode");
    openapiFields.add("name");
    openapiFields.add("subtype");
    openapiFields.add("relevance");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RecommendedLocation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RecommendedLocation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RecommendedLocation is not found in the empty JSON string", RecommendedLocation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RecommendedLocation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RecommendedLocation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `geoCode`
      if (jsonObj.get("geoCode") != null && !jsonObj.get("geoCode").isJsonNull()) {
        GeoCode.validateJsonElement(jsonObj.get("geoCode"));
      }
      if ((jsonObj.get("iataCode") != null && !jsonObj.get("iataCode").isJsonNull()) && !jsonObj.get("iataCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iataCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iataCode").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("subtype") != null && !jsonObj.get("subtype").isJsonNull()) && !jsonObj.get("subtype").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subtype` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subtype").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RecommendedLocation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RecommendedLocation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RecommendedLocation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RecommendedLocation.class));

       return (TypeAdapter<T>) new TypeAdapter<RecommendedLocation>() {
           @Override
           public void write(JsonWriter out, RecommendedLocation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RecommendedLocation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RecommendedLocation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RecommendedLocation
   * @throws IOException if the JSON string is invalid with respect to RecommendedLocation
   */
  public static RecommendedLocation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RecommendedLocation.class);
  }

  /**
   * Convert an instance of RecommendedLocation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

