/*
 * Football Prediction API
 * The Football Prediction API allows developers to get predictions for upcoming football (soccer) matches, results for past matches, and performance monitoring for statistical models.
 *
 * The version of the OpenAPI document: 2
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
 * ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:57.981204-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days {
  public static final String SERIALIZED_NAME_LOST = "lost";
  @SerializedName(SERIALIZED_NAME_LOST)
  private Integer lost;

  public static final String SERIALIZED_NAME_PENDING = "pending";
  @SerializedName(SERIALIZED_NAME_PENDING)
  private Integer pending;

  public static final String SERIALIZED_NAME_POSTPONED = "postponed";
  @SerializedName(SERIALIZED_NAME_POSTPONED)
  private Integer postponed;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Integer total;

  public static final String SERIALIZED_NAME_WON = "won";
  @SerializedName(SERIALIZED_NAME_WON)
  private Integer won;

  public ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days() {
  }

  public ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days lost(Integer lost) {
    this.lost = lost;
    return this;
  }

  /**
   * Get lost
   * @return lost
   */
  @javax.annotation.Nullable
  public Integer getLost() {
    return lost;
  }

  public void setLost(Integer lost) {
    this.lost = lost;
  }


  public ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days pending(Integer pending) {
    this.pending = pending;
    return this;
  }

  /**
   * Get pending
   * @return pending
   */
  @javax.annotation.Nullable
  public Integer getPending() {
    return pending;
  }

  public void setPending(Integer pending) {
    this.pending = pending;
  }


  public ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days postponed(Integer postponed) {
    this.postponed = postponed;
    return this;
  }

  /**
   * Get postponed
   * @return postponed
   */
  @javax.annotation.Nullable
  public Integer getPostponed() {
    return postponed;
  }

  public void setPostponed(Integer postponed) {
    this.postponed = postponed;
  }


  public ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days total(Integer total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public Integer getTotal() {
    return total;
  }

  public void setTotal(Integer total) {
    this.total = total;
  }


  public ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days won(Integer won) {
    this.won = won;
    return this;
  }

  /**
   * Get won
   * @return won
   */
  @javax.annotation.Nullable
  public Integer getWon() {
    return won;
  }

  public void setWon(Integer won) {
    this.won = won;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days apiV2PerformanceStatsGet200ResponseDataDetailsLast14Days = (ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days) o;
    return Objects.equals(this.lost, apiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.lost) &&
        Objects.equals(this.pending, apiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.pending) &&
        Objects.equals(this.postponed, apiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.postponed) &&
        Objects.equals(this.total, apiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.total) &&
        Objects.equals(this.won, apiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.won);
  }

  @Override
  public int hashCode() {
    return Objects.hash(lost, pending, postponed, total, won);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days {\n");
    sb.append("    lost: ").append(toIndentedString(lost)).append("\n");
    sb.append("    pending: ").append(toIndentedString(pending)).append("\n");
    sb.append("    postponed: ").append(toIndentedString(postponed)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    won: ").append(toIndentedString(won)).append("\n");
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
    openapiFields.add("lost");
    openapiFields.add("pending");
    openapiFields.add("postponed");
    openapiFields.add("total");
    openapiFields.add("won");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days is not found in the empty JSON string", ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days>() {
           @Override
           public void write(JsonWriter out, ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days
   * @throws IOException if the JSON string is invalid with respect to ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days
   */
  public static ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days.class);
  }

  /**
   * Convert an instance of ApiV2PerformanceStatsGet200ResponseDataDetailsLast14Days to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

