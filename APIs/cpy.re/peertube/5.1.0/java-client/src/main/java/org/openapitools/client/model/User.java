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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Account;
import org.openapitools.client.model.NSFWPolicy;
import org.openapitools.client.model.UserRole;
import org.openapitools.client.model.VideoChannel;

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
 * User
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class User {
  public static final String SERIALIZED_NAME_ACCOUNT = "account";
  @SerializedName(SERIALIZED_NAME_ACCOUNT)
  private Account account;

  public static final String SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO = "autoPlayNextVideo";
  @SerializedName(SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO)
  private Boolean autoPlayNextVideo;

  public static final String SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO_PLAYLIST = "autoPlayNextVideoPlaylist";
  @SerializedName(SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO_PLAYLIST)
  private Boolean autoPlayNextVideoPlaylist;

  public static final String SERIALIZED_NAME_AUTO_PLAY_VIDEO = "autoPlayVideo";
  @SerializedName(SERIALIZED_NAME_AUTO_PLAY_VIDEO)
  private Boolean autoPlayVideo;

  public static final String SERIALIZED_NAME_BLOCKED = "blocked";
  @SerializedName(SERIALIZED_NAME_BLOCKED)
  private Boolean blocked;

  public static final String SERIALIZED_NAME_BLOCKED_REASON = "blockedReason";
  @SerializedName(SERIALIZED_NAME_BLOCKED_REASON)
  private String blockedReason;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_EMAIL_VERIFIED = "emailVerified";
  @SerializedName(SERIALIZED_NAME_EMAIL_VERIFIED)
  private Boolean emailVerified;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LAST_LOGIN_DATE = "lastLoginDate";
  @SerializedName(SERIALIZED_NAME_LAST_LOGIN_DATE)
  private OffsetDateTime lastLoginDate;

  public static final String SERIALIZED_NAME_NO_ACCOUNT_SETUP_WARNING_MODAL = "noAccountSetupWarningModal";
  @SerializedName(SERIALIZED_NAME_NO_ACCOUNT_SETUP_WARNING_MODAL)
  private Boolean noAccountSetupWarningModal;

  public static final String SERIALIZED_NAME_NO_INSTANCE_CONFIG_WARNING_MODAL = "noInstanceConfigWarningModal";
  @SerializedName(SERIALIZED_NAME_NO_INSTANCE_CONFIG_WARNING_MODAL)
  private Boolean noInstanceConfigWarningModal;

  public static final String SERIALIZED_NAME_NO_WELCOME_MODAL = "noWelcomeModal";
  @SerializedName(SERIALIZED_NAME_NO_WELCOME_MODAL)
  private Boolean noWelcomeModal;

  public static final String SERIALIZED_NAME_NSFW_POLICY = "nsfwPolicy";
  @SerializedName(SERIALIZED_NAME_NSFW_POLICY)
  private NSFWPolicy nsfwPolicy;

  public static final String SERIALIZED_NAME_P2P_ENABLED = "p2pEnabled";
  @SerializedName(SERIALIZED_NAME_P2P_ENABLED)
  private Boolean p2pEnabled;

  public static final String SERIALIZED_NAME_PLUGIN_AUTH = "pluginAuth";
  @SerializedName(SERIALIZED_NAME_PLUGIN_AUTH)
  private String pluginAuth;

  public static final String SERIALIZED_NAME_ROLE = "role";
  @SerializedName(SERIALIZED_NAME_ROLE)
  private UserRole role;

  public static final String SERIALIZED_NAME_THEME = "theme";
  @SerializedName(SERIALIZED_NAME_THEME)
  private String theme;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public static final String SERIALIZED_NAME_VIDEO_CHANNELS = "videoChannels";
  @SerializedName(SERIALIZED_NAME_VIDEO_CHANNELS)
  private List<VideoChannel> videoChannels = new ArrayList<>();

  public static final String SERIALIZED_NAME_VIDEO_QUOTA = "videoQuota";
  @SerializedName(SERIALIZED_NAME_VIDEO_QUOTA)
  private Integer videoQuota;

  public static final String SERIALIZED_NAME_VIDEO_QUOTA_DAILY = "videoQuotaDaily";
  @SerializedName(SERIALIZED_NAME_VIDEO_QUOTA_DAILY)
  private Integer videoQuotaDaily;

  public User() {
  }

  public User(
     Integer id
  ) {
    this();
    this.id = id;
  }

  public User account(Account account) {
    this.account = account;
    return this;
  }

  /**
   * Get account
   * @return account
   */
  @javax.annotation.Nullable
  public Account getAccount() {
    return account;
  }

  public void setAccount(Account account) {
    this.account = account;
  }


  public User autoPlayNextVideo(Boolean autoPlayNextVideo) {
    this.autoPlayNextVideo = autoPlayNextVideo;
    return this;
  }

  /**
   * Automatically start playing the upcoming video after the currently playing video
   * @return autoPlayNextVideo
   */
  @javax.annotation.Nullable
  public Boolean getAutoPlayNextVideo() {
    return autoPlayNextVideo;
  }

  public void setAutoPlayNextVideo(Boolean autoPlayNextVideo) {
    this.autoPlayNextVideo = autoPlayNextVideo;
  }


  public User autoPlayNextVideoPlaylist(Boolean autoPlayNextVideoPlaylist) {
    this.autoPlayNextVideoPlaylist = autoPlayNextVideoPlaylist;
    return this;
  }

  /**
   * Automatically start playing the video on the playlist after the currently playing video
   * @return autoPlayNextVideoPlaylist
   */
  @javax.annotation.Nullable
  public Boolean getAutoPlayNextVideoPlaylist() {
    return autoPlayNextVideoPlaylist;
  }

  public void setAutoPlayNextVideoPlaylist(Boolean autoPlayNextVideoPlaylist) {
    this.autoPlayNextVideoPlaylist = autoPlayNextVideoPlaylist;
  }


  public User autoPlayVideo(Boolean autoPlayVideo) {
    this.autoPlayVideo = autoPlayVideo;
    return this;
  }

  /**
   * Automatically start playing the video on the watch page
   * @return autoPlayVideo
   */
  @javax.annotation.Nullable
  public Boolean getAutoPlayVideo() {
    return autoPlayVideo;
  }

  public void setAutoPlayVideo(Boolean autoPlayVideo) {
    this.autoPlayVideo = autoPlayVideo;
  }


  public User blocked(Boolean blocked) {
    this.blocked = blocked;
    return this;
  }

  /**
   * Get blocked
   * @return blocked
   */
  @javax.annotation.Nullable
  public Boolean getBlocked() {
    return blocked;
  }

  public void setBlocked(Boolean blocked) {
    this.blocked = blocked;
  }


  public User blockedReason(String blockedReason) {
    this.blockedReason = blockedReason;
    return this;
  }

  /**
   * Get blockedReason
   * @return blockedReason
   */
  @javax.annotation.Nullable
  public String getBlockedReason() {
    return blockedReason;
  }

  public void setBlockedReason(String blockedReason) {
    this.blockedReason = blockedReason;
  }


  public User createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public User email(String email) {
    this.email = email;
    return this;
  }

  /**
   * The user email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public User emailVerified(Boolean emailVerified) {
    this.emailVerified = emailVerified;
    return this;
  }

  /**
   * Has the user confirmed their email address?
   * @return emailVerified
   */
  @javax.annotation.Nullable
  public Boolean getEmailVerified() {
    return emailVerified;
  }

  public void setEmailVerified(Boolean emailVerified) {
    this.emailVerified = emailVerified;
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



  public User lastLoginDate(OffsetDateTime lastLoginDate) {
    this.lastLoginDate = lastLoginDate;
    return this;
  }

  /**
   * Get lastLoginDate
   * @return lastLoginDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastLoginDate() {
    return lastLoginDate;
  }

  public void setLastLoginDate(OffsetDateTime lastLoginDate) {
    this.lastLoginDate = lastLoginDate;
  }


  public User noAccountSetupWarningModal(Boolean noAccountSetupWarningModal) {
    this.noAccountSetupWarningModal = noAccountSetupWarningModal;
    return this;
  }

  /**
   * Get noAccountSetupWarningModal
   * @return noAccountSetupWarningModal
   */
  @javax.annotation.Nullable
  public Boolean getNoAccountSetupWarningModal() {
    return noAccountSetupWarningModal;
  }

  public void setNoAccountSetupWarningModal(Boolean noAccountSetupWarningModal) {
    this.noAccountSetupWarningModal = noAccountSetupWarningModal;
  }


  public User noInstanceConfigWarningModal(Boolean noInstanceConfigWarningModal) {
    this.noInstanceConfigWarningModal = noInstanceConfigWarningModal;
    return this;
  }

  /**
   * Get noInstanceConfigWarningModal
   * @return noInstanceConfigWarningModal
   */
  @javax.annotation.Nullable
  public Boolean getNoInstanceConfigWarningModal() {
    return noInstanceConfigWarningModal;
  }

  public void setNoInstanceConfigWarningModal(Boolean noInstanceConfigWarningModal) {
    this.noInstanceConfigWarningModal = noInstanceConfigWarningModal;
  }


  public User noWelcomeModal(Boolean noWelcomeModal) {
    this.noWelcomeModal = noWelcomeModal;
    return this;
  }

  /**
   * Get noWelcomeModal
   * @return noWelcomeModal
   */
  @javax.annotation.Nullable
  public Boolean getNoWelcomeModal() {
    return noWelcomeModal;
  }

  public void setNoWelcomeModal(Boolean noWelcomeModal) {
    this.noWelcomeModal = noWelcomeModal;
  }


  public User nsfwPolicy(NSFWPolicy nsfwPolicy) {
    this.nsfwPolicy = nsfwPolicy;
    return this;
  }

  /**
   * Get nsfwPolicy
   * @return nsfwPolicy
   */
  @javax.annotation.Nullable
  public NSFWPolicy getNsfwPolicy() {
    return nsfwPolicy;
  }

  public void setNsfwPolicy(NSFWPolicy nsfwPolicy) {
    this.nsfwPolicy = nsfwPolicy;
  }


  public User p2pEnabled(Boolean p2pEnabled) {
    this.p2pEnabled = p2pEnabled;
    return this;
  }

  /**
   * Enable P2P in the player
   * @return p2pEnabled
   */
  @javax.annotation.Nullable
  public Boolean getP2pEnabled() {
    return p2pEnabled;
  }

  public void setP2pEnabled(Boolean p2pEnabled) {
    this.p2pEnabled = p2pEnabled;
  }


  public User pluginAuth(String pluginAuth) {
    this.pluginAuth = pluginAuth;
    return this;
  }

  /**
   * Auth plugin to use to authenticate the user
   * @return pluginAuth
   */
  @javax.annotation.Nullable
  public String getPluginAuth() {
    return pluginAuth;
  }

  public void setPluginAuth(String pluginAuth) {
    this.pluginAuth = pluginAuth;
  }


  public User role(UserRole role) {
    this.role = role;
    return this;
  }

  /**
   * Get role
   * @return role
   */
  @javax.annotation.Nullable
  public UserRole getRole() {
    return role;
  }

  public void setRole(UserRole role) {
    this.role = role;
  }


  public User theme(String theme) {
    this.theme = theme;
    return this;
  }

  /**
   * Theme enabled by this user
   * @return theme
   */
  @javax.annotation.Nullable
  public String getTheme() {
    return theme;
  }

  public void setTheme(String theme) {
    this.theme = theme;
  }


  public User username(String username) {
    this.username = username;
    return this;
  }

  /**
   * immutable name of the user, used to find or mention its actor
   * @return username
   */
  @javax.annotation.Nullable
  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }


  public User videoChannels(List<VideoChannel> videoChannels) {
    this.videoChannels = videoChannels;
    return this;
  }

  public User addVideoChannelsItem(VideoChannel videoChannelsItem) {
    if (this.videoChannels == null) {
      this.videoChannels = new ArrayList<>();
    }
    this.videoChannels.add(videoChannelsItem);
    return this;
  }

  /**
   * Get videoChannels
   * @return videoChannels
   */
  @javax.annotation.Nullable
  public List<VideoChannel> getVideoChannels() {
    return videoChannels;
  }

  public void setVideoChannels(List<VideoChannel> videoChannels) {
    this.videoChannels = videoChannels;
  }


  public User videoQuota(Integer videoQuota) {
    this.videoQuota = videoQuota;
    return this;
  }

  /**
   * The user video quota in bytes
   * @return videoQuota
   */
  @javax.annotation.Nullable
  public Integer getVideoQuota() {
    return videoQuota;
  }

  public void setVideoQuota(Integer videoQuota) {
    this.videoQuota = videoQuota;
  }


  public User videoQuotaDaily(Integer videoQuotaDaily) {
    this.videoQuotaDaily = videoQuotaDaily;
    return this;
  }

  /**
   * The user daily video quota in bytes
   * @return videoQuotaDaily
   */
  @javax.annotation.Nullable
  public Integer getVideoQuotaDaily() {
    return videoQuotaDaily;
  }

  public void setVideoQuotaDaily(Integer videoQuotaDaily) {
    this.videoQuotaDaily = videoQuotaDaily;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    User user = (User) o;
    return Objects.equals(this.account, user.account) &&
        Objects.equals(this.autoPlayNextVideo, user.autoPlayNextVideo) &&
        Objects.equals(this.autoPlayNextVideoPlaylist, user.autoPlayNextVideoPlaylist) &&
        Objects.equals(this.autoPlayVideo, user.autoPlayVideo) &&
        Objects.equals(this.blocked, user.blocked) &&
        Objects.equals(this.blockedReason, user.blockedReason) &&
        Objects.equals(this.createdAt, user.createdAt) &&
        Objects.equals(this.email, user.email) &&
        Objects.equals(this.emailVerified, user.emailVerified) &&
        Objects.equals(this.id, user.id) &&
        Objects.equals(this.lastLoginDate, user.lastLoginDate) &&
        Objects.equals(this.noAccountSetupWarningModal, user.noAccountSetupWarningModal) &&
        Objects.equals(this.noInstanceConfigWarningModal, user.noInstanceConfigWarningModal) &&
        Objects.equals(this.noWelcomeModal, user.noWelcomeModal) &&
        Objects.equals(this.nsfwPolicy, user.nsfwPolicy) &&
        Objects.equals(this.p2pEnabled, user.p2pEnabled) &&
        Objects.equals(this.pluginAuth, user.pluginAuth) &&
        Objects.equals(this.role, user.role) &&
        Objects.equals(this.theme, user.theme) &&
        Objects.equals(this.username, user.username) &&
        Objects.equals(this.videoChannels, user.videoChannels) &&
        Objects.equals(this.videoQuota, user.videoQuota) &&
        Objects.equals(this.videoQuotaDaily, user.videoQuotaDaily);
  }

  @Override
  public int hashCode() {
    return Objects.hash(account, autoPlayNextVideo, autoPlayNextVideoPlaylist, autoPlayVideo, blocked, blockedReason, createdAt, email, emailVerified, id, lastLoginDate, noAccountSetupWarningModal, noInstanceConfigWarningModal, noWelcomeModal, nsfwPolicy, p2pEnabled, pluginAuth, role, theme, username, videoChannels, videoQuota, videoQuotaDaily);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class User {\n");
    sb.append("    account: ").append(toIndentedString(account)).append("\n");
    sb.append("    autoPlayNextVideo: ").append(toIndentedString(autoPlayNextVideo)).append("\n");
    sb.append("    autoPlayNextVideoPlaylist: ").append(toIndentedString(autoPlayNextVideoPlaylist)).append("\n");
    sb.append("    autoPlayVideo: ").append(toIndentedString(autoPlayVideo)).append("\n");
    sb.append("    blocked: ").append(toIndentedString(blocked)).append("\n");
    sb.append("    blockedReason: ").append(toIndentedString(blockedReason)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    emailVerified: ").append(toIndentedString(emailVerified)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastLoginDate: ").append(toIndentedString(lastLoginDate)).append("\n");
    sb.append("    noAccountSetupWarningModal: ").append(toIndentedString(noAccountSetupWarningModal)).append("\n");
    sb.append("    noInstanceConfigWarningModal: ").append(toIndentedString(noInstanceConfigWarningModal)).append("\n");
    sb.append("    noWelcomeModal: ").append(toIndentedString(noWelcomeModal)).append("\n");
    sb.append("    nsfwPolicy: ").append(toIndentedString(nsfwPolicy)).append("\n");
    sb.append("    p2pEnabled: ").append(toIndentedString(p2pEnabled)).append("\n");
    sb.append("    pluginAuth: ").append(toIndentedString(pluginAuth)).append("\n");
    sb.append("    role: ").append(toIndentedString(role)).append("\n");
    sb.append("    theme: ").append(toIndentedString(theme)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
    sb.append("    videoChannels: ").append(toIndentedString(videoChannels)).append("\n");
    sb.append("    videoQuota: ").append(toIndentedString(videoQuota)).append("\n");
    sb.append("    videoQuotaDaily: ").append(toIndentedString(videoQuotaDaily)).append("\n");
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
    openapiFields.add("autoPlayNextVideo");
    openapiFields.add("autoPlayNextVideoPlaylist");
    openapiFields.add("autoPlayVideo");
    openapiFields.add("blocked");
    openapiFields.add("blockedReason");
    openapiFields.add("createdAt");
    openapiFields.add("email");
    openapiFields.add("emailVerified");
    openapiFields.add("id");
    openapiFields.add("lastLoginDate");
    openapiFields.add("noAccountSetupWarningModal");
    openapiFields.add("noInstanceConfigWarningModal");
    openapiFields.add("noWelcomeModal");
    openapiFields.add("nsfwPolicy");
    openapiFields.add("p2pEnabled");
    openapiFields.add("pluginAuth");
    openapiFields.add("role");
    openapiFields.add("theme");
    openapiFields.add("username");
    openapiFields.add("videoChannels");
    openapiFields.add("videoQuota");
    openapiFields.add("videoQuotaDaily");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to User
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!User.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in User is not found in the empty JSON string", User.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!User.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `User` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `account`
      if (jsonObj.get("account") != null && !jsonObj.get("account").isJsonNull()) {
        Account.validateJsonElement(jsonObj.get("account"));
      }
      if ((jsonObj.get("blockedReason") != null && !jsonObj.get("blockedReason").isJsonNull()) && !jsonObj.get("blockedReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `blockedReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("blockedReason").toString()));
      }
      if ((jsonObj.get("createdAt") != null && !jsonObj.get("createdAt").isJsonNull()) && !jsonObj.get("createdAt").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `createdAt` to be a primitive type in the JSON string but got `%s`", jsonObj.get("createdAt").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      // validate the optional field `nsfwPolicy`
      if (jsonObj.get("nsfwPolicy") != null && !jsonObj.get("nsfwPolicy").isJsonNull()) {
        NSFWPolicy.validateJsonElement(jsonObj.get("nsfwPolicy"));
      }
      if ((jsonObj.get("pluginAuth") != null && !jsonObj.get("pluginAuth").isJsonNull()) && !jsonObj.get("pluginAuth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pluginAuth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pluginAuth").toString()));
      }
      // validate the optional field `role`
      if (jsonObj.get("role") != null && !jsonObj.get("role").isJsonNull()) {
        UserRole.validateJsonElement(jsonObj.get("role"));
      }
      if ((jsonObj.get("theme") != null && !jsonObj.get("theme").isJsonNull()) && !jsonObj.get("theme").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `theme` to be a primitive type in the JSON string but got `%s`", jsonObj.get("theme").toString()));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
      if (jsonObj.get("videoChannels") != null && !jsonObj.get("videoChannels").isJsonNull()) {
        JsonArray jsonArrayvideoChannels = jsonObj.getAsJsonArray("videoChannels");
        if (jsonArrayvideoChannels != null) {
          // ensure the json data is an array
          if (!jsonObj.get("videoChannels").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `videoChannels` to be an array in the JSON string but got `%s`", jsonObj.get("videoChannels").toString()));
          }

          // validate the optional field `videoChannels` (array)
          for (int i = 0; i < jsonArrayvideoChannels.size(); i++) {
            VideoChannel.validateJsonElement(jsonArrayvideoChannels.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!User.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'User' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<User> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(User.class));

       return (TypeAdapter<T>) new TypeAdapter<User>() {
           @Override
           public void write(JsonWriter out, User value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public User read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of User given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of User
   * @throws IOException if the JSON string is invalid with respect to User
   */
  public static User fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, User.class);
  }

  /**
   * Convert an instance of User to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

