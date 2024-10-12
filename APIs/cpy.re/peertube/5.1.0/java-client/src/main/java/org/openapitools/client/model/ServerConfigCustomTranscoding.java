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
import java.util.Arrays;
import org.openapitools.client.model.ServerConfigCustomTranscodingHls;
import org.openapitools.client.model.ServerConfigCustomTranscodingResolutions;
import org.openapitools.client.model.ServerConfigCustomTranscodingWebtorrent;

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
 * Settings pertaining to transcoding jobs
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerConfigCustomTranscoding {
  public static final String SERIALIZED_NAME_ALLOW_ADDITIONAL_EXTENSIONS = "allowAdditionalExtensions";
  @SerializedName(SERIALIZED_NAME_ALLOW_ADDITIONAL_EXTENSIONS)
  private Boolean allowAdditionalExtensions;

  public static final String SERIALIZED_NAME_ALLOW_AUDIO_FILES = "allowAudioFiles";
  @SerializedName(SERIALIZED_NAME_ALLOW_AUDIO_FILES)
  private Boolean allowAudioFiles;

  public static final String SERIALIZED_NAME_CONCURRENCY = "concurrency";
  @SerializedName(SERIALIZED_NAME_CONCURRENCY)
  private BigDecimal concurrency;

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_HLS = "hls";
  @SerializedName(SERIALIZED_NAME_HLS)
  private ServerConfigCustomTranscodingHls hls;

  /**
   * New profiles can be added by plugins ; available in core PeerTube: &#39;default&#39;. 
   */
  @JsonAdapter(ProfileEnum.Adapter.class)
  public enum ProfileEnum {
    DEFAULT("default");

    private String value;

    ProfileEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProfileEnum fromValue(String value) {
      for (ProfileEnum b : ProfileEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProfileEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProfileEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProfileEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProfileEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProfileEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROFILE = "profile";
  @SerializedName(SERIALIZED_NAME_PROFILE)
  private ProfileEnum profile;

  public static final String SERIALIZED_NAME_RESOLUTIONS = "resolutions";
  @SerializedName(SERIALIZED_NAME_RESOLUTIONS)
  private ServerConfigCustomTranscodingResolutions resolutions;

  public static final String SERIALIZED_NAME_THREADS = "threads";
  @SerializedName(SERIALIZED_NAME_THREADS)
  private Integer threads;

  public static final String SERIALIZED_NAME_WEBTORRENT = "webtorrent";
  @SerializedName(SERIALIZED_NAME_WEBTORRENT)
  private ServerConfigCustomTranscodingWebtorrent webtorrent;

  public ServerConfigCustomTranscoding() {
  }

  public ServerConfigCustomTranscoding allowAdditionalExtensions(Boolean allowAdditionalExtensions) {
    this.allowAdditionalExtensions = allowAdditionalExtensions;
    return this;
  }

  /**
   * Allow your users to upload .mkv, .mov, .avi, .wmv, .flv, .f4v, .3g2, .3gp, .mts, m2ts, .mxf, .nut videos
   * @return allowAdditionalExtensions
   */
  @javax.annotation.Nullable
  public Boolean getAllowAdditionalExtensions() {
    return allowAdditionalExtensions;
  }

  public void setAllowAdditionalExtensions(Boolean allowAdditionalExtensions) {
    this.allowAdditionalExtensions = allowAdditionalExtensions;
  }


  public ServerConfigCustomTranscoding allowAudioFiles(Boolean allowAudioFiles) {
    this.allowAudioFiles = allowAudioFiles;
    return this;
  }

  /**
   * If a user uploads an audio file, PeerTube will create a video by merging the preview file and the audio file
   * @return allowAudioFiles
   */
  @javax.annotation.Nullable
  public Boolean getAllowAudioFiles() {
    return allowAudioFiles;
  }

  public void setAllowAudioFiles(Boolean allowAudioFiles) {
    this.allowAudioFiles = allowAudioFiles;
  }


  public ServerConfigCustomTranscoding concurrency(BigDecimal concurrency) {
    this.concurrency = concurrency;
    return this;
  }

  /**
   * Amount of transcoding jobs to execute in parallel
   * @return concurrency
   */
  @javax.annotation.Nullable
  public BigDecimal getConcurrency() {
    return concurrency;
  }

  public void setConcurrency(BigDecimal concurrency) {
    this.concurrency = concurrency;
  }


  public ServerConfigCustomTranscoding enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Get enabled
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public ServerConfigCustomTranscoding hls(ServerConfigCustomTranscodingHls hls) {
    this.hls = hls;
    return this;
  }

  /**
   * Get hls
   * @return hls
   */
  @javax.annotation.Nullable
  public ServerConfigCustomTranscodingHls getHls() {
    return hls;
  }

  public void setHls(ServerConfigCustomTranscodingHls hls) {
    this.hls = hls;
  }


  public ServerConfigCustomTranscoding profile(ProfileEnum profile) {
    this.profile = profile;
    return this;
  }

  /**
   * New profiles can be added by plugins ; available in core PeerTube: &#39;default&#39;. 
   * @return profile
   */
  @javax.annotation.Nullable
  public ProfileEnum getProfile() {
    return profile;
  }

  public void setProfile(ProfileEnum profile) {
    this.profile = profile;
  }


  public ServerConfigCustomTranscoding resolutions(ServerConfigCustomTranscodingResolutions resolutions) {
    this.resolutions = resolutions;
    return this;
  }

  /**
   * Get resolutions
   * @return resolutions
   */
  @javax.annotation.Nullable
  public ServerConfigCustomTranscodingResolutions getResolutions() {
    return resolutions;
  }

  public void setResolutions(ServerConfigCustomTranscodingResolutions resolutions) {
    this.resolutions = resolutions;
  }


  public ServerConfigCustomTranscoding threads(Integer threads) {
    this.threads = threads;
    return this;
  }

  /**
   * Amount of threads used by ffmpeg for 1 transcoding job
   * @return threads
   */
  @javax.annotation.Nullable
  public Integer getThreads() {
    return threads;
  }

  public void setThreads(Integer threads) {
    this.threads = threads;
  }


  public ServerConfigCustomTranscoding webtorrent(ServerConfigCustomTranscodingWebtorrent webtorrent) {
    this.webtorrent = webtorrent;
    return this;
  }

  /**
   * Get webtorrent
   * @return webtorrent
   */
  @javax.annotation.Nullable
  public ServerConfigCustomTranscodingWebtorrent getWebtorrent() {
    return webtorrent;
  }

  public void setWebtorrent(ServerConfigCustomTranscodingWebtorrent webtorrent) {
    this.webtorrent = webtorrent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerConfigCustomTranscoding serverConfigCustomTranscoding = (ServerConfigCustomTranscoding) o;
    return Objects.equals(this.allowAdditionalExtensions, serverConfigCustomTranscoding.allowAdditionalExtensions) &&
        Objects.equals(this.allowAudioFiles, serverConfigCustomTranscoding.allowAudioFiles) &&
        Objects.equals(this.concurrency, serverConfigCustomTranscoding.concurrency) &&
        Objects.equals(this.enabled, serverConfigCustomTranscoding.enabled) &&
        Objects.equals(this.hls, serverConfigCustomTranscoding.hls) &&
        Objects.equals(this.profile, serverConfigCustomTranscoding.profile) &&
        Objects.equals(this.resolutions, serverConfigCustomTranscoding.resolutions) &&
        Objects.equals(this.threads, serverConfigCustomTranscoding.threads) &&
        Objects.equals(this.webtorrent, serverConfigCustomTranscoding.webtorrent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowAdditionalExtensions, allowAudioFiles, concurrency, enabled, hls, profile, resolutions, threads, webtorrent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerConfigCustomTranscoding {\n");
    sb.append("    allowAdditionalExtensions: ").append(toIndentedString(allowAdditionalExtensions)).append("\n");
    sb.append("    allowAudioFiles: ").append(toIndentedString(allowAudioFiles)).append("\n");
    sb.append("    concurrency: ").append(toIndentedString(concurrency)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    hls: ").append(toIndentedString(hls)).append("\n");
    sb.append("    profile: ").append(toIndentedString(profile)).append("\n");
    sb.append("    resolutions: ").append(toIndentedString(resolutions)).append("\n");
    sb.append("    threads: ").append(toIndentedString(threads)).append("\n");
    sb.append("    webtorrent: ").append(toIndentedString(webtorrent)).append("\n");
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
    openapiFields.add("allowAdditionalExtensions");
    openapiFields.add("allowAudioFiles");
    openapiFields.add("concurrency");
    openapiFields.add("enabled");
    openapiFields.add("hls");
    openapiFields.add("profile");
    openapiFields.add("resolutions");
    openapiFields.add("threads");
    openapiFields.add("webtorrent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerConfigCustomTranscoding
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerConfigCustomTranscoding.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerConfigCustomTranscoding is not found in the empty JSON string", ServerConfigCustomTranscoding.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerConfigCustomTranscoding.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerConfigCustomTranscoding` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `hls`
      if (jsonObj.get("hls") != null && !jsonObj.get("hls").isJsonNull()) {
        ServerConfigCustomTranscodingHls.validateJsonElement(jsonObj.get("hls"));
      }
      if ((jsonObj.get("profile") != null && !jsonObj.get("profile").isJsonNull()) && !jsonObj.get("profile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profile").toString()));
      }
      // validate the optional field `profile`
      if (jsonObj.get("profile") != null && !jsonObj.get("profile").isJsonNull()) {
        ProfileEnum.validateJsonElement(jsonObj.get("profile"));
      }
      // validate the optional field `resolutions`
      if (jsonObj.get("resolutions") != null && !jsonObj.get("resolutions").isJsonNull()) {
        ServerConfigCustomTranscodingResolutions.validateJsonElement(jsonObj.get("resolutions"));
      }
      // validate the optional field `webtorrent`
      if (jsonObj.get("webtorrent") != null && !jsonObj.get("webtorrent").isJsonNull()) {
        ServerConfigCustomTranscodingWebtorrent.validateJsonElement(jsonObj.get("webtorrent"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerConfigCustomTranscoding.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerConfigCustomTranscoding' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerConfigCustomTranscoding> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerConfigCustomTranscoding.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerConfigCustomTranscoding>() {
           @Override
           public void write(JsonWriter out, ServerConfigCustomTranscoding value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerConfigCustomTranscoding read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerConfigCustomTranscoding given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerConfigCustomTranscoding
   * @throws IOException if the JSON string is invalid with respect to ServerConfigCustomTranscoding
   */
  public static ServerConfigCustomTranscoding fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerConfigCustomTranscoding.class);
  }

  /**
   * Convert an instance of ServerConfigCustomTranscoding to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

