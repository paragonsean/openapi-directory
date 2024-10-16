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
 * UpdateNetworkWirelessSsidIdentityPskRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkWirelessSsidIdentityPskRequest {
  public static final String SERIALIZED_NAME_GROUP_POLICY_ID = "groupPolicyId";
  @SerializedName(SERIALIZED_NAME_GROUP_POLICY_ID)
  private String groupPolicyId;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PASSPHRASE = "passphrase";
  @SerializedName(SERIALIZED_NAME_PASSPHRASE)
  private String passphrase;

  public UpdateNetworkWirelessSsidIdentityPskRequest() {
  }

  public UpdateNetworkWirelessSsidIdentityPskRequest groupPolicyId(String groupPolicyId) {
    this.groupPolicyId = groupPolicyId;
    return this;
  }

  /**
   * The group policy to be applied to clients
   * @return groupPolicyId
   */
  @javax.annotation.Nullable
  public String getGroupPolicyId() {
    return groupPolicyId;
  }

  public void setGroupPolicyId(String groupPolicyId) {
    this.groupPolicyId = groupPolicyId;
  }


  public UpdateNetworkWirelessSsidIdentityPskRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the Identity PSK
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public UpdateNetworkWirelessSsidIdentityPskRequest passphrase(String passphrase) {
    this.passphrase = passphrase;
    return this;
  }

  /**
   * The passphrase for client authentication
   * @return passphrase
   */
  @javax.annotation.Nullable
  public String getPassphrase() {
    return passphrase;
  }

  public void setPassphrase(String passphrase) {
    this.passphrase = passphrase;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkWirelessSsidIdentityPskRequest updateNetworkWirelessSsidIdentityPskRequest = (UpdateNetworkWirelessSsidIdentityPskRequest) o;
    return Objects.equals(this.groupPolicyId, updateNetworkWirelessSsidIdentityPskRequest.groupPolicyId) &&
        Objects.equals(this.name, updateNetworkWirelessSsidIdentityPskRequest.name) &&
        Objects.equals(this.passphrase, updateNetworkWirelessSsidIdentityPskRequest.passphrase);
  }

  @Override
  public int hashCode() {
    return Objects.hash(groupPolicyId, name, passphrase);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkWirelessSsidIdentityPskRequest {\n");
    sb.append("    groupPolicyId: ").append(toIndentedString(groupPolicyId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    passphrase: ").append(toIndentedString(passphrase)).append("\n");
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
    openapiFields.add("groupPolicyId");
    openapiFields.add("name");
    openapiFields.add("passphrase");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkWirelessSsidIdentityPskRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkWirelessSsidIdentityPskRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkWirelessSsidIdentityPskRequest is not found in the empty JSON string", UpdateNetworkWirelessSsidIdentityPskRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkWirelessSsidIdentityPskRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkWirelessSsidIdentityPskRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("groupPolicyId") != null && !jsonObj.get("groupPolicyId").isJsonNull()) && !jsonObj.get("groupPolicyId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupPolicyId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupPolicyId").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("passphrase") != null && !jsonObj.get("passphrase").isJsonNull()) && !jsonObj.get("passphrase").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `passphrase` to be a primitive type in the JSON string but got `%s`", jsonObj.get("passphrase").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkWirelessSsidIdentityPskRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkWirelessSsidIdentityPskRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkWirelessSsidIdentityPskRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkWirelessSsidIdentityPskRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkWirelessSsidIdentityPskRequest>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkWirelessSsidIdentityPskRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkWirelessSsidIdentityPskRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkWirelessSsidIdentityPskRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkWirelessSsidIdentityPskRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkWirelessSsidIdentityPskRequest
   */
  public static UpdateNetworkWirelessSsidIdentityPskRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkWirelessSsidIdentityPskRequest.class);
  }

  /**
   * Convert an instance of UpdateNetworkWirelessSsidIdentityPskRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

