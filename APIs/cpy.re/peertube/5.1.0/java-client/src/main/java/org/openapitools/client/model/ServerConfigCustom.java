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
import org.openapitools.client.model.ServerConfigCustomAdmin;
import org.openapitools.client.model.ServerConfigCustomCache;
import org.openapitools.client.model.ServerConfigCustomFollowers;
import org.openapitools.client.model.ServerConfigCustomImport;
import org.openapitools.client.model.ServerConfigCustomInstance;
import org.openapitools.client.model.ServerConfigCustomServices;
import org.openapitools.client.model.ServerConfigCustomSignup;
import org.openapitools.client.model.ServerConfigCustomTheme;
import org.openapitools.client.model.ServerConfigCustomTranscoding;
import org.openapitools.client.model.ServerConfigCustomUser;

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
 * ServerConfigCustom
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerConfigCustom {
  public static final String SERIALIZED_NAME_ADMIN = "admin";
  @SerializedName(SERIALIZED_NAME_ADMIN)
  private ServerConfigCustomAdmin admin;

  public static final String SERIALIZED_NAME_AUTO_BLACKLIST = "autoBlacklist";
  @SerializedName(SERIALIZED_NAME_AUTO_BLACKLIST)
  private ServerConfigAutoBlacklist autoBlacklist;

  public static final String SERIALIZED_NAME_CACHE = "cache";
  @SerializedName(SERIALIZED_NAME_CACHE)
  private ServerConfigCustomCache cache;

  public static final String SERIALIZED_NAME_CONTACT_FORM = "contactForm";
  @SerializedName(SERIALIZED_NAME_CONTACT_FORM)
  private ServerConfigAutoBlacklistVideosOfUsers contactForm;

  public static final String SERIALIZED_NAME_FOLLOWERS = "followers";
  @SerializedName(SERIALIZED_NAME_FOLLOWERS)
  private ServerConfigCustomFollowers followers;

  public static final String SERIALIZED_NAME_IMPORT = "import";
  @SerializedName(SERIALIZED_NAME_IMPORT)
  private ServerConfigCustomImport _import;

  public static final String SERIALIZED_NAME_INSTANCE = "instance";
  @SerializedName(SERIALIZED_NAME_INSTANCE)
  private ServerConfigCustomInstance instance;

  public static final String SERIALIZED_NAME_SERVICES = "services";
  @SerializedName(SERIALIZED_NAME_SERVICES)
  private ServerConfigCustomServices services;

  public static final String SERIALIZED_NAME_SIGNUP = "signup";
  @SerializedName(SERIALIZED_NAME_SIGNUP)
  private ServerConfigCustomSignup signup;

  public static final String SERIALIZED_NAME_THEME = "theme";
  @SerializedName(SERIALIZED_NAME_THEME)
  private ServerConfigCustomTheme theme;

  public static final String SERIALIZED_NAME_TRANSCODING = "transcoding";
  @SerializedName(SERIALIZED_NAME_TRANSCODING)
  private ServerConfigCustomTranscoding transcoding;

  public static final String SERIALIZED_NAME_USER = "user";
  @SerializedName(SERIALIZED_NAME_USER)
  private ServerConfigCustomUser user;

  public ServerConfigCustom() {
  }

  public ServerConfigCustom admin(ServerConfigCustomAdmin admin) {
    this.admin = admin;
    return this;
  }

  /**
   * Get admin
   * @return admin
   */
  @javax.annotation.Nullable
  public ServerConfigCustomAdmin getAdmin() {
    return admin;
  }

  public void setAdmin(ServerConfigCustomAdmin admin) {
    this.admin = admin;
  }


  public ServerConfigCustom autoBlacklist(ServerConfigAutoBlacklist autoBlacklist) {
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


  public ServerConfigCustom cache(ServerConfigCustomCache cache) {
    this.cache = cache;
    return this;
  }

  /**
   * Get cache
   * @return cache
   */
  @javax.annotation.Nullable
  public ServerConfigCustomCache getCache() {
    return cache;
  }

  public void setCache(ServerConfigCustomCache cache) {
    this.cache = cache;
  }


  public ServerConfigCustom contactForm(ServerConfigAutoBlacklistVideosOfUsers contactForm) {
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


  public ServerConfigCustom followers(ServerConfigCustomFollowers followers) {
    this.followers = followers;
    return this;
  }

  /**
   * Get followers
   * @return followers
   */
  @javax.annotation.Nullable
  public ServerConfigCustomFollowers getFollowers() {
    return followers;
  }

  public void setFollowers(ServerConfigCustomFollowers followers) {
    this.followers = followers;
  }


  public ServerConfigCustom _import(ServerConfigCustomImport _import) {
    this._import = _import;
    return this;
  }

  /**
   * Get _import
   * @return _import
   */
  @javax.annotation.Nullable
  public ServerConfigCustomImport getImport() {
    return _import;
  }

  public void setImport(ServerConfigCustomImport _import) {
    this._import = _import;
  }


  public ServerConfigCustom instance(ServerConfigCustomInstance instance) {
    this.instance = instance;
    return this;
  }

  /**
   * Get instance
   * @return instance
   */
  @javax.annotation.Nullable
  public ServerConfigCustomInstance getInstance() {
    return instance;
  }

  public void setInstance(ServerConfigCustomInstance instance) {
    this.instance = instance;
  }


  public ServerConfigCustom services(ServerConfigCustomServices services) {
    this.services = services;
    return this;
  }

  /**
   * Get services
   * @return services
   */
  @javax.annotation.Nullable
  public ServerConfigCustomServices getServices() {
    return services;
  }

  public void setServices(ServerConfigCustomServices services) {
    this.services = services;
  }


  public ServerConfigCustom signup(ServerConfigCustomSignup signup) {
    this.signup = signup;
    return this;
  }

  /**
   * Get signup
   * @return signup
   */
  @javax.annotation.Nullable
  public ServerConfigCustomSignup getSignup() {
    return signup;
  }

  public void setSignup(ServerConfigCustomSignup signup) {
    this.signup = signup;
  }


  public ServerConfigCustom theme(ServerConfigCustomTheme theme) {
    this.theme = theme;
    return this;
  }

  /**
   * Get theme
   * @return theme
   */
  @javax.annotation.Nullable
  public ServerConfigCustomTheme getTheme() {
    return theme;
  }

  public void setTheme(ServerConfigCustomTheme theme) {
    this.theme = theme;
  }


  public ServerConfigCustom transcoding(ServerConfigCustomTranscoding transcoding) {
    this.transcoding = transcoding;
    return this;
  }

  /**
   * Get transcoding
   * @return transcoding
   */
  @javax.annotation.Nullable
  public ServerConfigCustomTranscoding getTranscoding() {
    return transcoding;
  }

  public void setTranscoding(ServerConfigCustomTranscoding transcoding) {
    this.transcoding = transcoding;
  }


  public ServerConfigCustom user(ServerConfigCustomUser user) {
    this.user = user;
    return this;
  }

  /**
   * Get user
   * @return user
   */
  @javax.annotation.Nullable
  public ServerConfigCustomUser getUser() {
    return user;
  }

  public void setUser(ServerConfigCustomUser user) {
    this.user = user;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerConfigCustom serverConfigCustom = (ServerConfigCustom) o;
    return Objects.equals(this.admin, serverConfigCustom.admin) &&
        Objects.equals(this.autoBlacklist, serverConfigCustom.autoBlacklist) &&
        Objects.equals(this.cache, serverConfigCustom.cache) &&
        Objects.equals(this.contactForm, serverConfigCustom.contactForm) &&
        Objects.equals(this.followers, serverConfigCustom.followers) &&
        Objects.equals(this._import, serverConfigCustom._import) &&
        Objects.equals(this.instance, serverConfigCustom.instance) &&
        Objects.equals(this.services, serverConfigCustom.services) &&
        Objects.equals(this.signup, serverConfigCustom.signup) &&
        Objects.equals(this.theme, serverConfigCustom.theme) &&
        Objects.equals(this.transcoding, serverConfigCustom.transcoding) &&
        Objects.equals(this.user, serverConfigCustom.user);
  }

  @Override
  public int hashCode() {
    return Objects.hash(admin, autoBlacklist, cache, contactForm, followers, _import, instance, services, signup, theme, transcoding, user);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerConfigCustom {\n");
    sb.append("    admin: ").append(toIndentedString(admin)).append("\n");
    sb.append("    autoBlacklist: ").append(toIndentedString(autoBlacklist)).append("\n");
    sb.append("    cache: ").append(toIndentedString(cache)).append("\n");
    sb.append("    contactForm: ").append(toIndentedString(contactForm)).append("\n");
    sb.append("    followers: ").append(toIndentedString(followers)).append("\n");
    sb.append("    _import: ").append(toIndentedString(_import)).append("\n");
    sb.append("    instance: ").append(toIndentedString(instance)).append("\n");
    sb.append("    services: ").append(toIndentedString(services)).append("\n");
    sb.append("    signup: ").append(toIndentedString(signup)).append("\n");
    sb.append("    theme: ").append(toIndentedString(theme)).append("\n");
    sb.append("    transcoding: ").append(toIndentedString(transcoding)).append("\n");
    sb.append("    user: ").append(toIndentedString(user)).append("\n");
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
    openapiFields.add("admin");
    openapiFields.add("autoBlacklist");
    openapiFields.add("cache");
    openapiFields.add("contactForm");
    openapiFields.add("followers");
    openapiFields.add("import");
    openapiFields.add("instance");
    openapiFields.add("services");
    openapiFields.add("signup");
    openapiFields.add("theme");
    openapiFields.add("transcoding");
    openapiFields.add("user");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerConfigCustom
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerConfigCustom.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerConfigCustom is not found in the empty JSON string", ServerConfigCustom.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerConfigCustom.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerConfigCustom` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `admin`
      if (jsonObj.get("admin") != null && !jsonObj.get("admin").isJsonNull()) {
        ServerConfigCustomAdmin.validateJsonElement(jsonObj.get("admin"));
      }
      // validate the optional field `autoBlacklist`
      if (jsonObj.get("autoBlacklist") != null && !jsonObj.get("autoBlacklist").isJsonNull()) {
        ServerConfigAutoBlacklist.validateJsonElement(jsonObj.get("autoBlacklist"));
      }
      // validate the optional field `cache`
      if (jsonObj.get("cache") != null && !jsonObj.get("cache").isJsonNull()) {
        ServerConfigCustomCache.validateJsonElement(jsonObj.get("cache"));
      }
      // validate the optional field `contactForm`
      if (jsonObj.get("contactForm") != null && !jsonObj.get("contactForm").isJsonNull()) {
        ServerConfigAutoBlacklistVideosOfUsers.validateJsonElement(jsonObj.get("contactForm"));
      }
      // validate the optional field `followers`
      if (jsonObj.get("followers") != null && !jsonObj.get("followers").isJsonNull()) {
        ServerConfigCustomFollowers.validateJsonElement(jsonObj.get("followers"));
      }
      // validate the optional field `import`
      if (jsonObj.get("import") != null && !jsonObj.get("import").isJsonNull()) {
        ServerConfigCustomImport.validateJsonElement(jsonObj.get("import"));
      }
      // validate the optional field `instance`
      if (jsonObj.get("instance") != null && !jsonObj.get("instance").isJsonNull()) {
        ServerConfigCustomInstance.validateJsonElement(jsonObj.get("instance"));
      }
      // validate the optional field `services`
      if (jsonObj.get("services") != null && !jsonObj.get("services").isJsonNull()) {
        ServerConfigCustomServices.validateJsonElement(jsonObj.get("services"));
      }
      // validate the optional field `signup`
      if (jsonObj.get("signup") != null && !jsonObj.get("signup").isJsonNull()) {
        ServerConfigCustomSignup.validateJsonElement(jsonObj.get("signup"));
      }
      // validate the optional field `theme`
      if (jsonObj.get("theme") != null && !jsonObj.get("theme").isJsonNull()) {
        ServerConfigCustomTheme.validateJsonElement(jsonObj.get("theme"));
      }
      // validate the optional field `transcoding`
      if (jsonObj.get("transcoding") != null && !jsonObj.get("transcoding").isJsonNull()) {
        ServerConfigCustomTranscoding.validateJsonElement(jsonObj.get("transcoding"));
      }
      // validate the optional field `user`
      if (jsonObj.get("user") != null && !jsonObj.get("user").isJsonNull()) {
        ServerConfigCustomUser.validateJsonElement(jsonObj.get("user"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerConfigCustom.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerConfigCustom' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerConfigCustom> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerConfigCustom.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerConfigCustom>() {
           @Override
           public void write(JsonWriter out, ServerConfigCustom value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerConfigCustom read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerConfigCustom given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerConfigCustom
   * @throws IOException if the JSON string is invalid with respect to ServerConfigCustom
   */
  public static ServerConfigCustom fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerConfigCustom.class);
  }

  /**
   * Convert an instance of ServerConfigCustom to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

