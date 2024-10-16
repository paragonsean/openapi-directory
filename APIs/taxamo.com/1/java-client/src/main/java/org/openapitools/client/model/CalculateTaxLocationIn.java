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
 * CalculateTaxLocationIn
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CalculateTaxLocationIn {
  public static final String SERIALIZED_NAME_BILLING_COUNTRY_CODE = "billing_country_code";
  @SerializedName(SERIALIZED_NAME_BILLING_COUNTRY_CODE)
  private String billingCountryCode;

  public static final String SERIALIZED_NAME_BUYER_CREDIT_CARD_PREFIX = "buyer_credit_card_prefix";
  @SerializedName(SERIALIZED_NAME_BUYER_CREDIT_CARD_PREFIX)
  private String buyerCreditCardPrefix;

  public CalculateTaxLocationIn() {
  }

  public CalculateTaxLocationIn billingCountryCode(String billingCountryCode) {
    this.billingCountryCode = billingCountryCode;
    return this;
  }

  /**
   * Billing two letter ISO country code.
   * @return billingCountryCode
   */
  @javax.annotation.Nullable
  public String getBillingCountryCode() {
    return billingCountryCode;
  }

  public void setBillingCountryCode(String billingCountryCode) {
    this.billingCountryCode = billingCountryCode;
  }


  public CalculateTaxLocationIn buyerCreditCardPrefix(String buyerCreditCardPrefix) {
    this.buyerCreditCardPrefix = buyerCreditCardPrefix;
    return this;
  }

  /**
   * First 6 digits of buyer&#39;s credit card prefix.
   * @return buyerCreditCardPrefix
   */
  @javax.annotation.Nullable
  public String getBuyerCreditCardPrefix() {
    return buyerCreditCardPrefix;
  }

  public void setBuyerCreditCardPrefix(String buyerCreditCardPrefix) {
    this.buyerCreditCardPrefix = buyerCreditCardPrefix;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CalculateTaxLocationIn calculateTaxLocationIn = (CalculateTaxLocationIn) o;
    return Objects.equals(this.billingCountryCode, calculateTaxLocationIn.billingCountryCode) &&
        Objects.equals(this.buyerCreditCardPrefix, calculateTaxLocationIn.buyerCreditCardPrefix);
  }

  @Override
  public int hashCode() {
    return Objects.hash(billingCountryCode, buyerCreditCardPrefix);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CalculateTaxLocationIn {\n");
    sb.append("    billingCountryCode: ").append(toIndentedString(billingCountryCode)).append("\n");
    sb.append("    buyerCreditCardPrefix: ").append(toIndentedString(buyerCreditCardPrefix)).append("\n");
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
    openapiFields.add("billing_country_code");
    openapiFields.add("buyer_credit_card_prefix");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CalculateTaxLocationIn
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CalculateTaxLocationIn.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CalculateTaxLocationIn is not found in the empty JSON string", CalculateTaxLocationIn.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CalculateTaxLocationIn.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CalculateTaxLocationIn` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("billing_country_code") != null && !jsonObj.get("billing_country_code").isJsonNull()) && !jsonObj.get("billing_country_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billing_country_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billing_country_code").toString()));
      }
      if ((jsonObj.get("buyer_credit_card_prefix") != null && !jsonObj.get("buyer_credit_card_prefix").isJsonNull()) && !jsonObj.get("buyer_credit_card_prefix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `buyer_credit_card_prefix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("buyer_credit_card_prefix").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CalculateTaxLocationIn.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CalculateTaxLocationIn' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CalculateTaxLocationIn> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CalculateTaxLocationIn.class));

       return (TypeAdapter<T>) new TypeAdapter<CalculateTaxLocationIn>() {
           @Override
           public void write(JsonWriter out, CalculateTaxLocationIn value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CalculateTaxLocationIn read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CalculateTaxLocationIn given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CalculateTaxLocationIn
   * @throws IOException if the JSON string is invalid with respect to CalculateTaxLocationIn
   */
  public static CalculateTaxLocationIn fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CalculateTaxLocationIn.class);
  }

  /**
   * Convert an instance of CalculateTaxLocationIn to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

