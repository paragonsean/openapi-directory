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
 * KeyStoreConfig
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class KeyStoreConfig {
  public static final String SERIALIZED_NAME_FORMAT = "format";
  @SerializedName(SERIALIZED_NAME_FORMAT)
  private String format;

  public static final String SERIALIZED_NAME_KEY_ALIAS = "keyAlias";
  @SerializedName(SERIALIZED_NAME_KEY_ALIAS)
  private String keyAlias;

  public static final String SERIALIZED_NAME_KEY_PASSWORD = "keyPassword";
  @SerializedName(SERIALIZED_NAME_KEY_PASSWORD)
  private String keyPassword;

  public static final String SERIALIZED_NAME_REALM_ALIAS = "realmAlias";
  @SerializedName(SERIALIZED_NAME_REALM_ALIAS)
  private String realmAlias;

  public static final String SERIALIZED_NAME_REALM_CERTIFICATE = "realmCertificate";
  @SerializedName(SERIALIZED_NAME_REALM_CERTIFICATE)
  private Boolean realmCertificate;

  public static final String SERIALIZED_NAME_STORE_PASSWORD = "storePassword";
  @SerializedName(SERIALIZED_NAME_STORE_PASSWORD)
  private String storePassword;

  public KeyStoreConfig() {
  }

  public KeyStoreConfig format(String format) {
    this.format = format;
    return this;
  }

  /**
   * Get format
   * @return format
   */
  @javax.annotation.Nullable
  public String getFormat() {
    return format;
  }

  public void setFormat(String format) {
    this.format = format;
  }


  public KeyStoreConfig keyAlias(String keyAlias) {
    this.keyAlias = keyAlias;
    return this;
  }

  /**
   * Get keyAlias
   * @return keyAlias
   */
  @javax.annotation.Nullable
  public String getKeyAlias() {
    return keyAlias;
  }

  public void setKeyAlias(String keyAlias) {
    this.keyAlias = keyAlias;
  }


  public KeyStoreConfig keyPassword(String keyPassword) {
    this.keyPassword = keyPassword;
    return this;
  }

  /**
   * Get keyPassword
   * @return keyPassword
   */
  @javax.annotation.Nullable
  public String getKeyPassword() {
    return keyPassword;
  }

  public void setKeyPassword(String keyPassword) {
    this.keyPassword = keyPassword;
  }


  public KeyStoreConfig realmAlias(String realmAlias) {
    this.realmAlias = realmAlias;
    return this;
  }

  /**
   * Get realmAlias
   * @return realmAlias
   */
  @javax.annotation.Nullable
  public String getRealmAlias() {
    return realmAlias;
  }

  public void setRealmAlias(String realmAlias) {
    this.realmAlias = realmAlias;
  }


  public KeyStoreConfig realmCertificate(Boolean realmCertificate) {
    this.realmCertificate = realmCertificate;
    return this;
  }

  /**
   * Get realmCertificate
   * @return realmCertificate
   */
  @javax.annotation.Nullable
  public Boolean getRealmCertificate() {
    return realmCertificate;
  }

  public void setRealmCertificate(Boolean realmCertificate) {
    this.realmCertificate = realmCertificate;
  }


  public KeyStoreConfig storePassword(String storePassword) {
    this.storePassword = storePassword;
    return this;
  }

  /**
   * Get storePassword
   * @return storePassword
   */
  @javax.annotation.Nullable
  public String getStorePassword() {
    return storePassword;
  }

  public void setStorePassword(String storePassword) {
    this.storePassword = storePassword;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    KeyStoreConfig keyStoreConfig = (KeyStoreConfig) o;
    return Objects.equals(this.format, keyStoreConfig.format) &&
        Objects.equals(this.keyAlias, keyStoreConfig.keyAlias) &&
        Objects.equals(this.keyPassword, keyStoreConfig.keyPassword) &&
        Objects.equals(this.realmAlias, keyStoreConfig.realmAlias) &&
        Objects.equals(this.realmCertificate, keyStoreConfig.realmCertificate) &&
        Objects.equals(this.storePassword, keyStoreConfig.storePassword);
  }

  @Override
  public int hashCode() {
    return Objects.hash(format, keyAlias, keyPassword, realmAlias, realmCertificate, storePassword);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class KeyStoreConfig {\n");
    sb.append("    format: ").append(toIndentedString(format)).append("\n");
    sb.append("    keyAlias: ").append(toIndentedString(keyAlias)).append("\n");
    sb.append("    keyPassword: ").append(toIndentedString(keyPassword)).append("\n");
    sb.append("    realmAlias: ").append(toIndentedString(realmAlias)).append("\n");
    sb.append("    realmCertificate: ").append(toIndentedString(realmCertificate)).append("\n");
    sb.append("    storePassword: ").append(toIndentedString(storePassword)).append("\n");
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
    openapiFields.add("format");
    openapiFields.add("keyAlias");
    openapiFields.add("keyPassword");
    openapiFields.add("realmAlias");
    openapiFields.add("realmCertificate");
    openapiFields.add("storePassword");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to KeyStoreConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!KeyStoreConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in KeyStoreConfig is not found in the empty JSON string", KeyStoreConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!KeyStoreConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `KeyStoreConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("format") != null && !jsonObj.get("format").isJsonNull()) && !jsonObj.get("format").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `format` to be a primitive type in the JSON string but got `%s`", jsonObj.get("format").toString()));
      }
      if ((jsonObj.get("keyAlias") != null && !jsonObj.get("keyAlias").isJsonNull()) && !jsonObj.get("keyAlias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `keyAlias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("keyAlias").toString()));
      }
      if ((jsonObj.get("keyPassword") != null && !jsonObj.get("keyPassword").isJsonNull()) && !jsonObj.get("keyPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `keyPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("keyPassword").toString()));
      }
      if ((jsonObj.get("realmAlias") != null && !jsonObj.get("realmAlias").isJsonNull()) && !jsonObj.get("realmAlias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `realmAlias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("realmAlias").toString()));
      }
      if ((jsonObj.get("storePassword") != null && !jsonObj.get("storePassword").isJsonNull()) && !jsonObj.get("storePassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `storePassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("storePassword").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!KeyStoreConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'KeyStoreConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<KeyStoreConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(KeyStoreConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<KeyStoreConfig>() {
           @Override
           public void write(JsonWriter out, KeyStoreConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public KeyStoreConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of KeyStoreConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of KeyStoreConfig
   * @throws IOException if the JSON string is invalid with respect to KeyStoreConfig
   */
  public static KeyStoreConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, KeyStoreConfig.class);
  }

  /**
   * Convert an instance of KeyStoreConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

