/*
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
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
 * The reasons that contributed to the price unavailable count and the total count for each reason.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:52.320664-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PriceUnavailableCountDetails {
  public static final String SERIALIZED_NAME_PARTICIPATION_NOT_LIKELY_COUNT = "participationNotLikelyCount";
  @SerializedName(SERIALIZED_NAME_PARTICIPATION_NOT_LIKELY_COUNT)
  private String participationNotLikelyCount;

  public static final String SERIALIZED_NAME_PRICE_UNAVAILABLE_COUNT = "priceUnavailableCount";
  @SerializedName(SERIALIZED_NAME_PRICE_UNAVAILABLE_COUNT)
  private String priceUnavailableCount;

  public PriceUnavailableCountDetails() {
  }

  public PriceUnavailableCountDetails participationNotLikelyCount(String participationNotLikelyCount) {
    this.participationNotLikelyCount = participationNotLikelyCount;
    return this;
  }

  /**
   * No price was cached for this itinerary, and no live query was done because your server usually tells us the hotel is unavailable or sold out.
   * @return participationNotLikelyCount
   */
  @javax.annotation.Nullable
  public String getParticipationNotLikelyCount() {
    return participationNotLikelyCount;
  }

  public void setParticipationNotLikelyCount(String participationNotLikelyCount) {
    this.participationNotLikelyCount = participationNotLikelyCount;
  }


  public PriceUnavailableCountDetails priceUnavailableCount(String priceUnavailableCount) {
    this.priceUnavailableCount = priceUnavailableCount;
    return this;
  }

  /**
   * Hotel did not participate because it wasn&#39;t available for the itinerary dates.
   * @return priceUnavailableCount
   */
  @javax.annotation.Nullable
  public String getPriceUnavailableCount() {
    return priceUnavailableCount;
  }

  public void setPriceUnavailableCount(String priceUnavailableCount) {
    this.priceUnavailableCount = priceUnavailableCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PriceUnavailableCountDetails priceUnavailableCountDetails = (PriceUnavailableCountDetails) o;
    return Objects.equals(this.participationNotLikelyCount, priceUnavailableCountDetails.participationNotLikelyCount) &&
        Objects.equals(this.priceUnavailableCount, priceUnavailableCountDetails.priceUnavailableCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(participationNotLikelyCount, priceUnavailableCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PriceUnavailableCountDetails {\n");
    sb.append("    participationNotLikelyCount: ").append(toIndentedString(participationNotLikelyCount)).append("\n");
    sb.append("    priceUnavailableCount: ").append(toIndentedString(priceUnavailableCount)).append("\n");
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
    openapiFields.add("participationNotLikelyCount");
    openapiFields.add("priceUnavailableCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PriceUnavailableCountDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PriceUnavailableCountDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PriceUnavailableCountDetails is not found in the empty JSON string", PriceUnavailableCountDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PriceUnavailableCountDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PriceUnavailableCountDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("participationNotLikelyCount") != null && !jsonObj.get("participationNotLikelyCount").isJsonNull()) && !jsonObj.get("participationNotLikelyCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `participationNotLikelyCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("participationNotLikelyCount").toString()));
      }
      if ((jsonObj.get("priceUnavailableCount") != null && !jsonObj.get("priceUnavailableCount").isJsonNull()) && !jsonObj.get("priceUnavailableCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `priceUnavailableCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("priceUnavailableCount").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PriceUnavailableCountDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PriceUnavailableCountDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PriceUnavailableCountDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PriceUnavailableCountDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<PriceUnavailableCountDetails>() {
           @Override
           public void write(JsonWriter out, PriceUnavailableCountDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PriceUnavailableCountDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PriceUnavailableCountDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PriceUnavailableCountDetails
   * @throws IOException if the JSON string is invalid with respect to PriceUnavailableCountDetails
   */
  public static PriceUnavailableCountDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PriceUnavailableCountDetails.class);
  }

  /**
   * Convert an instance of PriceUnavailableCountDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

