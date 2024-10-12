/*
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
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
 * PublicFile
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:45.951625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PublicFile {
  public static final String SERIALIZED_NAME_COMPUTED_MD5 = "computed_md5";
  @SerializedName(SERIALIZED_NAME_COMPUTED_MD5)
  private String computedMd5;

  public static final String SERIALIZED_NAME_DOWNLOAD_URL = "download_url";
  @SerializedName(SERIALIZED_NAME_DOWNLOAD_URL)
  private String downloadUrl;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_IS_LINK_ONLY = "is_link_only";
  @SerializedName(SERIALIZED_NAME_IS_LINK_ONLY)
  private Boolean isLinkOnly;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private Long size;

  public static final String SERIALIZED_NAME_SUPPLIED_MD5 = "supplied_md5";
  @SerializedName(SERIALIZED_NAME_SUPPLIED_MD5)
  private String suppliedMd5;

  public PublicFile() {
  }

  public PublicFile computedMd5(String computedMd5) {
    this.computedMd5 = computedMd5;
    return this;
  }

  /**
   * File computed md5
   * @return computedMd5
   */
  @javax.annotation.Nonnull
  public String getComputedMd5() {
    return computedMd5;
  }

  public void setComputedMd5(String computedMd5) {
    this.computedMd5 = computedMd5;
  }


  public PublicFile downloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
    return this;
  }

  /**
   * Url for file download
   * @return downloadUrl
   */
  @javax.annotation.Nonnull
  public String getDownloadUrl() {
    return downloadUrl;
  }

  public void setDownloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
  }


  public PublicFile id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * File id
   * @return id
   */
  @javax.annotation.Nonnull
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public PublicFile isLinkOnly(Boolean isLinkOnly) {
    this.isLinkOnly = isLinkOnly;
    return this;
  }

  /**
   * True if file is hosted somewhere else
   * @return isLinkOnly
   */
  @javax.annotation.Nonnull
  public Boolean getIsLinkOnly() {
    return isLinkOnly;
  }

  public void setIsLinkOnly(Boolean isLinkOnly) {
    this.isLinkOnly = isLinkOnly;
  }


  public PublicFile name(String name) {
    this.name = name;
    return this;
  }

  /**
   * File name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PublicFile size(Long size) {
    this.size = size;
    return this;
  }

  /**
   * File size
   * @return size
   */
  @javax.annotation.Nonnull
  public Long getSize() {
    return size;
  }

  public void setSize(Long size) {
    this.size = size;
  }


  public PublicFile suppliedMd5(String suppliedMd5) {
    this.suppliedMd5 = suppliedMd5;
    return this;
  }

  /**
   * File supplied md5
   * @return suppliedMd5
   */
  @javax.annotation.Nonnull
  public String getSuppliedMd5() {
    return suppliedMd5;
  }

  public void setSuppliedMd5(String suppliedMd5) {
    this.suppliedMd5 = suppliedMd5;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PublicFile publicFile = (PublicFile) o;
    return Objects.equals(this.computedMd5, publicFile.computedMd5) &&
        Objects.equals(this.downloadUrl, publicFile.downloadUrl) &&
        Objects.equals(this.id, publicFile.id) &&
        Objects.equals(this.isLinkOnly, publicFile.isLinkOnly) &&
        Objects.equals(this.name, publicFile.name) &&
        Objects.equals(this.size, publicFile.size) &&
        Objects.equals(this.suppliedMd5, publicFile.suppliedMd5);
  }

  @Override
  public int hashCode() {
    return Objects.hash(computedMd5, downloadUrl, id, isLinkOnly, name, size, suppliedMd5);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PublicFile {\n");
    sb.append("    computedMd5: ").append(toIndentedString(computedMd5)).append("\n");
    sb.append("    downloadUrl: ").append(toIndentedString(downloadUrl)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isLinkOnly: ").append(toIndentedString(isLinkOnly)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    suppliedMd5: ").append(toIndentedString(suppliedMd5)).append("\n");
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
    openapiFields.add("computed_md5");
    openapiFields.add("download_url");
    openapiFields.add("id");
    openapiFields.add("is_link_only");
    openapiFields.add("name");
    openapiFields.add("size");
    openapiFields.add("supplied_md5");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("computed_md5");
    openapiRequiredFields.add("download_url");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("is_link_only");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("size");
    openapiRequiredFields.add("supplied_md5");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PublicFile
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PublicFile.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PublicFile is not found in the empty JSON string", PublicFile.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PublicFile.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PublicFile` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PublicFile.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("computed_md5").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `computed_md5` to be a primitive type in the JSON string but got `%s`", jsonObj.get("computed_md5").toString()));
      }
      if (!jsonObj.get("download_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `download_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("download_url").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("supplied_md5").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supplied_md5` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supplied_md5").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PublicFile.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PublicFile' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PublicFile> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PublicFile.class));

       return (TypeAdapter<T>) new TypeAdapter<PublicFile>() {
           @Override
           public void write(JsonWriter out, PublicFile value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PublicFile read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PublicFile given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PublicFile
   * @throws IOException if the JSON string is invalid with respect to PublicFile
   */
  public static PublicFile fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PublicFile.class);
  }

  /**
   * Convert an instance of PublicFile to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

