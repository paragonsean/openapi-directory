/*
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
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
 * IssueTokenRequestMetadataEncryptionsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:38.969239-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IssueTokenRequestMetadataEncryptionsInner {
  public static final String SERIALIZED_NAME_FORMAT = "format";
  @SerializedName(SERIALIZED_NAME_FORMAT)
  private String format;

  public static final String SERIALIZED_NAME_KEY = "key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_PUBKEY = "pubkey";
  @SerializedName(SERIALIZED_NAME_PUBKEY)
  private String pubkey;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public IssueTokenRequestMetadataEncryptionsInner() {
  }

  public IssueTokenRequestMetadataEncryptionsInner format(String format) {
    this.format = format;
    return this;
  }

  /**
   * key format (pem or der)
   * @return format
   */
  @javax.annotation.Nullable
  public String getFormat() {
    return format;
  }

  public void setFormat(String format) {
    this.format = format;
  }


  public IssueTokenRequestMetadataEncryptionsInner key(String key) {
    this.key = key;
    return this;
  }

  /**
   * userData key to encrypt
   * @return key
   */
  @javax.annotation.Nullable
  public String getKey() {
    return key;
  }

  public void setKey(String key) {
    this.key = key;
  }


  public IssueTokenRequestMetadataEncryptionsInner pubkey(String pubkey) {
    this.pubkey = pubkey;
    return this;
  }

  /**
   * RSA public key used for encryption
   * @return pubkey
   */
  @javax.annotation.Nullable
  public String getPubkey() {
    return pubkey;
  }

  public void setPubkey(String pubkey) {
    this.pubkey = pubkey;
  }


  public IssueTokenRequestMetadataEncryptionsInner type(String type) {
    this.type = type;
    return this;
  }

  /**
   * pkcs1 or pkcs8
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IssueTokenRequestMetadataEncryptionsInner issueTokenRequestMetadataEncryptionsInner = (IssueTokenRequestMetadataEncryptionsInner) o;
    return Objects.equals(this.format, issueTokenRequestMetadataEncryptionsInner.format) &&
        Objects.equals(this.key, issueTokenRequestMetadataEncryptionsInner.key) &&
        Objects.equals(this.pubkey, issueTokenRequestMetadataEncryptionsInner.pubkey) &&
        Objects.equals(this.type, issueTokenRequestMetadataEncryptionsInner.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(format, key, pubkey, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IssueTokenRequestMetadataEncryptionsInner {\n");
    sb.append("    format: ").append(toIndentedString(format)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    pubkey: ").append(toIndentedString(pubkey)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("key");
    openapiFields.add("pubkey");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IssueTokenRequestMetadataEncryptionsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IssueTokenRequestMetadataEncryptionsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IssueTokenRequestMetadataEncryptionsInner is not found in the empty JSON string", IssueTokenRequestMetadataEncryptionsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IssueTokenRequestMetadataEncryptionsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IssueTokenRequestMetadataEncryptionsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("format") != null && !jsonObj.get("format").isJsonNull()) && !jsonObj.get("format").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `format` to be a primitive type in the JSON string but got `%s`", jsonObj.get("format").toString()));
      }
      if ((jsonObj.get("key") != null && !jsonObj.get("key").isJsonNull()) && !jsonObj.get("key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key").toString()));
      }
      if ((jsonObj.get("pubkey") != null && !jsonObj.get("pubkey").isJsonNull()) && !jsonObj.get("pubkey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pubkey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pubkey").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IssueTokenRequestMetadataEncryptionsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IssueTokenRequestMetadataEncryptionsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IssueTokenRequestMetadataEncryptionsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IssueTokenRequestMetadataEncryptionsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<IssueTokenRequestMetadataEncryptionsInner>() {
           @Override
           public void write(JsonWriter out, IssueTokenRequestMetadataEncryptionsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IssueTokenRequestMetadataEncryptionsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IssueTokenRequestMetadataEncryptionsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IssueTokenRequestMetadataEncryptionsInner
   * @throws IOException if the JSON string is invalid with respect to IssueTokenRequestMetadataEncryptionsInner
   */
  public static IssueTokenRequestMetadataEncryptionsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IssueTokenRequestMetadataEncryptionsInner.class);
  }

  /**
   * Convert an instance of IssueTokenRequestMetadataEncryptionsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

