/*
 * Hubhopper Partner Integration API(s) - Production
 * This is an interactive document explaining the API(s) that could be used to fetch data from [Hubhopper](https://hubhopper.com). Use the api key provided to authorize `x-api-key` and test the API(s). The output data models are also available for reference.
 *
 * The version of the OpenAPI document: v5
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
import org.openapitools.client.model.PodcastEpisodeListEpisodesItemPlay;

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
 * PodcastEpisodeListEpisodesItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:08.334207-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PodcastEpisodeListEpisodesItem {
  public static final String SERIALIZED_NAME_AUTHOR = "author";
  @SerializedName(SERIALIZED_NAME_AUTHOR)
  private String author;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EPISODE_ID = "episodeId";
  @SerializedName(SERIALIZED_NAME_EPISODE_ID)
  private Integer episodeId;

  public static final String SERIALIZED_NAME_EPISODE_URL = "episodeUrl";
  @SerializedName(SERIALIZED_NAME_EPISODE_URL)
  private String episodeUrl;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_IS_NEW = "isNew";
  @SerializedName(SERIALIZED_NAME_IS_NEW)
  private Boolean isNew;

  public static final String SERIALIZED_NAME_PLAY = "play";
  @SerializedName(SERIALIZED_NAME_PLAY)
  private PodcastEpisodeListEpisodesItemPlay play;

  public static final String SERIALIZED_NAME_PODCAST_ID = "podcastId";
  @SerializedName(SERIALIZED_NAME_PODCAST_ID)
  private Integer podcastId;

  public static final String SERIALIZED_NAME_PODCAST_URL = "podcastUrl";
  @SerializedName(SERIALIZED_NAME_PODCAST_URL)
  private String podcastUrl;

  public static final String SERIALIZED_NAME_PUBLISH_TIME = "publishTime";
  @SerializedName(SERIALIZED_NAME_PUBLISH_TIME)
  private String publishTime;

  public static final String SERIALIZED_NAME_PUBLISHED_ON = "publishedOn";
  @SerializedName(SERIALIZED_NAME_PUBLISHED_ON)
  private Integer publishedOn;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public PodcastEpisodeListEpisodesItem() {
  }

  public PodcastEpisodeListEpisodesItem author(String author) {
    this.author = author;
    return this;
  }

  /**
   * Get author
   * @return author
   */
  @javax.annotation.Nullable
  public String getAuthor() {
    return author;
  }

  public void setAuthor(String author) {
    this.author = author;
  }


  public PodcastEpisodeListEpisodesItem description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public PodcastEpisodeListEpisodesItem episodeId(Integer episodeId) {
    this.episodeId = episodeId;
    return this;
  }

  /**
   * Get episodeId
   * @return episodeId
   */
  @javax.annotation.Nullable
  public Integer getEpisodeId() {
    return episodeId;
  }

  public void setEpisodeId(Integer episodeId) {
    this.episodeId = episodeId;
  }


  public PodcastEpisodeListEpisodesItem episodeUrl(String episodeUrl) {
    this.episodeUrl = episodeUrl;
    return this;
  }

  /**
   * Get episodeUrl
   * @return episodeUrl
   */
  @javax.annotation.Nullable
  public String getEpisodeUrl() {
    return episodeUrl;
  }

  public void setEpisodeUrl(String episodeUrl) {
    this.episodeUrl = episodeUrl;
  }


  public PodcastEpisodeListEpisodesItem image(String image) {
    this.image = image;
    return this;
  }

  /**
   * Get image
   * @return image
   */
  @javax.annotation.Nullable
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public PodcastEpisodeListEpisodesItem isNew(Boolean isNew) {
    this.isNew = isNew;
    return this;
  }

  /**
   * Get isNew
   * @return isNew
   */
  @javax.annotation.Nullable
  public Boolean getIsNew() {
    return isNew;
  }

  public void setIsNew(Boolean isNew) {
    this.isNew = isNew;
  }


  public PodcastEpisodeListEpisodesItem play(PodcastEpisodeListEpisodesItemPlay play) {
    this.play = play;
    return this;
  }

  /**
   * Get play
   * @return play
   */
  @javax.annotation.Nullable
  public PodcastEpisodeListEpisodesItemPlay getPlay() {
    return play;
  }

  public void setPlay(PodcastEpisodeListEpisodesItemPlay play) {
    this.play = play;
  }


  public PodcastEpisodeListEpisodesItem podcastId(Integer podcastId) {
    this.podcastId = podcastId;
    return this;
  }

  /**
   * Get podcastId
   * @return podcastId
   */
  @javax.annotation.Nullable
  public Integer getPodcastId() {
    return podcastId;
  }

  public void setPodcastId(Integer podcastId) {
    this.podcastId = podcastId;
  }


  public PodcastEpisodeListEpisodesItem podcastUrl(String podcastUrl) {
    this.podcastUrl = podcastUrl;
    return this;
  }

  /**
   * Get podcastUrl
   * @return podcastUrl
   */
  @javax.annotation.Nullable
  public String getPodcastUrl() {
    return podcastUrl;
  }

  public void setPodcastUrl(String podcastUrl) {
    this.podcastUrl = podcastUrl;
  }


  public PodcastEpisodeListEpisodesItem publishTime(String publishTime) {
    this.publishTime = publishTime;
    return this;
  }

  /**
   * Get publishTime
   * @return publishTime
   */
  @javax.annotation.Nullable
  public String getPublishTime() {
    return publishTime;
  }

  public void setPublishTime(String publishTime) {
    this.publishTime = publishTime;
  }


  public PodcastEpisodeListEpisodesItem publishedOn(Integer publishedOn) {
    this.publishedOn = publishedOn;
    return this;
  }

  /**
   * Get publishedOn
   * @return publishedOn
   */
  @javax.annotation.Nullable
  public Integer getPublishedOn() {
    return publishedOn;
  }

  public void setPublishedOn(Integer publishedOn) {
    this.publishedOn = publishedOn;
  }


  public PodcastEpisodeListEpisodesItem title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PodcastEpisodeListEpisodesItem podcastEpisodeListEpisodesItem = (PodcastEpisodeListEpisodesItem) o;
    return Objects.equals(this.author, podcastEpisodeListEpisodesItem.author) &&
        Objects.equals(this.description, podcastEpisodeListEpisodesItem.description) &&
        Objects.equals(this.episodeId, podcastEpisodeListEpisodesItem.episodeId) &&
        Objects.equals(this.episodeUrl, podcastEpisodeListEpisodesItem.episodeUrl) &&
        Objects.equals(this.image, podcastEpisodeListEpisodesItem.image) &&
        Objects.equals(this.isNew, podcastEpisodeListEpisodesItem.isNew) &&
        Objects.equals(this.play, podcastEpisodeListEpisodesItem.play) &&
        Objects.equals(this.podcastId, podcastEpisodeListEpisodesItem.podcastId) &&
        Objects.equals(this.podcastUrl, podcastEpisodeListEpisodesItem.podcastUrl) &&
        Objects.equals(this.publishTime, podcastEpisodeListEpisodesItem.publishTime) &&
        Objects.equals(this.publishedOn, podcastEpisodeListEpisodesItem.publishedOn) &&
        Objects.equals(this.title, podcastEpisodeListEpisodesItem.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(author, description, episodeId, episodeUrl, image, isNew, play, podcastId, podcastUrl, publishTime, publishedOn, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PodcastEpisodeListEpisodesItem {\n");
    sb.append("    author: ").append(toIndentedString(author)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    episodeId: ").append(toIndentedString(episodeId)).append("\n");
    sb.append("    episodeUrl: ").append(toIndentedString(episodeUrl)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    isNew: ").append(toIndentedString(isNew)).append("\n");
    sb.append("    play: ").append(toIndentedString(play)).append("\n");
    sb.append("    podcastId: ").append(toIndentedString(podcastId)).append("\n");
    sb.append("    podcastUrl: ").append(toIndentedString(podcastUrl)).append("\n");
    sb.append("    publishTime: ").append(toIndentedString(publishTime)).append("\n");
    sb.append("    publishedOn: ").append(toIndentedString(publishedOn)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("author");
    openapiFields.add("description");
    openapiFields.add("episodeId");
    openapiFields.add("episodeUrl");
    openapiFields.add("image");
    openapiFields.add("isNew");
    openapiFields.add("play");
    openapiFields.add("podcastId");
    openapiFields.add("podcastUrl");
    openapiFields.add("publishTime");
    openapiFields.add("publishedOn");
    openapiFields.add("title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PodcastEpisodeListEpisodesItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PodcastEpisodeListEpisodesItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PodcastEpisodeListEpisodesItem is not found in the empty JSON string", PodcastEpisodeListEpisodesItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PodcastEpisodeListEpisodesItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PodcastEpisodeListEpisodesItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("author") != null && !jsonObj.get("author").isJsonNull()) && !jsonObj.get("author").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `author` to be a primitive type in the JSON string but got `%s`", jsonObj.get("author").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("episodeUrl") != null && !jsonObj.get("episodeUrl").isJsonNull()) && !jsonObj.get("episodeUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `episodeUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("episodeUrl").toString()));
      }
      if ((jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) && !jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      // validate the optional field `play`
      if (jsonObj.get("play") != null && !jsonObj.get("play").isJsonNull()) {
        PodcastEpisodeListEpisodesItemPlay.validateJsonElement(jsonObj.get("play"));
      }
      if ((jsonObj.get("podcastUrl") != null && !jsonObj.get("podcastUrl").isJsonNull()) && !jsonObj.get("podcastUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `podcastUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("podcastUrl").toString()));
      }
      if ((jsonObj.get("publishTime") != null && !jsonObj.get("publishTime").isJsonNull()) && !jsonObj.get("publishTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publishTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publishTime").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PodcastEpisodeListEpisodesItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PodcastEpisodeListEpisodesItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PodcastEpisodeListEpisodesItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PodcastEpisodeListEpisodesItem.class));

       return (TypeAdapter<T>) new TypeAdapter<PodcastEpisodeListEpisodesItem>() {
           @Override
           public void write(JsonWriter out, PodcastEpisodeListEpisodesItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PodcastEpisodeListEpisodesItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PodcastEpisodeListEpisodesItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PodcastEpisodeListEpisodesItem
   * @throws IOException if the JSON string is invalid with respect to PodcastEpisodeListEpisodesItem
   */
  public static PodcastEpisodeListEpisodesItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PodcastEpisodeListEpisodesItem.class);
  }

  /**
   * Convert an instance of PodcastEpisodeListEpisodesItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

