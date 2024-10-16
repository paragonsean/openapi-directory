/*
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
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
 * A key/cert pair that will be served when a domain terminates a SSL/TLS request.  Paths should be absolute and accessible to the user running the proxy instance. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:51.953320-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CertKeyPathPair {
  public static final String SERIALIZED_NAME_CERTIFICATE_PATH = "certificate_path";
  @SerializedName(SERIALIZED_NAME_CERTIFICATE_PATH)
  private String certificatePath;

  public static final String SERIALIZED_NAME_KEY_PATH = "key_path";
  @SerializedName(SERIALIZED_NAME_KEY_PATH)
  private String keyPath;

  public CertKeyPathPair() {
  }

  public CertKeyPathPair certificatePath(String certificatePath) {
    this.certificatePath = certificatePath;
    return this;
  }

  /**
   * Path to a certificate in the PEM format for the domain. If multiple certificates need to be specified then should be contained in this file in the following order: first the primary certificate followed by any intermediary certificats. 
   * @return certificatePath
   */
  @javax.annotation.Nonnull
  public String getCertificatePath() {
    return certificatePath;
  }

  public void setCertificatePath(String certificatePath) {
    this.certificatePath = certificatePath;
  }


  public CertKeyPathPair keyPath(String keyPath) {
    this.keyPath = keyPath;
    return this;
  }

  /**
   * Path to a file with the secret key in the PEM format for the domain. 
   * @return keyPath
   */
  @javax.annotation.Nonnull
  public String getKeyPath() {
    return keyPath;
  }

  public void setKeyPath(String keyPath) {
    this.keyPath = keyPath;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CertKeyPathPair certKeyPathPair = (CertKeyPathPair) o;
    return Objects.equals(this.certificatePath, certKeyPathPair.certificatePath) &&
        Objects.equals(this.keyPath, certKeyPathPair.keyPath);
  }

  @Override
  public int hashCode() {
    return Objects.hash(certificatePath, keyPath);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CertKeyPathPair {\n");
    sb.append("    certificatePath: ").append(toIndentedString(certificatePath)).append("\n");
    sb.append("    keyPath: ").append(toIndentedString(keyPath)).append("\n");
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
    openapiFields.add("certificate_path");
    openapiFields.add("key_path");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("certificate_path");
    openapiRequiredFields.add("key_path");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CertKeyPathPair
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CertKeyPathPair.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CertKeyPathPair is not found in the empty JSON string", CertKeyPathPair.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CertKeyPathPair.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CertKeyPathPair` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CertKeyPathPair.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("certificate_path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `certificate_path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("certificate_path").toString()));
      }
      if (!jsonObj.get("key_path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key_path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key_path").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CertKeyPathPair.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CertKeyPathPair' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CertKeyPathPair> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CertKeyPathPair.class));

       return (TypeAdapter<T>) new TypeAdapter<CertKeyPathPair>() {
           @Override
           public void write(JsonWriter out, CertKeyPathPair value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CertKeyPathPair read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CertKeyPathPair given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CertKeyPathPair
   * @throws IOException if the JSON string is invalid with respect to CertKeyPathPair
   */
  public static CertKeyPathPair fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CertKeyPathPair.class);
  }

  /**
   * Convert an instance of CertKeyPathPair to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

