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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner {
  public static final String SERIALIZED_NAME_APP_ID = "app_id";
  @SerializedName(SERIALIZED_NAME_APP_ID)
  private String appId;

  public static final String SERIALIZED_NAME_ORIGIN = "origin";
  @SerializedName(SERIALIZED_NAME_ORIGIN)
  private String origin;

  public static final String SERIALIZED_NAME_PERMISSIONS = "permissions";
  @SerializedName(SERIALIZED_NAME_PERMISSIONS)
  private List<String> permissions = new ArrayList<>();

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner() {
  }

  public AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner appId(String appId) {
    this.appId = appId;
    return this;
  }

  /**
   * Get appId
   * @return appId
   */
  @javax.annotation.Nullable
  public String getAppId() {
    return appId;
  }

  public void setAppId(String appId) {
    this.appId = appId;
  }


  public AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner origin(String origin) {
    this.origin = origin;
    return this;
  }

  /**
   * Get origin
   * @return origin
   */
  @javax.annotation.Nullable
  public String getOrigin() {
    return origin;
  }

  public void setOrigin(String origin) {
    this.origin = origin;
  }


  public AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner permissions(List<String> permissions) {
    this.permissions = permissions;
    return this;
  }

  public AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner addPermissionsItem(String permissionsItem) {
    if (this.permissions == null) {
      this.permissions = new ArrayList<>();
    }
    this.permissions.add(permissionsItem);
    return this;
  }

  /**
   * Get permissions
   * @return permissions
   */
  @javax.annotation.Nullable
  public List<String> getPermissions() {
    return permissions;
  }

  public void setPermissions(List<String> permissions) {
    this.permissions = permissions;
  }


  public AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * Get userId
   * @return userId
   */
  @javax.annotation.Nullable
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner appMembershipsValidationResponseAppUsersWithMissingMembershipsInner = (AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner) o;
    return Objects.equals(this.appId, appMembershipsValidationResponseAppUsersWithMissingMembershipsInner.appId) &&
        Objects.equals(this.origin, appMembershipsValidationResponseAppUsersWithMissingMembershipsInner.origin) &&
        Objects.equals(this.permissions, appMembershipsValidationResponseAppUsersWithMissingMembershipsInner.permissions) &&
        Objects.equals(this.userId, appMembershipsValidationResponseAppUsersWithMissingMembershipsInner.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appId, origin, permissions, userId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner {\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    origin: ").append(toIndentedString(origin)).append("\n");
    sb.append("    permissions: ").append(toIndentedString(permissions)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
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
    openapiFields.add("origin");
    openapiFields.add("permissions");
    openapiFields.add("user_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner is not found in the empty JSON string", AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("app_id") != null && !jsonObj.get("app_id").isJsonNull()) && !jsonObj.get("app_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `app_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("app_id").toString()));
      }
      if ((jsonObj.get("origin") != null && !jsonObj.get("origin").isJsonNull()) && !jsonObj.get("origin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `origin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("origin").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("permissions") != null && !jsonObj.get("permissions").isJsonNull() && !jsonObj.get("permissions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `permissions` to be an array in the JSON string but got `%s`", jsonObj.get("permissions").toString()));
      }
      if ((jsonObj.get("user_id") != null && !jsonObj.get("user_id").isJsonNull()) && !jsonObj.get("user_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner>() {
           @Override
           public void write(JsonWriter out, AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner
   * @throws IOException if the JSON string is invalid with respect to AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner
   */
  public static AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner.class);
  }

  /**
   * Convert an instance of AppMembershipsValidationResponseAppUsersWithMissingMembershipsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

