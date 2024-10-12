/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-04-01
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
import java.util.HashMap;
import java.util.Map;
import org.openapitools.client.model.UserIdentityProperties;

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
 * Managed identity for the resource.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IdentityProperties {
  public static final String SERIALIZED_NAME_PRINCIPAL_ID = "principalId";
  @SerializedName(SERIALIZED_NAME_PRINCIPAL_ID)
  private String principalId;

  public static final String SERIALIZED_NAME_TENANT_ID = "tenantId";
  @SerializedName(SERIALIZED_NAME_TENANT_ID)
  private String tenantId;

  /**
   * The identity type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    SYSTEM_ASSIGNED("SystemAssigned"),
    
    USER_ASSIGNED("UserAssigned"),
    
    SYSTEM_ASSIGNED_USER_ASSIGNED("SystemAssigned, UserAssigned"),
    
    NONE("None");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_USER_ASSIGNED_IDENTITIES = "userAssignedIdentities";
  @SerializedName(SERIALIZED_NAME_USER_ASSIGNED_IDENTITIES)
  private Map<String, UserIdentityProperties> userAssignedIdentities = new HashMap<>();

  public IdentityProperties() {
  }

  public IdentityProperties principalId(String principalId) {
    this.principalId = principalId;
    return this;
  }

  /**
   * The principal ID of resource identity.
   * @return principalId
   */
  @javax.annotation.Nullable
  public String getPrincipalId() {
    return principalId;
  }

  public void setPrincipalId(String principalId) {
    this.principalId = principalId;
  }


  public IdentityProperties tenantId(String tenantId) {
    this.tenantId = tenantId;
    return this;
  }

  /**
   * The tenant ID of resource.
   * @return tenantId
   */
  @javax.annotation.Nullable
  public String getTenantId() {
    return tenantId;
  }

  public void setTenantId(String tenantId) {
    this.tenantId = tenantId;
  }


  public IdentityProperties type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The identity type.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public IdentityProperties userAssignedIdentities(Map<String, UserIdentityProperties> userAssignedIdentities) {
    this.userAssignedIdentities = userAssignedIdentities;
    return this;
  }

  public IdentityProperties putUserAssignedIdentitiesItem(String key, UserIdentityProperties userAssignedIdentitiesItem) {
    if (this.userAssignedIdentities == null) {
      this.userAssignedIdentities = new HashMap<>();
    }
    this.userAssignedIdentities.put(key, userAssignedIdentitiesItem);
    return this;
  }

  /**
   * The list of user identities associated with the resource. The user identity   dictionary key references will be ARM resource ids in the form:   &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/      providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;.
   * @return userAssignedIdentities
   */
  @javax.annotation.Nullable
  public Map<String, UserIdentityProperties> getUserAssignedIdentities() {
    return userAssignedIdentities;
  }

  public void setUserAssignedIdentities(Map<String, UserIdentityProperties> userAssignedIdentities) {
    this.userAssignedIdentities = userAssignedIdentities;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IdentityProperties identityProperties = (IdentityProperties) o;
    return Objects.equals(this.principalId, identityProperties.principalId) &&
        Objects.equals(this.tenantId, identityProperties.tenantId) &&
        Objects.equals(this.type, identityProperties.type) &&
        Objects.equals(this.userAssignedIdentities, identityProperties.userAssignedIdentities);
  }

  @Override
  public int hashCode() {
    return Objects.hash(principalId, tenantId, type, userAssignedIdentities);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IdentityProperties {\n");
    sb.append("    principalId: ").append(toIndentedString(principalId)).append("\n");
    sb.append("    tenantId: ").append(toIndentedString(tenantId)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    userAssignedIdentities: ").append(toIndentedString(userAssignedIdentities)).append("\n");
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
    openapiFields.add("principalId");
    openapiFields.add("tenantId");
    openapiFields.add("type");
    openapiFields.add("userAssignedIdentities");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IdentityProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IdentityProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IdentityProperties is not found in the empty JSON string", IdentityProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IdentityProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IdentityProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("principalId") != null && !jsonObj.get("principalId").isJsonNull()) && !jsonObj.get("principalId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `principalId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("principalId").toString()));
      }
      if ((jsonObj.get("tenantId") != null && !jsonObj.get("tenantId").isJsonNull()) && !jsonObj.get("tenantId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tenantId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tenantId").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IdentityProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IdentityProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IdentityProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IdentityProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<IdentityProperties>() {
           @Override
           public void write(JsonWriter out, IdentityProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IdentityProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IdentityProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IdentityProperties
   * @throws IOException if the JSON string is invalid with respect to IdentityProperties
   */
  public static IdentityProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IdentityProperties.class);
  }

  /**
   * Convert an instance of IdentityProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

