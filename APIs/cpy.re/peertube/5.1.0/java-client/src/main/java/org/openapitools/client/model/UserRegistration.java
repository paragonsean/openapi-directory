/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.UserRegistrationState;
import org.openapitools.client.model.UserRegistrationUser;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * UserRegistration
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UserRegistration {
  public static final String SERIALIZED_NAME_ACCOUNT_DISPLAY_NAME = "accountDisplayName";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_DISPLAY_NAME)
  private String accountDisplayName;

  public static final String SERIALIZED_NAME_CHANNEL_DISPLAY_NAME = "channelDisplayName";
  @SerializedName(SERIALIZED_NAME_CHANNEL_DISPLAY_NAME)
  private String channelDisplayName;

  public static final String SERIALIZED_NAME_CHANNEL_HANDLE = "channelHandle";
  @SerializedName(SERIALIZED_NAME_CHANNEL_HANDLE)
  private String channelHandle;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_EMAIL_VERIFIED = "emailVerified";
  @SerializedName(SERIALIZED_NAME_EMAIL_VERIFIED)
  private Boolean emailVerified;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_MODERATION_RESPONSE = "moderationResponse";
  @SerializedName(SERIALIZED_NAME_MODERATION_RESPONSE)
  private String moderationResponse;

  public static final String SERIALIZED_NAME_REGISTRATION_REASON = "registrationReason";
  @SerializedName(SERIALIZED_NAME_REGISTRATION_REASON)
  private String registrationReason;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private UserRegistrationState state;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_USER = "user";
  @SerializedName(SERIALIZED_NAME_USER)
  private UserRegistrationUser user;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public UserRegistration() {
  }

  public UserRegistration accountDisplayName(String accountDisplayName) {
    this.accountDisplayName = accountDisplayName;
    return this;
  }

  /**
   * Get accountDisplayName
   * @return accountDisplayName
   */
  @javax.annotation.Nullable
  public String getAccountDisplayName() {
    return accountDisplayName;
  }

  public void setAccountDisplayName(String accountDisplayName) {
    this.accountDisplayName = accountDisplayName;
  }


  public UserRegistration channelDisplayName(String channelDisplayName) {
    this.channelDisplayName = channelDisplayName;
    return this;
  }

  /**
   * Get channelDisplayName
   * @return channelDisplayName
   */
  @javax.annotation.Nullable
  public String getChannelDisplayName() {
    return channelDisplayName;
  }

  public void setChannelDisplayName(String channelDisplayName) {
    this.channelDisplayName = channelDisplayName;
  }


  public UserRegistration channelHandle(String channelHandle) {
    this.channelHandle = channelHandle;
    return this;
  }

  /**
   * Get channelHandle
   * @return channelHandle
   */
  @javax.annotation.Nullable
  public String getChannelHandle() {
    return channelHandle;
  }

  public void setChannelHandle(String channelHandle) {
    this.channelHandle = channelHandle;
  }


  public UserRegistration createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public UserRegistration email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public UserRegistration emailVerified(Boolean emailVerified) {
    this.emailVerified = emailVerified;
    return this;
  }

  /**
   * Get emailVerified
   * @return emailVerified
   */
  @javax.annotation.Nullable
  public Boolean getEmailVerified() {
    return emailVerified;
  }

  public void setEmailVerified(Boolean emailVerified) {
    this.emailVerified = emailVerified;
  }


  public UserRegistration id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * minimum: 1
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public UserRegistration moderationResponse(String moderationResponse) {
    this.moderationResponse = moderationResponse;
    return this;
  }

  /**
   * Get moderationResponse
   * @return moderationResponse
   */
  @javax.annotation.Nullable
  public String getModerationResponse() {
    return moderationResponse;
  }

  public void setModerationResponse(String moderationResponse) {
    this.moderationResponse = moderationResponse;
  }


  public UserRegistration registrationReason(String registrationReason) {
    this.registrationReason = registrationReason;
    return this;
  }

  /**
   * Get registrationReason
   * @return registrationReason
   */
  @javax.annotation.Nullable
  public String getRegistrationReason() {
    return registrationReason;
  }

  public void setRegistrationReason(String registrationReason) {
    this.registrationReason = registrationReason;
  }


  public UserRegistration state(UserRegistrationState state) {
    this.state = state;
    return this;
  }

  /**
   * Get state
   * @return state
   */
  @javax.annotation.Nullable
  public UserRegistrationState getState() {
    return state;
  }

  public void setState(UserRegistrationState state) {
    this.state = state;
  }


  public UserRegistration updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public UserRegistration user(UserRegistrationUser user) {
    this.user = user;
    return this;
  }

  /**
   * Get user
   * @return user
   */
  @javax.annotation.Nullable
  public UserRegistrationUser getUser() {
    return user;
  }

  public void setUser(UserRegistrationUser user) {
    this.user = user;
  }


  public UserRegistration username(String username) {
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
    UserRegistration userRegistration = (UserRegistration) o;
    return Objects.equals(this.accountDisplayName, userRegistration.accountDisplayName) &&
        Objects.equals(this.channelDisplayName, userRegistration.channelDisplayName) &&
        Objects.equals(this.channelHandle, userRegistration.channelHandle) &&
        Objects.equals(this.createdAt, userRegistration.createdAt) &&
        Objects.equals(this.email, userRegistration.email) &&
        Objects.equals(this.emailVerified, userRegistration.emailVerified) &&
        Objects.equals(this.id, userRegistration.id) &&
        Objects.equals(this.moderationResponse, userRegistration.moderationResponse) &&
        Objects.equals(this.registrationReason, userRegistration.registrationReason) &&
        Objects.equals(this.state, userRegistration.state) &&
        Objects.equals(this.updatedAt, userRegistration.updatedAt) &&
        Objects.equals(this.user, userRegistration.user) &&
        Objects.equals(this.username, userRegistration.username);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountDisplayName, channelDisplayName, channelHandle, createdAt, email, emailVerified, id, moderationResponse, registrationReason, state, updatedAt, user, username);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserRegistration {\n");
    sb.append("    accountDisplayName: ").append(toIndentedString(accountDisplayName)).append("\n");
    sb.append("    channelDisplayName: ").append(toIndentedString(channelDisplayName)).append("\n");
    sb.append("    channelHandle: ").append(toIndentedString(channelHandle)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    emailVerified: ").append(toIndentedString(emailVerified)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    moderationResponse: ").append(toIndentedString(moderationResponse)).append("\n");
    sb.append("    registrationReason: ").append(toIndentedString(registrationReason)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    user: ").append(toIndentedString(user)).append("\n");
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
    openapiFields.add("accountDisplayName");
    openapiFields.add("channelDisplayName");
    openapiFields.add("channelHandle");
    openapiFields.add("createdAt");
    openapiFields.add("email");
    openapiFields.add("emailVerified");
    openapiFields.add("id");
    openapiFields.add("moderationResponse");
    openapiFields.add("registrationReason");
    openapiFields.add("state");
    openapiFields.add("updatedAt");
    openapiFields.add("user");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UserRegistration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserRegistration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserRegistration is not found in the empty JSON string", UserRegistration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserRegistration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserRegistration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("accountDisplayName") != null && !jsonObj.get("accountDisplayName").isJsonNull()) && !jsonObj.get("accountDisplayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountDisplayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountDisplayName").toString()));
      }
      if ((jsonObj.get("channelDisplayName") != null && !jsonObj.get("channelDisplayName").isJsonNull()) && !jsonObj.get("channelDisplayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `channelDisplayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("channelDisplayName").toString()));
      }
      if ((jsonObj.get("channelHandle") != null && !jsonObj.get("channelHandle").isJsonNull()) && !jsonObj.get("channelHandle").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `channelHandle` to be a primitive type in the JSON string but got `%s`", jsonObj.get("channelHandle").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("moderationResponse") != null && !jsonObj.get("moderationResponse").isJsonNull()) && !jsonObj.get("moderationResponse").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `moderationResponse` to be a primitive type in the JSON string but got `%s`", jsonObj.get("moderationResponse").toString()));
      }
      if ((jsonObj.get("registrationReason") != null && !jsonObj.get("registrationReason").isJsonNull()) && !jsonObj.get("registrationReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `registrationReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("registrationReason").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        UserRegistrationState.validateJsonElement(jsonObj.get("state"));
      }
      // validate the optional field `user`
      if (jsonObj.get("user") != null && !jsonObj.get("user").isJsonNull()) {
        UserRegistrationUser.validateJsonElement(jsonObj.get("user"));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserRegistration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserRegistration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserRegistration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserRegistration.class));

       return (TypeAdapter<T>) new TypeAdapter<UserRegistration>() {
           @Override
           public void write(JsonWriter out, UserRegistration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserRegistration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UserRegistration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UserRegistration
   * @throws IOException if the JSON string is invalid with respect to UserRegistration
   */
  public static UserRegistration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserRegistration.class);
  }

  /**
   * Convert an instance of UserRegistration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

