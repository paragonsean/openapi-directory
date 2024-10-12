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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.VideosForXMLInnerEnclosure;
import org.openapitools.client.model.VideosForXMLInnerMediaCommunity;
import org.openapitools.client.model.VideosForXMLInnerMediaEmbed;
import org.openapitools.client.model.VideosForXMLInnerMediaGroupInner;
import org.openapitools.client.model.VideosForXMLInnerMediaPlayer;
import org.openapitools.client.model.VideosForXMLInnerMediaThumbnail;

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
 * VideosForXMLInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideosForXMLInner {
  public static final String SERIALIZED_NAME_CONTENT_COLON_ENCODED = "content:encoded";
  @SerializedName(SERIALIZED_NAME_CONTENT_COLON_ENCODED)
  private String contentColonEncoded;

  public static final String SERIALIZED_NAME_DC_COLON_CREATOR = "dc:creator";
  @SerializedName(SERIALIZED_NAME_DC_COLON_CREATOR)
  private String dcColonCreator;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ENCLOSURE = "enclosure";
  @SerializedName(SERIALIZED_NAME_ENCLOSURE)
  private VideosForXMLInnerEnclosure enclosure;

  public static final String SERIALIZED_NAME_GUID = "guid";
  @SerializedName(SERIALIZED_NAME_GUID)
  private String guid;

  public static final String SERIALIZED_NAME_LINK = "link";
  @SerializedName(SERIALIZED_NAME_LINK)
  private String link;

  public static final String SERIALIZED_NAME_MEDIA_COLON_CATEGORY = "media:category";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_CATEGORY)
  private Integer mediaColonCategory;

  public static final String SERIALIZED_NAME_MEDIA_COLON_COMMUNITY = "media:community";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_COMMUNITY)
  private VideosForXMLInnerMediaCommunity mediaColonCommunity;

  public static final String SERIALIZED_NAME_MEDIA_COLON_DESCRIPTION = "media:description";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_DESCRIPTION)
  private String mediaColonDescription;

  public static final String SERIALIZED_NAME_MEDIA_COLON_EMBED = "media:embed";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_EMBED)
  private VideosForXMLInnerMediaEmbed mediaColonEmbed;

  public static final String SERIALIZED_NAME_MEDIA_COLON_GROUP = "media:group";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_GROUP)
  private List<VideosForXMLInnerMediaGroupInner> mediaColonGroup = new ArrayList<>();

  public static final String SERIALIZED_NAME_MEDIA_COLON_PLAYER = "media:player";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_PLAYER)
  private VideosForXMLInnerMediaPlayer mediaColonPlayer;

  /**
   * see [media:rating](https://www.rssboard.org/media-rss#media-rating) (MRSS)
   */
  @JsonAdapter(MediaColonRatingEnum.Adapter.class)
  public enum MediaColonRatingEnum {
    NONADULT("nonadult"),
    
    ADULT("adult");

    private String value;

    MediaColonRatingEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MediaColonRatingEnum fromValue(String value) {
      for (MediaColonRatingEnum b : MediaColonRatingEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MediaColonRatingEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MediaColonRatingEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MediaColonRatingEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MediaColonRatingEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MediaColonRatingEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_MEDIA_COLON_RATING = "media:rating";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_RATING)
  private MediaColonRatingEnum mediaColonRating;

  public static final String SERIALIZED_NAME_MEDIA_COLON_THUMBNAIL = "media:thumbnail";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_THUMBNAIL)
  private VideosForXMLInnerMediaThumbnail mediaColonThumbnail;

  public static final String SERIALIZED_NAME_MEDIA_COLON_TITLE = "media:title";
  @SerializedName(SERIALIZED_NAME_MEDIA_COLON_TITLE)
  private String mediaColonTitle;

  public static final String SERIALIZED_NAME_PUB_DATE = "pubDate";
  @SerializedName(SERIALIZED_NAME_PUB_DATE)
  private OffsetDateTime pubDate;

  public VideosForXMLInner() {
  }

  public VideosForXMLInner contentColonEncoded(String contentColonEncoded) {
    this.contentColonEncoded = contentColonEncoded;
    return this;
  }

  /**
   * video description
   * @return contentColonEncoded
   */
  @javax.annotation.Nullable
  public String getContentColonEncoded() {
    return contentColonEncoded;
  }

  public void setContentColonEncoded(String contentColonEncoded) {
    this.contentColonEncoded = contentColonEncoded;
  }


  public VideosForXMLInner dcColonCreator(String dcColonCreator) {
    this.dcColonCreator = dcColonCreator;
    return this;
  }

  /**
   * publisher user name
   * @return dcColonCreator
   */
  @javax.annotation.Nullable
  public String getDcColonCreator() {
    return dcColonCreator;
  }

  public void setDcColonCreator(String dcColonCreator) {
    this.dcColonCreator = dcColonCreator;
  }


  public VideosForXMLInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * video description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public VideosForXMLInner enclosure(VideosForXMLInnerEnclosure enclosure) {
    this.enclosure = enclosure;
    return this;
  }

  /**
   * Get enclosure
   * @return enclosure
   */
  @javax.annotation.Nullable
  public VideosForXMLInnerEnclosure getEnclosure() {
    return enclosure;
  }

  public void setEnclosure(VideosForXMLInnerEnclosure enclosure) {
    this.enclosure = enclosure;
  }


  public VideosForXMLInner guid(String guid) {
    this.guid = guid;
    return this;
  }

  /**
   * video canonical URL
   * @return guid
   */
  @javax.annotation.Nullable
  public String getGuid() {
    return guid;
  }

  public void setGuid(String guid) {
    this.guid = guid;
  }


  public VideosForXMLInner link(String link) {
    this.link = link;
    return this;
  }

  /**
   * video watch page URL
   * @return link
   */
  @javax.annotation.Nullable
  public String getLink() {
    return link;
  }

  public void setLink(String link) {
    this.link = link;
  }


  public VideosForXMLInner mediaColonCategory(Integer mediaColonCategory) {
    this.mediaColonCategory = mediaColonCategory;
    return this;
  }

  /**
   * video category (MRSS)
   * @return mediaColonCategory
   */
  @javax.annotation.Nullable
  public Integer getMediaColonCategory() {
    return mediaColonCategory;
  }

  public void setMediaColonCategory(Integer mediaColonCategory) {
    this.mediaColonCategory = mediaColonCategory;
  }


  public VideosForXMLInner mediaColonCommunity(VideosForXMLInnerMediaCommunity mediaColonCommunity) {
    this.mediaColonCommunity = mediaColonCommunity;
    return this;
  }

  /**
   * Get mediaColonCommunity
   * @return mediaColonCommunity
   */
  @javax.annotation.Nullable
  public VideosForXMLInnerMediaCommunity getMediaColonCommunity() {
    return mediaColonCommunity;
  }

  public void setMediaColonCommunity(VideosForXMLInnerMediaCommunity mediaColonCommunity) {
    this.mediaColonCommunity = mediaColonCommunity;
  }


  public VideosForXMLInner mediaColonDescription(String mediaColonDescription) {
    this.mediaColonDescription = mediaColonDescription;
    return this;
  }

  /**
   * Get mediaColonDescription
   * @return mediaColonDescription
   */
  @javax.annotation.Nullable
  public String getMediaColonDescription() {
    return mediaColonDescription;
  }

  public void setMediaColonDescription(String mediaColonDescription) {
    this.mediaColonDescription = mediaColonDescription;
  }


  public VideosForXMLInner mediaColonEmbed(VideosForXMLInnerMediaEmbed mediaColonEmbed) {
    this.mediaColonEmbed = mediaColonEmbed;
    return this;
  }

  /**
   * Get mediaColonEmbed
   * @return mediaColonEmbed
   */
  @javax.annotation.Nullable
  public VideosForXMLInnerMediaEmbed getMediaColonEmbed() {
    return mediaColonEmbed;
  }

  public void setMediaColonEmbed(VideosForXMLInnerMediaEmbed mediaColonEmbed) {
    this.mediaColonEmbed = mediaColonEmbed;
  }


  public VideosForXMLInner mediaColonGroup(List<VideosForXMLInnerMediaGroupInner> mediaColonGroup) {
    this.mediaColonGroup = mediaColonGroup;
    return this;
  }

  public VideosForXMLInner addMediaColonGroupItem(VideosForXMLInnerMediaGroupInner mediaColonGroupItem) {
    if (this.mediaColonGroup == null) {
      this.mediaColonGroup = new ArrayList<>();
    }
    this.mediaColonGroup.add(mediaColonGroupItem);
    return this;
  }

  /**
   * list of streamable files for the video. see [media:peerLink](https://www.rssboard.org/media-rss#media-peerlink) and [media:content](https://www.rssboard.org/media-rss#media-content) or  (MRSS)
   * @return mediaColonGroup
   */
  @javax.annotation.Nullable
  public List<VideosForXMLInnerMediaGroupInner> getMediaColonGroup() {
    return mediaColonGroup;
  }

  public void setMediaColonGroup(List<VideosForXMLInnerMediaGroupInner> mediaColonGroup) {
    this.mediaColonGroup = mediaColonGroup;
  }


  public VideosForXMLInner mediaColonPlayer(VideosForXMLInnerMediaPlayer mediaColonPlayer) {
    this.mediaColonPlayer = mediaColonPlayer;
    return this;
  }

  /**
   * Get mediaColonPlayer
   * @return mediaColonPlayer
   */
  @javax.annotation.Nullable
  public VideosForXMLInnerMediaPlayer getMediaColonPlayer() {
    return mediaColonPlayer;
  }

  public void setMediaColonPlayer(VideosForXMLInnerMediaPlayer mediaColonPlayer) {
    this.mediaColonPlayer = mediaColonPlayer;
  }


  public VideosForXMLInner mediaColonRating(MediaColonRatingEnum mediaColonRating) {
    this.mediaColonRating = mediaColonRating;
    return this;
  }

  /**
   * see [media:rating](https://www.rssboard.org/media-rss#media-rating) (MRSS)
   * @return mediaColonRating
   */
  @javax.annotation.Nullable
  public MediaColonRatingEnum getMediaColonRating() {
    return mediaColonRating;
  }

  public void setMediaColonRating(MediaColonRatingEnum mediaColonRating) {
    this.mediaColonRating = mediaColonRating;
  }


  public VideosForXMLInner mediaColonThumbnail(VideosForXMLInnerMediaThumbnail mediaColonThumbnail) {
    this.mediaColonThumbnail = mediaColonThumbnail;
    return this;
  }

  /**
   * Get mediaColonThumbnail
   * @return mediaColonThumbnail
   */
  @javax.annotation.Nullable
  public VideosForXMLInnerMediaThumbnail getMediaColonThumbnail() {
    return mediaColonThumbnail;
  }

  public void setMediaColonThumbnail(VideosForXMLInnerMediaThumbnail mediaColonThumbnail) {
    this.mediaColonThumbnail = mediaColonThumbnail;
  }


  public VideosForXMLInner mediaColonTitle(String mediaColonTitle) {
    this.mediaColonTitle = mediaColonTitle;
    return this;
  }

  /**
   * see [media:title](https://www.rssboard.org/media-rss#media-title) (MRSS). We only use &#x60;plain&#x60; titles.
   * @return mediaColonTitle
   */
  @javax.annotation.Nullable
  public String getMediaColonTitle() {
    return mediaColonTitle;
  }

  public void setMediaColonTitle(String mediaColonTitle) {
    this.mediaColonTitle = mediaColonTitle;
  }


  public VideosForXMLInner pubDate(OffsetDateTime pubDate) {
    this.pubDate = pubDate;
    return this;
  }

  /**
   * video publication date
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
    VideosForXMLInner videosForXMLInner = (VideosForXMLInner) o;
    return Objects.equals(this.contentColonEncoded, videosForXMLInner.contentColonEncoded) &&
        Objects.equals(this.dcColonCreator, videosForXMLInner.dcColonCreator) &&
        Objects.equals(this.description, videosForXMLInner.description) &&
        Objects.equals(this.enclosure, videosForXMLInner.enclosure) &&
        Objects.equals(this.guid, videosForXMLInner.guid) &&
        Objects.equals(this.link, videosForXMLInner.link) &&
        Objects.equals(this.mediaColonCategory, videosForXMLInner.mediaColonCategory) &&
        Objects.equals(this.mediaColonCommunity, videosForXMLInner.mediaColonCommunity) &&
        Objects.equals(this.mediaColonDescription, videosForXMLInner.mediaColonDescription) &&
        Objects.equals(this.mediaColonEmbed, videosForXMLInner.mediaColonEmbed) &&
        Objects.equals(this.mediaColonGroup, videosForXMLInner.mediaColonGroup) &&
        Objects.equals(this.mediaColonPlayer, videosForXMLInner.mediaColonPlayer) &&
        Objects.equals(this.mediaColonRating, videosForXMLInner.mediaColonRating) &&
        Objects.equals(this.mediaColonThumbnail, videosForXMLInner.mediaColonThumbnail) &&
        Objects.equals(this.mediaColonTitle, videosForXMLInner.mediaColonTitle) &&
        Objects.equals(this.pubDate, videosForXMLInner.pubDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contentColonEncoded, dcColonCreator, description, enclosure, guid, link, mediaColonCategory, mediaColonCommunity, mediaColonDescription, mediaColonEmbed, mediaColonGroup, mediaColonPlayer, mediaColonRating, mediaColonThumbnail, mediaColonTitle, pubDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VideosForXMLInner {\n");
    sb.append("    contentColonEncoded: ").append(toIndentedString(contentColonEncoded)).append("\n");
    sb.append("    dcColonCreator: ").append(toIndentedString(dcColonCreator)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    enclosure: ").append(toIndentedString(enclosure)).append("\n");
    sb.append("    guid: ").append(toIndentedString(guid)).append("\n");
    sb.append("    link: ").append(toIndentedString(link)).append("\n");
    sb.append("    mediaColonCategory: ").append(toIndentedString(mediaColonCategory)).append("\n");
    sb.append("    mediaColonCommunity: ").append(toIndentedString(mediaColonCommunity)).append("\n");
    sb.append("    mediaColonDescription: ").append(toIndentedString(mediaColonDescription)).append("\n");
    sb.append("    mediaColonEmbed: ").append(toIndentedString(mediaColonEmbed)).append("\n");
    sb.append("    mediaColonGroup: ").append(toIndentedString(mediaColonGroup)).append("\n");
    sb.append("    mediaColonPlayer: ").append(toIndentedString(mediaColonPlayer)).append("\n");
    sb.append("    mediaColonRating: ").append(toIndentedString(mediaColonRating)).append("\n");
    sb.append("    mediaColonThumbnail: ").append(toIndentedString(mediaColonThumbnail)).append("\n");
    sb.append("    mediaColonTitle: ").append(toIndentedString(mediaColonTitle)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("enclosure");
    openapiFields.add("guid");
    openapiFields.add("link");
    openapiFields.add("media:category");
    openapiFields.add("media:community");
    openapiFields.add("media:description");
    openapiFields.add("media:embed");
    openapiFields.add("media:group");
    openapiFields.add("media:player");
    openapiFields.add("media:rating");
    openapiFields.add("media:thumbnail");
    openapiFields.add("media:title");
    openapiFields.add("pubDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VideosForXMLInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VideosForXMLInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VideosForXMLInner is not found in the empty JSON string", VideosForXMLInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VideosForXMLInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VideosForXMLInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("content:encoded") != null && !jsonObj.get("content:encoded").isJsonNull()) && !jsonObj.get("content:encoded").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content:encoded` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content:encoded").toString()));
      }
      if ((jsonObj.get("dc:creator") != null && !jsonObj.get("dc:creator").isJsonNull()) && !jsonObj.get("dc:creator").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dc:creator` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dc:creator").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `enclosure`
      if (jsonObj.get("enclosure") != null && !jsonObj.get("enclosure").isJsonNull()) {
        VideosForXMLInnerEnclosure.validateJsonElement(jsonObj.get("enclosure"));
      }
      if ((jsonObj.get("guid") != null && !jsonObj.get("guid").isJsonNull()) && !jsonObj.get("guid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `guid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("guid").toString()));
      }
      if ((jsonObj.get("link") != null && !jsonObj.get("link").isJsonNull()) && !jsonObj.get("link").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `link` to be a primitive type in the JSON string but got `%s`", jsonObj.get("link").toString()));
      }
      // validate the optional field `media:community`
      if (jsonObj.get("media:community") != null && !jsonObj.get("media:community").isJsonNull()) {
        VideosForXMLInnerMediaCommunity.validateJsonElement(jsonObj.get("media:community"));
      }
      if ((jsonObj.get("media:description") != null && !jsonObj.get("media:description").isJsonNull()) && !jsonObj.get("media:description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `media:description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("media:description").toString()));
      }
      // validate the optional field `media:embed`
      if (jsonObj.get("media:embed") != null && !jsonObj.get("media:embed").isJsonNull()) {
        VideosForXMLInnerMediaEmbed.validateJsonElement(jsonObj.get("media:embed"));
      }
      if (jsonObj.get("media:group") != null && !jsonObj.get("media:group").isJsonNull()) {
        JsonArray jsonArraymediaColonGroup = jsonObj.getAsJsonArray("media:group");
        if (jsonArraymediaColonGroup != null) {
          // ensure the json data is an array
          if (!jsonObj.get("media:group").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `media:group` to be an array in the JSON string but got `%s`", jsonObj.get("media:group").toString()));
          }

          // validate the optional field `media:group` (array)
          for (int i = 0; i < jsonArraymediaColonGroup.size(); i++) {
            VideosForXMLInnerMediaGroupInner.validateJsonElement(jsonArraymediaColonGroup.get(i));
          };
        }
      }
      // validate the optional field `media:player`
      if (jsonObj.get("media:player") != null && !jsonObj.get("media:player").isJsonNull()) {
        VideosForXMLInnerMediaPlayer.validateJsonElement(jsonObj.get("media:player"));
      }
      if ((jsonObj.get("media:rating") != null && !jsonObj.get("media:rating").isJsonNull()) && !jsonObj.get("media:rating").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `media:rating` to be a primitive type in the JSON string but got `%s`", jsonObj.get("media:rating").toString()));
      }
      // validate the optional field `media:rating`
      if (jsonObj.get("media:rating") != null && !jsonObj.get("media:rating").isJsonNull()) {
        MediaColonRatingEnum.validateJsonElement(jsonObj.get("media:rating"));
      }
      // validate the optional field `media:thumbnail`
      if (jsonObj.get("media:thumbnail") != null && !jsonObj.get("media:thumbnail").isJsonNull()) {
        VideosForXMLInnerMediaThumbnail.validateJsonElement(jsonObj.get("media:thumbnail"));
      }
      if ((jsonObj.get("media:title") != null && !jsonObj.get("media:title").isJsonNull()) && !jsonObj.get("media:title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `media:title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("media:title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VideosForXMLInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VideosForXMLInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VideosForXMLInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VideosForXMLInner.class));

       return (TypeAdapter<T>) new TypeAdapter<VideosForXMLInner>() {
           @Override
           public void write(JsonWriter out, VideosForXMLInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VideosForXMLInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VideosForXMLInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VideosForXMLInner
   * @throws IOException if the JSON string is invalid with respect to VideosForXMLInner
   */
  public static VideosForXMLInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VideosForXMLInner.class);
  }

  /**
   * Convert an instance of VideosForXMLInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

