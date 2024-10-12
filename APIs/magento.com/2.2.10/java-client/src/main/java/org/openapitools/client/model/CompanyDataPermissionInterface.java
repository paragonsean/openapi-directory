/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
 * Permission interface.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompanyDataPermissionInterface {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_PERMISSION = "permission";
  @SerializedName(SERIALIZED_NAME_PERMISSION)
  private String permission;

  public static final String SERIALIZED_NAME_RESOURCE_ID = "resource_id";
  @SerializedName(SERIALIZED_NAME_RESOURCE_ID)
  private String resourceId;

  public static final String SERIALIZED_NAME_ROLE_ID = "role_id";
  @SerializedName(SERIALIZED_NAME_ROLE_ID)
  private Integer roleId;

  public CompanyDataPermissionInterface() {
  }

  public CompanyDataPermissionInterface id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Id.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public CompanyDataPermissionInterface permission(String permission) {
    this.permission = permission;
    return this;
  }

  /**
   * Permission.
   * @return permission
   */
  @javax.annotation.Nonnull
  public String getPermission() {
    return permission;
  }

  public void setPermission(String permission) {
    this.permission = permission;
  }


  public CompanyDataPermissionInterface resourceId(String resourceId) {
    this.resourceId = resourceId;
    return this;
  }

  /**
   * Resource id.
   * @return resourceId
   */
  @javax.annotation.Nonnull
  public String getResourceId() {
    return resourceId;
  }

  public void setResourceId(String resourceId) {
    this.resourceId = resourceId;
  }


  public CompanyDataPermissionInterface roleId(Integer roleId) {
    this.roleId = roleId;
    return this;
  }

  /**
   * Role id.
   * @return roleId
   */
  @javax.annotation.Nullable
  public Integer getRoleId() {
    return roleId;
  }

  public void setRoleId(Integer roleId) {
    this.roleId = roleId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompanyDataPermissionInterface companyDataPermissionInterface = (CompanyDataPermissionInterface) o;
    return Objects.equals(this.id, companyDataPermissionInterface.id) &&
        Objects.equals(this.permission, companyDataPermissionInterface.permission) &&
        Objects.equals(this.resourceId, companyDataPermissionInterface.resourceId) &&
        Objects.equals(this.roleId, companyDataPermissionInterface.roleId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, permission, resourceId, roleId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompanyDataPermissionInterface {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    permission: ").append(toIndentedString(permission)).append("\n");
    sb.append("    resourceId: ").append(toIndentedString(resourceId)).append("\n");
    sb.append("    roleId: ").append(toIndentedString(roleId)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("permission");
    openapiFields.add("resource_id");
    openapiFields.add("role_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("permission");
    openapiRequiredFields.add("resource_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompanyDataPermissionInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompanyDataPermissionInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompanyDataPermissionInterface is not found in the empty JSON string", CompanyDataPermissionInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompanyDataPermissionInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompanyDataPermissionInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CompanyDataPermissionInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("permission").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `permission` to be a primitive type in the JSON string but got `%s`", jsonObj.get("permission").toString()));
      }
      if (!jsonObj.get("resource_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resource_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resource_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompanyDataPermissionInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompanyDataPermissionInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompanyDataPermissionInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompanyDataPermissionInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<CompanyDataPermissionInterface>() {
           @Override
           public void write(JsonWriter out, CompanyDataPermissionInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompanyDataPermissionInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompanyDataPermissionInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompanyDataPermissionInterface
   * @throws IOException if the JSON string is invalid with respect to CompanyDataPermissionInterface
   */
  public static CompanyDataPermissionInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompanyDataPermissionInterface.class);
  }

  /**
   * Convert an instance of CompanyDataPermissionInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

