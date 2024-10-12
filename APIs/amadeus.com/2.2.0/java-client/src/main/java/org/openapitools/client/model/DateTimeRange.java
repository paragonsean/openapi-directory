/*
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
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
import java.time.LocalDate;
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
 * DateTimeRange
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:36.621787-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DateTimeRange {
  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private LocalDate date;

  public static final String SERIALIZED_NAME_DATE_WINDOW = "dateWindow";
  @SerializedName(SERIALIZED_NAME_DATE_WINDOW)
  private String dateWindow;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private String time;

  public static final String SERIALIZED_NAME_TIME_WINDOW = "timeWindow";
  @SerializedName(SERIALIZED_NAME_TIME_WINDOW)
  private String timeWindow;

  public DateTimeRange() {
  }

  public DateTimeRange date(LocalDate date) {
    this.date = date;
    return this;
  }

  /**
   * Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-12-25
   * @return date
   */
  @javax.annotation.Nonnull
  public LocalDate getDate() {
    return date;
  }

  public void setDate(LocalDate date) {
    this.date = date;
  }


  public DateTimeRange dateWindow(String dateWindow) {
    this.dateWindow = dateWindow;
    return this;
  }

  /**
   * Either 1, 2 or 3 extra days around the local date (IxD for +/- x days - Ex: I3D), Either 1 to 3 days after the local date (PxD for +x days - Ex: P3D), or 1 to 3 days before the local date (MxD for -x days - Ex: M3D)  Can not be combined with \&quot;originRadius\&quot; or \&quot;destinationRadius\&quot;. 
   * @return dateWindow
   */
  @javax.annotation.Nullable
  public String getDateWindow() {
    return dateWindow;
  }

  public void setDateWindow(String dateWindow) {
    this.dateWindow = dateWindow;
  }


  public DateTimeRange time(String time) {
    this.time = time;
    return this;
  }

  /**
   * Local time. hh:mm:ss format, e.g 10:30:00
   * @return time
   */
  @javax.annotation.Nullable
  public String getTime() {
    return time;
  }

  public void setTime(String time) {
    this.time = time;
  }


  public DateTimeRange timeWindow(String timeWindow) {
    this.timeWindow = timeWindow;
    return this;
  }

  /**
   * 1 to 12 hours around (both +and -) the local time. Possibly limited by the number of extra days when specified, i.e.  in some situations, it may not be used to exceed the maximum date range. [1-12]H format, e.g. 6H  Can not be combined with \&quot;originRadius\&quot; or \&quot;destinationRadius\&quot;. 
   * @return timeWindow
   */
  @javax.annotation.Nullable
  public String getTimeWindow() {
    return timeWindow;
  }

  public void setTimeWindow(String timeWindow) {
    this.timeWindow = timeWindow;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DateTimeRange dateTimeRange = (DateTimeRange) o;
    return Objects.equals(this.date, dateTimeRange.date) &&
        Objects.equals(this.dateWindow, dateTimeRange.dateWindow) &&
        Objects.equals(this.time, dateTimeRange.time) &&
        Objects.equals(this.timeWindow, dateTimeRange.timeWindow);
  }

  @Override
  public int hashCode() {
    return Objects.hash(date, dateWindow, time, timeWindow);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DateTimeRange {\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    dateWindow: ").append(toIndentedString(dateWindow)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
    sb.append("    timeWindow: ").append(toIndentedString(timeWindow)).append("\n");
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
    openapiFields.add("dateWindow");
    openapiFields.add("time");
    openapiFields.add("timeWindow");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("date");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DateTimeRange
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DateTimeRange.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DateTimeRange is not found in the empty JSON string", DateTimeRange.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DateTimeRange.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DateTimeRange` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DateTimeRange.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("dateWindow") != null && !jsonObj.get("dateWindow").isJsonNull()) && !jsonObj.get("dateWindow").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dateWindow` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dateWindow").toString()));
      }
      if ((jsonObj.get("time") != null && !jsonObj.get("time").isJsonNull()) && !jsonObj.get("time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("time").toString()));
      }
      if ((jsonObj.get("timeWindow") != null && !jsonObj.get("timeWindow").isJsonNull()) && !jsonObj.get("timeWindow").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timeWindow` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timeWindow").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DateTimeRange.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DateTimeRange' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DateTimeRange> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DateTimeRange.class));

       return (TypeAdapter<T>) new TypeAdapter<DateTimeRange>() {
           @Override
           public void write(JsonWriter out, DateTimeRange value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DateTimeRange read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DateTimeRange given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DateTimeRange
   * @throws IOException if the JSON string is invalid with respect to DateTimeRange
   */
  public static DateTimeRange fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DateTimeRange.class);
  }

  /**
   * Convert an instance of DateTimeRange to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

