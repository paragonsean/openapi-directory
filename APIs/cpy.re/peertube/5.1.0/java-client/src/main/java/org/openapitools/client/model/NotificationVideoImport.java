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
import java.net.URI;
import java.util.Arrays;
import org.openapitools.client.model.VideoInfo;
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
 * NotificationVideoImport
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NotificationVideoImport {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_MAGNET_URI = "magnetUri";
  @SerializedName(SERIALIZED_NAME_MAGNET_URI)
  private URI magnetUri;

  public static final String SERIALIZED_NAME_TARGET_URI = "targetUri";
  @SerializedName(SERIALIZED_NAME_TARGET_URI)
  private URI targetUri;

  public static final String SERIALIZED_NAME_TORRENT_NAME = "torrentName";
  @SerializedName(SERIALIZED_NAME_TORRENT_NAME)
  private String torrentName;

  public static final String SERIALIZED_NAME_VIDEO = "video";
  @SerializedName(SERIALIZED_NAME_VIDEO)
  private VideoInfo video;

  public NotificationVideoImport() {
  }

  public NotificationVideoImport id(Integer id) {
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


  public NotificationVideoImport magnetUri(URI magnetUri) {
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


  public NotificationVideoImport targetUri(URI targetUri) {
    this.targetUri = targetUri;
    return this;
  }

  /**
   * Get targetUri
   * @return targetUri
   */
  @javax.annotation.Nullable
  public URI getTargetUri() {
    return targetUri;
  }

  public void setTargetUri(URI targetUri) {
    this.targetUri = targetUri;
  }


  public NotificationVideoImport torrentName(String torrentName) {
    this.torrentName = torrentName;
    return this;
  }

  /**
   * Get torrentName
   * @return torrentName
   */
  @javax.annotation.Nullable
  public String getTorrentName() {
    return torrentName;
  }

  public void setTorrentName(String torrentName) {
    this.torrentName = torrentName;
  }


  public NotificationVideoImport video(VideoInfo video) {
    this.video = video;
    return this;
  }

  /**
   * Get video
   * @return video
   */
  @javax.annotation.Nullable
  public VideoInfo getVideo() {
    return video;
  }

  public void setVideo(VideoInfo video) {
    this.video = video;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NotificationVideoImport notificationVideoImport = (NotificationVideoImport) o;
    return Objects.equals(this.id, notificationVideoImport.id) &&
        Objects.equals(this.magnetUri, notificationVideoImport.magnetUri) &&
        Objects.equals(this.targetUri, notificationVideoImport.targetUri) &&
        Objects.equals(this.torrentName, notificationVideoImport.torrentName) &&
        Objects.equals(this.video, notificationVideoImport.video);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, magnetUri, targetUri, torrentName, video);
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
    sb.append("class NotificationVideoImport {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    magnetUri: ").append(toIndentedString(magnetUri)).append("\n");
    sb.append("    targetUri: ").append(toIndentedString(targetUri)).append("\n");
    sb.append("    torrentName: ").append(toIndentedString(torrentName)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("magnetUri");
    openapiFields.add("targetUri");
    openapiFields.add("torrentName");
    openapiFields.add("video");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NotificationVideoImport
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NotificationVideoImport.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NotificationVideoImport is not found in the empty JSON string", NotificationVideoImport.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NotificationVideoImport.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NotificationVideoImport` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("magnetUri") != null && !jsonObj.get("magnetUri").isJsonNull()) && !jsonObj.get("magnetUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `magnetUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("magnetUri").toString()));
      }
      if ((jsonObj.get("targetUri") != null && !jsonObj.get("targetUri").isJsonNull()) && !jsonObj.get("targetUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("targetUri").toString()));
      }
      if ((jsonObj.get("torrentName") != null && !jsonObj.get("torrentName").isJsonNull()) && !jsonObj.get("torrentName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `torrentName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("torrentName").toString()));
      }
      // validate the optional field `video`
      if (jsonObj.get("video") != null && !jsonObj.get("video").isJsonNull()) {
        VideoInfo.validateJsonElement(jsonObj.get("video"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NotificationVideoImport.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NotificationVideoImport' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NotificationVideoImport> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NotificationVideoImport.class));

       return (TypeAdapter<T>) new TypeAdapter<NotificationVideoImport>() {
           @Override
           public void write(JsonWriter out, NotificationVideoImport value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NotificationVideoImport read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NotificationVideoImport given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NotificationVideoImport
   * @throws IOException if the JSON string is invalid with respect to NotificationVideoImport
   */
  public static NotificationVideoImport fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NotificationVideoImport.class);
  }

  /**
   * Convert an instance of NotificationVideoImport to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

