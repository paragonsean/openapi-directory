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
 * LegacyCodePushReleaseResponsePackage
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LegacyCodePushReleaseResponsePackage {
  public static final String SERIALIZED_NAME_APP_VERSION = "appVersion";
  @SerializedName(SERIALIZED_NAME_APP_VERSION)
  private String appVersion;

  public static final String SERIALIZED_NAME_BLOB_URL = "blobUrl";
  @SerializedName(SERIALIZED_NAME_BLOB_URL)
  private String blobUrl;

  public static final String SERIALIZED_NAME_DIFF_PACKAGE_MAP = "diffPackageMap";
  @SerializedName(SERIALIZED_NAME_DIFF_PACKAGE_MAP)
  private Object diffPackageMap;

  public static final String SERIALIZED_NAME_IS_DISABLED = "isDisabled";
  @SerializedName(SERIALIZED_NAME_IS_DISABLED)
  private Boolean isDisabled;

  public static final String SERIALIZED_NAME_IS_MANDATORY = "isMandatory";
  @SerializedName(SERIALIZED_NAME_IS_MANDATORY)
  private Boolean isMandatory;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_MANIFEST_BLOB_URL = "manifestBlobUrl";
  @SerializedName(SERIALIZED_NAME_MANIFEST_BLOB_URL)
  private String manifestBlobUrl;

  public static final String SERIALIZED_NAME_RELEASE_METHOD = "releaseMethod";
  @SerializedName(SERIALIZED_NAME_RELEASE_METHOD)
  private String releaseMethod;

  public static final String SERIALIZED_NAME_RELEASED_BY_USER_ID = "releasedByUserId";
  @SerializedName(SERIALIZED_NAME_RELEASED_BY_USER_ID)
  private String releasedByUserId;

  public static final String SERIALIZED_NAME_ROLLOUT = "rollout";
  @SerializedName(SERIALIZED_NAME_ROLLOUT)
  private Integer rollout;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private Integer size;

  public static final String SERIALIZED_NAME_UPLOAD_TIME = "uploadTime";
  @SerializedName(SERIALIZED_NAME_UPLOAD_TIME)
  private Integer uploadTime;

  public LegacyCodePushReleaseResponsePackage() {
  }

  public LegacyCodePushReleaseResponsePackage appVersion(String appVersion) {
    this.appVersion = appVersion;
    return this;
  }

  /**
   * The version of the release
   * @return appVersion
   */
  @javax.annotation.Nullable
  public String getAppVersion() {
    return appVersion;
  }

  public void setAppVersion(String appVersion) {
    this.appVersion = appVersion;
  }


  public LegacyCodePushReleaseResponsePackage blobUrl(String blobUrl) {
    this.blobUrl = blobUrl;
    return this;
  }

  /**
   * Location (URL) of release package
   * @return blobUrl
   */
  @javax.annotation.Nullable
  public String getBlobUrl() {
    return blobUrl;
  }

  public void setBlobUrl(String blobUrl) {
    this.blobUrl = blobUrl;
  }


  public LegacyCodePushReleaseResponsePackage diffPackageMap(Object diffPackageMap) {
    this.diffPackageMap = diffPackageMap;
    return this;
  }

  /**
   * Object containing URL and size of changed package hashes contained in the release
   * @return diffPackageMap
   */
  @javax.annotation.Nullable
  public Object getDiffPackageMap() {
    return diffPackageMap;
  }

  public void setDiffPackageMap(Object diffPackageMap) {
    this.diffPackageMap = diffPackageMap;
  }


  public LegacyCodePushReleaseResponsePackage isDisabled(Boolean isDisabled) {
    this.isDisabled = isDisabled;
    return this;
  }

  /**
   * Flag used to determine if release is disabled
   * @return isDisabled
   */
  @javax.annotation.Nullable
  public Boolean getIsDisabled() {
    return isDisabled;
  }

  public void setIsDisabled(Boolean isDisabled) {
    this.isDisabled = isDisabled;
  }


  public LegacyCodePushReleaseResponsePackage isMandatory(Boolean isMandatory) {
    this.isMandatory = isMandatory;
    return this;
  }

  /**
   * Flag used to determine if release is mandatory
   * @return isMandatory
   */
  @javax.annotation.Nullable
  public Boolean getIsMandatory() {
    return isMandatory;
  }

  public void setIsMandatory(Boolean isMandatory) {
    this.isMandatory = isMandatory;
  }


  public LegacyCodePushReleaseResponsePackage label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Release label (aka release name)
   * @return label
   */
  @javax.annotation.Nullable
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public LegacyCodePushReleaseResponsePackage manifestBlobUrl(String manifestBlobUrl) {
    this.manifestBlobUrl = manifestBlobUrl;
    return this;
  }

  /**
   * The URL location of the package&#39;s manifest file.
   * @return manifestBlobUrl
   */
  @javax.annotation.Nullable
  public String getManifestBlobUrl() {
    return manifestBlobUrl;
  }

  public void setManifestBlobUrl(String manifestBlobUrl) {
    this.manifestBlobUrl = manifestBlobUrl;
  }


  public LegacyCodePushReleaseResponsePackage releaseMethod(String releaseMethod) {
    this.releaseMethod = releaseMethod;
    return this;
  }

  /**
   * Method used to deploy release
   * @return releaseMethod
   */
  @javax.annotation.Nullable
  public String getReleaseMethod() {
    return releaseMethod;
  }

  public void setReleaseMethod(String releaseMethod) {
    this.releaseMethod = releaseMethod;
  }


  public LegacyCodePushReleaseResponsePackage releasedByUserId(String releasedByUserId) {
    this.releasedByUserId = releasedByUserId;
    return this;
  }

  /**
   * User ID that triggered most recent release
   * @return releasedByUserId
   */
  @javax.annotation.Nullable
  public String getReleasedByUserId() {
    return releasedByUserId;
  }

  public void setReleasedByUserId(String releasedByUserId) {
    this.releasedByUserId = releasedByUserId;
  }


  public LegacyCodePushReleaseResponsePackage rollout(Integer rollout) {
    this.rollout = rollout;
    return this;
  }

  /**
   * Percentage (out of 100) that release is deployed to
   * @return rollout
   */
  @javax.annotation.Nullable
  public Integer getRollout() {
    return rollout;
  }

  public void setRollout(Integer rollout) {
    this.rollout = rollout;
  }


  public LegacyCodePushReleaseResponsePackage size(Integer size) {
    this.size = size;
    return this;
  }

  /**
   * Size of release package
   * @return size
   */
  @javax.annotation.Nullable
  public Integer getSize() {
    return size;
  }

  public void setSize(Integer size) {
    this.size = size;
  }


  public LegacyCodePushReleaseResponsePackage uploadTime(Integer uploadTime) {
    this.uploadTime = uploadTime;
    return this;
  }

  /**
   * Release upload time as epoch Unix timestamp
   * @return uploadTime
   */
  @javax.annotation.Nullable
  public Integer getUploadTime() {
    return uploadTime;
  }

  public void setUploadTime(Integer uploadTime) {
    this.uploadTime = uploadTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LegacyCodePushReleaseResponsePackage legacyCodePushReleaseResponsePackage = (LegacyCodePushReleaseResponsePackage) o;
    return Objects.equals(this.appVersion, legacyCodePushReleaseResponsePackage.appVersion) &&
        Objects.equals(this.blobUrl, legacyCodePushReleaseResponsePackage.blobUrl) &&
        Objects.equals(this.diffPackageMap, legacyCodePushReleaseResponsePackage.diffPackageMap) &&
        Objects.equals(this.isDisabled, legacyCodePushReleaseResponsePackage.isDisabled) &&
        Objects.equals(this.isMandatory, legacyCodePushReleaseResponsePackage.isMandatory) &&
        Objects.equals(this.label, legacyCodePushReleaseResponsePackage.label) &&
        Objects.equals(this.manifestBlobUrl, legacyCodePushReleaseResponsePackage.manifestBlobUrl) &&
        Objects.equals(this.releaseMethod, legacyCodePushReleaseResponsePackage.releaseMethod) &&
        Objects.equals(this.releasedByUserId, legacyCodePushReleaseResponsePackage.releasedByUserId) &&
        Objects.equals(this.rollout, legacyCodePushReleaseResponsePackage.rollout) &&
        Objects.equals(this.size, legacyCodePushReleaseResponsePackage.size) &&
        Objects.equals(this.uploadTime, legacyCodePushReleaseResponsePackage.uploadTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appVersion, blobUrl, diffPackageMap, isDisabled, isMandatory, label, manifestBlobUrl, releaseMethod, releasedByUserId, rollout, size, uploadTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LegacyCodePushReleaseResponsePackage {\n");
    sb.append("    appVersion: ").append(toIndentedString(appVersion)).append("\n");
    sb.append("    blobUrl: ").append(toIndentedString(blobUrl)).append("\n");
    sb.append("    diffPackageMap: ").append(toIndentedString(diffPackageMap)).append("\n");
    sb.append("    isDisabled: ").append(toIndentedString(isDisabled)).append("\n");
    sb.append("    isMandatory: ").append(toIndentedString(isMandatory)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    manifestBlobUrl: ").append(toIndentedString(manifestBlobUrl)).append("\n");
    sb.append("    releaseMethod: ").append(toIndentedString(releaseMethod)).append("\n");
    sb.append("    releasedByUserId: ").append(toIndentedString(releasedByUserId)).append("\n");
    sb.append("    rollout: ").append(toIndentedString(rollout)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    uploadTime: ").append(toIndentedString(uploadTime)).append("\n");
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
    openapiFields.add("appVersion");
    openapiFields.add("blobUrl");
    openapiFields.add("diffPackageMap");
    openapiFields.add("isDisabled");
    openapiFields.add("isMandatory");
    openapiFields.add("label");
    openapiFields.add("manifestBlobUrl");
    openapiFields.add("releaseMethod");
    openapiFields.add("releasedByUserId");
    openapiFields.add("rollout");
    openapiFields.add("size");
    openapiFields.add("uploadTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LegacyCodePushReleaseResponsePackage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LegacyCodePushReleaseResponsePackage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LegacyCodePushReleaseResponsePackage is not found in the empty JSON string", LegacyCodePushReleaseResponsePackage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LegacyCodePushReleaseResponsePackage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LegacyCodePushReleaseResponsePackage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appVersion") != null && !jsonObj.get("appVersion").isJsonNull()) && !jsonObj.get("appVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appVersion").toString()));
      }
      if ((jsonObj.get("blobUrl") != null && !jsonObj.get("blobUrl").isJsonNull()) && !jsonObj.get("blobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `blobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("blobUrl").toString()));
      }
      if ((jsonObj.get("label") != null && !jsonObj.get("label").isJsonNull()) && !jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      if ((jsonObj.get("manifestBlobUrl") != null && !jsonObj.get("manifestBlobUrl").isJsonNull()) && !jsonObj.get("manifestBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `manifestBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("manifestBlobUrl").toString()));
      }
      if ((jsonObj.get("releaseMethod") != null && !jsonObj.get("releaseMethod").isJsonNull()) && !jsonObj.get("releaseMethod").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `releaseMethod` to be a primitive type in the JSON string but got `%s`", jsonObj.get("releaseMethod").toString()));
      }
      if ((jsonObj.get("releasedByUserId") != null && !jsonObj.get("releasedByUserId").isJsonNull()) && !jsonObj.get("releasedByUserId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `releasedByUserId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("releasedByUserId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LegacyCodePushReleaseResponsePackage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LegacyCodePushReleaseResponsePackage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LegacyCodePushReleaseResponsePackage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LegacyCodePushReleaseResponsePackage.class));

       return (TypeAdapter<T>) new TypeAdapter<LegacyCodePushReleaseResponsePackage>() {
           @Override
           public void write(JsonWriter out, LegacyCodePushReleaseResponsePackage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LegacyCodePushReleaseResponsePackage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LegacyCodePushReleaseResponsePackage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LegacyCodePushReleaseResponsePackage
   * @throws IOException if the JSON string is invalid with respect to LegacyCodePushReleaseResponsePackage
   */
  public static LegacyCodePushReleaseResponsePackage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LegacyCodePushReleaseResponsePackage.class);
  }

  /**
   * Convert an instance of LegacyCodePushReleaseResponsePackage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

