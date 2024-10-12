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
 * Gets or Sets PurchaseStatuses
 */
@JsonAdapter(PurchaseStatuses.Adapter.class)
public enum PurchaseStatuses {
  
  NOTHING("Nothing"),
  
  WISHLISTED("Wishlisted"),
  
  ORDERED("Ordered"),
  
  OWNED("Owned"),
  
  ALL("All");

  private String value;

  PurchaseStatuses(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static PurchaseStatuses fromValue(String value) {
    for (PurchaseStatuses b : PurchaseStatuses.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<PurchaseStatuses> {
    @Override
    public void write(final JsonWriter jsonWriter, final PurchaseStatuses enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public PurchaseStatuses read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return PurchaseStatuses.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    PurchaseStatuses.fromValue(value);
  }
}

