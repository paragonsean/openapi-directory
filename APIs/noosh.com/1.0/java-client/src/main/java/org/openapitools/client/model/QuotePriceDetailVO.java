/*
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
import org.openapitools.client.model.BreakoutVO;
import org.openapitools.client.model.PropertyPaAndAttVO;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * Java type: com.noosh.nooshapi.vo.QuotePriceDetailVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QuotePriceDetailVO {
  public static final String SERIALIZED_NAME_BREAKOUTS = "breakouts";
  @SerializedName(SERIALIZED_NAME_BREAKOUTS)
  private List<BreakoutVO> breakouts = new ArrayList<>();

  public static final String SERIALIZED_NAME_COST = "cost";
  @SerializedName(SERIALIZED_NAME_COST)
  private Object cost = null;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<PropertyPaAndAttVO> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIXED = "fixed";
  @SerializedName(SERIALIZED_NAME_FIXED)
  private Object fixed = null;

  public static final String SERIALIZED_NAME_IS_CHOSEN = "is_chosen";
  @SerializedName(SERIALIZED_NAME_IS_CHOSEN)
  private Boolean isChosen;

  public static final String SERIALIZED_NAME_IS_INCLUDED = "is_included";
  @SerializedName(SERIALIZED_NAME_IS_INCLUDED)
  private Boolean isIncluded;

  public static final String SERIALIZED_NAME_IS_QUOTED = "is_quoted";
  @SerializedName(SERIALIZED_NAME_IS_QUOTED)
  private Boolean isQuoted;

  public static final String SERIALIZED_NAME_PARENT_PRICE_ID = "parent_price_id";
  @SerializedName(SERIALIZED_NAME_PARENT_PRICE_ID)
  private Long parentPriceId;

  public static final String SERIALIZED_NAME_PRICE_ID = "price_id";
  @SerializedName(SERIALIZED_NAME_PRICE_ID)
  private Long priceId;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Object quantity = null;

  public static final String SERIALIZED_NAME_SELL_PRICE = "sell_price";
  @SerializedName(SERIALIZED_NAME_SELL_PRICE)
  private Object sellPrice = null;

  public static final String SERIALIZED_NAME_SHIPPING = "shipping";
  @SerializedName(SERIALIZED_NAME_SHIPPING)
  private Object shipping = null;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private Object source = null;

  public static final String SERIALIZED_NAME_SUPPLIER = "supplier";
  @SerializedName(SERIALIZED_NAME_SUPPLIER)
  private String supplier;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private Object tax = null;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Object total = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_COST = "transactional_cost";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_COST)
  private Object transactionalCost = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_FIXED = "transactional_fixed";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_FIXED)
  private Object transactionalFixed = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_SELL_PRICE = "transactional_sell_price";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_SELL_PRICE)
  private Object transactionalSellPrice = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_SHIPPING = "transactional_shipping";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_SHIPPING)
  private Object transactionalShipping = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_TAX = "transactional_tax";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_TAX)
  private Object transactionalTax = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_TOTAL = "transactional_total";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_TOTAL)
  private Object transactionalTotal = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_VARIABLE = "transactional_variable";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_VARIABLE)
  private Object transactionalVariable = null;

  public static final String SERIALIZED_NAME_VARIABLE = "variable";
  @SerializedName(SERIALIZED_NAME_VARIABLE)
  private Object variable = null;

  public static final String SERIALIZED_NAME_VARIABLE_PERCENT = "variable_percent";
  @SerializedName(SERIALIZED_NAME_VARIABLE_PERCENT)
  private Object variablePercent = null;

  public QuotePriceDetailVO() {
  }

  public QuotePriceDetailVO breakouts(List<BreakoutVO> breakouts) {
    this.breakouts = breakouts;
    return this;
  }

  public QuotePriceDetailVO addBreakoutsItem(BreakoutVO breakoutsItem) {
    if (this.breakouts == null) {
      this.breakouts = new ArrayList<>();
    }
    this.breakouts.add(breakoutsItem);
    return this;
  }

  /**
   * 
   * @return breakouts
   */
  @javax.annotation.Nullable
  public List<BreakoutVO> getBreakouts() {
    return breakouts;
  }

  public void setBreakouts(List<BreakoutVO> breakouts) {
    this.breakouts = breakouts;
  }


  public QuotePriceDetailVO cost(Object cost) {
    this.cost = cost;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return cost
   */
  @javax.annotation.Nullable
  public Object getCost() {
    return cost;
  }

  public void setCost(Object cost) {
    this.cost = cost;
  }


  public QuotePriceDetailVO customFields(List<PropertyPaAndAttVO> customFields) {
    this.customFields = customFields;
    return this;
  }

  public QuotePriceDetailVO addCustomFieldsItem(PropertyPaAndAttVO customFieldsItem) {
    if (this.customFields == null) {
      this.customFields = new ArrayList<>();
    }
    this.customFields.add(customFieldsItem);
    return this;
  }

  /**
   * 
   * @return customFields
   */
  @javax.annotation.Nullable
  public List<PropertyPaAndAttVO> getCustomFields() {
    return customFields;
  }

  public void setCustomFields(List<PropertyPaAndAttVO> customFields) {
    this.customFields = customFields;
  }


  public QuotePriceDetailVO fixed(Object fixed) {
    this.fixed = fixed;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return fixed
   */
  @javax.annotation.Nullable
  public Object getFixed() {
    return fixed;
  }

  public void setFixed(Object fixed) {
    this.fixed = fixed;
  }


  public QuotePriceDetailVO isChosen(Boolean isChosen) {
    this.isChosen = isChosen;
    return this;
  }

  /**
   * 
   * @return isChosen
   */
  @javax.annotation.Nullable
  public Boolean getIsChosen() {
    return isChosen;
  }

  public void setIsChosen(Boolean isChosen) {
    this.isChosen = isChosen;
  }


  public QuotePriceDetailVO isIncluded(Boolean isIncluded) {
    this.isIncluded = isIncluded;
    return this;
  }

  /**
   * 
   * @return isIncluded
   */
  @javax.annotation.Nullable
  public Boolean getIsIncluded() {
    return isIncluded;
  }

  public void setIsIncluded(Boolean isIncluded) {
    this.isIncluded = isIncluded;
  }


  public QuotePriceDetailVO isQuoted(Boolean isQuoted) {
    this.isQuoted = isQuoted;
    return this;
  }

  /**
   * 
   * @return isQuoted
   */
  @javax.annotation.Nullable
  public Boolean getIsQuoted() {
    return isQuoted;
  }

  public void setIsQuoted(Boolean isQuoted) {
    this.isQuoted = isQuoted;
  }


  public QuotePriceDetailVO parentPriceId(Long parentPriceId) {
    this.parentPriceId = parentPriceId;
    return this;
  }

  /**
   * 
   * @return parentPriceId
   */
  @javax.annotation.Nullable
  public Long getParentPriceId() {
    return parentPriceId;
  }

  public void setParentPriceId(Long parentPriceId) {
    this.parentPriceId = parentPriceId;
  }


  public QuotePriceDetailVO priceId(Long priceId) {
    this.priceId = priceId;
    return this;
  }

  /**
   * 
   * @return priceId
   */
  @javax.annotation.Nullable
  public Long getPriceId() {
    return priceId;
  }

  public void setPriceId(Long priceId) {
    this.priceId = priceId;
  }


  public QuotePriceDetailVO quantity(Object quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return quantity
   */
  @javax.annotation.Nullable
  public Object getQuantity() {
    return quantity;
  }

  public void setQuantity(Object quantity) {
    this.quantity = quantity;
  }


  public QuotePriceDetailVO sellPrice(Object sellPrice) {
    this.sellPrice = sellPrice;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return sellPrice
   */
  @javax.annotation.Nullable
  public Object getSellPrice() {
    return sellPrice;
  }

  public void setSellPrice(Object sellPrice) {
    this.sellPrice = sellPrice;
  }


  public QuotePriceDetailVO shipping(Object shipping) {
    this.shipping = shipping;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return shipping
   */
  @javax.annotation.Nullable
  public Object getShipping() {
    return shipping;
  }

  public void setShipping(Object shipping) {
    this.shipping = shipping;
  }


  public QuotePriceDetailVO source(Object source) {
    this.source = source;
    return this;
  }

  /**
   * Java type: com.noosh.nooshapi.vo.QuotePriceSourceVO
   * @return source
   */
  @javax.annotation.Nullable
  public Object getSource() {
    return source;
  }

  public void setSource(Object source) {
    this.source = source;
  }


  public QuotePriceDetailVO supplier(String supplier) {
    this.supplier = supplier;
    return this;
  }

  /**
   * 
   * @return supplier
   */
  @javax.annotation.Nullable
  public String getSupplier() {
    return supplier;
  }

  public void setSupplier(String supplier) {
    this.supplier = supplier;
  }


  public QuotePriceDetailVO tax(Object tax) {
    this.tax = tax;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return tax
   */
  @javax.annotation.Nullable
  public Object getTax() {
    return tax;
  }

  public void setTax(Object tax) {
    this.tax = tax;
  }


  public QuotePriceDetailVO total(Object total) {
    this.total = total;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return total
   */
  @javax.annotation.Nullable
  public Object getTotal() {
    return total;
  }

  public void setTotal(Object total) {
    this.total = total;
  }


  public QuotePriceDetailVO transactionalCost(Object transactionalCost) {
    this.transactionalCost = transactionalCost;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalCost
   */
  @javax.annotation.Nullable
  public Object getTransactionalCost() {
    return transactionalCost;
  }

  public void setTransactionalCost(Object transactionalCost) {
    this.transactionalCost = transactionalCost;
  }


  public QuotePriceDetailVO transactionalFixed(Object transactionalFixed) {
    this.transactionalFixed = transactionalFixed;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalFixed
   */
  @javax.annotation.Nullable
  public Object getTransactionalFixed() {
    return transactionalFixed;
  }

  public void setTransactionalFixed(Object transactionalFixed) {
    this.transactionalFixed = transactionalFixed;
  }


  public QuotePriceDetailVO transactionalSellPrice(Object transactionalSellPrice) {
    this.transactionalSellPrice = transactionalSellPrice;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalSellPrice
   */
  @javax.annotation.Nullable
  public Object getTransactionalSellPrice() {
    return transactionalSellPrice;
  }

  public void setTransactionalSellPrice(Object transactionalSellPrice) {
    this.transactionalSellPrice = transactionalSellPrice;
  }


  public QuotePriceDetailVO transactionalShipping(Object transactionalShipping) {
    this.transactionalShipping = transactionalShipping;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalShipping
   */
  @javax.annotation.Nullable
  public Object getTransactionalShipping() {
    return transactionalShipping;
  }

  public void setTransactionalShipping(Object transactionalShipping) {
    this.transactionalShipping = transactionalShipping;
  }


  public QuotePriceDetailVO transactionalTax(Object transactionalTax) {
    this.transactionalTax = transactionalTax;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalTax
   */
  @javax.annotation.Nullable
  public Object getTransactionalTax() {
    return transactionalTax;
  }

  public void setTransactionalTax(Object transactionalTax) {
    this.transactionalTax = transactionalTax;
  }


  public QuotePriceDetailVO transactionalTotal(Object transactionalTotal) {
    this.transactionalTotal = transactionalTotal;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalTotal
   */
  @javax.annotation.Nullable
  public Object getTransactionalTotal() {
    return transactionalTotal;
  }

  public void setTransactionalTotal(Object transactionalTotal) {
    this.transactionalTotal = transactionalTotal;
  }


  public QuotePriceDetailVO transactionalVariable(Object transactionalVariable) {
    this.transactionalVariable = transactionalVariable;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalVariable
   */
  @javax.annotation.Nullable
  public Object getTransactionalVariable() {
    return transactionalVariable;
  }

  public void setTransactionalVariable(Object transactionalVariable) {
    this.transactionalVariable = transactionalVariable;
  }


  public QuotePriceDetailVO variable(Object variable) {
    this.variable = variable;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return variable
   */
  @javax.annotation.Nullable
  public Object getVariable() {
    return variable;
  }

  public void setVariable(Object variable) {
    this.variable = variable;
  }


  public QuotePriceDetailVO variablePercent(Object variablePercent) {
    this.variablePercent = variablePercent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return variablePercent
   */
  @javax.annotation.Nullable
  public Object getVariablePercent() {
    return variablePercent;
  }

  public void setVariablePercent(Object variablePercent) {
    this.variablePercent = variablePercent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QuotePriceDetailVO quotePriceDetailVO = (QuotePriceDetailVO) o;
    return Objects.equals(this.breakouts, quotePriceDetailVO.breakouts) &&
        Objects.equals(this.cost, quotePriceDetailVO.cost) &&
        Objects.equals(this.customFields, quotePriceDetailVO.customFields) &&
        Objects.equals(this.fixed, quotePriceDetailVO.fixed) &&
        Objects.equals(this.isChosen, quotePriceDetailVO.isChosen) &&
        Objects.equals(this.isIncluded, quotePriceDetailVO.isIncluded) &&
        Objects.equals(this.isQuoted, quotePriceDetailVO.isQuoted) &&
        Objects.equals(this.parentPriceId, quotePriceDetailVO.parentPriceId) &&
        Objects.equals(this.priceId, quotePriceDetailVO.priceId) &&
        Objects.equals(this.quantity, quotePriceDetailVO.quantity) &&
        Objects.equals(this.sellPrice, quotePriceDetailVO.sellPrice) &&
        Objects.equals(this.shipping, quotePriceDetailVO.shipping) &&
        Objects.equals(this.source, quotePriceDetailVO.source) &&
        Objects.equals(this.supplier, quotePriceDetailVO.supplier) &&
        Objects.equals(this.tax, quotePriceDetailVO.tax) &&
        Objects.equals(this.total, quotePriceDetailVO.total) &&
        Objects.equals(this.transactionalCost, quotePriceDetailVO.transactionalCost) &&
        Objects.equals(this.transactionalFixed, quotePriceDetailVO.transactionalFixed) &&
        Objects.equals(this.transactionalSellPrice, quotePriceDetailVO.transactionalSellPrice) &&
        Objects.equals(this.transactionalShipping, quotePriceDetailVO.transactionalShipping) &&
        Objects.equals(this.transactionalTax, quotePriceDetailVO.transactionalTax) &&
        Objects.equals(this.transactionalTotal, quotePriceDetailVO.transactionalTotal) &&
        Objects.equals(this.transactionalVariable, quotePriceDetailVO.transactionalVariable) &&
        Objects.equals(this.variable, quotePriceDetailVO.variable) &&
        Objects.equals(this.variablePercent, quotePriceDetailVO.variablePercent);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(breakouts, cost, customFields, fixed, isChosen, isIncluded, isQuoted, parentPriceId, priceId, quantity, sellPrice, shipping, source, supplier, tax, total, transactionalCost, transactionalFixed, transactionalSellPrice, transactionalShipping, transactionalTax, transactionalTotal, transactionalVariable, variable, variablePercent);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QuotePriceDetailVO {\n");
    sb.append("    breakouts: ").append(toIndentedString(breakouts)).append("\n");
    sb.append("    cost: ").append(toIndentedString(cost)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    fixed: ").append(toIndentedString(fixed)).append("\n");
    sb.append("    isChosen: ").append(toIndentedString(isChosen)).append("\n");
    sb.append("    isIncluded: ").append(toIndentedString(isIncluded)).append("\n");
    sb.append("    isQuoted: ").append(toIndentedString(isQuoted)).append("\n");
    sb.append("    parentPriceId: ").append(toIndentedString(parentPriceId)).append("\n");
    sb.append("    priceId: ").append(toIndentedString(priceId)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    sellPrice: ").append(toIndentedString(sellPrice)).append("\n");
    sb.append("    shipping: ").append(toIndentedString(shipping)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    supplier: ").append(toIndentedString(supplier)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    transactionalCost: ").append(toIndentedString(transactionalCost)).append("\n");
    sb.append("    transactionalFixed: ").append(toIndentedString(transactionalFixed)).append("\n");
    sb.append("    transactionalSellPrice: ").append(toIndentedString(transactionalSellPrice)).append("\n");
    sb.append("    transactionalShipping: ").append(toIndentedString(transactionalShipping)).append("\n");
    sb.append("    transactionalTax: ").append(toIndentedString(transactionalTax)).append("\n");
    sb.append("    transactionalTotal: ").append(toIndentedString(transactionalTotal)).append("\n");
    sb.append("    transactionalVariable: ").append(toIndentedString(transactionalVariable)).append("\n");
    sb.append("    variable: ").append(toIndentedString(variable)).append("\n");
    sb.append("    variablePercent: ").append(toIndentedString(variablePercent)).append("\n");
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
    openapiFields.add("breakouts");
    openapiFields.add("cost");
    openapiFields.add("custom_fields");
    openapiFields.add("fixed");
    openapiFields.add("is_chosen");
    openapiFields.add("is_included");
    openapiFields.add("is_quoted");
    openapiFields.add("parent_price_id");
    openapiFields.add("price_id");
    openapiFields.add("quantity");
    openapiFields.add("sell_price");
    openapiFields.add("shipping");
    openapiFields.add("source");
    openapiFields.add("supplier");
    openapiFields.add("tax");
    openapiFields.add("total");
    openapiFields.add("transactional_cost");
    openapiFields.add("transactional_fixed");
    openapiFields.add("transactional_sell_price");
    openapiFields.add("transactional_shipping");
    openapiFields.add("transactional_tax");
    openapiFields.add("transactional_total");
    openapiFields.add("transactional_variable");
    openapiFields.add("variable");
    openapiFields.add("variable_percent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QuotePriceDetailVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QuotePriceDetailVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QuotePriceDetailVO is not found in the empty JSON string", QuotePriceDetailVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QuotePriceDetailVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QuotePriceDetailVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("breakouts") != null && !jsonObj.get("breakouts").isJsonNull()) {
        JsonArray jsonArraybreakouts = jsonObj.getAsJsonArray("breakouts");
        if (jsonArraybreakouts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("breakouts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `breakouts` to be an array in the JSON string but got `%s`", jsonObj.get("breakouts").toString()));
          }

          // validate the optional field `breakouts` (array)
          for (int i = 0; i < jsonArraybreakouts.size(); i++) {
            BreakoutVO.validateJsonElement(jsonArraybreakouts.get(i));
          };
        }
      }
      if (jsonObj.get("custom_fields") != null && !jsonObj.get("custom_fields").isJsonNull()) {
        JsonArray jsonArraycustomFields = jsonObj.getAsJsonArray("custom_fields");
        if (jsonArraycustomFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_fields` to be an array in the JSON string but got `%s`", jsonObj.get("custom_fields").toString()));
          }

          // validate the optional field `custom_fields` (array)
          for (int i = 0; i < jsonArraycustomFields.size(); i++) {
            PropertyPaAndAttVO.validateJsonElement(jsonArraycustomFields.get(i));
          };
        }
      }
      if ((jsonObj.get("supplier") != null && !jsonObj.get("supplier").isJsonNull()) && !jsonObj.get("supplier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supplier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supplier").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QuotePriceDetailVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QuotePriceDetailVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QuotePriceDetailVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QuotePriceDetailVO.class));

       return (TypeAdapter<T>) new TypeAdapter<QuotePriceDetailVO>() {
           @Override
           public void write(JsonWriter out, QuotePriceDetailVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QuotePriceDetailVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QuotePriceDetailVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QuotePriceDetailVO
   * @throws IOException if the JSON string is invalid with respect to QuotePriceDetailVO
   */
  public static QuotePriceDetailVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QuotePriceDetailVO.class);
  }

  /**
   * Convert an instance of QuotePriceDetailVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

