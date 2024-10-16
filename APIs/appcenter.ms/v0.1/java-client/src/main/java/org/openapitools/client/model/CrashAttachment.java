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
import java.math.BigDecimal;
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
 * CrashAttachment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CrashAttachment {
  public static final String SERIALIZED_NAME_APP_ID = "app_id";
  @SerializedName(SERIALIZED_NAME_APP_ID)
  private String appId;

  public static final String SERIALIZED_NAME_ATTACHMENT_ID = "attachment_id";
  @SerializedName(SERIALIZED_NAME_ATTACHMENT_ID)
  private String attachmentId;

  public static final String SERIALIZED_NAME_BLOB_LOCATION = "blob_location";
  @SerializedName(SERIALIZED_NAME_BLOB_LOCATION)
  private String blobLocation;

  public static final String SERIALIZED_NAME_CONTENT_TYPE = "content_type";
  @SerializedName(SERIALIZED_NAME_CONTENT_TYPE)
  private String contentType;

  public static final String SERIALIZED_NAME_CRASH_ID = "crash_id";
  @SerializedName(SERIALIZED_NAME_CRASH_ID)
  private String crashId;

  public static final String SERIALIZED_NAME_CREATED_TIME = "created_time";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_FILE_NAME = "file_name";
  @SerializedName(SERIALIZED_NAME_FILE_NAME)
  private String fileName;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private BigDecimal size;

  public CrashAttachment() {
  }

  public CrashAttachment appId(String appId) {
    this.appId = appId;
    return this;
  }

  /**
   * Get appId
   * @return appId
   */
  @javax.annotation.Nonnull
  public String getAppId() {
    return appId;
  }

  public void setAppId(String appId) {
    this.appId = appId;
  }


  public CrashAttachment attachmentId(String attachmentId) {
    this.attachmentId = attachmentId;
    return this;
  }

  /**
   * Get attachmentId
   * @return attachmentId
   */
  @javax.annotation.Nonnull
  public String getAttachmentId() {
    return attachmentId;
  }

  public void setAttachmentId(String attachmentId) {
    this.attachmentId = attachmentId;
  }


  public CrashAttachment blobLocation(String blobLocation) {
    this.blobLocation = blobLocation;
    return this;
  }

  /**
   * Get blobLocation
   * @return blobLocation
   */
  @javax.annotation.Nonnull
  public String getBlobLocation() {
    return blobLocation;
  }

  public void setBlobLocation(String blobLocation) {
    this.blobLocation = blobLocation;
  }


  public CrashAttachment contentType(String contentType) {
    this.contentType = contentType;
    return this;
  }

  /**
   * Get contentType
   * @return contentType
   */
  @javax.annotation.Nonnull
  public String getContentType() {
    return contentType;
  }

  public void setContentType(String contentType) {
    this.contentType = contentType;
  }


  public CrashAttachment crashId(String crashId) {
    this.crashId = crashId;
    return this;
  }

  /**
   * Get crashId
   * @return crashId
   */
  @javax.annotation.Nonnull
  public String getCrashId() {
    return crashId;
  }

  public void setCrashId(String crashId) {
    this.crashId = crashId;
  }


  public CrashAttachment createdTime(OffsetDateTime createdTime) {
    this.createdTime = createdTime;
    return this;
  }

  /**
   * Get createdTime
   * @return createdTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }

  public void setCreatedTime(OffsetDateTime createdTime) {
    this.createdTime = createdTime;
  }


  public CrashAttachment fileName(String fileName) {
    this.fileName = fileName;
    return this;
  }

  /**
   * Get fileName
   * @return fileName
   */
  @javax.annotation.Nonnull
  public String getFileName() {
    return fileName;
  }

  public void setFileName(String fileName) {
    this.fileName = fileName;
  }


  public CrashAttachment size(BigDecimal size) {
    this.size = size;
    return this;
  }

  /**
   * Get size
   * @return size
   */
  @javax.annotation.Nonnull
  public BigDecimal getSize() {
    return size;
  }

  public void setSize(BigDecimal size) {
    this.size = size;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CrashAttachment crashAttachment = (CrashAttachment) o;
    return Objects.equals(this.appId, crashAttachment.appId) &&
        Objects.equals(this.attachmentId, crashAttachment.attachmentId) &&
        Objects.equals(this.blobLocation, crashAttachment.blobLocation) &&
        Objects.equals(this.contentType, crashAttachment.contentType) &&
        Objects.equals(this.crashId, crashAttachment.crashId) &&
        Objects.equals(this.createdTime, crashAttachment.createdTime) &&
        Objects.equals(this.fileName, crashAttachment.fileName) &&
        Objects.equals(this.size, crashAttachment.size);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appId, attachmentId, blobLocation, contentType, crashId, createdTime, fileName, size);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CrashAttachment {\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    attachmentId: ").append(toIndentedString(attachmentId)).append("\n");
    sb.append("    blobLocation: ").append(toIndentedString(blobLocation)).append("\n");
    sb.append("    contentType: ").append(toIndentedString(contentType)).append("\n");
    sb.append("    crashId: ").append(toIndentedString(crashId)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    fileName: ").append(toIndentedString(fileName)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
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
    openapiFields.add("app_id");
    openapiFields.add("attachment_id");
    openapiFields.add("blob_location");
    openapiFields.add("content_type");
    openapiFields.add("crash_id");
    openapiFields.add("created_time");
    openapiFields.add("file_name");
    openapiFields.add("size");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("app_id");
    openapiRequiredFields.add("attachment_id");
    openapiRequiredFields.add("blob_location");
    openapiRequiredFields.add("content_type");
    openapiRequiredFields.add("crash_id");
    openapiRequiredFields.add("created_time");
    openapiRequiredFields.add("file_name");
    openapiRequiredFields.add("size");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CrashAttachment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CrashAttachment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CrashAttachment is not found in the empty JSON string", CrashAttachment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CrashAttachment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CrashAttachment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CrashAttachment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("app_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `app_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("app_id").toString()));
      }
      if (!jsonObj.get("attachment_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `attachment_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("attachment_id").toString()));
      }
      if (!jsonObj.get("blob_location").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `blob_location` to be a primitive type in the JSON string but got `%s`", jsonObj.get("blob_location").toString()));
      }
      if (!jsonObj.get("content_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content_type").toString()));
      }
      if (!jsonObj.get("crash_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `crash_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("crash_id").toString()));
      }
      if (!jsonObj.get("file_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `file_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("file_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CrashAttachment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CrashAttachment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CrashAttachment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CrashAttachment.class));

       return (TypeAdapter<T>) new TypeAdapter<CrashAttachment>() {
           @Override
           public void write(JsonWriter out, CrashAttachment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CrashAttachment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CrashAttachment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CrashAttachment
   * @throws IOException if the JSON string is invalid with respect to CrashAttachment
   */
  public static CrashAttachment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CrashAttachment.class);
  }

  /**
   * Convert an instance of CrashAttachment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

