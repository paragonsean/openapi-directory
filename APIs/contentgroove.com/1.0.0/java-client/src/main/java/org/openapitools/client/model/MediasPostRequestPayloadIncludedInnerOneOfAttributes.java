/*
 * ContentGroove API
 * # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \"CALLBACKS\" sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \"processing\" state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \"Ok\"   - The request was valid - 400 \"Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether - 401 \"Unauthorized\"   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \"Payment Required\"   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \"Not Found\"   - This is returned when the resource you are trying to view does not exist - 429 \"Too Many Requests\"   - This is returned when you have performed too many requests within a given period of time - 500 \"Internal Server Error\"   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   ```   curl -T /path/to/file upload_url   ``` - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   > At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header `Authorization: Bearer abc123` - Request header `X-API-KEY: abc123` - Query parameter `api_key=abc123`   > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
 *
 * The version of the OpenAPI document: 1.0.0
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
 * MediasPostRequestPayloadIncludedInnerOneOfAttributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:59:27.157946-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MediasPostRequestPayloadIncludedInnerOneOfAttributes {
  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_END_CHAR = "end_char";
  @SerializedName(SERIALIZED_NAME_END_CHAR)
  private String endChar;

  public static final String SERIALIZED_NAME_END_TIME = "end_time";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private BigDecimal endTime;

  public static final String SERIALIZED_NAME_EXTERNAL_ID = "external_id";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_ID)
  private String externalId;

  public static final String SERIALIZED_NAME_MEDIA_FILE_CONTENT_TYPE = "media_file_content_type";
  @SerializedName(SERIALIZED_NAME_MEDIA_FILE_CONTENT_TYPE)
  private String mediaFileContentType;

  public static final String SERIALIZED_NAME_MEDIA_FILE_DURATION = "media_file_duration";
  @SerializedName(SERIALIZED_NAME_MEDIA_FILE_DURATION)
  private BigDecimal mediaFileDuration;

  public static final String SERIALIZED_NAME_MEDIA_FILE_HEIGHT = "media_file_height";
  @SerializedName(SERIALIZED_NAME_MEDIA_FILE_HEIGHT)
  private BigDecimal mediaFileHeight;

  public static final String SERIALIZED_NAME_MEDIA_FILE_PREVIEW_IMAGE_URL = "media_file_preview_image_url";
  @SerializedName(SERIALIZED_NAME_MEDIA_FILE_PREVIEW_IMAGE_URL)
  private String mediaFilePreviewImageUrl;

  public static final String SERIALIZED_NAME_MEDIA_FILE_URL = "media_file_url";
  @SerializedName(SERIALIZED_NAME_MEDIA_FILE_URL)
  private String mediaFileUrl;

  public static final String SERIALIZED_NAME_MEDIA_FILE_WIDTH = "media_file_width";
  @SerializedName(SERIALIZED_NAME_MEDIA_FILE_WIDTH)
  private BigDecimal mediaFileWidth;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_RANK = "rank";
  @SerializedName(SERIALIZED_NAME_RANK)
  private Integer rank;

  public static final String SERIALIZED_NAME_START_CHAR = "start_char";
  @SerializedName(SERIALIZED_NAME_START_CHAR)
  private Integer startChar;

  public static final String SERIALIZED_NAME_START_TIME = "start_time";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private BigDecimal startTime;

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public MediasPostRequestPayloadIncludedInnerOneOfAttributes() {
  }

  public MediasPostRequestPayloadIncludedInnerOneOfAttributes createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes endChar(String endChar) {
    this.endChar = endChar;
    return this;
  }

  /**
   * Get endChar
   * @return endChar
   */
  @javax.annotation.Nullable
  public String getEndChar() {
    return endChar;
  }

  public void setEndChar(String endChar) {
    this.endChar = endChar;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes endTime(BigDecimal endTime) {
    this.endTime = endTime;
    return this;
  }

  /**
   * Get endTime
   * @return endTime
   */
  @javax.annotation.Nullable
  public BigDecimal getEndTime() {
    return endTime;
  }

  public void setEndTime(BigDecimal endTime) {
    this.endTime = endTime;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes externalId(String externalId) {
    this.externalId = externalId;
    return this;
  }

  /**
   * Get externalId
   * @return externalId
   */
  @javax.annotation.Nullable
  public String getExternalId() {
    return externalId;
  }

  public void setExternalId(String externalId) {
    this.externalId = externalId;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes mediaFileContentType(String mediaFileContentType) {
    this.mediaFileContentType = mediaFileContentType;
    return this;
  }

  /**
   * Get mediaFileContentType
   * @return mediaFileContentType
   */
  @javax.annotation.Nullable
  public String getMediaFileContentType() {
    return mediaFileContentType;
  }

  public void setMediaFileContentType(String mediaFileContentType) {
    this.mediaFileContentType = mediaFileContentType;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes mediaFileDuration(BigDecimal mediaFileDuration) {
    this.mediaFileDuration = mediaFileDuration;
    return this;
  }

  /**
   * Get mediaFileDuration
   * @return mediaFileDuration
   */
  @javax.annotation.Nullable
  public BigDecimal getMediaFileDuration() {
    return mediaFileDuration;
  }

  public void setMediaFileDuration(BigDecimal mediaFileDuration) {
    this.mediaFileDuration = mediaFileDuration;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes mediaFileHeight(BigDecimal mediaFileHeight) {
    this.mediaFileHeight = mediaFileHeight;
    return this;
  }

  /**
   * Get mediaFileHeight
   * @return mediaFileHeight
   */
  @javax.annotation.Nullable
  public BigDecimal getMediaFileHeight() {
    return mediaFileHeight;
  }

  public void setMediaFileHeight(BigDecimal mediaFileHeight) {
    this.mediaFileHeight = mediaFileHeight;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes mediaFilePreviewImageUrl(String mediaFilePreviewImageUrl) {
    this.mediaFilePreviewImageUrl = mediaFilePreviewImageUrl;
    return this;
  }

  /**
   * Get mediaFilePreviewImageUrl
   * @return mediaFilePreviewImageUrl
   */
  @javax.annotation.Nullable
  public String getMediaFilePreviewImageUrl() {
    return mediaFilePreviewImageUrl;
  }

  public void setMediaFilePreviewImageUrl(String mediaFilePreviewImageUrl) {
    this.mediaFilePreviewImageUrl = mediaFilePreviewImageUrl;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes mediaFileUrl(String mediaFileUrl) {
    this.mediaFileUrl = mediaFileUrl;
    return this;
  }

  /**
   * Get mediaFileUrl
   * @return mediaFileUrl
   */
  @javax.annotation.Nullable
  public String getMediaFileUrl() {
    return mediaFileUrl;
  }

  public void setMediaFileUrl(String mediaFileUrl) {
    this.mediaFileUrl = mediaFileUrl;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes mediaFileWidth(BigDecimal mediaFileWidth) {
    this.mediaFileWidth = mediaFileWidth;
    return this;
  }

  /**
   * Get mediaFileWidth
   * @return mediaFileWidth
   */
  @javax.annotation.Nullable
  public BigDecimal getMediaFileWidth() {
    return mediaFileWidth;
  }

  public void setMediaFileWidth(BigDecimal mediaFileWidth) {
    this.mediaFileWidth = mediaFileWidth;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes rank(Integer rank) {
    this.rank = rank;
    return this;
  }

  /**
   * Get rank
   * @return rank
   */
  @javax.annotation.Nullable
  public Integer getRank() {
    return rank;
  }

  public void setRank(Integer rank) {
    this.rank = rank;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes startChar(Integer startChar) {
    this.startChar = startChar;
    return this;
  }

  /**
   * Get startChar
   * @return startChar
   */
  @javax.annotation.Nullable
  public Integer getStartChar() {
    return startChar;
  }

  public void setStartChar(Integer startChar) {
    this.startChar = startChar;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes startTime(BigDecimal startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Get startTime
   * @return startTime
   */
  @javax.annotation.Nullable
  public BigDecimal getStartTime() {
    return startTime;
  }

  public void setStartTime(BigDecimal startTime) {
    this.startTime = startTime;
  }


  public MediasPostRequestPayloadIncludedInnerOneOfAttributes text(String text) {
    this.text = text;
    return this;
  }

  /**
   * Get text
   * @return text
   */
  @javax.annotation.Nullable
  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MediasPostRequestPayloadIncludedInnerOneOfAttributes mediasPostRequestPayloadIncludedInnerOneOfAttributes = (MediasPostRequestPayloadIncludedInnerOneOfAttributes) o;
    return Objects.equals(this.createdAt, mediasPostRequestPayloadIncludedInnerOneOfAttributes.createdAt) &&
        Objects.equals(this.endChar, mediasPostRequestPayloadIncludedInnerOneOfAttributes.endChar) &&
        Objects.equals(this.endTime, mediasPostRequestPayloadIncludedInnerOneOfAttributes.endTime) &&
        Objects.equals(this.externalId, mediasPostRequestPayloadIncludedInnerOneOfAttributes.externalId) &&
        Objects.equals(this.mediaFileContentType, mediasPostRequestPayloadIncludedInnerOneOfAttributes.mediaFileContentType) &&
        Objects.equals(this.mediaFileDuration, mediasPostRequestPayloadIncludedInnerOneOfAttributes.mediaFileDuration) &&
        Objects.equals(this.mediaFileHeight, mediasPostRequestPayloadIncludedInnerOneOfAttributes.mediaFileHeight) &&
        Objects.equals(this.mediaFilePreviewImageUrl, mediasPostRequestPayloadIncludedInnerOneOfAttributes.mediaFilePreviewImageUrl) &&
        Objects.equals(this.mediaFileUrl, mediasPostRequestPayloadIncludedInnerOneOfAttributes.mediaFileUrl) &&
        Objects.equals(this.mediaFileWidth, mediasPostRequestPayloadIncludedInnerOneOfAttributes.mediaFileWidth) &&
        Objects.equals(this.name, mediasPostRequestPayloadIncludedInnerOneOfAttributes.name) &&
        Objects.equals(this.rank, mediasPostRequestPayloadIncludedInnerOneOfAttributes.rank) &&
        Objects.equals(this.startChar, mediasPostRequestPayloadIncludedInnerOneOfAttributes.startChar) &&
        Objects.equals(this.startTime, mediasPostRequestPayloadIncludedInnerOneOfAttributes.startTime) &&
        Objects.equals(this.text, mediasPostRequestPayloadIncludedInnerOneOfAttributes.text);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, endChar, endTime, externalId, mediaFileContentType, mediaFileDuration, mediaFileHeight, mediaFilePreviewImageUrl, mediaFileUrl, mediaFileWidth, name, rank, startChar, startTime, text);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MediasPostRequestPayloadIncludedInnerOneOfAttributes {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    endChar: ").append(toIndentedString(endChar)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    externalId: ").append(toIndentedString(externalId)).append("\n");
    sb.append("    mediaFileContentType: ").append(toIndentedString(mediaFileContentType)).append("\n");
    sb.append("    mediaFileDuration: ").append(toIndentedString(mediaFileDuration)).append("\n");
    sb.append("    mediaFileHeight: ").append(toIndentedString(mediaFileHeight)).append("\n");
    sb.append("    mediaFilePreviewImageUrl: ").append(toIndentedString(mediaFilePreviewImageUrl)).append("\n");
    sb.append("    mediaFileUrl: ").append(toIndentedString(mediaFileUrl)).append("\n");
    sb.append("    mediaFileWidth: ").append(toIndentedString(mediaFileWidth)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    rank: ").append(toIndentedString(rank)).append("\n");
    sb.append("    startChar: ").append(toIndentedString(startChar)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
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
    openapiFields.add("created_at");
    openapiFields.add("end_char");
    openapiFields.add("end_time");
    openapiFields.add("external_id");
    openapiFields.add("media_file_content_type");
    openapiFields.add("media_file_duration");
    openapiFields.add("media_file_height");
    openapiFields.add("media_file_preview_image_url");
    openapiFields.add("media_file_url");
    openapiFields.add("media_file_width");
    openapiFields.add("name");
    openapiFields.add("rank");
    openapiFields.add("start_char");
    openapiFields.add("start_time");
    openapiFields.add("text");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MediasPostRequestPayloadIncludedInnerOneOfAttributes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MediasPostRequestPayloadIncludedInnerOneOfAttributes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MediasPostRequestPayloadIncludedInnerOneOfAttributes is not found in the empty JSON string", MediasPostRequestPayloadIncludedInnerOneOfAttributes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MediasPostRequestPayloadIncludedInnerOneOfAttributes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MediasPostRequestPayloadIncludedInnerOneOfAttributes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("end_char") != null && !jsonObj.get("end_char").isJsonNull()) && !jsonObj.get("end_char").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_char` to be a primitive type in the JSON string but got `%s`", jsonObj.get("end_char").toString()));
      }
      if ((jsonObj.get("external_id") != null && !jsonObj.get("external_id").isJsonNull()) && !jsonObj.get("external_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `external_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("external_id").toString()));
      }
      if ((jsonObj.get("media_file_content_type") != null && !jsonObj.get("media_file_content_type").isJsonNull()) && !jsonObj.get("media_file_content_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `media_file_content_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("media_file_content_type").toString()));
      }
      if ((jsonObj.get("media_file_preview_image_url") != null && !jsonObj.get("media_file_preview_image_url").isJsonNull()) && !jsonObj.get("media_file_preview_image_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `media_file_preview_image_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("media_file_preview_image_url").toString()));
      }
      if ((jsonObj.get("media_file_url") != null && !jsonObj.get("media_file_url").isJsonNull()) && !jsonObj.get("media_file_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `media_file_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("media_file_url").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("text") != null && !jsonObj.get("text").isJsonNull()) && !jsonObj.get("text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("text").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MediasPostRequestPayloadIncludedInnerOneOfAttributes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MediasPostRequestPayloadIncludedInnerOneOfAttributes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MediasPostRequestPayloadIncludedInnerOneOfAttributes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MediasPostRequestPayloadIncludedInnerOneOfAttributes.class));

       return (TypeAdapter<T>) new TypeAdapter<MediasPostRequestPayloadIncludedInnerOneOfAttributes>() {
           @Override
           public void write(JsonWriter out, MediasPostRequestPayloadIncludedInnerOneOfAttributes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MediasPostRequestPayloadIncludedInnerOneOfAttributes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MediasPostRequestPayloadIncludedInnerOneOfAttributes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MediasPostRequestPayloadIncludedInnerOneOfAttributes
   * @throws IOException if the JSON string is invalid with respect to MediasPostRequestPayloadIncludedInnerOneOfAttributes
   */
  public static MediasPostRequestPayloadIncludedInnerOneOfAttributes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MediasPostRequestPayloadIncludedInnerOneOfAttributes.class);
  }

  /**
   * Convert an instance of MediasPostRequestPayloadIncludedInnerOneOfAttributes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

