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
import org.openapitools.client.model.CrashesGetAppCrashesInfo200ResponseFeatures;

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
 * AppCrashesInfo
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppCrashesInfo {
  public static final String SERIALIZED_NAME_FEATURES = "features";
  @SerializedName(SERIALIZED_NAME_FEATURES)
  private CrashesGetAppCrashesInfo200ResponseFeatures features;

  public static final String SERIALIZED_NAME_HAS_CRASHES = "has_crashes";
  @SerializedName(SERIALIZED_NAME_HAS_CRASHES)
  private Boolean hasCrashes;

  public AppCrashesInfo() {
  }

  public AppCrashesInfo features(CrashesGetAppCrashesInfo200ResponseFeatures features) {
    this.features = features;
    return this;
  }

  /**
   * Get features
   * @return features
   */
  @javax.annotation.Nonnull
  public CrashesGetAppCrashesInfo200ResponseFeatures getFeatures() {
    return features;
  }

  public void setFeatures(CrashesGetAppCrashesInfo200ResponseFeatures features) {
    this.features = features;
  }


  public AppCrashesInfo hasCrashes(Boolean hasCrashes) {
    this.hasCrashes = hasCrashes;
    return this;
  }

  /**
   * Get hasCrashes
   * @return hasCrashes
   */
  @javax.annotation.Nonnull
  public Boolean getHasCrashes() {
    return hasCrashes;
  }

  public void setHasCrashes(Boolean hasCrashes) {
    this.hasCrashes = hasCrashes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppCrashesInfo appCrashesInfo = (AppCrashesInfo) o;
    return Objects.equals(this.features, appCrashesInfo.features) &&
        Objects.equals(this.hasCrashes, appCrashesInfo.hasCrashes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(features, hasCrashes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppCrashesInfo {\n");
    sb.append("    features: ").append(toIndentedString(features)).append("\n");
    sb.append("    hasCrashes: ").append(toIndentedString(hasCrashes)).append("\n");
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
    openapiFields.add("features");
    openapiFields.add("has_crashes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("features");
    openapiRequiredFields.add("has_crashes");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppCrashesInfo
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppCrashesInfo.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppCrashesInfo is not found in the empty JSON string", AppCrashesInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppCrashesInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppCrashesInfo` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AppCrashesInfo.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `features`
      CrashesGetAppCrashesInfo200ResponseFeatures.validateJsonElement(jsonObj.get("features"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppCrashesInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppCrashesInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppCrashesInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppCrashesInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<AppCrashesInfo>() {
           @Override
           public void write(JsonWriter out, AppCrashesInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppCrashesInfo read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppCrashesInfo given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppCrashesInfo
   * @throws IOException if the JSON string is invalid with respect to AppCrashesInfo
   */
  public static AppCrashesInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppCrashesInfo.class);
  }

  /**
   * Convert an instance of AppCrashesInfo to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

