/*
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
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
 * option specifying a group of fares, which may be valid under certain conditons Can be used to specify special fare discount for a passenger 
 */
@JsonAdapter(TravelerPricingFareOption.Adapter.class)
public enum TravelerPricingFareOption {
  
  STANDARD("STANDARD"),
  
  INCLUSIVE_TOUR("INCLUSIVE_TOUR"),
  
  SPANISH_MELILLA_RESIDENT("SPANISH_MELILLA_RESIDENT"),
  
  SPANISH_CEUTA_RESIDENT("SPANISH_CEUTA_RESIDENT"),
  
  SPANISH_CANARY_RESIDENT("SPANISH_CANARY_RESIDENT"),
  
  SPANISH_BALEARIC_RESIDENT("SPANISH_BALEARIC_RESIDENT"),
  
  AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS("AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS"),
  
  AIR_FRANCE_DOM_DISCOUNT_PASS("AIR_FRANCE_DOM_DISCOUNT_PASS"),
  
  AIR_FRANCE_COMBINED_DISCOUNT_PASS("AIR_FRANCE_COMBINED_DISCOUNT_PASS"),
  
  AIR_FRANCE_FAMILY("AIR_FRANCE_FAMILY"),
  
  ADULT_WITH_COMPANION("ADULT_WITH_COMPANION"),
  
  COMPANION("COMPANION");

  private String value;

  TravelerPricingFareOption(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static TravelerPricingFareOption fromValue(String value) {
    for (TravelerPricingFareOption b : TravelerPricingFareOption.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<TravelerPricingFareOption> {
    @Override
    public void write(final JsonWriter jsonWriter, final TravelerPricingFareOption enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public TravelerPricingFareOption read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return TravelerPricingFareOption.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    TravelerPricingFareOption.fromValue(value);
  }
}

