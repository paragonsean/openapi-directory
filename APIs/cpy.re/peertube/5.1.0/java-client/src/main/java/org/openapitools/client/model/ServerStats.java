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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ServerStatsVideosRedundancyInner;

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
 * ServerStats
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerStats {
  public static final String SERIALIZED_NAME_ACTIVITY_PUB_MESSAGES_PROCESSED_PER_SECOND = "activityPubMessagesProcessedPerSecond";
  @SerializedName(SERIALIZED_NAME_ACTIVITY_PUB_MESSAGES_PROCESSED_PER_SECOND)
  private BigDecimal activityPubMessagesProcessedPerSecond;

  public static final String SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_ERRORS = "totalActivityPubMessagesErrors";
  @SerializedName(SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_ERRORS)
  private BigDecimal totalActivityPubMessagesErrors;

  public static final String SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_PROCESSED = "totalActivityPubMessagesProcessed";
  @SerializedName(SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_PROCESSED)
  private BigDecimal totalActivityPubMessagesProcessed;

  public static final String SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_SUCCESSES = "totalActivityPubMessagesSuccesses";
  @SerializedName(SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_SUCCESSES)
  private BigDecimal totalActivityPubMessagesSuccesses;

  public static final String SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_WAITING = "totalActivityPubMessagesWaiting";
  @SerializedName(SERIALIZED_NAME_TOTAL_ACTIVITY_PUB_MESSAGES_WAITING)
  private BigDecimal totalActivityPubMessagesWaiting;

  public static final String SERIALIZED_NAME_TOTAL_DAILY_ACTIVE_USERS = "totalDailyActiveUsers";
  @SerializedName(SERIALIZED_NAME_TOTAL_DAILY_ACTIVE_USERS)
  private BigDecimal totalDailyActiveUsers;

  public static final String SERIALIZED_NAME_TOTAL_INSTANCE_FOLLOWERS = "totalInstanceFollowers";
  @SerializedName(SERIALIZED_NAME_TOTAL_INSTANCE_FOLLOWERS)
  private BigDecimal totalInstanceFollowers;

  public static final String SERIALIZED_NAME_TOTAL_INSTANCE_FOLLOWING = "totalInstanceFollowing";
  @SerializedName(SERIALIZED_NAME_TOTAL_INSTANCE_FOLLOWING)
  private BigDecimal totalInstanceFollowing;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_DAILY_ACTIVE_VIDEO_CHANNELS = "totalLocalDailyActiveVideoChannels";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_DAILY_ACTIVE_VIDEO_CHANNELS)
  private BigDecimal totalLocalDailyActiveVideoChannels;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_MONTHLY_ACTIVE_VIDEO_CHANNELS = "totalLocalMonthlyActiveVideoChannels";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_MONTHLY_ACTIVE_VIDEO_CHANNELS)
  private BigDecimal totalLocalMonthlyActiveVideoChannels;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_PLAYLISTS = "totalLocalPlaylists";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_PLAYLISTS)
  private BigDecimal totalLocalPlaylists;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_CHANNELS = "totalLocalVideoChannels";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_CHANNELS)
  private BigDecimal totalLocalVideoChannels;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_COMMENTS = "totalLocalVideoComments";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_COMMENTS)
  private BigDecimal totalLocalVideoComments;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_FILES_SIZE = "totalLocalVideoFilesSize";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_FILES_SIZE)
  private BigDecimal totalLocalVideoFilesSize;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_VIEWS = "totalLocalVideoViews";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_VIDEO_VIEWS)
  private BigDecimal totalLocalVideoViews;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_VIDEOS = "totalLocalVideos";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_VIDEOS)
  private BigDecimal totalLocalVideos;

  public static final String SERIALIZED_NAME_TOTAL_LOCAL_WEEKLY_ACTIVE_VIDEO_CHANNELS = "totalLocalWeeklyActiveVideoChannels";
  @SerializedName(SERIALIZED_NAME_TOTAL_LOCAL_WEEKLY_ACTIVE_VIDEO_CHANNELS)
  private BigDecimal totalLocalWeeklyActiveVideoChannels;

  public static final String SERIALIZED_NAME_TOTAL_MONTHLY_ACTIVE_USERS = "totalMonthlyActiveUsers";
  @SerializedName(SERIALIZED_NAME_TOTAL_MONTHLY_ACTIVE_USERS)
  private BigDecimal totalMonthlyActiveUsers;

  public static final String SERIALIZED_NAME_TOTAL_USERS = "totalUsers";
  @SerializedName(SERIALIZED_NAME_TOTAL_USERS)
  private BigDecimal totalUsers;

  public static final String SERIALIZED_NAME_TOTAL_VIDEO_COMMENTS = "totalVideoComments";
  @SerializedName(SERIALIZED_NAME_TOTAL_VIDEO_COMMENTS)
  private BigDecimal totalVideoComments;

  public static final String SERIALIZED_NAME_TOTAL_VIDEOS = "totalVideos";
  @SerializedName(SERIALIZED_NAME_TOTAL_VIDEOS)
  private BigDecimal totalVideos;

  public static final String SERIALIZED_NAME_TOTAL_WEEKLY_ACTIVE_USERS = "totalWeeklyActiveUsers";
  @SerializedName(SERIALIZED_NAME_TOTAL_WEEKLY_ACTIVE_USERS)
  private BigDecimal totalWeeklyActiveUsers;

  public static final String SERIALIZED_NAME_VIDEOS_REDUNDANCY = "videosRedundancy";
  @SerializedName(SERIALIZED_NAME_VIDEOS_REDUNDANCY)
  private List<ServerStatsVideosRedundancyInner> videosRedundancy = new ArrayList<>();

  public ServerStats() {
  }

  public ServerStats activityPubMessagesProcessedPerSecond(BigDecimal activityPubMessagesProcessedPerSecond) {
    this.activityPubMessagesProcessedPerSecond = activityPubMessagesProcessedPerSecond;
    return this;
  }

  /**
   * Get activityPubMessagesProcessedPerSecond
   * @return activityPubMessagesProcessedPerSecond
   */
  @javax.annotation.Nullable
  public BigDecimal getActivityPubMessagesProcessedPerSecond() {
    return activityPubMessagesProcessedPerSecond;
  }

  public void setActivityPubMessagesProcessedPerSecond(BigDecimal activityPubMessagesProcessedPerSecond) {
    this.activityPubMessagesProcessedPerSecond = activityPubMessagesProcessedPerSecond;
  }


  public ServerStats totalActivityPubMessagesErrors(BigDecimal totalActivityPubMessagesErrors) {
    this.totalActivityPubMessagesErrors = totalActivityPubMessagesErrors;
    return this;
  }

  /**
   * Get totalActivityPubMessagesErrors
   * @return totalActivityPubMessagesErrors
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalActivityPubMessagesErrors() {
    return totalActivityPubMessagesErrors;
  }

  public void setTotalActivityPubMessagesErrors(BigDecimal totalActivityPubMessagesErrors) {
    this.totalActivityPubMessagesErrors = totalActivityPubMessagesErrors;
  }


  public ServerStats totalActivityPubMessagesProcessed(BigDecimal totalActivityPubMessagesProcessed) {
    this.totalActivityPubMessagesProcessed = totalActivityPubMessagesProcessed;
    return this;
  }

  /**
   * Get totalActivityPubMessagesProcessed
   * @return totalActivityPubMessagesProcessed
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalActivityPubMessagesProcessed() {
    return totalActivityPubMessagesProcessed;
  }

  public void setTotalActivityPubMessagesProcessed(BigDecimal totalActivityPubMessagesProcessed) {
    this.totalActivityPubMessagesProcessed = totalActivityPubMessagesProcessed;
  }


  public ServerStats totalActivityPubMessagesSuccesses(BigDecimal totalActivityPubMessagesSuccesses) {
    this.totalActivityPubMessagesSuccesses = totalActivityPubMessagesSuccesses;
    return this;
  }

  /**
   * Get totalActivityPubMessagesSuccesses
   * @return totalActivityPubMessagesSuccesses
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalActivityPubMessagesSuccesses() {
    return totalActivityPubMessagesSuccesses;
  }

  public void setTotalActivityPubMessagesSuccesses(BigDecimal totalActivityPubMessagesSuccesses) {
    this.totalActivityPubMessagesSuccesses = totalActivityPubMessagesSuccesses;
  }


  public ServerStats totalActivityPubMessagesWaiting(BigDecimal totalActivityPubMessagesWaiting) {
    this.totalActivityPubMessagesWaiting = totalActivityPubMessagesWaiting;
    return this;
  }

  /**
   * Get totalActivityPubMessagesWaiting
   * @return totalActivityPubMessagesWaiting
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalActivityPubMessagesWaiting() {
    return totalActivityPubMessagesWaiting;
  }

  public void setTotalActivityPubMessagesWaiting(BigDecimal totalActivityPubMessagesWaiting) {
    this.totalActivityPubMessagesWaiting = totalActivityPubMessagesWaiting;
  }


  public ServerStats totalDailyActiveUsers(BigDecimal totalDailyActiveUsers) {
    this.totalDailyActiveUsers = totalDailyActiveUsers;
    return this;
  }

  /**
   * Get totalDailyActiveUsers
   * @return totalDailyActiveUsers
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalDailyActiveUsers() {
    return totalDailyActiveUsers;
  }

  public void setTotalDailyActiveUsers(BigDecimal totalDailyActiveUsers) {
    this.totalDailyActiveUsers = totalDailyActiveUsers;
  }


  public ServerStats totalInstanceFollowers(BigDecimal totalInstanceFollowers) {
    this.totalInstanceFollowers = totalInstanceFollowers;
    return this;
  }

  /**
   * Get totalInstanceFollowers
   * @return totalInstanceFollowers
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalInstanceFollowers() {
    return totalInstanceFollowers;
  }

  public void setTotalInstanceFollowers(BigDecimal totalInstanceFollowers) {
    this.totalInstanceFollowers = totalInstanceFollowers;
  }


  public ServerStats totalInstanceFollowing(BigDecimal totalInstanceFollowing) {
    this.totalInstanceFollowing = totalInstanceFollowing;
    return this;
  }

  /**
   * Get totalInstanceFollowing
   * @return totalInstanceFollowing
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalInstanceFollowing() {
    return totalInstanceFollowing;
  }

  public void setTotalInstanceFollowing(BigDecimal totalInstanceFollowing) {
    this.totalInstanceFollowing = totalInstanceFollowing;
  }


  public ServerStats totalLocalDailyActiveVideoChannels(BigDecimal totalLocalDailyActiveVideoChannels) {
    this.totalLocalDailyActiveVideoChannels = totalLocalDailyActiveVideoChannels;
    return this;
  }

  /**
   * Get totalLocalDailyActiveVideoChannels
   * @return totalLocalDailyActiveVideoChannels
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalDailyActiveVideoChannels() {
    return totalLocalDailyActiveVideoChannels;
  }

  public void setTotalLocalDailyActiveVideoChannels(BigDecimal totalLocalDailyActiveVideoChannels) {
    this.totalLocalDailyActiveVideoChannels = totalLocalDailyActiveVideoChannels;
  }


  public ServerStats totalLocalMonthlyActiveVideoChannels(BigDecimal totalLocalMonthlyActiveVideoChannels) {
    this.totalLocalMonthlyActiveVideoChannels = totalLocalMonthlyActiveVideoChannels;
    return this;
  }

  /**
   * Get totalLocalMonthlyActiveVideoChannels
   * @return totalLocalMonthlyActiveVideoChannels
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalMonthlyActiveVideoChannels() {
    return totalLocalMonthlyActiveVideoChannels;
  }

  public void setTotalLocalMonthlyActiveVideoChannels(BigDecimal totalLocalMonthlyActiveVideoChannels) {
    this.totalLocalMonthlyActiveVideoChannels = totalLocalMonthlyActiveVideoChannels;
  }


  public ServerStats totalLocalPlaylists(BigDecimal totalLocalPlaylists) {
    this.totalLocalPlaylists = totalLocalPlaylists;
    return this;
  }

  /**
   * Get totalLocalPlaylists
   * @return totalLocalPlaylists
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalPlaylists() {
    return totalLocalPlaylists;
  }

  public void setTotalLocalPlaylists(BigDecimal totalLocalPlaylists) {
    this.totalLocalPlaylists = totalLocalPlaylists;
  }


  public ServerStats totalLocalVideoChannels(BigDecimal totalLocalVideoChannels) {
    this.totalLocalVideoChannels = totalLocalVideoChannels;
    return this;
  }

  /**
   * Get totalLocalVideoChannels
   * @return totalLocalVideoChannels
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalVideoChannels() {
    return totalLocalVideoChannels;
  }

  public void setTotalLocalVideoChannels(BigDecimal totalLocalVideoChannels) {
    this.totalLocalVideoChannels = totalLocalVideoChannels;
  }


  public ServerStats totalLocalVideoComments(BigDecimal totalLocalVideoComments) {
    this.totalLocalVideoComments = totalLocalVideoComments;
    return this;
  }

  /**
   * Total comments made by local users
   * @return totalLocalVideoComments
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalVideoComments() {
    return totalLocalVideoComments;
  }

  public void setTotalLocalVideoComments(BigDecimal totalLocalVideoComments) {
    this.totalLocalVideoComments = totalLocalVideoComments;
  }


  public ServerStats totalLocalVideoFilesSize(BigDecimal totalLocalVideoFilesSize) {
    this.totalLocalVideoFilesSize = totalLocalVideoFilesSize;
    return this;
  }

  /**
   * Get totalLocalVideoFilesSize
   * @return totalLocalVideoFilesSize
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalVideoFilesSize() {
    return totalLocalVideoFilesSize;
  }

  public void setTotalLocalVideoFilesSize(BigDecimal totalLocalVideoFilesSize) {
    this.totalLocalVideoFilesSize = totalLocalVideoFilesSize;
  }


  public ServerStats totalLocalVideoViews(BigDecimal totalLocalVideoViews) {
    this.totalLocalVideoViews = totalLocalVideoViews;
    return this;
  }

  /**
   * Total video views made on the instance
   * @return totalLocalVideoViews
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalVideoViews() {
    return totalLocalVideoViews;
  }

  public void setTotalLocalVideoViews(BigDecimal totalLocalVideoViews) {
    this.totalLocalVideoViews = totalLocalVideoViews;
  }


  public ServerStats totalLocalVideos(BigDecimal totalLocalVideos) {
    this.totalLocalVideos = totalLocalVideos;
    return this;
  }

  /**
   * Get totalLocalVideos
   * @return totalLocalVideos
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalVideos() {
    return totalLocalVideos;
  }

  public void setTotalLocalVideos(BigDecimal totalLocalVideos) {
    this.totalLocalVideos = totalLocalVideos;
  }


  public ServerStats totalLocalWeeklyActiveVideoChannels(BigDecimal totalLocalWeeklyActiveVideoChannels) {
    this.totalLocalWeeklyActiveVideoChannels = totalLocalWeeklyActiveVideoChannels;
    return this;
  }

  /**
   * Get totalLocalWeeklyActiveVideoChannels
   * @return totalLocalWeeklyActiveVideoChannels
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalLocalWeeklyActiveVideoChannels() {
    return totalLocalWeeklyActiveVideoChannels;
  }

  public void setTotalLocalWeeklyActiveVideoChannels(BigDecimal totalLocalWeeklyActiveVideoChannels) {
    this.totalLocalWeeklyActiveVideoChannels = totalLocalWeeklyActiveVideoChannels;
  }


  public ServerStats totalMonthlyActiveUsers(BigDecimal totalMonthlyActiveUsers) {
    this.totalMonthlyActiveUsers = totalMonthlyActiveUsers;
    return this;
  }

  /**
   * Get totalMonthlyActiveUsers
   * @return totalMonthlyActiveUsers
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalMonthlyActiveUsers() {
    return totalMonthlyActiveUsers;
  }

  public void setTotalMonthlyActiveUsers(BigDecimal totalMonthlyActiveUsers) {
    this.totalMonthlyActiveUsers = totalMonthlyActiveUsers;
  }


  public ServerStats totalUsers(BigDecimal totalUsers) {
    this.totalUsers = totalUsers;
    return this;
  }

  /**
   * Get totalUsers
   * @return totalUsers
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalUsers() {
    return totalUsers;
  }

  public void setTotalUsers(BigDecimal totalUsers) {
    this.totalUsers = totalUsers;
  }


  public ServerStats totalVideoComments(BigDecimal totalVideoComments) {
    this.totalVideoComments = totalVideoComments;
    return this;
  }

  /**
   * Get totalVideoComments
   * @return totalVideoComments
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalVideoComments() {
    return totalVideoComments;
  }

  public void setTotalVideoComments(BigDecimal totalVideoComments) {
    this.totalVideoComments = totalVideoComments;
  }


  public ServerStats totalVideos(BigDecimal totalVideos) {
    this.totalVideos = totalVideos;
    return this;
  }

  /**
   * Get totalVideos
   * @return totalVideos
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalVideos() {
    return totalVideos;
  }

  public void setTotalVideos(BigDecimal totalVideos) {
    this.totalVideos = totalVideos;
  }


  public ServerStats totalWeeklyActiveUsers(BigDecimal totalWeeklyActiveUsers) {
    this.totalWeeklyActiveUsers = totalWeeklyActiveUsers;
    return this;
  }

  /**
   * Get totalWeeklyActiveUsers
   * @return totalWeeklyActiveUsers
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalWeeklyActiveUsers() {
    return totalWeeklyActiveUsers;
  }

  public void setTotalWeeklyActiveUsers(BigDecimal totalWeeklyActiveUsers) {
    this.totalWeeklyActiveUsers = totalWeeklyActiveUsers;
  }


  public ServerStats videosRedundancy(List<ServerStatsVideosRedundancyInner> videosRedundancy) {
    this.videosRedundancy = videosRedundancy;
    return this;
  }

  public ServerStats addVideosRedundancyItem(ServerStatsVideosRedundancyInner videosRedundancyItem) {
    if (this.videosRedundancy == null) {
      this.videosRedundancy = new ArrayList<>();
    }
    this.videosRedundancy.add(videosRedundancyItem);
    return this;
  }

  /**
   * Get videosRedundancy
   * @return videosRedundancy
   */
  @javax.annotation.Nullable
  public List<ServerStatsVideosRedundancyInner> getVideosRedundancy() {
    return videosRedundancy;
  }

  public void setVideosRedundancy(List<ServerStatsVideosRedundancyInner> videosRedundancy) {
    this.videosRedundancy = videosRedundancy;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerStats serverStats = (ServerStats) o;
    return Objects.equals(this.activityPubMessagesProcessedPerSecond, serverStats.activityPubMessagesProcessedPerSecond) &&
        Objects.equals(this.totalActivityPubMessagesErrors, serverStats.totalActivityPubMessagesErrors) &&
        Objects.equals(this.totalActivityPubMessagesProcessed, serverStats.totalActivityPubMessagesProcessed) &&
        Objects.equals(this.totalActivityPubMessagesSuccesses, serverStats.totalActivityPubMessagesSuccesses) &&
        Objects.equals(this.totalActivityPubMessagesWaiting, serverStats.totalActivityPubMessagesWaiting) &&
        Objects.equals(this.totalDailyActiveUsers, serverStats.totalDailyActiveUsers) &&
        Objects.equals(this.totalInstanceFollowers, serverStats.totalInstanceFollowers) &&
        Objects.equals(this.totalInstanceFollowing, serverStats.totalInstanceFollowing) &&
        Objects.equals(this.totalLocalDailyActiveVideoChannels, serverStats.totalLocalDailyActiveVideoChannels) &&
        Objects.equals(this.totalLocalMonthlyActiveVideoChannels, serverStats.totalLocalMonthlyActiveVideoChannels) &&
        Objects.equals(this.totalLocalPlaylists, serverStats.totalLocalPlaylists) &&
        Objects.equals(this.totalLocalVideoChannels, serverStats.totalLocalVideoChannels) &&
        Objects.equals(this.totalLocalVideoComments, serverStats.totalLocalVideoComments) &&
        Objects.equals(this.totalLocalVideoFilesSize, serverStats.totalLocalVideoFilesSize) &&
        Objects.equals(this.totalLocalVideoViews, serverStats.totalLocalVideoViews) &&
        Objects.equals(this.totalLocalVideos, serverStats.totalLocalVideos) &&
        Objects.equals(this.totalLocalWeeklyActiveVideoChannels, serverStats.totalLocalWeeklyActiveVideoChannels) &&
        Objects.equals(this.totalMonthlyActiveUsers, serverStats.totalMonthlyActiveUsers) &&
        Objects.equals(this.totalUsers, serverStats.totalUsers) &&
        Objects.equals(this.totalVideoComments, serverStats.totalVideoComments) &&
        Objects.equals(this.totalVideos, serverStats.totalVideos) &&
        Objects.equals(this.totalWeeklyActiveUsers, serverStats.totalWeeklyActiveUsers) &&
        Objects.equals(this.videosRedundancy, serverStats.videosRedundancy);
  }

  @Override
  public int hashCode() {
    return Objects.hash(activityPubMessagesProcessedPerSecond, totalActivityPubMessagesErrors, totalActivityPubMessagesProcessed, totalActivityPubMessagesSuccesses, totalActivityPubMessagesWaiting, totalDailyActiveUsers, totalInstanceFollowers, totalInstanceFollowing, totalLocalDailyActiveVideoChannels, totalLocalMonthlyActiveVideoChannels, totalLocalPlaylists, totalLocalVideoChannels, totalLocalVideoComments, totalLocalVideoFilesSize, totalLocalVideoViews, totalLocalVideos, totalLocalWeeklyActiveVideoChannels, totalMonthlyActiveUsers, totalUsers, totalVideoComments, totalVideos, totalWeeklyActiveUsers, videosRedundancy);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerStats {\n");
    sb.append("    activityPubMessagesProcessedPerSecond: ").append(toIndentedString(activityPubMessagesProcessedPerSecond)).append("\n");
    sb.append("    totalActivityPubMessagesErrors: ").append(toIndentedString(totalActivityPubMessagesErrors)).append("\n");
    sb.append("    totalActivityPubMessagesProcessed: ").append(toIndentedString(totalActivityPubMessagesProcessed)).append("\n");
    sb.append("    totalActivityPubMessagesSuccesses: ").append(toIndentedString(totalActivityPubMessagesSuccesses)).append("\n");
    sb.append("    totalActivityPubMessagesWaiting: ").append(toIndentedString(totalActivityPubMessagesWaiting)).append("\n");
    sb.append("    totalDailyActiveUsers: ").append(toIndentedString(totalDailyActiveUsers)).append("\n");
    sb.append("    totalInstanceFollowers: ").append(toIndentedString(totalInstanceFollowers)).append("\n");
    sb.append("    totalInstanceFollowing: ").append(toIndentedString(totalInstanceFollowing)).append("\n");
    sb.append("    totalLocalDailyActiveVideoChannels: ").append(toIndentedString(totalLocalDailyActiveVideoChannels)).append("\n");
    sb.append("    totalLocalMonthlyActiveVideoChannels: ").append(toIndentedString(totalLocalMonthlyActiveVideoChannels)).append("\n");
    sb.append("    totalLocalPlaylists: ").append(toIndentedString(totalLocalPlaylists)).append("\n");
    sb.append("    totalLocalVideoChannels: ").append(toIndentedString(totalLocalVideoChannels)).append("\n");
    sb.append("    totalLocalVideoComments: ").append(toIndentedString(totalLocalVideoComments)).append("\n");
    sb.append("    totalLocalVideoFilesSize: ").append(toIndentedString(totalLocalVideoFilesSize)).append("\n");
    sb.append("    totalLocalVideoViews: ").append(toIndentedString(totalLocalVideoViews)).append("\n");
    sb.append("    totalLocalVideos: ").append(toIndentedString(totalLocalVideos)).append("\n");
    sb.append("    totalLocalWeeklyActiveVideoChannels: ").append(toIndentedString(totalLocalWeeklyActiveVideoChannels)).append("\n");
    sb.append("    totalMonthlyActiveUsers: ").append(toIndentedString(totalMonthlyActiveUsers)).append("\n");
    sb.append("    totalUsers: ").append(toIndentedString(totalUsers)).append("\n");
    sb.append("    totalVideoComments: ").append(toIndentedString(totalVideoComments)).append("\n");
    sb.append("    totalVideos: ").append(toIndentedString(totalVideos)).append("\n");
    sb.append("    totalWeeklyActiveUsers: ").append(toIndentedString(totalWeeklyActiveUsers)).append("\n");
    sb.append("    videosRedundancy: ").append(toIndentedString(videosRedundancy)).append("\n");
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
    openapiFields.add("activityPubMessagesProcessedPerSecond");
    openapiFields.add("totalActivityPubMessagesErrors");
    openapiFields.add("totalActivityPubMessagesProcessed");
    openapiFields.add("totalActivityPubMessagesSuccesses");
    openapiFields.add("totalActivityPubMessagesWaiting");
    openapiFields.add("totalDailyActiveUsers");
    openapiFields.add("totalInstanceFollowers");
    openapiFields.add("totalInstanceFollowing");
    openapiFields.add("totalLocalDailyActiveVideoChannels");
    openapiFields.add("totalLocalMonthlyActiveVideoChannels");
    openapiFields.add("totalLocalPlaylists");
    openapiFields.add("totalLocalVideoChannels");
    openapiFields.add("totalLocalVideoComments");
    openapiFields.add("totalLocalVideoFilesSize");
    openapiFields.add("totalLocalVideoViews");
    openapiFields.add("totalLocalVideos");
    openapiFields.add("totalLocalWeeklyActiveVideoChannels");
    openapiFields.add("totalMonthlyActiveUsers");
    openapiFields.add("totalUsers");
    openapiFields.add("totalVideoComments");
    openapiFields.add("totalVideos");
    openapiFields.add("totalWeeklyActiveUsers");
    openapiFields.add("videosRedundancy");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerStats
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerStats.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerStats is not found in the empty JSON string", ServerStats.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerStats.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerStats` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("videosRedundancy") != null && !jsonObj.get("videosRedundancy").isJsonNull()) {
        JsonArray jsonArrayvideosRedundancy = jsonObj.getAsJsonArray("videosRedundancy");
        if (jsonArrayvideosRedundancy != null) {
          // ensure the json data is an array
          if (!jsonObj.get("videosRedundancy").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `videosRedundancy` to be an array in the JSON string but got `%s`", jsonObj.get("videosRedundancy").toString()));
          }

          // validate the optional field `videosRedundancy` (array)
          for (int i = 0; i < jsonArrayvideosRedundancy.size(); i++) {
            ServerStatsVideosRedundancyInner.validateJsonElement(jsonArrayvideosRedundancy.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerStats.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerStats' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerStats> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerStats.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerStats>() {
           @Override
           public void write(JsonWriter out, ServerStats value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerStats read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerStats given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerStats
   * @throws IOException if the JSON string is invalid with respect to ServerStats
   */
  public static ServerStats fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerStats.class);
  }

  /**
   * Convert an instance of ServerStats to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

