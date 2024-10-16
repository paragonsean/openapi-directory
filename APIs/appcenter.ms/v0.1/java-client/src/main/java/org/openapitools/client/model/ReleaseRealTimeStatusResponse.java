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
import org.openapitools.client.model.StoreReleasesGetRealTimeStatusByReleaseId200ResponseStatus;

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
 * status of the app from store
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReleaseRealTimeStatusResponse {
  public static final String SERIALIZED_NAME_APP_ID = "app_id";
  @SerializedName(SERIALIZED_NAME_APP_ID)
  private String appId;

  public static final String SERIALIZED_NAME_RELEASE_ID = "release_id";
  @SerializedName(SERIALIZED_NAME_RELEASE_ID)
  private String releaseId;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StoreReleasesGetRealTimeStatusByReleaseId200ResponseStatus status;

  public ReleaseRealTimeStatusResponse() {
  }

  public ReleaseRealTimeStatusResponse appId(String appId) {
    this.appId = appId;
    return this;
  }

  /**
   * app id
   * @return appId
   */
  @javax.annotation.Nullable
  public String getAppId() {
    return appId;
  }

  public void setAppId(String appId) {
    this.appId = appId;
  }


  public ReleaseRealTimeStatusResponse releaseId(String releaseId) {
    this.releaseId = releaseId;
    return this;
  }

  /**
   * release id
   * @return releaseId
   */
  @javax.annotation.Nullable
  public String getReleaseId() {
    return releaseId;
  }

  public void setReleaseId(String releaseId) {
    this.releaseId = releaseId;
  }


  public ReleaseRealTimeStatusResponse status(StoreReleasesGetRealTimeStatusByReleaseId200ResponseStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public StoreReleasesGetRealTimeStatusByReleaseId200ResponseStatus getStatus() {
    return status;
  }

  public void setStatus(StoreReleasesGetRealTimeStatusByReleaseId200ResponseStatus status) {
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
    ReleaseRealTimeStatusResponse releaseRealTimeStatusResponse = (ReleaseRealTimeStatusResponse) o;
    return Objects.equals(this.appId, releaseRealTimeStatusResponse.appId) &&
        Objects.equals(this.releaseId, releaseRealTimeStatusResponse.releaseId) &&
        Objects.equals(this.status, releaseRealTimeStatusResponse.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appId, releaseId, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReleaseRealTimeStatusResponse {\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    releaseId: ").append(toIndentedString(releaseId)).append("\n");
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
    openapiFields.add("app_id");
    openapiFields.add("release_id");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReleaseRealTimeStatusResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReleaseRealTimeStatusResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReleaseRealTimeStatusResponse is not found in the empty JSON string", ReleaseRealTimeStatusResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReleaseRealTimeStatusResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReleaseRealTimeStatusResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("app_id") != null && !jsonObj.get("app_id").isJsonNull()) && !jsonObj.get("app_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `app_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("app_id").toString()));
      }
      if ((jsonObj.get("release_id") != null && !jsonObj.get("release_id").isJsonNull()) && !jsonObj.get("release_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `release_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("release_id").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StoreReleasesGetRealTimeStatusByReleaseId200ResponseStatus.validateJsonElement(jsonObj.get("status"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReleaseRealTimeStatusResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReleaseRealTimeStatusResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReleaseRealTimeStatusResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReleaseRealTimeStatusResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<ReleaseRealTimeStatusResponse>() {
           @Override
           public void write(JsonWriter out, ReleaseRealTimeStatusResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReleaseRealTimeStatusResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReleaseRealTimeStatusResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReleaseRealTimeStatusResponse
   * @throws IOException if the JSON string is invalid with respect to ReleaseRealTimeStatusResponse
   */
  public static ReleaseRealTimeStatusResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReleaseRealTimeStatusResponse.class);
  }

  /**
   * Convert an instance of ReleaseRealTimeStatusResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

