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
import java.util.UUID;
import org.openapitools.client.model.AccountSummary;
import org.openapitools.client.model.VideoChannelSummary;
import org.openapitools.client.model.VideoConstantNumberCategory;
import org.openapitools.client.model.VideoConstantNumberLicence;
import org.openapitools.client.model.VideoConstantStringLanguage;
import org.openapitools.client.model.VideoPrivacyConstant;
import org.openapitools.client.model.VideoScheduledUpdate;
import org.openapitools.client.model.VideoStateConstant;
import org.openapitools.client.model.VideoUserHistory;
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
 * Video
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Video {
  public static final String SERIALIZED_NAME_ACCOUNT = "account";
  @SerializedName(SERIALIZED_NAME_ACCOUNT)
  private AccountSummary account;

  public static final String SERIALIZED_NAME_BLACKLISTED = "blacklisted";
  @SerializedName(SERIALIZED_NAME_BLACKLISTED)
  private Boolean blacklisted;

  public static final String SERIALIZED_NAME_BLACKLISTED_REASON = "blacklistedReason";
  @SerializedName(SERIALIZED_NAME_BLACKLISTED_REASON)
  private String blacklistedReason;

  public static final String SERIALIZED_NAME_CATEGORY = "category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private VideoConstantNumberCategory category;

  public static final String SERIALIZED_NAME_CHANNEL = "channel";
  @SerializedName(SERIALIZED_NAME_CHANNEL)
  private VideoChannelSummary channel;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISLIKES = "dislikes";
  @SerializedName(SERIALIZED_NAME_DISLIKES)
  private Integer dislikes;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private Integer duration;

  public static final String SERIALIZED_NAME_EMBED_PATH = "embedPath";
  @SerializedName(SERIALIZED_NAME_EMBED_PATH)
  private String embedPath;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_LIVE = "isLive";
  @SerializedName(SERIALIZED_NAME_IS_LIVE)
  private Boolean isLive;

  public static final String SERIALIZED_NAME_IS_LOCAL = "isLocal";
  @SerializedName(SERIALIZED_NAME_IS_LOCAL)
  private Boolean isLocal;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private VideoConstantStringLanguage language;

  public static final String SERIALIZED_NAME_LICENCE = "licence";
  @SerializedName(SERIALIZED_NAME_LICENCE)
  private VideoConstantNumberLicence licence;

  public static final String SERIALIZED_NAME_LIKES = "likes";
  @SerializedName(SERIALIZED_NAME_LIKES)
  private Integer likes;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NSFW = "nsfw";
  @SerializedName(SERIALIZED_NAME_NSFW)
  private Boolean nsfw;

  public static final String SERIALIZED_NAME_ORIGINALLY_PUBLISHED_AT = "originallyPublishedAt";
  @SerializedName(SERIALIZED_NAME_ORIGINALLY_PUBLISHED_AT)
  private OffsetDateTime originallyPublishedAt;

  public static final String SERIALIZED_NAME_PREVIEW_PATH = "previewPath";
  @SerializedName(SERIALIZED_NAME_PREVIEW_PATH)
  private String previewPath;

  public static final String SERIALIZED_NAME_PRIVACY = "privacy";
  @SerializedName(SERIALIZED_NAME_PRIVACY)
  private VideoPrivacyConstant privacy;

  public static final String SERIALIZED_NAME_PUBLISHED_AT = "publishedAt";
  @SerializedName(SERIALIZED_NAME_PUBLISHED_AT)
  private OffsetDateTime publishedAt;

  public static final String SERIALIZED_NAME_SCHEDULED_UPDATE = "scheduledUpdate";
  @SerializedName(SERIALIZED_NAME_SCHEDULED_UPDATE)
  private VideoScheduledUpdate scheduledUpdate;

  public static final String SERIALIZED_NAME_SHORT_U_U_I_D = "shortUUID";
  @SerializedName(SERIALIZED_NAME_SHORT_U_U_I_D)
  private String shortUUID;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private VideoStateConstant state;

  public static final String SERIALIZED_NAME_THUMBNAIL_PATH = "thumbnailPath";
  @SerializedName(SERIALIZED_NAME_THUMBNAIL_PATH)
  private String thumbnailPath;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_USER_HISTORY = "userHistory";
  @SerializedName(SERIALIZED_NAME_USER_HISTORY)
  private VideoUserHistory userHistory;

  public static final String SERIALIZED_NAME_UUID = "uuid";
  @SerializedName(SERIALIZED_NAME_UUID)
  private UUID uuid;

  public static final String SERIALIZED_NAME_VIEWS = "views";
  @SerializedName(SERIALIZED_NAME_VIEWS)
  private Integer views;

  public static final String SERIALIZED_NAME_WAIT_TRANSCODING = "waitTranscoding";
  @SerializedName(SERIALIZED_NAME_WAIT_TRANSCODING)
  private Boolean waitTranscoding;

  public Video() {
  }

  public Video account(AccountSummary account) {
    this.account = account;
    return this;
  }

  /**
   * Get account
   * @return account
   */
  @javax.annotation.Nullable
  public AccountSummary getAccount() {
    return account;
  }

  public void setAccount(AccountSummary account) {
    this.account = account;
  }


  public Video blacklisted(Boolean blacklisted) {
    this.blacklisted = blacklisted;
    return this;
  }

  /**
   * Get blacklisted
   * @return blacklisted
   */
  @javax.annotation.Nullable
  public Boolean getBlacklisted() {
    return blacklisted;
  }

  public void setBlacklisted(Boolean blacklisted) {
    this.blacklisted = blacklisted;
  }


  public Video blacklistedReason(String blacklistedReason) {
    this.blacklistedReason = blacklistedReason;
    return this;
  }

  /**
   * Get blacklistedReason
   * @return blacklistedReason
   */
  @javax.annotation.Nullable
  public String getBlacklistedReason() {
    return blacklistedReason;
  }

  public void setBlacklistedReason(String blacklistedReason) {
    this.blacklistedReason = blacklistedReason;
  }


  public Video category(VideoConstantNumberCategory category) {
    this.category = category;
    return this;
  }

  /**
   * category in which the video is classified
   * @return category
   */
  @javax.annotation.Nullable
  public VideoConstantNumberCategory getCategory() {
    return category;
  }

  public void setCategory(VideoConstantNumberCategory category) {
    this.category = category;
  }


  public Video channel(VideoChannelSummary channel) {
    this.channel = channel;
    return this;
  }

  /**
   * Get channel
   * @return channel
   */
  @javax.annotation.Nullable
  public VideoChannelSummary getChannel() {
    return channel;
  }

  public void setChannel(VideoChannelSummary channel) {
    this.channel = channel;
  }


  public Video createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * time at which the video object was first drafted
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public Video description(String description) {
    this.description = description;
    return this;
  }

  /**
   * truncated description of the video, written in Markdown. Resolve &#x60;descriptionPath&#x60; to get the full description of maximum &#x60;10000&#x60; characters. 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Video dislikes(Integer dislikes) {
    this.dislikes = dislikes;
    return this;
  }

  /**
   * Get dislikes
   * @return dislikes
   */
  @javax.annotation.Nullable
  public Integer getDislikes() {
    return dislikes;
  }

  public void setDislikes(Integer dislikes) {
    this.dislikes = dislikes;
  }


  public Video duration(Integer duration) {
    this.duration = duration;
    return this;
  }

  /**
   * duration of the video in seconds
   * @return duration
   */
  @javax.annotation.Nullable
  public Integer getDuration() {
    return duration;
  }

  public void setDuration(Integer duration) {
    this.duration = duration;
  }


  public Video embedPath(String embedPath) {
    this.embedPath = embedPath;
    return this;
  }

  /**
   * Get embedPath
   * @return embedPath
   */
  @javax.annotation.Nullable
  public String getEmbedPath() {
    return embedPath;
  }

  public void setEmbedPath(String embedPath) {
    this.embedPath = embedPath;
  }


  public Video id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * object id for the video
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


  public Video isLive(Boolean isLive) {
    this.isLive = isLive;
    return this;
  }

  /**
   * Get isLive
   * @return isLive
   */
  @javax.annotation.Nullable
  public Boolean getIsLive() {
    return isLive;
  }

  public void setIsLive(Boolean isLive) {
    this.isLive = isLive;
  }


  public Video isLocal(Boolean isLocal) {
    this.isLocal = isLocal;
    return this;
  }

  /**
   * Get isLocal
   * @return isLocal
   */
  @javax.annotation.Nullable
  public Boolean getIsLocal() {
    return isLocal;
  }

  public void setIsLocal(Boolean isLocal) {
    this.isLocal = isLocal;
  }


  public Video language(VideoConstantStringLanguage language) {
    this.language = language;
    return this;
  }

  /**
   * main language used in the video
   * @return language
   */
  @javax.annotation.Nullable
  public VideoConstantStringLanguage getLanguage() {
    return language;
  }

  public void setLanguage(VideoConstantStringLanguage language) {
    this.language = language;
  }


  public Video licence(VideoConstantNumberLicence licence) {
    this.licence = licence;
    return this;
  }

  /**
   * licence under which the video is distributed
   * @return licence
   */
  @javax.annotation.Nullable
  public VideoConstantNumberLicence getLicence() {
    return licence;
  }

  public void setLicence(VideoConstantNumberLicence licence) {
    this.licence = licence;
  }


  public Video likes(Integer likes) {
    this.likes = likes;
    return this;
  }

  /**
   * Get likes
   * @return likes
   */
  @javax.annotation.Nullable
  public Integer getLikes() {
    return likes;
  }

  public void setLikes(Integer likes) {
    this.likes = likes;
  }


  public Video name(String name) {
    this.name = name;
    return this;
  }

  /**
   * title of the video
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Video nsfw(Boolean nsfw) {
    this.nsfw = nsfw;
    return this;
  }

  /**
   * Get nsfw
   * @return nsfw
   */
  @javax.annotation.Nullable
  public Boolean getNsfw() {
    return nsfw;
  }

  public void setNsfw(Boolean nsfw) {
    this.nsfw = nsfw;
  }


  public Video originallyPublishedAt(OffsetDateTime originallyPublishedAt) {
    this.originallyPublishedAt = originallyPublishedAt;
    return this;
  }

  /**
   * used to represent a date of first publication, prior to the practical publication date of &#x60;publishedAt&#x60;
   * @return originallyPublishedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getOriginallyPublishedAt() {
    return originallyPublishedAt;
  }

  public void setOriginallyPublishedAt(OffsetDateTime originallyPublishedAt) {
    this.originallyPublishedAt = originallyPublishedAt;
  }


  public Video previewPath(String previewPath) {
    this.previewPath = previewPath;
    return this;
  }

  /**
   * Get previewPath
   * @return previewPath
   */
  @javax.annotation.Nullable
  public String getPreviewPath() {
    return previewPath;
  }

  public void setPreviewPath(String previewPath) {
    this.previewPath = previewPath;
  }


  public Video privacy(VideoPrivacyConstant privacy) {
    this.privacy = privacy;
    return this;
  }

  /**
   * privacy policy used to distribute the video
   * @return privacy
   */
  @javax.annotation.Nullable
  public VideoPrivacyConstant getPrivacy() {
    return privacy;
  }

  public void setPrivacy(VideoPrivacyConstant privacy) {
    this.privacy = privacy;
  }


  public Video publishedAt(OffsetDateTime publishedAt) {
    this.publishedAt = publishedAt;
    return this;
  }

  /**
   * time at which the video was marked as ready for playback (with restrictions depending on &#x60;privacy&#x60;). Usually set after a &#x60;state&#x60; evolution.
   * @return publishedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPublishedAt() {
    return publishedAt;
  }

  public void setPublishedAt(OffsetDateTime publishedAt) {
    this.publishedAt = publishedAt;
  }


  public Video scheduledUpdate(VideoScheduledUpdate scheduledUpdate) {
    this.scheduledUpdate = scheduledUpdate;
    return this;
  }

  /**
   * Get scheduledUpdate
   * @return scheduledUpdate
   */
  @javax.annotation.Nullable
  public VideoScheduledUpdate getScheduledUpdate() {
    return scheduledUpdate;
  }

  public void setScheduledUpdate(VideoScheduledUpdate scheduledUpdate) {
    this.scheduledUpdate = scheduledUpdate;
  }


  public Video shortUUID(String shortUUID) {
    this.shortUUID = shortUUID;
    return this;
  }

  /**
   * translation of a uuid v4 with a bigger alphabet to have a shorter uuid
   * @return shortUUID
   */
  @javax.annotation.Nullable
  public String getShortUUID() {
    return shortUUID;
  }

  public void setShortUUID(String shortUUID) {
    this.shortUUID = shortUUID;
  }


  public Video state(VideoStateConstant state) {
    this.state = state;
    return this;
  }

  /**
   * represents the internal state of the video processing within the PeerTube instance
   * @return state
   */
  @javax.annotation.Nullable
  public VideoStateConstant getState() {
    return state;
  }

  public void setState(VideoStateConstant state) {
    this.state = state;
  }


  public Video thumbnailPath(String thumbnailPath) {
    this.thumbnailPath = thumbnailPath;
    return this;
  }

  /**
   * Get thumbnailPath
   * @return thumbnailPath
   */
  @javax.annotation.Nullable
  public String getThumbnailPath() {
    return thumbnailPath;
  }

  public void setThumbnailPath(String thumbnailPath) {
    this.thumbnailPath = thumbnailPath;
  }


  public Video updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * last time the video&#39;s metadata was modified
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public Video userHistory(VideoUserHistory userHistory) {
    this.userHistory = userHistory;
    return this;
  }

  /**
   * Get userHistory
   * @return userHistory
   */
  @javax.annotation.Nullable
  public VideoUserHistory getUserHistory() {
    return userHistory;
  }

  public void setUserHistory(VideoUserHistory userHistory) {
    this.userHistory = userHistory;
  }


  public Video uuid(UUID uuid) {
    this.uuid = uuid;
    return this;
  }

  /**
   * universal identifier for the video, that can be used across instances
   * @return uuid
   */
  @javax.annotation.Nullable
  public UUID getUuid() {
    return uuid;
  }

  public void setUuid(UUID uuid) {
    this.uuid = uuid;
  }


  public Video views(Integer views) {
    this.views = views;
    return this;
  }

  /**
   * Get views
   * @return views
   */
  @javax.annotation.Nullable
  public Integer getViews() {
    return views;
  }

  public void setViews(Integer views) {
    this.views = views;
  }


  public Video waitTranscoding(Boolean waitTranscoding) {
    this.waitTranscoding = waitTranscoding;
    return this;
  }

  /**
   * Get waitTranscoding
   * @return waitTranscoding
   */
  @javax.annotation.Nullable
  public Boolean getWaitTranscoding() {
    return waitTranscoding;
  }

  public void setWaitTranscoding(Boolean waitTranscoding) {
    this.waitTranscoding = waitTranscoding;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Video video = (Video) o;
    return Objects.equals(this.account, video.account) &&
        Objects.equals(this.blacklisted, video.blacklisted) &&
        Objects.equals(this.blacklistedReason, video.blacklistedReason) &&
        Objects.equals(this.category, video.category) &&
        Objects.equals(this.channel, video.channel) &&
        Objects.equals(this.createdAt, video.createdAt) &&
        Objects.equals(this.description, video.description) &&
        Objects.equals(this.dislikes, video.dislikes) &&
        Objects.equals(this.duration, video.duration) &&
        Objects.equals(this.embedPath, video.embedPath) &&
        Objects.equals(this.id, video.id) &&
        Objects.equals(this.isLive, video.isLive) &&
        Objects.equals(this.isLocal, video.isLocal) &&
        Objects.equals(this.language, video.language) &&
        Objects.equals(this.licence, video.licence) &&
        Objects.equals(this.likes, video.likes) &&
        Objects.equals(this.name, video.name) &&
        Objects.equals(this.nsfw, video.nsfw) &&
        Objects.equals(this.originallyPublishedAt, video.originallyPublishedAt) &&
        Objects.equals(this.previewPath, video.previewPath) &&
        Objects.equals(this.privacy, video.privacy) &&
        Objects.equals(this.publishedAt, video.publishedAt) &&
        Objects.equals(this.scheduledUpdate, video.scheduledUpdate) &&
        Objects.equals(this.shortUUID, video.shortUUID) &&
        Objects.equals(this.state, video.state) &&
        Objects.equals(this.thumbnailPath, video.thumbnailPath) &&
        Objects.equals(this.updatedAt, video.updatedAt) &&
        Objects.equals(this.userHistory, video.userHistory) &&
        Objects.equals(this.uuid, video.uuid) &&
        Objects.equals(this.views, video.views) &&
        Objects.equals(this.waitTranscoding, video.waitTranscoding);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(account, blacklisted, blacklistedReason, category, channel, createdAt, description, dislikes, duration, embedPath, id, isLive, isLocal, language, licence, likes, name, nsfw, originallyPublishedAt, previewPath, privacy, publishedAt, scheduledUpdate, shortUUID, state, thumbnailPath, updatedAt, userHistory, uuid, views, waitTranscoding);
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
    sb.append("class Video {\n");
    sb.append("    account: ").append(toIndentedString(account)).append("\n");
    sb.append("    blacklisted: ").append(toIndentedString(blacklisted)).append("\n");
    sb.append("    blacklistedReason: ").append(toIndentedString(blacklistedReason)).append("\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    channel: ").append(toIndentedString(channel)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    dislikes: ").append(toIndentedString(dislikes)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    embedPath: ").append(toIndentedString(embedPath)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isLive: ").append(toIndentedString(isLive)).append("\n");
    sb.append("    isLocal: ").append(toIndentedString(isLocal)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    licence: ").append(toIndentedString(licence)).append("\n");
    sb.append("    likes: ").append(toIndentedString(likes)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nsfw: ").append(toIndentedString(nsfw)).append("\n");
    sb.append("    originallyPublishedAt: ").append(toIndentedString(originallyPublishedAt)).append("\n");
    sb.append("    previewPath: ").append(toIndentedString(previewPath)).append("\n");
    sb.append("    privacy: ").append(toIndentedString(privacy)).append("\n");
    sb.append("    publishedAt: ").append(toIndentedString(publishedAt)).append("\n");
    sb.append("    scheduledUpdate: ").append(toIndentedString(scheduledUpdate)).append("\n");
    sb.append("    shortUUID: ").append(toIndentedString(shortUUID)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    thumbnailPath: ").append(toIndentedString(thumbnailPath)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    userHistory: ").append(toIndentedString(userHistory)).append("\n");
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
    sb.append("    views: ").append(toIndentedString(views)).append("\n");
    sb.append("    waitTranscoding: ").append(toIndentedString(waitTranscoding)).append("\n");
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
    openapiFields.add("account");
    openapiFields.add("blacklisted");
    openapiFields.add("blacklistedReason");
    openapiFields.add("category");
    openapiFields.add("channel");
    openapiFields.add("createdAt");
    openapiFields.add("description");
    openapiFields.add("dislikes");
    openapiFields.add("duration");
    openapiFields.add("embedPath");
    openapiFields.add("id");
    openapiFields.add("isLive");
    openapiFields.add("isLocal");
    openapiFields.add("language");
    openapiFields.add("licence");
    openapiFields.add("likes");
    openapiFields.add("name");
    openapiFields.add("nsfw");
    openapiFields.add("originallyPublishedAt");
    openapiFields.add("previewPath");
    openapiFields.add("privacy");
    openapiFields.add("publishedAt");
    openapiFields.add("scheduledUpdate");
    openapiFields.add("shortUUID");
    openapiFields.add("state");
    openapiFields.add("thumbnailPath");
    openapiFields.add("updatedAt");
    openapiFields.add("userHistory");
    openapiFields.add("uuid");
    openapiFields.add("views");
    openapiFields.add("waitTranscoding");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Video
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Video.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Video is not found in the empty JSON string", Video.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Video.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Video` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `account`
      if (jsonObj.get("account") != null && !jsonObj.get("account").isJsonNull()) {
        AccountSummary.validateJsonElement(jsonObj.get("account"));
      }
      if ((jsonObj.get("blacklistedReason") != null && !jsonObj.get("blacklistedReason").isJsonNull()) && !jsonObj.get("blacklistedReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `blacklistedReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("blacklistedReason").toString()));
      }
      // validate the optional field `category`
      if (jsonObj.get("category") != null && !jsonObj.get("category").isJsonNull()) {
        VideoConstantNumberCategory.validateJsonElement(jsonObj.get("category"));
      }
      // validate the optional field `channel`
      if (jsonObj.get("channel") != null && !jsonObj.get("channel").isJsonNull()) {
        VideoChannelSummary.validateJsonElement(jsonObj.get("channel"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("embedPath") != null && !jsonObj.get("embedPath").isJsonNull()) && !jsonObj.get("embedPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `embedPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("embedPath").toString()));
      }
      // validate the optional field `language`
      if (jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) {
        VideoConstantStringLanguage.validateJsonElement(jsonObj.get("language"));
      }
      // validate the optional field `licence`
      if (jsonObj.get("licence") != null && !jsonObj.get("licence").isJsonNull()) {
        VideoConstantNumberLicence.validateJsonElement(jsonObj.get("licence"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("previewPath") != null && !jsonObj.get("previewPath").isJsonNull()) && !jsonObj.get("previewPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `previewPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("previewPath").toString()));
      }
      // validate the optional field `privacy`
      if (jsonObj.get("privacy") != null && !jsonObj.get("privacy").isJsonNull()) {
        VideoPrivacyConstant.validateJsonElement(jsonObj.get("privacy"));
      }
      // validate the optional field `scheduledUpdate`
      if (jsonObj.get("scheduledUpdate") != null && !jsonObj.get("scheduledUpdate").isJsonNull()) {
        VideoScheduledUpdate.validateJsonElement(jsonObj.get("scheduledUpdate"));
      }
      if ((jsonObj.get("shortUUID") != null && !jsonObj.get("shortUUID").isJsonNull()) && !jsonObj.get("shortUUID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shortUUID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shortUUID").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        VideoStateConstant.validateJsonElement(jsonObj.get("state"));
      }
      if ((jsonObj.get("thumbnailPath") != null && !jsonObj.get("thumbnailPath").isJsonNull()) && !jsonObj.get("thumbnailPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `thumbnailPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("thumbnailPath").toString()));
      }
      // validate the optional field `userHistory`
      if (jsonObj.get("userHistory") != null && !jsonObj.get("userHistory").isJsonNull()) {
        VideoUserHistory.validateJsonElement(jsonObj.get("userHistory"));
      }
      if ((jsonObj.get("uuid") != null && !jsonObj.get("uuid").isJsonNull()) && !jsonObj.get("uuid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uuid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uuid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Video.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Video' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Video> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Video.class));

       return (TypeAdapter<T>) new TypeAdapter<Video>() {
           @Override
           public void write(JsonWriter out, Video value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Video read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Video given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Video
   * @throws IOException if the JSON string is invalid with respect to Video
   */
  public static Video fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Video.class);
  }

  /**
   * Convert an instance of Video to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

