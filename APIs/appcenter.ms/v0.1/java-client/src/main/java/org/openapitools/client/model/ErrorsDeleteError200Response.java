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
 * ErrorsDeleteError200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorsDeleteError200Response {
  public static final String SERIALIZED_NAME_APP_ID = "appId";
  @SerializedName(SERIALIZED_NAME_APP_ID)
  private String appId;

  public static final String SERIALIZED_NAME_ATTACHMENTS_DELETED = "attachmentsDeleted";
  @SerializedName(SERIALIZED_NAME_ATTACHMENTS_DELETED)
  private Integer attachmentsDeleted;

  public static final String SERIALIZED_NAME_BLOBS_FAILED = "blobsFailed";
  @SerializedName(SERIALIZED_NAME_BLOBS_FAILED)
  private Integer blobsFailed;

  public static final String SERIALIZED_NAME_BLOBS_SUCCEEDED = "blobsSucceeded";
  @SerializedName(SERIALIZED_NAME_BLOBS_SUCCEEDED)
  private Integer blobsSucceeded;

  public static final String SERIALIZED_NAME_ERROR_GROUP_ID = "errorGroupId";
  @SerializedName(SERIALIZED_NAME_ERROR_GROUP_ID)
  private String errorGroupId;

  public static final String SERIALIZED_NAME_ERROR_ID = "errorId";
  @SerializedName(SERIALIZED_NAME_ERROR_ID)
  private String errorId;

  public static final String SERIALIZED_NAME_ERRORS_DELETED = "errorsDeleted";
  @SerializedName(SERIALIZED_NAME_ERRORS_DELETED)
  private Integer errorsDeleted;

  public ErrorsDeleteError200Response() {
  }

  public ErrorsDeleteError200Response appId(String appId) {
    this.appId = appId;
    return this;
  }

  /**
   * Get appId
   * @return appId
   */
  @javax.annotation.Nullable
  public String getAppId() {
    return appId;
  }

  public void setAppId(String appId) {
    this.appId = appId;
  }


  public ErrorsDeleteError200Response attachmentsDeleted(Integer attachmentsDeleted) {
    this.attachmentsDeleted = attachmentsDeleted;
    return this;
  }

  /**
   * Get attachmentsDeleted
   * @return attachmentsDeleted
   */
  @javax.annotation.Nullable
  public Integer getAttachmentsDeleted() {
    return attachmentsDeleted;
  }

  public void setAttachmentsDeleted(Integer attachmentsDeleted) {
    this.attachmentsDeleted = attachmentsDeleted;
  }


  public ErrorsDeleteError200Response blobsFailed(Integer blobsFailed) {
    this.blobsFailed = blobsFailed;
    return this;
  }

  /**
   * Get blobsFailed
   * @return blobsFailed
   */
  @javax.annotation.Nullable
  public Integer getBlobsFailed() {
    return blobsFailed;
  }

  public void setBlobsFailed(Integer blobsFailed) {
    this.blobsFailed = blobsFailed;
  }


  public ErrorsDeleteError200Response blobsSucceeded(Integer blobsSucceeded) {
    this.blobsSucceeded = blobsSucceeded;
    return this;
  }

  /**
   * Get blobsSucceeded
   * @return blobsSucceeded
   */
  @javax.annotation.Nullable
  public Integer getBlobsSucceeded() {
    return blobsSucceeded;
  }

  public void setBlobsSucceeded(Integer blobsSucceeded) {
    this.blobsSucceeded = blobsSucceeded;
  }


  public ErrorsDeleteError200Response errorGroupId(String errorGroupId) {
    this.errorGroupId = errorGroupId;
    return this;
  }

  /**
   * Get errorGroupId
   * @return errorGroupId
   */
  @javax.annotation.Nullable
  public String getErrorGroupId() {
    return errorGroupId;
  }

  public void setErrorGroupId(String errorGroupId) {
    this.errorGroupId = errorGroupId;
  }


  public ErrorsDeleteError200Response errorId(String errorId) {
    this.errorId = errorId;
    return this;
  }

  /**
   * Get errorId
   * @return errorId
   */
  @javax.annotation.Nullable
  public String getErrorId() {
    return errorId;
  }

  public void setErrorId(String errorId) {
    this.errorId = errorId;
  }


  public ErrorsDeleteError200Response errorsDeleted(Integer errorsDeleted) {
    this.errorsDeleted = errorsDeleted;
    return this;
  }

  /**
   * Get errorsDeleted
   * @return errorsDeleted
   */
  @javax.annotation.Nullable
  public Integer getErrorsDeleted() {
    return errorsDeleted;
  }

  public void setErrorsDeleted(Integer errorsDeleted) {
    this.errorsDeleted = errorsDeleted;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ErrorsDeleteError200Response errorsDeleteError200Response = (ErrorsDeleteError200Response) o;
    return Objects.equals(this.appId, errorsDeleteError200Response.appId) &&
        Objects.equals(this.attachmentsDeleted, errorsDeleteError200Response.attachmentsDeleted) &&
        Objects.equals(this.blobsFailed, errorsDeleteError200Response.blobsFailed) &&
        Objects.equals(this.blobsSucceeded, errorsDeleteError200Response.blobsSucceeded) &&
        Objects.equals(this.errorGroupId, errorsDeleteError200Response.errorGroupId) &&
        Objects.equals(this.errorId, errorsDeleteError200Response.errorId) &&
        Objects.equals(this.errorsDeleted, errorsDeleteError200Response.errorsDeleted);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appId, attachmentsDeleted, blobsFailed, blobsSucceeded, errorGroupId, errorId, errorsDeleted);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorsDeleteError200Response {\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    attachmentsDeleted: ").append(toIndentedString(attachmentsDeleted)).append("\n");
    sb.append("    blobsFailed: ").append(toIndentedString(blobsFailed)).append("\n");
    sb.append("    blobsSucceeded: ").append(toIndentedString(blobsSucceeded)).append("\n");
    sb.append("    errorGroupId: ").append(toIndentedString(errorGroupId)).append("\n");
    sb.append("    errorId: ").append(toIndentedString(errorId)).append("\n");
    sb.append("    errorsDeleted: ").append(toIndentedString(errorsDeleted)).append("\n");
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
    openapiFields.add("appId");
    openapiFields.add("attachmentsDeleted");
    openapiFields.add("blobsFailed");
    openapiFields.add("blobsSucceeded");
    openapiFields.add("errorGroupId");
    openapiFields.add("errorId");
    openapiFields.add("errorsDeleted");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorsDeleteError200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorsDeleteError200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorsDeleteError200Response is not found in the empty JSON string", ErrorsDeleteError200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorsDeleteError200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorsDeleteError200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appId") != null && !jsonObj.get("appId").isJsonNull()) && !jsonObj.get("appId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appId").toString()));
      }
      if ((jsonObj.get("errorGroupId") != null && !jsonObj.get("errorGroupId").isJsonNull()) && !jsonObj.get("errorGroupId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `errorGroupId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("errorGroupId").toString()));
      }
      if ((jsonObj.get("errorId") != null && !jsonObj.get("errorId").isJsonNull()) && !jsonObj.get("errorId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `errorId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("errorId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ErrorsDeleteError200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorsDeleteError200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorsDeleteError200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorsDeleteError200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorsDeleteError200Response>() {
           @Override
           public void write(JsonWriter out, ErrorsDeleteError200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorsDeleteError200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorsDeleteError200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorsDeleteError200Response
   * @throws IOException if the JSON string is invalid with respect to ErrorsDeleteError200Response
   */
  public static ErrorsDeleteError200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorsDeleteError200Response.class);
  }

  /**
   * Convert an instance of ErrorsDeleteError200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

