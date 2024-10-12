/*
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
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
 * GetNotifications200ResponseNotificationsInnerData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:34.324076-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNotifications200ResponseNotificationsInnerData {
  public static final String SERIALIZED_NAME_BADGE_ID = "badge_id";
  @SerializedName(SERIALIZED_NAME_BADGE_ID)
  private Integer badgeId;

  public static final String SERIALIZED_NAME_BADGE_NAME = "badge_name";
  @SerializedName(SERIALIZED_NAME_BADGE_NAME)
  private String badgeName;

  public static final String SERIALIZED_NAME_BADGE_SLUG = "badge_slug";
  @SerializedName(SERIALIZED_NAME_BADGE_SLUG)
  private String badgeSlug;

  public static final String SERIALIZED_NAME_BADGE_TITLE = "badge_title";
  @SerializedName(SERIALIZED_NAME_BADGE_TITLE)
  private Boolean badgeTitle;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public GetNotifications200ResponseNotificationsInnerData() {
  }

  public GetNotifications200ResponseNotificationsInnerData badgeId(Integer badgeId) {
    this.badgeId = badgeId;
    return this;
  }

  /**
   * Get badgeId
   * @return badgeId
   */
  @javax.annotation.Nullable
  public Integer getBadgeId() {
    return badgeId;
  }

  public void setBadgeId(Integer badgeId) {
    this.badgeId = badgeId;
  }


  public GetNotifications200ResponseNotificationsInnerData badgeName(String badgeName) {
    this.badgeName = badgeName;
    return this;
  }

  /**
   * Get badgeName
   * @return badgeName
   */
  @javax.annotation.Nullable
  public String getBadgeName() {
    return badgeName;
  }

  public void setBadgeName(String badgeName) {
    this.badgeName = badgeName;
  }


  public GetNotifications200ResponseNotificationsInnerData badgeSlug(String badgeSlug) {
    this.badgeSlug = badgeSlug;
    return this;
  }

  /**
   * Get badgeSlug
   * @return badgeSlug
   */
  @javax.annotation.Nullable
  public String getBadgeSlug() {
    return badgeSlug;
  }

  public void setBadgeSlug(String badgeSlug) {
    this.badgeSlug = badgeSlug;
  }


  public GetNotifications200ResponseNotificationsInnerData badgeTitle(Boolean badgeTitle) {
    this.badgeTitle = badgeTitle;
    return this;
  }

  /**
   * Get badgeTitle
   * @return badgeTitle
   */
  @javax.annotation.Nullable
  public Boolean getBadgeTitle() {
    return badgeTitle;
  }

  public void setBadgeTitle(Boolean badgeTitle) {
    this.badgeTitle = badgeTitle;
  }


  public GetNotifications200ResponseNotificationsInnerData username(String username) {
    this.username = username;
    return this;
  }

  /**
   * Get username
   * @return username
   */
  @javax.annotation.Nullable
  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNotifications200ResponseNotificationsInnerData getNotifications200ResponseNotificationsInnerData = (GetNotifications200ResponseNotificationsInnerData) o;
    return Objects.equals(this.badgeId, getNotifications200ResponseNotificationsInnerData.badgeId) &&
        Objects.equals(this.badgeName, getNotifications200ResponseNotificationsInnerData.badgeName) &&
        Objects.equals(this.badgeSlug, getNotifications200ResponseNotificationsInnerData.badgeSlug) &&
        Objects.equals(this.badgeTitle, getNotifications200ResponseNotificationsInnerData.badgeTitle) &&
        Objects.equals(this.username, getNotifications200ResponseNotificationsInnerData.username);
  }

  @Override
  public int hashCode() {
    return Objects.hash(badgeId, badgeName, badgeSlug, badgeTitle, username);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNotifications200ResponseNotificationsInnerData {\n");
    sb.append("    badgeId: ").append(toIndentedString(badgeId)).append("\n");
    sb.append("    badgeName: ").append(toIndentedString(badgeName)).append("\n");
    sb.append("    badgeSlug: ").append(toIndentedString(badgeSlug)).append("\n");
    sb.append("    badgeTitle: ").append(toIndentedString(badgeTitle)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
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
    openapiFields.add("badge_id");
    openapiFields.add("badge_name");
    openapiFields.add("badge_slug");
    openapiFields.add("badge_title");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNotifications200ResponseNotificationsInnerData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNotifications200ResponseNotificationsInnerData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNotifications200ResponseNotificationsInnerData is not found in the empty JSON string", GetNotifications200ResponseNotificationsInnerData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNotifications200ResponseNotificationsInnerData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNotifications200ResponseNotificationsInnerData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("badge_name") != null && !jsonObj.get("badge_name").isJsonNull()) && !jsonObj.get("badge_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `badge_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("badge_name").toString()));
      }
      if ((jsonObj.get("badge_slug") != null && !jsonObj.get("badge_slug").isJsonNull()) && !jsonObj.get("badge_slug").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `badge_slug` to be a primitive type in the JSON string but got `%s`", jsonObj.get("badge_slug").toString()));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNotifications200ResponseNotificationsInnerData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNotifications200ResponseNotificationsInnerData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNotifications200ResponseNotificationsInnerData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNotifications200ResponseNotificationsInnerData.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNotifications200ResponseNotificationsInnerData>() {
           @Override
           public void write(JsonWriter out, GetNotifications200ResponseNotificationsInnerData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNotifications200ResponseNotificationsInnerData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNotifications200ResponseNotificationsInnerData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNotifications200ResponseNotificationsInnerData
   * @throws IOException if the JSON string is invalid with respect to GetNotifications200ResponseNotificationsInnerData
   */
  public static GetNotifications200ResponseNotificationsInnerData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNotifications200ResponseNotificationsInnerData.class);
  }

  /**
   * Convert an instance of GetNotifications200ResponseNotificationsInnerData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

