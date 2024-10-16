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
 * RepoConfigCommon
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RepoConfigCommon {
  public static final String SERIALIZED_NAME_EXTERNAL_USER_ID = "external_user_id";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_USER_ID)
  private String externalUserId;

  public static final String SERIALIZED_NAME_REPO_ID = "repo_id";
  @SerializedName(SERIALIZED_NAME_REPO_ID)
  private String repoId;

  public static final String SERIALIZED_NAME_REPO_URL = "repo_url";
  @SerializedName(SERIALIZED_NAME_REPO_URL)
  private String repoUrl;

  public static final String SERIALIZED_NAME_SERVICE_CONNECTION_ID = "service_connection_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_CONNECTION_ID)
  private String serviceConnectionId;

  public RepoConfigCommon() {
  }

  public RepoConfigCommon externalUserId(String externalUserId) {
    this.externalUserId = externalUserId;
    return this;
  }

  /**
   * The external user id from the repository provider. Required for GitLab.com repositories
   * @return externalUserId
   */
  @javax.annotation.Nullable
  public String getExternalUserId() {
    return externalUserId;
  }

  public void setExternalUserId(String externalUserId) {
    this.externalUserId = externalUserId;
  }


  public RepoConfigCommon repoId(String repoId) {
    this.repoId = repoId;
    return this;
  }

  /**
   * The repository id from the repository provider. Required for repositories connected from GitHub App and GitLab.com
   * @return repoId
   */
  @javax.annotation.Nullable
  public String getRepoId() {
    return repoId;
  }

  public void setRepoId(String repoId) {
    this.repoId = repoId;
  }


  public RepoConfigCommon repoUrl(String repoUrl) {
    this.repoUrl = repoUrl;
    return this;
  }

  /**
   * The repository&#39;s git url, must be a HTTPS URL
   * @return repoUrl
   */
  @javax.annotation.Nullable
  public String getRepoUrl() {
    return repoUrl;
  }

  public void setRepoUrl(String repoUrl) {
    this.repoUrl = repoUrl;
  }


  public RepoConfigCommon serviceConnectionId(String serviceConnectionId) {
    this.serviceConnectionId = serviceConnectionId;
    return this;
  }

  /**
   * The id of the service connection (private). Required for GitLab self-hosted repositories
   * @return serviceConnectionId
   */
  @javax.annotation.Nullable
  public String getServiceConnectionId() {
    return serviceConnectionId;
  }

  public void setServiceConnectionId(String serviceConnectionId) {
    this.serviceConnectionId = serviceConnectionId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RepoConfigCommon repoConfigCommon = (RepoConfigCommon) o;
    return Objects.equals(this.externalUserId, repoConfigCommon.externalUserId) &&
        Objects.equals(this.repoId, repoConfigCommon.repoId) &&
        Objects.equals(this.repoUrl, repoConfigCommon.repoUrl) &&
        Objects.equals(this.serviceConnectionId, repoConfigCommon.serviceConnectionId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(externalUserId, repoId, repoUrl, serviceConnectionId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RepoConfigCommon {\n");
    sb.append("    externalUserId: ").append(toIndentedString(externalUserId)).append("\n");
    sb.append("    repoId: ").append(toIndentedString(repoId)).append("\n");
    sb.append("    repoUrl: ").append(toIndentedString(repoUrl)).append("\n");
    sb.append("    serviceConnectionId: ").append(toIndentedString(serviceConnectionId)).append("\n");
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
    openapiFields.add("external_user_id");
    openapiFields.add("repo_id");
    openapiFields.add("repo_url");
    openapiFields.add("service_connection_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RepoConfigCommon
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RepoConfigCommon.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RepoConfigCommon is not found in the empty JSON string", RepoConfigCommon.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RepoConfigCommon.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RepoConfigCommon` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("external_user_id") != null && !jsonObj.get("external_user_id").isJsonNull()) && !jsonObj.get("external_user_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `external_user_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("external_user_id").toString()));
      }
      if ((jsonObj.get("repo_id") != null && !jsonObj.get("repo_id").isJsonNull()) && !jsonObj.get("repo_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `repo_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("repo_id").toString()));
      }
      if ((jsonObj.get("repo_url") != null && !jsonObj.get("repo_url").isJsonNull()) && !jsonObj.get("repo_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `repo_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("repo_url").toString()));
      }
      if ((jsonObj.get("service_connection_id") != null && !jsonObj.get("service_connection_id").isJsonNull()) && !jsonObj.get("service_connection_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_connection_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_connection_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RepoConfigCommon.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RepoConfigCommon' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RepoConfigCommon> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RepoConfigCommon.class));

       return (TypeAdapter<T>) new TypeAdapter<RepoConfigCommon>() {
           @Override
           public void write(JsonWriter out, RepoConfigCommon value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RepoConfigCommon read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RepoConfigCommon given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RepoConfigCommon
   * @throws IOException if the JSON string is invalid with respect to RepoConfigCommon
   */
  public static RepoConfigCommon fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RepoConfigCommon.class);
  }

  /**
   * Convert an instance of RepoConfigCommon to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

