/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.UserInfo;

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
 * Webhook information
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Webhook {
  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "createdBy";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private UserInfo createdBy;

  public static final String SERIALIZED_NAME_EVENT_TYPE_NAMES = "eventTypeNames";
  @SerializedName(SERIALIZED_NAME_EVENT_TYPE_NAMES)
  private List<String> eventTypeNames = new ArrayList<>();

  public static final String SERIALIZED_NAME_EXPIRE_AT = "expireAt";
  @SerializedName(SERIALIZED_NAME_EXPIRE_AT)
  private OffsetDateTime expireAt;

  public static final String SERIALIZED_NAME_FAIL_STATUS = "failStatus";
  @SerializedName(SERIALIZED_NAME_FAIL_STATUS)
  private Integer failStatus;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_IS_ENABLED = "isEnabled";
  @SerializedName(SERIALIZED_NAME_IS_ENABLED)
  private Boolean isEnabled;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SECRET = "secret";
  @SerializedName(SERIALIZED_NAME_SECRET)
  private String secret;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updatedBy";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private UserInfo updatedBy;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public Webhook() {
  }

  public Webhook createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Creation date
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public Webhook createdBy(UserInfo createdBy) {
    this.createdBy = createdBy;
    return this;
  }

  /**
   * Get createdBy
   * @return createdBy
   */
  @javax.annotation.Nullable
  public UserInfo getCreatedBy() {
    return createdBy;
  }

  public void setCreatedBy(UserInfo createdBy) {
    this.createdBy = createdBy;
  }


  public Webhook eventTypeNames(List<String> eventTypeNames) {
    this.eventTypeNames = eventTypeNames;
    return this;
  }

  public Webhook addEventTypeNamesItem(String eventTypeNamesItem) {
    if (this.eventTypeNames == null) {
      this.eventTypeNames = new ArrayList<>();
    }
    this.eventTypeNames.add(eventTypeNamesItem);
    return this;
  }

  /**
   * List of names of event types
   * @return eventTypeNames
   */
  @javax.annotation.Nonnull
  public List<String> getEventTypeNames() {
    return eventTypeNames;
  }

  public void setEventTypeNames(List<String> eventTypeNames) {
    this.eventTypeNames = eventTypeNames;
  }


  public Webhook expireAt(OffsetDateTime expireAt) {
    this.expireAt = expireAt;
    return this;
  }

  /**
   * Expiration date / time
   * @return expireAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getExpireAt() {
    return expireAt;
  }

  public void setExpireAt(OffsetDateTime expireAt) {
    this.expireAt = expireAt;
  }


  public Webhook failStatus(Integer failStatus) {
    this.failStatus = failStatus;
    return this;
  }

  /**
   * Last HTTP status code when a webhook is disabled due to delivery failures
   * @return failStatus
   */
  @javax.annotation.Nullable
  public Integer getFailStatus() {
    return failStatus;
  }

  public void setFailStatus(Integer failStatus) {
    this.failStatus = failStatus;
  }


  public Webhook id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * ID
   * @return id
   */
  @javax.annotation.Nonnull
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public Webhook isEnabled(Boolean isEnabled) {
    this.isEnabled = isEnabled;
    return this;
  }

  /**
   * Is enabled
   * @return isEnabled
   */
  @javax.annotation.Nonnull
  public Boolean getIsEnabled() {
    return isEnabled;
  }

  public void setIsEnabled(Boolean isEnabled) {
    this.isEnabled = isEnabled;
  }


  public Webhook name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Webhook secret(String secret) {
    this.secret = secret;
    return this;
  }

  /**
   * Secret; used for event message signatures
   * @return secret
   */
  @javax.annotation.Nullable
  public String getSecret() {
    return secret;
  }

  public void setSecret(String secret) {
    this.secret = secret;
  }


  public Webhook updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Modification date
   * @return updatedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public Webhook updatedBy(UserInfo updatedBy) {
    this.updatedBy = updatedBy;
    return this;
  }

  /**
   * Get updatedBy
   * @return updatedBy
   */
  @javax.annotation.Nullable
  public UserInfo getUpdatedBy() {
    return updatedBy;
  }

  public void setUpdatedBy(UserInfo updatedBy) {
    this.updatedBy = updatedBy;
  }


  public Webhook url(String url) {
    this.url = url;
    return this;
  }

  /**
   * URL
   * @return url
   */
  @javax.annotation.Nonnull
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Webhook webhook = (Webhook) o;
    return Objects.equals(this.createdAt, webhook.createdAt) &&
        Objects.equals(this.createdBy, webhook.createdBy) &&
        Objects.equals(this.eventTypeNames, webhook.eventTypeNames) &&
        Objects.equals(this.expireAt, webhook.expireAt) &&
        Objects.equals(this.failStatus, webhook.failStatus) &&
        Objects.equals(this.id, webhook.id) &&
        Objects.equals(this.isEnabled, webhook.isEnabled) &&
        Objects.equals(this.name, webhook.name) &&
        Objects.equals(this.secret, webhook.secret) &&
        Objects.equals(this.updatedAt, webhook.updatedAt) &&
        Objects.equals(this.updatedBy, webhook.updatedBy) &&
        Objects.equals(this.url, webhook.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, createdBy, eventTypeNames, expireAt, failStatus, id, isEnabled, name, secret, updatedAt, updatedBy, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Webhook {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    eventTypeNames: ").append(toIndentedString(eventTypeNames)).append("\n");
    sb.append("    expireAt: ").append(toIndentedString(expireAt)).append("\n");
    sb.append("    failStatus: ").append(toIndentedString(failStatus)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isEnabled: ").append(toIndentedString(isEnabled)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    secret: ").append(toIndentedString(secret)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("createdAt");
    openapiFields.add("createdBy");
    openapiFields.add("eventTypeNames");
    openapiFields.add("expireAt");
    openapiFields.add("failStatus");
    openapiFields.add("id");
    openapiFields.add("isEnabled");
    openapiFields.add("name");
    openapiFields.add("secret");
    openapiFields.add("updatedAt");
    openapiFields.add("updatedBy");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("eventTypeNames");
    openapiRequiredFields.add("expireAt");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("isEnabled");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("updatedAt");
    openapiRequiredFields.add("url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Webhook
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Webhook.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Webhook is not found in the empty JSON string", Webhook.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Webhook.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Webhook` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Webhook.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `createdBy`
      if (jsonObj.get("createdBy") != null && !jsonObj.get("createdBy").isJsonNull()) {
        UserInfo.validateJsonElement(jsonObj.get("createdBy"));
      }
      // ensure the required json array is present
      if (jsonObj.get("eventTypeNames") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("eventTypeNames").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `eventTypeNames` to be an array in the JSON string but got `%s`", jsonObj.get("eventTypeNames").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("secret") != null && !jsonObj.get("secret").isJsonNull()) && !jsonObj.get("secret").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secret` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secret").toString()));
      }
      // validate the optional field `updatedBy`
      if (jsonObj.get("updatedBy") != null && !jsonObj.get("updatedBy").isJsonNull()) {
        UserInfo.validateJsonElement(jsonObj.get("updatedBy"));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Webhook.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Webhook' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Webhook> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Webhook.class));

       return (TypeAdapter<T>) new TypeAdapter<Webhook>() {
           @Override
           public void write(JsonWriter out, Webhook value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Webhook read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Webhook given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Webhook
   * @throws IOException if the JSON string is invalid with respect to Webhook
   */
  public static Webhook fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Webhook.class);
  }

  /**
   * Convert an instance of Webhook to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

