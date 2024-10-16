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
import java.util.UUID;

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
 * Patch the asset id of a release request body
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatchReleaseAssetIdRequest {
  public static final String SERIALIZED_NAME_IPA_UUIDS = "ipa_uuids";
  @SerializedName(SERIALIZED_NAME_IPA_UUIDS)
  private String ipaUuids;

  public static final String SERIALIZED_NAME_PACKAGE_ASSET_ID = "package_asset_id";
  @SerializedName(SERIALIZED_NAME_PACKAGE_ASSET_ID)
  private UUID packageAssetId;

  public static final String SERIALIZED_NAME_UPLOAD_ID = "upload_id";
  @SerializedName(SERIALIZED_NAME_UPLOAD_ID)
  private UUID uploadId;

  public PatchReleaseAssetIdRequest() {
  }

  public PatchReleaseAssetIdRequest ipaUuids(String ipaUuids) {
    this.ipaUuids = ipaUuids;
    return this;
  }

  /**
   * The ipa UUIDs for this release, as a serialized JSON array
   * @return ipaUuids
   */
  @javax.annotation.Nullable
  public String getIpaUuids() {
    return ipaUuids;
  }

  public void setIpaUuids(String ipaUuids) {
    this.ipaUuids = ipaUuids;
  }


  public PatchReleaseAssetIdRequest packageAssetId(UUID packageAssetId) {
    this.packageAssetId = packageAssetId;
    return this;
  }

  /**
   * The release new package id in ACFUS
   * @return packageAssetId
   */
  @javax.annotation.Nonnull
  public UUID getPackageAssetId() {
    return packageAssetId;
  }

  public void setPackageAssetId(UUID packageAssetId) {
    this.packageAssetId = packageAssetId;
  }


  public PatchReleaseAssetIdRequest uploadId(UUID uploadId) {
    this.uploadId = uploadId;
    return this;
  }

  /**
   * The release upload id used to upload the release
   * @return uploadId
   */
  @javax.annotation.Nonnull
  public UUID getUploadId() {
    return uploadId;
  }

  public void setUploadId(UUID uploadId) {
    this.uploadId = uploadId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatchReleaseAssetIdRequest patchReleaseAssetIdRequest = (PatchReleaseAssetIdRequest) o;
    return Objects.equals(this.ipaUuids, patchReleaseAssetIdRequest.ipaUuids) &&
        Objects.equals(this.packageAssetId, patchReleaseAssetIdRequest.packageAssetId) &&
        Objects.equals(this.uploadId, patchReleaseAssetIdRequest.uploadId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ipaUuids, packageAssetId, uploadId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatchReleaseAssetIdRequest {\n");
    sb.append("    ipaUuids: ").append(toIndentedString(ipaUuids)).append("\n");
    sb.append("    packageAssetId: ").append(toIndentedString(packageAssetId)).append("\n");
    sb.append("    uploadId: ").append(toIndentedString(uploadId)).append("\n");
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
    openapiFields.add("ipa_uuids");
    openapiFields.add("package_asset_id");
    openapiFields.add("upload_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("package_asset_id");
    openapiRequiredFields.add("upload_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatchReleaseAssetIdRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatchReleaseAssetIdRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatchReleaseAssetIdRequest is not found in the empty JSON string", PatchReleaseAssetIdRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatchReleaseAssetIdRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatchReleaseAssetIdRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatchReleaseAssetIdRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ipa_uuids") != null && !jsonObj.get("ipa_uuids").isJsonNull()) && !jsonObj.get("ipa_uuids").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ipa_uuids` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ipa_uuids").toString()));
      }
      if (!jsonObj.get("package_asset_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `package_asset_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("package_asset_id").toString()));
      }
      if (!jsonObj.get("upload_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `upload_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("upload_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatchReleaseAssetIdRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatchReleaseAssetIdRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatchReleaseAssetIdRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatchReleaseAssetIdRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<PatchReleaseAssetIdRequest>() {
           @Override
           public void write(JsonWriter out, PatchReleaseAssetIdRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatchReleaseAssetIdRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatchReleaseAssetIdRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatchReleaseAssetIdRequest
   * @throws IOException if the JSON string is invalid with respect to PatchReleaseAssetIdRequest
   */
  public static PatchReleaseAssetIdRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatchReleaseAssetIdRequest.class);
  }

  /**
   * Convert an instance of PatchReleaseAssetIdRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

