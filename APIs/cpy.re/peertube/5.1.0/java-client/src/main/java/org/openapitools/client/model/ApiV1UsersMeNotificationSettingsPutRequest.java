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
 * ApiV1UsersMeNotificationSettingsPutRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiV1UsersMeNotificationSettingsPutRequest {
  public static final String SERIALIZED_NAME_ABUSE_AS_MODERATOR = "abuseAsModerator";
  @SerializedName(SERIALIZED_NAME_ABUSE_AS_MODERATOR)
  private Integer abuseAsModerator;

  public static final String SERIALIZED_NAME_AUTO_INSTANCE_FOLLOWING = "autoInstanceFollowing";
  @SerializedName(SERIALIZED_NAME_AUTO_INSTANCE_FOLLOWING)
  private Integer autoInstanceFollowing;

  public static final String SERIALIZED_NAME_BLACKLIST_ON_MY_VIDEO = "blacklistOnMyVideo";
  @SerializedName(SERIALIZED_NAME_BLACKLIST_ON_MY_VIDEO)
  private Integer blacklistOnMyVideo;

  public static final String SERIALIZED_NAME_COMMENT_MENTION = "commentMention";
  @SerializedName(SERIALIZED_NAME_COMMENT_MENTION)
  private Integer commentMention;

  public static final String SERIALIZED_NAME_MY_VIDEO_IMPORT_FINISHED = "myVideoImportFinished";
  @SerializedName(SERIALIZED_NAME_MY_VIDEO_IMPORT_FINISHED)
  private Integer myVideoImportFinished;

  public static final String SERIALIZED_NAME_MY_VIDEO_PUBLISHED = "myVideoPublished";
  @SerializedName(SERIALIZED_NAME_MY_VIDEO_PUBLISHED)
  private Integer myVideoPublished;

  public static final String SERIALIZED_NAME_NEW_COMMENT_ON_MY_VIDEO = "newCommentOnMyVideo";
  @SerializedName(SERIALIZED_NAME_NEW_COMMENT_ON_MY_VIDEO)
  private Integer newCommentOnMyVideo;

  public static final String SERIALIZED_NAME_NEW_FOLLOW = "newFollow";
  @SerializedName(SERIALIZED_NAME_NEW_FOLLOW)
  private Integer newFollow;

  public static final String SERIALIZED_NAME_NEW_INSTANCE_FOLLOWER = "newInstanceFollower";
  @SerializedName(SERIALIZED_NAME_NEW_INSTANCE_FOLLOWER)
  private Integer newInstanceFollower;

  public static final String SERIALIZED_NAME_NEW_USER_REGISTRATION = "newUserRegistration";
  @SerializedName(SERIALIZED_NAME_NEW_USER_REGISTRATION)
  private Integer newUserRegistration;

  public static final String SERIALIZED_NAME_NEW_VIDEO_FROM_SUBSCRIPTION = "newVideoFromSubscription";
  @SerializedName(SERIALIZED_NAME_NEW_VIDEO_FROM_SUBSCRIPTION)
  private Integer newVideoFromSubscription;

  public static final String SERIALIZED_NAME_VIDEO_AUTO_BLACKLIST_AS_MODERATOR = "videoAutoBlacklistAsModerator";
  @SerializedName(SERIALIZED_NAME_VIDEO_AUTO_BLACKLIST_AS_MODERATOR)
  private Integer videoAutoBlacklistAsModerator;

  public ApiV1UsersMeNotificationSettingsPutRequest() {
  }

  public ApiV1UsersMeNotificationSettingsPutRequest abuseAsModerator(Integer abuseAsModerator) {
    this.abuseAsModerator = abuseAsModerator;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return abuseAsModerator
   */
  @javax.annotation.Nullable
  public Integer getAbuseAsModerator() {
    return abuseAsModerator;
  }

  public void setAbuseAsModerator(Integer abuseAsModerator) {
    this.abuseAsModerator = abuseAsModerator;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest autoInstanceFollowing(Integer autoInstanceFollowing) {
    this.autoInstanceFollowing = autoInstanceFollowing;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return autoInstanceFollowing
   */
  @javax.annotation.Nullable
  public Integer getAutoInstanceFollowing() {
    return autoInstanceFollowing;
  }

  public void setAutoInstanceFollowing(Integer autoInstanceFollowing) {
    this.autoInstanceFollowing = autoInstanceFollowing;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest blacklistOnMyVideo(Integer blacklistOnMyVideo) {
    this.blacklistOnMyVideo = blacklistOnMyVideo;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return blacklistOnMyVideo
   */
  @javax.annotation.Nullable
  public Integer getBlacklistOnMyVideo() {
    return blacklistOnMyVideo;
  }

  public void setBlacklistOnMyVideo(Integer blacklistOnMyVideo) {
    this.blacklistOnMyVideo = blacklistOnMyVideo;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest commentMention(Integer commentMention) {
    this.commentMention = commentMention;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return commentMention
   */
  @javax.annotation.Nullable
  public Integer getCommentMention() {
    return commentMention;
  }

  public void setCommentMention(Integer commentMention) {
    this.commentMention = commentMention;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest myVideoImportFinished(Integer myVideoImportFinished) {
    this.myVideoImportFinished = myVideoImportFinished;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return myVideoImportFinished
   */
  @javax.annotation.Nullable
  public Integer getMyVideoImportFinished() {
    return myVideoImportFinished;
  }

  public void setMyVideoImportFinished(Integer myVideoImportFinished) {
    this.myVideoImportFinished = myVideoImportFinished;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest myVideoPublished(Integer myVideoPublished) {
    this.myVideoPublished = myVideoPublished;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return myVideoPublished
   */
  @javax.annotation.Nullable
  public Integer getMyVideoPublished() {
    return myVideoPublished;
  }

  public void setMyVideoPublished(Integer myVideoPublished) {
    this.myVideoPublished = myVideoPublished;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest newCommentOnMyVideo(Integer newCommentOnMyVideo) {
    this.newCommentOnMyVideo = newCommentOnMyVideo;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return newCommentOnMyVideo
   */
  @javax.annotation.Nullable
  public Integer getNewCommentOnMyVideo() {
    return newCommentOnMyVideo;
  }

  public void setNewCommentOnMyVideo(Integer newCommentOnMyVideo) {
    this.newCommentOnMyVideo = newCommentOnMyVideo;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest newFollow(Integer newFollow) {
    this.newFollow = newFollow;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return newFollow
   */
  @javax.annotation.Nullable
  public Integer getNewFollow() {
    return newFollow;
  }

  public void setNewFollow(Integer newFollow) {
    this.newFollow = newFollow;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest newInstanceFollower(Integer newInstanceFollower) {
    this.newInstanceFollower = newInstanceFollower;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return newInstanceFollower
   */
  @javax.annotation.Nullable
  public Integer getNewInstanceFollower() {
    return newInstanceFollower;
  }

  public void setNewInstanceFollower(Integer newInstanceFollower) {
    this.newInstanceFollower = newInstanceFollower;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest newUserRegistration(Integer newUserRegistration) {
    this.newUserRegistration = newUserRegistration;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return newUserRegistration
   */
  @javax.annotation.Nullable
  public Integer getNewUserRegistration() {
    return newUserRegistration;
  }

  public void setNewUserRegistration(Integer newUserRegistration) {
    this.newUserRegistration = newUserRegistration;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest newVideoFromSubscription(Integer newVideoFromSubscription) {
    this.newVideoFromSubscription = newVideoFromSubscription;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return newVideoFromSubscription
   */
  @javax.annotation.Nullable
  public Integer getNewVideoFromSubscription() {
    return newVideoFromSubscription;
  }

  public void setNewVideoFromSubscription(Integer newVideoFromSubscription) {
    this.newVideoFromSubscription = newVideoFromSubscription;
  }


  public ApiV1UsersMeNotificationSettingsPutRequest videoAutoBlacklistAsModerator(Integer videoAutoBlacklistAsModerator) {
    this.videoAutoBlacklistAsModerator = videoAutoBlacklistAsModerator;
    return this;
  }

  /**
   * Notification type. One of the following values, or a sum of multiple values: - &#x60;0&#x60; NONE - &#x60;1&#x60; WEB - &#x60;2&#x60; EMAIL 
   * @return videoAutoBlacklistAsModerator
   */
  @javax.annotation.Nullable
  public Integer getVideoAutoBlacklistAsModerator() {
    return videoAutoBlacklistAsModerator;
  }

  public void setVideoAutoBlacklistAsModerator(Integer videoAutoBlacklistAsModerator) {
    this.videoAutoBlacklistAsModerator = videoAutoBlacklistAsModerator;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiV1UsersMeNotificationSettingsPutRequest apiV1UsersMeNotificationSettingsPutRequest = (ApiV1UsersMeNotificationSettingsPutRequest) o;
    return Objects.equals(this.abuseAsModerator, apiV1UsersMeNotificationSettingsPutRequest.abuseAsModerator) &&
        Objects.equals(this.autoInstanceFollowing, apiV1UsersMeNotificationSettingsPutRequest.autoInstanceFollowing) &&
        Objects.equals(this.blacklistOnMyVideo, apiV1UsersMeNotificationSettingsPutRequest.blacklistOnMyVideo) &&
        Objects.equals(this.commentMention, apiV1UsersMeNotificationSettingsPutRequest.commentMention) &&
        Objects.equals(this.myVideoImportFinished, apiV1UsersMeNotificationSettingsPutRequest.myVideoImportFinished) &&
        Objects.equals(this.myVideoPublished, apiV1UsersMeNotificationSettingsPutRequest.myVideoPublished) &&
        Objects.equals(this.newCommentOnMyVideo, apiV1UsersMeNotificationSettingsPutRequest.newCommentOnMyVideo) &&
        Objects.equals(this.newFollow, apiV1UsersMeNotificationSettingsPutRequest.newFollow) &&
        Objects.equals(this.newInstanceFollower, apiV1UsersMeNotificationSettingsPutRequest.newInstanceFollower) &&
        Objects.equals(this.newUserRegistration, apiV1UsersMeNotificationSettingsPutRequest.newUserRegistration) &&
        Objects.equals(this.newVideoFromSubscription, apiV1UsersMeNotificationSettingsPutRequest.newVideoFromSubscription) &&
        Objects.equals(this.videoAutoBlacklistAsModerator, apiV1UsersMeNotificationSettingsPutRequest.videoAutoBlacklistAsModerator);
  }

  @Override
  public int hashCode() {
    return Objects.hash(abuseAsModerator, autoInstanceFollowing, blacklistOnMyVideo, commentMention, myVideoImportFinished, myVideoPublished, newCommentOnMyVideo, newFollow, newInstanceFollower, newUserRegistration, newVideoFromSubscription, videoAutoBlacklistAsModerator);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiV1UsersMeNotificationSettingsPutRequest {\n");
    sb.append("    abuseAsModerator: ").append(toIndentedString(abuseAsModerator)).append("\n");
    sb.append("    autoInstanceFollowing: ").append(toIndentedString(autoInstanceFollowing)).append("\n");
    sb.append("    blacklistOnMyVideo: ").append(toIndentedString(blacklistOnMyVideo)).append("\n");
    sb.append("    commentMention: ").append(toIndentedString(commentMention)).append("\n");
    sb.append("    myVideoImportFinished: ").append(toIndentedString(myVideoImportFinished)).append("\n");
    sb.append("    myVideoPublished: ").append(toIndentedString(myVideoPublished)).append("\n");
    sb.append("    newCommentOnMyVideo: ").append(toIndentedString(newCommentOnMyVideo)).append("\n");
    sb.append("    newFollow: ").append(toIndentedString(newFollow)).append("\n");
    sb.append("    newInstanceFollower: ").append(toIndentedString(newInstanceFollower)).append("\n");
    sb.append("    newUserRegistration: ").append(toIndentedString(newUserRegistration)).append("\n");
    sb.append("    newVideoFromSubscription: ").append(toIndentedString(newVideoFromSubscription)).append("\n");
    sb.append("    videoAutoBlacklistAsModerator: ").append(toIndentedString(videoAutoBlacklistAsModerator)).append("\n");
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
    openapiFields.add("abuseAsModerator");
    openapiFields.add("autoInstanceFollowing");
    openapiFields.add("blacklistOnMyVideo");
    openapiFields.add("commentMention");
    openapiFields.add("myVideoImportFinished");
    openapiFields.add("myVideoPublished");
    openapiFields.add("newCommentOnMyVideo");
    openapiFields.add("newFollow");
    openapiFields.add("newInstanceFollower");
    openapiFields.add("newUserRegistration");
    openapiFields.add("newVideoFromSubscription");
    openapiFields.add("videoAutoBlacklistAsModerator");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiV1UsersMeNotificationSettingsPutRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiV1UsersMeNotificationSettingsPutRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiV1UsersMeNotificationSettingsPutRequest is not found in the empty JSON string", ApiV1UsersMeNotificationSettingsPutRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiV1UsersMeNotificationSettingsPutRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiV1UsersMeNotificationSettingsPutRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiV1UsersMeNotificationSettingsPutRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiV1UsersMeNotificationSettingsPutRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiV1UsersMeNotificationSettingsPutRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiV1UsersMeNotificationSettingsPutRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiV1UsersMeNotificationSettingsPutRequest>() {
           @Override
           public void write(JsonWriter out, ApiV1UsersMeNotificationSettingsPutRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiV1UsersMeNotificationSettingsPutRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiV1UsersMeNotificationSettingsPutRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiV1UsersMeNotificationSettingsPutRequest
   * @throws IOException if the JSON string is invalid with respect to ApiV1UsersMeNotificationSettingsPutRequest
   */
  public static ApiV1UsersMeNotificationSettingsPutRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiV1UsersMeNotificationSettingsPutRequest.class);
  }

  /**
   * Convert an instance of ApiV1UsersMeNotificationSettingsPutRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

