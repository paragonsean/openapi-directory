/*
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
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
 * traveler type age restrictions : CHILD &lt; 12y, HELD_INFANT &lt; 2y, SEATED_INFANT &lt; 2y, SENIOR &gt;&#x3D;60y 
 */
@JsonAdapter(TravelerType.Adapter.class)
public enum TravelerType {
  
  ADULT("ADULT"),
  
  CHILD("CHILD"),
  
  SENIOR("SENIOR"),
  
  YOUNG("YOUNG"),
  
  HELD_INFANT("HELD_INFANT"),
  
  SEATED_INFANT("SEATED_INFANT"),
  
  STUDENT("STUDENT");

  private String value;

  TravelerType(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static TravelerType fromValue(String value) {
    for (TravelerType b : TravelerType.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<TravelerType> {
    @Override
    public void write(final JsonWriter jsonWriter, final TravelerType enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public TravelerType read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return TravelerType.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    TravelerType.fromValue(value);
  }
}

