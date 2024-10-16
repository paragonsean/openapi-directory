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
 * CreateOrganizationPolicyObjectRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateOrganizationPolicyObjectRequest {
  public static final String SERIALIZED_NAME_CATEGORY = "category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private String category;

  public static final String SERIALIZED_NAME_CIDR = "cidr";
  @SerializedName(SERIALIZED_NAME_CIDR)
  private String cidr;

  public static final String SERIALIZED_NAME_FQDN = "fqdn";
  @SerializedName(SERIALIZED_NAME_FQDN)
  private String fqdn;

  public static final String SERIALIZED_NAME_GROUP_IDS = "groupIds";
  @SerializedName(SERIALIZED_NAME_GROUP_IDS)
  private List<Integer> groupIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_IP = "ip";
  @SerializedName(SERIALIZED_NAME_IP)
  private String ip;

  public static final String SERIALIZED_NAME_MASK = "mask";
  @SerializedName(SERIALIZED_NAME_MASK)
  private String mask;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public CreateOrganizationPolicyObjectRequest() {
  }

  public CreateOrganizationPolicyObjectRequest category(String category) {
    this.category = category;
    return this;
  }

  /**
   * Category of a policy object (one of: adaptivePolicy, network)
   * @return category
   */
  @javax.annotation.Nonnull
  public String getCategory() {
    return category;
  }

  public void setCategory(String category) {
    this.category = category;
  }


  public CreateOrganizationPolicyObjectRequest cidr(String cidr) {
    this.cidr = cidr;
    return this;
  }

  /**
   * CIDR Value of a policy object (e.g. 10.11.12.1/24\&quot;)
   * @return cidr
   */
  @javax.annotation.Nullable
  public String getCidr() {
    return cidr;
  }

  public void setCidr(String cidr) {
    this.cidr = cidr;
  }


  public CreateOrganizationPolicyObjectRequest fqdn(String fqdn) {
    this.fqdn = fqdn;
    return this;
  }

  /**
   * Fully qualified domain name of policy object (e.g. \&quot;example.com\&quot;)
   * @return fqdn
   */
  @javax.annotation.Nullable
  public String getFqdn() {
    return fqdn;
  }

  public void setFqdn(String fqdn) {
    this.fqdn = fqdn;
  }


  public CreateOrganizationPolicyObjectRequest groupIds(List<Integer> groupIds) {
    this.groupIds = groupIds;
    return this;
  }

  public CreateOrganizationPolicyObjectRequest addGroupIdsItem(Integer groupIdsItem) {
    if (this.groupIds == null) {
      this.groupIds = new ArrayList<>();
    }
    this.groupIds.add(groupIdsItem);
    return this;
  }

  /**
   * The IDs of policy object groups the policy object belongs to
   * @return groupIds
   */
  @javax.annotation.Nullable
  public List<Integer> getGroupIds() {
    return groupIds;
  }

  public void setGroupIds(List<Integer> groupIds) {
    this.groupIds = groupIds;
  }


  public CreateOrganizationPolicyObjectRequest ip(String ip) {
    this.ip = ip;
    return this;
  }

  /**
   * IP Address of a policy object (e.g. \&quot;1.2.3.4\&quot;)
   * @return ip
   */
  @javax.annotation.Nullable
  public String getIp() {
    return ip;
  }

  public void setIp(String ip) {
    this.ip = ip;
  }


  public CreateOrganizationPolicyObjectRequest mask(String mask) {
    this.mask = mask;
    return this;
  }

  /**
   * Mask of a policy object (e.g. \&quot;255.255.0.0\&quot;)
   * @return mask
   */
  @javax.annotation.Nullable
  public String getMask() {
    return mask;
  }

  public void setMask(String mask) {
    this.mask = mask;
  }


  public CreateOrganizationPolicyObjectRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateOrganizationPolicyObjectRequest type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Type of a policy object (one of: adaptivePolicyIpv4Cidr, cidr, fqdn, ipAndMask)
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateOrganizationPolicyObjectRequest createOrganizationPolicyObjectRequest = (CreateOrganizationPolicyObjectRequest) o;
    return Objects.equals(this.category, createOrganizationPolicyObjectRequest.category) &&
        Objects.equals(this.cidr, createOrganizationPolicyObjectRequest.cidr) &&
        Objects.equals(this.fqdn, createOrganizationPolicyObjectRequest.fqdn) &&
        Objects.equals(this.groupIds, createOrganizationPolicyObjectRequest.groupIds) &&
        Objects.equals(this.ip, createOrganizationPolicyObjectRequest.ip) &&
        Objects.equals(this.mask, createOrganizationPolicyObjectRequest.mask) &&
        Objects.equals(this.name, createOrganizationPolicyObjectRequest.name) &&
        Objects.equals(this.type, createOrganizationPolicyObjectRequest.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(category, cidr, fqdn, groupIds, ip, mask, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateOrganizationPolicyObjectRequest {\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    cidr: ").append(toIndentedString(cidr)).append("\n");
    sb.append("    fqdn: ").append(toIndentedString(fqdn)).append("\n");
    sb.append("    groupIds: ").append(toIndentedString(groupIds)).append("\n");
    sb.append("    ip: ").append(toIndentedString(ip)).append("\n");
    sb.append("    mask: ").append(toIndentedString(mask)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("category");
    openapiFields.add("cidr");
    openapiFields.add("fqdn");
    openapiFields.add("groupIds");
    openapiFields.add("ip");
    openapiFields.add("mask");
    openapiFields.add("name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("category");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateOrganizationPolicyObjectRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateOrganizationPolicyObjectRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateOrganizationPolicyObjectRequest is not found in the empty JSON string", CreateOrganizationPolicyObjectRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateOrganizationPolicyObjectRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateOrganizationPolicyObjectRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateOrganizationPolicyObjectRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("category").toString()));
      }
      if ((jsonObj.get("cidr") != null && !jsonObj.get("cidr").isJsonNull()) && !jsonObj.get("cidr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cidr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cidr").toString()));
      }
      if ((jsonObj.get("fqdn") != null && !jsonObj.get("fqdn").isJsonNull()) && !jsonObj.get("fqdn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fqdn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fqdn").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("groupIds") != null && !jsonObj.get("groupIds").isJsonNull() && !jsonObj.get("groupIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupIds` to be an array in the JSON string but got `%s`", jsonObj.get("groupIds").toString()));
      }
      if ((jsonObj.get("ip") != null && !jsonObj.get("ip").isJsonNull()) && !jsonObj.get("ip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ip").toString()));
      }
      if ((jsonObj.get("mask") != null && !jsonObj.get("mask").isJsonNull()) && !jsonObj.get("mask").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mask` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mask").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateOrganizationPolicyObjectRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateOrganizationPolicyObjectRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateOrganizationPolicyObjectRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateOrganizationPolicyObjectRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateOrganizationPolicyObjectRequest>() {
           @Override
           public void write(JsonWriter out, CreateOrganizationPolicyObjectRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateOrganizationPolicyObjectRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateOrganizationPolicyObjectRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateOrganizationPolicyObjectRequest
   * @throws IOException if the JSON string is invalid with respect to CreateOrganizationPolicyObjectRequest
   */
  public static CreateOrganizationPolicyObjectRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateOrganizationPolicyObjectRequest.class);
  }

  /**
   * Convert an instance of CreateOrganizationPolicyObjectRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

