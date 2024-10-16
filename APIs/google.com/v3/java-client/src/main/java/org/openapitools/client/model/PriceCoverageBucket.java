/*
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.Arrays;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * Coverage stats for one combination of advance booking window and length of stay.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:52.320664-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PriceCoverageBucket {
  /**
   * Advance booking window range.
   */
  @JsonAdapter(AdvanceBookingWindowRangeEnum.Adapter.class)
  public enum AdvanceBookingWindowRangeEnum {
    ADVANCE_BOOKING_WINDOW_RANGE_UNSPECIFIED("ADVANCE_BOOKING_WINDOW_RANGE_UNSPECIFIED"),
    
    ADVANCE_BOOKING_WINDOW_RANGE_UNKNOWN("ADVANCE_BOOKING_WINDOW_RANGE_UNKNOWN"),
    
    DAYS_0_TO_30("DAYS_0_TO_30"),
    
    DAYS_31_TO_60("DAYS_31_TO_60"),
    
    DAYS_61_TO_90("DAYS_61_TO_90"),
    
    DAYS_91_TO_120("DAYS_91_TO_120"),
    
    DAYS_121_TO_150("DAYS_121_TO_150"),
    
    DAYS_151_TO_180("DAYS_151_TO_180"),
    
    DAYS_181_TO_210("DAYS_181_TO_210"),
    
    DAYS_211_TO_240("DAYS_211_TO_240"),
    
    DAYS_241_TO_270("DAYS_241_TO_270"),
    
    DAYS_271_TO_300("DAYS_271_TO_300"),
    
    DAYS_301_TO_330("DAYS_301_TO_330");

    private String value;

    AdvanceBookingWindowRangeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AdvanceBookingWindowRangeEnum fromValue(String value) {
      for (AdvanceBookingWindowRangeEnum b : AdvanceBookingWindowRangeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AdvanceBookingWindowRangeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AdvanceBookingWindowRangeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AdvanceBookingWindowRangeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AdvanceBookingWindowRangeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AdvanceBookingWindowRangeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ADVANCE_BOOKING_WINDOW_RANGE = "advanceBookingWindowRange";
  @SerializedName(SERIALIZED_NAME_ADVANCE_BOOKING_WINDOW_RANGE)
  private AdvanceBookingWindowRangeEnum advanceBookingWindowRange;

  public static final String SERIALIZED_NAME_AVAILABLE_PRICE_COUNT = "availablePriceCount";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_PRICE_COUNT)
  private String availablePriceCount;

  /**
   * Length of stay range.
   */
  @JsonAdapter(LengthOfStayRangeEnum.Adapter.class)
  public enum LengthOfStayRangeEnum {
    RANGE_UNSPECIFIED("LENGTH_OF_STAY_RANGE_UNSPECIFIED"),
    
    RANGE_UNKNOWN("LENGTH_OF_STAY_RANGE_UNKNOWN"),
    
    _1_TO_7("LENGTH_OF_STAY_1_TO_7"),
    
    _8_TO_14("LENGTH_OF_STAY_8_TO_14"),
    
    _15_TO_30("LENGTH_OF_STAY_15_TO_30");

    private String value;

    LengthOfStayRangeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static LengthOfStayRangeEnum fromValue(String value) {
      for (LengthOfStayRangeEnum b : LengthOfStayRangeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<LengthOfStayRangeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final LengthOfStayRangeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public LengthOfStayRangeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return LengthOfStayRangeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      LengthOfStayRangeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_LENGTH_OF_STAY_RANGE = "lengthOfStayRange";
  @SerializedName(SERIALIZED_NAME_LENGTH_OF_STAY_RANGE)
  private LengthOfStayRangeEnum lengthOfStayRange;

  public static final String SERIALIZED_NAME_PRICE_COVERAGE_PERCENT = "priceCoveragePercent";
  @SerializedName(SERIALIZED_NAME_PRICE_COVERAGE_PERCENT)
  private Double priceCoveragePercent;

  public PriceCoverageBucket() {
  }

  public PriceCoverageBucket advanceBookingWindowRange(AdvanceBookingWindowRangeEnum advanceBookingWindowRange) {
    this.advanceBookingWindowRange = advanceBookingWindowRange;
    return this;
  }

  /**
   * Advance booking window range.
   * @return advanceBookingWindowRange
   */
  @javax.annotation.Nullable
  public AdvanceBookingWindowRangeEnum getAdvanceBookingWindowRange() {
    return advanceBookingWindowRange;
  }

  public void setAdvanceBookingWindowRange(AdvanceBookingWindowRangeEnum advanceBookingWindowRange) {
    this.advanceBookingWindowRange = advanceBookingWindowRange;
  }


  public PriceCoverageBucket availablePriceCount(String availablePriceCount) {
    this.availablePriceCount = availablePriceCount;
    return this;
  }

  /**
   * Number of prices for this advance booking window bucket and length of stay bucket.
   * @return availablePriceCount
   */
  @javax.annotation.Nullable
  public String getAvailablePriceCount() {
    return availablePriceCount;
  }

  public void setAvailablePriceCount(String availablePriceCount) {
    this.availablePriceCount = availablePriceCount;
  }


  public PriceCoverageBucket lengthOfStayRange(LengthOfStayRangeEnum lengthOfStayRange) {
    this.lengthOfStayRange = lengthOfStayRange;
    return this;
  }

  /**
   * Length of stay range.
   * @return lengthOfStayRange
   */
  @javax.annotation.Nullable
  public LengthOfStayRangeEnum getLengthOfStayRange() {
    return lengthOfStayRange;
  }

  public void setLengthOfStayRange(LengthOfStayRangeEnum lengthOfStayRange) {
    this.lengthOfStayRange = lengthOfStayRange;
  }


  public PriceCoverageBucket priceCoveragePercent(Double priceCoveragePercent) {
    this.priceCoveragePercent = priceCoveragePercent;
    return this;
  }

  /**
   * The percent of itineraries for which you have coverage for this advance booking window bucket and length of stay bucket.
   * @return priceCoveragePercent
   */
  @javax.annotation.Nullable
  public Double getPriceCoveragePercent() {
    return priceCoveragePercent;
  }

  public void setPriceCoveragePercent(Double priceCoveragePercent) {
    this.priceCoveragePercent = priceCoveragePercent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PriceCoverageBucket priceCoverageBucket = (PriceCoverageBucket) o;
    return Objects.equals(this.advanceBookingWindowRange, priceCoverageBucket.advanceBookingWindowRange) &&
        Objects.equals(this.availablePriceCount, priceCoverageBucket.availablePriceCount) &&
        Objects.equals(this.lengthOfStayRange, priceCoverageBucket.lengthOfStayRange) &&
        Objects.equals(this.priceCoveragePercent, priceCoverageBucket.priceCoveragePercent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(advanceBookingWindowRange, availablePriceCount, lengthOfStayRange, priceCoveragePercent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PriceCoverageBucket {\n");
    sb.append("    advanceBookingWindowRange: ").append(toIndentedString(advanceBookingWindowRange)).append("\n");
    sb.append("    availablePriceCount: ").append(toIndentedString(availablePriceCount)).append("\n");
    sb.append("    lengthOfStayRange: ").append(toIndentedString(lengthOfStayRange)).append("\n");
    sb.append("    priceCoveragePercent: ").append(toIndentedString(priceCoveragePercent)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("advanceBookingWindowRange");
    openapiFields.add("availablePriceCount");
    openapiFields.add("lengthOfStayRange");
    openapiFields.add("priceCoveragePercent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PriceCoverageBucket
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PriceCoverageBucket.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PriceCoverageBucket is not found in the empty JSON string", PriceCoverageBucket.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PriceCoverageBucket.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PriceCoverageBucket` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("advanceBookingWindowRange") != null && !jsonObj.get("advanceBookingWindowRange").isJsonNull()) && !jsonObj.get("advanceBookingWindowRange").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `advanceBookingWindowRange` to be a primitive type in the JSON string but got `%s`", jsonObj.get("advanceBookingWindowRange").toString()));
      }
      // validate the optional field `advanceBookingWindowRange`
      if (jsonObj.get("advanceBookingWindowRange") != null && !jsonObj.get("advanceBookingWindowRange").isJsonNull()) {
        AdvanceBookingWindowRangeEnum.validateJsonElement(jsonObj.get("advanceBookingWindowRange"));
      }
      if ((jsonObj.get("availablePriceCount") != null && !jsonObj.get("availablePriceCount").isJsonNull()) && !jsonObj.get("availablePriceCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `availablePriceCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("availablePriceCount").toString()));
      }
      if ((jsonObj.get("lengthOfStayRange") != null && !jsonObj.get("lengthOfStayRange").isJsonNull()) && !jsonObj.get("lengthOfStayRange").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lengthOfStayRange` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lengthOfStayRange").toString()));
      }
      // validate the optional field `lengthOfStayRange`
      if (jsonObj.get("lengthOfStayRange") != null && !jsonObj.get("lengthOfStayRange").isJsonNull()) {
        LengthOfStayRangeEnum.validateJsonElement(jsonObj.get("lengthOfStayRange"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PriceCoverageBucket.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PriceCoverageBucket' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PriceCoverageBucket> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PriceCoverageBucket.class));

       return (TypeAdapter<T>) new TypeAdapter<PriceCoverageBucket>() {
           @Override
           public void write(JsonWriter out, PriceCoverageBucket value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PriceCoverageBucket read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PriceCoverageBucket given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PriceCoverageBucket
   * @throws IOException if the JSON string is invalid with respect to PriceCoverageBucket
   */
  public static PriceCoverageBucket fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PriceCoverageBucket.class);
  }

  /**
   * Convert an instance of PriceCoverageBucket to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

