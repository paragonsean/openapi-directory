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
 * Price
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:44.468167-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Price {
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

  public Price() {
  }

  public Price base(String base) {
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


  public Price currency(String currency) {
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


  public Price fees(List<Fee> fees) {
    this.fees = fees;
    return this;
  }

  public Price addFeesItem(Fee feesItem) {
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


  public Price refundableTaxes(String refundableTaxes) {
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


  public Price taxes(List<Tax> taxes) {
    this.taxes = taxes;
    return this;
  }

  public Price addTaxesItem(Tax taxesItem) {
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


  public Price total(String total) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Price price = (Price) o;
    return Objects.equals(this.base, price.base) &&
        Objects.equals(this.currency, price.currency) &&
        Objects.equals(this.fees, price.fees) &&
        Objects.equals(this.refundableTaxes, price.refundableTaxes) &&
        Objects.equals(this.taxes, price.taxes) &&
        Objects.equals(this.total, price.total);
  }

  @Override
  public int hashCode() {
    return Objects.hash(base, currency, fees, refundableTaxes, taxes, total);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Price {\n");
    sb.append("    base: ").append(toIndentedString(base)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    fees: ").append(toIndentedString(fees)).append("\n");
    sb.append("    refundableTaxes: ").append(toIndentedString(refundableTaxes)).append("\n");
    sb.append("    taxes: ").append(toIndentedString(taxes)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Price
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Price.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Price is not found in the empty JSON string", Price.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Price.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Price` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Price.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Price' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Price> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Price.class));

       return (TypeAdapter<T>) new TypeAdapter<Price>() {
           @Override
           public void write(JsonWriter out, Price value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Price read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Price given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Price
   * @throws IOException if the JSON string is invalid with respect to Price
   */
  public static Price fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Price.class);
  }

  /**
   * Convert an instance of Price to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

