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
 * Gets or Sets VenueOptionalFields
 */
@JsonAdapter(VenueOptionalFields.Adapter.class)
public enum VenueOptionalFields {
  
  NONE("None"),
  
  ADDITIONAL_NAMES("AdditionalNames"),
  
  DESCRIPTION("Description"),
  
  EVENTS("Events"),
  
  NAMES("Names"),
  
  WEB_LINKS("WebLinks");

  private String value;

  VenueOptionalFields(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static VenueOptionalFields fromValue(String value) {
    for (VenueOptionalFields b : VenueOptionalFields.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<VenueOptionalFields> {
    @Override
    public void write(final JsonWriter jsonWriter, final VenueOptionalFields enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public VenueOptionalFields read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return VenueOptionalFields.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    VenueOptionalFields.fromValue(value);
  }
}

