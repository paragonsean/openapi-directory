/*
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
 * AvailableVersions
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:46.845451-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AvailableVersions {
  public static final String SERIALIZED_NAME_AVAILABLE = "available";
  @SerializedName(SERIALIZED_NAME_AVAILABLE)
  private String available;

  public static final String SERIALIZED_NAME_AVAILABLE_FROM_DATE = "available_from_date";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_FROM_DATE)
  private String availableFromDate;

  public static final String SERIALIZED_NAME_AVAILABLE_TO_DATE = "available_to_date";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_TO_DATE)
  private String availableToDate;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private String duration;

  public static final String SERIALIZED_NAME_HAS_GUIDANCE = "has_guidance";
  @SerializedName(SERIALIZED_NAME_HAS_GUIDANCE)
  private Boolean hasGuidance;

  public static final String SERIALIZED_NAME_MEDIA_SET = "media_set";
  @SerializedName(SERIALIZED_NAME_MEDIA_SET)
  private String mediaSet;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_VERSION_PID = "version_pid";
  @SerializedName(SERIALIZED_NAME_VERSION_PID)
  private String versionPid;

  public static final String SERIALIZED_NAME_VERSION_TYPE = "version_type";
  @SerializedName(SERIALIZED_NAME_VERSION_TYPE)
  private String versionType;

  public AvailableVersions() {
  }

  public AvailableVersions available(String available) {
    this.available = available;
    return this;
  }

  /**
   * Get available
   * @return available
   */
  @javax.annotation.Nonnull
  public String getAvailable() {
    return available;
  }

  public void setAvailable(String available) {
    this.available = available;
  }


  public AvailableVersions availableFromDate(String availableFromDate) {
    this.availableFromDate = availableFromDate;
    return this;
  }

  /**
   * Get availableFromDate
   * @return availableFromDate
   */
  @javax.annotation.Nonnull
  public String getAvailableFromDate() {
    return availableFromDate;
  }

  public void setAvailableFromDate(String availableFromDate) {
    this.availableFromDate = availableFromDate;
  }


  public AvailableVersions availableToDate(String availableToDate) {
    this.availableToDate = availableToDate;
    return this;
  }

  /**
   * Get availableToDate
   * @return availableToDate
   */
  @javax.annotation.Nonnull
  public String getAvailableToDate() {
    return availableToDate;
  }

  public void setAvailableToDate(String availableToDate) {
    this.availableToDate = availableToDate;
  }


  public AvailableVersions duration(String duration) {
    this.duration = duration;
    return this;
  }

  /**
   * Get duration
   * @return duration
   */
  @javax.annotation.Nonnull
  public String getDuration() {
    return duration;
  }

  public void setDuration(String duration) {
    this.duration = duration;
  }


  public AvailableVersions hasGuidance(Boolean hasGuidance) {
    this.hasGuidance = hasGuidance;
    return this;
  }

  /**
   * Get hasGuidance
   * @return hasGuidance
   */
  @javax.annotation.Nonnull
  public Boolean getHasGuidance() {
    return hasGuidance;
  }

  public void setHasGuidance(Boolean hasGuidance) {
    this.hasGuidance = hasGuidance;
  }


  public AvailableVersions mediaSet(String mediaSet) {
    this.mediaSet = mediaSet;
    return this;
  }

  /**
   * Get mediaSet
   * @return mediaSet
   */
  @javax.annotation.Nonnull
  public String getMediaSet() {
    return mediaSet;
  }

  public void setMediaSet(String mediaSet) {
    this.mediaSet = mediaSet;
  }


  public AvailableVersions type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public AvailableVersions versionPid(String versionPid) {
    this.versionPid = versionPid;
    return this;
  }

  /**
   * Get versionPid
   * @return versionPid
   */
  @javax.annotation.Nonnull
  public String getVersionPid() {
    return versionPid;
  }

  public void setVersionPid(String versionPid) {
    this.versionPid = versionPid;
  }


  public AvailableVersions versionType(String versionType) {
    this.versionType = versionType;
    return this;
  }

  /**
   * Get versionType
   * @return versionType
   */
  @javax.annotation.Nonnull
  public String getVersionType() {
    return versionType;
  }

  public void setVersionType(String versionType) {
    this.versionType = versionType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AvailableVersions availableVersions = (AvailableVersions) o;
    return Objects.equals(this.available, availableVersions.available) &&
        Objects.equals(this.availableFromDate, availableVersions.availableFromDate) &&
        Objects.equals(this.availableToDate, availableVersions.availableToDate) &&
        Objects.equals(this.duration, availableVersions.duration) &&
        Objects.equals(this.hasGuidance, availableVersions.hasGuidance) &&
        Objects.equals(this.mediaSet, availableVersions.mediaSet) &&
        Objects.equals(this.type, availableVersions.type) &&
        Objects.equals(this.versionPid, availableVersions.versionPid) &&
        Objects.equals(this.versionType, availableVersions.versionType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(available, availableFromDate, availableToDate, duration, hasGuidance, mediaSet, type, versionPid, versionType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AvailableVersions {\n");
    sb.append("    available: ").append(toIndentedString(available)).append("\n");
    sb.append("    availableFromDate: ").append(toIndentedString(availableFromDate)).append("\n");
    sb.append("    availableToDate: ").append(toIndentedString(availableToDate)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    hasGuidance: ").append(toIndentedString(hasGuidance)).append("\n");
    sb.append("    mediaSet: ").append(toIndentedString(mediaSet)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    versionPid: ").append(toIndentedString(versionPid)).append("\n");
    sb.append("    versionType: ").append(toIndentedString(versionType)).append("\n");
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
    openapiFields.add("available");
    openapiFields.add("available_from_date");
    openapiFields.add("available_to_date");
    openapiFields.add("duration");
    openapiFields.add("has_guidance");
    openapiFields.add("media_set");
    openapiFields.add("type");
    openapiFields.add("version_pid");
    openapiFields.add("version_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("available");
    openapiRequiredFields.add("available_from_date");
    openapiRequiredFields.add("available_to_date");
    openapiRequiredFields.add("duration");
    openapiRequiredFields.add("has_guidance");
    openapiRequiredFields.add("media_set");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("version_pid");
    openapiRequiredFields.add("version_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AvailableVersions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AvailableVersions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AvailableVersions is not found in the empty JSON string", AvailableVersions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AvailableVersions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AvailableVersions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AvailableVersions.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("available").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `available` to be a primitive type in the JSON string but got `%s`", jsonObj.get("available").toString()));
      }
      if (!jsonObj.get("available_from_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `available_from_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("available_from_date").toString()));
      }
      if (!jsonObj.get("available_to_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `available_to_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("available_to_date").toString()));
      }
      if (!jsonObj.get("duration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `duration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("duration").toString()));
      }
      if (!jsonObj.get("media_set").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `media_set` to be a primitive type in the JSON string but got `%s`", jsonObj.get("media_set").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      if (!jsonObj.get("version_pid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version_pid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version_pid").toString()));
      }
      if (!jsonObj.get("version_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version_type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AvailableVersions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AvailableVersions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AvailableVersions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AvailableVersions.class));

       return (TypeAdapter<T>) new TypeAdapter<AvailableVersions>() {
           @Override
           public void write(JsonWriter out, AvailableVersions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AvailableVersions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AvailableVersions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AvailableVersions
   * @throws IOException if the JSON string is invalid with respect to AvailableVersions
   */
  public static AvailableVersions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AvailableVersions.class);
  }

  /**
   * Convert an instance of AvailableVersions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

