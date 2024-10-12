/*
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
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
 * airline remark type
 */
@JsonAdapter(AirlineRemarkType.Adapter.class)
public enum AirlineRemarkType {
  
  OTHER_SERVICE_INFORMATION("OTHER_SERVICE_INFORMATION"),
  
  KEYWORD("KEYWORD"),
  
  OTHER_SERVICE("OTHER_SERVICE"),
  
  CLIENT_ID("CLIENT_ID"),
  
  ADVANCED_TICKET_TIME_LIMIT("ADVANCED_TICKET_TIME_LIMIT");

  private String value;

  AirlineRemarkType(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static AirlineRemarkType fromValue(String value) {
    for (AirlineRemarkType b : AirlineRemarkType.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<AirlineRemarkType> {
    @Override
    public void write(final JsonWriter jsonWriter, final AirlineRemarkType enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public AirlineRemarkType read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return AirlineRemarkType.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    AirlineRemarkType.fromValue(value);
  }
}

