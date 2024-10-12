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
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.Video;
import org.openapitools.client.model.VideoImportStateConstant;
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
 * VideoImport
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideoImport {
  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private String error;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_MAGNET_URI = "magnetUri";
  @SerializedName(SERIALIZED_NAME_MAGNET_URI)
  private URI magnetUri;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private VideoImportStateConstant state;

  public static final String SERIALIZED_NAME_TARGET_URL = "targetUrl";
  @SerializedName(SERIALIZED_NAME_TARGET_URL)
  private String targetUrl;

  public static final String SERIALIZED_NAME_TORRENT_NAME = "torrentName";
  @SerializedName(SERIALIZED_NAME_TORRENT_NAME)
  private String torrentName;

  public static final String SERIALIZED_NAME_TORRENTFILE = "torrentfile";
  @SerializedName(SERIALIZED_NAME_TORRENTFILE)
  private File torrentfile;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_VIDEO = "video";
  @SerializedName(SERIALIZED_NAME_VIDEO)
  private Video video;

  public VideoImport() {
  }

  public VideoImport(
     OffsetDateTime createdAt, 
     String error, 
     Integer id, 
     VideoImportStateConstant state, 
     String torrentName, 
     OffsetDateTime updatedAt, 
     Video video
  ) {
    this();
    this.createdAt = createdAt;
    this.error = error;
    this.id = id;
    this.state = state;
    this.torrentName = torrentName;
    this.updatedAt = updatedAt;
    this.video = video;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



  /**
   * Get error
   * @return error
   */
  @javax.annotation.Nullable
  public String getError() {
    return error;
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



  public VideoImport magnetUri(URI magnetUri) {
    this.magnetUri = magnetUri;
    return this;
  }

  /**
   * magnet URI allowing to resolve the import&#39;s source video
   * @return magnetUri
   */
  @javax.annotation.Nullable
  public URI getMagnetUri() {
    return magnetUri;
  }

  public void setMagnetUri(URI magnetUri) {
    this.magnetUri = magnetUri;
  }


  /**
   * Get state
   * @return state
   */
  @javax.annotation.Nullable
  public VideoImportStateConstant getState() {
    return state;
  }



  public VideoImport targetUrl(String targetUrl) {
    this.targetUrl = targetUrl;
    return this;
  }

  /**
   * remote URL where to find the import&#39;s source video
   * @return targetUrl
   */
  @javax.annotation.Nullable
  public String getTargetUrl() {
    return targetUrl;
  }

  public void setTargetUrl(String targetUrl) {
    this.targetUrl = targetUrl;
  }


  /**
   * Get torrentName
   * @return torrentName
   */
  @javax.annotation.Nullable
  public String getTorrentName() {
    return torrentName;
  }



  public VideoImport torrentfile(File torrentfile) {
    this.torrentfile = torrentfile;
    return this;
  }

  /**
   * Torrent file containing only the video file
   * @return torrentfile
   */
  @javax.annotation.Nullable
  public File getTorrentfile() {
    return torrentfile;
  }

  public void setTorrentfile(File torrentfile) {
    this.torrentfile = torrentfile;
  }


  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }



  /**
   * Get video
   * @return video
   */
  @javax.annotation.Nullable
  public Video getVideo() {
    return video;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VideoImport videoImport = (VideoImport) o;
    return Objects.equals(this.createdAt, videoImport.createdAt) &&
        Objects.equals(this.error, videoImport.error) &&
        Objects.equals(this.id, videoImport.id) &&
        Objects.equals(this.magnetUri, videoImport.magnetUri) &&
        Objects.equals(this.state, videoImport.state) &&
        Objects.equals(this.targetUrl, videoImport.targetUrl) &&
        Objects.equals(this.torrentName, videoImport.torrentName) &&
        Objects.equals(this.torrentfile, videoImport.torrentfile) &&
        Objects.equals(this.updatedAt, videoImport.updatedAt) &&
        Objects.equals(this.video, videoImport.video);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, error, id, magnetUri, state, targetUrl, torrentName, torrentfile, updatedAt, video);
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
    sb.append("class VideoImport {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    magnetUri: ").append(toIndentedString(magnetUri)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    targetUrl: ").append(toIndentedString(targetUrl)).append("\n");
    sb.append("    torrentName: ").append(toIndentedString(torrentName)).append("\n");
    sb.append("    torrentfile: ").append(toIndentedString(torrentfile)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    video: ").append(toIndentedString(video)).append("\n");
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
    openapiFields.add("createdAt");
    openapiFields.add("error");
    openapiFields.add("id");
    openapiFields.add("magnetUri");
    openapiFields.add("state");
    openapiFields.add("targetUrl");
    openapiFields.add("torrentName");
    openapiFields.add("torrentfile");
    openapiFields.add("updatedAt");
    openapiFields.add("video");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VideoImport
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VideoImport.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VideoImport is not found in the empty JSON string", VideoImport.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VideoImport.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VideoImport` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("error") != null && !jsonObj.get("error").isJsonNull()) && !jsonObj.get("error").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `error` to be a primitive type in the JSON string but got `%s`", jsonObj.get("error").toString()));
      }
      if ((jsonObj.get("magnetUri") != null && !jsonObj.get("magnetUri").isJsonNull()) && !jsonObj.get("magnetUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `magnetUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("magnetUri").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        VideoImportStateConstant.validateJsonElement(jsonObj.get("state"));
      }
      if ((jsonObj.get("targetUrl") != null && !jsonObj.get("targetUrl").isJsonNull()) && !jsonObj.get("targetUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("targetUrl").toString()));
      }
      if ((jsonObj.get("torrentName") != null && !jsonObj.get("torrentName").isJsonNull()) && !jsonObj.get("torrentName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `torrentName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("torrentName").toString()));
      }
      // validate the optional field `video`
      if (jsonObj.get("video") != null && !jsonObj.get("video").isJsonNull()) {
        Video.validateJsonElement(jsonObj.get("video"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VideoImport.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VideoImport' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VideoImport> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VideoImport.class));

       return (TypeAdapter<T>) new TypeAdapter<VideoImport>() {
           @Override
           public void write(JsonWriter out, VideoImport value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VideoImport read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VideoImport given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VideoImport
   * @throws IOException if the JSON string is invalid with respect to VideoImport
   */
  public static VideoImport fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VideoImport.class);
  }

  /**
   * Convert an instance of VideoImport to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

