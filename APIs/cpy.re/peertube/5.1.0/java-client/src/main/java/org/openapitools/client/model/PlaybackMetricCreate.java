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
import org.openapitools.client.model.GetLiveIdIdParameter;

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
 * PlaybackMetricCreate
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaybackMetricCreate {
  public static final String SERIALIZED_NAME_DOWNLOADED_BYTES_H_T_T_P = "downloadedBytesHTTP";
  @SerializedName(SERIALIZED_NAME_DOWNLOADED_BYTES_H_T_T_P)
  private BigDecimal downloadedBytesHTTP;

  public static final String SERIALIZED_NAME_DOWNLOADED_BYTES_P2_P = "downloadedBytesP2P";
  @SerializedName(SERIALIZED_NAME_DOWNLOADED_BYTES_P2_P)
  private BigDecimal downloadedBytesP2P;

  public static final String SERIALIZED_NAME_ERRORS = "errors";
  @SerializedName(SERIALIZED_NAME_ERRORS)
  private BigDecimal errors;

  public static final String SERIALIZED_NAME_FPS = "fps";
  @SerializedName(SERIALIZED_NAME_FPS)
  private BigDecimal fps;

  /**
   * Gets or Sets playerMode
   */
  @JsonAdapter(PlayerModeEnum.Adapter.class)
  public enum PlayerModeEnum {
    P2P_MEDIA_LOADER("p2p-media-loader"),
    
    WEBTORRENT("webtorrent");

    private String value;

    PlayerModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PlayerModeEnum fromValue(String value) {
      for (PlayerModeEnum b : PlayerModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PlayerModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PlayerModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PlayerModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PlayerModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PlayerModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PLAYER_MODE = "playerMode";
  @SerializedName(SERIALIZED_NAME_PLAYER_MODE)
  private PlayerModeEnum playerMode;

  public static final String SERIALIZED_NAME_RESOLUTION = "resolution";
  @SerializedName(SERIALIZED_NAME_RESOLUTION)
  private BigDecimal resolution;

  public static final String SERIALIZED_NAME_RESOLUTION_CHANGES = "resolutionChanges";
  @SerializedName(SERIALIZED_NAME_RESOLUTION_CHANGES)
  private BigDecimal resolutionChanges;

  public static final String SERIALIZED_NAME_UPLOADED_BYTES_P2_P = "uploadedBytesP2P";
  @SerializedName(SERIALIZED_NAME_UPLOADED_BYTES_P2_P)
  private BigDecimal uploadedBytesP2P;

  public static final String SERIALIZED_NAME_VIDEO_ID = "videoId";
  @SerializedName(SERIALIZED_NAME_VIDEO_ID)
  private GetLiveIdIdParameter videoId;

  public PlaybackMetricCreate() {
  }

  public PlaybackMetricCreate downloadedBytesHTTP(BigDecimal downloadedBytesHTTP) {
    this.downloadedBytesHTTP = downloadedBytesHTTP;
    return this;
  }

  /**
   * How many bytes were downloaded with HTTP since the last metric creation
   * @return downloadedBytesHTTP
   */
  @javax.annotation.Nonnull
  public BigDecimal getDownloadedBytesHTTP() {
    return downloadedBytesHTTP;
  }

  public void setDownloadedBytesHTTP(BigDecimal downloadedBytesHTTP) {
    this.downloadedBytesHTTP = downloadedBytesHTTP;
  }


  public PlaybackMetricCreate downloadedBytesP2P(BigDecimal downloadedBytesP2P) {
    this.downloadedBytesP2P = downloadedBytesP2P;
    return this;
  }

  /**
   * How many bytes were downloaded with P2P since the last metric creation
   * @return downloadedBytesP2P
   */
  @javax.annotation.Nonnull
  public BigDecimal getDownloadedBytesP2P() {
    return downloadedBytesP2P;
  }

  public void setDownloadedBytesP2P(BigDecimal downloadedBytesP2P) {
    this.downloadedBytesP2P = downloadedBytesP2P;
  }


  public PlaybackMetricCreate errors(BigDecimal errors) {
    this.errors = errors;
    return this;
  }

  /**
   * How many errors occured since the last metric creation
   * @return errors
   */
  @javax.annotation.Nonnull
  public BigDecimal getErrors() {
    return errors;
  }

  public void setErrors(BigDecimal errors) {
    this.errors = errors;
  }


  public PlaybackMetricCreate fps(BigDecimal fps) {
    this.fps = fps;
    return this;
  }

  /**
   * Current player video fps
   * @return fps
   */
  @javax.annotation.Nullable
  public BigDecimal getFps() {
    return fps;
  }

  public void setFps(BigDecimal fps) {
    this.fps = fps;
  }


  public PlaybackMetricCreate playerMode(PlayerModeEnum playerMode) {
    this.playerMode = playerMode;
    return this;
  }

  /**
   * Get playerMode
   * @return playerMode
   */
  @javax.annotation.Nonnull
  public PlayerModeEnum getPlayerMode() {
    return playerMode;
  }

  public void setPlayerMode(PlayerModeEnum playerMode) {
    this.playerMode = playerMode;
  }


  public PlaybackMetricCreate resolution(BigDecimal resolution) {
    this.resolution = resolution;
    return this;
  }

  /**
   * Current player video resolution
   * @return resolution
   */
  @javax.annotation.Nullable
  public BigDecimal getResolution() {
    return resolution;
  }

  public void setResolution(BigDecimal resolution) {
    this.resolution = resolution;
  }


  public PlaybackMetricCreate resolutionChanges(BigDecimal resolutionChanges) {
    this.resolutionChanges = resolutionChanges;
    return this;
  }

  /**
   * How many resolution changes occured since the last metric creation
   * @return resolutionChanges
   */
  @javax.annotation.Nonnull
  public BigDecimal getResolutionChanges() {
    return resolutionChanges;
  }

  public void setResolutionChanges(BigDecimal resolutionChanges) {
    this.resolutionChanges = resolutionChanges;
  }


  public PlaybackMetricCreate uploadedBytesP2P(BigDecimal uploadedBytesP2P) {
    this.uploadedBytesP2P = uploadedBytesP2P;
    return this;
  }

  /**
   * How many bytes were uploaded with P2P since the last metric creation
   * @return uploadedBytesP2P
   */
  @javax.annotation.Nonnull
  public BigDecimal getUploadedBytesP2P() {
    return uploadedBytesP2P;
  }

  public void setUploadedBytesP2P(BigDecimal uploadedBytesP2P) {
    this.uploadedBytesP2P = uploadedBytesP2P;
  }


  public PlaybackMetricCreate videoId(GetLiveIdIdParameter videoId) {
    this.videoId = videoId;
    return this;
  }

  /**
   * Get videoId
   * @return videoId
   */
  @javax.annotation.Nonnull
  public GetLiveIdIdParameter getVideoId() {
    return videoId;
  }

  public void setVideoId(GetLiveIdIdParameter videoId) {
    this.videoId = videoId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaybackMetricCreate playbackMetricCreate = (PlaybackMetricCreate) o;
    return Objects.equals(this.downloadedBytesHTTP, playbackMetricCreate.downloadedBytesHTTP) &&
        Objects.equals(this.downloadedBytesP2P, playbackMetricCreate.downloadedBytesP2P) &&
        Objects.equals(this.errors, playbackMetricCreate.errors) &&
        Objects.equals(this.fps, playbackMetricCreate.fps) &&
        Objects.equals(this.playerMode, playbackMetricCreate.playerMode) &&
        Objects.equals(this.resolution, playbackMetricCreate.resolution) &&
        Objects.equals(this.resolutionChanges, playbackMetricCreate.resolutionChanges) &&
        Objects.equals(this.uploadedBytesP2P, playbackMetricCreate.uploadedBytesP2P) &&
        Objects.equals(this.videoId, playbackMetricCreate.videoId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(downloadedBytesHTTP, downloadedBytesP2P, errors, fps, playerMode, resolution, resolutionChanges, uploadedBytesP2P, videoId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaybackMetricCreate {\n");
    sb.append("    downloadedBytesHTTP: ").append(toIndentedString(downloadedBytesHTTP)).append("\n");
    sb.append("    downloadedBytesP2P: ").append(toIndentedString(downloadedBytesP2P)).append("\n");
    sb.append("    errors: ").append(toIndentedString(errors)).append("\n");
    sb.append("    fps: ").append(toIndentedString(fps)).append("\n");
    sb.append("    playerMode: ").append(toIndentedString(playerMode)).append("\n");
    sb.append("    resolution: ").append(toIndentedString(resolution)).append("\n");
    sb.append("    resolutionChanges: ").append(toIndentedString(resolutionChanges)).append("\n");
    sb.append("    uploadedBytesP2P: ").append(toIndentedString(uploadedBytesP2P)).append("\n");
    sb.append("    videoId: ").append(toIndentedString(videoId)).append("\n");
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
    openapiFields.add("downloadedBytesHTTP");
    openapiFields.add("downloadedBytesP2P");
    openapiFields.add("errors");
    openapiFields.add("fps");
    openapiFields.add("playerMode");
    openapiFields.add("resolution");
    openapiFields.add("resolutionChanges");
    openapiFields.add("uploadedBytesP2P");
    openapiFields.add("videoId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("downloadedBytesHTTP");
    openapiRequiredFields.add("downloadedBytesP2P");
    openapiRequiredFields.add("errors");
    openapiRequiredFields.add("playerMode");
    openapiRequiredFields.add("resolutionChanges");
    openapiRequiredFields.add("uploadedBytesP2P");
    openapiRequiredFields.add("videoId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaybackMetricCreate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaybackMetricCreate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaybackMetricCreate is not found in the empty JSON string", PlaybackMetricCreate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaybackMetricCreate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaybackMetricCreate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PlaybackMetricCreate.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("playerMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `playerMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("playerMode").toString()));
      }
      // validate the required field `playerMode`
      PlayerModeEnum.validateJsonElement(jsonObj.get("playerMode"));
      // validate the required field `videoId`
      GetLiveIdIdParameter.validateJsonElement(jsonObj.get("videoId"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaybackMetricCreate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaybackMetricCreate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaybackMetricCreate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaybackMetricCreate.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaybackMetricCreate>() {
           @Override
           public void write(JsonWriter out, PlaybackMetricCreate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaybackMetricCreate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaybackMetricCreate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaybackMetricCreate
   * @throws IOException if the JSON string is invalid with respect to PlaybackMetricCreate
   */
  public static PlaybackMetricCreate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaybackMetricCreate.class);
  }

  /**
   * Convert an instance of PlaybackMetricCreate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

