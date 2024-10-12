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
import org.openapitools.client.model.ServerConfigAutoBlacklist;
import org.openapitools.client.model.ServerConfigAutoBlacklistVideosOfUsers;
import org.openapitools.client.model.ServerConfigAvatar;
import org.openapitools.client.model.ServerConfigFollowings;
import org.openapitools.client.model.ServerConfigImport;
import org.openapitools.client.model.ServerConfigInstance;
import org.openapitools.client.model.ServerConfigPlugin;
import org.openapitools.client.model.ServerConfigSearch;
import org.openapitools.client.model.ServerConfigSignup;
import org.openapitools.client.model.ServerConfigTranscoding;
import org.openapitools.client.model.ServerConfigTrending;
import org.openapitools.client.model.ServerConfigUser;
import org.openapitools.client.model.ServerConfigVideo;
import org.openapitools.client.model.ServerConfigVideoCaption;

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
 * ServerConfig
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerConfig {
  public static final String SERIALIZED_NAME_AUTO_BLACKLIST = "autoBlacklist";
  @SerializedName(SERIALIZED_NAME_AUTO_BLACKLIST)
  private ServerConfigAutoBlacklist autoBlacklist;

  public static final String SERIALIZED_NAME_AVATAR = "avatar";
  @SerializedName(SERIALIZED_NAME_AVATAR)
  private ServerConfigAvatar avatar;

  public static final String SERIALIZED_NAME_CONTACT_FORM = "contactForm";
  @SerializedName(SERIALIZED_NAME_CONTACT_FORM)
  private ServerConfigAutoBlacklistVideosOfUsers contactForm;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private ServerConfigAutoBlacklistVideosOfUsers email;

  public static final String SERIALIZED_NAME_FOLLOWINGS = "followings";
  @SerializedName(SERIALIZED_NAME_FOLLOWINGS)
  private ServerConfigFollowings followings;

  public static final String SERIALIZED_NAME_HOMEPAGE = "homepage";
  @SerializedName(SERIALIZED_NAME_HOMEPAGE)
  private ServerConfigAutoBlacklistVideosOfUsers homepage;

  public static final String SERIALIZED_NAME_IMPORT = "import";
  @SerializedName(SERIALIZED_NAME_IMPORT)
  private ServerConfigImport _import;

  public static final String SERIALIZED_NAME_INSTANCE = "instance";
  @SerializedName(SERIALIZED_NAME_INSTANCE)
  private ServerConfigInstance instance;

  public static final String SERIALIZED_NAME_PLUGIN = "plugin";
  @SerializedName(SERIALIZED_NAME_PLUGIN)
  private ServerConfigPlugin plugin;

  public static final String SERIALIZED_NAME_SEARCH = "search";
  @SerializedName(SERIALIZED_NAME_SEARCH)
  private ServerConfigSearch search;

  public static final String SERIALIZED_NAME_SERVER_COMMIT = "serverCommit";
  @SerializedName(SERIALIZED_NAME_SERVER_COMMIT)
  private String serverCommit;

  public static final String SERIALIZED_NAME_SERVER_VERSION = "serverVersion";
  @SerializedName(SERIALIZED_NAME_SERVER_VERSION)
  private String serverVersion;

  public static final String SERIALIZED_NAME_SIGNUP = "signup";
  @SerializedName(SERIALIZED_NAME_SIGNUP)
  private ServerConfigSignup signup;

  public static final String SERIALIZED_NAME_THEME = "theme";
  @SerializedName(SERIALIZED_NAME_THEME)
  private ServerConfigPlugin theme;

  public static final String SERIALIZED_NAME_TRACKER = "tracker";
  @SerializedName(SERIALIZED_NAME_TRACKER)
  private ServerConfigAutoBlacklistVideosOfUsers tracker;

  public static final String SERIALIZED_NAME_TRANSCODING = "transcoding";
  @SerializedName(SERIALIZED_NAME_TRANSCODING)
  private ServerConfigTranscoding transcoding;

  public static final String SERIALIZED_NAME_TRENDING = "trending";
  @SerializedName(SERIALIZED_NAME_TRENDING)
  private ServerConfigTrending trending;

  public static final String SERIALIZED_NAME_USER = "user";
  @SerializedName(SERIALIZED_NAME_USER)
  private ServerConfigUser user;

  public static final String SERIALIZED_NAME_VIDEO = "video";
  @SerializedName(SERIALIZED_NAME_VIDEO)
  private ServerConfigVideo video;

  public static final String SERIALIZED_NAME_VIDEO_CAPTION = "videoCaption";
  @SerializedName(SERIALIZED_NAME_VIDEO_CAPTION)
  private ServerConfigVideoCaption videoCaption;

  public ServerConfig() {
  }

  public ServerConfig autoBlacklist(ServerConfigAutoBlacklist autoBlacklist) {
    this.autoBlacklist = autoBlacklist;
    return this;
  }

  /**
   * Get autoBlacklist
   * @return autoBlacklist
   */
  @javax.annotation.Nullable
  public ServerConfigAutoBlacklist getAutoBlacklist() {
    return autoBlacklist;
  }

  public void setAutoBlacklist(ServerConfigAutoBlacklist autoBlacklist) {
    this.autoBlacklist = autoBlacklist;
  }


  public ServerConfig avatar(ServerConfigAvatar avatar) {
    this.avatar = avatar;
    return this;
  }

  /**
   * Get avatar
   * @return avatar
   */
  @javax.annotation.Nullable
  public ServerConfigAvatar getAvatar() {
    return avatar;
  }

  public void setAvatar(ServerConfigAvatar avatar) {
    this.avatar = avatar;
  }


  public ServerConfig contactForm(ServerConfigAutoBlacklistVideosOfUsers contactForm) {
    this.contactForm = contactForm;
    return this;
  }

  /**
   * Get contactForm
   * @return contactForm
   */
  @javax.annotation.Nullable
  public ServerConfigAutoBlacklistVideosOfUsers getContactForm() {
    return contactForm;
  }

  public void setContactForm(ServerConfigAutoBlacklistVideosOfUsers contactForm) {
    this.contactForm = contactForm;
  }


  public ServerConfig email(ServerConfigAutoBlacklistVideosOfUsers email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public ServerConfigAutoBlacklistVideosOfUsers getEmail() {
    return email;
  }

  public void setEmail(ServerConfigAutoBlacklistVideosOfUsers email) {
    this.email = email;
  }


  public ServerConfig followings(ServerConfigFollowings followings) {
    this.followings = followings;
    return this;
  }

  /**
   * Get followings
   * @return followings
   */
  @javax.annotation.Nullable
  public ServerConfigFollowings getFollowings() {
    return followings;
  }

  public void setFollowings(ServerConfigFollowings followings) {
    this.followings = followings;
  }


  public ServerConfig homepage(ServerConfigAutoBlacklistVideosOfUsers homepage) {
    this.homepage = homepage;
    return this;
  }

  /**
   * Get homepage
   * @return homepage
   */
  @javax.annotation.Nullable
  public ServerConfigAutoBlacklistVideosOfUsers getHomepage() {
    return homepage;
  }

  public void setHomepage(ServerConfigAutoBlacklistVideosOfUsers homepage) {
    this.homepage = homepage;
  }


  public ServerConfig _import(ServerConfigImport _import) {
    this._import = _import;
    return this;
  }

  /**
   * Get _import
   * @return _import
   */
  @javax.annotation.Nullable
  public ServerConfigImport getImport() {
    return _import;
  }

  public void setImport(ServerConfigImport _import) {
    this._import = _import;
  }


  public ServerConfig instance(ServerConfigInstance instance) {
    this.instance = instance;
    return this;
  }

  /**
   * Get instance
   * @return instance
   */
  @javax.annotation.Nullable
  public ServerConfigInstance getInstance() {
    return instance;
  }

  public void setInstance(ServerConfigInstance instance) {
    this.instance = instance;
  }


  public ServerConfig plugin(ServerConfigPlugin plugin) {
    this.plugin = plugin;
    return this;
  }

  /**
   * Get plugin
   * @return plugin
   */
  @javax.annotation.Nullable
  public ServerConfigPlugin getPlugin() {
    return plugin;
  }

  public void setPlugin(ServerConfigPlugin plugin) {
    this.plugin = plugin;
  }


  public ServerConfig search(ServerConfigSearch search) {
    this.search = search;
    return this;
  }

  /**
   * Get search
   * @return search
   */
  @javax.annotation.Nullable
  public ServerConfigSearch getSearch() {
    return search;
  }

  public void setSearch(ServerConfigSearch search) {
    this.search = search;
  }


  public ServerConfig serverCommit(String serverCommit) {
    this.serverCommit = serverCommit;
    return this;
  }

  /**
   * Get serverCommit
   * @return serverCommit
   */
  @javax.annotation.Nullable
  public String getServerCommit() {
    return serverCommit;
  }

  public void setServerCommit(String serverCommit) {
    this.serverCommit = serverCommit;
  }


  public ServerConfig serverVersion(String serverVersion) {
    this.serverVersion = serverVersion;
    return this;
  }

  /**
   * Get serverVersion
   * @return serverVersion
   */
  @javax.annotation.Nullable
  public String getServerVersion() {
    return serverVersion;
  }

  public void setServerVersion(String serverVersion) {
    this.serverVersion = serverVersion;
  }


  public ServerConfig signup(ServerConfigSignup signup) {
    this.signup = signup;
    return this;
  }

  /**
   * Get signup
   * @return signup
   */
  @javax.annotation.Nullable
  public ServerConfigSignup getSignup() {
    return signup;
  }

  public void setSignup(ServerConfigSignup signup) {
    this.signup = signup;
  }


  public ServerConfig theme(ServerConfigPlugin theme) {
    this.theme = theme;
    return this;
  }

  /**
   * Get theme
   * @return theme
   */
  @javax.annotation.Nullable
  public ServerConfigPlugin getTheme() {
    return theme;
  }

  public void setTheme(ServerConfigPlugin theme) {
    this.theme = theme;
  }


  public ServerConfig tracker(ServerConfigAutoBlacklistVideosOfUsers tracker) {
    this.tracker = tracker;
    return this;
  }

  /**
   * Get tracker
   * @return tracker
   */
  @javax.annotation.Nullable
  public ServerConfigAutoBlacklistVideosOfUsers getTracker() {
    return tracker;
  }

  public void setTracker(ServerConfigAutoBlacklistVideosOfUsers tracker) {
    this.tracker = tracker;
  }


  public ServerConfig transcoding(ServerConfigTranscoding transcoding) {
    this.transcoding = transcoding;
    return this;
  }

  /**
   * Get transcoding
   * @return transcoding
   */
  @javax.annotation.Nullable
  public ServerConfigTranscoding getTranscoding() {
    return transcoding;
  }

  public void setTranscoding(ServerConfigTranscoding transcoding) {
    this.transcoding = transcoding;
  }


  public ServerConfig trending(ServerConfigTrending trending) {
    this.trending = trending;
    return this;
  }

  /**
   * Get trending
   * @return trending
   */
  @javax.annotation.Nullable
  public ServerConfigTrending getTrending() {
    return trending;
  }

  public void setTrending(ServerConfigTrending trending) {
    this.trending = trending;
  }


  public ServerConfig user(ServerConfigUser user) {
    this.user = user;
    return this;
  }

  /**
   * Get user
   * @return user
   */
  @javax.annotation.Nullable
  public ServerConfigUser getUser() {
    return user;
  }

  public void setUser(ServerConfigUser user) {
    this.user = user;
  }


  public ServerConfig video(ServerConfigVideo video) {
    this.video = video;
    return this;
  }

  /**
   * Get video
   * @return video
   */
  @javax.annotation.Nullable
  public ServerConfigVideo getVideo() {
    return video;
  }

  public void setVideo(ServerConfigVideo video) {
    this.video = video;
  }


  public ServerConfig videoCaption(ServerConfigVideoCaption videoCaption) {
    this.videoCaption = videoCaption;
    return this;
  }

  /**
   * Get videoCaption
   * @return videoCaption
   */
  @javax.annotation.Nullable
  public ServerConfigVideoCaption getVideoCaption() {
    return videoCaption;
  }

  public void setVideoCaption(ServerConfigVideoCaption videoCaption) {
    this.videoCaption = videoCaption;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerConfig serverConfig = (ServerConfig) o;
    return Objects.equals(this.autoBlacklist, serverConfig.autoBlacklist) &&
        Objects.equals(this.avatar, serverConfig.avatar) &&
        Objects.equals(this.contactForm, serverConfig.contactForm) &&
        Objects.equals(this.email, serverConfig.email) &&
        Objects.equals(this.followings, serverConfig.followings) &&
        Objects.equals(this.homepage, serverConfig.homepage) &&
        Objects.equals(this._import, serverConfig._import) &&
        Objects.equals(this.instance, serverConfig.instance) &&
        Objects.equals(this.plugin, serverConfig.plugin) &&
        Objects.equals(this.search, serverConfig.search) &&
        Objects.equals(this.serverCommit, serverConfig.serverCommit) &&
        Objects.equals(this.serverVersion, serverConfig.serverVersion) &&
        Objects.equals(this.signup, serverConfig.signup) &&
        Objects.equals(this.theme, serverConfig.theme) &&
        Objects.equals(this.tracker, serverConfig.tracker) &&
        Objects.equals(this.transcoding, serverConfig.transcoding) &&
        Objects.equals(this.trending, serverConfig.trending) &&
        Objects.equals(this.user, serverConfig.user) &&
        Objects.equals(this.video, serverConfig.video) &&
        Objects.equals(this.videoCaption, serverConfig.videoCaption);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoBlacklist, avatar, contactForm, email, followings, homepage, _import, instance, plugin, search, serverCommit, serverVersion, signup, theme, tracker, transcoding, trending, user, video, videoCaption);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerConfig {\n");
    sb.append("    autoBlacklist: ").append(toIndentedString(autoBlacklist)).append("\n");
    sb.append("    avatar: ").append(toIndentedString(avatar)).append("\n");
    sb.append("    contactForm: ").append(toIndentedString(contactForm)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    followings: ").append(toIndentedString(followings)).append("\n");
    sb.append("    homepage: ").append(toIndentedString(homepage)).append("\n");
    sb.append("    _import: ").append(toIndentedString(_import)).append("\n");
    sb.append("    instance: ").append(toIndentedString(instance)).append("\n");
    sb.append("    plugin: ").append(toIndentedString(plugin)).append("\n");
    sb.append("    search: ").append(toIndentedString(search)).append("\n");
    sb.append("    serverCommit: ").append(toIndentedString(serverCommit)).append("\n");
    sb.append("    serverVersion: ").append(toIndentedString(serverVersion)).append("\n");
    sb.append("    signup: ").append(toIndentedString(signup)).append("\n");
    sb.append("    theme: ").append(toIndentedString(theme)).append("\n");
    sb.append("    tracker: ").append(toIndentedString(tracker)).append("\n");
    sb.append("    transcoding: ").append(toIndentedString(transcoding)).append("\n");
    sb.append("    trending: ").append(toIndentedString(trending)).append("\n");
    sb.append("    user: ").append(toIndentedString(user)).append("\n");
    sb.append("    video: ").append(toIndentedString(video)).append("\n");
    sb.append("    videoCaption: ").append(toIndentedString(videoCaption)).append("\n");
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
    openapiFields.add("autoBlacklist");
    openapiFields.add("avatar");
    openapiFields.add("contactForm");
    openapiFields.add("email");
    openapiFields.add("followings");
    openapiFields.add("homepage");
    openapiFields.add("import");
    openapiFields.add("instance");
    openapiFields.add("plugin");
    openapiFields.add("search");
    openapiFields.add("serverCommit");
    openapiFields.add("serverVersion");
    openapiFields.add("signup");
    openapiFields.add("theme");
    openapiFields.add("tracker");
    openapiFields.add("transcoding");
    openapiFields.add("trending");
    openapiFields.add("user");
    openapiFields.add("video");
    openapiFields.add("videoCaption");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerConfig is not found in the empty JSON string", ServerConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `autoBlacklist`
      if (jsonObj.get("autoBlacklist") != null && !jsonObj.get("autoBlacklist").isJsonNull()) {
        ServerConfigAutoBlacklist.validateJsonElement(jsonObj.get("autoBlacklist"));
      }
      // validate the optional field `avatar`
      if (jsonObj.get("avatar") != null && !jsonObj.get("avatar").isJsonNull()) {
        ServerConfigAvatar.validateJsonElement(jsonObj.get("avatar"));
      }
      // validate the optional field `contactForm`
      if (jsonObj.get("contactForm") != null && !jsonObj.get("contactForm").isJsonNull()) {
        ServerConfigAutoBlacklistVideosOfUsers.validateJsonElement(jsonObj.get("contactForm"));
      }
      // validate the optional field `email`
      if (jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) {
        ServerConfigAutoBlacklistVideosOfUsers.validateJsonElement(jsonObj.get("email"));
      }
      // validate the optional field `followings`
      if (jsonObj.get("followings") != null && !jsonObj.get("followings").isJsonNull()) {
        ServerConfigFollowings.validateJsonElement(jsonObj.get("followings"));
      }
      // validate the optional field `homepage`
      if (jsonObj.get("homepage") != null && !jsonObj.get("homepage").isJsonNull()) {
        ServerConfigAutoBlacklistVideosOfUsers.validateJsonElement(jsonObj.get("homepage"));
      }
      // validate the optional field `import`
      if (jsonObj.get("import") != null && !jsonObj.get("import").isJsonNull()) {
        ServerConfigImport.validateJsonElement(jsonObj.get("import"));
      }
      // validate the optional field `instance`
      if (jsonObj.get("instance") != null && !jsonObj.get("instance").isJsonNull()) {
        ServerConfigInstance.validateJsonElement(jsonObj.get("instance"));
      }
      // validate the optional field `plugin`
      if (jsonObj.get("plugin") != null && !jsonObj.get("plugin").isJsonNull()) {
        ServerConfigPlugin.validateJsonElement(jsonObj.get("plugin"));
      }
      // validate the optional field `search`
      if (jsonObj.get("search") != null && !jsonObj.get("search").isJsonNull()) {
        ServerConfigSearch.validateJsonElement(jsonObj.get("search"));
      }
      if ((jsonObj.get("serverCommit") != null && !jsonObj.get("serverCommit").isJsonNull()) && !jsonObj.get("serverCommit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverCommit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serverCommit").toString()));
      }
      if ((jsonObj.get("serverVersion") != null && !jsonObj.get("serverVersion").isJsonNull()) && !jsonObj.get("serverVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serverVersion").toString()));
      }
      // validate the optional field `signup`
      if (jsonObj.get("signup") != null && !jsonObj.get("signup").isJsonNull()) {
        ServerConfigSignup.validateJsonElement(jsonObj.get("signup"));
      }
      // validate the optional field `theme`
      if (jsonObj.get("theme") != null && !jsonObj.get("theme").isJsonNull()) {
        ServerConfigPlugin.validateJsonElement(jsonObj.get("theme"));
      }
      // validate the optional field `tracker`
      if (jsonObj.get("tracker") != null && !jsonObj.get("tracker").isJsonNull()) {
        ServerConfigAutoBlacklistVideosOfUsers.validateJsonElement(jsonObj.get("tracker"));
      }
      // validate the optional field `transcoding`
      if (jsonObj.get("transcoding") != null && !jsonObj.get("transcoding").isJsonNull()) {
        ServerConfigTranscoding.validateJsonElement(jsonObj.get("transcoding"));
      }
      // validate the optional field `trending`
      if (jsonObj.get("trending") != null && !jsonObj.get("trending").isJsonNull()) {
        ServerConfigTrending.validateJsonElement(jsonObj.get("trending"));
      }
      // validate the optional field `user`
      if (jsonObj.get("user") != null && !jsonObj.get("user").isJsonNull()) {
        ServerConfigUser.validateJsonElement(jsonObj.get("user"));
      }
      // validate the optional field `video`
      if (jsonObj.get("video") != null && !jsonObj.get("video").isJsonNull()) {
        ServerConfigVideo.validateJsonElement(jsonObj.get("video"));
      }
      // validate the optional field `videoCaption`
      if (jsonObj.get("videoCaption") != null && !jsonObj.get("videoCaption").isJsonNull()) {
        ServerConfigVideoCaption.validateJsonElement(jsonObj.get("videoCaption"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerConfig>() {
           @Override
           public void write(JsonWriter out, ServerConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerConfig
   * @throws IOException if the JSON string is invalid with respect to ServerConfig
   */
  public static ServerConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerConfig.class);
  }

  /**
   * Convert an instance of ServerConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

