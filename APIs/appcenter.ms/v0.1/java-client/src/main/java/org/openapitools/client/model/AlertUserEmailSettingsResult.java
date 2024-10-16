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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner;

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
 * Alerting Default Email Settings of the user
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AlertUserEmailSettingsResult {
  public static final String SERIALIZED_NAME_REQUEST_ID = "request_id";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private String requestId;

  public static final String SERIALIZED_NAME_E_TAG = "eTag";
  @SerializedName(SERIALIZED_NAME_E_TAG)
  private String eTag;

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_SETTINGS = "settings";
  @SerializedName(SERIALIZED_NAME_SETTINGS)
  private List<NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner> settings = new ArrayList<>();

  public static final String SERIALIZED_NAME_USER_ID = "userId";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public AlertUserEmailSettingsResult() {
  }

  public AlertUserEmailSettingsResult requestId(String requestId) {
    this.requestId = requestId;
    return this;
  }

  /**
   * Unique request identifier for tracking
   * @return requestId
   */
  @javax.annotation.Nonnull
  public String getRequestId() {
    return requestId;
  }

  public void setRequestId(String requestId) {
    this.requestId = requestId;
  }


  public AlertUserEmailSettingsResult eTag(String eTag) {
    this.eTag = eTag;
    return this;
  }

  /**
   * The ETag of the entity
   * @return eTag
   */
  @javax.annotation.Nullable
  public String geteTag() {
    return eTag;
  }

  public void seteTag(String eTag) {
    this.eTag = eTag;
  }


  public AlertUserEmailSettingsResult enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Allows to forcefully disable emails on app or user level
   * @return enabled
   */
  @javax.annotation.Nonnull
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public AlertUserEmailSettingsResult settings(List<NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner> settings) {
    this.settings = settings;
    return this;
  }

  public AlertUserEmailSettingsResult addSettingsItem(NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner settingsItem) {
    if (this.settings == null) {
      this.settings = new ArrayList<>();
    }
    this.settings.add(settingsItem);
    return this;
  }

  /**
   * The settings the user has for the app
   * @return settings
   */
  @javax.annotation.Nonnull
  public List<NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner> getSettings() {
    return settings;
  }

  public void setSettings(List<NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner> settings) {
    this.settings = settings;
  }


  public AlertUserEmailSettingsResult userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * The unique id (UUID) of the user
   * @return userId
   */
  @javax.annotation.Nullable
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AlertUserEmailSettingsResult alertUserEmailSettingsResult = (AlertUserEmailSettingsResult) o;
    return Objects.equals(this.requestId, alertUserEmailSettingsResult.requestId) &&
        Objects.equals(this.eTag, alertUserEmailSettingsResult.eTag) &&
        Objects.equals(this.enabled, alertUserEmailSettingsResult.enabled) &&
        Objects.equals(this.settings, alertUserEmailSettingsResult.settings) &&
        Objects.equals(this.userId, alertUserEmailSettingsResult.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(requestId, eTag, enabled, settings, userId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AlertUserEmailSettingsResult {\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    eTag: ").append(toIndentedString(eTag)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    settings: ").append(toIndentedString(settings)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
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
    openapiFields.add("request_id");
    openapiFields.add("eTag");
    openapiFields.add("enabled");
    openapiFields.add("settings");
    openapiFields.add("userId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("request_id");
    openapiRequiredFields.add("enabled");
    openapiRequiredFields.add("settings");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AlertUserEmailSettingsResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AlertUserEmailSettingsResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AlertUserEmailSettingsResult is not found in the empty JSON string", AlertUserEmailSettingsResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AlertUserEmailSettingsResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AlertUserEmailSettingsResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AlertUserEmailSettingsResult.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("request_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `request_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("request_id").toString()));
      }
      if ((jsonObj.get("eTag") != null && !jsonObj.get("eTag").isJsonNull()) && !jsonObj.get("eTag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eTag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eTag").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("settings").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `settings` to be an array in the JSON string but got `%s`", jsonObj.get("settings").toString()));
      }

      JsonArray jsonArraysettings = jsonObj.getAsJsonArray("settings");
      // validate the required field `settings` (array)
      for (int i = 0; i < jsonArraysettings.size(); i++) {
        NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner.validateJsonElement(jsonArraysettings.get(i));
      };
      if ((jsonObj.get("userId") != null && !jsonObj.get("userId").isJsonNull()) && !jsonObj.get("userId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AlertUserEmailSettingsResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AlertUserEmailSettingsResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AlertUserEmailSettingsResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AlertUserEmailSettingsResult.class));

       return (TypeAdapter<T>) new TypeAdapter<AlertUserEmailSettingsResult>() {
           @Override
           public void write(JsonWriter out, AlertUserEmailSettingsResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AlertUserEmailSettingsResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AlertUserEmailSettingsResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AlertUserEmailSettingsResult
   * @throws IOException if the JSON string is invalid with respect to AlertUserEmailSettingsResult
   */
  public static AlertUserEmailSettingsResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AlertUserEmailSettingsResult.class);
  }

  /**
   * Convert an instance of AlertUserEmailSettingsResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

