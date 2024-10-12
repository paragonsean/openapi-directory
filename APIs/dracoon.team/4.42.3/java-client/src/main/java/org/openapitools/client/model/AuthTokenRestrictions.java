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
 * Auth token restrictions
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AuthTokenRestrictions {
  public static final String SERIALIZED_NAME_ACCESS_TOKEN_VALIDITY = "accessTokenValidity";
  @SerializedName(SERIALIZED_NAME_ACCESS_TOKEN_VALIDITY)
  private Integer accessTokenValidity;

  public static final String SERIALIZED_NAME_REFRESH_TOKEN_VALIDITY = "refreshTokenValidity";
  @SerializedName(SERIALIZED_NAME_REFRESH_TOKEN_VALIDITY)
  private Integer refreshTokenValidity;

  public static final String SERIALIZED_NAME_RESTRICTION_ENABLED = "restrictionEnabled";
  @SerializedName(SERIALIZED_NAME_RESTRICTION_ENABLED)
  private Boolean restrictionEnabled;

  public AuthTokenRestrictions() {
  }

  public AuthTokenRestrictions accessTokenValidity(Integer accessTokenValidity) {
    this.accessTokenValidity = accessTokenValidity;
    return this;
  }

  /**
   * &amp;#128640; Since v4.13.0  Restricted OAuth access token validity (in seconds)
   * @return accessTokenValidity
   */
  @javax.annotation.Nullable
  public Integer getAccessTokenValidity() {
    return accessTokenValidity;
  }

  public void setAccessTokenValidity(Integer accessTokenValidity) {
    this.accessTokenValidity = accessTokenValidity;
  }


  public AuthTokenRestrictions refreshTokenValidity(Integer refreshTokenValidity) {
    this.refreshTokenValidity = refreshTokenValidity;
    return this;
  }

  /**
   * &amp;#128640; Since v4.13.0  Restricted OAuth refresh token validity (in seconds)
   * @return refreshTokenValidity
   */
  @javax.annotation.Nullable
  public Integer getRefreshTokenValidity() {
    return refreshTokenValidity;
  }

  public void setRefreshTokenValidity(Integer refreshTokenValidity) {
    this.refreshTokenValidity = refreshTokenValidity;
  }


  public AuthTokenRestrictions restrictionEnabled(Boolean restrictionEnabled) {
    this.restrictionEnabled = restrictionEnabled;
    return this;
  }

  /**
   * &amp;#128640; Since v4.13.0  Defines if OAuth token restrictions are enabled
   * @return restrictionEnabled
   */
  @javax.annotation.Nullable
  public Boolean getRestrictionEnabled() {
    return restrictionEnabled;
  }

  public void setRestrictionEnabled(Boolean restrictionEnabled) {
    this.restrictionEnabled = restrictionEnabled;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AuthTokenRestrictions authTokenRestrictions = (AuthTokenRestrictions) o;
    return Objects.equals(this.accessTokenValidity, authTokenRestrictions.accessTokenValidity) &&
        Objects.equals(this.refreshTokenValidity, authTokenRestrictions.refreshTokenValidity) &&
        Objects.equals(this.restrictionEnabled, authTokenRestrictions.restrictionEnabled);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accessTokenValidity, refreshTokenValidity, restrictionEnabled);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AuthTokenRestrictions {\n");
    sb.append("    accessTokenValidity: ").append(toIndentedString(accessTokenValidity)).append("\n");
    sb.append("    refreshTokenValidity: ").append(toIndentedString(refreshTokenValidity)).append("\n");
    sb.append("    restrictionEnabled: ").append(toIndentedString(restrictionEnabled)).append("\n");
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
    openapiFields.add("accessTokenValidity");
    openapiFields.add("refreshTokenValidity");
    openapiFields.add("restrictionEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AuthTokenRestrictions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AuthTokenRestrictions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AuthTokenRestrictions is not found in the empty JSON string", AuthTokenRestrictions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AuthTokenRestrictions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AuthTokenRestrictions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AuthTokenRestrictions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AuthTokenRestrictions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AuthTokenRestrictions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AuthTokenRestrictions.class));

       return (TypeAdapter<T>) new TypeAdapter<AuthTokenRestrictions>() {
           @Override
           public void write(JsonWriter out, AuthTokenRestrictions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AuthTokenRestrictions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AuthTokenRestrictions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AuthTokenRestrictions
   * @throws IOException if the JSON string is invalid with respect to AuthTokenRestrictions
   */
  public static AuthTokenRestrictions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AuthTokenRestrictions.class);
  }

  /**
   * Convert an instance of AuthTokenRestrictions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

