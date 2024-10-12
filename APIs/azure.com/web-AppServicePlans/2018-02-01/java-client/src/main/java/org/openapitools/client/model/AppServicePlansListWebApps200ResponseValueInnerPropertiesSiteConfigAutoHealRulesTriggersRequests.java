/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
 * Trigger based on total requests.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:50.309367-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests {
  public static final String SERIALIZED_NAME_COUNT = "count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Integer count;

  public static final String SERIALIZED_NAME_TIME_INTERVAL = "timeInterval";
  @SerializedName(SERIALIZED_NAME_TIME_INTERVAL)
  private String timeInterval;

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests() {
  }

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests count(Integer count) {
    this.count = count;
    return this;
  }

  /**
   * Request Count.
   * @return count
   */
  @javax.annotation.Nullable
  public Integer getCount() {
    return count;
  }

  public void setCount(Integer count) {
    this.count = count;
  }


  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests timeInterval(String timeInterval) {
    this.timeInterval = timeInterval;
    return this;
  }

  /**
   * Time interval.
   * @return timeInterval
   */
  @javax.annotation.Nullable
  public String getTimeInterval() {
    return timeInterval;
  }

  public void setTimeInterval(String timeInterval) {
    this.timeInterval = timeInterval;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests = (AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests) o;
    return Objects.equals(this.count, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.count) &&
        Objects.equals(this.timeInterval, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.timeInterval);
  }

  @Override
  public int hashCode() {
    return Objects.hash(count, timeInterval);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests {\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    timeInterval: ").append(toIndentedString(timeInterval)).append("\n");
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
    openapiFields.add("timeInterval");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests is not found in the empty JSON string", AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("timeInterval") != null && !jsonObj.get("timeInterval").isJsonNull()) && !jsonObj.get("timeInterval").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timeInterval` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timeInterval").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests>() {
           @Override
           public void write(JsonWriter out, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests
   */
  public static AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests.class);
  }

  /**
   * Convert an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

