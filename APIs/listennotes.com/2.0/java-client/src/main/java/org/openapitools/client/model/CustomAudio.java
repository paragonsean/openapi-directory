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
 * A custom audio in a playlist, which is a type of playlist item.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:39.439950-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CustomAudio {
  public static final String SERIALIZED_NAME_AUDIO = "audio";
  @SerializedName(SERIALIZED_NAME_AUDIO)
  private String audio;

  public static final String SERIALIZED_NAME_AUDIO_LENGTH_SEC = "audio_length_sec";
  @SerializedName(SERIALIZED_NAME_AUDIO_LENGTH_SEC)
  private Integer audioLengthSec;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_PUB_DATE_MS = "pub_date_ms";
  @SerializedName(SERIALIZED_NAME_PUB_DATE_MS)
  private Integer pubDateMs;

  public static final String SERIALIZED_NAME_THUMBNAIL = "thumbnail";
  @SerializedName(SERIALIZED_NAME_THUMBNAIL)
  private String thumbnail;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public CustomAudio() {
  }

  public CustomAudio audio(String audio) {
    this.audio = audio;
    return this;
  }

  /**
   * Audio url, which can be played directly.
   * @return audio
   */
  @javax.annotation.Nullable
  public String getAudio() {
    return audio;
  }

  public void setAudio(String audio) {
    this.audio = audio;
  }


  public CustomAudio audioLengthSec(Integer audioLengthSec) {
    this.audioLengthSec = audioLengthSec;
    return this;
  }

  /**
   * Audio length in seconds.
   * @return audioLengthSec
   */
  @javax.annotation.Nullable
  public Integer getAudioLengthSec() {
    return audioLengthSec;
  }

  public void setAudioLengthSec(Integer audioLengthSec) {
    this.audioLengthSec = audioLengthSec;
  }


  public CustomAudio image(String image) {
    this.image = image;
    return this;
  }

  /**
   * High resolution image url of this custom audio.
   * @return image
   */
  @javax.annotation.Nullable
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public CustomAudio pubDateMs(Integer pubDateMs) {
    this.pubDateMs = pubDateMs;
    return this;
  }

  /**
   * Published date (in milliseconds) of this custom audio. For now, it&#39;s the same as **added_at_ms** of this playlist item. 
   * @return pubDateMs
   */
  @javax.annotation.Nullable
  public Integer getPubDateMs() {
    return pubDateMs;
  }

  public void setPubDateMs(Integer pubDateMs) {
    this.pubDateMs = pubDateMs;
  }


  public CustomAudio thumbnail(String thumbnail) {
    this.thumbnail = thumbnail;
    return this;
  }

  /**
   * Low resolution image url of this custom audio.
   * @return thumbnail
   */
  @javax.annotation.Nullable
  public String getThumbnail() {
    return thumbnail;
  }

  public void setThumbnail(String thumbnail) {
    this.thumbnail = thumbnail;
  }


  public CustomAudio title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Custom audio title.
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
    CustomAudio customAudio = (CustomAudio) o;
    return Objects.equals(this.audio, customAudio.audio) &&
        Objects.equals(this.audioLengthSec, customAudio.audioLengthSec) &&
        Objects.equals(this.image, customAudio.image) &&
        Objects.equals(this.pubDateMs, customAudio.pubDateMs) &&
        Objects.equals(this.thumbnail, customAudio.thumbnail) &&
        Objects.equals(this.title, customAudio.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(audio, audioLengthSec, image, pubDateMs, thumbnail, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CustomAudio {\n");
    sb.append("    audio: ").append(toIndentedString(audio)).append("\n");
    sb.append("    audioLengthSec: ").append(toIndentedString(audioLengthSec)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    pubDateMs: ").append(toIndentedString(pubDateMs)).append("\n");
    sb.append("    thumbnail: ").append(toIndentedString(thumbnail)).append("\n");
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
    openapiFields.add("audio");
    openapiFields.add("audio_length_sec");
    openapiFields.add("image");
    openapiFields.add("pub_date_ms");
    openapiFields.add("thumbnail");
    openapiFields.add("title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CustomAudio
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CustomAudio.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CustomAudio is not found in the empty JSON string", CustomAudio.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CustomAudio.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CustomAudio` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("audio") != null && !jsonObj.get("audio").isJsonNull()) && !jsonObj.get("audio").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `audio` to be a primitive type in the JSON string but got `%s`", jsonObj.get("audio").toString()));
      }
      if ((jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) && !jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if ((jsonObj.get("thumbnail") != null && !jsonObj.get("thumbnail").isJsonNull()) && !jsonObj.get("thumbnail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `thumbnail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("thumbnail").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CustomAudio.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CustomAudio' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CustomAudio> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CustomAudio.class));

       return (TypeAdapter<T>) new TypeAdapter<CustomAudio>() {
           @Override
           public void write(JsonWriter out, CustomAudio value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CustomAudio read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CustomAudio given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CustomAudio
   * @throws IOException if the JSON string is invalid with respect to CustomAudio
   */
  public static CustomAudio fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CustomAudio.class);
  }

  /**
   * Convert an instance of CustomAudio to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

