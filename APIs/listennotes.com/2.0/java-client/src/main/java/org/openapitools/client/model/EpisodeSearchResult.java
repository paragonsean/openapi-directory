/*
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
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
import org.openapitools.client.model.EpisodeSearchResultPodcast;

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
 * When **type** is *episode*.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:39.439950-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EpisodeSearchResult {
  public static final String SERIALIZED_NAME_AUDIO = "audio";
  @SerializedName(SERIALIZED_NAME_AUDIO)
  private String audio;

  public static final String SERIALIZED_NAME_AUDIO_LENGTH_SEC = "audio_length_sec";
  @SerializedName(SERIALIZED_NAME_AUDIO_LENGTH_SEC)
  private Integer audioLengthSec;

  public static final String SERIALIZED_NAME_DESCRIPTION_HIGHLIGHTED = "description_highlighted";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION_HIGHLIGHTED)
  private String descriptionHighlighted;

  public static final String SERIALIZED_NAME_DESCRIPTION_ORIGINAL = "description_original";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION_ORIGINAL)
  private String descriptionOriginal;

  public static final String SERIALIZED_NAME_EXPLICIT_CONTENT = "explicit_content";
  @SerializedName(SERIALIZED_NAME_EXPLICIT_CONTENT)
  private Boolean explicitContent;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_ITUNES_ID = "itunes_id";
  @SerializedName(SERIALIZED_NAME_ITUNES_ID)
  private Integer itunesId;

  public static final String SERIALIZED_NAME_LINK = "link";
  @SerializedName(SERIALIZED_NAME_LINK)
  private String link;

  public static final String SERIALIZED_NAME_LISTENNOTES_URL = "listennotes_url";
  @SerializedName(SERIALIZED_NAME_LISTENNOTES_URL)
  private String listennotesUrl;

  public static final String SERIALIZED_NAME_PODCAST = "podcast";
  @SerializedName(SERIALIZED_NAME_PODCAST)
  private EpisodeSearchResultPodcast podcast;

  public static final String SERIALIZED_NAME_PUB_DATE_MS = "pub_date_ms";
  @SerializedName(SERIALIZED_NAME_PUB_DATE_MS)
  private Integer pubDateMs;

  public static final String SERIALIZED_NAME_RSS = "rss";
  @SerializedName(SERIALIZED_NAME_RSS)
  private String rss;

  public static final String SERIALIZED_NAME_THUMBNAIL = "thumbnail";
  @SerializedName(SERIALIZED_NAME_THUMBNAIL)
  private String thumbnail;

  public static final String SERIALIZED_NAME_TITLE_HIGHLIGHTED = "title_highlighted";
  @SerializedName(SERIALIZED_NAME_TITLE_HIGHLIGHTED)
  private String titleHighlighted;

  public static final String SERIALIZED_NAME_TITLE_ORIGINAL = "title_original";
  @SerializedName(SERIALIZED_NAME_TITLE_ORIGINAL)
  private String titleOriginal;

  public static final String SERIALIZED_NAME_TRANSCRIPTS_HIGHLIGHTED = "transcripts_highlighted";
  @SerializedName(SERIALIZED_NAME_TRANSCRIPTS_HIGHLIGHTED)
  private List<String> transcriptsHighlighted = new ArrayList<>();

  public EpisodeSearchResult() {
  }

  public EpisodeSearchResult audio(String audio) {
    this.audio = audio;
    return this;
  }

  /**
   * Audio url of this episode, which can be played directly.
   * @return audio
   */
  @javax.annotation.Nullable
  public String getAudio() {
    return audio;
  }

  public void setAudio(String audio) {
    this.audio = audio;
  }


  public EpisodeSearchResult audioLengthSec(Integer audioLengthSec) {
    this.audioLengthSec = audioLengthSec;
    return this;
  }

  /**
   * Audio length of this episode. In seconds.
   * @return audioLengthSec
   */
  @javax.annotation.Nullable
  public Integer getAudioLengthSec() {
    return audioLengthSec;
  }

  public void setAudioLengthSec(Integer audioLengthSec) {
    this.audioLengthSec = audioLengthSec;
  }


  public EpisodeSearchResult descriptionHighlighted(String descriptionHighlighted) {
    this.descriptionHighlighted = descriptionHighlighted;
    return this;
  }

  /**
   * Highlighted segment of this episode&#39;s description
   * @return descriptionHighlighted
   */
  @javax.annotation.Nullable
  public String getDescriptionHighlighted() {
    return descriptionHighlighted;
  }

  public void setDescriptionHighlighted(String descriptionHighlighted) {
    this.descriptionHighlighted = descriptionHighlighted;
  }


  public EpisodeSearchResult descriptionOriginal(String descriptionOriginal) {
    this.descriptionOriginal = descriptionOriginal;
    return this;
  }

  /**
   * Plain text of this episode&#39;s description
   * @return descriptionOriginal
   */
  @javax.annotation.Nullable
  public String getDescriptionOriginal() {
    return descriptionOriginal;
  }

  public void setDescriptionOriginal(String descriptionOriginal) {
    this.descriptionOriginal = descriptionOriginal;
  }


  public EpisodeSearchResult explicitContent(Boolean explicitContent) {
    this.explicitContent = explicitContent;
    return this;
  }

  /**
   * Whether this podcast contains explicit language.
   * @return explicitContent
   */
  @javax.annotation.Nullable
  public Boolean getExplicitContent() {
    return explicitContent;
  }

  public void setExplicitContent(Boolean explicitContent) {
    this.explicitContent = explicitContent;
  }


  public EpisodeSearchResult id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Episode id, which can be used to further fetch detailed episode metadata via &#x60;GET /episodes/{id}&#x60;.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public EpisodeSearchResult image(String image) {
    this.image = image;
    return this;
  }

  /**
   * Image url for this episode. If an episode doesn&#39;t have its own image, then this field would be the url of the podcast artwork image. If you are using PRO/ENTERPRISE plan, then it&#39;s a high resolution image (1400x1400). If you are using FREE plan, then it&#39;s the same as **thumbnail**, low resolution image (300x300). 
   * @return image
   */
  @javax.annotation.Nullable
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public EpisodeSearchResult itunesId(Integer itunesId) {
    this.itunesId = itunesId;
    return this;
  }

  /**
   * iTunes id for this podcast.
   * @return itunesId
   */
  @javax.annotation.Nullable
  public Integer getItunesId() {
    return itunesId;
  }

  public void setItunesId(Integer itunesId) {
    this.itunesId = itunesId;
  }


  public EpisodeSearchResult link(String link) {
    this.link = link;
    return this;
  }

  /**
   * Web link of this episode.
   * @return link
   */
  @javax.annotation.Nullable
  public String getLink() {
    return link;
  }

  public void setLink(String link) {
    this.link = link;
  }


  public EpisodeSearchResult listennotesUrl(String listennotesUrl) {
    this.listennotesUrl = listennotesUrl;
    return this;
  }

  /**
   * The url of this episode on [ListenNotes.com](https://www.ListenNotes.com).
   * @return listennotesUrl
   */
  @javax.annotation.Nullable
  public String getListennotesUrl() {
    return listennotesUrl;
  }

  public void setListennotesUrl(String listennotesUrl) {
    this.listennotesUrl = listennotesUrl;
  }


  public EpisodeSearchResult podcast(EpisodeSearchResultPodcast podcast) {
    this.podcast = podcast;
    return this;
  }

  /**
   * Get podcast
   * @return podcast
   */
  @javax.annotation.Nullable
  public EpisodeSearchResultPodcast getPodcast() {
    return podcast;
  }

  public void setPodcast(EpisodeSearchResultPodcast podcast) {
    this.podcast = podcast;
  }


  public EpisodeSearchResult pubDateMs(Integer pubDateMs) {
    this.pubDateMs = pubDateMs;
    return this;
  }

  /**
   * Published date for this episode. In millisecond.
   * @return pubDateMs
   */
  @javax.annotation.Nullable
  public Integer getPubDateMs() {
    return pubDateMs;
  }

  public void setPubDateMs(Integer pubDateMs) {
    this.pubDateMs = pubDateMs;
  }


  public EpisodeSearchResult rss(String rss) {
    this.rss = rss;
    return this;
  }

  /**
   * RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan.
   * @return rss
   */
  @javax.annotation.Nullable
  public String getRss() {
    return rss;
  }

  public void setRss(String rss) {
    this.rss = rss;
  }


  public EpisodeSearchResult thumbnail(String thumbnail) {
    this.thumbnail = thumbnail;
    return this;
  }

  /**
   * Thumbnail image (300x300) url for this episode. If an episode doesn&#39;t have its own image, then this field would be the url of the podcast artwork thumbnail image. 
   * @return thumbnail
   */
  @javax.annotation.Nullable
  public String getThumbnail() {
    return thumbnail;
  }

  public void setThumbnail(String thumbnail) {
    this.thumbnail = thumbnail;
  }


  public EpisodeSearchResult titleHighlighted(String titleHighlighted) {
    this.titleHighlighted = titleHighlighted;
    return this;
  }

  /**
   * Highlighted segment of this episode&#39;s title
   * @return titleHighlighted
   */
  @javax.annotation.Nullable
  public String getTitleHighlighted() {
    return titleHighlighted;
  }

  public void setTitleHighlighted(String titleHighlighted) {
    this.titleHighlighted = titleHighlighted;
  }


  public EpisodeSearchResult titleOriginal(String titleOriginal) {
    this.titleOriginal = titleOriginal;
    return this;
  }

  /**
   * Plain text of this episode&#39; title
   * @return titleOriginal
   */
  @javax.annotation.Nullable
  public String getTitleOriginal() {
    return titleOriginal;
  }

  public void setTitleOriginal(String titleOriginal) {
    this.titleOriginal = titleOriginal;
  }


  public EpisodeSearchResult transcriptsHighlighted(List<String> transcriptsHighlighted) {
    this.transcriptsHighlighted = transcriptsHighlighted;
    return this;
  }

  public EpisodeSearchResult addTranscriptsHighlightedItem(String transcriptsHighlightedItem) {
    if (this.transcriptsHighlighted == null) {
      this.transcriptsHighlighted = new ArrayList<>();
    }
    this.transcriptsHighlighted.add(transcriptsHighlightedItem);
    return this;
  }

  /**
   * Up to 2 highlighted segments of the audio transcript of this episode.
   * @return transcriptsHighlighted
   */
  @javax.annotation.Nullable
  public List<String> getTranscriptsHighlighted() {
    return transcriptsHighlighted;
  }

  public void setTranscriptsHighlighted(List<String> transcriptsHighlighted) {
    this.transcriptsHighlighted = transcriptsHighlighted;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EpisodeSearchResult episodeSearchResult = (EpisodeSearchResult) o;
    return Objects.equals(this.audio, episodeSearchResult.audio) &&
        Objects.equals(this.audioLengthSec, episodeSearchResult.audioLengthSec) &&
        Objects.equals(this.descriptionHighlighted, episodeSearchResult.descriptionHighlighted) &&
        Objects.equals(this.descriptionOriginal, episodeSearchResult.descriptionOriginal) &&
        Objects.equals(this.explicitContent, episodeSearchResult.explicitContent) &&
        Objects.equals(this.id, episodeSearchResult.id) &&
        Objects.equals(this.image, episodeSearchResult.image) &&
        Objects.equals(this.itunesId, episodeSearchResult.itunesId) &&
        Objects.equals(this.link, episodeSearchResult.link) &&
        Objects.equals(this.listennotesUrl, episodeSearchResult.listennotesUrl) &&
        Objects.equals(this.podcast, episodeSearchResult.podcast) &&
        Objects.equals(this.pubDateMs, episodeSearchResult.pubDateMs) &&
        Objects.equals(this.rss, episodeSearchResult.rss) &&
        Objects.equals(this.thumbnail, episodeSearchResult.thumbnail) &&
        Objects.equals(this.titleHighlighted, episodeSearchResult.titleHighlighted) &&
        Objects.equals(this.titleOriginal, episodeSearchResult.titleOriginal) &&
        Objects.equals(this.transcriptsHighlighted, episodeSearchResult.transcriptsHighlighted);
  }

  @Override
  public int hashCode() {
    return Objects.hash(audio, audioLengthSec, descriptionHighlighted, descriptionOriginal, explicitContent, id, image, itunesId, link, listennotesUrl, podcast, pubDateMs, rss, thumbnail, titleHighlighted, titleOriginal, transcriptsHighlighted);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EpisodeSearchResult {\n");
    sb.append("    audio: ").append(toIndentedString(audio)).append("\n");
    sb.append("    audioLengthSec: ").append(toIndentedString(audioLengthSec)).append("\n");
    sb.append("    descriptionHighlighted: ").append(toIndentedString(descriptionHighlighted)).append("\n");
    sb.append("    descriptionOriginal: ").append(toIndentedString(descriptionOriginal)).append("\n");
    sb.append("    explicitContent: ").append(toIndentedString(explicitContent)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    itunesId: ").append(toIndentedString(itunesId)).append("\n");
    sb.append("    link: ").append(toIndentedString(link)).append("\n");
    sb.append("    listennotesUrl: ").append(toIndentedString(listennotesUrl)).append("\n");
    sb.append("    podcast: ").append(toIndentedString(podcast)).append("\n");
    sb.append("    pubDateMs: ").append(toIndentedString(pubDateMs)).append("\n");
    sb.append("    rss: ").append(toIndentedString(rss)).append("\n");
    sb.append("    thumbnail: ").append(toIndentedString(thumbnail)).append("\n");
    sb.append("    titleHighlighted: ").append(toIndentedString(titleHighlighted)).append("\n");
    sb.append("    titleOriginal: ").append(toIndentedString(titleOriginal)).append("\n");
    sb.append("    transcriptsHighlighted: ").append(toIndentedString(transcriptsHighlighted)).append("\n");
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
    openapiFields.add("audio");
    openapiFields.add("audio_length_sec");
    openapiFields.add("description_highlighted");
    openapiFields.add("description_original");
    openapiFields.add("explicit_content");
    openapiFields.add("id");
    openapiFields.add("image");
    openapiFields.add("itunes_id");
    openapiFields.add("link");
    openapiFields.add("listennotes_url");
    openapiFields.add("podcast");
    openapiFields.add("pub_date_ms");
    openapiFields.add("rss");
    openapiFields.add("thumbnail");
    openapiFields.add("title_highlighted");
    openapiFields.add("title_original");
    openapiFields.add("transcripts_highlighted");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EpisodeSearchResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EpisodeSearchResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EpisodeSearchResult is not found in the empty JSON string", EpisodeSearchResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EpisodeSearchResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EpisodeSearchResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("audio") != null && !jsonObj.get("audio").isJsonNull()) && !jsonObj.get("audio").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `audio` to be a primitive type in the JSON string but got `%s`", jsonObj.get("audio").toString()));
      }
      if ((jsonObj.get("description_highlighted") != null && !jsonObj.get("description_highlighted").isJsonNull()) && !jsonObj.get("description_highlighted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description_highlighted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description_highlighted").toString()));
      }
      if ((jsonObj.get("description_original") != null && !jsonObj.get("description_original").isJsonNull()) && !jsonObj.get("description_original").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description_original` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description_original").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) && !jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if ((jsonObj.get("link") != null && !jsonObj.get("link").isJsonNull()) && !jsonObj.get("link").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `link` to be a primitive type in the JSON string but got `%s`", jsonObj.get("link").toString()));
      }
      if ((jsonObj.get("listennotes_url") != null && !jsonObj.get("listennotes_url").isJsonNull()) && !jsonObj.get("listennotes_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `listennotes_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("listennotes_url").toString()));
      }
      // validate the optional field `podcast`
      if (jsonObj.get("podcast") != null && !jsonObj.get("podcast").isJsonNull()) {
        EpisodeSearchResultPodcast.validateJsonElement(jsonObj.get("podcast"));
      }
      if ((jsonObj.get("rss") != null && !jsonObj.get("rss").isJsonNull()) && !jsonObj.get("rss").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rss` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rss").toString()));
      }
      if ((jsonObj.get("thumbnail") != null && !jsonObj.get("thumbnail").isJsonNull()) && !jsonObj.get("thumbnail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `thumbnail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("thumbnail").toString()));
      }
      if ((jsonObj.get("title_highlighted") != null && !jsonObj.get("title_highlighted").isJsonNull()) && !jsonObj.get("title_highlighted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title_highlighted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title_highlighted").toString()));
      }
      if ((jsonObj.get("title_original") != null && !jsonObj.get("title_original").isJsonNull()) && !jsonObj.get("title_original").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title_original` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title_original").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("transcripts_highlighted") != null && !jsonObj.get("transcripts_highlighted").isJsonNull() && !jsonObj.get("transcripts_highlighted").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `transcripts_highlighted` to be an array in the JSON string but got `%s`", jsonObj.get("transcripts_highlighted").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EpisodeSearchResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EpisodeSearchResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EpisodeSearchResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EpisodeSearchResult.class));

       return (TypeAdapter<T>) new TypeAdapter<EpisodeSearchResult>() {
           @Override
           public void write(JsonWriter out, EpisodeSearchResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EpisodeSearchResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EpisodeSearchResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EpisodeSearchResult
   * @throws IOException if the JSON string is invalid with respect to EpisodeSearchResult
   */
  public static EpisodeSearchResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EpisodeSearchResult.class);
  }

  /**
   * Convert an instance of EpisodeSearchResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

