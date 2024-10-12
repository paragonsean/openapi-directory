/*
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * PricingOptions
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:43.662685-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PricingOptions {
  /**
   * Gets or Sets fareType
   */
  @JsonAdapter(FareTypeEnum.Adapter.class)
  public enum FareTypeEnum {
    PUBLISHED("PUBLISHED");

    private String value;

    FareTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static FareTypeEnum fromValue(String value) {
      for (FareTypeEnum b : FareTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<FareTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final FareTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public FareTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return FareTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      FareTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_FARE_TYPE = "fareType";
  @SerializedName(SERIALIZED_NAME_FARE_TYPE)
  private List<FareTypeEnum> fareType = new ArrayList<>();

  public static final String SERIALIZED_NAME_INCLUDED_CHECKED_BAGS_ONLY = "includedCheckedBagsOnly";
  @SerializedName(SERIALIZED_NAME_INCLUDED_CHECKED_BAGS_ONLY)
  private Boolean includedCheckedBagsOnly;

  public static final String SERIALIZED_NAME_NO_PENALTY_FARE = "noPenaltyFare";
  @SerializedName(SERIALIZED_NAME_NO_PENALTY_FARE)
  private Boolean noPenaltyFare;

  public static final String SERIALIZED_NAME_NO_RESTRICTION_FARE = "noRestrictionFare";
  @SerializedName(SERIALIZED_NAME_NO_RESTRICTION_FARE)
  private Boolean noRestrictionFare;

  public static final String SERIALIZED_NAME_REFUNDABLE_FARE = "refundableFare";
  @SerializedName(SERIALIZED_NAME_REFUNDABLE_FARE)
  private Boolean refundableFare;

  public PricingOptions() {
  }

  public PricingOptions fareType(List<FareTypeEnum> fareType) {
    this.fareType = fareType;
    return this;
  }

  public PricingOptions addFareTypeItem(FareTypeEnum fareTypeItem) {
    if (this.fareType == null) {
      this.fareType = new ArrayList<>();
    }
    this.fareType.add(fareTypeItem);
    return this;
  }

  /**
   * type of fare of the flight-offer
   * @return fareType
   */
  @javax.annotation.Nullable
  public List<FareTypeEnum> getFareType() {
    return fareType;
  }

  public void setFareType(List<FareTypeEnum> fareType) {
    this.fareType = fareType;
  }


  public PricingOptions includedCheckedBagsOnly(Boolean includedCheckedBagsOnly) {
    this.includedCheckedBagsOnly = includedCheckedBagsOnly;
    return this;
  }

  /**
   * If true, returns the flight-offers with included checked bags only
   * @return includedCheckedBagsOnly
   */
  @javax.annotation.Nullable
  public Boolean getIncludedCheckedBagsOnly() {
    return includedCheckedBagsOnly;
  }

  public void setIncludedCheckedBagsOnly(Boolean includedCheckedBagsOnly) {
    this.includedCheckedBagsOnly = includedCheckedBagsOnly;
  }


  public PricingOptions noPenaltyFare(Boolean noPenaltyFare) {
    this.noPenaltyFare = noPenaltyFare;
    return this;
  }

  /**
   * If true, returns the flight-offers with no penalty fares only
   * @return noPenaltyFare
   */
  @javax.annotation.Nullable
  public Boolean getNoPenaltyFare() {
    return noPenaltyFare;
  }

  public void setNoPenaltyFare(Boolean noPenaltyFare) {
    this.noPenaltyFare = noPenaltyFare;
  }


  public PricingOptions noRestrictionFare(Boolean noRestrictionFare) {
    this.noRestrictionFare = noRestrictionFare;
    return this;
  }

  /**
   * If true, returns the flight-offers with no restriction fares only
   * @return noRestrictionFare
   */
  @javax.annotation.Nullable
  public Boolean getNoRestrictionFare() {
    return noRestrictionFare;
  }

  public void setNoRestrictionFare(Boolean noRestrictionFare) {
    this.noRestrictionFare = noRestrictionFare;
  }


  public PricingOptions refundableFare(Boolean refundableFare) {
    this.refundableFare = refundableFare;
    return this;
  }

  /**
   * If true, returns the flight-offers with refundable fares only
   * @return refundableFare
   */
  @javax.annotation.Nullable
  public Boolean getRefundableFare() {
    return refundableFare;
  }

  public void setRefundableFare(Boolean refundableFare) {
    this.refundableFare = refundableFare;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PricingOptions pricingOptions = (PricingOptions) o;
    return Objects.equals(this.fareType, pricingOptions.fareType) &&
        Objects.equals(this.includedCheckedBagsOnly, pricingOptions.includedCheckedBagsOnly) &&
        Objects.equals(this.noPenaltyFare, pricingOptions.noPenaltyFare) &&
        Objects.equals(this.noRestrictionFare, pricingOptions.noRestrictionFare) &&
        Objects.equals(this.refundableFare, pricingOptions.refundableFare);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fareType, includedCheckedBagsOnly, noPenaltyFare, noRestrictionFare, refundableFare);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PricingOptions {\n");
    sb.append("    fareType: ").append(toIndentedString(fareType)).append("\n");
    sb.append("    includedCheckedBagsOnly: ").append(toIndentedString(includedCheckedBagsOnly)).append("\n");
    sb.append("    noPenaltyFare: ").append(toIndentedString(noPenaltyFare)).append("\n");
    sb.append("    noRestrictionFare: ").append(toIndentedString(noRestrictionFare)).append("\n");
    sb.append("    refundableFare: ").append(toIndentedString(refundableFare)).append("\n");
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
    openapiFields.add("fareType");
    openapiFields.add("includedCheckedBagsOnly");
    openapiFields.add("noPenaltyFare");
    openapiFields.add("noRestrictionFare");
    openapiFields.add("refundableFare");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PricingOptions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PricingOptions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PricingOptions is not found in the empty JSON string", PricingOptions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PricingOptions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PricingOptions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("fareType") != null && !jsonObj.get("fareType").isJsonNull() && !jsonObj.get("fareType").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `fareType` to be an array in the JSON string but got `%s`", jsonObj.get("fareType").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PricingOptions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PricingOptions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PricingOptions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PricingOptions.class));

       return (TypeAdapter<T>) new TypeAdapter<PricingOptions>() {
           @Override
           public void write(JsonWriter out, PricingOptions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PricingOptions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PricingOptions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PricingOptions
   * @throws IOException if the JSON string is invalid with respect to PricingOptions
   */
  public static PricingOptions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PricingOptions.class);
  }

  /**
   * Convert an instance of PricingOptions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

