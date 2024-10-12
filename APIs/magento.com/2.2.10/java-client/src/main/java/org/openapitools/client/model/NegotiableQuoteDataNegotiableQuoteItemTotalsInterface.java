/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
 * Extension attribute for quote item totals model.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NegotiableQuoteDataNegotiableQuoteItemTotalsInterface {
  public static final String SERIALIZED_NAME_BASE_CART_PRICE = "base_cart_price";
  @SerializedName(SERIALIZED_NAME_BASE_CART_PRICE)
  private BigDecimal baseCartPrice;

  public static final String SERIALIZED_NAME_BASE_CART_PRICE_INCL_TAX = "base_cart_price_incl_tax";
  @SerializedName(SERIALIZED_NAME_BASE_CART_PRICE_INCL_TAX)
  private BigDecimal baseCartPriceInclTax;

  public static final String SERIALIZED_NAME_BASE_CART_TAX = "base_cart_tax";
  @SerializedName(SERIALIZED_NAME_BASE_CART_TAX)
  private BigDecimal baseCartTax;

  public static final String SERIALIZED_NAME_BASE_CATALOG_PRICE = "base_catalog_price";
  @SerializedName(SERIALIZED_NAME_BASE_CATALOG_PRICE)
  private BigDecimal baseCatalogPrice;

  public static final String SERIALIZED_NAME_BASE_CATALOG_PRICE_INCL_TAX = "base_catalog_price_incl_tax";
  @SerializedName(SERIALIZED_NAME_BASE_CATALOG_PRICE_INCL_TAX)
  private BigDecimal baseCatalogPriceInclTax;

  public static final String SERIALIZED_NAME_CART_PRICE = "cart_price";
  @SerializedName(SERIALIZED_NAME_CART_PRICE)
  private BigDecimal cartPrice;

  public static final String SERIALIZED_NAME_CART_PRICE_INCL_TAX = "cart_price_incl_tax";
  @SerializedName(SERIALIZED_NAME_CART_PRICE_INCL_TAX)
  private BigDecimal cartPriceInclTax;

  public static final String SERIALIZED_NAME_CART_TAX = "cart_tax";
  @SerializedName(SERIALIZED_NAME_CART_TAX)
  private BigDecimal cartTax;

  public static final String SERIALIZED_NAME_CATALOG_PRICE = "catalog_price";
  @SerializedName(SERIALIZED_NAME_CATALOG_PRICE)
  private BigDecimal catalogPrice;

  public static final String SERIALIZED_NAME_CATALOG_PRICE_INCL_TAX = "catalog_price_incl_tax";
  @SerializedName(SERIALIZED_NAME_CATALOG_PRICE_INCL_TAX)
  private BigDecimal catalogPriceInclTax;

  public static final String SERIALIZED_NAME_COST = "cost";
  @SerializedName(SERIALIZED_NAME_COST)
  private BigDecimal cost;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private Object extensionAttributes;

  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface() {
  }

  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface baseCartPrice(BigDecimal baseCartPrice) {
    this.baseCartPrice = baseCartPrice;
    return this;
  }

  /**
   * Cart price for quote item in base currency.
   * @return baseCartPrice
   */
  @javax.annotation.Nonnull
  public BigDecimal getBaseCartPrice() {
    return baseCartPrice;
  }

  public void setBaseCartPrice(BigDecimal baseCartPrice) {
    this.baseCartPrice = baseCartPrice;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface baseCartPriceInclTax(BigDecimal baseCartPriceInclTax) {
    this.baseCartPriceInclTax = baseCartPriceInclTax;
    return this;
  }

  /**
   * Cart price with included tax for quote item in base currency.
   * @return baseCartPriceInclTax
   */
  @javax.annotation.Nonnull
  public BigDecimal getBaseCartPriceInclTax() {
    return baseCartPriceInclTax;
  }

  public void setBaseCartPriceInclTax(BigDecimal baseCartPriceInclTax) {
    this.baseCartPriceInclTax = baseCartPriceInclTax;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface baseCartTax(BigDecimal baseCartTax) {
    this.baseCartTax = baseCartTax;
    return this;
  }

  /**
   * Tax from catalog price for quote item in base currency.
   * @return baseCartTax
   */
  @javax.annotation.Nonnull
  public BigDecimal getBaseCartTax() {
    return baseCartTax;
  }

  public void setBaseCartTax(BigDecimal baseCartTax) {
    this.baseCartTax = baseCartTax;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface baseCatalogPrice(BigDecimal baseCatalogPrice) {
    this.baseCatalogPrice = baseCatalogPrice;
    return this;
  }

  /**
   * Catalog price for quote item in base currency.
   * @return baseCatalogPrice
   */
  @javax.annotation.Nonnull
  public BigDecimal getBaseCatalogPrice() {
    return baseCatalogPrice;
  }

  public void setBaseCatalogPrice(BigDecimal baseCatalogPrice) {
    this.baseCatalogPrice = baseCatalogPrice;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface baseCatalogPriceInclTax(BigDecimal baseCatalogPriceInclTax) {
    this.baseCatalogPriceInclTax = baseCatalogPriceInclTax;
    return this;
  }

  /**
   * Catalog price with included tax for quote item in base currency.
   * @return baseCatalogPriceInclTax
   */
  @javax.annotation.Nonnull
  public BigDecimal getBaseCatalogPriceInclTax() {
    return baseCatalogPriceInclTax;
  }

  public void setBaseCatalogPriceInclTax(BigDecimal baseCatalogPriceInclTax) {
    this.baseCatalogPriceInclTax = baseCatalogPriceInclTax;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface cartPrice(BigDecimal cartPrice) {
    this.cartPrice = cartPrice;
    return this;
  }

  /**
   * Cart price for quote item.
   * @return cartPrice
   */
  @javax.annotation.Nonnull
  public BigDecimal getCartPrice() {
    return cartPrice;
  }

  public void setCartPrice(BigDecimal cartPrice) {
    this.cartPrice = cartPrice;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface cartPriceInclTax(BigDecimal cartPriceInclTax) {
    this.cartPriceInclTax = cartPriceInclTax;
    return this;
  }

  /**
   * Cart price with included tax for quote item.
   * @return cartPriceInclTax
   */
  @javax.annotation.Nonnull
  public BigDecimal getCartPriceInclTax() {
    return cartPriceInclTax;
  }

  public void setCartPriceInclTax(BigDecimal cartPriceInclTax) {
    this.cartPriceInclTax = cartPriceInclTax;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface cartTax(BigDecimal cartTax) {
    this.cartTax = cartTax;
    return this;
  }

  /**
   * Tax from catalog price for quote item.
   * @return cartTax
   */
  @javax.annotation.Nonnull
  public BigDecimal getCartTax() {
    return cartTax;
  }

  public void setCartTax(BigDecimal cartTax) {
    this.cartTax = cartTax;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface catalogPrice(BigDecimal catalogPrice) {
    this.catalogPrice = catalogPrice;
    return this;
  }

  /**
   * Catalog price for quote item.
   * @return catalogPrice
   */
  @javax.annotation.Nonnull
  public BigDecimal getCatalogPrice() {
    return catalogPrice;
  }

  public void setCatalogPrice(BigDecimal catalogPrice) {
    this.catalogPrice = catalogPrice;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface catalogPriceInclTax(BigDecimal catalogPriceInclTax) {
    this.catalogPriceInclTax = catalogPriceInclTax;
    return this;
  }

  /**
   * Catalog price with included tax for quote item.
   * @return catalogPriceInclTax
   */
  @javax.annotation.Nonnull
  public BigDecimal getCatalogPriceInclTax() {
    return catalogPriceInclTax;
  }

  public void setCatalogPriceInclTax(BigDecimal catalogPriceInclTax) {
    this.catalogPriceInclTax = catalogPriceInclTax;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface cost(BigDecimal cost) {
    this.cost = cost;
    return this;
  }

  /**
   * Cost for quote item.
   * @return cost
   */
  @javax.annotation.Nonnull
  public BigDecimal getCost() {
    return cost;
  }

  public void setCost(BigDecimal cost) {
    this.cost = cost;
  }


  public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface extensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * ExtensionInterface class for @see \\Magento\\NegotiableQuote\\Api\\Data\\NegotiableQuoteItemTotalsInterface
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public Object getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NegotiableQuoteDataNegotiableQuoteItemTotalsInterface negotiableQuoteDataNegotiableQuoteItemTotalsInterface = (NegotiableQuoteDataNegotiableQuoteItemTotalsInterface) o;
    return Objects.equals(this.baseCartPrice, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.baseCartPrice) &&
        Objects.equals(this.baseCartPriceInclTax, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.baseCartPriceInclTax) &&
        Objects.equals(this.baseCartTax, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.baseCartTax) &&
        Objects.equals(this.baseCatalogPrice, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.baseCatalogPrice) &&
        Objects.equals(this.baseCatalogPriceInclTax, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.baseCatalogPriceInclTax) &&
        Objects.equals(this.cartPrice, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.cartPrice) &&
        Objects.equals(this.cartPriceInclTax, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.cartPriceInclTax) &&
        Objects.equals(this.cartTax, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.cartTax) &&
        Objects.equals(this.catalogPrice, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.catalogPrice) &&
        Objects.equals(this.catalogPriceInclTax, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.catalogPriceInclTax) &&
        Objects.equals(this.cost, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.cost) &&
        Objects.equals(this.extensionAttributes, negotiableQuoteDataNegotiableQuoteItemTotalsInterface.extensionAttributes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(baseCartPrice, baseCartPriceInclTax, baseCartTax, baseCatalogPrice, baseCatalogPriceInclTax, cartPrice, cartPriceInclTax, cartTax, catalogPrice, catalogPriceInclTax, cost, extensionAttributes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NegotiableQuoteDataNegotiableQuoteItemTotalsInterface {\n");
    sb.append("    baseCartPrice: ").append(toIndentedString(baseCartPrice)).append("\n");
    sb.append("    baseCartPriceInclTax: ").append(toIndentedString(baseCartPriceInclTax)).append("\n");
    sb.append("    baseCartTax: ").append(toIndentedString(baseCartTax)).append("\n");
    sb.append("    baseCatalogPrice: ").append(toIndentedString(baseCatalogPrice)).append("\n");
    sb.append("    baseCatalogPriceInclTax: ").append(toIndentedString(baseCatalogPriceInclTax)).append("\n");
    sb.append("    cartPrice: ").append(toIndentedString(cartPrice)).append("\n");
    sb.append("    cartPriceInclTax: ").append(toIndentedString(cartPriceInclTax)).append("\n");
    sb.append("    cartTax: ").append(toIndentedString(cartTax)).append("\n");
    sb.append("    catalogPrice: ").append(toIndentedString(catalogPrice)).append("\n");
    sb.append("    catalogPriceInclTax: ").append(toIndentedString(catalogPriceInclTax)).append("\n");
    sb.append("    cost: ").append(toIndentedString(cost)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
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
    openapiFields.add("base_cart_price");
    openapiFields.add("base_cart_price_incl_tax");
    openapiFields.add("base_cart_tax");
    openapiFields.add("base_catalog_price");
    openapiFields.add("base_catalog_price_incl_tax");
    openapiFields.add("cart_price");
    openapiFields.add("cart_price_incl_tax");
    openapiFields.add("cart_tax");
    openapiFields.add("catalog_price");
    openapiFields.add("catalog_price_incl_tax");
    openapiFields.add("cost");
    openapiFields.add("extension_attributes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("base_cart_price");
    openapiRequiredFields.add("base_cart_price_incl_tax");
    openapiRequiredFields.add("base_cart_tax");
    openapiRequiredFields.add("base_catalog_price");
    openapiRequiredFields.add("base_catalog_price_incl_tax");
    openapiRequiredFields.add("cart_price");
    openapiRequiredFields.add("cart_price_incl_tax");
    openapiRequiredFields.add("cart_tax");
    openapiRequiredFields.add("catalog_price");
    openapiRequiredFields.add("catalog_price_incl_tax");
    openapiRequiredFields.add("cost");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NegotiableQuoteDataNegotiableQuoteItemTotalsInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NegotiableQuoteDataNegotiableQuoteItemTotalsInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NegotiableQuoteDataNegotiableQuoteItemTotalsInterface is not found in the empty JSON string", NegotiableQuoteDataNegotiableQuoteItemTotalsInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NegotiableQuoteDataNegotiableQuoteItemTotalsInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NegotiableQuoteDataNegotiableQuoteItemTotalsInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : NegotiableQuoteDataNegotiableQuoteItemTotalsInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NegotiableQuoteDataNegotiableQuoteItemTotalsInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NegotiableQuoteDataNegotiableQuoteItemTotalsInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NegotiableQuoteDataNegotiableQuoteItemTotalsInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NegotiableQuoteDataNegotiableQuoteItemTotalsInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<NegotiableQuoteDataNegotiableQuoteItemTotalsInterface>() {
           @Override
           public void write(JsonWriter out, NegotiableQuoteDataNegotiableQuoteItemTotalsInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NegotiableQuoteDataNegotiableQuoteItemTotalsInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NegotiableQuoteDataNegotiableQuoteItemTotalsInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NegotiableQuoteDataNegotiableQuoteItemTotalsInterface
   * @throws IOException if the JSON string is invalid with respect to NegotiableQuoteDataNegotiableQuoteItemTotalsInterface
   */
  public static NegotiableQuoteDataNegotiableQuoteItemTotalsInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NegotiableQuoteDataNegotiableQuoteItemTotalsInterface.class);
  }

  /**
   * Convert an instance of NegotiableQuoteDataNegotiableQuoteItemTotalsInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

