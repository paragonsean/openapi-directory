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
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;
import org.openapitools.client.model.VideoPrivacySet;
import org.openapitools.client.model.VideoScheduledUpdate;

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
 * VideoUploadRequestResumable
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideoUploadRequestResumable {
  public static final String SERIALIZED_NAME_CATEGORY = "category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private Integer category;

  public static final String SERIALIZED_NAME_CHANNEL_ID = "channelId";
  @SerializedName(SERIALIZED_NAME_CHANNEL_ID)
  private Integer channelId;

  public static final String SERIALIZED_NAME_COMMENTS_ENABLED = "commentsEnabled";
  @SerializedName(SERIALIZED_NAME_COMMENTS_ENABLED)
  private Boolean commentsEnabled;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DOWNLOAD_ENABLED = "downloadEnabled";
  @SerializedName(SERIALIZED_NAME_DOWNLOAD_ENABLED)
  private Boolean downloadEnabled;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_LICENCE = "licence";
  @SerializedName(SERIALIZED_NAME_LICENCE)
  private Integer licence;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NSFW = "nsfw";
  @SerializedName(SERIALIZED_NAME_NSFW)
  private Boolean nsfw;

  public static final String SERIALIZED_NAME_ORIGINALLY_PUBLISHED_AT = "originallyPublishedAt";
  @SerializedName(SERIALIZED_NAME_ORIGINALLY_PUBLISHED_AT)
  private OffsetDateTime originallyPublishedAt;

  public static final String SERIALIZED_NAME_PREVIEWFILE = "previewfile";
  @SerializedName(SERIALIZED_NAME_PREVIEWFILE)
  private File previewfile;

  public static final String SERIALIZED_NAME_PRIVACY = "privacy";
  @SerializedName(SERIALIZED_NAME_PRIVACY)
  private VideoPrivacySet privacy;

  public static final String SERIALIZED_NAME_SCHEDULE_UPDATE = "scheduleUpdate";
  @SerializedName(SERIALIZED_NAME_SCHEDULE_UPDATE)
  private VideoScheduledUpdate scheduleUpdate;

  public static final String SERIALIZED_NAME_SUPPORT = "support";
  @SerializedName(SERIALIZED_NAME_SUPPORT)
  private String support;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private Set<String> tags = new LinkedHashSet<>();

  public static final String SERIALIZED_NAME_THUMBNAILFILE = "thumbnailfile";
  @SerializedName(SERIALIZED_NAME_THUMBNAILFILE)
  private File thumbnailfile;

  public static final String SERIALIZED_NAME_WAIT_TRANSCODING = "waitTranscoding";
  @SerializedName(SERIALIZED_NAME_WAIT_TRANSCODING)
  private Boolean waitTranscoding;

  public static final String SERIALIZED_NAME_FILENAME = "filename";
  @SerializedName(SERIALIZED_NAME_FILENAME)
  private String filename;

  public VideoUploadRequestResumable() {
  }

  public VideoUploadRequestResumable category(Integer category) {
    this.category = category;
    return this;
  }

  /**
   * category id of the video (see [/videos/categories](#operation/getCategories))
   * @return category
   */
  @javax.annotation.Nullable
  public Integer getCategory() {
    return category;
  }

  public void setCategory(Integer category) {
    this.category = category;
  }


  public VideoUploadRequestResumable channelId(Integer channelId) {
    this.channelId = channelId;
    return this;
  }

  /**
   * Channel id that will contain this video
   * minimum: 1
   * @return channelId
   */
  @javax.annotation.Nonnull
  public Integer getChannelId() {
    return channelId;
  }

  public void setChannelId(Integer channelId) {
    this.channelId = channelId;
  }


  public VideoUploadRequestResumable commentsEnabled(Boolean commentsEnabled) {
    this.commentsEnabled = commentsEnabled;
    return this;
  }

  /**
   * Enable or disable comments for this video
   * @return commentsEnabled
   */
  @javax.annotation.Nullable
  public Boolean getCommentsEnabled() {
    return commentsEnabled;
  }

  public void setCommentsEnabled(Boolean commentsEnabled) {
    this.commentsEnabled = commentsEnabled;
  }


  public VideoUploadRequestResumable description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Video description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public VideoUploadRequestResumable downloadEnabled(Boolean downloadEnabled) {
    this.downloadEnabled = downloadEnabled;
    return this;
  }

  /**
   * Enable or disable downloading for this video
   * @return downloadEnabled
   */
  @javax.annotation.Nullable
  public Boolean getDownloadEnabled() {
    return downloadEnabled;
  }

  public void setDownloadEnabled(Boolean downloadEnabled) {
    this.downloadEnabled = downloadEnabled;
  }


  public VideoUploadRequestResumable language(String language) {
    this.language = language;
    return this;
  }

  /**
   * language id of the video (see [/videos/languages](#operation/getLanguages))
   * @return language
   */
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public VideoUploadRequestResumable licence(Integer licence) {
    this.licence = licence;
    return this;
  }

  /**
   * licence id of the video (see [/videos/licences](#operation/getLicences))
   * @return licence
   */
  @javax.annotation.Nullable
  public Integer getLicence() {
    return licence;
  }

  public void setLicence(Integer licence) {
    this.licence = licence;
  }


  public VideoUploadRequestResumable name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Video name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public VideoUploadRequestResumable nsfw(Boolean nsfw) {
    this.nsfw = nsfw;
    return this;
  }

  /**
   * Whether or not this video contains sensitive content
   * @return nsfw
   */
  @javax.annotation.Nullable
  public Boolean getNsfw() {
    return nsfw;
  }

  public void setNsfw(Boolean nsfw) {
    this.nsfw = nsfw;
  }


  public VideoUploadRequestResumable originallyPublishedAt(OffsetDateTime originallyPublishedAt) {
    this.originallyPublishedAt = originallyPublishedAt;
    return this;
  }

  /**
   * Date when the content was originally published
   * @return originallyPublishedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getOriginallyPublishedAt() {
    return originallyPublishedAt;
  }

  public void setOriginallyPublishedAt(OffsetDateTime originallyPublishedAt) {
    this.originallyPublishedAt = originallyPublishedAt;
  }


  public VideoUploadRequestResumable previewfile(File previewfile) {
    this.previewfile = previewfile;
    return this;
  }

  /**
   * Video preview file
   * @return previewfile
   */
  @javax.annotation.Nullable
  public File getPreviewfile() {
    return previewfile;
  }

  public void setPreviewfile(File previewfile) {
    this.previewfile = previewfile;
  }


  public VideoUploadRequestResumable privacy(VideoPrivacySet privacy) {
    this.privacy = privacy;
    return this;
  }

  /**
   * Get privacy
   * @return privacy
   */
  @javax.annotation.Nullable
  public VideoPrivacySet getPrivacy() {
    return privacy;
  }

  public void setPrivacy(VideoPrivacySet privacy) {
    this.privacy = privacy;
  }


  public VideoUploadRequestResumable scheduleUpdate(VideoScheduledUpdate scheduleUpdate) {
    this.scheduleUpdate = scheduleUpdate;
    return this;
  }

  /**
   * Get scheduleUpdate
   * @return scheduleUpdate
   */
  @javax.annotation.Nullable
  public VideoScheduledUpdate getScheduleUpdate() {
    return scheduleUpdate;
  }

  public void setScheduleUpdate(VideoScheduledUpdate scheduleUpdate) {
    this.scheduleUpdate = scheduleUpdate;
  }


  public VideoUploadRequestResumable support(String support) {
    this.support = support;
    return this;
  }

  /**
   * A text tell the audience how to support the video creator
   * @return support
   */
  @javax.annotation.Nullable
  public String getSupport() {
    return support;
  }

  public void setSupport(String support) {
    this.support = support;
  }


  public VideoUploadRequestResumable tags(Set<String> tags) {
    this.tags = tags;
    return this;
  }

  public VideoUploadRequestResumable addTagsItem(String tagsItem) {
    if (this.tags == null) {
      this.tags = new LinkedHashSet<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * Video tags (maximum 5 tags each between 2 and 30 characters)
   * @return tags
   */
  @javax.annotation.Nullable
  public Set<String> getTags() {
    return tags;
  }

  public void setTags(Set<String> tags) {
    this.tags = tags;
  }


  public VideoUploadRequestResumable thumbnailfile(File thumbnailfile) {
    this.thumbnailfile = thumbnailfile;
    return this;
  }

  /**
   * Video thumbnail file
   * @return thumbnailfile
   */
  @javax.annotation.Nullable
  public File getThumbnailfile() {
    return thumbnailfile;
  }

  public void setThumbnailfile(File thumbnailfile) {
    this.thumbnailfile = thumbnailfile;
  }


  public VideoUploadRequestResumable waitTranscoding(Boolean waitTranscoding) {
    this.waitTranscoding = waitTranscoding;
    return this;
  }

  /**
   * Whether or not we wait transcoding before publish the video
   * @return waitTranscoding
   */
  @javax.annotation.Nullable
  public Boolean getWaitTranscoding() {
    return waitTranscoding;
  }

  public void setWaitTranscoding(Boolean waitTranscoding) {
    this.waitTranscoding = waitTranscoding;
  }


  public VideoUploadRequestResumable filename(String filename) {
    this.filename = filename;
    return this;
  }

  /**
   * Video filename including extension
   * @return filename
   */
  @javax.annotation.Nonnull
  public String getFilename() {
    return filename;
  }

  public void setFilename(String filename) {
    this.filename = filename;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VideoUploadRequestResumable videoUploadRequestResumable = (VideoUploadRequestResumable) o;
    return Objects.equals(this.category, videoUploadRequestResumable.category) &&
        Objects.equals(this.channelId, videoUploadRequestResumable.channelId) &&
        Objects.equals(this.commentsEnabled, videoUploadRequestResumable.commentsEnabled) &&
        Objects.equals(this.description, videoUploadRequestResumable.description) &&
        Objects.equals(this.downloadEnabled, videoUploadRequestResumable.downloadEnabled) &&
        Objects.equals(this.language, videoUploadRequestResumable.language) &&
        Objects.equals(this.licence, videoUploadRequestResumable.licence) &&
        Objects.equals(this.name, videoUploadRequestResumable.name) &&
        Objects.equals(this.nsfw, videoUploadRequestResumable.nsfw) &&
        Objects.equals(this.originallyPublishedAt, videoUploadRequestResumable.originallyPublishedAt) &&
        Objects.equals(this.previewfile, videoUploadRequestResumable.previewfile) &&
        Objects.equals(this.privacy, videoUploadRequestResumable.privacy) &&
        Objects.equals(this.scheduleUpdate, videoUploadRequestResumable.scheduleUpdate) &&
        Objects.equals(this.support, videoUploadRequestResumable.support) &&
        Objects.equals(this.tags, videoUploadRequestResumable.tags) &&
        Objects.equals(this.thumbnailfile, videoUploadRequestResumable.thumbnailfile) &&
        Objects.equals(this.waitTranscoding, videoUploadRequestResumable.waitTranscoding) &&
        Objects.equals(this.filename, videoUploadRequestResumable.filename);
  }

  @Override
  public int hashCode() {
    return Objects.hash(category, channelId, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, filename);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VideoUploadRequestResumable {\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    channelId: ").append(toIndentedString(channelId)).append("\n");
    sb.append("    commentsEnabled: ").append(toIndentedString(commentsEnabled)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    downloadEnabled: ").append(toIndentedString(downloadEnabled)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    licence: ").append(toIndentedString(licence)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nsfw: ").append(toIndentedString(nsfw)).append("\n");
    sb.append("    originallyPublishedAt: ").append(toIndentedString(originallyPublishedAt)).append("\n");
    sb.append("    previewfile: ").append(toIndentedString(previewfile)).append("\n");
    sb.append("    privacy: ").append(toIndentedString(privacy)).append("\n");
    sb.append("    scheduleUpdate: ").append(toIndentedString(scheduleUpdate)).append("\n");
    sb.append("    support: ").append(toIndentedString(support)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    thumbnailfile: ").append(toIndentedString(thumbnailfile)).append("\n");
    sb.append("    waitTranscoding: ").append(toIndentedString(waitTranscoding)).append("\n");
    sb.append("    filename: ").append(toIndentedString(filename)).append("\n");
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
    openapiFields.add("category");
    openapiFields.add("channelId");
    openapiFields.add("commentsEnabled");
    openapiFields.add("description");
    openapiFields.add("downloadEnabled");
    openapiFields.add("language");
    openapiFields.add("licence");
    openapiFields.add("name");
    openapiFields.add("nsfw");
    openapiFields.add("originallyPublishedAt");
    openapiFields.add("previewfile");
    openapiFields.add("privacy");
    openapiFields.add("scheduleUpdate");
    openapiFields.add("support");
    openapiFields.add("tags");
    openapiFields.add("thumbnailfile");
    openapiFields.add("waitTranscoding");
    openapiFields.add("filename");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("channelId");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("filename");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VideoUploadRequestResumable
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VideoUploadRequestResumable.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VideoUploadRequestResumable is not found in the empty JSON string", VideoUploadRequestResumable.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VideoUploadRequestResumable.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VideoUploadRequestResumable` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : VideoUploadRequestResumable.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `privacy`
      if (jsonObj.get("privacy") != null && !jsonObj.get("privacy").isJsonNull()) {
        VideoPrivacySet.validateJsonElement(jsonObj.get("privacy"));
      }
      // validate the optional field `scheduleUpdate`
      if (jsonObj.get("scheduleUpdate") != null && !jsonObj.get("scheduleUpdate").isJsonNull()) {
        VideoScheduledUpdate.validateJsonElement(jsonObj.get("scheduleUpdate"));
      }
      if ((jsonObj.get("support") != null && !jsonObj.get("support").isJsonNull()) && !jsonObj.get("support").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `support` to be a primitive type in the JSON string but got `%s`", jsonObj.get("support").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if (!jsonObj.get("filename").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `filename` to be a primitive type in the JSON string but got `%s`", jsonObj.get("filename").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VideoUploadRequestResumable.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VideoUploadRequestResumable' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VideoUploadRequestResumable> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VideoUploadRequestResumable.class));

       return (TypeAdapter<T>) new TypeAdapter<VideoUploadRequestResumable>() {
           @Override
           public void write(JsonWriter out, VideoUploadRequestResumable value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VideoUploadRequestResumable read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VideoUploadRequestResumable given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VideoUploadRequestResumable
   * @throws IOException if the JSON string is invalid with respect to VideoUploadRequestResumable
   */
  public static VideoUploadRequestResumable fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VideoUploadRequestResumable.class);
  }

  /**
   * Convert an instance of VideoUploadRequestResumable to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

