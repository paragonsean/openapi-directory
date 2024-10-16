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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CreateOrganizationSamlRoleRequestNetworksInner;
import org.openapitools.client.model.CreateOrganizationSamlRoleRequestTagsInner;

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
 * UpdateOrganizationSamlRoleRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:53.186925-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateOrganizationSamlRoleRequest {
  public static final String SERIALIZED_NAME_NETWORKS = "networks";
  @SerializedName(SERIALIZED_NAME_NETWORKS)
  private List<CreateOrganizationSamlRoleRequestNetworksInner> networks = new ArrayList<>();

  public static final String SERIALIZED_NAME_ORG_ACCESS = "orgAccess";
  @SerializedName(SERIALIZED_NAME_ORG_ACCESS)
  private String orgAccess;

  public static final String SERIALIZED_NAME_ROLE = "role";
  @SerializedName(SERIALIZED_NAME_ROLE)
  private String role;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<CreateOrganizationSamlRoleRequestTagsInner> tags = new ArrayList<>();

  public UpdateOrganizationSamlRoleRequest() {
  }

  public UpdateOrganizationSamlRoleRequest networks(List<CreateOrganizationSamlRoleRequestNetworksInner> networks) {
    this.networks = networks;
    return this;
  }

  public UpdateOrganizationSamlRoleRequest addNetworksItem(CreateOrganizationSamlRoleRequestNetworksInner networksItem) {
    if (this.networks == null) {
      this.networks = new ArrayList<>();
    }
    this.networks.add(networksItem);
    return this;
  }

  /**
   * The list of networks that the SAML administrator has privileges on
   * @return networks
   */
  @javax.annotation.Nullable
  public List<CreateOrganizationSamlRoleRequestNetworksInner> getNetworks() {
    return networks;
  }

  public void setNetworks(List<CreateOrganizationSamlRoleRequestNetworksInner> networks) {
    this.networks = networks;
  }


  public UpdateOrganizationSamlRoleRequest orgAccess(String orgAccess) {
    this.orgAccess = orgAccess;
    return this;
  }

  /**
   * The privilege of the SAML administrator on the organization
   * @return orgAccess
   */
  @javax.annotation.Nullable
  public String getOrgAccess() {
    return orgAccess;
  }

  public void setOrgAccess(String orgAccess) {
    this.orgAccess = orgAccess;
  }


  public UpdateOrganizationSamlRoleRequest role(String role) {
    this.role = role;
    return this;
  }

  /**
   * The role of the SAML administrator
   * @return role
   */
  @javax.annotation.Nullable
  public String getRole() {
    return role;
  }

  public void setRole(String role) {
    this.role = role;
  }


  public UpdateOrganizationSamlRoleRequest tags(List<CreateOrganizationSamlRoleRequestTagsInner> tags) {
    this.tags = tags;
    return this;
  }

  public UpdateOrganizationSamlRoleRequest addTagsItem(CreateOrganizationSamlRoleRequestTagsInner tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * The list of tags that the SAML administrator has privleges on
   * @return tags
   */
  @javax.annotation.Nullable
  public List<CreateOrganizationSamlRoleRequestTagsInner> getTags() {
    return tags;
  }

  public void setTags(List<CreateOrganizationSamlRoleRequestTagsInner> tags) {
    this.tags = tags;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateOrganizationSamlRoleRequest updateOrganizationSamlRoleRequest = (UpdateOrganizationSamlRoleRequest) o;
    return Objects.equals(this.networks, updateOrganizationSamlRoleRequest.networks) &&
        Objects.equals(this.orgAccess, updateOrganizationSamlRoleRequest.orgAccess) &&
        Objects.equals(this.role, updateOrganizationSamlRoleRequest.role) &&
        Objects.equals(this.tags, updateOrganizationSamlRoleRequest.tags);
  }

  @Override
  public int hashCode() {
    return Objects.hash(networks, orgAccess, role, tags);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateOrganizationSamlRoleRequest {\n");
    sb.append("    networks: ").append(toIndentedString(networks)).append("\n");
    sb.append("    orgAccess: ").append(toIndentedString(orgAccess)).append("\n");
    sb.append("    role: ").append(toIndentedString(role)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
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
    openapiFields.add("networks");
    openapiFields.add("orgAccess");
    openapiFields.add("role");
    openapiFields.add("tags");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateOrganizationSamlRoleRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateOrganizationSamlRoleRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateOrganizationSamlRoleRequest is not found in the empty JSON string", UpdateOrganizationSamlRoleRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateOrganizationSamlRoleRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateOrganizationSamlRoleRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("networks") != null && !jsonObj.get("networks").isJsonNull()) {
        JsonArray jsonArraynetworks = jsonObj.getAsJsonArray("networks");
        if (jsonArraynetworks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("networks").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `networks` to be an array in the JSON string but got `%s`", jsonObj.get("networks").toString()));
          }

          // validate the optional field `networks` (array)
          for (int i = 0; i < jsonArraynetworks.size(); i++) {
            CreateOrganizationSamlRoleRequestNetworksInner.validateJsonElement(jsonArraynetworks.get(i));
          };
        }
      }
      if ((jsonObj.get("orgAccess") != null && !jsonObj.get("orgAccess").isJsonNull()) && !jsonObj.get("orgAccess").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orgAccess` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orgAccess").toString()));
      }
      if ((jsonObj.get("role") != null && !jsonObj.get("role").isJsonNull()) && !jsonObj.get("role").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `role` to be a primitive type in the JSON string but got `%s`", jsonObj.get("role").toString()));
      }
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull()) {
        JsonArray jsonArraytags = jsonObj.getAsJsonArray("tags");
        if (jsonArraytags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
          }

          // validate the optional field `tags` (array)
          for (int i = 0; i < jsonArraytags.size(); i++) {
            CreateOrganizationSamlRoleRequestTagsInner.validateJsonElement(jsonArraytags.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateOrganizationSamlRoleRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateOrganizationSamlRoleRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateOrganizationSamlRoleRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateOrganizationSamlRoleRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateOrganizationSamlRoleRequest>() {
           @Override
           public void write(JsonWriter out, UpdateOrganizationSamlRoleRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateOrganizationSamlRoleRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateOrganizationSamlRoleRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateOrganizationSamlRoleRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateOrganizationSamlRoleRequest
   */
  public static UpdateOrganizationSamlRoleRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateOrganizationSamlRoleRequest.class);
  }

  /**
   * Convert an instance of UpdateOrganizationSamlRoleRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

