/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
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
 * UpdateSystemModelsUpdateGroupClientRelationship
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:35.511967-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateSystemModelsUpdateGroupClientRelationship {
  public static final String SERIALIZED_NAME_ACTIVE = "Active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_CLIENT_I_D = "ClientID";
  @SerializedName(SERIALIZED_NAME_CLIENT_I_D)
  private String clientID;

  public static final String SERIALIZED_NAME_LAST_CHECKIN = "LastCheckin";
  @SerializedName(SERIALIZED_NAME_LAST_CHECKIN)
  private OffsetDateTime lastCheckin;

  public static final String SERIALIZED_NAME_RELATIONSHIP_I_D = "RelationshipID";
  @SerializedName(SERIALIZED_NAME_RELATIONSHIP_I_D)
  private String relationshipID;

  public static final String SERIALIZED_NAME_UPDATE_GROUP_I_D = "UpdateGroupID";
  @SerializedName(SERIALIZED_NAME_UPDATE_GROUP_I_D)
  private String updateGroupID;

  public UpdateSystemModelsUpdateGroupClientRelationship() {
  }

  public UpdateSystemModelsUpdateGroupClientRelationship active(Boolean active) {
    this.active = active;
    return this;
  }

  /**
   * The subscription status.  The status is active by default.
   * @return active
   */
  @javax.annotation.Nullable
  public Boolean getActive() {
    return active;
  }

  public void setActive(Boolean active) {
    this.active = active;
  }


  public UpdateSystemModelsUpdateGroupClientRelationship clientID(String clientID) {
    this.clientID = clientID;
    return this;
  }

  /**
   * Read Only after creation. The client id of the subscriber.
   * @return clientID
   */
  @javax.annotation.Nonnull
  public String getClientID() {
    return clientID;
  }

  public void setClientID(String clientID) {
    this.clientID = clientID;
  }


  public UpdateSystemModelsUpdateGroupClientRelationship lastCheckin(OffsetDateTime lastCheckin) {
    this.lastCheckin = lastCheckin;
    return this;
  }

  /**
   * ReadOnly. The timestamp of the last checkin.
   * @return lastCheckin
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastCheckin() {
    return lastCheckin;
  }

  public void setLastCheckin(OffsetDateTime lastCheckin) {
    this.lastCheckin = lastCheckin;
  }


  public UpdateSystemModelsUpdateGroupClientRelationship relationshipID(String relationshipID) {
    this.relationshipID = relationshipID;
    return this;
  }

  /**
   * Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.
   * @return relationshipID
   */
  @javax.annotation.Nullable
  public String getRelationshipID() {
    return relationshipID;
  }

  public void setRelationshipID(String relationshipID) {
    this.relationshipID = relationshipID;
  }


  public UpdateSystemModelsUpdateGroupClientRelationship updateGroupID(String updateGroupID) {
    this.updateGroupID = updateGroupID;
    return this;
  }

  /**
   * Read Only after creation. The update group to subscribe to.
   * @return updateGroupID
   */
  @javax.annotation.Nonnull
  public String getUpdateGroupID() {
    return updateGroupID;
  }

  public void setUpdateGroupID(String updateGroupID) {
    this.updateGroupID = updateGroupID;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateSystemModelsUpdateGroupClientRelationship updateSystemModelsUpdateGroupClientRelationship = (UpdateSystemModelsUpdateGroupClientRelationship) o;
    return Objects.equals(this.active, updateSystemModelsUpdateGroupClientRelationship.active) &&
        Objects.equals(this.clientID, updateSystemModelsUpdateGroupClientRelationship.clientID) &&
        Objects.equals(this.lastCheckin, updateSystemModelsUpdateGroupClientRelationship.lastCheckin) &&
        Objects.equals(this.relationshipID, updateSystemModelsUpdateGroupClientRelationship.relationshipID) &&
        Objects.equals(this.updateGroupID, updateSystemModelsUpdateGroupClientRelationship.updateGroupID);
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, clientID, lastCheckin, relationshipID, updateGroupID);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateSystemModelsUpdateGroupClientRelationship {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    clientID: ").append(toIndentedString(clientID)).append("\n");
    sb.append("    lastCheckin: ").append(toIndentedString(lastCheckin)).append("\n");
    sb.append("    relationshipID: ").append(toIndentedString(relationshipID)).append("\n");
    sb.append("    updateGroupID: ").append(toIndentedString(updateGroupID)).append("\n");
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
    openapiFields.add("Active");
    openapiFields.add("ClientID");
    openapiFields.add("LastCheckin");
    openapiFields.add("RelationshipID");
    openapiFields.add("UpdateGroupID");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ClientID");
    openapiRequiredFields.add("UpdateGroupID");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateSystemModelsUpdateGroupClientRelationship
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateSystemModelsUpdateGroupClientRelationship.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateSystemModelsUpdateGroupClientRelationship is not found in the empty JSON string", UpdateSystemModelsUpdateGroupClientRelationship.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateSystemModelsUpdateGroupClientRelationship.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateSystemModelsUpdateGroupClientRelationship` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateSystemModelsUpdateGroupClientRelationship.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("ClientID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ClientID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ClientID").toString()));
      }
      if ((jsonObj.get("RelationshipID") != null && !jsonObj.get("RelationshipID").isJsonNull()) && !jsonObj.get("RelationshipID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `RelationshipID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("RelationshipID").toString()));
      }
      if (!jsonObj.get("UpdateGroupID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `UpdateGroupID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("UpdateGroupID").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateSystemModelsUpdateGroupClientRelationship.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateSystemModelsUpdateGroupClientRelationship' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateSystemModelsUpdateGroupClientRelationship> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateSystemModelsUpdateGroupClientRelationship.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateSystemModelsUpdateGroupClientRelationship>() {
           @Override
           public void write(JsonWriter out, UpdateSystemModelsUpdateGroupClientRelationship value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateSystemModelsUpdateGroupClientRelationship read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateSystemModelsUpdateGroupClientRelationship given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateSystemModelsUpdateGroupClientRelationship
   * @throws IOException if the JSON string is invalid with respect to UpdateSystemModelsUpdateGroupClientRelationship
   */
  public static UpdateSystemModelsUpdateGroupClientRelationship fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateSystemModelsUpdateGroupClientRelationship.class);
  }

  /**
   * Convert an instance of UpdateSystemModelsUpdateGroupClientRelationship to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

