/*
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
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
 * PointPointMinutelyPrecipitationData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:13.236583-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PointPointMinutelyPrecipitationData {
  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private OffsetDateTime date;

  public static final String SERIALIZED_NAME_PRECIPITATION = "precipitation";
  @SerializedName(SERIALIZED_NAME_PRECIPITATION)
  private BigDecimal precipitation;

  public PointPointMinutelyPrecipitationData() {
  }

  public PointPointMinutelyPrecipitationData date(OffsetDateTime date) {
    this.date = date;
    return this;
  }

  /**
   * Datetime in YYYY-MM-DDTHH:MM:SS format.
   * @return date
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDate() {
    return date;
  }

  public void setDate(OffsetDateTime date) {
    this.date = date;
  }


  public PointPointMinutelyPrecipitationData precipitation(BigDecimal precipitation) {
    this.precipitation = precipitation;
    return this;
  }

  /**
   * Minutely precipitation amount (per hour). For the startup tier, showing one value per 10 minutes. For other tiers, showing one value per each minute.  Unit: mm/h
   * @return precipitation
   */
  @javax.annotation.Nullable
  public BigDecimal getPrecipitation() {
    return precipitation;
  }

  public void setPrecipitation(BigDecimal precipitation) {
    this.precipitation = precipitation;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PointPointMinutelyPrecipitationData pointPointMinutelyPrecipitationData = (PointPointMinutelyPrecipitationData) o;
    return Objects.equals(this.date, pointPointMinutelyPrecipitationData.date) &&
        Objects.equals(this.precipitation, pointPointMinutelyPrecipitationData.precipitation);
  }

  @Override
  public int hashCode() {
    return Objects.hash(date, precipitation);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PointPointMinutelyPrecipitationData {\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    precipitation: ").append(toIndentedString(precipitation)).append("\n");
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
    openapiFields.add("date");
    openapiFields.add("precipitation");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PointPointMinutelyPrecipitationData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PointPointMinutelyPrecipitationData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PointPointMinutelyPrecipitationData is not found in the empty JSON string", PointPointMinutelyPrecipitationData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PointPointMinutelyPrecipitationData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PointPointMinutelyPrecipitationData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PointPointMinutelyPrecipitationData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PointPointMinutelyPrecipitationData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PointPointMinutelyPrecipitationData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PointPointMinutelyPrecipitationData.class));

       return (TypeAdapter<T>) new TypeAdapter<PointPointMinutelyPrecipitationData>() {
           @Override
           public void write(JsonWriter out, PointPointMinutelyPrecipitationData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PointPointMinutelyPrecipitationData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PointPointMinutelyPrecipitationData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PointPointMinutelyPrecipitationData
   * @throws IOException if the JSON string is invalid with respect to PointPointMinutelyPrecipitationData
   */
  public static PointPointMinutelyPrecipitationData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PointPointMinutelyPrecipitationData.class);
  }

  /**
   * Convert an instance of PointPointMinutelyPrecipitationData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

