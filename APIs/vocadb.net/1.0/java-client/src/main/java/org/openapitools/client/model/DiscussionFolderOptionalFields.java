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
 * Gets or Sets DiscussionFolderOptionalFields
 */
@JsonAdapter(DiscussionFolderOptionalFields.Adapter.class)
public enum DiscussionFolderOptionalFields {
  
  NONE("None"),
  
  LAST_TOPIC("LastTopic"),
  
  TOPIC_COUNT("TopicCount");

  private String value;

  DiscussionFolderOptionalFields(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static DiscussionFolderOptionalFields fromValue(String value) {
    for (DiscussionFolderOptionalFields b : DiscussionFolderOptionalFields.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<DiscussionFolderOptionalFields> {
    @Override
    public void write(final JsonWriter jsonWriter, final DiscussionFolderOptionalFields enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public DiscussionFolderOptionalFields read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return DiscussionFolderOptionalFields.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    DiscussionFolderOptionalFields.fromValue(value);
  }
}

