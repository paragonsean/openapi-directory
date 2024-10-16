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
 * CodePushReleaseMetric
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CodePushReleaseMetric {
  public static final String SERIALIZED_NAME_ACTIVE = "active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Integer active;

  public static final String SERIALIZED_NAME_DOWNLOADED = "downloaded";
  @SerializedName(SERIALIZED_NAME_DOWNLOADED)
  private Integer downloaded;

  public static final String SERIALIZED_NAME_FAILED = "failed";
  @SerializedName(SERIALIZED_NAME_FAILED)
  private Integer failed;

  public static final String SERIALIZED_NAME_INSTALLED = "installed";
  @SerializedName(SERIALIZED_NAME_INSTALLED)
  private Integer installed;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public CodePushReleaseMetric() {
  }

  public CodePushReleaseMetric active(Integer active) {
    this.active = active;
    return this;
  }

  /**
   * Get active
   * @return active
   */
  @javax.annotation.Nonnull
  public Integer getActive() {
    return active;
  }

  public void setActive(Integer active) {
    this.active = active;
  }


  public CodePushReleaseMetric downloaded(Integer downloaded) {
    this.downloaded = downloaded;
    return this;
  }

  /**
   * Get downloaded
   * @return downloaded
   */
  @javax.annotation.Nullable
  public Integer getDownloaded() {
    return downloaded;
  }

  public void setDownloaded(Integer downloaded) {
    this.downloaded = downloaded;
  }


  public CodePushReleaseMetric failed(Integer failed) {
    this.failed = failed;
    return this;
  }

  /**
   * Get failed
   * @return failed
   */
  @javax.annotation.Nullable
  public Integer getFailed() {
    return failed;
  }

  public void setFailed(Integer failed) {
    this.failed = failed;
  }


  public CodePushReleaseMetric installed(Integer installed) {
    this.installed = installed;
    return this;
  }

  /**
   * Get installed
   * @return installed
   */
  @javax.annotation.Nullable
  public Integer getInstalled() {
    return installed;
  }

  public void setInstalled(Integer installed) {
    this.installed = installed;
  }


  public CodePushReleaseMetric label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Get label
   * @return label
   */
  @javax.annotation.Nonnull
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CodePushReleaseMetric codePushReleaseMetric = (CodePushReleaseMetric) o;
    return Objects.equals(this.active, codePushReleaseMetric.active) &&
        Objects.equals(this.downloaded, codePushReleaseMetric.downloaded) &&
        Objects.equals(this.failed, codePushReleaseMetric.failed) &&
        Objects.equals(this.installed, codePushReleaseMetric.installed) &&
        Objects.equals(this.label, codePushReleaseMetric.label);
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, downloaded, failed, installed, label);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CodePushReleaseMetric {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    downloaded: ").append(toIndentedString(downloaded)).append("\n");
    sb.append("    failed: ").append(toIndentedString(failed)).append("\n");
    sb.append("    installed: ").append(toIndentedString(installed)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
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
    openapiFields.add("active");
    openapiFields.add("downloaded");
    openapiFields.add("failed");
    openapiFields.add("installed");
    openapiFields.add("label");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("active");
    openapiRequiredFields.add("label");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CodePushReleaseMetric
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CodePushReleaseMetric.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CodePushReleaseMetric is not found in the empty JSON string", CodePushReleaseMetric.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CodePushReleaseMetric.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CodePushReleaseMetric` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CodePushReleaseMetric.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CodePushReleaseMetric.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CodePushReleaseMetric' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CodePushReleaseMetric> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CodePushReleaseMetric.class));

       return (TypeAdapter<T>) new TypeAdapter<CodePushReleaseMetric>() {
           @Override
           public void write(JsonWriter out, CodePushReleaseMetric value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CodePushReleaseMetric read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CodePushReleaseMetric given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CodePushReleaseMetric
   * @throws IOException if the JSON string is invalid with respect to CodePushReleaseMetric
   */
  public static CodePushReleaseMetric fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CodePushReleaseMetric.class);
  }

  /**
   * Convert an instance of CodePushReleaseMetric to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

