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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.GetAdministeredIdentitiesMe200ResponseAuthentication;

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
 * GetAdministeredIdentitiesMe200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetAdministeredIdentitiesMe200Response {
  public static final String SERIALIZED_NAME_AUTHENTICATION = "authentication";
  @SerializedName(SERIALIZED_NAME_AUTHENTICATION)
  private GetAdministeredIdentitiesMe200ResponseAuthentication authentication;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_LAST_USED_DASHBOARD_AT = "lastUsedDashboardAt";
  @SerializedName(SERIALIZED_NAME_LAST_USED_DASHBOARD_AT)
  private OffsetDateTime lastUsedDashboardAt;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public GetAdministeredIdentitiesMe200Response() {
  }

  public GetAdministeredIdentitiesMe200Response authentication(GetAdministeredIdentitiesMe200ResponseAuthentication authentication) {
    this.authentication = authentication;
    return this;
  }

  /**
   * Get authentication
   * @return authentication
   */
  @javax.annotation.Nullable
  public GetAdministeredIdentitiesMe200ResponseAuthentication getAuthentication() {
    return authentication;
  }

  public void setAuthentication(GetAdministeredIdentitiesMe200ResponseAuthentication authentication) {
    this.authentication = authentication;
  }


  public GetAdministeredIdentitiesMe200Response email(String email) {
    this.email = email;
    return this;
  }

  /**
   * User email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public GetAdministeredIdentitiesMe200Response lastUsedDashboardAt(OffsetDateTime lastUsedDashboardAt) {
    this.lastUsedDashboardAt = lastUsedDashboardAt;
    return this;
  }

  /**
   * Last seen active on Dashboard UI
   * @return lastUsedDashboardAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastUsedDashboardAt() {
    return lastUsedDashboardAt;
  }

  public void setLastUsedDashboardAt(OffsetDateTime lastUsedDashboardAt) {
    this.lastUsedDashboardAt = lastUsedDashboardAt;
  }


  public GetAdministeredIdentitiesMe200Response name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Username
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetAdministeredIdentitiesMe200Response getAdministeredIdentitiesMe200Response = (GetAdministeredIdentitiesMe200Response) o;
    return Objects.equals(this.authentication, getAdministeredIdentitiesMe200Response.authentication) &&
        Objects.equals(this.email, getAdministeredIdentitiesMe200Response.email) &&
        Objects.equals(this.lastUsedDashboardAt, getAdministeredIdentitiesMe200Response.lastUsedDashboardAt) &&
        Objects.equals(this.name, getAdministeredIdentitiesMe200Response.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authentication, email, lastUsedDashboardAt, name);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetAdministeredIdentitiesMe200Response {\n");
    sb.append("    authentication: ").append(toIndentedString(authentication)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    lastUsedDashboardAt: ").append(toIndentedString(lastUsedDashboardAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("authentication");
    openapiFields.add("email");
    openapiFields.add("lastUsedDashboardAt");
    openapiFields.add("name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetAdministeredIdentitiesMe200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetAdministeredIdentitiesMe200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetAdministeredIdentitiesMe200Response is not found in the empty JSON string", GetAdministeredIdentitiesMe200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetAdministeredIdentitiesMe200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetAdministeredIdentitiesMe200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `authentication`
      if (jsonObj.get("authentication") != null && !jsonObj.get("authentication").isJsonNull()) {
        GetAdministeredIdentitiesMe200ResponseAuthentication.validateJsonElement(jsonObj.get("authentication"));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetAdministeredIdentitiesMe200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetAdministeredIdentitiesMe200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetAdministeredIdentitiesMe200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetAdministeredIdentitiesMe200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetAdministeredIdentitiesMe200Response>() {
           @Override
           public void write(JsonWriter out, GetAdministeredIdentitiesMe200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetAdministeredIdentitiesMe200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetAdministeredIdentitiesMe200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetAdministeredIdentitiesMe200Response
   * @throws IOException if the JSON string is invalid with respect to GetAdministeredIdentitiesMe200Response
   */
  public static GetAdministeredIdentitiesMe200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetAdministeredIdentitiesMe200Response.class);
  }

  /**
   * Convert an instance of GetAdministeredIdentitiesMe200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

