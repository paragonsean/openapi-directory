/*
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
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
 * SampleResponseModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:47.855117-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SampleResponseModel {
  public static final String SERIALIZED_NAME_FILE_NAME = "file_name";
  @SerializedName(SERIALIZED_NAME_FILE_NAME)
  private String fileName;

  public static final String SERIALIZED_NAME_HASH = "hash";
  @SerializedName(SERIALIZED_NAME_HASH)
  private String hash;

  public static final String SERIALIZED_NAME_MIME_TYPE = "mime_type";
  @SerializedName(SERIALIZED_NAME_MIME_TYPE)
  private String mimeType;

  public static final String SERIALIZED_NAME_SAMPLE_ID = "sample_id";
  @SerializedName(SERIALIZED_NAME_SAMPLE_ID)
  private String sampleId;

  public static final String SERIALIZED_NAME_SIZE_BYTES = "size_bytes";
  @SerializedName(SERIALIZED_NAME_SIZE_BYTES)
  private Integer sizeBytes;

  public SampleResponseModel() {
  }

  public SampleResponseModel fileName(String fileName) {
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


  public SampleResponseModel hash(String hash) {
    this.hash = hash;
    return this;
  }

  /**
   * Get hash
   * @return hash
   */
  @javax.annotation.Nonnull
  public String getHash() {
    return hash;
  }

  public void setHash(String hash) {
    this.hash = hash;
  }


  public SampleResponseModel mimeType(String mimeType) {
    this.mimeType = mimeType;
    return this;
  }

  /**
   * Get mimeType
   * @return mimeType
   */
  @javax.annotation.Nonnull
  public String getMimeType() {
    return mimeType;
  }

  public void setMimeType(String mimeType) {
    this.mimeType = mimeType;
  }


  public SampleResponseModel sampleId(String sampleId) {
    this.sampleId = sampleId;
    return this;
  }

  /**
   * Get sampleId
   * @return sampleId
   */
  @javax.annotation.Nonnull
  public String getSampleId() {
    return sampleId;
  }

  public void setSampleId(String sampleId) {
    this.sampleId = sampleId;
  }


  public SampleResponseModel sizeBytes(Integer sizeBytes) {
    this.sizeBytes = sizeBytes;
    return this;
  }

  /**
   * Get sizeBytes
   * @return sizeBytes
   */
  @javax.annotation.Nonnull
  public Integer getSizeBytes() {
    return sizeBytes;
  }

  public void setSizeBytes(Integer sizeBytes) {
    this.sizeBytes = sizeBytes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SampleResponseModel sampleResponseModel = (SampleResponseModel) o;
    return Objects.equals(this.fileName, sampleResponseModel.fileName) &&
        Objects.equals(this.hash, sampleResponseModel.hash) &&
        Objects.equals(this.mimeType, sampleResponseModel.mimeType) &&
        Objects.equals(this.sampleId, sampleResponseModel.sampleId) &&
        Objects.equals(this.sizeBytes, sampleResponseModel.sizeBytes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fileName, hash, mimeType, sampleId, sizeBytes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SampleResponseModel {\n");
    sb.append("    fileName: ").append(toIndentedString(fileName)).append("\n");
    sb.append("    hash: ").append(toIndentedString(hash)).append("\n");
    sb.append("    mimeType: ").append(toIndentedString(mimeType)).append("\n");
    sb.append("    sampleId: ").append(toIndentedString(sampleId)).append("\n");
    sb.append("    sizeBytes: ").append(toIndentedString(sizeBytes)).append("\n");
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
    openapiFields.add("file_name");
    openapiFields.add("hash");
    openapiFields.add("mime_type");
    openapiFields.add("sample_id");
    openapiFields.add("size_bytes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("file_name");
    openapiRequiredFields.add("hash");
    openapiRequiredFields.add("mime_type");
    openapiRequiredFields.add("sample_id");
    openapiRequiredFields.add("size_bytes");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SampleResponseModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SampleResponseModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SampleResponseModel is not found in the empty JSON string", SampleResponseModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SampleResponseModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SampleResponseModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SampleResponseModel.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("file_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `file_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("file_name").toString()));
      }
      if (!jsonObj.get("hash").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hash` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hash").toString()));
      }
      if (!jsonObj.get("mime_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mime_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mime_type").toString()));
      }
      if (!jsonObj.get("sample_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sample_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sample_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SampleResponseModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SampleResponseModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SampleResponseModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SampleResponseModel.class));

       return (TypeAdapter<T>) new TypeAdapter<SampleResponseModel>() {
           @Override
           public void write(JsonWriter out, SampleResponseModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SampleResponseModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SampleResponseModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SampleResponseModel
   * @throws IOException if the JSON string is invalid with respect to SampleResponseModel
   */
  public static SampleResponseModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SampleResponseModel.class);
  }

  /**
   * Convert an instance of SampleResponseModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

