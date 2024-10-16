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
 * Apple credentials with username, password or service_connection_id of the stored credentials is needed.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ItunesTeamsRequest {
  public static final String SERIALIZED_NAME_COOKIE = "cookie";
  @SerializedName(SERIALIZED_NAME_COOKIE)
  private String cookie;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_SERVICE_CONNECTION_ID = "service_connection_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_CONNECTION_ID)
  private String serviceConnectionId;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public ItunesTeamsRequest() {
  }

  public ItunesTeamsRequest cookie(String cookie) {
    this.cookie = cookie;
    return this;
  }

  /**
   * The 30-day session cookie for multi-factor authentication backed accounts.
   * @return cookie
   */
  @javax.annotation.Nullable
  public String getCookie() {
    return cookie;
  }

  public void setCookie(String cookie) {
    this.cookie = cookie;
  }


  public ItunesTeamsRequest password(String password) {
    this.password = password;
    return this;
  }

  /**
   * The password for the Apple Developer account.
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public ItunesTeamsRequest serviceConnectionId(String serviceConnectionId) {
    this.serviceConnectionId = serviceConnectionId;
    return this;
  }

  /**
   * The service_connection_id of the stored Apple credentials instead of username, password.
   * @return serviceConnectionId
   */
  @javax.annotation.Nullable
  public String getServiceConnectionId() {
    return serviceConnectionId;
  }

  public void setServiceConnectionId(String serviceConnectionId) {
    this.serviceConnectionId = serviceConnectionId;
  }


  public ItunesTeamsRequest username(String username) {
    this.username = username;
    return this;
  }

  /**
   * The username for the Apple Developer account.
   * @return username
   */
  @javax.annotation.Nullable
  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ItunesTeamsRequest itunesTeamsRequest = (ItunesTeamsRequest) o;
    return Objects.equals(this.cookie, itunesTeamsRequest.cookie) &&
        Objects.equals(this.password, itunesTeamsRequest.password) &&
        Objects.equals(this.serviceConnectionId, itunesTeamsRequest.serviceConnectionId) &&
        Objects.equals(this.username, itunesTeamsRequest.username);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cookie, password, serviceConnectionId, username);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ItunesTeamsRequest {\n");
    sb.append("    cookie: ").append(toIndentedString(cookie)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    serviceConnectionId: ").append(toIndentedString(serviceConnectionId)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
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
    openapiFields.add("cookie");
    openapiFields.add("password");
    openapiFields.add("service_connection_id");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ItunesTeamsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ItunesTeamsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ItunesTeamsRequest is not found in the empty JSON string", ItunesTeamsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ItunesTeamsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ItunesTeamsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("cookie") != null && !jsonObj.get("cookie").isJsonNull()) && !jsonObj.get("cookie").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cookie` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cookie").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("service_connection_id") != null && !jsonObj.get("service_connection_id").isJsonNull()) && !jsonObj.get("service_connection_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_connection_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_connection_id").toString()));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ItunesTeamsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ItunesTeamsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ItunesTeamsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ItunesTeamsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ItunesTeamsRequest>() {
           @Override
           public void write(JsonWriter out, ItunesTeamsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ItunesTeamsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ItunesTeamsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ItunesTeamsRequest
   * @throws IOException if the JSON string is invalid with respect to ItunesTeamsRequest
   */
  public static ItunesTeamsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ItunesTeamsRequest.class);
  }

  /**
   * Convert an instance of ItunesTeamsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

