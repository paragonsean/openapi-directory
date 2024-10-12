/*
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
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
 * Configuration for CleverCloud client
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:27.562730-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CleverSettings {
  public static final String SERIALIZED_NAME_CONSUMER_KEY = "consumerKey";
  @SerializedName(SERIALIZED_NAME_CONSUMER_KEY)
  private String consumerKey;

  public static final String SERIALIZED_NAME_CONSUMER_SECRET = "consumerSecret";
  @SerializedName(SERIALIZED_NAME_CONSUMER_SECRET)
  private String consumerSecret;

  public static final String SERIALIZED_NAME_ORGA_ID = "orgaId";
  @SerializedName(SERIALIZED_NAME_ORGA_ID)
  private String orgaId;

  public static final String SERIALIZED_NAME_SECRET = "secret";
  @SerializedName(SERIALIZED_NAME_SECRET)
  private String secret;

  public static final String SERIALIZED_NAME_TOKEN = "token";
  @SerializedName(SERIALIZED_NAME_TOKEN)
  private String token;

  public CleverSettings() {
  }

  public CleverSettings consumerKey(String consumerKey) {
    this.consumerKey = consumerKey;
    return this;
  }

  /**
   * CleverCloud consumer key
   * @return consumerKey
   */
  @javax.annotation.Nonnull
  public String getConsumerKey() {
    return consumerKey;
  }

  public void setConsumerKey(String consumerKey) {
    this.consumerKey = consumerKey;
  }


  public CleverSettings consumerSecret(String consumerSecret) {
    this.consumerSecret = consumerSecret;
    return this;
  }

  /**
   * CleverCloud consumer token
   * @return consumerSecret
   */
  @javax.annotation.Nonnull
  public String getConsumerSecret() {
    return consumerSecret;
  }

  public void setConsumerSecret(String consumerSecret) {
    this.consumerSecret = consumerSecret;
  }


  public CleverSettings orgaId(String orgaId) {
    this.orgaId = orgaId;
    return this;
  }

  /**
   * CleverCloud organization id
   * @return orgaId
   */
  @javax.annotation.Nonnull
  public String getOrgaId() {
    return orgaId;
  }

  public void setOrgaId(String orgaId) {
    this.orgaId = orgaId;
  }


  public CleverSettings secret(String secret) {
    this.secret = secret;
    return this;
  }

  /**
   * CleverCloud oauth secret
   * @return secret
   */
  @javax.annotation.Nonnull
  public String getSecret() {
    return secret;
  }

  public void setSecret(String secret) {
    this.secret = secret;
  }


  public CleverSettings token(String token) {
    this.token = token;
    return this;
  }

  /**
   * CleverCloud oauth token
   * @return token
   */
  @javax.annotation.Nonnull
  public String getToken() {
    return token;
  }

  public void setToken(String token) {
    this.token = token;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CleverSettings cleverSettings = (CleverSettings) o;
    return Objects.equals(this.consumerKey, cleverSettings.consumerKey) &&
        Objects.equals(this.consumerSecret, cleverSettings.consumerSecret) &&
        Objects.equals(this.orgaId, cleverSettings.orgaId) &&
        Objects.equals(this.secret, cleverSettings.secret) &&
        Objects.equals(this.token, cleverSettings.token);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consumerKey, consumerSecret, orgaId, secret, token);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CleverSettings {\n");
    sb.append("    consumerKey: ").append(toIndentedString(consumerKey)).append("\n");
    sb.append("    consumerSecret: ").append(toIndentedString(consumerSecret)).append("\n");
    sb.append("    orgaId: ").append(toIndentedString(orgaId)).append("\n");
    sb.append("    secret: ").append(toIndentedString(secret)).append("\n");
    sb.append("    token: ").append(toIndentedString(token)).append("\n");
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
    openapiFields.add("consumerKey");
    openapiFields.add("consumerSecret");
    openapiFields.add("orgaId");
    openapiFields.add("secret");
    openapiFields.add("token");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("consumerKey");
    openapiRequiredFields.add("consumerSecret");
    openapiRequiredFields.add("orgaId");
    openapiRequiredFields.add("secret");
    openapiRequiredFields.add("token");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CleverSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CleverSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CleverSettings is not found in the empty JSON string", CleverSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CleverSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CleverSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CleverSettings.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("consumerKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consumerKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consumerKey").toString()));
      }
      if (!jsonObj.get("consumerSecret").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consumerSecret` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consumerSecret").toString()));
      }
      if (!jsonObj.get("orgaId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orgaId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orgaId").toString()));
      }
      if (!jsonObj.get("secret").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secret` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secret").toString()));
      }
      if (!jsonObj.get("token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("token").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CleverSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CleverSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CleverSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CleverSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<CleverSettings>() {
           @Override
           public void write(JsonWriter out, CleverSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CleverSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CleverSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CleverSettings
   * @throws IOException if the JSON string is invalid with respect to CleverSettings
   */
  public static CleverSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CleverSettings.class);
  }

  /**
   * Convert an instance of CleverSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

