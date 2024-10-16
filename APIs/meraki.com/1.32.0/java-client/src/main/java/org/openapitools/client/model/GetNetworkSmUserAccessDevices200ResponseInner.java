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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GetNetworkSmUserAccessDevices200ResponseInnerTrustedAccessConnectionsInner;

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
 * GetNetworkSmUserAccessDevices200ResponseInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkSmUserAccessDevices200ResponseInner {
  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MAC = "mac";
  @SerializedName(SERIALIZED_NAME_MAC)
  private String mac;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SYSTEM_TYPE = "systemType";
  @SerializedName(SERIALIZED_NAME_SYSTEM_TYPE)
  private String systemType;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRUSTED_ACCESS_CONNECTIONS = "trustedAccessConnections";
  @SerializedName(SERIALIZED_NAME_TRUSTED_ACCESS_CONNECTIONS)
  private List<GetNetworkSmUserAccessDevices200ResponseInnerTrustedAccessConnectionsInner> trustedAccessConnections = new ArrayList<>();

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public GetNetworkSmUserAccessDevices200ResponseInner() {
  }

  public GetNetworkSmUserAccessDevices200ResponseInner email(String email) {
    this.email = email;
    return this;
  }

  /**
   * user email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public GetNetworkSmUserAccessDevices200ResponseInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * device ID
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public GetNetworkSmUserAccessDevices200ResponseInner mac(String mac) {
    this.mac = mac;
    return this;
  }

  /**
   * mac address
   * @return mac
   */
  @javax.annotation.Nullable
  public String getMac() {
    return mac;
  }

  public void setMac(String mac) {
    this.mac = mac;
  }


  public GetNetworkSmUserAccessDevices200ResponseInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * device name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public GetNetworkSmUserAccessDevices200ResponseInner systemType(String systemType) {
    this.systemType = systemType;
    return this;
  }

  /**
   * system type
   * @return systemType
   */
  @javax.annotation.Nullable
  public String getSystemType() {
    return systemType;
  }

  public void setSystemType(String systemType) {
    this.systemType = systemType;
  }


  public GetNetworkSmUserAccessDevices200ResponseInner tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public GetNetworkSmUserAccessDevices200ResponseInner addTagsItem(String tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * device tags
   * @return tags
   */
  @javax.annotation.Nullable
  public List<String> getTags() {
    return tags;
  }

  public void setTags(List<String> tags) {
    this.tags = tags;
  }


  public GetNetworkSmUserAccessDevices200ResponseInner trustedAccessConnections(List<GetNetworkSmUserAccessDevices200ResponseInnerTrustedAccessConnectionsInner> trustedAccessConnections) {
    this.trustedAccessConnections = trustedAccessConnections;
    return this;
  }

  public GetNetworkSmUserAccessDevices200ResponseInner addTrustedAccessConnectionsItem(GetNetworkSmUserAccessDevices200ResponseInnerTrustedAccessConnectionsInner trustedAccessConnectionsItem) {
    if (this.trustedAccessConnections == null) {
      this.trustedAccessConnections = new ArrayList<>();
    }
    this.trustedAccessConnections.add(trustedAccessConnectionsItem);
    return this;
  }

  /**
   * Array of trusted access configs
   * @return trustedAccessConnections
   */
  @javax.annotation.Nullable
  public List<GetNetworkSmUserAccessDevices200ResponseInnerTrustedAccessConnectionsInner> getTrustedAccessConnections() {
    return trustedAccessConnections;
  }

  public void setTrustedAccessConnections(List<GetNetworkSmUserAccessDevices200ResponseInnerTrustedAccessConnectionsInner> trustedAccessConnections) {
    this.trustedAccessConnections = trustedAccessConnections;
  }


  public GetNetworkSmUserAccessDevices200ResponseInner username(String username) {
    this.username = username;
    return this;
  }

  /**
   * username
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
    GetNetworkSmUserAccessDevices200ResponseInner getNetworkSmUserAccessDevices200ResponseInner = (GetNetworkSmUserAccessDevices200ResponseInner) o;
    return Objects.equals(this.email, getNetworkSmUserAccessDevices200ResponseInner.email) &&
        Objects.equals(this.id, getNetworkSmUserAccessDevices200ResponseInner.id) &&
        Objects.equals(this.mac, getNetworkSmUserAccessDevices200ResponseInner.mac) &&
        Objects.equals(this.name, getNetworkSmUserAccessDevices200ResponseInner.name) &&
        Objects.equals(this.systemType, getNetworkSmUserAccessDevices200ResponseInner.systemType) &&
        Objects.equals(this.tags, getNetworkSmUserAccessDevices200ResponseInner.tags) &&
        Objects.equals(this.trustedAccessConnections, getNetworkSmUserAccessDevices200ResponseInner.trustedAccessConnections) &&
        Objects.equals(this.username, getNetworkSmUserAccessDevices200ResponseInner.username);
  }

  @Override
  public int hashCode() {
    return Objects.hash(email, id, mac, name, systemType, tags, trustedAccessConnections, username);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkSmUserAccessDevices200ResponseInner {\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    mac: ").append(toIndentedString(mac)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    systemType: ").append(toIndentedString(systemType)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    trustedAccessConnections: ").append(toIndentedString(trustedAccessConnections)).append("\n");
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
    openapiFields.add("email");
    openapiFields.add("id");
    openapiFields.add("mac");
    openapiFields.add("name");
    openapiFields.add("systemType");
    openapiFields.add("tags");
    openapiFields.add("trustedAccessConnections");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkSmUserAccessDevices200ResponseInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkSmUserAccessDevices200ResponseInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkSmUserAccessDevices200ResponseInner is not found in the empty JSON string", GetNetworkSmUserAccessDevices200ResponseInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkSmUserAccessDevices200ResponseInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkSmUserAccessDevices200ResponseInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("mac") != null && !jsonObj.get("mac").isJsonNull()) && !jsonObj.get("mac").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mac` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mac").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("systemType") != null && !jsonObj.get("systemType").isJsonNull()) && !jsonObj.get("systemType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `systemType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("systemType").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if (jsonObj.get("trustedAccessConnections") != null && !jsonObj.get("trustedAccessConnections").isJsonNull()) {
        JsonArray jsonArraytrustedAccessConnections = jsonObj.getAsJsonArray("trustedAccessConnections");
        if (jsonArraytrustedAccessConnections != null) {
          // ensure the json data is an array
          if (!jsonObj.get("trustedAccessConnections").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `trustedAccessConnections` to be an array in the JSON string but got `%s`", jsonObj.get("trustedAccessConnections").toString()));
          }

          // validate the optional field `trustedAccessConnections` (array)
          for (int i = 0; i < jsonArraytrustedAccessConnections.size(); i++) {
            GetNetworkSmUserAccessDevices200ResponseInnerTrustedAccessConnectionsInner.validateJsonElement(jsonArraytrustedAccessConnections.get(i));
          };
        }
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkSmUserAccessDevices200ResponseInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkSmUserAccessDevices200ResponseInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkSmUserAccessDevices200ResponseInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkSmUserAccessDevices200ResponseInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkSmUserAccessDevices200ResponseInner>() {
           @Override
           public void write(JsonWriter out, GetNetworkSmUserAccessDevices200ResponseInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkSmUserAccessDevices200ResponseInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkSmUserAccessDevices200ResponseInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkSmUserAccessDevices200ResponseInner
   * @throws IOException if the JSON string is invalid with respect to GetNetworkSmUserAccessDevices200ResponseInner
   */
  public static GetNetworkSmUserAccessDevices200ResponseInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkSmUserAccessDevices200ResponseInner.class);
  }

  /**
   * Convert an instance of GetNetworkSmUserAccessDevices200ResponseInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

