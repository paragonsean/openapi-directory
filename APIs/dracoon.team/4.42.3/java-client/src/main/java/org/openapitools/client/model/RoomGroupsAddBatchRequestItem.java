/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
import org.openapitools.client.model.NodePermissions;

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
 * Request item model for granting group to the room
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RoomGroupsAddBatchRequestItem {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  /**
   * Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items.
   */
  @JsonAdapter(NewGroupMemberAcceptanceEnum.Adapter.class)
  public enum NewGroupMemberAcceptanceEnum {
    AUTOALLOW("autoallow"),
    
    PENDING("pending");

    private String value;

    NewGroupMemberAcceptanceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NewGroupMemberAcceptanceEnum fromValue(String value) {
      for (NewGroupMemberAcceptanceEnum b : NewGroupMemberAcceptanceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NewGroupMemberAcceptanceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NewGroupMemberAcceptanceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NewGroupMemberAcceptanceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NewGroupMemberAcceptanceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NewGroupMemberAcceptanceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NEW_GROUP_MEMBER_ACCEPTANCE = "newGroupMemberAcceptance";
  @SerializedName(SERIALIZED_NAME_NEW_GROUP_MEMBER_ACCEPTANCE)
  private NewGroupMemberAcceptanceEnum newGroupMemberAcceptance = NewGroupMemberAcceptanceEnum.AUTOALLOW;

  public static final String SERIALIZED_NAME_PERMISSIONS = "permissions";
  @SerializedName(SERIALIZED_NAME_PERMISSIONS)
  private NodePermissions permissions;

  public RoomGroupsAddBatchRequestItem() {
  }

  public RoomGroupsAddBatchRequestItem id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * Unique identifier for the group
   * @return id
   */
  @javax.annotation.Nonnull
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public RoomGroupsAddBatchRequestItem newGroupMemberAcceptance(NewGroupMemberAcceptanceEnum newGroupMemberAcceptance) {
    this.newGroupMemberAcceptance = newGroupMemberAcceptance;
    return this;
  }

  /**
   * Behaviour when new users are added to the group:  * &#x60;autoallow&#x60;  * &#x60;pending&#x60;    Only relevant if &#x60;adminGroupIds&#x60; has items.
   * @return newGroupMemberAcceptance
   */
  @javax.annotation.Nullable
  public NewGroupMemberAcceptanceEnum getNewGroupMemberAcceptance() {
    return newGroupMemberAcceptance;
  }

  public void setNewGroupMemberAcceptance(NewGroupMemberAcceptanceEnum newGroupMemberAcceptance) {
    this.newGroupMemberAcceptance = newGroupMemberAcceptance;
  }


  public RoomGroupsAddBatchRequestItem permissions(NodePermissions permissions) {
    this.permissions = permissions;
    return this;
  }

  /**
   * Get permissions
   * @return permissions
   */
  @javax.annotation.Nonnull
  public NodePermissions getPermissions() {
    return permissions;
  }

  public void setPermissions(NodePermissions permissions) {
    this.permissions = permissions;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RoomGroupsAddBatchRequestItem roomGroupsAddBatchRequestItem = (RoomGroupsAddBatchRequestItem) o;
    return Objects.equals(this.id, roomGroupsAddBatchRequestItem.id) &&
        Objects.equals(this.newGroupMemberAcceptance, roomGroupsAddBatchRequestItem.newGroupMemberAcceptance) &&
        Objects.equals(this.permissions, roomGroupsAddBatchRequestItem.permissions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, newGroupMemberAcceptance, permissions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RoomGroupsAddBatchRequestItem {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    newGroupMemberAcceptance: ").append(toIndentedString(newGroupMemberAcceptance)).append("\n");
    sb.append("    permissions: ").append(toIndentedString(permissions)).append("\n");
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
    openapiFields.add("newGroupMemberAcceptance");
    openapiFields.add("permissions");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("permissions");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RoomGroupsAddBatchRequestItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RoomGroupsAddBatchRequestItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RoomGroupsAddBatchRequestItem is not found in the empty JSON string", RoomGroupsAddBatchRequestItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RoomGroupsAddBatchRequestItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RoomGroupsAddBatchRequestItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : RoomGroupsAddBatchRequestItem.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("newGroupMemberAcceptance") != null && !jsonObj.get("newGroupMemberAcceptance").isJsonNull()) && !jsonObj.get("newGroupMemberAcceptance").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `newGroupMemberAcceptance` to be a primitive type in the JSON string but got `%s`", jsonObj.get("newGroupMemberAcceptance").toString()));
      }
      // validate the optional field `newGroupMemberAcceptance`
      if (jsonObj.get("newGroupMemberAcceptance") != null && !jsonObj.get("newGroupMemberAcceptance").isJsonNull()) {
        NewGroupMemberAcceptanceEnum.validateJsonElement(jsonObj.get("newGroupMemberAcceptance"));
      }
      // validate the required field `permissions`
      NodePermissions.validateJsonElement(jsonObj.get("permissions"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RoomGroupsAddBatchRequestItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RoomGroupsAddBatchRequestItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RoomGroupsAddBatchRequestItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RoomGroupsAddBatchRequestItem.class));

       return (TypeAdapter<T>) new TypeAdapter<RoomGroupsAddBatchRequestItem>() {
           @Override
           public void write(JsonWriter out, RoomGroupsAddBatchRequestItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RoomGroupsAddBatchRequestItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RoomGroupsAddBatchRequestItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RoomGroupsAddBatchRequestItem
   * @throws IOException if the JSON string is invalid with respect to RoomGroupsAddBatchRequestItem
   */
  public static RoomGroupsAddBatchRequestItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RoomGroupsAddBatchRequestItem.class);
  }

  /**
   * Convert an instance of RoomGroupsAddBatchRequestItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

