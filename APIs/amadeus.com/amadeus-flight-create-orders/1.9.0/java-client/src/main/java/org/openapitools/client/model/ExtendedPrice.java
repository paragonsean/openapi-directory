/*
 * Flight Create Orders
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
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AdditionalService;
import org.openapitools.client.model.Fee;
import org.openapitools.client.model.Tax;

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
 * price information
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:44.468167-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExtendedPrice {
  public static final String SERIALIZED_NAME_BASE = "base";
  @SerializedName(SERIALIZED_NAME_BASE)
  private String base;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_FEES = "fees";
  @SerializedName(SERIALIZED_NAME_FEES)
  private List<Fee> fees = new ArrayList<>();

  public static final String SERIALIZED_NAME_REFUNDABLE_TAXES = "refundableTaxes";
  @SerializedName(SERIALIZED_NAME_REFUNDABLE_TAXES)
  private String refundableTaxes;

  public static final String SERIALIZED_NAME_TAXES = "taxes";
  @SerializedName(SERIALIZED_NAME_TAXES)
  private List<Tax> taxes = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private String total;

  public static final String SERIALIZED_NAME_ADDITIONAL_SERVICES = "additionalServices";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_SERVICES)
  private List<AdditionalService> additionalServices = new ArrayList<>();

  public static final String SERIALIZED_NAME_BILLING_CURRENCY = "billingCurrency";
  @SerializedName(SERIALIZED_NAME_BILLING_CURRENCY)
  private String billingCurrency;

  public static final String SERIALIZED_NAME_GRAND_TOTAL = "grandTotal";
  @SerializedName(SERIALIZED_NAME_GRAND_TOTAL)
  private String grandTotal;

  public static final String SERIALIZED_NAME_MARGIN = "margin";
  @SerializedName(SERIALIZED_NAME_MARGIN)
  private String margin;

  public ExtendedPrice() {
  }

  public ExtendedPrice base(String base) {
    this.base = base;
    return this;
  }

  /**
   * Amount without taxes
   * @return base
   */
  @javax.annotation.Nullable
  public String getBase() {
    return base;
  }

  public void setBase(String base) {
    this.base = base;
  }


  public ExtendedPrice currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Get currency
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public ExtendedPrice fees(List<Fee> fees) {
    this.fees = fees;
    return this;
  }

  public ExtendedPrice addFeesItem(Fee feesItem) {
    if (this.fees == null) {
      this.fees = new ArrayList<>();
    }
    this.fees.add(feesItem);
    return this;
  }

  /**
   * List of applicable fees
   * @return fees
   */
  @javax.annotation.Nullable
  public List<Fee> getFees() {
    return fees;
  }

  public void setFees(List<Fee> fees) {
    this.fees = fees;
  }


  public ExtendedPrice refundableTaxes(String refundableTaxes) {
    this.refundableTaxes = refundableTaxes;
    return this;
  }

  /**
   * The amount of taxes which are refundable
   * @return refundableTaxes
   */
  @javax.annotation.Nullable
  public String getRefundableTaxes() {
    return refundableTaxes;
  }

  public void setRefundableTaxes(String refundableTaxes) {
    this.refundableTaxes = refundableTaxes;
  }


  public ExtendedPrice taxes(List<Tax> taxes) {
    this.taxes = taxes;
    return this;
  }

  public ExtendedPrice addTaxesItem(Tax taxesItem) {
    if (this.taxes == null) {
      this.taxes = new ArrayList<>();
    }
    this.taxes.add(taxesItem);
    return this;
  }

  /**
   * Get taxes
   * @return taxes
   */
  @javax.annotation.Nullable
  public List<Tax> getTaxes() {
    return taxes;
  }

  public void setTaxes(List<Tax> taxes) {
    this.taxes = taxes;
  }


  public ExtendedPrice total(String total) {
    this.total = total;
    return this;
  }

  /**
   * Total amount paid by the user
   * @return total
   */
  @javax.annotation.Nullable
  public String getTotal() {
    return total;
  }

  public void setTotal(String total) {
    this.total = total;
  }


  public ExtendedPrice additionalServices(List<AdditionalService> additionalServices) {
    this.additionalServices = additionalServices;
    return this;
  }

  public ExtendedPrice addAdditionalServicesItem(AdditionalService additionalServicesItem) {
    if (this.additionalServices == null) {
      this.additionalServices = new ArrayList<>();
    }
    this.additionalServices.add(additionalServicesItem);
    return this;
  }

  /**
   * Get additionalServices
   * @return additionalServices
   */
  @javax.annotation.Nullable
  public List<AdditionalService> getAdditionalServices() {
    return additionalServices;
  }

  public void setAdditionalServices(List<AdditionalService> additionalServices) {
    this.additionalServices = additionalServices;
  }


  public ExtendedPrice billingCurrency(String billingCurrency) {
    this.billingCurrency = billingCurrency;
    return this;
  }

  /**
   * Currency of the payment. It may be different than the requested currency
   * @return billingCurrency
   */
  @javax.annotation.Nullable
  public String getBillingCurrency() {
    return billingCurrency;
  }

  public void setBillingCurrency(String billingCurrency) {
    this.billingCurrency = billingCurrency;
  }


  public ExtendedPrice grandTotal(String grandTotal) {
    this.grandTotal = grandTotal;
    return this;
  }

  /**
   * Total amount paid by the user (including fees and selected additional services).
   * @return grandTotal
   */
  @javax.annotation.Nullable
  public String getGrandTotal() {
    return grandTotal;
  }

  public void setGrandTotal(String grandTotal) {
    this.grandTotal = grandTotal;
  }


  public ExtendedPrice margin(String margin) {
    this.margin = margin;
    return this;
  }

  /**
   * BOOK step ONLY - The price margin percentage (plus or minus) that the booking can tolerate. When set to 0, then no price magin is tolerated.
   * @return margin
   */
  @javax.annotation.Nullable
  public String getMargin() {
    return margin;
  }

  public void setMargin(String margin) {
    this.margin = margin;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExtendedPrice extendedPrice = (ExtendedPrice) o;
    return Objects.equals(this.base, extendedPrice.base) &&
        Objects.equals(this.currency, extendedPrice.currency) &&
        Objects.equals(this.fees, extendedPrice.fees) &&
        Objects.equals(this.refundableTaxes, extendedPrice.refundableTaxes) &&
        Objects.equals(this.taxes, extendedPrice.taxes) &&
        Objects.equals(this.total, extendedPrice.total) &&
        Objects.equals(this.additionalServices, extendedPrice.additionalServices) &&
        Objects.equals(this.billingCurrency, extendedPrice.billingCurrency) &&
        Objects.equals(this.grandTotal, extendedPrice.grandTotal) &&
        Objects.equals(this.margin, extendedPrice.margin);
  }

  @Override
  public int hashCode() {
    return Objects.hash(base, currency, fees, refundableTaxes, taxes, total, additionalServices, billingCurrency, grandTotal, margin);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExtendedPrice {\n");
    sb.append("    base: ").append(toIndentedString(base)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    fees: ").append(toIndentedString(fees)).append("\n");
    sb.append("    refundableTaxes: ").append(toIndentedString(refundableTaxes)).append("\n");
    sb.append("    taxes: ").append(toIndentedString(taxes)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    additionalServices: ").append(toIndentedString(additionalServices)).append("\n");
    sb.append("    billingCurrency: ").append(toIndentedString(billingCurrency)).append("\n");
    sb.append("    grandTotal: ").append(toIndentedString(grandTotal)).append("\n");
    sb.append("    margin: ").append(toIndentedString(margin)).append("\n");
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
    openapiFields.add("base");
    openapiFields.add("currency");
    openapiFields.add("fees");
    openapiFields.add("refundableTaxes");
    openapiFields.add("taxes");
    openapiFields.add("total");
    openapiFields.add("additionalServices");
    openapiFields.add("billingCurrency");
    openapiFields.add("grandTotal");
    openapiFields.add("margin");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExtendedPrice
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExtendedPrice.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExtendedPrice is not found in the empty JSON string", ExtendedPrice.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExtendedPrice.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExtendedPrice` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("base") != null && !jsonObj.get("base").isJsonNull()) && !jsonObj.get("base").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `base` to be a primitive type in the JSON string but got `%s`", jsonObj.get("base").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (jsonObj.get("fees") != null && !jsonObj.get("fees").isJsonNull()) {
        JsonArray jsonArrayfees = jsonObj.getAsJsonArray("fees");
        if (jsonArrayfees != null) {
          // ensure the json data is an array
          if (!jsonObj.get("fees").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `fees` to be an array in the JSON string but got `%s`", jsonObj.get("fees").toString()));
          }

          // validate the optional field `fees` (array)
          for (int i = 0; i < jsonArrayfees.size(); i++) {
            Fee.validateJsonElement(jsonArrayfees.get(i));
          };
        }
      }
      if ((jsonObj.get("refundableTaxes") != null && !jsonObj.get("refundableTaxes").isJsonNull()) && !jsonObj.get("refundableTaxes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `refundableTaxes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("refundableTaxes").toString()));
      }
      if (jsonObj.get("taxes") != null && !jsonObj.get("taxes").isJsonNull()) {
        JsonArray jsonArraytaxes = jsonObj.getAsJsonArray("taxes");
        if (jsonArraytaxes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("taxes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `taxes` to be an array in the JSON string but got `%s`", jsonObj.get("taxes").toString()));
          }

          // validate the optional field `taxes` (array)
          for (int i = 0; i < jsonArraytaxes.size(); i++) {
            Tax.validateJsonElement(jsonArraytaxes.get(i));
          };
        }
      }
      if ((jsonObj.get("total") != null && !jsonObj.get("total").isJsonNull()) && !jsonObj.get("total").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total").toString()));
      }
      if (jsonObj.get("additionalServices") != null && !jsonObj.get("additionalServices").isJsonNull()) {
        JsonArray jsonArrayadditionalServices = jsonObj.getAsJsonArray("additionalServices");
        if (jsonArrayadditionalServices != null) {
          // ensure the json data is an array
          if (!jsonObj.get("additionalServices").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `additionalServices` to be an array in the JSON string but got `%s`", jsonObj.get("additionalServices").toString()));
          }

          // validate the optional field `additionalServices` (array)
          for (int i = 0; i < jsonArrayadditionalServices.size(); i++) {
            AdditionalService.validateJsonElement(jsonArrayadditionalServices.get(i));
          };
        }
      }
      if ((jsonObj.get("billingCurrency") != null && !jsonObj.get("billingCurrency").isJsonNull()) && !jsonObj.get("billingCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billingCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billingCurrency").toString()));
      }
      if ((jsonObj.get("grandTotal") != null && !jsonObj.get("grandTotal").isJsonNull()) && !jsonObj.get("grandTotal").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `grandTotal` to be a primitive type in the JSON string but got `%s`", jsonObj.get("grandTotal").toString()));
      }
      if ((jsonObj.get("margin") != null && !jsonObj.get("margin").isJsonNull()) && !jsonObj.get("margin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `margin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("margin").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExtendedPrice.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExtendedPrice' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExtendedPrice> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExtendedPrice.class));

       return (TypeAdapter<T>) new TypeAdapter<ExtendedPrice>() {
           @Override
           public void write(JsonWriter out, ExtendedPrice value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExtendedPrice read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExtendedPrice given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExtendedPrice
   * @throws IOException if the JSON string is invalid with respect to ExtendedPrice
   */
  public static ExtendedPrice fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExtendedPrice.class);
  }

  /**
   * Convert an instance of ExtendedPrice to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

