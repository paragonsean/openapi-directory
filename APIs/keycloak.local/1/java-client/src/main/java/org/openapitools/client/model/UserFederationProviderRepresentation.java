/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
import java.util.HashMap;
import java.util.Map;

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
 * UserFederationProviderRepresentation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UserFederationProviderRepresentation {
  public static final String SERIALIZED_NAME_CHANGED_SYNC_PERIOD = "changedSyncPeriod";
  @SerializedName(SERIALIZED_NAME_CHANGED_SYNC_PERIOD)
  private Integer changedSyncPeriod;

  public static final String SERIALIZED_NAME_CONFIG = "config";
  @SerializedName(SERIALIZED_NAME_CONFIG)
  private Map<String, Object> config = new HashMap<>();

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_FULL_SYNC_PERIOD = "fullSyncPeriod";
  @SerializedName(SERIALIZED_NAME_FULL_SYNC_PERIOD)
  private Integer fullSyncPeriod;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LAST_SYNC = "lastSync";
  @SerializedName(SERIALIZED_NAME_LAST_SYNC)
  private Integer lastSync;

  public static final String SERIALIZED_NAME_PRIORITY = "priority";
  @SerializedName(SERIALIZED_NAME_PRIORITY)
  private Integer priority;

  public static final String SERIALIZED_NAME_PROVIDER_NAME = "providerName";
  @SerializedName(SERIALIZED_NAME_PROVIDER_NAME)
  private String providerName;

  public UserFederationProviderRepresentation() {
  }

  public UserFederationProviderRepresentation changedSyncPeriod(Integer changedSyncPeriod) {
    this.changedSyncPeriod = changedSyncPeriod;
    return this;
  }

  /**
   * Get changedSyncPeriod
   * @return changedSyncPeriod
   */
  @javax.annotation.Nullable
  public Integer getChangedSyncPeriod() {
    return changedSyncPeriod;
  }

  public void setChangedSyncPeriod(Integer changedSyncPeriod) {
    this.changedSyncPeriod = changedSyncPeriod;
  }


  public UserFederationProviderRepresentation config(Map<String, Object> config) {
    this.config = config;
    return this;
  }

  public UserFederationProviderRepresentation putConfigItem(String key, Object configItem) {
    if (this.config == null) {
      this.config = new HashMap<>();
    }
    this.config.put(key, configItem);
    return this;
  }

  /**
   * Get config
   * @return config
   */
  @javax.annotation.Nullable
  public Map<String, Object> getConfig() {
    return config;
  }

  public void setConfig(Map<String, Object> config) {
    this.config = config;
  }


  public UserFederationProviderRepresentation displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * Get displayName
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public UserFederationProviderRepresentation fullSyncPeriod(Integer fullSyncPeriod) {
    this.fullSyncPeriod = fullSyncPeriod;
    return this;
  }

  /**
   * Get fullSyncPeriod
   * @return fullSyncPeriod
   */
  @javax.annotation.Nullable
  public Integer getFullSyncPeriod() {
    return fullSyncPeriod;
  }

  public void setFullSyncPeriod(Integer fullSyncPeriod) {
    this.fullSyncPeriod = fullSyncPeriod;
  }


  public UserFederationProviderRepresentation id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public UserFederationProviderRepresentation lastSync(Integer lastSync) {
    this.lastSync = lastSync;
    return this;
  }

  /**
   * Get lastSync
   * @return lastSync
   */
  @javax.annotation.Nullable
  public Integer getLastSync() {
    return lastSync;
  }

  public void setLastSync(Integer lastSync) {
    this.lastSync = lastSync;
  }


  public UserFederationProviderRepresentation priority(Integer priority) {
    this.priority = priority;
    return this;
  }

  /**
   * Get priority
   * @return priority
   */
  @javax.annotation.Nullable
  public Integer getPriority() {
    return priority;
  }

  public void setPriority(Integer priority) {
    this.priority = priority;
  }


  public UserFederationProviderRepresentation providerName(String providerName) {
    this.providerName = providerName;
    return this;
  }

  /**
   * Get providerName
   * @return providerName
   */
  @javax.annotation.Nullable
  public String getProviderName() {
    return providerName;
  }

  public void setProviderName(String providerName) {
    this.providerName = providerName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserFederationProviderRepresentation userFederationProviderRepresentation = (UserFederationProviderRepresentation) o;
    return Objects.equals(this.changedSyncPeriod, userFederationProviderRepresentation.changedSyncPeriod) &&
        Objects.equals(this.config, userFederationProviderRepresentation.config) &&
        Objects.equals(this.displayName, userFederationProviderRepresentation.displayName) &&
        Objects.equals(this.fullSyncPeriod, userFederationProviderRepresentation.fullSyncPeriod) &&
        Objects.equals(this.id, userFederationProviderRepresentation.id) &&
        Objects.equals(this.lastSync, userFederationProviderRepresentation.lastSync) &&
        Objects.equals(this.priority, userFederationProviderRepresentation.priority) &&
        Objects.equals(this.providerName, userFederationProviderRepresentation.providerName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(changedSyncPeriod, config, displayName, fullSyncPeriod, id, lastSync, priority, providerName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserFederationProviderRepresentation {\n");
    sb.append("    changedSyncPeriod: ").append(toIndentedString(changedSyncPeriod)).append("\n");
    sb.append("    config: ").append(toIndentedString(config)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    fullSyncPeriod: ").append(toIndentedString(fullSyncPeriod)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastSync: ").append(toIndentedString(lastSync)).append("\n");
    sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
    sb.append("    providerName: ").append(toIndentedString(providerName)).append("\n");
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
    openapiFields.add("changedSyncPeriod");
    openapiFields.add("config");
    openapiFields.add("displayName");
    openapiFields.add("fullSyncPeriod");
    openapiFields.add("id");
    openapiFields.add("lastSync");
    openapiFields.add("priority");
    openapiFields.add("providerName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UserFederationProviderRepresentation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserFederationProviderRepresentation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserFederationProviderRepresentation is not found in the empty JSON string", UserFederationProviderRepresentation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserFederationProviderRepresentation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserFederationProviderRepresentation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("providerName") != null && !jsonObj.get("providerName").isJsonNull()) && !jsonObj.get("providerName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `providerName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("providerName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserFederationProviderRepresentation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserFederationProviderRepresentation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserFederationProviderRepresentation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserFederationProviderRepresentation.class));

       return (TypeAdapter<T>) new TypeAdapter<UserFederationProviderRepresentation>() {
           @Override
           public void write(JsonWriter out, UserFederationProviderRepresentation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserFederationProviderRepresentation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UserFederationProviderRepresentation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UserFederationProviderRepresentation
   * @throws IOException if the JSON string is invalid with respect to UserFederationProviderRepresentation
   */
  public static UserFederationProviderRepresentation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserFederationProviderRepresentation.class);
  }

  /**
   * Convert an instance of UserFederationProviderRepresentation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

