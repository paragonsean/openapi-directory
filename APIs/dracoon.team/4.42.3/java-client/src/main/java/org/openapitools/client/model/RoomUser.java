/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
import org.openapitools.client.model.NodePermissions;
import org.openapitools.client.model.PublicKeyContainer;
import org.openapitools.client.model.UserInfo;

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
 * User information
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RoomUser {
  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_ID = "id";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_IS_GRANTED = "isGranted";
  @SerializedName(SERIALIZED_NAME_IS_GRANTED)
  private Boolean isGranted;

  public static final String SERIALIZED_NAME_LOGIN = "login";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_LOGIN)
  private String login;

  public static final String SERIALIZED_NAME_PERMISSIONS = "permissions";
  @SerializedName(SERIALIZED_NAME_PERMISSIONS)
  private NodePermissions permissions;

  public static final String SERIALIZED_NAME_PUBLIC_KEY_CONTAINER = "publicKeyContainer";
  @SerializedName(SERIALIZED_NAME_PUBLIC_KEY_CONTAINER)
  private PublicKeyContainer publicKeyContainer;

  public static final String SERIALIZED_NAME_USER_INFO = "userInfo";
  @SerializedName(SERIALIZED_NAME_USER_INFO)
  private UserInfo userInfo;

  public RoomUser() {
  }

  @Deprecated
  public RoomUser displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  Display name  use information from &#x60;UserInfo&#x60; instead to combine a display name
   * @return displayName
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public String getDisplayName() {
    return displayName;
  }

  @Deprecated
  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  @Deprecated
  public RoomUser email(String email) {
    this.email = email;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  Email   use &#x60;email&#x60; from &#x60;UserInfo&#x60; instead
   * @return email
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public String getEmail() {
    return email;
  }

  @Deprecated
  public void setEmail(String email) {
    this.email = email;
  }


  @Deprecated
  public RoomUser id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  Unique identifier for the user  use &#x60;id&#x60; from &#x60;UserInfo&#x60; instead
   * @return id
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Long getId() {
    return id;
  }

  @Deprecated
  public void setId(Long id) {
    this.id = id;
  }


  public RoomUser isGranted(Boolean isGranted) {
    this.isGranted = isGranted;
    return this;
  }

  /**
   * Is user granted room permissions
   * @return isGranted
   */
  @javax.annotation.Nonnull
  public Boolean getIsGranted() {
    return isGranted;
  }

  public void setIsGranted(Boolean isGranted) {
    this.isGranted = isGranted;
  }


  @Deprecated
  public RoomUser login(String login) {
    this.login = login;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  User login name
   * @return login
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public String getLogin() {
    return login;
  }

  @Deprecated
  public void setLogin(String login) {
    this.login = login;
  }


  public RoomUser permissions(NodePermissions permissions) {
    this.permissions = permissions;
    return this;
  }

  /**
   * Get permissions
   * @return permissions
   */
  @javax.annotation.Nullable
  public NodePermissions getPermissions() {
    return permissions;
  }

  public void setPermissions(NodePermissions permissions) {
    this.permissions = permissions;
  }


  public RoomUser publicKeyContainer(PublicKeyContainer publicKeyContainer) {
    this.publicKeyContainer = publicKeyContainer;
    return this;
  }

  /**
   * Get publicKeyContainer
   * @return publicKeyContainer
   */
  @javax.annotation.Nullable
  public PublicKeyContainer getPublicKeyContainer() {
    return publicKeyContainer;
  }

  public void setPublicKeyContainer(PublicKeyContainer publicKeyContainer) {
    this.publicKeyContainer = publicKeyContainer;
  }


  public RoomUser userInfo(UserInfo userInfo) {
    this.userInfo = userInfo;
    return this;
  }

  /**
   * Get userInfo
   * @return userInfo
   */
  @javax.annotation.Nonnull
  public UserInfo getUserInfo() {
    return userInfo;
  }

  public void setUserInfo(UserInfo userInfo) {
    this.userInfo = userInfo;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RoomUser roomUser = (RoomUser) o;
    return Objects.equals(this.displayName, roomUser.displayName) &&
        Objects.equals(this.email, roomUser.email) &&
        Objects.equals(this.id, roomUser.id) &&
        Objects.equals(this.isGranted, roomUser.isGranted) &&
        Objects.equals(this.login, roomUser.login) &&
        Objects.equals(this.permissions, roomUser.permissions) &&
        Objects.equals(this.publicKeyContainer, roomUser.publicKeyContainer) &&
        Objects.equals(this.userInfo, roomUser.userInfo);
  }

  @Override
  public int hashCode() {
    return Objects.hash(displayName, email, id, isGranted, login, permissions, publicKeyContainer, userInfo);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RoomUser {\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isGranted: ").append(toIndentedString(isGranted)).append("\n");
    sb.append("    login: ").append(toIndentedString(login)).append("\n");
    sb.append("    permissions: ").append(toIndentedString(permissions)).append("\n");
    sb.append("    publicKeyContainer: ").append(toIndentedString(publicKeyContainer)).append("\n");
    sb.append("    userInfo: ").append(toIndentedString(userInfo)).append("\n");
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
    openapiFields.add("displayName");
    openapiFields.add("email");
    openapiFields.add("id");
    openapiFields.add("isGranted");
    openapiFields.add("login");
    openapiFields.add("permissions");
    openapiFields.add("publicKeyContainer");
    openapiFields.add("userInfo");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("displayName");
    openapiRequiredFields.add("email");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("isGranted");
    openapiRequiredFields.add("login");
    openapiRequiredFields.add("userInfo");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RoomUser
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RoomUser.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RoomUser is not found in the empty JSON string", RoomUser.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RoomUser.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RoomUser` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : RoomUser.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      if (!jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if (!jsonObj.get("login").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `login` to be a primitive type in the JSON string but got `%s`", jsonObj.get("login").toString()));
      }
      // validate the optional field `permissions`
      if (jsonObj.get("permissions") != null && !jsonObj.get("permissions").isJsonNull()) {
        NodePermissions.validateJsonElement(jsonObj.get("permissions"));
      }
      // validate the optional field `publicKeyContainer`
      if (jsonObj.get("publicKeyContainer") != null && !jsonObj.get("publicKeyContainer").isJsonNull()) {
        PublicKeyContainer.validateJsonElement(jsonObj.get("publicKeyContainer"));
      }
      // validate the required field `userInfo`
      UserInfo.validateJsonElement(jsonObj.get("userInfo"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RoomUser.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RoomUser' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RoomUser> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RoomUser.class));

       return (TypeAdapter<T>) new TypeAdapter<RoomUser>() {
           @Override
           public void write(JsonWriter out, RoomUser value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RoomUser read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RoomUser given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RoomUser
   * @throws IOException if the JSON string is invalid with respect to RoomUser
   */
  public static RoomUser fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RoomUser.class);
  }

  /**
   * Convert an instance of RoomUser to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

