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
 * Gets or Sets TagSortRule
 */
@JsonAdapter(TagSortRule.Adapter.class)
public enum TagSortRule {
  
  NOTHING("Nothing"),
  
  NAME("Name"),
  
  ADDITION_DATE("AdditionDate"),
  
  USAGE_COUNT("UsageCount");

  private String value;

  TagSortRule(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static TagSortRule fromValue(String value) {
    for (TagSortRule b : TagSortRule.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<TagSortRule> {
    @Override
    public void write(final JsonWriter jsonWriter, final TagSortRule enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public TagSortRule read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return TagSortRule.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    TagSortRule.fromValue(value);
  }
}

