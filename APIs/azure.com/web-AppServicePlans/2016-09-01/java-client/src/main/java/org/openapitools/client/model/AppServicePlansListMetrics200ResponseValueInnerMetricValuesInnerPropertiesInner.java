/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
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
 * Resource metric property.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:53.445242-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner {
  public static final String SERIALIZED_NAME_KEY = "key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner() {
  }

  public AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner key(String key) {
    this.key = key;
    return this;
  }

  /**
   * Key for resource metric property.
   * @return key
   */
  @javax.annotation.Nullable
  public String getKey() {
    return key;
  }

  public void setKey(String key) {
    this.key = key;
  }


  public AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner value(String value) {
    this.value = value;
    return this;
  }

  /**
   * Value of pair.
   * @return value
   */
  @javax.annotation.Nullable
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner appServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner = (AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner) o;
    return Objects.equals(this.key, appServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.key) &&
        Objects.equals(this.value, appServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(key, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner {\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("key");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner is not found in the empty JSON string", AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("key") != null && !jsonObj.get("key").isJsonNull()) && !jsonObj.get("key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key").toString()));
      }
      if ((jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner>() {
           @Override
           public void write(JsonWriter out, AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner
   */
  public static AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner.class);
  }

  /**
   * Convert an instance of AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

