/*
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
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
import org.openapitools.client.model.UserPermissions;

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
 * UpdateUserRequestBody
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:39.505408-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateUserRequestBody {
  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_EXPIRATION = "expiration";
  @SerializedName(SERIALIZED_NAME_EXPIRATION)
  private String expiration;

  public static final String SERIALIZED_NAME_HOME_RESOURCE = "homeResource";
  @SerializedName(SERIALIZED_NAME_HOME_RESOURCE)
  private String homeResource;

  public static final String SERIALIZED_NAME_LOCKED = "locked";
  @SerializedName(SERIALIZED_NAME_LOCKED)
  private Boolean locked;

  public static final String SERIALIZED_NAME_NICKNAME = "nickname";
  @SerializedName(SERIALIZED_NAME_NICKNAME)
  private String nickname;

  public static final String SERIALIZED_NAME_ONBOARDING = "onboarding";
  @SerializedName(SERIALIZED_NAME_ONBOARDING)
  private Boolean onboarding;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_PERMISSIONS = "permissions";
  @SerializedName(SERIALIZED_NAME_PERMISSIONS)
  private UserPermissions permissions;

  /**
   * The type of user (**admin** or **user**). Note that admin users cannot have a &#x60;homeResource&#x60; other than &#39;/&#39;, and will have full permissions, but you must provide at least \&quot;download,upload,list,delete\&quot; in the &#x60;permissions&#x60; parameter.
   */
  @JsonAdapter(RoleEnum.Adapter.class)
  public enum RoleEnum {
    USER("user"),
    
    ADMIN("admin");

    private String value;

    RoleEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RoleEnum fromValue(String value) {
      for (RoleEnum b : RoleEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RoleEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RoleEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RoleEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RoleEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RoleEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ROLE = "role";
  @SerializedName(SERIALIZED_NAME_ROLE)
  private RoleEnum role;

  public static final String SERIALIZED_NAME_TIME_ZONE = "timeZone";
  @SerializedName(SERIALIZED_NAME_TIME_ZONE)
  private String timeZone;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public UpdateUserRequestBody() {
  }

  public UpdateUserRequestBody email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Email address for the user
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public UpdateUserRequestBody expiration(String expiration) {
    this.expiration = expiration;
    return this;
  }

  /**
   * Optional timestamp when the user should expire.
   * @return expiration
   */
  @javax.annotation.Nullable
  public String getExpiration() {
    return expiration;
  }

  public void setExpiration(String expiration) {
    this.expiration = expiration;
  }


  public UpdateUserRequestBody homeResource(String homeResource) {
    this.homeResource = homeResource;
    return this;
  }

  /**
   * Resource identifier for the user&#39;s home folder. See details on [how to specify resources](#section/Identifying-Resources) above.  The user will be locked to this directory and unable to move &#39;up&#39; in the account. If the folder does not exist in the account, it will be created when the user logs in.  This setting is ignored for users with the &#x60;role&#x60; **admin**.
   * @return homeResource
   */
  @javax.annotation.Nullable
  public String getHomeResource() {
    return homeResource;
  }

  public void setHomeResource(String homeResource) {
    this.homeResource = homeResource;
  }


  public UpdateUserRequestBody locked(Boolean locked) {
    this.locked = locked;
    return this;
  }

  /**
   * If true, the user will be prevented from logging in
   * @return locked
   */
  @javax.annotation.Nullable
  public Boolean getLocked() {
    return locked;
  }

  public void setLocked(Boolean locked) {
    this.locked = locked;
  }


  public UpdateUserRequestBody nickname(String nickname) {
    this.nickname = nickname;
    return this;
  }

  /**
   * An optional nickname (e.g. &#39;David from Sales&#39;).
   * @return nickname
   */
  @javax.annotation.Nullable
  public String getNickname() {
    return nickname;
  }

  public void setNickname(String nickname) {
    this.nickname = nickname;
  }


  public UpdateUserRequestBody onboarding(Boolean onboarding) {
    this.onboarding = onboarding;
    return this;
  }

  /**
   * Set this to **true** to enable extra help popups in the web file manager for this user.
   * @return onboarding
   */
  @javax.annotation.Nullable
  public Boolean getOnboarding() {
    return onboarding;
  }

  public void setOnboarding(Boolean onboarding) {
    this.onboarding = onboarding;
  }


  public UpdateUserRequestBody password(String password) {
    this.password = password;
    return this;
  }

  /**
   * New password for the user
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public UpdateUserRequestBody permissions(UserPermissions permissions) {
    this.permissions = permissions;
    return this;
  }

  /**
   * Get permissions
   * @return permissions
   */
  @javax.annotation.Nullable
  public UserPermissions getPermissions() {
    return permissions;
  }

  public void setPermissions(UserPermissions permissions) {
    this.permissions = permissions;
  }


  public UpdateUserRequestBody role(RoleEnum role) {
    this.role = role;
    return this;
  }

  /**
   * The type of user (**admin** or **user**). Note that admin users cannot have a &#x60;homeResource&#x60; other than &#39;/&#39;, and will have full permissions, but you must provide at least \&quot;download,upload,list,delete\&quot; in the &#x60;permissions&#x60; parameter.
   * @return role
   */
  @javax.annotation.Nullable
  public RoleEnum getRole() {
    return role;
  }

  public void setRole(RoleEnum role) {
    this.role = role;
  }


  public UpdateUserRequestBody timeZone(String timeZone) {
    this.timeZone = timeZone;
    return this;
  }

  /**
   * Time zone, used for accurate time display within the application. See &lt;a href&#x3D;&#39;https://php.net/manual/en/timezones.php&#39; target&#x3D;&#39;blank&#39;&gt;this page&lt;/a&gt; for allowed values. 
   * @return timeZone
   */
  @javax.annotation.Nullable
  public String getTimeZone() {
    return timeZone;
  }

  public void setTimeZone(String timeZone) {
    this.timeZone = timeZone;
  }


  public UpdateUserRequestBody username(String username) {
    this.username = username;
    return this;
  }

  /**
   * New username for the user. This should follow standard username conventions - spaces are not allowed, etc. We do allow email addresses as usernames.  **Note** Usernames must be unique across all ExaVault accounts.
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
    UpdateUserRequestBody updateUserRequestBody = (UpdateUserRequestBody) o;
    return Objects.equals(this.email, updateUserRequestBody.email) &&
        Objects.equals(this.expiration, updateUserRequestBody.expiration) &&
        Objects.equals(this.homeResource, updateUserRequestBody.homeResource) &&
        Objects.equals(this.locked, updateUserRequestBody.locked) &&
        Objects.equals(this.nickname, updateUserRequestBody.nickname) &&
        Objects.equals(this.onboarding, updateUserRequestBody.onboarding) &&
        Objects.equals(this.password, updateUserRequestBody.password) &&
        Objects.equals(this.permissions, updateUserRequestBody.permissions) &&
        Objects.equals(this.role, updateUserRequestBody.role) &&
        Objects.equals(this.timeZone, updateUserRequestBody.timeZone) &&
        Objects.equals(this.username, updateUserRequestBody.username);
  }

  @Override
  public int hashCode() {
    return Objects.hash(email, expiration, homeResource, locked, nickname, onboarding, password, permissions, role, timeZone, username);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateUserRequestBody {\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    expiration: ").append(toIndentedString(expiration)).append("\n");
    sb.append("    homeResource: ").append(toIndentedString(homeResource)).append("\n");
    sb.append("    locked: ").append(toIndentedString(locked)).append("\n");
    sb.append("    nickname: ").append(toIndentedString(nickname)).append("\n");
    sb.append("    onboarding: ").append(toIndentedString(onboarding)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    permissions: ").append(toIndentedString(permissions)).append("\n");
    sb.append("    role: ").append(toIndentedString(role)).append("\n");
    sb.append("    timeZone: ").append(toIndentedString(timeZone)).append("\n");
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
    openapiFields.add("email");
    openapiFields.add("expiration");
    openapiFields.add("homeResource");
    openapiFields.add("locked");
    openapiFields.add("nickname");
    openapiFields.add("onboarding");
    openapiFields.add("password");
    openapiFields.add("permissions");
    openapiFields.add("role");
    openapiFields.add("timeZone");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateUserRequestBody
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateUserRequestBody.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateUserRequestBody is not found in the empty JSON string", UpdateUserRequestBody.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateUserRequestBody.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateUserRequestBody` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("expiration") != null && !jsonObj.get("expiration").isJsonNull()) && !jsonObj.get("expiration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `expiration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("expiration").toString()));
      }
      if ((jsonObj.get("homeResource") != null && !jsonObj.get("homeResource").isJsonNull()) && !jsonObj.get("homeResource").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `homeResource` to be a primitive type in the JSON string but got `%s`", jsonObj.get("homeResource").toString()));
      }
      if ((jsonObj.get("nickname") != null && !jsonObj.get("nickname").isJsonNull()) && !jsonObj.get("nickname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nickname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nickname").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      // validate the optional field `permissions`
      if (jsonObj.get("permissions") != null && !jsonObj.get("permissions").isJsonNull()) {
        UserPermissions.validateJsonElement(jsonObj.get("permissions"));
      }
      if ((jsonObj.get("role") != null && !jsonObj.get("role").isJsonNull()) && !jsonObj.get("role").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `role` to be a primitive type in the JSON string but got `%s`", jsonObj.get("role").toString()));
      }
      // validate the optional field `role`
      if (jsonObj.get("role") != null && !jsonObj.get("role").isJsonNull()) {
        RoleEnum.validateJsonElement(jsonObj.get("role"));
      }
      if ((jsonObj.get("timeZone") != null && !jsonObj.get("timeZone").isJsonNull()) && !jsonObj.get("timeZone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timeZone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timeZone").toString()));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateUserRequestBody.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateUserRequestBody' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateUserRequestBody> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateUserRequestBody.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateUserRequestBody>() {
           @Override
           public void write(JsonWriter out, UpdateUserRequestBody value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateUserRequestBody read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateUserRequestBody given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateUserRequestBody
   * @throws IOException if the JSON string is invalid with respect to UpdateUserRequestBody
   */
  public static UpdateUserRequestBody fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateUserRequestBody.class);
  }

  /**
   * Convert an instance of UpdateUserRequestBody to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

