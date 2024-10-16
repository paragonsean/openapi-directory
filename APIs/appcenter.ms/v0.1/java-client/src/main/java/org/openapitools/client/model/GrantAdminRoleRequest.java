/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
 * GrantAdminRoleRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GrantAdminRoleRequest {
  /**
   * The new admin_role
   */
  @JsonAdapter(AdminRoleEnum.Adapter.class)
  public enum AdminRoleEnum {
    SUPER_ADMIN("superAdmin"),
    
    ADMIN("admin"),
    
    DEV_OPS("devOps"),
    
    CUSTOMER_SUPPORT("customerSupport"),
    
    NOT_ADMIN("notAdmin");

    private String value;

    AdminRoleEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AdminRoleEnum fromValue(String value) {
      for (AdminRoleEnum b : AdminRoleEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AdminRoleEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AdminRoleEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AdminRoleEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AdminRoleEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AdminRoleEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ADMIN_ROLE = "admin_role";
  @SerializedName(SERIALIZED_NAME_ADMIN_ROLE)
  private AdminRoleEnum adminRole;

  public GrantAdminRoleRequest() {
  }

  public GrantAdminRoleRequest adminRole(AdminRoleEnum adminRole) {
    this.adminRole = adminRole;
    return this;
  }

  /**
   * The new admin_role
   * @return adminRole
   */
  @javax.annotation.Nonnull
  public AdminRoleEnum getAdminRole() {
    return adminRole;
  }

  public void setAdminRole(AdminRoleEnum adminRole) {
    this.adminRole = adminRole;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GrantAdminRoleRequest grantAdminRoleRequest = (GrantAdminRoleRequest) o;
    return Objects.equals(this.adminRole, grantAdminRoleRequest.adminRole);
  }

  @Override
  public int hashCode() {
    return Objects.hash(adminRole);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GrantAdminRoleRequest {\n");
    sb.append("    adminRole: ").append(toIndentedString(adminRole)).append("\n");
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
    openapiFields.add("admin_role");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("admin_role");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GrantAdminRoleRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GrantAdminRoleRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GrantAdminRoleRequest is not found in the empty JSON string", GrantAdminRoleRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GrantAdminRoleRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GrantAdminRoleRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GrantAdminRoleRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("admin_role").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `admin_role` to be a primitive type in the JSON string but got `%s`", jsonObj.get("admin_role").toString()));
      }
      // validate the required field `admin_role`
      AdminRoleEnum.validateJsonElement(jsonObj.get("admin_role"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GrantAdminRoleRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GrantAdminRoleRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GrantAdminRoleRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GrantAdminRoleRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<GrantAdminRoleRequest>() {
           @Override
           public void write(JsonWriter out, GrantAdminRoleRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GrantAdminRoleRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GrantAdminRoleRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GrantAdminRoleRequest
   * @throws IOException if the JSON string is invalid with respect to GrantAdminRoleRequest
   */
  public static GrantAdminRoleRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GrantAdminRoleRequest.class);
  }

  /**
   * Convert an instance of GrantAdminRoleRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

