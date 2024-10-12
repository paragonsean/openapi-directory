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
 * Response message for HotelViewService.SummarizeHotelViews.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:52.320664-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SummarizeHotelViewsResponse {
  public static final String SERIALIZED_NAME_LAST_FEED_SUBMISSION_TIME = "lastFeedSubmissionTime";
  @SerializedName(SERIALIZED_NAME_LAST_FEED_SUBMISSION_TIME)
  private String lastFeedSubmissionTime;

  public static final String SERIALIZED_NAME_LAST_MANIFEST_UPDATE_TIME = "lastManifestUpdateTime";
  @SerializedName(SERIALIZED_NAME_LAST_MANIFEST_UPDATE_TIME)
  private String lastManifestUpdateTime;

  public static final String SERIALIZED_NAME_LIVE_ON_GOOGLE_PROPERTY_COUNT = "liveOnGooglePropertyCount";
  @SerializedName(SERIALIZED_NAME_LIVE_ON_GOOGLE_PROPERTY_COUNT)
  private String liveOnGooglePropertyCount;

  public static final String SERIALIZED_NAME_MATCHED_PROPERTY_COUNT = "matchedPropertyCount";
  @SerializedName(SERIALIZED_NAME_MATCHED_PROPERTY_COUNT)
  private String matchedPropertyCount;

  public static final String SERIALIZED_NAME_OVERCLUSTERED_PROPERTY_COUNT = "overclusteredPropertyCount";
  @SerializedName(SERIALIZED_NAME_OVERCLUSTERED_PROPERTY_COUNT)
  private String overclusteredPropertyCount;

  public static final String SERIALIZED_NAME_OVERCLUSTERED_PROPERTY_WITH_ERRORS_COUNT = "overclusteredPropertyWithErrorsCount";
  @SerializedName(SERIALIZED_NAME_OVERCLUSTERED_PROPERTY_WITH_ERRORS_COUNT)
  private String overclusteredPropertyWithErrorsCount;

  public static final String SERIALIZED_NAME_UNMATCHED_PROPERTY_COUNT = "unmatchedPropertyCount";
  @SerializedName(SERIALIZED_NAME_UNMATCHED_PROPERTY_COUNT)
  private String unmatchedPropertyCount;

  public static final String SERIALIZED_NAME_UNMATCHED_PROPERTY_WITH_ERRORS_COUNT = "unmatchedPropertyWithErrorsCount";
  @SerializedName(SERIALIZED_NAME_UNMATCHED_PROPERTY_WITH_ERRORS_COUNT)
  private String unmatchedPropertyWithErrorsCount;

  public SummarizeHotelViewsResponse() {
  }

  public SummarizeHotelViewsResponse lastFeedSubmissionTime(String lastFeedSubmissionTime) {
    this.lastFeedSubmissionTime = lastFeedSubmissionTime;
    return this;
  }

  /**
   * Timestamp of the last hotel feed submission.
   * @return lastFeedSubmissionTime
   */
  @javax.annotation.Nullable
  public String getLastFeedSubmissionTime() {
    return lastFeedSubmissionTime;
  }

  public void setLastFeedSubmissionTime(String lastFeedSubmissionTime) {
    this.lastFeedSubmissionTime = lastFeedSubmissionTime;
  }


  public SummarizeHotelViewsResponse lastManifestUpdateTime(String lastManifestUpdateTime) {
    this.lastManifestUpdateTime = lastManifestUpdateTime;
    return this;
  }

  /**
   * Timestamp of the last hotel manifest update.
   * @return lastManifestUpdateTime
   */
  @javax.annotation.Nullable
  public String getLastManifestUpdateTime() {
    return lastManifestUpdateTime;
  }

  public void setLastManifestUpdateTime(String lastManifestUpdateTime) {
    this.lastManifestUpdateTime = lastManifestUpdateTime;
  }


  public SummarizeHotelViewsResponse liveOnGooglePropertyCount(String liveOnGooglePropertyCount) {
    this.liveOnGooglePropertyCount = liveOnGooglePropertyCount;
    return this;
  }

  /**
   * The number of properties that are Live on Google.
   * @return liveOnGooglePropertyCount
   */
  @javax.annotation.Nullable
  public String getLiveOnGooglePropertyCount() {
    return liveOnGooglePropertyCount;
  }

  public void setLiveOnGooglePropertyCount(String liveOnGooglePropertyCount) {
    this.liveOnGooglePropertyCount = liveOnGooglePropertyCount;
  }


  public SummarizeHotelViewsResponse matchedPropertyCount(String matchedPropertyCount) {
    this.matchedPropertyCount = matchedPropertyCount;
    return this;
  }

  /**
   * The number of properties that match Google&#39;s manifest.
   * @return matchedPropertyCount
   */
  @javax.annotation.Nullable
  public String getMatchedPropertyCount() {
    return matchedPropertyCount;
  }

  public void setMatchedPropertyCount(String matchedPropertyCount) {
    this.matchedPropertyCount = matchedPropertyCount;
  }


  public SummarizeHotelViewsResponse overclusteredPropertyCount(String overclusteredPropertyCount) {
    this.overclusteredPropertyCount = overclusteredPropertyCount;
    return this;
  }

  /**
   * The number of hotels that are considered overclustered.
   * @return overclusteredPropertyCount
   */
  @javax.annotation.Nullable
  public String getOverclusteredPropertyCount() {
    return overclusteredPropertyCount;
  }

  public void setOverclusteredPropertyCount(String overclusteredPropertyCount) {
    this.overclusteredPropertyCount = overclusteredPropertyCount;
  }


  public SummarizeHotelViewsResponse overclusteredPropertyWithErrorsCount(String overclusteredPropertyWithErrorsCount) {
    this.overclusteredPropertyWithErrorsCount = overclusteredPropertyWithErrorsCount;
    return this;
  }

  /**
   * The number of overclustered properties that have data-related errors.
   * @return overclusteredPropertyWithErrorsCount
   */
  @javax.annotation.Nullable
  public String getOverclusteredPropertyWithErrorsCount() {
    return overclusteredPropertyWithErrorsCount;
  }

  public void setOverclusteredPropertyWithErrorsCount(String overclusteredPropertyWithErrorsCount) {
    this.overclusteredPropertyWithErrorsCount = overclusteredPropertyWithErrorsCount;
  }


  public SummarizeHotelViewsResponse unmatchedPropertyCount(String unmatchedPropertyCount) {
    this.unmatchedPropertyCount = unmatchedPropertyCount;
    return this;
  }

  /**
   * The number of properties that are considered unmatched.
   * @return unmatchedPropertyCount
   */
  @javax.annotation.Nullable
  public String getUnmatchedPropertyCount() {
    return unmatchedPropertyCount;
  }

  public void setUnmatchedPropertyCount(String unmatchedPropertyCount) {
    this.unmatchedPropertyCount = unmatchedPropertyCount;
  }


  public SummarizeHotelViewsResponse unmatchedPropertyWithErrorsCount(String unmatchedPropertyWithErrorsCount) {
    this.unmatchedPropertyWithErrorsCount = unmatchedPropertyWithErrorsCount;
    return this;
  }

  /**
   * The number of unmatched properties that have data-related errors.
   * @return unmatchedPropertyWithErrorsCount
   */
  @javax.annotation.Nullable
  public String getUnmatchedPropertyWithErrorsCount() {
    return unmatchedPropertyWithErrorsCount;
  }

  public void setUnmatchedPropertyWithErrorsCount(String unmatchedPropertyWithErrorsCount) {
    this.unmatchedPropertyWithErrorsCount = unmatchedPropertyWithErrorsCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SummarizeHotelViewsResponse summarizeHotelViewsResponse = (SummarizeHotelViewsResponse) o;
    return Objects.equals(this.lastFeedSubmissionTime, summarizeHotelViewsResponse.lastFeedSubmissionTime) &&
        Objects.equals(this.lastManifestUpdateTime, summarizeHotelViewsResponse.lastManifestUpdateTime) &&
        Objects.equals(this.liveOnGooglePropertyCount, summarizeHotelViewsResponse.liveOnGooglePropertyCount) &&
        Objects.equals(this.matchedPropertyCount, summarizeHotelViewsResponse.matchedPropertyCount) &&
        Objects.equals(this.overclusteredPropertyCount, summarizeHotelViewsResponse.overclusteredPropertyCount) &&
        Objects.equals(this.overclusteredPropertyWithErrorsCount, summarizeHotelViewsResponse.overclusteredPropertyWithErrorsCount) &&
        Objects.equals(this.unmatchedPropertyCount, summarizeHotelViewsResponse.unmatchedPropertyCount) &&
        Objects.equals(this.unmatchedPropertyWithErrorsCount, summarizeHotelViewsResponse.unmatchedPropertyWithErrorsCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(lastFeedSubmissionTime, lastManifestUpdateTime, liveOnGooglePropertyCount, matchedPropertyCount, overclusteredPropertyCount, overclusteredPropertyWithErrorsCount, unmatchedPropertyCount, unmatchedPropertyWithErrorsCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SummarizeHotelViewsResponse {\n");
    sb.append("    lastFeedSubmissionTime: ").append(toIndentedString(lastFeedSubmissionTime)).append("\n");
    sb.append("    lastManifestUpdateTime: ").append(toIndentedString(lastManifestUpdateTime)).append("\n");
    sb.append("    liveOnGooglePropertyCount: ").append(toIndentedString(liveOnGooglePropertyCount)).append("\n");
    sb.append("    matchedPropertyCount: ").append(toIndentedString(matchedPropertyCount)).append("\n");
    sb.append("    overclusteredPropertyCount: ").append(toIndentedString(overclusteredPropertyCount)).append("\n");
    sb.append("    overclusteredPropertyWithErrorsCount: ").append(toIndentedString(overclusteredPropertyWithErrorsCount)).append("\n");
    sb.append("    unmatchedPropertyCount: ").append(toIndentedString(unmatchedPropertyCount)).append("\n");
    sb.append("    unmatchedPropertyWithErrorsCount: ").append(toIndentedString(unmatchedPropertyWithErrorsCount)).append("\n");
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
    openapiFields.add("lastFeedSubmissionTime");
    openapiFields.add("lastManifestUpdateTime");
    openapiFields.add("liveOnGooglePropertyCount");
    openapiFields.add("matchedPropertyCount");
    openapiFields.add("overclusteredPropertyCount");
    openapiFields.add("overclusteredPropertyWithErrorsCount");
    openapiFields.add("unmatchedPropertyCount");
    openapiFields.add("unmatchedPropertyWithErrorsCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SummarizeHotelViewsResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SummarizeHotelViewsResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SummarizeHotelViewsResponse is not found in the empty JSON string", SummarizeHotelViewsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SummarizeHotelViewsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SummarizeHotelViewsResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("lastFeedSubmissionTime") != null && !jsonObj.get("lastFeedSubmissionTime").isJsonNull()) && !jsonObj.get("lastFeedSubmissionTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastFeedSubmissionTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastFeedSubmissionTime").toString()));
      }
      if ((jsonObj.get("lastManifestUpdateTime") != null && !jsonObj.get("lastManifestUpdateTime").isJsonNull()) && !jsonObj.get("lastManifestUpdateTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastManifestUpdateTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastManifestUpdateTime").toString()));
      }
      if ((jsonObj.get("liveOnGooglePropertyCount") != null && !jsonObj.get("liveOnGooglePropertyCount").isJsonNull()) && !jsonObj.get("liveOnGooglePropertyCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `liveOnGooglePropertyCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("liveOnGooglePropertyCount").toString()));
      }
      if ((jsonObj.get("matchedPropertyCount") != null && !jsonObj.get("matchedPropertyCount").isJsonNull()) && !jsonObj.get("matchedPropertyCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `matchedPropertyCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("matchedPropertyCount").toString()));
      }
      if ((jsonObj.get("overclusteredPropertyCount") != null && !jsonObj.get("overclusteredPropertyCount").isJsonNull()) && !jsonObj.get("overclusteredPropertyCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `overclusteredPropertyCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("overclusteredPropertyCount").toString()));
      }
      if ((jsonObj.get("overclusteredPropertyWithErrorsCount") != null && !jsonObj.get("overclusteredPropertyWithErrorsCount").isJsonNull()) && !jsonObj.get("overclusteredPropertyWithErrorsCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `overclusteredPropertyWithErrorsCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("overclusteredPropertyWithErrorsCount").toString()));
      }
      if ((jsonObj.get("unmatchedPropertyCount") != null && !jsonObj.get("unmatchedPropertyCount").isJsonNull()) && !jsonObj.get("unmatchedPropertyCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unmatchedPropertyCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unmatchedPropertyCount").toString()));
      }
      if ((jsonObj.get("unmatchedPropertyWithErrorsCount") != null && !jsonObj.get("unmatchedPropertyWithErrorsCount").isJsonNull()) && !jsonObj.get("unmatchedPropertyWithErrorsCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unmatchedPropertyWithErrorsCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unmatchedPropertyWithErrorsCount").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SummarizeHotelViewsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SummarizeHotelViewsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SummarizeHotelViewsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SummarizeHotelViewsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<SummarizeHotelViewsResponse>() {
           @Override
           public void write(JsonWriter out, SummarizeHotelViewsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SummarizeHotelViewsResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SummarizeHotelViewsResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SummarizeHotelViewsResponse
   * @throws IOException if the JSON string is invalid with respect to SummarizeHotelViewsResponse
   */
  public static SummarizeHotelViewsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SummarizeHotelViewsResponse.class);
  }

  /**
   * Convert an instance of SummarizeHotelViewsResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

