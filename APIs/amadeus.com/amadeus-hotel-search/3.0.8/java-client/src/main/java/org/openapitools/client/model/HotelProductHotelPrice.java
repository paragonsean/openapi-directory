/*
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
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
import org.openapitools.client.model.HotelProductPriceVariations;
import org.openapitools.client.model.Markup;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:09.974193-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HotelProductHotelPrice {
  public static final String SERIALIZED_NAME_BASE = "base";
  @SerializedName(SERIALIZED_NAME_BASE)
  private String base;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_MARKUPS = "markups";
  @SerializedName(SERIALIZED_NAME_MARKUPS)
  private List<Markup> markups = new ArrayList<>();

  public static final String SERIALIZED_NAME_SELLING_TOTAL = "sellingTotal";
  @SerializedName(SERIALIZED_NAME_SELLING_TOTAL)
  private String sellingTotal;

  public static final String SERIALIZED_NAME_TAXES = "taxes";
  @SerializedName(SERIALIZED_NAME_TAXES)
  private List<Tax> taxes = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private String total;

  public static final String SERIALIZED_NAME_VARIATIONS = "variations";
  @SerializedName(SERIALIZED_NAME_VARIATIONS)
  private HotelProductPriceVariations variations;

  public HotelProductHotelPrice() {
  }

  public HotelProductHotelPrice base(String base) {
    this.base = base;
    return this;
  }

  /**
   * Get base
   * @return base
   */
  @javax.annotation.Nullable
  public String getBase() {
    return base;
  }

  public void setBase(String base) {
    this.base = base;
  }


  public HotelProductHotelPrice currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * currency Code apply to all elements of the price
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public HotelProductHotelPrice markups(List<Markup> markups) {
    this.markups = markups;
    return this;
  }

  public HotelProductHotelPrice addMarkupsItem(Markup markupsItem) {
    if (this.markups == null) {
      this.markups = new ArrayList<>();
    }
    this.markups.add(markupsItem);
    return this;
  }

  /**
   * Get markups
   * @return markups
   */
  @javax.annotation.Nullable
  public List<Markup> getMarkups() {
    return markups;
  }

  public void setMarkups(List<Markup> markups) {
    this.markups = markups;
  }


  public HotelProductHotelPrice sellingTotal(String sellingTotal) {
    this.sellingTotal = sellingTotal;
    return this;
  }

  /**
   * sellingTotal &#x3D; Total + margins + markup + totalFees - discounts
   * @return sellingTotal
   */
  @javax.annotation.Nullable
  public String getSellingTotal() {
    return sellingTotal;
  }

  public void setSellingTotal(String sellingTotal) {
    this.sellingTotal = sellingTotal;
  }


  public HotelProductHotelPrice taxes(List<Tax> taxes) {
    this.taxes = taxes;
    return this;
  }

  public HotelProductHotelPrice addTaxesItem(Tax taxesItem) {
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


  public HotelProductHotelPrice total(String total) {
    this.total = total;
    return this;
  }

  /**
   * total &#x3D; base + totalTaxes
   * @return total
   */
  @javax.annotation.Nullable
  public String getTotal() {
    return total;
  }

  public void setTotal(String total) {
    this.total = total;
  }


  public HotelProductHotelPrice variations(HotelProductPriceVariations variations) {
    this.variations = variations;
    return this;
  }

  /**
   * Get variations
   * @return variations
   */
  @javax.annotation.Nullable
  public HotelProductPriceVariations getVariations() {
    return variations;
  }

  public void setVariations(HotelProductPriceVariations variations) {
    this.variations = variations;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HotelProductHotelPrice hotelProductHotelPrice = (HotelProductHotelPrice) o;
    return Objects.equals(this.base, hotelProductHotelPrice.base) &&
        Objects.equals(this.currency, hotelProductHotelPrice.currency) &&
        Objects.equals(this.markups, hotelProductHotelPrice.markups) &&
        Objects.equals(this.sellingTotal, hotelProductHotelPrice.sellingTotal) &&
        Objects.equals(this.taxes, hotelProductHotelPrice.taxes) &&
        Objects.equals(this.total, hotelProductHotelPrice.total) &&
        Objects.equals(this.variations, hotelProductHotelPrice.variations);
  }

  @Override
  public int hashCode() {
    return Objects.hash(base, currency, markups, sellingTotal, taxes, total, variations);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HotelProductHotelPrice {\n");
    sb.append("    base: ").append(toIndentedString(base)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    markups: ").append(toIndentedString(markups)).append("\n");
    sb.append("    sellingTotal: ").append(toIndentedString(sellingTotal)).append("\n");
    sb.append("    taxes: ").append(toIndentedString(taxes)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    variations: ").append(toIndentedString(variations)).append("\n");
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
    openapiFields.add("markups");
    openapiFields.add("sellingTotal");
    openapiFields.add("taxes");
    openapiFields.add("total");
    openapiFields.add("variations");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HotelProductHotelPrice
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HotelProductHotelPrice.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HotelProductHotelPrice is not found in the empty JSON string", HotelProductHotelPrice.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HotelProductHotelPrice.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HotelProductHotelPrice` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("base") != null && !jsonObj.get("base").isJsonNull()) && !jsonObj.get("base").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `base` to be a primitive type in the JSON string but got `%s`", jsonObj.get("base").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (jsonObj.get("markups") != null && !jsonObj.get("markups").isJsonNull()) {
        JsonArray jsonArraymarkups = jsonObj.getAsJsonArray("markups");
        if (jsonArraymarkups != null) {
          // ensure the json data is an array
          if (!jsonObj.get("markups").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `markups` to be an array in the JSON string but got `%s`", jsonObj.get("markups").toString()));
          }

          // validate the optional field `markups` (array)
          for (int i = 0; i < jsonArraymarkups.size(); i++) {
            Markup.validateJsonElement(jsonArraymarkups.get(i));
          };
        }
      }
      if ((jsonObj.get("sellingTotal") != null && !jsonObj.get("sellingTotal").isJsonNull()) && !jsonObj.get("sellingTotal").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellingTotal` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sellingTotal").toString()));
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
      // validate the optional field `variations`
      if (jsonObj.get("variations") != null && !jsonObj.get("variations").isJsonNull()) {
        HotelProductPriceVariations.validateJsonElement(jsonObj.get("variations"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HotelProductHotelPrice.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HotelProductHotelPrice' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HotelProductHotelPrice> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HotelProductHotelPrice.class));

       return (TypeAdapter<T>) new TypeAdapter<HotelProductHotelPrice>() {
           @Override
           public void write(JsonWriter out, HotelProductHotelPrice value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HotelProductHotelPrice read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HotelProductHotelPrice given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HotelProductHotelPrice
   * @throws IOException if the JSON string is invalid with respect to HotelProductHotelPrice
   */
  public static HotelProductHotelPrice fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HotelProductHotelPrice.class);
  }

  /**
   * Convert an instance of HotelProductHotelPrice to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

