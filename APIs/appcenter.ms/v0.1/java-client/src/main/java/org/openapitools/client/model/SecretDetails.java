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
 * SecretDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SecretDetails {
  public static final String SERIALIZED_NAME_ID_TOKEN = "id_token";
  @SerializedName(SERIALIZED_NAME_ID_TOKEN)
  private String idToken;

  public static final String SERIALIZED_NAME_REFRESH_TOKEN = "refresh_token";
  @SerializedName(SERIALIZED_NAME_REFRESH_TOKEN)
  private String refreshToken;

  public static final String SERIALIZED_NAME_REFRESH_TOKEN_EXPIRY = "refresh_token_expiry";
  @SerializedName(SERIALIZED_NAME_REFRESH_TOKEN_EXPIRY)
  private String refreshTokenExpiry;

  public SecretDetails() {
  }

  public SecretDetails idToken(String idToken) {
    this.idToken = idToken;
    return this;
  }

  /**
   * the id token of user
   * @return idToken
   */
  @javax.annotation.Nullable
  public String getIdToken() {
    return idToken;
  }

  public void setIdToken(String idToken) {
    this.idToken = idToken;
  }


  public SecretDetails refreshToken(String refreshToken) {
    this.refreshToken = refreshToken;
    return this;
  }

  /**
   * the refresh token for user
   * @return refreshToken
   */
  @javax.annotation.Nullable
  public String getRefreshToken() {
    return refreshToken;
  }

  public void setRefreshToken(String refreshToken) {
    this.refreshToken = refreshToken;
  }


  public SecretDetails refreshTokenExpiry(String refreshTokenExpiry) {
    this.refreshTokenExpiry = refreshTokenExpiry;
    return this;
  }

  /**
   * the expiry of refresh token
   * @return refreshTokenExpiry
   */
  @javax.annotation.Nullable
  public String getRefreshTokenExpiry() {
    return refreshTokenExpiry;
  }

  public void setRefreshTokenExpiry(String refreshTokenExpiry) {
    this.refreshTokenExpiry = refreshTokenExpiry;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SecretDetails secretDetails = (SecretDetails) o;
    return Objects.equals(this.idToken, secretDetails.idToken) &&
        Objects.equals(this.refreshToken, secretDetails.refreshToken) &&
        Objects.equals(this.refreshTokenExpiry, secretDetails.refreshTokenExpiry);
  }

  @Override
  public int hashCode() {
    return Objects.hash(idToken, refreshToken, refreshTokenExpiry);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SecretDetails {\n");
    sb.append("    idToken: ").append(toIndentedString(idToken)).append("\n");
    sb.append("    refreshToken: ").append(toIndentedString(refreshToken)).append("\n");
    sb.append("    refreshTokenExpiry: ").append(toIndentedString(refreshTokenExpiry)).append("\n");
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
    openapiFields.add("id_token");
    openapiFields.add("refresh_token");
    openapiFields.add("refresh_token_expiry");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SecretDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SecretDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SecretDetails is not found in the empty JSON string", SecretDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SecretDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SecretDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id_token") != null && !jsonObj.get("id_token").isJsonNull()) && !jsonObj.get("id_token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id_token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id_token").toString()));
      }
      if ((jsonObj.get("refresh_token") != null && !jsonObj.get("refresh_token").isJsonNull()) && !jsonObj.get("refresh_token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `refresh_token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("refresh_token").toString()));
      }
      if ((jsonObj.get("refresh_token_expiry") != null && !jsonObj.get("refresh_token_expiry").isJsonNull()) && !jsonObj.get("refresh_token_expiry").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `refresh_token_expiry` to be a primitive type in the JSON string but got `%s`", jsonObj.get("refresh_token_expiry").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SecretDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SecretDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SecretDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SecretDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<SecretDetails>() {
           @Override
           public void write(JsonWriter out, SecretDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SecretDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SecretDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SecretDetails
   * @throws IOException if the JSON string is invalid with respect to SecretDetails
   */
  public static SecretDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SecretDetails.class);
  }

  /**
   * Convert an instance of SecretDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

