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
import org.openapitools.client.model.LiveVideoLatencyMode;
import org.openapitools.client.model.LiveVideoReplaySettings;

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
 * LiveVideoResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LiveVideoResponse {
  public static final String SERIALIZED_NAME_LATENCY_MODE = "latencyMode";
  @SerializedName(SERIALIZED_NAME_LATENCY_MODE)
  private LiveVideoLatencyMode latencyMode;

  public static final String SERIALIZED_NAME_PERMANENT_LIVE = "permanentLive";
  @SerializedName(SERIALIZED_NAME_PERMANENT_LIVE)
  private Boolean permanentLive;

  public static final String SERIALIZED_NAME_REPLAY_SETTINGS = "replaySettings";
  @SerializedName(SERIALIZED_NAME_REPLAY_SETTINGS)
  private LiveVideoReplaySettings replaySettings;

  public static final String SERIALIZED_NAME_RTMP_URL = "rtmpUrl";
  @SerializedName(SERIALIZED_NAME_RTMP_URL)
  private String rtmpUrl;

  public static final String SERIALIZED_NAME_RTMPS_URL = "rtmpsUrl";
  @SerializedName(SERIALIZED_NAME_RTMPS_URL)
  private String rtmpsUrl;

  public static final String SERIALIZED_NAME_SAVE_REPLAY = "saveReplay";
  @SerializedName(SERIALIZED_NAME_SAVE_REPLAY)
  private Boolean saveReplay;

  public static final String SERIALIZED_NAME_STREAM_KEY = "streamKey";
  @SerializedName(SERIALIZED_NAME_STREAM_KEY)
  private String streamKey;

  public LiveVideoResponse() {
  }

  public LiveVideoResponse latencyMode(LiveVideoLatencyMode latencyMode) {
    this.latencyMode = latencyMode;
    return this;
  }

  /**
   * Get latencyMode
   * @return latencyMode
   */
  @javax.annotation.Nullable
  public LiveVideoLatencyMode getLatencyMode() {
    return latencyMode;
  }

  public void setLatencyMode(LiveVideoLatencyMode latencyMode) {
    this.latencyMode = latencyMode;
  }


  public LiveVideoResponse permanentLive(Boolean permanentLive) {
    this.permanentLive = permanentLive;
    return this;
  }

  /**
   * User can stream multiple times in a permanent live
   * @return permanentLive
   */
  @javax.annotation.Nullable
  public Boolean getPermanentLive() {
    return permanentLive;
  }

  public void setPermanentLive(Boolean permanentLive) {
    this.permanentLive = permanentLive;
  }


  public LiveVideoResponse replaySettings(LiveVideoReplaySettings replaySettings) {
    this.replaySettings = replaySettings;
    return this;
  }

  /**
   * Get replaySettings
   * @return replaySettings
   */
  @javax.annotation.Nullable
  public LiveVideoReplaySettings getReplaySettings() {
    return replaySettings;
  }

  public void setReplaySettings(LiveVideoReplaySettings replaySettings) {
    this.replaySettings = replaySettings;
  }


  public LiveVideoResponse rtmpUrl(String rtmpUrl) {
    this.rtmpUrl = rtmpUrl;
    return this;
  }

  /**
   * Included in the response if an appropriate token is provided
   * @return rtmpUrl
   */
  @javax.annotation.Nullable
  public String getRtmpUrl() {
    return rtmpUrl;
  }

  public void setRtmpUrl(String rtmpUrl) {
    this.rtmpUrl = rtmpUrl;
  }


  public LiveVideoResponse rtmpsUrl(String rtmpsUrl) {
    this.rtmpsUrl = rtmpsUrl;
    return this;
  }

  /**
   * Included in the response if an appropriate token is provided
   * @return rtmpsUrl
   */
  @javax.annotation.Nullable
  public String getRtmpsUrl() {
    return rtmpsUrl;
  }

  public void setRtmpsUrl(String rtmpsUrl) {
    this.rtmpsUrl = rtmpsUrl;
  }


  public LiveVideoResponse saveReplay(Boolean saveReplay) {
    this.saveReplay = saveReplay;
    return this;
  }

  /**
   * Get saveReplay
   * @return saveReplay
   */
  @javax.annotation.Nullable
  public Boolean getSaveReplay() {
    return saveReplay;
  }

  public void setSaveReplay(Boolean saveReplay) {
    this.saveReplay = saveReplay;
  }


  public LiveVideoResponse streamKey(String streamKey) {
    this.streamKey = streamKey;
    return this;
  }

  /**
   * RTMP stream key to use to stream into this live video. Included in the response if an appropriate token is provided
   * @return streamKey
   */
  @javax.annotation.Nullable
  public String getStreamKey() {
    return streamKey;
  }

  public void setStreamKey(String streamKey) {
    this.streamKey = streamKey;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LiveVideoResponse liveVideoResponse = (LiveVideoResponse) o;
    return Objects.equals(this.latencyMode, liveVideoResponse.latencyMode) &&
        Objects.equals(this.permanentLive, liveVideoResponse.permanentLive) &&
        Objects.equals(this.replaySettings, liveVideoResponse.replaySettings) &&
        Objects.equals(this.rtmpUrl, liveVideoResponse.rtmpUrl) &&
        Objects.equals(this.rtmpsUrl, liveVideoResponse.rtmpsUrl) &&
        Objects.equals(this.saveReplay, liveVideoResponse.saveReplay) &&
        Objects.equals(this.streamKey, liveVideoResponse.streamKey);
  }

  @Override
  public int hashCode() {
    return Objects.hash(latencyMode, permanentLive, replaySettings, rtmpUrl, rtmpsUrl, saveReplay, streamKey);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LiveVideoResponse {\n");
    sb.append("    latencyMode: ").append(toIndentedString(latencyMode)).append("\n");
    sb.append("    permanentLive: ").append(toIndentedString(permanentLive)).append("\n");
    sb.append("    replaySettings: ").append(toIndentedString(replaySettings)).append("\n");
    sb.append("    rtmpUrl: ").append(toIndentedString(rtmpUrl)).append("\n");
    sb.append("    rtmpsUrl: ").append(toIndentedString(rtmpsUrl)).append("\n");
    sb.append("    saveReplay: ").append(toIndentedString(saveReplay)).append("\n");
    sb.append("    streamKey: ").append(toIndentedString(streamKey)).append("\n");
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
    openapiFields.add("latencyMode");
    openapiFields.add("permanentLive");
    openapiFields.add("replaySettings");
    openapiFields.add("rtmpUrl");
    openapiFields.add("rtmpsUrl");
    openapiFields.add("saveReplay");
    openapiFields.add("streamKey");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LiveVideoResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LiveVideoResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LiveVideoResponse is not found in the empty JSON string", LiveVideoResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LiveVideoResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LiveVideoResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `latencyMode`
      if (jsonObj.get("latencyMode") != null && !jsonObj.get("latencyMode").isJsonNull()) {
        LiveVideoLatencyMode.validateJsonElement(jsonObj.get("latencyMode"));
      }
      // validate the optional field `replaySettings`
      if (jsonObj.get("replaySettings") != null && !jsonObj.get("replaySettings").isJsonNull()) {
        LiveVideoReplaySettings.validateJsonElement(jsonObj.get("replaySettings"));
      }
      if ((jsonObj.get("rtmpUrl") != null && !jsonObj.get("rtmpUrl").isJsonNull()) && !jsonObj.get("rtmpUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rtmpUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rtmpUrl").toString()));
      }
      if ((jsonObj.get("rtmpsUrl") != null && !jsonObj.get("rtmpsUrl").isJsonNull()) && !jsonObj.get("rtmpsUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rtmpsUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rtmpsUrl").toString()));
      }
      if ((jsonObj.get("streamKey") != null && !jsonObj.get("streamKey").isJsonNull()) && !jsonObj.get("streamKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `streamKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("streamKey").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LiveVideoResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LiveVideoResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LiveVideoResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LiveVideoResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<LiveVideoResponse>() {
           @Override
           public void write(JsonWriter out, LiveVideoResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LiveVideoResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LiveVideoResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LiveVideoResponse
   * @throws IOException if the JSON string is invalid with respect to LiveVideoResponse
   */
  public static LiveVideoResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LiveVideoResponse.class);
  }

  /**
   * Convert an instance of LiveVideoResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

