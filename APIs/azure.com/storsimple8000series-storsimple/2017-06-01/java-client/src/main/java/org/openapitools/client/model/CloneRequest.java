/*
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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
import org.openapitools.client.model.BackupElement;

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
 * The clone job request.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:41.316643-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CloneRequest {
  public static final String SERIALIZED_NAME_BACKUP_ELEMENT = "backupElement";
  @SerializedName(SERIALIZED_NAME_BACKUP_ELEMENT)
  private BackupElement backupElement;

  public static final String SERIALIZED_NAME_TARGET_ACCESS_CONTROL_RECORD_IDS = "targetAccessControlRecordIds";
  @SerializedName(SERIALIZED_NAME_TARGET_ACCESS_CONTROL_RECORD_IDS)
  private List<String> targetAccessControlRecordIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_TARGET_DEVICE_ID = "targetDeviceId";
  @SerializedName(SERIALIZED_NAME_TARGET_DEVICE_ID)
  private String targetDeviceId;

  public static final String SERIALIZED_NAME_TARGET_VOLUME_NAME = "targetVolumeName";
  @SerializedName(SERIALIZED_NAME_TARGET_VOLUME_NAME)
  private String targetVolumeName;

  public CloneRequest() {
  }

  public CloneRequest backupElement(BackupElement backupElement) {
    this.backupElement = backupElement;
    return this;
  }

  /**
   * Get backupElement
   * @return backupElement
   */
  @javax.annotation.Nonnull
  public BackupElement getBackupElement() {
    return backupElement;
  }

  public void setBackupElement(BackupElement backupElement) {
    this.backupElement = backupElement;
  }


  public CloneRequest targetAccessControlRecordIds(List<String> targetAccessControlRecordIds) {
    this.targetAccessControlRecordIds = targetAccessControlRecordIds;
    return this;
  }

  public CloneRequest addTargetAccessControlRecordIdsItem(String targetAccessControlRecordIdsItem) {
    if (this.targetAccessControlRecordIds == null) {
      this.targetAccessControlRecordIds = new ArrayList<>();
    }
    this.targetAccessControlRecordIds.add(targetAccessControlRecordIdsItem);
    return this;
  }

  /**
   * The list of path IDs of the access control records to be associated to the new cloned volume.
   * @return targetAccessControlRecordIds
   */
  @javax.annotation.Nonnull
  public List<String> getTargetAccessControlRecordIds() {
    return targetAccessControlRecordIds;
  }

  public void setTargetAccessControlRecordIds(List<String> targetAccessControlRecordIds) {
    this.targetAccessControlRecordIds = targetAccessControlRecordIds;
  }


  public CloneRequest targetDeviceId(String targetDeviceId) {
    this.targetDeviceId = targetDeviceId;
    return this;
  }

  /**
   * The path ID of the device which will act as the clone target.
   * @return targetDeviceId
   */
  @javax.annotation.Nonnull
  public String getTargetDeviceId() {
    return targetDeviceId;
  }

  public void setTargetDeviceId(String targetDeviceId) {
    this.targetDeviceId = targetDeviceId;
  }


  public CloneRequest targetVolumeName(String targetVolumeName) {
    this.targetVolumeName = targetVolumeName;
    return this;
  }

  /**
   * The name of the new volume which will be created and the backup will be cloned into.
   * @return targetVolumeName
   */
  @javax.annotation.Nonnull
  public String getTargetVolumeName() {
    return targetVolumeName;
  }

  public void setTargetVolumeName(String targetVolumeName) {
    this.targetVolumeName = targetVolumeName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CloneRequest cloneRequest = (CloneRequest) o;
    return Objects.equals(this.backupElement, cloneRequest.backupElement) &&
        Objects.equals(this.targetAccessControlRecordIds, cloneRequest.targetAccessControlRecordIds) &&
        Objects.equals(this.targetDeviceId, cloneRequest.targetDeviceId) &&
        Objects.equals(this.targetVolumeName, cloneRequest.targetVolumeName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(backupElement, targetAccessControlRecordIds, targetDeviceId, targetVolumeName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CloneRequest {\n");
    sb.append("    backupElement: ").append(toIndentedString(backupElement)).append("\n");
    sb.append("    targetAccessControlRecordIds: ").append(toIndentedString(targetAccessControlRecordIds)).append("\n");
    sb.append("    targetDeviceId: ").append(toIndentedString(targetDeviceId)).append("\n");
    sb.append("    targetVolumeName: ").append(toIndentedString(targetVolumeName)).append("\n");
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
    openapiFields.add("backupElement");
    openapiFields.add("targetAccessControlRecordIds");
    openapiFields.add("targetDeviceId");
    openapiFields.add("targetVolumeName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("backupElement");
    openapiRequiredFields.add("targetAccessControlRecordIds");
    openapiRequiredFields.add("targetDeviceId");
    openapiRequiredFields.add("targetVolumeName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CloneRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CloneRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CloneRequest is not found in the empty JSON string", CloneRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CloneRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CloneRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CloneRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `backupElement`
      BackupElement.validateJsonElement(jsonObj.get("backupElement"));
      // ensure the required json array is present
      if (jsonObj.get("targetAccessControlRecordIds") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("targetAccessControlRecordIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetAccessControlRecordIds` to be an array in the JSON string but got `%s`", jsonObj.get("targetAccessControlRecordIds").toString()));
      }
      if (!jsonObj.get("targetDeviceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetDeviceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("targetDeviceId").toString()));
      }
      if (!jsonObj.get("targetVolumeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetVolumeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("targetVolumeName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CloneRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CloneRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CloneRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CloneRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CloneRequest>() {
           @Override
           public void write(JsonWriter out, CloneRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CloneRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CloneRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CloneRequest
   * @throws IOException if the JSON string is invalid with respect to CloneRequest
   */
  public static CloneRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CloneRequest.class);
  }

  /**
   * Convert an instance of CloneRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

