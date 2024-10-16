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
 * LegacyDeploymentMetric
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LegacyDeploymentMetric {
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

  public LegacyDeploymentMetric() {
  }

  public LegacyDeploymentMetric active(Integer active) {
    this.active = active;
    return this;
  }

  /**
   * The number of devices that have this release installed currently
   * @return active
   */
  @javax.annotation.Nonnull
  public Integer getActive() {
    return active;
  }

  public void setActive(Integer active) {
    this.active = active;
  }


  public LegacyDeploymentMetric downloaded(Integer downloaded) {
    this.downloaded = downloaded;
    return this;
  }

  /**
   * The number of times this release has been downloaded
   * @return downloaded
   */
  @javax.annotation.Nullable
  public Integer getDownloaded() {
    return downloaded;
  }

  public void setDownloaded(Integer downloaded) {
    this.downloaded = downloaded;
  }


  public LegacyDeploymentMetric failed(Integer failed) {
    this.failed = failed;
    return this;
  }

  /**
   * The number of times this release has failed to be installed on a device
   * @return failed
   */
  @javax.annotation.Nullable
  public Integer getFailed() {
    return failed;
  }

  public void setFailed(Integer failed) {
    this.failed = failed;
  }


  public LegacyDeploymentMetric installed(Integer installed) {
    this.installed = installed;
    return this;
  }

  /**
   * The number of times this release has been installed on a device
   * @return installed
   */
  @javax.annotation.Nullable
  public Integer getInstalled() {
    return installed;
  }

  public void setInstalled(Integer installed) {
    this.installed = installed;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LegacyDeploymentMetric legacyDeploymentMetric = (LegacyDeploymentMetric) o;
    return Objects.equals(this.active, legacyDeploymentMetric.active) &&
        Objects.equals(this.downloaded, legacyDeploymentMetric.downloaded) &&
        Objects.equals(this.failed, legacyDeploymentMetric.failed) &&
        Objects.equals(this.installed, legacyDeploymentMetric.installed);
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, downloaded, failed, installed);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LegacyDeploymentMetric {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    downloaded: ").append(toIndentedString(downloaded)).append("\n");
    sb.append("    failed: ").append(toIndentedString(failed)).append("\n");
    sb.append("    installed: ").append(toIndentedString(installed)).append("\n");
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

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("active");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LegacyDeploymentMetric
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LegacyDeploymentMetric.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LegacyDeploymentMetric is not found in the empty JSON string", LegacyDeploymentMetric.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LegacyDeploymentMetric.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LegacyDeploymentMetric` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : LegacyDeploymentMetric.openapiRequiredFields) {
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
       if (!LegacyDeploymentMetric.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LegacyDeploymentMetric' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LegacyDeploymentMetric> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LegacyDeploymentMetric.class));

       return (TypeAdapter<T>) new TypeAdapter<LegacyDeploymentMetric>() {
           @Override
           public void write(JsonWriter out, LegacyDeploymentMetric value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LegacyDeploymentMetric read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LegacyDeploymentMetric given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LegacyDeploymentMetric
   * @throws IOException if the JSON string is invalid with respect to LegacyDeploymentMetric
   */
  public static LegacyDeploymentMetric fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LegacyDeploymentMetric.class);
  }

  /**
   * Convert an instance of LegacyDeploymentMetric to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

