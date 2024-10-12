/*
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AirlineRemarkType;

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
 * AirlineRemark
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:54.608298-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AirlineRemark {
  public static final String SERIALIZED_NAME_AIRLINE_CODE = "airlineCode";
  @SerializedName(SERIALIZED_NAME_AIRLINE_CODE)
  private String airlineCode;

  public static final String SERIALIZED_NAME_FLIGHT_OFFER_IDS = "flightOfferIds";
  @SerializedName(SERIALIZED_NAME_FLIGHT_OFFER_IDS)
  private List<String> flightOfferIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_KEYWORD = "keyword";
  @SerializedName(SERIALIZED_NAME_KEYWORD)
  private String keyword;

  public static final String SERIALIZED_NAME_SUB_TYPE = "subType";
  @SerializedName(SERIALIZED_NAME_SUB_TYPE)
  private AirlineRemarkType subType;

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public static final String SERIALIZED_NAME_TRAVELER_IDS = "travelerIds";
  @SerializedName(SERIALIZED_NAME_TRAVELER_IDS)
  private List<String> travelerIds = new ArrayList<>();

  public AirlineRemark() {
  }

  public AirlineRemark airlineCode(String airlineCode) {
    this.airlineCode = airlineCode;
    return this;
  }

  /**
   * Code of the airline following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx))  When it apply to any airline, value is YY. 
   * @return airlineCode
   */
  @javax.annotation.Nonnull
  public String getAirlineCode() {
    return airlineCode;
  }

  public void setAirlineCode(String airlineCode) {
    this.airlineCode = airlineCode;
  }


  public AirlineRemark flightOfferIds(List<String> flightOfferIds) {
    this.flightOfferIds = flightOfferIds;
    return this;
  }

  public AirlineRemark addFlightOfferIdsItem(String flightOfferIdsItem) {
    if (this.flightOfferIds == null) {
      this.flightOfferIds = new ArrayList<>();
    }
    this.flightOfferIds.add(flightOfferIdsItem);
    return this;
  }

  /**
   * Id of the concern flightOffers
   * @return flightOfferIds
   */
  @javax.annotation.Nullable
  public List<String> getFlightOfferIds() {
    return flightOfferIds;
  }

  public void setFlightOfferIds(List<String> flightOfferIds) {
    this.flightOfferIds = flightOfferIds;
  }


  public AirlineRemark keyword(String keyword) {
    this.keyword = keyword;
    return this;
  }

  /**
   * keyword code - only applicable for subType Keyword
   * @return keyword
   */
  @javax.annotation.Nullable
  public String getKeyword() {
    return keyword;
  }

  public void setKeyword(String keyword) {
    this.keyword = keyword;
  }


  public AirlineRemark subType(AirlineRemarkType subType) {
    this.subType = subType;
    return this;
  }

  /**
   * Get subType
   * @return subType
   */
  @javax.annotation.Nonnull
  public AirlineRemarkType getSubType() {
    return subType;
  }

  public void setSubType(AirlineRemarkType subType) {
    this.subType = subType;
  }


  public AirlineRemark text(String text) {
    this.text = text;
    return this;
  }

  /**
   * remark free text
   * @return text
   */
  @javax.annotation.Nonnull
  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }


  public AirlineRemark travelerIds(List<String> travelerIds) {
    this.travelerIds = travelerIds;
    return this;
  }

  public AirlineRemark addTravelerIdsItem(String travelerIdsItem) {
    if (this.travelerIds == null) {
      this.travelerIds = new ArrayList<>();
    }
    this.travelerIds.add(travelerIdsItem);
    return this;
  }

  /**
   * Id of the concerned traveler
   * @return travelerIds
   */
  @javax.annotation.Nullable
  public List<String> getTravelerIds() {
    return travelerIds;
  }

  public void setTravelerIds(List<String> travelerIds) {
    this.travelerIds = travelerIds;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AirlineRemark airlineRemark = (AirlineRemark) o;
    return Objects.equals(this.airlineCode, airlineRemark.airlineCode) &&
        Objects.equals(this.flightOfferIds, airlineRemark.flightOfferIds) &&
        Objects.equals(this.keyword, airlineRemark.keyword) &&
        Objects.equals(this.subType, airlineRemark.subType) &&
        Objects.equals(this.text, airlineRemark.text) &&
        Objects.equals(this.travelerIds, airlineRemark.travelerIds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(airlineCode, flightOfferIds, keyword, subType, text, travelerIds);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AirlineRemark {\n");
    sb.append("    airlineCode: ").append(toIndentedString(airlineCode)).append("\n");
    sb.append("    flightOfferIds: ").append(toIndentedString(flightOfferIds)).append("\n");
    sb.append("    keyword: ").append(toIndentedString(keyword)).append("\n");
    sb.append("    subType: ").append(toIndentedString(subType)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
    sb.append("    travelerIds: ").append(toIndentedString(travelerIds)).append("\n");
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
    openapiFields.add("airlineCode");
    openapiFields.add("flightOfferIds");
    openapiFields.add("keyword");
    openapiFields.add("subType");
    openapiFields.add("text");
    openapiFields.add("travelerIds");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("airlineCode");
    openapiRequiredFields.add("subType");
    openapiRequiredFields.add("text");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AirlineRemark
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AirlineRemark.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AirlineRemark is not found in the empty JSON string", AirlineRemark.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AirlineRemark.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AirlineRemark` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AirlineRemark.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("airlineCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `airlineCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("airlineCode").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("flightOfferIds") != null && !jsonObj.get("flightOfferIds").isJsonNull() && !jsonObj.get("flightOfferIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `flightOfferIds` to be an array in the JSON string but got `%s`", jsonObj.get("flightOfferIds").toString()));
      }
      if ((jsonObj.get("keyword") != null && !jsonObj.get("keyword").isJsonNull()) && !jsonObj.get("keyword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `keyword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("keyword").toString()));
      }
      // validate the required field `subType`
      AirlineRemarkType.validateJsonElement(jsonObj.get("subType"));
      if (!jsonObj.get("text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("text").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("travelerIds") != null && !jsonObj.get("travelerIds").isJsonNull() && !jsonObj.get("travelerIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `travelerIds` to be an array in the JSON string but got `%s`", jsonObj.get("travelerIds").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AirlineRemark.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AirlineRemark' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AirlineRemark> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AirlineRemark.class));

       return (TypeAdapter<T>) new TypeAdapter<AirlineRemark>() {
           @Override
           public void write(JsonWriter out, AirlineRemark value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AirlineRemark read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AirlineRemark given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AirlineRemark
   * @throws IOException if the JSON string is invalid with respect to AirlineRemark
   */
  public static AirlineRemark fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AirlineRemark.class);
  }

  /**
   * Convert an instance of AirlineRemark to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

