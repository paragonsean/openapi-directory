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
 * The reasons that contributed to the no price count and the total count for each reason.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:52.320664-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NoPriceCountDetails {
  public static final String SERIALIZED_NAME_LIVE_PRICING_CONFIG_ISSUE_COUNT = "livePricingConfigIssueCount";
  @SerializedName(SERIALIZED_NAME_LIVE_PRICING_CONFIG_ISSUE_COUNT)
  private String livePricingConfigIssueCount;

  public static final String SERIALIZED_NAME_LIVE_PRICING_NOT_AVAILABLE_COUNT = "livePricingNotAvailableCount";
  @SerializedName(SERIALIZED_NAME_LIVE_PRICING_NOT_AVAILABLE_COUNT)
  private String livePricingNotAvailableCount;

  public static final String SERIALIZED_NAME_LIVE_PRICING_NOT_TRIGGERED_COUNT = "livePricingNotTriggeredCount";
  @SerializedName(SERIALIZED_NAME_LIVE_PRICING_NOT_TRIGGERED_COUNT)
  private String livePricingNotTriggeredCount;

  public static final String SERIALIZED_NAME_LIVE_PRICING_OTHER_REASON_COUNT = "livePricingOtherReasonCount";
  @SerializedName(SERIALIZED_NAME_LIVE_PRICING_OTHER_REASON_COUNT)
  private String livePricingOtherReasonCount;

  public static final String SERIALIZED_NAME_LIVE_PRICING_TECHNICAL_ISSUE_COUNT = "livePricingTechnicalIssueCount";
  @SerializedName(SERIALIZED_NAME_LIVE_PRICING_TECHNICAL_ISSUE_COUNT)
  private String livePricingTechnicalIssueCount;

  public NoPriceCountDetails() {
  }

  public NoPriceCountDetails livePricingConfigIssueCount(String livePricingConfigIssueCount) {
    this.livePricingConfigIssueCount = livePricingConfigIssueCount;
    return this;
  }

  /**
   * The total number of missed participation due to live pricing not being triggered for any of the following reasons: * You didn&#39;t have live pricing configured for these searches. * You restricted Google from accessing the hotel itinerary in question.
   * @return livePricingConfigIssueCount
   */
  @javax.annotation.Nullable
  public String getLivePricingConfigIssueCount() {
    return livePricingConfigIssueCount;
  }

  public void setLivePricingConfigIssueCount(String livePricingConfigIssueCount) {
    this.livePricingConfigIssueCount = livePricingConfigIssueCount;
  }


  public NoPriceCountDetails livePricingNotAvailableCount(String livePricingNotAvailableCount) {
    this.livePricingNotAvailableCount = livePricingNotAvailableCount;
    return this;
  }

  /**
   * The total number of missed participation due to live pricing being unavailable. Live pricing will not be triggered for certain default itineraries or UIs. In this scenario, partners will need a cached price to participate.
   * @return livePricingNotAvailableCount
   */
  @javax.annotation.Nullable
  public String getLivePricingNotAvailableCount() {
    return livePricingNotAvailableCount;
  }

  public void setLivePricingNotAvailableCount(String livePricingNotAvailableCount) {
    this.livePricingNotAvailableCount = livePricingNotAvailableCount;
  }


  public NoPriceCountDetails livePricingNotTriggeredCount(String livePricingNotTriggeredCount) {
    this.livePricingNotTriggeredCount = livePricingNotTriggeredCount;
    return this;
  }

  /**
   * The total number of missed participation due to live pricing not being triggered for any of the following reasons: * You didn&#39;t set a bid. * You didn&#39;t have a valid landing page. * There weren&#39;t enough prices in the cache.
   * @return livePricingNotTriggeredCount
   */
  @javax.annotation.Nullable
  public String getLivePricingNotTriggeredCount() {
    return livePricingNotTriggeredCount;
  }

  public void setLivePricingNotTriggeredCount(String livePricingNotTriggeredCount) {
    this.livePricingNotTriggeredCount = livePricingNotTriggeredCount;
  }


  public NoPriceCountDetails livePricingOtherReasonCount(String livePricingOtherReasonCount) {
    this.livePricingOtherReasonCount = livePricingOtherReasonCount;
    return this;
  }

  /**
   * The number of missed participations due to other issues with live pricing.
   * @return livePricingOtherReasonCount
   */
  @javax.annotation.Nullable
  public String getLivePricingOtherReasonCount() {
    return livePricingOtherReasonCount;
  }

  public void setLivePricingOtherReasonCount(String livePricingOtherReasonCount) {
    this.livePricingOtherReasonCount = livePricingOtherReasonCount;
  }


  public NoPriceCountDetails livePricingTechnicalIssueCount(String livePricingTechnicalIssueCount) {
    this.livePricingTechnicalIssueCount = livePricingTechnicalIssueCount;
    return this;
  }

  /**
   * The total number of missed participation due to technical issues with live pricing for any of the following reasons: * You didn’t respond quickly enough and exceeded the response deadline (around 4000 milliseconds). * You returned an error. * Your response was malformed.
   * @return livePricingTechnicalIssueCount
   */
  @javax.annotation.Nullable
  public String getLivePricingTechnicalIssueCount() {
    return livePricingTechnicalIssueCount;
  }

  public void setLivePricingTechnicalIssueCount(String livePricingTechnicalIssueCount) {
    this.livePricingTechnicalIssueCount = livePricingTechnicalIssueCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NoPriceCountDetails noPriceCountDetails = (NoPriceCountDetails) o;
    return Objects.equals(this.livePricingConfigIssueCount, noPriceCountDetails.livePricingConfigIssueCount) &&
        Objects.equals(this.livePricingNotAvailableCount, noPriceCountDetails.livePricingNotAvailableCount) &&
        Objects.equals(this.livePricingNotTriggeredCount, noPriceCountDetails.livePricingNotTriggeredCount) &&
        Objects.equals(this.livePricingOtherReasonCount, noPriceCountDetails.livePricingOtherReasonCount) &&
        Objects.equals(this.livePricingTechnicalIssueCount, noPriceCountDetails.livePricingTechnicalIssueCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(livePricingConfigIssueCount, livePricingNotAvailableCount, livePricingNotTriggeredCount, livePricingOtherReasonCount, livePricingTechnicalIssueCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NoPriceCountDetails {\n");
    sb.append("    livePricingConfigIssueCount: ").append(toIndentedString(livePricingConfigIssueCount)).append("\n");
    sb.append("    livePricingNotAvailableCount: ").append(toIndentedString(livePricingNotAvailableCount)).append("\n");
    sb.append("    livePricingNotTriggeredCount: ").append(toIndentedString(livePricingNotTriggeredCount)).append("\n");
    sb.append("    livePricingOtherReasonCount: ").append(toIndentedString(livePricingOtherReasonCount)).append("\n");
    sb.append("    livePricingTechnicalIssueCount: ").append(toIndentedString(livePricingTechnicalIssueCount)).append("\n");
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
    openapiFields.add("livePricingConfigIssueCount");
    openapiFields.add("livePricingNotAvailableCount");
    openapiFields.add("livePricingNotTriggeredCount");
    openapiFields.add("livePricingOtherReasonCount");
    openapiFields.add("livePricingTechnicalIssueCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NoPriceCountDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NoPriceCountDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NoPriceCountDetails is not found in the empty JSON string", NoPriceCountDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NoPriceCountDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NoPriceCountDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("livePricingConfigIssueCount") != null && !jsonObj.get("livePricingConfigIssueCount").isJsonNull()) && !jsonObj.get("livePricingConfigIssueCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `livePricingConfigIssueCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("livePricingConfigIssueCount").toString()));
      }
      if ((jsonObj.get("livePricingNotAvailableCount") != null && !jsonObj.get("livePricingNotAvailableCount").isJsonNull()) && !jsonObj.get("livePricingNotAvailableCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `livePricingNotAvailableCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("livePricingNotAvailableCount").toString()));
      }
      if ((jsonObj.get("livePricingNotTriggeredCount") != null && !jsonObj.get("livePricingNotTriggeredCount").isJsonNull()) && !jsonObj.get("livePricingNotTriggeredCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `livePricingNotTriggeredCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("livePricingNotTriggeredCount").toString()));
      }
      if ((jsonObj.get("livePricingOtherReasonCount") != null && !jsonObj.get("livePricingOtherReasonCount").isJsonNull()) && !jsonObj.get("livePricingOtherReasonCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `livePricingOtherReasonCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("livePricingOtherReasonCount").toString()));
      }
      if ((jsonObj.get("livePricingTechnicalIssueCount") != null && !jsonObj.get("livePricingTechnicalIssueCount").isJsonNull()) && !jsonObj.get("livePricingTechnicalIssueCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `livePricingTechnicalIssueCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("livePricingTechnicalIssueCount").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NoPriceCountDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NoPriceCountDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NoPriceCountDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NoPriceCountDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<NoPriceCountDetails>() {
           @Override
           public void write(JsonWriter out, NoPriceCountDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NoPriceCountDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NoPriceCountDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NoPriceCountDetails
   * @throws IOException if the JSON string is invalid with respect to NoPriceCountDetails
   */
  public static NoPriceCountDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NoPriceCountDetails.class);
  }

  /**
   * Convert an instance of NoPriceCountDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

