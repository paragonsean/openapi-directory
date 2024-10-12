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
 * Gets or Sets ArtistType
 */
@JsonAdapter(ArtistType.Adapter.class)
public enum ArtistType {
  
  UNKNOWN("Unknown"),
  
  CIRCLE("Circle"),
  
  LABEL("Label"),
  
  PRODUCER("Producer"),
  
  ANIMATOR("Animator"),
  
  ILLUSTRATOR("Illustrator"),
  
  LYRICIST("Lyricist"),
  
  VOCALOID("Vocaloid"),
  
  UTAU("UTAU"),
  
  CE_VIO("CeVIO"),
  
  OTHER_VOICE_SYNTHESIZER("OtherVoiceSynthesizer"),
  
  OTHER_VOCALIST("OtherVocalist"),
  
  OTHER_GROUP("OtherGroup"),
  
  OTHER_INDIVIDUAL("OtherIndividual"),
  
  UTAITE("Utaite"),
  
  BAND("Band"),
  
  VOCALIST("Vocalist"),
  
  CHARACTER("Character"),
  
  SYNTHESIZER_V("SynthesizerV"),
  
  COVER_ARTIST("CoverArtist");

  private String value;

  ArtistType(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static ArtistType fromValue(String value) {
    for (ArtistType b : ArtistType.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<ArtistType> {
    @Override
    public void write(final JsonWriter jsonWriter, final ArtistType enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public ArtistType read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return ArtistType.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    ArtistType.fromValue(value);
  }
}

