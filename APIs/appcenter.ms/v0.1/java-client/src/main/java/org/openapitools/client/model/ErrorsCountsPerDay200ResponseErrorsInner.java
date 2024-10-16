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
 * ErrorsCountsPerDay200ResponseErrorsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorsCountsPerDay200ResponseErrorsInner {
  public static final String SERIALIZED_NAME_COUNT = "count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Long count;

  public static final String SERIALIZED_NAME_DATETIME = "datetime";
  @SerializedName(SERIALIZED_NAME_DATETIME)
  private String datetime;

  public ErrorsCountsPerDay200ResponseErrorsInner() {
  }

  public ErrorsCountsPerDay200ResponseErrorsInner count(Long count) {
    this.count = count;
    return this;
  }

  /**
   * count of the object
   * @return count
   */
  @javax.annotation.Nullable
  public Long getCount() {
    return count;
  }

  public void setCount(Long count) {
    this.count = count;
  }


  public ErrorsCountsPerDay200ResponseErrorsInner datetime(String datetime) {
    this.datetime = datetime;
    return this;
  }

  /**
   * the ISO 8601 datetime
   * @return datetime
   */
  @javax.annotation.Nullable
  public String getDatetime() {
    return datetime;
  }

  public void setDatetime(String datetime) {
    this.datetime = datetime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ErrorsCountsPerDay200ResponseErrorsInner errorsCountsPerDay200ResponseErrorsInner = (ErrorsCountsPerDay200ResponseErrorsInner) o;
    return Objects.equals(this.count, errorsCountsPerDay200ResponseErrorsInner.count) &&
        Objects.equals(this.datetime, errorsCountsPerDay200ResponseErrorsInner.datetime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(count, datetime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorsCountsPerDay200ResponseErrorsInner {\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    datetime: ").append(toIndentedString(datetime)).append("\n");
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
    openapiFields.add("count");
    openapiFields.add("datetime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorsCountsPerDay200ResponseErrorsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorsCountsPerDay200ResponseErrorsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorsCountsPerDay200ResponseErrorsInner is not found in the empty JSON string", ErrorsCountsPerDay200ResponseErrorsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorsCountsPerDay200ResponseErrorsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorsCountsPerDay200ResponseErrorsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("datetime") != null && !jsonObj.get("datetime").isJsonNull()) && !jsonObj.get("datetime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `datetime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("datetime").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ErrorsCountsPerDay200ResponseErrorsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorsCountsPerDay200ResponseErrorsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorsCountsPerDay200ResponseErrorsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorsCountsPerDay200ResponseErrorsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorsCountsPerDay200ResponseErrorsInner>() {
           @Override
           public void write(JsonWriter out, ErrorsCountsPerDay200ResponseErrorsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorsCountsPerDay200ResponseErrorsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorsCountsPerDay200ResponseErrorsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorsCountsPerDay200ResponseErrorsInner
   * @throws IOException if the JSON string is invalid with respect to ErrorsCountsPerDay200ResponseErrorsInner
   */
  public static ErrorsCountsPerDay200ResponseErrorsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorsCountsPerDay200ResponseErrorsInner.class);
  }

  /**
   * Convert an instance of ErrorsCountsPerDay200ResponseErrorsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

