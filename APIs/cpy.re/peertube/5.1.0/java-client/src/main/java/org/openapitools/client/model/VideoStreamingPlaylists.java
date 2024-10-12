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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.VideoFile;
import org.openapitools.client.model.VideoStreamingPlaylistsHLSRedundanciesInner;

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
 * VideoStreamingPlaylists
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideoStreamingPlaylists {
  public static final String SERIALIZED_NAME_FILES = "files";
  @SerializedName(SERIALIZED_NAME_FILES)
  private List<VideoFile> files = new ArrayList<>();

  public static final String SERIALIZED_NAME_PLAYLIST_URL = "playlistUrl";
  @SerializedName(SERIALIZED_NAME_PLAYLIST_URL)
  private String playlistUrl;

  public static final String SERIALIZED_NAME_REDUNDANCIES = "redundancies";
  @SerializedName(SERIALIZED_NAME_REDUNDANCIES)
  private List<VideoStreamingPlaylistsHLSRedundanciesInner> redundancies = new ArrayList<>();

  public static final String SERIALIZED_NAME_SEGMENTS_SHA256_URL = "segmentsSha256Url";
  @SerializedName(SERIALIZED_NAME_SEGMENTS_SHA256_URL)
  private String segmentsSha256Url;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  /**
   * Playlist type: - &#x60;1&#x60;: HLS 
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    NUMBER_1(1);

    private Integer value;

    TypeEnum(Integer value) {
      this.value = value;
    }

    public Integer getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(Integer value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        Integer value =  jsonReader.nextInt();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      Integer value = jsonElement.getAsInt();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public VideoStreamingPlaylists() {
  }

  public VideoStreamingPlaylists files(List<VideoFile> files) {
    this.files = files;
    return this;
  }

  public VideoStreamingPlaylists addFilesItem(VideoFile filesItem) {
    if (this.files == null) {
      this.files = new ArrayList<>();
    }
    this.files.add(filesItem);
    return this;
  }

  /**
   * Video files associated to this playlist.  The difference with the root &#x60;files&#x60; property is that these files are fragmented, so they can be used in this streaming playlist (HLS, etc.) 
   * @return files
   */
  @javax.annotation.Nullable
  public List<VideoFile> getFiles() {
    return files;
  }

  public void setFiles(List<VideoFile> files) {
    this.files = files;
  }


  public VideoStreamingPlaylists playlistUrl(String playlistUrl) {
    this.playlistUrl = playlistUrl;
    return this;
  }

  /**
   * Get playlistUrl
   * @return playlistUrl
   */
  @javax.annotation.Nullable
  public String getPlaylistUrl() {
    return playlistUrl;
  }

  public void setPlaylistUrl(String playlistUrl) {
    this.playlistUrl = playlistUrl;
  }


  public VideoStreamingPlaylists redundancies(List<VideoStreamingPlaylistsHLSRedundanciesInner> redundancies) {
    this.redundancies = redundancies;
    return this;
  }

  public VideoStreamingPlaylists addRedundanciesItem(VideoStreamingPlaylistsHLSRedundanciesInner redundanciesItem) {
    if (this.redundancies == null) {
      this.redundancies = new ArrayList<>();
    }
    this.redundancies.add(redundanciesItem);
    return this;
  }

  /**
   * Get redundancies
   * @return redundancies
   */
  @javax.annotation.Nullable
  public List<VideoStreamingPlaylistsHLSRedundanciesInner> getRedundancies() {
    return redundancies;
  }

  public void setRedundancies(List<VideoStreamingPlaylistsHLSRedundanciesInner> redundancies) {
    this.redundancies = redundancies;
  }


  public VideoStreamingPlaylists segmentsSha256Url(String segmentsSha256Url) {
    this.segmentsSha256Url = segmentsSha256Url;
    return this;
  }

  /**
   * Get segmentsSha256Url
   * @return segmentsSha256Url
   */
  @javax.annotation.Nullable
  public String getSegmentsSha256Url() {
    return segmentsSha256Url;
  }

  public void setSegmentsSha256Url(String segmentsSha256Url) {
    this.segmentsSha256Url = segmentsSha256Url;
  }


  public VideoStreamingPlaylists id(Integer id) {
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


  public VideoStreamingPlaylists type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Playlist type: - &#x60;1&#x60;: HLS 
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VideoStreamingPlaylists videoStreamingPlaylists = (VideoStreamingPlaylists) o;
    return Objects.equals(this.files, videoStreamingPlaylists.files) &&
        Objects.equals(this.playlistUrl, videoStreamingPlaylists.playlistUrl) &&
        Objects.equals(this.redundancies, videoStreamingPlaylists.redundancies) &&
        Objects.equals(this.segmentsSha256Url, videoStreamingPlaylists.segmentsSha256Url) &&
        Objects.equals(this.id, videoStreamingPlaylists.id) &&
        Objects.equals(this.type, videoStreamingPlaylists.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(files, playlistUrl, redundancies, segmentsSha256Url, id, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VideoStreamingPlaylists {\n");
    sb.append("    files: ").append(toIndentedString(files)).append("\n");
    sb.append("    playlistUrl: ").append(toIndentedString(playlistUrl)).append("\n");
    sb.append("    redundancies: ").append(toIndentedString(redundancies)).append("\n");
    sb.append("    segmentsSha256Url: ").append(toIndentedString(segmentsSha256Url)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("files");
    openapiFields.add("playlistUrl");
    openapiFields.add("redundancies");
    openapiFields.add("segmentsSha256Url");
    openapiFields.add("id");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VideoStreamingPlaylists
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VideoStreamingPlaylists.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VideoStreamingPlaylists is not found in the empty JSON string", VideoStreamingPlaylists.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VideoStreamingPlaylists.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VideoStreamingPlaylists` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("files") != null && !jsonObj.get("files").isJsonNull()) {
        JsonArray jsonArrayfiles = jsonObj.getAsJsonArray("files");
        if (jsonArrayfiles != null) {
          // ensure the json data is an array
          if (!jsonObj.get("files").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `files` to be an array in the JSON string but got `%s`", jsonObj.get("files").toString()));
          }

          // validate the optional field `files` (array)
          for (int i = 0; i < jsonArrayfiles.size(); i++) {
            VideoFile.validateJsonElement(jsonArrayfiles.get(i));
          };
        }
      }
      if ((jsonObj.get("playlistUrl") != null && !jsonObj.get("playlistUrl").isJsonNull()) && !jsonObj.get("playlistUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `playlistUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("playlistUrl").toString()));
      }
      if (jsonObj.get("redundancies") != null && !jsonObj.get("redundancies").isJsonNull()) {
        JsonArray jsonArrayredundancies = jsonObj.getAsJsonArray("redundancies");
        if (jsonArrayredundancies != null) {
          // ensure the json data is an array
          if (!jsonObj.get("redundancies").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `redundancies` to be an array in the JSON string but got `%s`", jsonObj.get("redundancies").toString()));
          }

          // validate the optional field `redundancies` (array)
          for (int i = 0; i < jsonArrayredundancies.size(); i++) {
            VideoStreamingPlaylistsHLSRedundanciesInner.validateJsonElement(jsonArrayredundancies.get(i));
          };
        }
      }
      if ((jsonObj.get("segmentsSha256Url") != null && !jsonObj.get("segmentsSha256Url").isJsonNull()) && !jsonObj.get("segmentsSha256Url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `segmentsSha256Url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("segmentsSha256Url").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VideoStreamingPlaylists.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VideoStreamingPlaylists' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VideoStreamingPlaylists> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VideoStreamingPlaylists.class));

       return (TypeAdapter<T>) new TypeAdapter<VideoStreamingPlaylists>() {
           @Override
           public void write(JsonWriter out, VideoStreamingPlaylists value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VideoStreamingPlaylists read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VideoStreamingPlaylists given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VideoStreamingPlaylists
   * @throws IOException if the JSON string is invalid with respect to VideoStreamingPlaylists
   */
  public static VideoStreamingPlaylists fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VideoStreamingPlaylists.class);
  }

  /**
   * Convert an instance of VideoStreamingPlaylists to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

