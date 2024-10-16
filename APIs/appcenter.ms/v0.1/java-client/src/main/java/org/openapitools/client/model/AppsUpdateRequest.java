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
 * AppsUpdateRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppsUpdateRequest {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "display_name";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_ICON_ASSET_ID = "icon_asset_id";
  @SerializedName(SERIALIZED_NAME_ICON_ASSET_ID)
  private UUID iconAssetId;

  public static final String SERIALIZED_NAME_ICON_URL = "icon_url";
  @SerializedName(SERIALIZED_NAME_ICON_URL)
  private String iconUrl;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_RELEASE_TYPE = "release_type";
  @SerializedName(SERIALIZED_NAME_RELEASE_TYPE)
  private String releaseType;

  public AppsUpdateRequest() {
  }

  public AppsUpdateRequest description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A short text describing the app
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AppsUpdateRequest displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * The display name of the app
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public AppsUpdateRequest iconAssetId(UUID iconAssetId) {
    this.iconAssetId = iconAssetId;
    return this;
  }

  /**
   * The uuid for the icon&#39;s asset id from ACFUS
   * @return iconAssetId
   */
  @javax.annotation.Nullable
  public UUID getIconAssetId() {
    return iconAssetId;
  }

  public void setIconAssetId(UUID iconAssetId) {
    this.iconAssetId = iconAssetId;
  }


  public AppsUpdateRequest iconUrl(String iconUrl) {
    this.iconUrl = iconUrl;
    return this;
  }

  /**
   * The string representation of the URL pointing to the app&#39;s icon
   * @return iconUrl
   */
  @javax.annotation.Nullable
  public String getIconUrl() {
    return iconUrl;
  }

  public void setIconUrl(String iconUrl) {
    this.iconUrl = iconUrl;
  }


  public AppsUpdateRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the app used in URLs
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public AppsUpdateRequest releaseType(String releaseType) {
    this.releaseType = releaseType;
    return this;
  }

  /**
   * A one-word descriptive release type value that starts with a capital letter but is otherwise lowercase
   * @return releaseType
   */
  @javax.annotation.Nullable
  public String getReleaseType() {
    return releaseType;
  }

  public void setReleaseType(String releaseType) {
    this.releaseType = releaseType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppsUpdateRequest appsUpdateRequest = (AppsUpdateRequest) o;
    return Objects.equals(this.description, appsUpdateRequest.description) &&
        Objects.equals(this.displayName, appsUpdateRequest.displayName) &&
        Objects.equals(this.iconAssetId, appsUpdateRequest.iconAssetId) &&
        Objects.equals(this.iconUrl, appsUpdateRequest.iconUrl) &&
        Objects.equals(this.name, appsUpdateRequest.name) &&
        Objects.equals(this.releaseType, appsUpdateRequest.releaseType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, displayName, iconAssetId, iconUrl, name, releaseType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppsUpdateRequest {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    iconAssetId: ").append(toIndentedString(iconAssetId)).append("\n");
    sb.append("    iconUrl: ").append(toIndentedString(iconUrl)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    releaseType: ").append(toIndentedString(releaseType)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("display_name");
    openapiFields.add("icon_asset_id");
    openapiFields.add("icon_url");
    openapiFields.add("name");
    openapiFields.add("release_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppsUpdateRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppsUpdateRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppsUpdateRequest is not found in the empty JSON string", AppsUpdateRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppsUpdateRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppsUpdateRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("display_name") != null && !jsonObj.get("display_name").isJsonNull()) && !jsonObj.get("display_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_name").toString()));
      }
      if ((jsonObj.get("icon_asset_id") != null && !jsonObj.get("icon_asset_id").isJsonNull()) && !jsonObj.get("icon_asset_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon_asset_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon_asset_id").toString()));
      }
      if ((jsonObj.get("icon_url") != null && !jsonObj.get("icon_url").isJsonNull()) && !jsonObj.get("icon_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon_url").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("release_type") != null && !jsonObj.get("release_type").isJsonNull()) && !jsonObj.get("release_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `release_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("release_type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppsUpdateRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppsUpdateRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppsUpdateRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppsUpdateRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AppsUpdateRequest>() {
           @Override
           public void write(JsonWriter out, AppsUpdateRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppsUpdateRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppsUpdateRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppsUpdateRequest
   * @throws IOException if the JSON string is invalid with respect to AppsUpdateRequest
   */
  public static AppsUpdateRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppsUpdateRequest.class);
  }

  /**
   * Convert an instance of AppsUpdateRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

