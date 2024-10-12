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
 * HybridConnectionKey resource specific properties
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:50.309367-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansListHybridConnectionKeys200ResponseProperties {
  public static final String SERIALIZED_NAME_SEND_KEY_NAME = "sendKeyName";
  @SerializedName(SERIALIZED_NAME_SEND_KEY_NAME)
  private String sendKeyName;

  public static final String SERIALIZED_NAME_SEND_KEY_VALUE = "sendKeyValue";
  @SerializedName(SERIALIZED_NAME_SEND_KEY_VALUE)
  private String sendKeyValue;

  public AppServicePlansListHybridConnectionKeys200ResponseProperties() {
  }

  public AppServicePlansListHybridConnectionKeys200ResponseProperties(
     String sendKeyName, 
     String sendKeyValue
  ) {
    this();
    this.sendKeyName = sendKeyName;
    this.sendKeyValue = sendKeyValue;
  }

  /**
   * The name of the send key.
   * @return sendKeyName
   */
  @javax.annotation.Nullable
  public String getSendKeyName() {
    return sendKeyName;
  }



  /**
   * The value of the send key.
   * @return sendKeyValue
   */
  @javax.annotation.Nullable
  public String getSendKeyValue() {
    return sendKeyValue;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansListHybridConnectionKeys200ResponseProperties appServicePlansListHybridConnectionKeys200ResponseProperties = (AppServicePlansListHybridConnectionKeys200ResponseProperties) o;
    return Objects.equals(this.sendKeyName, appServicePlansListHybridConnectionKeys200ResponseProperties.sendKeyName) &&
        Objects.equals(this.sendKeyValue, appServicePlansListHybridConnectionKeys200ResponseProperties.sendKeyValue);
  }

  @Override
  public int hashCode() {
    return Objects.hash(sendKeyName, sendKeyValue);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansListHybridConnectionKeys200ResponseProperties {\n");
    sb.append("    sendKeyName: ").append(toIndentedString(sendKeyName)).append("\n");
    sb.append("    sendKeyValue: ").append(toIndentedString(sendKeyValue)).append("\n");
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
    openapiFields.add("sendKeyName");
    openapiFields.add("sendKeyValue");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansListHybridConnectionKeys200ResponseProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansListHybridConnectionKeys200ResponseProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansListHybridConnectionKeys200ResponseProperties is not found in the empty JSON string", AppServicePlansListHybridConnectionKeys200ResponseProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansListHybridConnectionKeys200ResponseProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansListHybridConnectionKeys200ResponseProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("sendKeyName") != null && !jsonObj.get("sendKeyName").isJsonNull()) && !jsonObj.get("sendKeyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sendKeyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sendKeyName").toString()));
      }
      if ((jsonObj.get("sendKeyValue") != null && !jsonObj.get("sendKeyValue").isJsonNull()) && !jsonObj.get("sendKeyValue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sendKeyValue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sendKeyValue").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansListHybridConnectionKeys200ResponseProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansListHybridConnectionKeys200ResponseProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansListHybridConnectionKeys200ResponseProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansListHybridConnectionKeys200ResponseProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansListHybridConnectionKeys200ResponseProperties>() {
           @Override
           public void write(JsonWriter out, AppServicePlansListHybridConnectionKeys200ResponseProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansListHybridConnectionKeys200ResponseProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansListHybridConnectionKeys200ResponseProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansListHybridConnectionKeys200ResponseProperties
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansListHybridConnectionKeys200ResponseProperties
   */
  public static AppServicePlansListHybridConnectionKeys200ResponseProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansListHybridConnectionKeys200ResponseProperties.class);
  }

  /**
   * Convert an instance of AppServicePlansListHybridConnectionKeys200ResponseProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

