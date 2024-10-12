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
 * Node permissions
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NodePermissions {
  public static final String SERIALIZED_NAME_CHANGE = "change";
  @SerializedName(SERIALIZED_NAME_CHANGE)
  private Boolean change;

  public static final String SERIALIZED_NAME_CREATE = "create";
  @SerializedName(SERIALIZED_NAME_CREATE)
  private Boolean create;

  public static final String SERIALIZED_NAME_DELETE = "delete";
  @SerializedName(SERIALIZED_NAME_DELETE)
  private Boolean delete;

  public static final String SERIALIZED_NAME_DELETE_RECYCLE_BIN = "deleteRecycleBin";
  @SerializedName(SERIALIZED_NAME_DELETE_RECYCLE_BIN)
  private Boolean deleteRecycleBin;

  public static final String SERIALIZED_NAME_MANAGE = "manage";
  @SerializedName(SERIALIZED_NAME_MANAGE)
  private Boolean manage;

  public static final String SERIALIZED_NAME_MANAGE_DOWNLOAD_SHARE = "manageDownloadShare";
  @SerializedName(SERIALIZED_NAME_MANAGE_DOWNLOAD_SHARE)
  private Boolean manageDownloadShare;

  public static final String SERIALIZED_NAME_MANAGE_UPLOAD_SHARE = "manageUploadShare";
  @SerializedName(SERIALIZED_NAME_MANAGE_UPLOAD_SHARE)
  private Boolean manageUploadShare;

  public static final String SERIALIZED_NAME_READ = "read";
  @SerializedName(SERIALIZED_NAME_READ)
  private Boolean read;

  public static final String SERIALIZED_NAME_READ_RECYCLE_BIN = "readRecycleBin";
  @SerializedName(SERIALIZED_NAME_READ_RECYCLE_BIN)
  private Boolean readRecycleBin;

  public static final String SERIALIZED_NAME_RESTORE_RECYCLE_BIN = "restoreRecycleBin";
  @SerializedName(SERIALIZED_NAME_RESTORE_RECYCLE_BIN)
  private Boolean restoreRecycleBin;

  public NodePermissions() {
  }

  public NodePermissions change(Boolean change) {
    this.change = change;
    return this;
  }

  /**
   * User / Group may update metadata of nodes: rename files and folders, change classification, etc.
   * @return change
   */
  @javax.annotation.Nonnull
  public Boolean getChange() {
    return change;
  }

  public void setChange(Boolean change) {
    this.change = change;
  }


  public NodePermissions create(Boolean create) {
    this.create = create;
    return this;
  }

  /**
   * User / Group may upload files, create folders and copy / move files to this room, overwriting is not possible.
   * @return create
   */
  @javax.annotation.Nonnull
  public Boolean getCreate() {
    return create;
  }

  public void setCreate(Boolean create) {
    this.create = create;
  }


  public NodePermissions delete(Boolean delete) {
    this.delete = delete;
    return this;
  }

  /**
   * User / Group may overwrite and remove files / folders, move files from this room.
   * @return delete
   */
  @javax.annotation.Nonnull
  public Boolean getDelete() {
    return delete;
  }

  public void setDelete(Boolean delete) {
    this.delete = delete;
  }


  public NodePermissions deleteRecycleBin(Boolean deleteRecycleBin) {
    this.deleteRecycleBin = deleteRecycleBin;
    return this;
  }

  /**
   * User / Group may permanently remove files / folders from the recycle bin.
   * @return deleteRecycleBin
   */
  @javax.annotation.Nonnull
  public Boolean getDeleteRecycleBin() {
    return deleteRecycleBin;
  }

  public void setDeleteRecycleBin(Boolean deleteRecycleBin) {
    this.deleteRecycleBin = deleteRecycleBin;
  }


  public NodePermissions manage(Boolean manage) {
    this.manage = manage;
    return this;
  }

  /**
   * User / Group may grant all of the above permissions to other users and groups independently,  may update room metadata and create / update / delete subordinary rooms, has all permissions.
   * @return manage
   */
  @javax.annotation.Nonnull
  public Boolean getManage() {
    return manage;
  }

  public void setManage(Boolean manage) {
    this.manage = manage;
  }


  public NodePermissions manageDownloadShare(Boolean manageDownloadShare) {
    this.manageDownloadShare = manageDownloadShare;
    return this;
  }

  /**
   * User / Group may create Download Shares for files and containers view all previously created Download Shares in this room.
   * @return manageDownloadShare
   */
  @javax.annotation.Nonnull
  public Boolean getManageDownloadShare() {
    return manageDownloadShare;
  }

  public void setManageDownloadShare(Boolean manageDownloadShare) {
    this.manageDownloadShare = manageDownloadShare;
  }


  public NodePermissions manageUploadShare(Boolean manageUploadShare) {
    this.manageUploadShare = manageUploadShare;
    return this;
  }

  /**
   * User / Group may create Upload Shares for containers, view all previously created Upload Shares in this room.
   * @return manageUploadShare
   */
  @javax.annotation.Nonnull
  public Boolean getManageUploadShare() {
    return manageUploadShare;
  }

  public void setManageUploadShare(Boolean manageUploadShare) {
    this.manageUploadShare = manageUploadShare;
  }


  public NodePermissions read(Boolean read) {
    this.read = read;
    return this;
  }

  /**
   * User / Group may see all rooms, files and folders in the room and download everything, copy files from this room.
   * @return read
   */
  @javax.annotation.Nonnull
  public Boolean getRead() {
    return read;
  }

  public void setRead(Boolean read) {
    this.read = read;
  }


  public NodePermissions readRecycleBin(Boolean readRecycleBin) {
    this.readRecycleBin = readRecycleBin;
    return this;
  }

  /**
   * User / Group may look up files / folders in the recycle bin.
   * @return readRecycleBin
   */
  @javax.annotation.Nonnull
  public Boolean getReadRecycleBin() {
    return readRecycleBin;
  }

  public void setReadRecycleBin(Boolean readRecycleBin) {
    this.readRecycleBin = readRecycleBin;
  }


  public NodePermissions restoreRecycleBin(Boolean restoreRecycleBin) {
    this.restoreRecycleBin = restoreRecycleBin;
    return this;
  }

  /**
   * User / Group may restore files / folders from recycle bin - room permissions required.
   * @return restoreRecycleBin
   */
  @javax.annotation.Nonnull
  public Boolean getRestoreRecycleBin() {
    return restoreRecycleBin;
  }

  public void setRestoreRecycleBin(Boolean restoreRecycleBin) {
    this.restoreRecycleBin = restoreRecycleBin;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NodePermissions nodePermissions = (NodePermissions) o;
    return Objects.equals(this.change, nodePermissions.change) &&
        Objects.equals(this.create, nodePermissions.create) &&
        Objects.equals(this.delete, nodePermissions.delete) &&
        Objects.equals(this.deleteRecycleBin, nodePermissions.deleteRecycleBin) &&
        Objects.equals(this.manage, nodePermissions.manage) &&
        Objects.equals(this.manageDownloadShare, nodePermissions.manageDownloadShare) &&
        Objects.equals(this.manageUploadShare, nodePermissions.manageUploadShare) &&
        Objects.equals(this.read, nodePermissions.read) &&
        Objects.equals(this.readRecycleBin, nodePermissions.readRecycleBin) &&
        Objects.equals(this.restoreRecycleBin, nodePermissions.restoreRecycleBin);
  }

  @Override
  public int hashCode() {
    return Objects.hash(change, create, delete, deleteRecycleBin, manage, manageDownloadShare, manageUploadShare, read, readRecycleBin, restoreRecycleBin);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NodePermissions {\n");
    sb.append("    change: ").append(toIndentedString(change)).append("\n");
    sb.append("    create: ").append(toIndentedString(create)).append("\n");
    sb.append("    delete: ").append(toIndentedString(delete)).append("\n");
    sb.append("    deleteRecycleBin: ").append(toIndentedString(deleteRecycleBin)).append("\n");
    sb.append("    manage: ").append(toIndentedString(manage)).append("\n");
    sb.append("    manageDownloadShare: ").append(toIndentedString(manageDownloadShare)).append("\n");
    sb.append("    manageUploadShare: ").append(toIndentedString(manageUploadShare)).append("\n");
    sb.append("    read: ").append(toIndentedString(read)).append("\n");
    sb.append("    readRecycleBin: ").append(toIndentedString(readRecycleBin)).append("\n");
    sb.append("    restoreRecycleBin: ").append(toIndentedString(restoreRecycleBin)).append("\n");
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
    openapiFields.add("change");
    openapiFields.add("create");
    openapiFields.add("delete");
    openapiFields.add("deleteRecycleBin");
    openapiFields.add("manage");
    openapiFields.add("manageDownloadShare");
    openapiFields.add("manageUploadShare");
    openapiFields.add("read");
    openapiFields.add("readRecycleBin");
    openapiFields.add("restoreRecycleBin");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("change");
    openapiRequiredFields.add("create");
    openapiRequiredFields.add("delete");
    openapiRequiredFields.add("deleteRecycleBin");
    openapiRequiredFields.add("manage");
    openapiRequiredFields.add("manageDownloadShare");
    openapiRequiredFields.add("manageUploadShare");
    openapiRequiredFields.add("read");
    openapiRequiredFields.add("readRecycleBin");
    openapiRequiredFields.add("restoreRecycleBin");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NodePermissions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NodePermissions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NodePermissions is not found in the empty JSON string", NodePermissions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NodePermissions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NodePermissions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : NodePermissions.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NodePermissions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NodePermissions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NodePermissions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NodePermissions.class));

       return (TypeAdapter<T>) new TypeAdapter<NodePermissions>() {
           @Override
           public void write(JsonWriter out, NodePermissions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NodePermissions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NodePermissions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NodePermissions
   * @throws IOException if the JSON string is invalid with respect to NodePermissions
   */
  public static NodePermissions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NodePermissions.class);
  }

  /**
   * Convert an instance of NodePermissions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

