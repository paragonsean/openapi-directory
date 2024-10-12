/*
 * Mixed Reality
 * Mixed Reality Resource Provider Proxy API
 *
 * The version of the OpenAPI document: 2019-12-02-preview
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
 * reason of name unavailable.
 */
@JsonAdapter(NameUnavailableReason.Adapter.class)
public enum NameUnavailableReason {
  
  INVALID("Invalid"),
  
  ALREADY_EXISTS("AlreadyExists");

  private String value;

  NameUnavailableReason(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static NameUnavailableReason fromValue(String value) {
    for (NameUnavailableReason b : NameUnavailableReason.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<NameUnavailableReason> {
    @Override
    public void write(final JsonWriter jsonWriter, final NameUnavailableReason enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public NameUnavailableReason read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return NameUnavailableReason.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    NameUnavailableReason.fromValue(value);
  }
}

