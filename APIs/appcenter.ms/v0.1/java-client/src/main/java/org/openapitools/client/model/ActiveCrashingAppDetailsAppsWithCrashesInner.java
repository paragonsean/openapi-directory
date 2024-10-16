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
 * ActiveCrashingAppDetailsAppsWithCrashesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ActiveCrashingAppDetailsAppsWithCrashesInner {
  public static final String SERIALIZED_NAME_APP_ID = "appId";
  @SerializedName(SERIALIZED_NAME_APP_ID)
  private String appId;

  public static final String SERIALIZED_NAME_APP_VERSION = "appVersion";
  @SerializedName(SERIALIZED_NAME_APP_VERSION)
  private String appVersion;

  public static final String SERIALIZED_NAME_CRASH_GROUP_ID = "crashGroupId";
  @SerializedName(SERIALIZED_NAME_CRASH_GROUP_ID)
  private String crashGroupId;

  public ActiveCrashingAppDetailsAppsWithCrashesInner() {
  }

  public ActiveCrashingAppDetailsAppsWithCrashesInner appId(String appId) {
    this.appId = appId;
    return this;
  }

  /**
   * application identifier
   * @return appId
   */
  @javax.annotation.Nullable
  public String getAppId() {
    return appId;
  }

  public void setAppId(String appId) {
    this.appId = appId;
  }


  public ActiveCrashingAppDetailsAppsWithCrashesInner appVersion(String appVersion) {
    this.appVersion = appVersion;
    return this;
  }

  /**
   * application version
   * @return appVersion
   */
  @javax.annotation.Nullable
  public String getAppVersion() {
    return appVersion;
  }

  public void setAppVersion(String appVersion) {
    this.appVersion = appVersion;
  }


  public ActiveCrashingAppDetailsAppsWithCrashesInner crashGroupId(String crashGroupId) {
    this.crashGroupId = crashGroupId;
    return this;
  }

  /**
   * crash group identifier
   * @return crashGroupId
   */
  @javax.annotation.Nullable
  public String getCrashGroupId() {
    return crashGroupId;
  }

  public void setCrashGroupId(String crashGroupId) {
    this.crashGroupId = crashGroupId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ActiveCrashingAppDetailsAppsWithCrashesInner activeCrashingAppDetailsAppsWithCrashesInner = (ActiveCrashingAppDetailsAppsWithCrashesInner) o;
    return Objects.equals(this.appId, activeCrashingAppDetailsAppsWithCrashesInner.appId) &&
        Objects.equals(this.appVersion, activeCrashingAppDetailsAppsWithCrashesInner.appVersion) &&
        Objects.equals(this.crashGroupId, activeCrashingAppDetailsAppsWithCrashesInner.crashGroupId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appId, appVersion, crashGroupId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ActiveCrashingAppDetailsAppsWithCrashesInner {\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    appVersion: ").append(toIndentedString(appVersion)).append("\n");
    sb.append("    crashGroupId: ").append(toIndentedString(crashGroupId)).append("\n");
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
    openapiFields.add("appId");
    openapiFields.add("appVersion");
    openapiFields.add("crashGroupId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ActiveCrashingAppDetailsAppsWithCrashesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ActiveCrashingAppDetailsAppsWithCrashesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ActiveCrashingAppDetailsAppsWithCrashesInner is not found in the empty JSON string", ActiveCrashingAppDetailsAppsWithCrashesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ActiveCrashingAppDetailsAppsWithCrashesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ActiveCrashingAppDetailsAppsWithCrashesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appId") != null && !jsonObj.get("appId").isJsonNull()) && !jsonObj.get("appId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appId").toString()));
      }
      if ((jsonObj.get("appVersion") != null && !jsonObj.get("appVersion").isJsonNull()) && !jsonObj.get("appVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appVersion").toString()));
      }
      if ((jsonObj.get("crashGroupId") != null && !jsonObj.get("crashGroupId").isJsonNull()) && !jsonObj.get("crashGroupId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `crashGroupId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("crashGroupId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ActiveCrashingAppDetailsAppsWithCrashesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ActiveCrashingAppDetailsAppsWithCrashesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ActiveCrashingAppDetailsAppsWithCrashesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ActiveCrashingAppDetailsAppsWithCrashesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ActiveCrashingAppDetailsAppsWithCrashesInner>() {
           @Override
           public void write(JsonWriter out, ActiveCrashingAppDetailsAppsWithCrashesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ActiveCrashingAppDetailsAppsWithCrashesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ActiveCrashingAppDetailsAppsWithCrashesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ActiveCrashingAppDetailsAppsWithCrashesInner
   * @throws IOException if the JSON string is invalid with respect to ActiveCrashingAppDetailsAppsWithCrashesInner
   */
  public static ActiveCrashingAppDetailsAppsWithCrashesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ActiveCrashingAppDetailsAppsWithCrashesInner.class);
  }

  /**
   * Convert an instance of ActiveCrashingAppDetailsAppsWithCrashesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

