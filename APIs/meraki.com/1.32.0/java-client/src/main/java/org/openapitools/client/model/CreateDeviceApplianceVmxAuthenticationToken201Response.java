/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * CreateDeviceApplianceVmxAuthenticationToken201Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateDeviceApplianceVmxAuthenticationToken201Response {
  public static final String SERIALIZED_NAME_EXPIRES_AT = "expiresAt";
  @SerializedName(SERIALIZED_NAME_EXPIRES_AT)
  private String expiresAt;

  public static final String SERIALIZED_NAME_TOKEN = "token";
  @SerializedName(SERIALIZED_NAME_TOKEN)
  private String token;

  public CreateDeviceApplianceVmxAuthenticationToken201Response() {
  }

  public CreateDeviceApplianceVmxAuthenticationToken201Response expiresAt(String expiresAt) {
    this.expiresAt = expiresAt;
    return this;
  }

  /**
   * The expiration time for the token, in ISO 8601 format
   * @return expiresAt
   */
  @javax.annotation.Nullable
  public String getExpiresAt() {
    return expiresAt;
  }

  public void setExpiresAt(String expiresAt) {
    this.expiresAt = expiresAt;
  }


  public CreateDeviceApplianceVmxAuthenticationToken201Response token(String token) {
    this.token = token;
    return this;
  }

  /**
   * The newly generated authentication token for the vMX instance
   * @return token
   */
  @javax.annotation.Nullable
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
    CreateDeviceApplianceVmxAuthenticationToken201Response createDeviceApplianceVmxAuthenticationToken201Response = (CreateDeviceApplianceVmxAuthenticationToken201Response) o;
    return Objects.equals(this.expiresAt, createDeviceApplianceVmxAuthenticationToken201Response.expiresAt) &&
        Objects.equals(this.token, createDeviceApplianceVmxAuthenticationToken201Response.token);
  }

  @Override
  public int hashCode() {
    return Objects.hash(expiresAt, token);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateDeviceApplianceVmxAuthenticationToken201Response {\n");
    sb.append("    expiresAt: ").append(toIndentedString(expiresAt)).append("\n");
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
    openapiFields.add("expiresAt");
    openapiFields.add("token");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateDeviceApplianceVmxAuthenticationToken201Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateDeviceApplianceVmxAuthenticationToken201Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateDeviceApplianceVmxAuthenticationToken201Response is not found in the empty JSON string", CreateDeviceApplianceVmxAuthenticationToken201Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateDeviceApplianceVmxAuthenticationToken201Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateDeviceApplianceVmxAuthenticationToken201Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("expiresAt") != null && !jsonObj.get("expiresAt").isJsonNull()) && !jsonObj.get("expiresAt").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `expiresAt` to be a primitive type in the JSON string but got `%s`", jsonObj.get("expiresAt").toString()));
      }
      if ((jsonObj.get("token") != null && !jsonObj.get("token").isJsonNull()) && !jsonObj.get("token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("token").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateDeviceApplianceVmxAuthenticationToken201Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateDeviceApplianceVmxAuthenticationToken201Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateDeviceApplianceVmxAuthenticationToken201Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateDeviceApplianceVmxAuthenticationToken201Response.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateDeviceApplianceVmxAuthenticationToken201Response>() {
           @Override
           public void write(JsonWriter out, CreateDeviceApplianceVmxAuthenticationToken201Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateDeviceApplianceVmxAuthenticationToken201Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateDeviceApplianceVmxAuthenticationToken201Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateDeviceApplianceVmxAuthenticationToken201Response
   * @throws IOException if the JSON string is invalid with respect to CreateDeviceApplianceVmxAuthenticationToken201Response
   */
  public static CreateDeviceApplianceVmxAuthenticationToken201Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateDeviceApplianceVmxAuthenticationToken201Response.class);
  }

  /**
   * Convert an instance of CreateDeviceApplianceVmxAuthenticationToken201Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

