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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import org.openapitools.client.model.PriceCoverageBucket;

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
 * A price coverage view. Covers the &#x60;price_coverage_stats&#x60; Scorecard functionality in pre-v3.0 API versions. For more information, refer to Price Coverage for Push and Hint partners.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:52.320664-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PriceCoverageView {
  public static final String SERIALIZED_NAME_CALCULATION_DATE = "calculationDate";
  @SerializedName(SERIALIZED_NAME_CALCULATION_DATE)
  private Date calculationDate;

  public static final String SERIALIZED_NAME_MATCHED_PROPERTY_COUNT = "matchedPropertyCount";
  @SerializedName(SERIALIZED_NAME_MATCHED_PROPERTY_COUNT)
  private Integer matchedPropertyCount;

  public static final String SERIALIZED_NAME_PRICE_COVERAGE_BINARY_PERCENT = "priceCoverageBinaryPercent";
  @SerializedName(SERIALIZED_NAME_PRICE_COVERAGE_BINARY_PERCENT)
  private Double priceCoverageBinaryPercent;

  public static final String SERIALIZED_NAME_PRICE_COVERAGE_BUCKETS = "priceCoverageBuckets";
  @SerializedName(SERIALIZED_NAME_PRICE_COVERAGE_BUCKETS)
  private List<PriceCoverageBucket> priceCoverageBuckets = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRICE_COVERAGE_PERCENT = "priceCoveragePercent";
  @SerializedName(SERIALIZED_NAME_PRICE_COVERAGE_PERCENT)
  private Double priceCoveragePercent;

  public PriceCoverageView() {
  }

  public PriceCoverageView calculationDate(Date calculationDate) {
    this.calculationDate = calculationDate;
    return this;
  }

  /**
   * Get calculationDate
   * @return calculationDate
   */
  @javax.annotation.Nullable
  public Date getCalculationDate() {
    return calculationDate;
  }

  public void setCalculationDate(Date calculationDate) {
    this.calculationDate = calculationDate;
  }


  public PriceCoverageView matchedPropertyCount(Integer matchedPropertyCount) {
    this.matchedPropertyCount = matchedPropertyCount;
    return this;
  }

  /**
   * The total number of properties that have prices for the given itineraries.
   * @return matchedPropertyCount
   */
  @javax.annotation.Nullable
  public Integer getMatchedPropertyCount() {
    return matchedPropertyCount;
  }

  public void setMatchedPropertyCount(Integer matchedPropertyCount) {
    this.matchedPropertyCount = matchedPropertyCount;
  }


  public PriceCoverageView priceCoverageBinaryPercent(Double priceCoverageBinaryPercent) {
    this.priceCoverageBinaryPercent = priceCoverageBinaryPercent;
    return this;
  }

  /**
   * The ratio between the number of hotels which have at least one price for the calculation period and &#x60;matched_property_count&#x60;.
   * @return priceCoverageBinaryPercent
   */
  @javax.annotation.Nullable
  public Double getPriceCoverageBinaryPercent() {
    return priceCoverageBinaryPercent;
  }

  public void setPriceCoverageBinaryPercent(Double priceCoverageBinaryPercent) {
    this.priceCoverageBinaryPercent = priceCoverageBinaryPercent;
  }


  public PriceCoverageView priceCoverageBuckets(List<PriceCoverageBucket> priceCoverageBuckets) {
    this.priceCoverageBuckets = priceCoverageBuckets;
    return this;
  }

  public PriceCoverageView addPriceCoverageBucketsItem(PriceCoverageBucket priceCoverageBucketsItem) {
    if (this.priceCoverageBuckets == null) {
      this.priceCoverageBuckets = new ArrayList<>();
    }
    this.priceCoverageBuckets.add(priceCoverageBucketsItem);
    return this;
  }

  /**
   * Price coverage stats for combinations of advance booking window and length of stay ranges.
   * @return priceCoverageBuckets
   */
  @javax.annotation.Nullable
  public List<PriceCoverageBucket> getPriceCoverageBuckets() {
    return priceCoverageBuckets;
  }

  public void setPriceCoverageBuckets(List<PriceCoverageBucket> priceCoverageBuckets) {
    this.priceCoverageBuckets = priceCoverageBuckets;
  }


  public PriceCoverageView priceCoveragePercent(Double priceCoveragePercent) {
    this.priceCoveragePercent = priceCoveragePercent;
    return this;
  }

  /**
   * The overall price coverage for an account. This value is the ratio between the number of hotel prices for the calculation booking window and length of stay range divided by the number of all possible prices, which is &#x60;matched_property_count&#x60; times 330 (for advance book window) times 30 (for length of stay).
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
    PriceCoverageView priceCoverageView = (PriceCoverageView) o;
    return Objects.equals(this.calculationDate, priceCoverageView.calculationDate) &&
        Objects.equals(this.matchedPropertyCount, priceCoverageView.matchedPropertyCount) &&
        Objects.equals(this.priceCoverageBinaryPercent, priceCoverageView.priceCoverageBinaryPercent) &&
        Objects.equals(this.priceCoverageBuckets, priceCoverageView.priceCoverageBuckets) &&
        Objects.equals(this.priceCoveragePercent, priceCoverageView.priceCoveragePercent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(calculationDate, matchedPropertyCount, priceCoverageBinaryPercent, priceCoverageBuckets, priceCoveragePercent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PriceCoverageView {\n");
    sb.append("    calculationDate: ").append(toIndentedString(calculationDate)).append("\n");
    sb.append("    matchedPropertyCount: ").append(toIndentedString(matchedPropertyCount)).append("\n");
    sb.append("    priceCoverageBinaryPercent: ").append(toIndentedString(priceCoverageBinaryPercent)).append("\n");
    sb.append("    priceCoverageBuckets: ").append(toIndentedString(priceCoverageBuckets)).append("\n");
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
    openapiFields.add("calculationDate");
    openapiFields.add("matchedPropertyCount");
    openapiFields.add("priceCoverageBinaryPercent");
    openapiFields.add("priceCoverageBuckets");
    openapiFields.add("priceCoveragePercent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PriceCoverageView
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PriceCoverageView.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PriceCoverageView is not found in the empty JSON string", PriceCoverageView.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PriceCoverageView.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PriceCoverageView` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `calculationDate`
      if (jsonObj.get("calculationDate") != null && !jsonObj.get("calculationDate").isJsonNull()) {
        Date.validateJsonElement(jsonObj.get("calculationDate"));
      }
      if (jsonObj.get("priceCoverageBuckets") != null && !jsonObj.get("priceCoverageBuckets").isJsonNull()) {
        JsonArray jsonArraypriceCoverageBuckets = jsonObj.getAsJsonArray("priceCoverageBuckets");
        if (jsonArraypriceCoverageBuckets != null) {
          // ensure the json data is an array
          if (!jsonObj.get("priceCoverageBuckets").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `priceCoverageBuckets` to be an array in the JSON string but got `%s`", jsonObj.get("priceCoverageBuckets").toString()));
          }

          // validate the optional field `priceCoverageBuckets` (array)
          for (int i = 0; i < jsonArraypriceCoverageBuckets.size(); i++) {
            PriceCoverageBucket.validateJsonElement(jsonArraypriceCoverageBuckets.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PriceCoverageView.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PriceCoverageView' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PriceCoverageView> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PriceCoverageView.class));

       return (TypeAdapter<T>) new TypeAdapter<PriceCoverageView>() {
           @Override
           public void write(JsonWriter out, PriceCoverageView value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PriceCoverageView read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PriceCoverageView given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PriceCoverageView
   * @throws IOException if the JSON string is invalid with respect to PriceCoverageView
   */
  public static PriceCoverageView fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PriceCoverageView.class);
  }

  /**
   * Convert an instance of PriceCoverageView to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

