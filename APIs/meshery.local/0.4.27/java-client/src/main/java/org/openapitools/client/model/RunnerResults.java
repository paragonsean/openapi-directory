/*
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.RunnerResultsDurationHistogram;

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
 * RunnerResults
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:51.881749-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RunnerResults {
  public static final String SERIALIZED_NAME_ACTUAL_DURATION = "ActualDuration";
  @SerializedName(SERIALIZED_NAME_ACTUAL_DURATION)
  private Integer actualDuration;

  public static final String SERIALIZED_NAME_ACTUAL_Q_P_S = "ActualQPS";
  @SerializedName(SERIALIZED_NAME_ACTUAL_Q_P_S)
  private Double actualQPS;

  public static final String SERIALIZED_NAME_DURATION_HISTOGRAM = "DurationHistogram";
  @SerializedName(SERIALIZED_NAME_DURATION_HISTOGRAM)
  private RunnerResultsDurationHistogram durationHistogram;

  public static final String SERIALIZED_NAME_START_TIME = "StartTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private OffsetDateTime startTime;

  public static final String SERIALIZED_NAME_U_R_L = "URL";
  @SerializedName(SERIALIZED_NAME_U_R_L)
  private String URL;

  public static final String SERIALIZED_NAME_LOAD_GENERATOR = "load-generator";
  @SerializedName(SERIALIZED_NAME_LOAD_GENERATOR)
  private String loadGenerator;

  public RunnerResults() {
  }

  public RunnerResults actualDuration(Integer actualDuration) {
    this.actualDuration = actualDuration;
    return this;
  }

  /**
   * Get actualDuration
   * @return actualDuration
   */
  @javax.annotation.Nullable
  public Integer getActualDuration() {
    return actualDuration;
  }

  public void setActualDuration(Integer actualDuration) {
    this.actualDuration = actualDuration;
  }


  public RunnerResults actualQPS(Double actualQPS) {
    this.actualQPS = actualQPS;
    return this;
  }

  /**
   * Get actualQPS
   * @return actualQPS
   */
  @javax.annotation.Nullable
  public Double getActualQPS() {
    return actualQPS;
  }

  public void setActualQPS(Double actualQPS) {
    this.actualQPS = actualQPS;
  }


  public RunnerResults durationHistogram(RunnerResultsDurationHistogram durationHistogram) {
    this.durationHistogram = durationHistogram;
    return this;
  }

  /**
   * Get durationHistogram
   * @return durationHistogram
   */
  @javax.annotation.Nullable
  public RunnerResultsDurationHistogram getDurationHistogram() {
    return durationHistogram;
  }

  public void setDurationHistogram(RunnerResultsDurationHistogram durationHistogram) {
    this.durationHistogram = durationHistogram;
  }


  public RunnerResults startTime(OffsetDateTime startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Get startTime
   * @return startTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartTime() {
    return startTime;
  }

  public void setStartTime(OffsetDateTime startTime) {
    this.startTime = startTime;
  }


  public RunnerResults URL(String URL) {
    this.URL = URL;
    return this;
  }

  /**
   * Get URL
   * @return URL
   */
  @javax.annotation.Nullable
  public String getURL() {
    return URL;
  }

  public void setURL(String URL) {
    this.URL = URL;
  }


  public RunnerResults loadGenerator(String loadGenerator) {
    this.loadGenerator = loadGenerator;
    return this;
  }

  /**
   * Get loadGenerator
   * @return loadGenerator
   */
  @javax.annotation.Nullable
  public String getLoadGenerator() {
    return loadGenerator;
  }

  public void setLoadGenerator(String loadGenerator) {
    this.loadGenerator = loadGenerator;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RunnerResults runnerResults = (RunnerResults) o;
    return Objects.equals(this.actualDuration, runnerResults.actualDuration) &&
        Objects.equals(this.actualQPS, runnerResults.actualQPS) &&
        Objects.equals(this.durationHistogram, runnerResults.durationHistogram) &&
        Objects.equals(this.startTime, runnerResults.startTime) &&
        Objects.equals(this.URL, runnerResults.URL) &&
        Objects.equals(this.loadGenerator, runnerResults.loadGenerator);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actualDuration, actualQPS, durationHistogram, startTime, URL, loadGenerator);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RunnerResults {\n");
    sb.append("    actualDuration: ").append(toIndentedString(actualDuration)).append("\n");
    sb.append("    actualQPS: ").append(toIndentedString(actualQPS)).append("\n");
    sb.append("    durationHistogram: ").append(toIndentedString(durationHistogram)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    URL: ").append(toIndentedString(URL)).append("\n");
    sb.append("    loadGenerator: ").append(toIndentedString(loadGenerator)).append("\n");
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
    openapiFields.add("ActualDuration");
    openapiFields.add("ActualQPS");
    openapiFields.add("DurationHistogram");
    openapiFields.add("StartTime");
    openapiFields.add("URL");
    openapiFields.add("load-generator");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RunnerResults
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RunnerResults.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RunnerResults is not found in the empty JSON string", RunnerResults.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RunnerResults.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RunnerResults` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `DurationHistogram`
      if (jsonObj.get("DurationHistogram") != null && !jsonObj.get("DurationHistogram").isJsonNull()) {
        RunnerResultsDurationHistogram.validateJsonElement(jsonObj.get("DurationHistogram"));
      }
      if ((jsonObj.get("URL") != null && !jsonObj.get("URL").isJsonNull()) && !jsonObj.get("URL").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `URL` to be a primitive type in the JSON string but got `%s`", jsonObj.get("URL").toString()));
      }
      if ((jsonObj.get("load-generator") != null && !jsonObj.get("load-generator").isJsonNull()) && !jsonObj.get("load-generator").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `load-generator` to be a primitive type in the JSON string but got `%s`", jsonObj.get("load-generator").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RunnerResults.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RunnerResults' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RunnerResults> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RunnerResults.class));

       return (TypeAdapter<T>) new TypeAdapter<RunnerResults>() {
           @Override
           public void write(JsonWriter out, RunnerResults value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RunnerResults read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RunnerResults given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RunnerResults
   * @throws IOException if the JSON string is invalid with respect to RunnerResults
   */
  public static RunnerResults fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RunnerResults.class);
  }

  /**
   * Convert an instance of RunnerResults to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

