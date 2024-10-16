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
 * CreateNetworkWirelessSsidIdentityPskRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateNetworkWirelessSsidIdentityPskRequest {
  public static final String SERIALIZED_NAME_GROUP_POLICY_ID = "groupPolicyId";
  @SerializedName(SERIALIZED_NAME_GROUP_POLICY_ID)
  private String groupPolicyId;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PASSPHRASE = "passphrase";
  @SerializedName(SERIALIZED_NAME_PASSPHRASE)
  private String passphrase;

  public CreateNetworkWirelessSsidIdentityPskRequest() {
  }

  public CreateNetworkWirelessSsidIdentityPskRequest groupPolicyId(String groupPolicyId) {
    this.groupPolicyId = groupPolicyId;
    return this;
  }

  /**
   * The group policy to be applied to clients
   * @return groupPolicyId
   */
  @javax.annotation.Nonnull
  public String getGroupPolicyId() {
    return groupPolicyId;
  }

  public void setGroupPolicyId(String groupPolicyId) {
    this.groupPolicyId = groupPolicyId;
  }


  public CreateNetworkWirelessSsidIdentityPskRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the Identity PSK
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateNetworkWirelessSsidIdentityPskRequest passphrase(String passphrase) {
    this.passphrase = passphrase;
    return this;
  }

  /**
   * The passphrase for client authentication. If left blank, one will be auto-generated.
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
    CreateNetworkWirelessSsidIdentityPskRequest createNetworkWirelessSsidIdentityPskRequest = (CreateNetworkWirelessSsidIdentityPskRequest) o;
    return Objects.equals(this.groupPolicyId, createNetworkWirelessSsidIdentityPskRequest.groupPolicyId) &&
        Objects.equals(this.name, createNetworkWirelessSsidIdentityPskRequest.name) &&
        Objects.equals(this.passphrase, createNetworkWirelessSsidIdentityPskRequest.passphrase);
  }

  @Override
  public int hashCode() {
    return Objects.hash(groupPolicyId, name, passphrase);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateNetworkWirelessSsidIdentityPskRequest {\n");
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
    openapiRequiredFields.add("groupPolicyId");
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateNetworkWirelessSsidIdentityPskRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateNetworkWirelessSsidIdentityPskRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateNetworkWirelessSsidIdentityPskRequest is not found in the empty JSON string", CreateNetworkWirelessSsidIdentityPskRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateNetworkWirelessSsidIdentityPskRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateNetworkWirelessSsidIdentityPskRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateNetworkWirelessSsidIdentityPskRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("groupPolicyId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupPolicyId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupPolicyId").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
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
       if (!CreateNetworkWirelessSsidIdentityPskRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateNetworkWirelessSsidIdentityPskRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateNetworkWirelessSsidIdentityPskRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateNetworkWirelessSsidIdentityPskRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateNetworkWirelessSsidIdentityPskRequest>() {
           @Override
           public void write(JsonWriter out, CreateNetworkWirelessSsidIdentityPskRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateNetworkWirelessSsidIdentityPskRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateNetworkWirelessSsidIdentityPskRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateNetworkWirelessSsidIdentityPskRequest
   * @throws IOException if the JSON string is invalid with respect to CreateNetworkWirelessSsidIdentityPskRequest
   */
  public static CreateNetworkWirelessSsidIdentityPskRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateNetworkWirelessSsidIdentityPskRequest.class);
  }

  /**
   * Convert an instance of CreateNetworkWirelessSsidIdentityPskRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

