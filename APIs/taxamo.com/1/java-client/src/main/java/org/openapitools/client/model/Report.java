/*
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
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
import java.math.BigDecimal;
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
 * Report
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Report {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_COUNTRY_CODE = "country_code";
  @SerializedName(SERIALIZED_NAME_COUNTRY_CODE)
  private String countryCode;

  public static final String SERIALIZED_NAME_COUNTRY_NAME = "country_name";
  @SerializedName(SERIALIZED_NAME_COUNTRY_NAME)
  private String countryName;

  public static final String SERIALIZED_NAME_COUNTRY_SUBDIVISION = "country_subdivision";
  @SerializedName(SERIALIZED_NAME_COUNTRY_SUBDIVISION)
  private String countrySubdivision;

  public static final String SERIALIZED_NAME_CURRENCY_CODE = "currency_code";
  @SerializedName(SERIALIZED_NAME_CURRENCY_CODE)
  private String currencyCode;

  public static final String SERIALIZED_NAME_SKIP_MOSS = "skip_moss";
  @SerializedName(SERIALIZED_NAME_SKIP_MOSS)
  private Boolean skipMoss;

  public static final String SERIALIZED_NAME_TAX_AMOUNT = "tax_amount";
  @SerializedName(SERIALIZED_NAME_TAX_AMOUNT)
  private BigDecimal taxAmount;

  public static final String SERIALIZED_NAME_TAX_RATE = "tax_rate";
  @SerializedName(SERIALIZED_NAME_TAX_RATE)
  private BigDecimal taxRate;

  public static final String SERIALIZED_NAME_TAX_REGION = "tax_region";
  @SerializedName(SERIALIZED_NAME_TAX_REGION)
  private String taxRegion;

  public Report() {
  }

  public Report amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Amount w/o tax
   * @return amount
   */
  @javax.annotation.Nullable
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public Report countryCode(String countryCode) {
    this.countryCode = countryCode;
    return this;
  }

  /**
   * Two letter ISO country code.
   * @return countryCode
   */
  @javax.annotation.Nullable
  public String getCountryCode() {
    return countryCode;
  }

  public void setCountryCode(String countryCode) {
    this.countryCode = countryCode;
  }


  public Report countryName(String countryName) {
    this.countryName = countryName;
    return this;
  }

  /**
   * Country name
   * @return countryName
   */
  @javax.annotation.Nullable
  public String getCountryName() {
    return countryName;
  }

  public void setCountryName(String countryName) {
    this.countryName = countryName;
  }


  public Report countrySubdivision(String countrySubdivision) {
    this.countrySubdivision = countrySubdivision;
    return this;
  }

  /**
   * Country subdivision (e.g. state or provice or county)
   * @return countrySubdivision
   */
  @javax.annotation.Nullable
  public String getCountrySubdivision() {
    return countrySubdivision;
  }

  public void setCountrySubdivision(String countrySubdivision) {
    this.countrySubdivision = countrySubdivision;
  }


  public Report currencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
    return this;
  }

  /**
   * Three-letter ISO currency code.
   * @return currencyCode
   */
  @javax.annotation.Nullable
  public String getCurrencyCode() {
    return currencyCode;
  }

  public void setCurrencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
  }


  public Report skipMoss(Boolean skipMoss) {
    this.skipMoss = skipMoss;
    return this;
  }

  /**
   * If true, this line should not be entered into MOSS and is provided for informative purposes only. For example because the country is the same as MOSS registration country and merchant country.
   * @return skipMoss
   */
  @javax.annotation.Nullable
  public Boolean getSkipMoss() {
    return skipMoss;
  }

  public void setSkipMoss(Boolean skipMoss) {
    this.skipMoss = skipMoss;
  }


  public Report taxAmount(BigDecimal taxAmount) {
    this.taxAmount = taxAmount;
    return this;
  }

  /**
   * Tax amount
   * @return taxAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getTaxAmount() {
    return taxAmount;
  }

  public void setTaxAmount(BigDecimal taxAmount) {
    this.taxAmount = taxAmount;
  }


  public Report taxRate(BigDecimal taxRate) {
    this.taxRate = taxRate;
    return this;
  }

  /**
   * Tax rate
   * @return taxRate
   */
  @javax.annotation.Nullable
  public BigDecimal getTaxRate() {
    return taxRate;
  }

  public void setTaxRate(BigDecimal taxRate) {
    this.taxRate = taxRate;
  }


  public Report taxRegion(String taxRegion) {
    this.taxRegion = taxRegion;
    return this;
  }

  /**
   * Tax region key
   * @return taxRegion
   */
  @javax.annotation.Nullable
  public String getTaxRegion() {
    return taxRegion;
  }

  public void setTaxRegion(String taxRegion) {
    this.taxRegion = taxRegion;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Report report = (Report) o;
    return Objects.equals(this.amount, report.amount) &&
        Objects.equals(this.countryCode, report.countryCode) &&
        Objects.equals(this.countryName, report.countryName) &&
        Objects.equals(this.countrySubdivision, report.countrySubdivision) &&
        Objects.equals(this.currencyCode, report.currencyCode) &&
        Objects.equals(this.skipMoss, report.skipMoss) &&
        Objects.equals(this.taxAmount, report.taxAmount) &&
        Objects.equals(this.taxRate, report.taxRate) &&
        Objects.equals(this.taxRegion, report.taxRegion);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, countryCode, countryName, countrySubdivision, currencyCode, skipMoss, taxAmount, taxRate, taxRegion);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Report {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    countryCode: ").append(toIndentedString(countryCode)).append("\n");
    sb.append("    countryName: ").append(toIndentedString(countryName)).append("\n");
    sb.append("    countrySubdivision: ").append(toIndentedString(countrySubdivision)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    skipMoss: ").append(toIndentedString(skipMoss)).append("\n");
    sb.append("    taxAmount: ").append(toIndentedString(taxAmount)).append("\n");
    sb.append("    taxRate: ").append(toIndentedString(taxRate)).append("\n");
    sb.append("    taxRegion: ").append(toIndentedString(taxRegion)).append("\n");
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
    openapiFields.add("amount");
    openapiFields.add("country_code");
    openapiFields.add("country_name");
    openapiFields.add("country_subdivision");
    openapiFields.add("currency_code");
    openapiFields.add("skip_moss");
    openapiFields.add("tax_amount");
    openapiFields.add("tax_rate");
    openapiFields.add("tax_region");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Report
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Report.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Report is not found in the empty JSON string", Report.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Report.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Report` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("country_code") != null && !jsonObj.get("country_code").isJsonNull()) && !jsonObj.get("country_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country_code").toString()));
      }
      if ((jsonObj.get("country_name") != null && !jsonObj.get("country_name").isJsonNull()) && !jsonObj.get("country_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country_name").toString()));
      }
      if ((jsonObj.get("country_subdivision") != null && !jsonObj.get("country_subdivision").isJsonNull()) && !jsonObj.get("country_subdivision").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country_subdivision` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country_subdivision").toString()));
      }
      if ((jsonObj.get("currency_code") != null && !jsonObj.get("currency_code").isJsonNull()) && !jsonObj.get("currency_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency_code").toString()));
      }
      if ((jsonObj.get("tax_region") != null && !jsonObj.get("tax_region").isJsonNull()) && !jsonObj.get("tax_region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_region").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Report.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Report' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Report> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Report.class));

       return (TypeAdapter<T>) new TypeAdapter<Report>() {
           @Override
           public void write(JsonWriter out, Report value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Report read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Report given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Report
   * @throws IOException if the JSON string is invalid with respect to Report
   */
  public static Report fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Report.class);
  }

  /**
   * Convert an instance of Report to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

