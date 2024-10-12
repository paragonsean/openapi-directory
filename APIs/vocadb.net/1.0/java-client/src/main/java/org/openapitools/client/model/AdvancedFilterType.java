/*
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.annotations.SerializedName;

import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.JsonElement;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * Gets or Sets AdvancedFilterType
 */
@JsonAdapter(AdvancedFilterType.Adapter.class)
public enum AdvancedFilterType {
  
  NOTHING("Nothing"),
  
  ARTIST_TYPE("ArtistType"),
  
  WEB_LINK("WebLink"),
  
  HAS_USER_ACCOUNT("HasUserAccount"),
  
  ROOT_VOICEBANK("RootVoicebank"),
  
  VOICE_PROVIDER("VoiceProvider"),
  
  HAS_STORE_LINK("HasStoreLink"),
  
  HAS_TRACKS("HasTracks"),
  
  NO_COVER_PICTURE("NoCoverPicture"),
  
  HAS_ALBUM("HasAlbum"),
  
  HAS_ORIGINAL_MEDIA("HasOriginalMedia"),
  
  HAS_MEDIA("HasMedia"),
  
  HAS_MULTIPLE_VOICEBANKS("HasMultipleVoicebanks"),
  
  HAS_PUBLISH_DATE("HasPublishDate"),
  
  LYRICS("Lyrics"),
  
  LYRICS_CONTENT("LyricsContent");

  private String value;

  AdvancedFilterType(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static AdvancedFilterType fromValue(String value) {
    for (AdvancedFilterType b : AdvancedFilterType.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<AdvancedFilterType> {
    @Override
    public void write(final JsonWriter jsonWriter, final AdvancedFilterType enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public AdvancedFilterType read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return AdvancedFilterType.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    AdvancedFilterType.fromValue(value);
  }
}

