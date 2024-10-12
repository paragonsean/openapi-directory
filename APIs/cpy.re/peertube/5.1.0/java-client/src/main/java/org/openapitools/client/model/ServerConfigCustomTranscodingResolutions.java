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
 * Resolutions to transcode _new videos_ to
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerConfigCustomTranscodingResolutions {
  public static final String SERIALIZED_NAME_0P = "0p";
  @SerializedName(SERIALIZED_NAME_0P)
  private Boolean _0p;

  public static final String SERIALIZED_NAME_1080P = "1080p";
  @SerializedName(SERIALIZED_NAME_1080P)
  private Boolean _1080p;

  public static final String SERIALIZED_NAME_1440P = "1440p";
  @SerializedName(SERIALIZED_NAME_1440P)
  private Boolean _1440p;

  public static final String SERIALIZED_NAME_144P = "144p";
  @SerializedName(SERIALIZED_NAME_144P)
  private Boolean _144p;

  public static final String SERIALIZED_NAME_2160P = "2160p";
  @SerializedName(SERIALIZED_NAME_2160P)
  private Boolean _2160p;

  public static final String SERIALIZED_NAME_240P = "240p";
  @SerializedName(SERIALIZED_NAME_240P)
  private Boolean _240p;

  public static final String SERIALIZED_NAME_360P = "360p";
  @SerializedName(SERIALIZED_NAME_360P)
  private Boolean _360p;

  public static final String SERIALIZED_NAME_480P = "480p";
  @SerializedName(SERIALIZED_NAME_480P)
  private Boolean _480p;

  public static final String SERIALIZED_NAME_720P = "720p";
  @SerializedName(SERIALIZED_NAME_720P)
  private Boolean _720p;

  public ServerConfigCustomTranscodingResolutions() {
  }

  public ServerConfigCustomTranscodingResolutions _0p(Boolean _0p) {
    this._0p = _0p;
    return this;
  }

  /**
   * Get _0p
   * @return _0p
   */
  @javax.annotation.Nullable
  public Boolean get0p() {
    return _0p;
  }

  public void set0p(Boolean _0p) {
    this._0p = _0p;
  }


  public ServerConfigCustomTranscodingResolutions _1080p(Boolean _1080p) {
    this._1080p = _1080p;
    return this;
  }

  /**
   * Get _1080p
   * @return _1080p
   */
  @javax.annotation.Nullable
  public Boolean get1080p() {
    return _1080p;
  }

  public void set1080p(Boolean _1080p) {
    this._1080p = _1080p;
  }


  public ServerConfigCustomTranscodingResolutions _1440p(Boolean _1440p) {
    this._1440p = _1440p;
    return this;
  }

  /**
   * Get _1440p
   * @return _1440p
   */
  @javax.annotation.Nullable
  public Boolean get1440p() {
    return _1440p;
  }

  public void set1440p(Boolean _1440p) {
    this._1440p = _1440p;
  }


  public ServerConfigCustomTranscodingResolutions _144p(Boolean _144p) {
    this._144p = _144p;
    return this;
  }

  /**
   * Get _144p
   * @return _144p
   */
  @javax.annotation.Nullable
  public Boolean get144p() {
    return _144p;
  }

  public void set144p(Boolean _144p) {
    this._144p = _144p;
  }


  public ServerConfigCustomTranscodingResolutions _2160p(Boolean _2160p) {
    this._2160p = _2160p;
    return this;
  }

  /**
   * Get _2160p
   * @return _2160p
   */
  @javax.annotation.Nullable
  public Boolean get2160p() {
    return _2160p;
  }

  public void set2160p(Boolean _2160p) {
    this._2160p = _2160p;
  }


  public ServerConfigCustomTranscodingResolutions _240p(Boolean _240p) {
    this._240p = _240p;
    return this;
  }

  /**
   * Get _240p
   * @return _240p
   */
  @javax.annotation.Nullable
  public Boolean get240p() {
    return _240p;
  }

  public void set240p(Boolean _240p) {
    this._240p = _240p;
  }


  public ServerConfigCustomTranscodingResolutions _360p(Boolean _360p) {
    this._360p = _360p;
    return this;
  }

  /**
   * Get _360p
   * @return _360p
   */
  @javax.annotation.Nullable
  public Boolean get360p() {
    return _360p;
  }

  public void set360p(Boolean _360p) {
    this._360p = _360p;
  }


  public ServerConfigCustomTranscodingResolutions _480p(Boolean _480p) {
    this._480p = _480p;
    return this;
  }

  /**
   * Get _480p
   * @return _480p
   */
  @javax.annotation.Nullable
  public Boolean get480p() {
    return _480p;
  }

  public void set480p(Boolean _480p) {
    this._480p = _480p;
  }


  public ServerConfigCustomTranscodingResolutions _720p(Boolean _720p) {
    this._720p = _720p;
    return this;
  }

  /**
   * Get _720p
   * @return _720p
   */
  @javax.annotation.Nullable
  public Boolean get720p() {
    return _720p;
  }

  public void set720p(Boolean _720p) {
    this._720p = _720p;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerConfigCustomTranscodingResolutions serverConfigCustomTranscodingResolutions = (ServerConfigCustomTranscodingResolutions) o;
    return Objects.equals(this._0p, serverConfigCustomTranscodingResolutions._0p) &&
        Objects.equals(this._1080p, serverConfigCustomTranscodingResolutions._1080p) &&
        Objects.equals(this._1440p, serverConfigCustomTranscodingResolutions._1440p) &&
        Objects.equals(this._144p, serverConfigCustomTranscodingResolutions._144p) &&
        Objects.equals(this._2160p, serverConfigCustomTranscodingResolutions._2160p) &&
        Objects.equals(this._240p, serverConfigCustomTranscodingResolutions._240p) &&
        Objects.equals(this._360p, serverConfigCustomTranscodingResolutions._360p) &&
        Objects.equals(this._480p, serverConfigCustomTranscodingResolutions._480p) &&
        Objects.equals(this._720p, serverConfigCustomTranscodingResolutions._720p);
  }

  @Override
  public int hashCode() {
    return Objects.hash(_0p, _1080p, _1440p, _144p, _2160p, _240p, _360p, _480p, _720p);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerConfigCustomTranscodingResolutions {\n");
    sb.append("    _0p: ").append(toIndentedString(_0p)).append("\n");
    sb.append("    _1080p: ").append(toIndentedString(_1080p)).append("\n");
    sb.append("    _1440p: ").append(toIndentedString(_1440p)).append("\n");
    sb.append("    _144p: ").append(toIndentedString(_144p)).append("\n");
    sb.append("    _2160p: ").append(toIndentedString(_2160p)).append("\n");
    sb.append("    _240p: ").append(toIndentedString(_240p)).append("\n");
    sb.append("    _360p: ").append(toIndentedString(_360p)).append("\n");
    sb.append("    _480p: ").append(toIndentedString(_480p)).append("\n");
    sb.append("    _720p: ").append(toIndentedString(_720p)).append("\n");
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
    openapiFields.add("0p");
    openapiFields.add("1080p");
    openapiFields.add("1440p");
    openapiFields.add("144p");
    openapiFields.add("2160p");
    openapiFields.add("240p");
    openapiFields.add("360p");
    openapiFields.add("480p");
    openapiFields.add("720p");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerConfigCustomTranscodingResolutions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerConfigCustomTranscodingResolutions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerConfigCustomTranscodingResolutions is not found in the empty JSON string", ServerConfigCustomTranscodingResolutions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerConfigCustomTranscodingResolutions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerConfigCustomTranscodingResolutions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerConfigCustomTranscodingResolutions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerConfigCustomTranscodingResolutions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerConfigCustomTranscodingResolutions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerConfigCustomTranscodingResolutions.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerConfigCustomTranscodingResolutions>() {
           @Override
           public void write(JsonWriter out, ServerConfigCustomTranscodingResolutions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerConfigCustomTranscodingResolutions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerConfigCustomTranscodingResolutions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerConfigCustomTranscodingResolutions
   * @throws IOException if the JSON string is invalid with respect to ServerConfigCustomTranscodingResolutions
   */
  public static ServerConfigCustomTranscodingResolutions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerConfigCustomTranscodingResolutions.class);
  }

  /**
   * Convert an instance of ServerConfigCustomTranscodingResolutions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

