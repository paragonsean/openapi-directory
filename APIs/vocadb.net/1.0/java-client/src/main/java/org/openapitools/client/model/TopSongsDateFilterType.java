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
 * Gets or Sets TopSongsDateFilterType
 */
@JsonAdapter(TopSongsDateFilterType.Adapter.class)
public enum TopSongsDateFilterType {
  
  CREATE_DATE("CreateDate"),
  
  PUBLISH_DATE("PublishDate"),
  
  POPULARITY("Popularity");

  private String value;

  TopSongsDateFilterType(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static TopSongsDateFilterType fromValue(String value) {
    for (TopSongsDateFilterType b : TopSongsDateFilterType.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<TopSongsDateFilterType> {
    @Override
    public void write(final JsonWriter jsonWriter, final TopSongsDateFilterType enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public TopSongsDateFilterType read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return TopSongsDateFilterType.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    TopSongsDateFilterType.fromValue(value);
  }
}

