/*
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
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
 * ServerSession
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:02.089808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerSession {
  public static final String SERIALIZED_NAME_SERVERID = "serverid";
  @SerializedName(SERIALIZED_NAME_SERVERID)
  private String serverid;

  public static final String SERIALIZED_NAME_SESSIONID = "sessionid";
  @SerializedName(SERIALIZED_NAME_SESSIONID)
  private String sessionid;

  public ServerSession() {
  }

  public ServerSession serverid(String serverid) {
    this.serverid = serverid;
    return this;
  }

  /**
   * Server Id
   * @return serverid
   */
  @javax.annotation.Nonnull
  public String getServerid() {
    return serverid;
  }

  public void setServerid(String serverid) {
    this.serverid = serverid;
  }


  public ServerSession sessionid(String sessionid) {
    this.sessionid = sessionid;
    return this;
  }

  /**
   * Base64 encoded nonce
   * @return sessionid
   */
  @javax.annotation.Nonnull
  public String getSessionid() {
    return sessionid;
  }

  public void setSessionid(String sessionid) {
    this.sessionid = sessionid;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerSession serverSession = (ServerSession) o;
    return Objects.equals(this.serverid, serverSession.serverid) &&
        Objects.equals(this.sessionid, serverSession.sessionid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(serverid, sessionid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerSession {\n");
    sb.append("    serverid: ").append(toIndentedString(serverid)).append("\n");
    sb.append("    sessionid: ").append(toIndentedString(sessionid)).append("\n");
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
    openapiFields.add("serverid");
    openapiFields.add("sessionid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("serverid");
    openapiRequiredFields.add("sessionid");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerSession
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerSession.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerSession is not found in the empty JSON string", ServerSession.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerSession.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerSession` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ServerSession.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("serverid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serverid").toString()));
      }
      if (!jsonObj.get("sessionid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sessionid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sessionid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerSession.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerSession' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerSession> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerSession.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerSession>() {
           @Override
           public void write(JsonWriter out, ServerSession value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerSession read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerSession given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerSession
   * @throws IOException if the JSON string is invalid with respect to ServerSession
   */
  public static ServerSession fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerSession.class);
  }

  /**
   * Convert an instance of ServerSession to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

