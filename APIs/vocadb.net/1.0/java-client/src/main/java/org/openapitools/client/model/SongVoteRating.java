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
 * Gets or Sets SongVoteRating
 */
@JsonAdapter(SongVoteRating.Adapter.class)
public enum SongVoteRating {
  
  NOTHING("Nothing"),
  
  DISLIKE("Dislike"),
  
  LIKE("Like"),
  
  FAVORITE("Favorite");

  private String value;

  SongVoteRating(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static SongVoteRating fromValue(String value) {
    for (SongVoteRating b : SongVoteRating.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<SongVoteRating> {
    @Override
    public void write(final JsonWriter jsonWriter, final SongVoteRating enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public SongVoteRating read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return SongVoteRating.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    SongVoteRating.fromValue(value);
  }
}

