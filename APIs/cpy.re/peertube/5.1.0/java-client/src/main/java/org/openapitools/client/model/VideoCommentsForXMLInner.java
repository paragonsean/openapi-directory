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
 * VideoCommentsForXMLInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideoCommentsForXMLInner {
  public static final String SERIALIZED_NAME_CONTENT_COLON_ENCODED = "content:encoded";
  @SerializedName(SERIALIZED_NAME_CONTENT_COLON_ENCODED)
  private String contentColonEncoded;

  public static final String SERIALIZED_NAME_DC_COLON_CREATOR = "dc:creator";
  @SerializedName(SERIALIZED_NAME_DC_COLON_CREATOR)
  private String dcColonCreator;

  public static final String SERIALIZED_NAME_GUID = "guid";
  @SerializedName(SERIALIZED_NAME_GUID)
  private String guid;

  public static final String SERIALIZED_NAME_LINK = "link";
  @SerializedName(SERIALIZED_NAME_LINK)
  private String link;

  public static final String SERIALIZED_NAME_PUB_DATE = "pubDate";
  @SerializedName(SERIALIZED_NAME_PUB_DATE)
  private OffsetDateTime pubDate;

  public VideoCommentsForXMLInner() {
  }

  public VideoCommentsForXMLInner contentColonEncoded(String contentColonEncoded) {
    this.contentColonEncoded = contentColonEncoded;
    return this;
  }

  /**
   * Get contentColonEncoded
   * @return contentColonEncoded
   */
  @javax.annotation.Nullable
  public String getContentColonEncoded() {
    return contentColonEncoded;
  }

  public void setContentColonEncoded(String contentColonEncoded) {
    this.contentColonEncoded = contentColonEncoded;
  }


  public VideoCommentsForXMLInner dcColonCreator(String dcColonCreator) {
    this.dcColonCreator = dcColonCreator;
    return this;
  }

  /**
   * Get dcColonCreator
   * @return dcColonCreator
   */
  @javax.annotation.Nullable
  public String getDcColonCreator() {
    return dcColonCreator;
  }

  public void setDcColonCreator(String dcColonCreator) {
    this.dcColonCreator = dcColonCreator;
  }


  public VideoCommentsForXMLInner guid(String guid) {
    this.guid = guid;
    return this;
  }

  /**
   * Get guid
   * @return guid
   */
  @javax.annotation.Nullable
  public String getGuid() {
    return guid;
  }

  public void setGuid(String guid) {
    this.guid = guid;
  }


  public VideoCommentsForXMLInner link(String link) {
    this.link = link;
    return this;
  }

  /**
   * Get link
   * @return link
   */
  @javax.annotation.Nullable
  public String getLink() {
    return link;
  }

  public void setLink(String link) {
    this.link = link;
  }


  public VideoCommentsForXMLInner pubDate(OffsetDateTime pubDate) {
    this.pubDate = pubDate;
    return this;
  }

  /**
   * Get pubDate
   * @return pubDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPubDate() {
    return pubDate;
  }

  public void setPubDate(OffsetDateTime pubDate) {
    this.pubDate = pubDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VideoCommentsForXMLInner videoCommentsForXMLInner = (VideoCommentsForXMLInner) o;
    return Objects.equals(this.contentColonEncoded, videoCommentsForXMLInner.contentColonEncoded) &&
        Objects.equals(this.dcColonCreator, videoCommentsForXMLInner.dcColonCreator) &&
        Objects.equals(this.guid, videoCommentsForXMLInner.guid) &&
        Objects.equals(this.link, videoCommentsForXMLInner.link) &&
        Objects.equals(this.pubDate, videoCommentsForXMLInner.pubDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contentColonEncoded, dcColonCreator, guid, link, pubDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VideoCommentsForXMLInner {\n");
    sb.append("    contentColonEncoded: ").append(toIndentedString(contentColonEncoded)).append("\n");
    sb.append("    dcColonCreator: ").append(toIndentedString(dcColonCreator)).append("\n");
    sb.append("    guid: ").append(toIndentedString(guid)).append("\n");
    sb.append("    link: ").append(toIndentedString(link)).append("\n");
    sb.append("    pubDate: ").append(toIndentedString(pubDate)).append("\n");
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
    openapiFields.add("content:encoded");
    openapiFields.add("dc:creator");
    openapiFields.add("guid");
    openapiFields.add("link");
    openapiFields.add("pubDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VideoCommentsForXMLInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VideoCommentsForXMLInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VideoCommentsForXMLInner is not found in the empty JSON string", VideoCommentsForXMLInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VideoCommentsForXMLInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VideoCommentsForXMLInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("content:encoded") != null && !jsonObj.get("content:encoded").isJsonNull()) && !jsonObj.get("content:encoded").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content:encoded` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content:encoded").toString()));
      }
      if ((jsonObj.get("dc:creator") != null && !jsonObj.get("dc:creator").isJsonNull()) && !jsonObj.get("dc:creator").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dc:creator` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dc:creator").toString()));
      }
      if ((jsonObj.get("guid") != null && !jsonObj.get("guid").isJsonNull()) && !jsonObj.get("guid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `guid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("guid").toString()));
      }
      if ((jsonObj.get("link") != null && !jsonObj.get("link").isJsonNull()) && !jsonObj.get("link").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `link` to be a primitive type in the JSON string but got `%s`", jsonObj.get("link").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VideoCommentsForXMLInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VideoCommentsForXMLInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VideoCommentsForXMLInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VideoCommentsForXMLInner.class));

       return (TypeAdapter<T>) new TypeAdapter<VideoCommentsForXMLInner>() {
           @Override
           public void write(JsonWriter out, VideoCommentsForXMLInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VideoCommentsForXMLInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VideoCommentsForXMLInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VideoCommentsForXMLInner
   * @throws IOException if the JSON string is invalid with respect to VideoCommentsForXMLInner
   */
  public static VideoCommentsForXMLInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VideoCommentsForXMLInner.class);
  }

  /**
   * Convert an instance of VideoCommentsForXMLInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

