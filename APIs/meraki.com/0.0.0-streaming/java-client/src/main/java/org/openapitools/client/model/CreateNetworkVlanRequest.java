/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
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
 * CreateNetworkVlanRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:53.186925-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateNetworkVlanRequest {
  public static final String SERIALIZED_NAME_APPLIANCE_IP = "applianceIp";
  @SerializedName(SERIALIZED_NAME_APPLIANCE_IP)
  private String applianceIp;

  public static final String SERIALIZED_NAME_GROUP_POLICY_ID = "groupPolicyId";
  @SerializedName(SERIALIZED_NAME_GROUP_POLICY_ID)
  private String groupPolicyId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SUBNET = "subnet";
  @SerializedName(SERIALIZED_NAME_SUBNET)
  private String subnet;

  public CreateNetworkVlanRequest() {
  }

  public CreateNetworkVlanRequest applianceIp(String applianceIp) {
    this.applianceIp = applianceIp;
    return this;
  }

  /**
   * The local IP of the appliance on the VLAN
   * @return applianceIp
   */
  @javax.annotation.Nonnull
  public String getApplianceIp() {
    return applianceIp;
  }

  public void setApplianceIp(String applianceIp) {
    this.applianceIp = applianceIp;
  }


  public CreateNetworkVlanRequest groupPolicyId(String groupPolicyId) {
    this.groupPolicyId = groupPolicyId;
    return this;
  }

  /**
   * The id of the desired group policy to apply to the VLAN
   * @return groupPolicyId
   */
  @javax.annotation.Nullable
  public String getGroupPolicyId() {
    return groupPolicyId;
  }

  public void setGroupPolicyId(String groupPolicyId) {
    this.groupPolicyId = groupPolicyId;
  }


  public CreateNetworkVlanRequest id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The VLAN ID of the new VLAN (must be between 1 and 4094)
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public CreateNetworkVlanRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the new VLAN
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateNetworkVlanRequest subnet(String subnet) {
    this.subnet = subnet;
    return this;
  }

  /**
   * The subnet of the VLAN
   * @return subnet
   */
  @javax.annotation.Nonnull
  public String getSubnet() {
    return subnet;
  }

  public void setSubnet(String subnet) {
    this.subnet = subnet;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateNetworkVlanRequest createNetworkVlanRequest = (CreateNetworkVlanRequest) o;
    return Objects.equals(this.applianceIp, createNetworkVlanRequest.applianceIp) &&
        Objects.equals(this.groupPolicyId, createNetworkVlanRequest.groupPolicyId) &&
        Objects.equals(this.id, createNetworkVlanRequest.id) &&
        Objects.equals(this.name, createNetworkVlanRequest.name) &&
        Objects.equals(this.subnet, createNetworkVlanRequest.subnet);
  }

  @Override
  public int hashCode() {
    return Objects.hash(applianceIp, groupPolicyId, id, name, subnet);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateNetworkVlanRequest {\n");
    sb.append("    applianceIp: ").append(toIndentedString(applianceIp)).append("\n");
    sb.append("    groupPolicyId: ").append(toIndentedString(groupPolicyId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    subnet: ").append(toIndentedString(subnet)).append("\n");
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
    openapiFields.add("applianceIp");
    openapiFields.add("groupPolicyId");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("subnet");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("applianceIp");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("subnet");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateNetworkVlanRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateNetworkVlanRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateNetworkVlanRequest is not found in the empty JSON string", CreateNetworkVlanRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateNetworkVlanRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateNetworkVlanRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateNetworkVlanRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("applianceIp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `applianceIp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("applianceIp").toString()));
      }
      if ((jsonObj.get("groupPolicyId") != null && !jsonObj.get("groupPolicyId").isJsonNull()) && !jsonObj.get("groupPolicyId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupPolicyId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupPolicyId").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("subnet").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subnet` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subnet").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateNetworkVlanRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateNetworkVlanRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateNetworkVlanRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateNetworkVlanRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateNetworkVlanRequest>() {
           @Override
           public void write(JsonWriter out, CreateNetworkVlanRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateNetworkVlanRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateNetworkVlanRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateNetworkVlanRequest
   * @throws IOException if the JSON string is invalid with respect to CreateNetworkVlanRequest
   */
  public static CreateNetworkVlanRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateNetworkVlanRequest.class);
  }

  /**
   * Convert an instance of CreateNetworkVlanRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

