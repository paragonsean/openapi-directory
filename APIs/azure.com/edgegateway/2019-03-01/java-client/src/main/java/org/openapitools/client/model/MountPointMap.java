/*
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
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
 * The share mount point.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:10.716364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MountPointMap {
  public static final String SERIALIZED_NAME_MOUNT_POINT = "mountPoint";
  @SerializedName(SERIALIZED_NAME_MOUNT_POINT)
  private String mountPoint;

  public static final String SERIALIZED_NAME_ROLE_ID = "roleId";
  @SerializedName(SERIALIZED_NAME_ROLE_ID)
  private String roleId;

  /**
   * Role type.
   */
  @JsonAdapter(RoleTypeEnum.Adapter.class)
  public enum RoleTypeEnum {
    IOT("IOT"),
    
    ASA("ASA"),
    
    FUNCTIONS("Functions"),
    
    COGNITIVE("Cognitive");

    private String value;

    RoleTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RoleTypeEnum fromValue(String value) {
      for (RoleTypeEnum b : RoleTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RoleTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RoleTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RoleTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RoleTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RoleTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ROLE_TYPE = "roleType";
  @SerializedName(SERIALIZED_NAME_ROLE_TYPE)
  private RoleTypeEnum roleType;

  public static final String SERIALIZED_NAME_SHARE_ID = "shareId";
  @SerializedName(SERIALIZED_NAME_SHARE_ID)
  private String shareId;

  public MountPointMap() {
  }

  public MountPointMap(
     String mountPoint, 
     String roleId, 
     RoleTypeEnum roleType
  ) {
    this();
    this.mountPoint = mountPoint;
    this.roleId = roleId;
    this.roleType = roleType;
  }

  /**
   * Mount point for the share.
   * @return mountPoint
   */
  @javax.annotation.Nullable
  public String getMountPoint() {
    return mountPoint;
  }



  /**
   * ID of the role to which share is mounted.
   * @return roleId
   */
  @javax.annotation.Nullable
  public String getRoleId() {
    return roleId;
  }



  /**
   * Role type.
   * @return roleType
   */
  @javax.annotation.Nullable
  public RoleTypeEnum getRoleType() {
    return roleType;
  }



  public MountPointMap shareId(String shareId) {
    this.shareId = shareId;
    return this;
  }

  /**
   * ID of the share mounted to the role VM.
   * @return shareId
   */
  @javax.annotation.Nonnull
  public String getShareId() {
    return shareId;
  }

  public void setShareId(String shareId) {
    this.shareId = shareId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MountPointMap mountPointMap = (MountPointMap) o;
    return Objects.equals(this.mountPoint, mountPointMap.mountPoint) &&
        Objects.equals(this.roleId, mountPointMap.roleId) &&
        Objects.equals(this.roleType, mountPointMap.roleType) &&
        Objects.equals(this.shareId, mountPointMap.shareId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(mountPoint, roleId, roleType, shareId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MountPointMap {\n");
    sb.append("    mountPoint: ").append(toIndentedString(mountPoint)).append("\n");
    sb.append("    roleId: ").append(toIndentedString(roleId)).append("\n");
    sb.append("    roleType: ").append(toIndentedString(roleType)).append("\n");
    sb.append("    shareId: ").append(toIndentedString(shareId)).append("\n");
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
    openapiFields.add("mountPoint");
    openapiFields.add("roleId");
    openapiFields.add("roleType");
    openapiFields.add("shareId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("shareId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MountPointMap
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MountPointMap.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MountPointMap is not found in the empty JSON string", MountPointMap.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MountPointMap.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MountPointMap` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : MountPointMap.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("mountPoint") != null && !jsonObj.get("mountPoint").isJsonNull()) && !jsonObj.get("mountPoint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mountPoint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mountPoint").toString()));
      }
      if ((jsonObj.get("roleId") != null && !jsonObj.get("roleId").isJsonNull()) && !jsonObj.get("roleId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `roleId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("roleId").toString()));
      }
      if ((jsonObj.get("roleType") != null && !jsonObj.get("roleType").isJsonNull()) && !jsonObj.get("roleType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `roleType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("roleType").toString()));
      }
      // validate the optional field `roleType`
      if (jsonObj.get("roleType") != null && !jsonObj.get("roleType").isJsonNull()) {
        RoleTypeEnum.validateJsonElement(jsonObj.get("roleType"));
      }
      if (!jsonObj.get("shareId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shareId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shareId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MountPointMap.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MountPointMap' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MountPointMap> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MountPointMap.class));

       return (TypeAdapter<T>) new TypeAdapter<MountPointMap>() {
           @Override
           public void write(JsonWriter out, MountPointMap value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MountPointMap read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MountPointMap given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MountPointMap
   * @throws IOException if the JSON string is invalid with respect to MountPointMap
   */
  public static MountPointMap fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MountPointMap.class);
  }

  /**
   * Convert an instance of MountPointMap to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

