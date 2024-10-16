/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import org.openapitools.client.model.AnalyticsEventPerDeviceCount200ResponseCountPerDeviceInner;

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
 * EventCountPerSession
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EventCountPerSession {
  public static final String SERIALIZED_NAME_AVG_COUNT_PER_SESSION = "avg_count_per_session";
  @SerializedName(SERIALIZED_NAME_AVG_COUNT_PER_SESSION)
  private Double avgCountPerSession;

  public static final String SERIALIZED_NAME_COUNT_PER_SESSION = "count_per_session";
  @SerializedName(SERIALIZED_NAME_COUNT_PER_SESSION)
  private List<AnalyticsEventPerDeviceCount200ResponseCountPerDeviceInner> countPerSession = new ArrayList<>();

  public static final String SERIALIZED_NAME_PREVIOUS_AVG_COUNT_PER_SESSION = "previous_avg_count_per_session";
  @SerializedName(SERIALIZED_NAME_PREVIOUS_AVG_COUNT_PER_SESSION)
  private Double previousAvgCountPerSession;

  public EventCountPerSession() {
  }

  public EventCountPerSession avgCountPerSession(Double avgCountPerSession) {
    this.avgCountPerSession = avgCountPerSession;
    return this;
  }

  /**
   * Get avgCountPerSession
   * @return avgCountPerSession
   */
  @javax.annotation.Nullable
  public Double getAvgCountPerSession() {
    return avgCountPerSession;
  }

  public void setAvgCountPerSession(Double avgCountPerSession) {
    this.avgCountPerSession = avgCountPerSession;
  }


  public EventCountPerSession countPerSession(List<AnalyticsEventPerDeviceCount200ResponseCountPerDeviceInner> countPerSession) {
    this.countPerSession = countPerSession;
    return this;
  }

  public EventCountPerSession addCountPerSessionItem(AnalyticsEventPerDeviceCount200ResponseCountPerDeviceInner countPerSessionItem) {
    if (this.countPerSession == null) {
      this.countPerSession = new ArrayList<>();
    }
    this.countPerSession.add(countPerSessionItem);
    return this;
  }

  /**
   * Get countPerSession
   * @return countPerSession
   */
  @javax.annotation.Nullable
  public List<AnalyticsEventPerDeviceCount200ResponseCountPerDeviceInner> getCountPerSession() {
    return countPerSession;
  }

  public void setCountPerSession(List<AnalyticsEventPerDeviceCount200ResponseCountPerDeviceInner> countPerSession) {
    this.countPerSession = countPerSession;
  }


  public EventCountPerSession previousAvgCountPerSession(Double previousAvgCountPerSession) {
    this.previousAvgCountPerSession = previousAvgCountPerSession;
    return this;
  }

  /**
   * Get previousAvgCountPerSession
   * @return previousAvgCountPerSession
   */
  @javax.annotation.Nullable
  public Double getPreviousAvgCountPerSession() {
    return previousAvgCountPerSession;
  }

  public void setPreviousAvgCountPerSession(Double previousAvgCountPerSession) {
    this.previousAvgCountPerSession = previousAvgCountPerSession;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EventCountPerSession eventCountPerSession = (EventCountPerSession) o;
    return Objects.equals(this.avgCountPerSession, eventCountPerSession.avgCountPerSession) &&
        Objects.equals(this.countPerSession, eventCountPerSession.countPerSession) &&
        Objects.equals(this.previousAvgCountPerSession, eventCountPerSession.previousAvgCountPerSession);
  }

  @Override
  public int hashCode() {
    return Objects.hash(avgCountPerSession, countPerSession, previousAvgCountPerSession);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EventCountPerSession {\n");
    sb.append("    avgCountPerSession: ").append(toIndentedString(avgCountPerSession)).append("\n");
    sb.append("    countPerSession: ").append(toIndentedString(countPerSession)).append("\n");
    sb.append("    previousAvgCountPerSession: ").append(toIndentedString(previousAvgCountPerSession)).append("\n");
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
    openapiFields.add("avg_count_per_session");
    openapiFields.add("count_per_session");
    openapiFields.add("previous_avg_count_per_session");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EventCountPerSession
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EventCountPerSession.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EventCountPerSession is not found in the empty JSON string", EventCountPerSession.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EventCountPerSession.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EventCountPerSession` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("count_per_session") != null && !jsonObj.get("count_per_session").isJsonNull()) {
        JsonArray jsonArraycountPerSession = jsonObj.getAsJsonArray("count_per_session");
        if (jsonArraycountPerSession != null) {
          // ensure the json data is an array
          if (!jsonObj.get("count_per_session").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `count_per_session` to be an array in the JSON string but got `%s`", jsonObj.get("count_per_session").toString()));
          }

          // validate the optional field `count_per_session` (array)
          for (int i = 0; i < jsonArraycountPerSession.size(); i++) {
            AnalyticsEventPerDeviceCount200ResponseCountPerDeviceInner.validateJsonElement(jsonArraycountPerSession.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EventCountPerSession.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EventCountPerSession' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EventCountPerSession> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EventCountPerSession.class));

       return (TypeAdapter<T>) new TypeAdapter<EventCountPerSession>() {
           @Override
           public void write(JsonWriter out, EventCountPerSession value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EventCountPerSession read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EventCountPerSession given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EventCountPerSession
   * @throws IOException if the JSON string is invalid with respect to EventCountPerSession
   */
  public static EventCountPerSession fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EventCountPerSession.class);
  }

  /**
   * Convert an instance of EventCountPerSession to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

