/*
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
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
 * ArtifactFormat
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:26.140477-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ArtifactFormat {
  public static final String SERIALIZED_NAME_CONTENT_TYPE = "contentType";
  @SerializedName(SERIALIZED_NAME_CONTENT_TYPE)
  private String contentType;

  public static final String SERIALIZED_NAME_FILE_EXTENSION = "fileExtension";
  @SerializedName(SERIALIZED_NAME_FILE_EXTENSION)
  private String fileExtension;

  public static final String SERIALIZED_NAME_FOR_CONTENT_TYPE = "forContentType";
  @SerializedName(SERIALIZED_NAME_FOR_CONTENT_TYPE)
  private String forContentType;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_PRESERVE_ASPECT_RATIO = "preserveAspectRatio";
  @SerializedName(SERIALIZED_NAME_PRESERVE_ASPECT_RATIO)
  private Boolean preserveAspectRatio;

  public static final String SERIALIZED_NAME_PUBLIC = "public";
  @SerializedName(SERIALIZED_NAME_PUBLIC)
  private Boolean _public;

  public static final String SERIALIZED_NAME_UPSCALE_ALLOWED = "upscaleAllowed";
  @SerializedName(SERIALIZED_NAME_UPSCALE_ALLOWED)
  private Boolean upscaleAllowed;

  public ArtifactFormat() {
  }

  public ArtifactFormat contentType(String contentType) {
    this.contentType = contentType;
    return this;
  }

  /**
   * Get contentType
   * @return contentType
   */
  @javax.annotation.Nullable
  public String getContentType() {
    return contentType;
  }

  public void setContentType(String contentType) {
    this.contentType = contentType;
  }


  public ArtifactFormat fileExtension(String fileExtension) {
    this.fileExtension = fileExtension;
    return this;
  }

  /**
   * Get fileExtension
   * @return fileExtension
   */
  @javax.annotation.Nullable
  public String getFileExtension() {
    return fileExtension;
  }

  public void setFileExtension(String fileExtension) {
    this.fileExtension = fileExtension;
  }


  public ArtifactFormat forContentType(String forContentType) {
    this.forContentType = forContentType;
    return this;
  }

  /**
   * Get forContentType
   * @return forContentType
   */
  @javax.annotation.Nullable
  public String getForContentType() {
    return forContentType;
  }

  public void setForContentType(String forContentType) {
    this.forContentType = forContentType;
  }


  public ArtifactFormat label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Get label
   * @return label
   */
  @javax.annotation.Nullable
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public ArtifactFormat preserveAspectRatio(Boolean preserveAspectRatio) {
    this.preserveAspectRatio = preserveAspectRatio;
    return this;
  }

  /**
   * Get preserveAspectRatio
   * @return preserveAspectRatio
   */
  @javax.annotation.Nullable
  public Boolean getPreserveAspectRatio() {
    return preserveAspectRatio;
  }

  public void setPreserveAspectRatio(Boolean preserveAspectRatio) {
    this.preserveAspectRatio = preserveAspectRatio;
  }


  public ArtifactFormat _public(Boolean _public) {
    this._public = _public;
    return this;
  }

  /**
   * Get _public
   * @return _public
   */
  @javax.annotation.Nullable
  public Boolean getPublic() {
    return _public;
  }

  public void setPublic(Boolean _public) {
    this._public = _public;
  }


  public ArtifactFormat upscaleAllowed(Boolean upscaleAllowed) {
    this.upscaleAllowed = upscaleAllowed;
    return this;
  }

  /**
   * Get upscaleAllowed
   * @return upscaleAllowed
   */
  @javax.annotation.Nullable
  public Boolean getUpscaleAllowed() {
    return upscaleAllowed;
  }

  public void setUpscaleAllowed(Boolean upscaleAllowed) {
    this.upscaleAllowed = upscaleAllowed;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ArtifactFormat artifactFormat = (ArtifactFormat) o;
    return Objects.equals(this.contentType, artifactFormat.contentType) &&
        Objects.equals(this.fileExtension, artifactFormat.fileExtension) &&
        Objects.equals(this.forContentType, artifactFormat.forContentType) &&
        Objects.equals(this.label, artifactFormat.label) &&
        Objects.equals(this.preserveAspectRatio, artifactFormat.preserveAspectRatio) &&
        Objects.equals(this._public, artifactFormat._public) &&
        Objects.equals(this.upscaleAllowed, artifactFormat.upscaleAllowed);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contentType, fileExtension, forContentType, label, preserveAspectRatio, _public, upscaleAllowed);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ArtifactFormat {\n");
    sb.append("    contentType: ").append(toIndentedString(contentType)).append("\n");
    sb.append("    fileExtension: ").append(toIndentedString(fileExtension)).append("\n");
    sb.append("    forContentType: ").append(toIndentedString(forContentType)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    preserveAspectRatio: ").append(toIndentedString(preserveAspectRatio)).append("\n");
    sb.append("    _public: ").append(toIndentedString(_public)).append("\n");
    sb.append("    upscaleAllowed: ").append(toIndentedString(upscaleAllowed)).append("\n");
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
    openapiFields.add("contentType");
    openapiFields.add("fileExtension");
    openapiFields.add("forContentType");
    openapiFields.add("label");
    openapiFields.add("preserveAspectRatio");
    openapiFields.add("public");
    openapiFields.add("upscaleAllowed");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ArtifactFormat
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ArtifactFormat.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ArtifactFormat is not found in the empty JSON string", ArtifactFormat.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ArtifactFormat.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ArtifactFormat` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("contentType") != null && !jsonObj.get("contentType").isJsonNull()) && !jsonObj.get("contentType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contentType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contentType").toString()));
      }
      if ((jsonObj.get("fileExtension") != null && !jsonObj.get("fileExtension").isJsonNull()) && !jsonObj.get("fileExtension").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileExtension` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileExtension").toString()));
      }
      if ((jsonObj.get("forContentType") != null && !jsonObj.get("forContentType").isJsonNull()) && !jsonObj.get("forContentType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `forContentType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("forContentType").toString()));
      }
      if ((jsonObj.get("label") != null && !jsonObj.get("label").isJsonNull()) && !jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ArtifactFormat.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ArtifactFormat' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ArtifactFormat> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ArtifactFormat.class));

       return (TypeAdapter<T>) new TypeAdapter<ArtifactFormat>() {
           @Override
           public void write(JsonWriter out, ArtifactFormat value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ArtifactFormat read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ArtifactFormat given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ArtifactFormat
   * @throws IOException if the JSON string is invalid with respect to ArtifactFormat
   */
  public static ArtifactFormat fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ArtifactFormat.class);
  }

  /**
   * Convert an instance of ArtifactFormat to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

