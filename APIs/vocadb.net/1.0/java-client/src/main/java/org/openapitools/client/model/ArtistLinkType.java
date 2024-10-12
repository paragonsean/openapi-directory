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
 * Gets or Sets ArtistLinkType
 */
@JsonAdapter(ArtistLinkType.Adapter.class)
public enum ArtistLinkType {
  
  CHARACTER_DESIGNER("CharacterDesigner"),
  
  GROUP("Group"),
  
  ILLUSTRATOR("Illustrator"),
  
  MANAGER("Manager"),
  
  VOICE_PROVIDER("VoiceProvider");

  private String value;

  ArtistLinkType(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static ArtistLinkType fromValue(String value) {
    for (ArtistLinkType b : ArtistLinkType.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<ArtistLinkType> {
    @Override
    public void write(final JsonWriter jsonWriter, final ArtistLinkType enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public ArtistLinkType read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return ArtistLinkType.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    ArtistLinkType.fromValue(value);
  }
}

