/*
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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
 * The metric availability.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:41.316643-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MetricAvailablity {
  public static final String SERIALIZED_NAME_RETENTION = "retention";
  @SerializedName(SERIALIZED_NAME_RETENTION)
  private String retention;

  public static final String SERIALIZED_NAME_TIME_GRAIN = "timeGrain";
  @SerializedName(SERIALIZED_NAME_TIME_GRAIN)
  private String timeGrain;

  public MetricAvailablity() {
  }

  public MetricAvailablity retention(String retention) {
    this.retention = retention;
    return this;
  }

  /**
   * The retention period for the metric at the specified timegrain.
   * @return retention
   */
  @javax.annotation.Nullable
  public String getRetention() {
    return retention;
  }

  public void setRetention(String retention) {
    this.retention = retention;
  }


  public MetricAvailablity timeGrain(String timeGrain) {
    this.timeGrain = timeGrain;
    return this;
  }

  /**
   * The aggregation interval for the metric.
   * @return timeGrain
   */
  @javax.annotation.Nullable
  public String getTimeGrain() {
    return timeGrain;
  }

  public void setTimeGrain(String timeGrain) {
    this.timeGrain = timeGrain;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MetricAvailablity metricAvailablity = (MetricAvailablity) o;
    return Objects.equals(this.retention, metricAvailablity.retention) &&
        Objects.equals(this.timeGrain, metricAvailablity.timeGrain);
  }

  @Override
  public int hashCode() {
    return Objects.hash(retention, timeGrain);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MetricAvailablity {\n");
    sb.append("    retention: ").append(toIndentedString(retention)).append("\n");
    sb.append("    timeGrain: ").append(toIndentedString(timeGrain)).append("\n");
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
    openapiFields.add("retention");
    openapiFields.add("timeGrain");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MetricAvailablity
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MetricAvailablity.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MetricAvailablity is not found in the empty JSON string", MetricAvailablity.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MetricAvailablity.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MetricAvailablity` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("retention") != null && !jsonObj.get("retention").isJsonNull()) && !jsonObj.get("retention").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `retention` to be a primitive type in the JSON string but got `%s`", jsonObj.get("retention").toString()));
      }
      if ((jsonObj.get("timeGrain") != null && !jsonObj.get("timeGrain").isJsonNull()) && !jsonObj.get("timeGrain").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timeGrain` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timeGrain").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MetricAvailablity.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MetricAvailablity' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MetricAvailablity> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MetricAvailablity.class));

       return (TypeAdapter<T>) new TypeAdapter<MetricAvailablity>() {
           @Override
           public void write(JsonWriter out, MetricAvailablity value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MetricAvailablity read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MetricAvailablity given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MetricAvailablity
   * @throws IOException if the JSON string is invalid with respect to MetricAvailablity
   */
  public static MetricAvailablity fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MetricAvailablity.class);
  }

  /**
   * Convert an instance of MetricAvailablity to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

