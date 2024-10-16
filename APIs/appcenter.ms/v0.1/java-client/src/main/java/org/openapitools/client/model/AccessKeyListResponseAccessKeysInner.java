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
import java.math.BigDecimal;
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
 * AccessKeyListResponseAccessKeysInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AccessKeyListResponseAccessKeysInner {
  public static final String SERIALIZED_NAME_CREATED_BY = "createdBy";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private BigDecimal createdTime;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXPIRES = "expires";
  @SerializedName(SERIALIZED_NAME_EXPIRES)
  private BigDecimal expires;

  public static final String SERIALIZED_NAME_FRIENDLY_NAME = "friendlyName";
  @SerializedName(SERIALIZED_NAME_FRIENDLY_NAME)
  private String friendlyName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_SESSION = "isSession";
  @SerializedName(SERIALIZED_NAME_IS_SESSION)
  private Boolean isSession;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public AccessKeyListResponseAccessKeysInner() {
  }

  public AccessKeyListResponseAccessKeysInner createdBy(String createdBy) {
    this.createdBy = createdBy;
    return this;
  }

  /**
   * Account name of creator.
   * @return createdBy
   */
  @javax.annotation.Nullable
  public String getCreatedBy() {
    return createdBy;
  }

  public void setCreatedBy(String createdBy) {
    this.createdBy = createdBy;
  }


  public AccessKeyListResponseAccessKeysInner createdTime(BigDecimal createdTime) {
    this.createdTime = createdTime;
    return this;
  }

  /**
   * Created time of access key
   * @return createdTime
   */
  @javax.annotation.Nullable
  public BigDecimal getCreatedTime() {
    return createdTime;
  }

  public void setCreatedTime(BigDecimal createdTime) {
    this.createdTime = createdTime;
  }


  public AccessKeyListResponseAccessKeysInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description of access key
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AccessKeyListResponseAccessKeysInner expires(BigDecimal expires) {
    this.expires = expires;
    return this;
  }

  /**
   * Time of expiry of access key
   * @return expires
   */
  @javax.annotation.Nullable
  public BigDecimal getExpires() {
    return expires;
  }

  public void setExpires(BigDecimal expires) {
    this.expires = expires;
  }


  public AccessKeyListResponseAccessKeysInner friendlyName(String friendlyName) {
    this.friendlyName = friendlyName;
    return this;
  }

  /**
   * Friendly name of access key
   * @return friendlyName
   */
  @javax.annotation.Nullable
  public String getFriendlyName() {
    return friendlyName;
  }

  public void setFriendlyName(String friendlyName) {
    this.friendlyName = friendlyName;
  }


  public AccessKeyListResponseAccessKeysInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Id of accessKey
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public AccessKeyListResponseAccessKeysInner isSession(Boolean isSession) {
    this.isSession = isSession;
    return this;
  }

  /**
   * Legacy property which indicate if accessKey was created from session
   * @return isSession
   */
  @javax.annotation.Nullable
  public Boolean getIsSession() {
    return isSession;
  }

  public void setIsSession(Boolean isSession) {
    this.isSession = isSession;
  }


  public AccessKeyListResponseAccessKeysInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Key of access key
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccessKeyListResponseAccessKeysInner accessKeyListResponseAccessKeysInner = (AccessKeyListResponseAccessKeysInner) o;
    return Objects.equals(this.createdBy, accessKeyListResponseAccessKeysInner.createdBy) &&
        Objects.equals(this.createdTime, accessKeyListResponseAccessKeysInner.createdTime) &&
        Objects.equals(this.description, accessKeyListResponseAccessKeysInner.description) &&
        Objects.equals(this.expires, accessKeyListResponseAccessKeysInner.expires) &&
        Objects.equals(this.friendlyName, accessKeyListResponseAccessKeysInner.friendlyName) &&
        Objects.equals(this.id, accessKeyListResponseAccessKeysInner.id) &&
        Objects.equals(this.isSession, accessKeyListResponseAccessKeysInner.isSession) &&
        Objects.equals(this.name, accessKeyListResponseAccessKeysInner.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdBy, createdTime, description, expires, friendlyName, id, isSession, name);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccessKeyListResponseAccessKeysInner {\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    expires: ").append(toIndentedString(expires)).append("\n");
    sb.append("    friendlyName: ").append(toIndentedString(friendlyName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isSession: ").append(toIndentedString(isSession)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("createdBy");
    openapiFields.add("createdTime");
    openapiFields.add("description");
    openapiFields.add("expires");
    openapiFields.add("friendlyName");
    openapiFields.add("id");
    openapiFields.add("isSession");
    openapiFields.add("name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AccessKeyListResponseAccessKeysInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AccessKeyListResponseAccessKeysInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AccessKeyListResponseAccessKeysInner is not found in the empty JSON string", AccessKeyListResponseAccessKeysInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AccessKeyListResponseAccessKeysInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AccessKeyListResponseAccessKeysInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("createdBy") != null && !jsonObj.get("createdBy").isJsonNull()) && !jsonObj.get("createdBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `createdBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("createdBy").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("friendlyName") != null && !jsonObj.get("friendlyName").isJsonNull()) && !jsonObj.get("friendlyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `friendlyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("friendlyName").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AccessKeyListResponseAccessKeysInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AccessKeyListResponseAccessKeysInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AccessKeyListResponseAccessKeysInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AccessKeyListResponseAccessKeysInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AccessKeyListResponseAccessKeysInner>() {
           @Override
           public void write(JsonWriter out, AccessKeyListResponseAccessKeysInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AccessKeyListResponseAccessKeysInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AccessKeyListResponseAccessKeysInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AccessKeyListResponseAccessKeysInner
   * @throws IOException if the JSON string is invalid with respect to AccessKeyListResponseAccessKeysInner
   */
  public static AccessKeyListResponseAccessKeysInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AccessKeyListResponseAccessKeysInner.class);
  }

  /**
   * Convert an instance of AccessKeyListResponseAccessKeysInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

