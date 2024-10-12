/*
 *  API Client
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
 * User resource specific properties
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:50.427441-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetPublishingUser200ResponseProperties {
  public static final String SERIALIZED_NAME_PUBLISHING_PASSWORD = "publishingPassword";
  @SerializedName(SERIALIZED_NAME_PUBLISHING_PASSWORD)
  private String publishingPassword;

  public static final String SERIALIZED_NAME_PUBLISHING_PASSWORD_HASH = "publishingPasswordHash";
  @SerializedName(SERIALIZED_NAME_PUBLISHING_PASSWORD_HASH)
  private String publishingPasswordHash;

  public static final String SERIALIZED_NAME_PUBLISHING_PASSWORD_HASH_SALT = "publishingPasswordHashSalt";
  @SerializedName(SERIALIZED_NAME_PUBLISHING_PASSWORD_HASH_SALT)
  private String publishingPasswordHashSalt;

  public static final String SERIALIZED_NAME_PUBLISHING_USER_NAME = "publishingUserName";
  @SerializedName(SERIALIZED_NAME_PUBLISHING_USER_NAME)
  private String publishingUserName;

  public static final String SERIALIZED_NAME_SCM_URI = "scmUri";
  @SerializedName(SERIALIZED_NAME_SCM_URI)
  private String scmUri;

  public GetPublishingUser200ResponseProperties() {
  }

  public GetPublishingUser200ResponseProperties publishingPassword(String publishingPassword) {
    this.publishingPassword = publishingPassword;
    return this;
  }

  /**
   * Password used for publishing.
   * @return publishingPassword
   */
  @javax.annotation.Nullable
  public String getPublishingPassword() {
    return publishingPassword;
  }

  public void setPublishingPassword(String publishingPassword) {
    this.publishingPassword = publishingPassword;
  }


  public GetPublishingUser200ResponseProperties publishingPasswordHash(String publishingPasswordHash) {
    this.publishingPasswordHash = publishingPasswordHash;
    return this;
  }

  /**
   * Password hash used for publishing.
   * @return publishingPasswordHash
   */
  @javax.annotation.Nullable
  public String getPublishingPasswordHash() {
    return publishingPasswordHash;
  }

  public void setPublishingPasswordHash(String publishingPasswordHash) {
    this.publishingPasswordHash = publishingPasswordHash;
  }


  public GetPublishingUser200ResponseProperties publishingPasswordHashSalt(String publishingPasswordHashSalt) {
    this.publishingPasswordHashSalt = publishingPasswordHashSalt;
    return this;
  }

  /**
   * Password hash salt used for publishing.
   * @return publishingPasswordHashSalt
   */
  @javax.annotation.Nullable
  public String getPublishingPasswordHashSalt() {
    return publishingPasswordHashSalt;
  }

  public void setPublishingPasswordHashSalt(String publishingPasswordHashSalt) {
    this.publishingPasswordHashSalt = publishingPasswordHashSalt;
  }


  public GetPublishingUser200ResponseProperties publishingUserName(String publishingUserName) {
    this.publishingUserName = publishingUserName;
    return this;
  }

  /**
   * Username used for publishing.
   * @return publishingUserName
   */
  @javax.annotation.Nonnull
  public String getPublishingUserName() {
    return publishingUserName;
  }

  public void setPublishingUserName(String publishingUserName) {
    this.publishingUserName = publishingUserName;
  }


  public GetPublishingUser200ResponseProperties scmUri(String scmUri) {
    this.scmUri = scmUri;
    return this;
  }

  /**
   * Url of SCM site.
   * @return scmUri
   */
  @javax.annotation.Nullable
  public String getScmUri() {
    return scmUri;
  }

  public void setScmUri(String scmUri) {
    this.scmUri = scmUri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetPublishingUser200ResponseProperties getPublishingUser200ResponseProperties = (GetPublishingUser200ResponseProperties) o;
    return Objects.equals(this.publishingPassword, getPublishingUser200ResponseProperties.publishingPassword) &&
        Objects.equals(this.publishingPasswordHash, getPublishingUser200ResponseProperties.publishingPasswordHash) &&
        Objects.equals(this.publishingPasswordHashSalt, getPublishingUser200ResponseProperties.publishingPasswordHashSalt) &&
        Objects.equals(this.publishingUserName, getPublishingUser200ResponseProperties.publishingUserName) &&
        Objects.equals(this.scmUri, getPublishingUser200ResponseProperties.scmUri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(publishingPassword, publishingPasswordHash, publishingPasswordHashSalt, publishingUserName, scmUri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetPublishingUser200ResponseProperties {\n");
    sb.append("    publishingPassword: ").append("*").append("\n");
    sb.append("    publishingPasswordHash: ").append("*").append("\n");
    sb.append("    publishingPasswordHashSalt: ").append("*").append("\n");
    sb.append("    publishingUserName: ").append(toIndentedString(publishingUserName)).append("\n");
    sb.append("    scmUri: ").append(toIndentedString(scmUri)).append("\n");
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
    openapiFields.add("publishingPassword");
    openapiFields.add("publishingPasswordHash");
    openapiFields.add("publishingPasswordHashSalt");
    openapiFields.add("publishingUserName");
    openapiFields.add("scmUri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("publishingUserName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetPublishingUser200ResponseProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetPublishingUser200ResponseProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetPublishingUser200ResponseProperties is not found in the empty JSON string", GetPublishingUser200ResponseProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetPublishingUser200ResponseProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetPublishingUser200ResponseProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetPublishingUser200ResponseProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("publishingPassword") != null && !jsonObj.get("publishingPassword").isJsonNull()) && !jsonObj.get("publishingPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publishingPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publishingPassword").toString()));
      }
      if ((jsonObj.get("publishingPasswordHash") != null && !jsonObj.get("publishingPasswordHash").isJsonNull()) && !jsonObj.get("publishingPasswordHash").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publishingPasswordHash` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publishingPasswordHash").toString()));
      }
      if ((jsonObj.get("publishingPasswordHashSalt") != null && !jsonObj.get("publishingPasswordHashSalt").isJsonNull()) && !jsonObj.get("publishingPasswordHashSalt").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publishingPasswordHashSalt` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publishingPasswordHashSalt").toString()));
      }
      if (!jsonObj.get("publishingUserName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publishingUserName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publishingUserName").toString()));
      }
      if ((jsonObj.get("scmUri") != null && !jsonObj.get("scmUri").isJsonNull()) && !jsonObj.get("scmUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scmUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scmUri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetPublishingUser200ResponseProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetPublishingUser200ResponseProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetPublishingUser200ResponseProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetPublishingUser200ResponseProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<GetPublishingUser200ResponseProperties>() {
           @Override
           public void write(JsonWriter out, GetPublishingUser200ResponseProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetPublishingUser200ResponseProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetPublishingUser200ResponseProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetPublishingUser200ResponseProperties
   * @throws IOException if the JSON string is invalid with respect to GetPublishingUser200ResponseProperties
   */
  public static GetPublishingUser200ResponseProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetPublishingUser200ResponseProperties.class);
  }

  /**
   * Convert an instance of GetPublishingUser200ResponseProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

