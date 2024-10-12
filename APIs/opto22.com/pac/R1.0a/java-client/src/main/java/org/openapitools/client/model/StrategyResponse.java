/*
 * PAC Control REST API
 * #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller's variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC's strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   ``` https://1.2.3.4/api/v1/device/strategy/vars/int32s ``` and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  ```json [ { \"nMyVeryFavoriteNumber\": 22 },   { \"nWidgetsProducedToday\": 22222 },   { \"DELAY_LOOP_TIME_IN_MSECS\"  : 200 } ] ``` **Read the engineering units** (EU) of an analog input point configured in the PAC's strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   `https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu`  The GET response will be a single JSON name-value pair such as: ```json { \"value\": 72.22 } ```      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
 *
 * The version of the OpenAPI document: R1.0a
 * Contact: developer@opto22.com
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
 * StrategyResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:29.356996-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StrategyResponse {
  public static final String SERIALIZED_NAME_CRC = "crc";
  @SerializedName(SERIALIZED_NAME_CRC)
  private String crc;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_RUNNING_CHARTS = "runningCharts";
  @SerializedName(SERIALIZED_NAME_RUNNING_CHARTS)
  private Integer runningCharts;

  public static final String SERIALIZED_NAME_STRATEGY_NAME = "strategyName";
  @SerializedName(SERIALIZED_NAME_STRATEGY_NAME)
  private String strategyName;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private String time;

  public StrategyResponse() {
  }

  public StrategyResponse crc(String crc) {
    this.crc = crc;
    return this;
  }

  /**
   * Get crc
   * @return crc
   */
  @javax.annotation.Nullable
  public String getCrc() {
    return crc;
  }

  public void setCrc(String crc) {
    this.crc = crc;
  }


  public StrategyResponse date(String date) {
    this.date = date;
    return this;
  }

  /**
   * Get date
   * @return date
   */
  @javax.annotation.Nullable
  public String getDate() {
    return date;
  }

  public void setDate(String date) {
    this.date = date;
  }


  public StrategyResponse runningCharts(Integer runningCharts) {
    this.runningCharts = runningCharts;
    return this;
  }

  /**
   * Get runningCharts
   * @return runningCharts
   */
  @javax.annotation.Nullable
  public Integer getRunningCharts() {
    return runningCharts;
  }

  public void setRunningCharts(Integer runningCharts) {
    this.runningCharts = runningCharts;
  }


  public StrategyResponse strategyName(String strategyName) {
    this.strategyName = strategyName;
    return this;
  }

  /**
   * Get strategyName
   * @return strategyName
   */
  @javax.annotation.Nullable
  public String getStrategyName() {
    return strategyName;
  }

  public void setStrategyName(String strategyName) {
    this.strategyName = strategyName;
  }


  public StrategyResponse time(String time) {
    this.time = time;
    return this;
  }

  /**
   * Get time
   * @return time
   */
  @javax.annotation.Nullable
  public String getTime() {
    return time;
  }

  public void setTime(String time) {
    this.time = time;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StrategyResponse strategyResponse = (StrategyResponse) o;
    return Objects.equals(this.crc, strategyResponse.crc) &&
        Objects.equals(this.date, strategyResponse.date) &&
        Objects.equals(this.runningCharts, strategyResponse.runningCharts) &&
        Objects.equals(this.strategyName, strategyResponse.strategyName) &&
        Objects.equals(this.time, strategyResponse.time);
  }

  @Override
  public int hashCode() {
    return Objects.hash(crc, date, runningCharts, strategyName, time);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StrategyResponse {\n");
    sb.append("    crc: ").append(toIndentedString(crc)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    runningCharts: ").append(toIndentedString(runningCharts)).append("\n");
    sb.append("    strategyName: ").append(toIndentedString(strategyName)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
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
    openapiFields.add("crc");
    openapiFields.add("date");
    openapiFields.add("runningCharts");
    openapiFields.add("strategyName");
    openapiFields.add("time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StrategyResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StrategyResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StrategyResponse is not found in the empty JSON string", StrategyResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StrategyResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StrategyResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("crc") != null && !jsonObj.get("crc").isJsonNull()) && !jsonObj.get("crc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `crc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("crc").toString()));
      }
      if ((jsonObj.get("date") != null && !jsonObj.get("date").isJsonNull()) && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if ((jsonObj.get("strategyName") != null && !jsonObj.get("strategyName").isJsonNull()) && !jsonObj.get("strategyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `strategyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("strategyName").toString()));
      }
      if ((jsonObj.get("time") != null && !jsonObj.get("time").isJsonNull()) && !jsonObj.get("time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StrategyResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StrategyResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StrategyResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StrategyResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<StrategyResponse>() {
           @Override
           public void write(JsonWriter out, StrategyResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StrategyResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StrategyResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StrategyResponse
   * @throws IOException if the JSON string is invalid with respect to StrategyResponse
   */
  public static StrategyResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StrategyResponse.class);
  }

  /**
   * Convert an instance of StrategyResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

