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
import org.openapitools.client.model.ErrorResponse;

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
 * S3 file upload status information
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class S3ShareUploadStatus {
  public static final String SERIALIZED_NAME_ERROR_DETAILS = "errorDetails";
  @SerializedName(SERIALIZED_NAME_ERROR_DETAILS)
  private ErrorResponse errorDetails;

  public static final String SERIALIZED_NAME_FILE_NAME = "fileName";
  @SerializedName(SERIALIZED_NAME_FILE_NAME)
  private String fileName;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private Long size;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public S3ShareUploadStatus() {
  }

  public S3ShareUploadStatus errorDetails(ErrorResponse errorDetails) {
    this.errorDetails = errorDetails;
    return this;
  }

  /**
   * Get errorDetails
   * @return errorDetails
   */
  @javax.annotation.Nullable
  public ErrorResponse getErrorDetails() {
    return errorDetails;
  }

  public void setErrorDetails(ErrorResponse errorDetails) {
    this.errorDetails = errorDetails;
  }


  public S3ShareUploadStatus fileName(String fileName) {
    this.fileName = fileName;
    return this;
  }

  /**
   * File name
   * @return fileName
   */
  @javax.annotation.Nonnull
  public String getFileName() {
    return fileName;
  }

  public void setFileName(String fileName) {
    this.fileName = fileName;
  }


  public S3ShareUploadStatus size(Long size) {
    this.size = size;
    return this;
  }

  /**
   * File size in byte
   * @return size
   */
  @javax.annotation.Nullable
  public Long getSize() {
    return size;
  }

  public void setSize(Long size) {
    this.size = size;
  }


  public S3ShareUploadStatus status(String status) {
    this.status = status;
    return this;
  }

  /**
   * S3 file upload status:  * &#x60;transfer&#x60; - upload in progress  * &#x60;finishing&#x60; - completing file upload  * &#x60;done&#x60; - file upload successully done  * &#x60;error&#x60; - an error occurred while file upload
   * @return status
   */
  @javax.annotation.Nonnull
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    S3ShareUploadStatus s3ShareUploadStatus = (S3ShareUploadStatus) o;
    return Objects.equals(this.errorDetails, s3ShareUploadStatus.errorDetails) &&
        Objects.equals(this.fileName, s3ShareUploadStatus.fileName) &&
        Objects.equals(this.size, s3ShareUploadStatus.size) &&
        Objects.equals(this.status, s3ShareUploadStatus.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(errorDetails, fileName, size, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class S3ShareUploadStatus {\n");
    sb.append("    errorDetails: ").append(toIndentedString(errorDetails)).append("\n");
    sb.append("    fileName: ").append(toIndentedString(fileName)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("errorDetails");
    openapiFields.add("fileName");
    openapiFields.add("size");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("fileName");
    openapiRequiredFields.add("status");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to S3ShareUploadStatus
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!S3ShareUploadStatus.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in S3ShareUploadStatus is not found in the empty JSON string", S3ShareUploadStatus.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!S3ShareUploadStatus.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `S3ShareUploadStatus` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : S3ShareUploadStatus.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `errorDetails`
      if (jsonObj.get("errorDetails") != null && !jsonObj.get("errorDetails").isJsonNull()) {
        ErrorResponse.validateJsonElement(jsonObj.get("errorDetails"));
      }
      if (!jsonObj.get("fileName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileName").toString()));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!S3ShareUploadStatus.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'S3ShareUploadStatus' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<S3ShareUploadStatus> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(S3ShareUploadStatus.class));

       return (TypeAdapter<T>) new TypeAdapter<S3ShareUploadStatus>() {
           @Override
           public void write(JsonWriter out, S3ShareUploadStatus value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public S3ShareUploadStatus read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of S3ShareUploadStatus given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of S3ShareUploadStatus
   * @throws IOException if the JSON string is invalid with respect to S3ShareUploadStatus
   */
  public static S3ShareUploadStatus fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, S3ShareUploadStatus.class);
  }

  /**
   * Convert an instance of S3ShareUploadStatus to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

