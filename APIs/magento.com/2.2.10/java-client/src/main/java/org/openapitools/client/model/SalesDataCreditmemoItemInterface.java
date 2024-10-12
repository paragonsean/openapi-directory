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
import org.openapitools.client.model.SalesDataCreditmemoItemExtensionInterface;

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
 * Credit memo item interface. After a customer places and pays for an order and an invoice has been issued, the merchant can create a credit memo to refund all or part of the amount paid for any returned or undelivered items. The memo restores funds to the customer account so that the customer can make future purchases. A credit memo item is an invoiced item for which a merchant creates a credit memo.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SalesDataCreditmemoItemInterface {
  public static final String SERIALIZED_NAME_ADDITIONAL_DATA = "additional_data";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_DATA)
  private String additionalData;

  public static final String SERIALIZED_NAME_BASE_COST = "base_cost";
  @SerializedName(SERIALIZED_NAME_BASE_COST)
  private BigDecimal baseCost;

  public static final String SERIALIZED_NAME_BASE_DISCOUNT_AMOUNT = "base_discount_amount";
  @SerializedName(SERIALIZED_NAME_BASE_DISCOUNT_AMOUNT)
  private BigDecimal baseDiscountAmount;

  public static final String SERIALIZED_NAME_BASE_DISCOUNT_TAX_COMPENSATION_AMOUNT = "base_discount_tax_compensation_amount";
  @SerializedName(SERIALIZED_NAME_BASE_DISCOUNT_TAX_COMPENSATION_AMOUNT)
  private BigDecimal baseDiscountTaxCompensationAmount;

  public static final String SERIALIZED_NAME_BASE_PRICE = "base_price";
  @SerializedName(SERIALIZED_NAME_BASE_PRICE)
  private BigDecimal basePrice;

  public static final String SERIALIZED_NAME_BASE_PRICE_INCL_TAX = "base_price_incl_tax";
  @SerializedName(SERIALIZED_NAME_BASE_PRICE_INCL_TAX)
  private BigDecimal basePriceInclTax;

  public static final String SERIALIZED_NAME_BASE_ROW_TOTAL = "base_row_total";
  @SerializedName(SERIALIZED_NAME_BASE_ROW_TOTAL)
  private BigDecimal baseRowTotal;

  public static final String SERIALIZED_NAME_BASE_ROW_TOTAL_INCL_TAX = "base_row_total_incl_tax";
  @SerializedName(SERIALIZED_NAME_BASE_ROW_TOTAL_INCL_TAX)
  private BigDecimal baseRowTotalInclTax;

  public static final String SERIALIZED_NAME_BASE_TAX_AMOUNT = "base_tax_amount";
  @SerializedName(SERIALIZED_NAME_BASE_TAX_AMOUNT)
  private BigDecimal baseTaxAmount;

  public static final String SERIALIZED_NAME_BASE_WEEE_TAX_APPLIED_AMOUNT = "base_weee_tax_applied_amount";
  @SerializedName(SERIALIZED_NAME_BASE_WEEE_TAX_APPLIED_AMOUNT)
  private BigDecimal baseWeeeTaxAppliedAmount;

  public static final String SERIALIZED_NAME_BASE_WEEE_TAX_APPLIED_ROW_AMNT = "base_weee_tax_applied_row_amnt";
  @SerializedName(SERIALIZED_NAME_BASE_WEEE_TAX_APPLIED_ROW_AMNT)
  private BigDecimal baseWeeeTaxAppliedRowAmnt;

  public static final String SERIALIZED_NAME_BASE_WEEE_TAX_DISPOSITION = "base_weee_tax_disposition";
  @SerializedName(SERIALIZED_NAME_BASE_WEEE_TAX_DISPOSITION)
  private BigDecimal baseWeeeTaxDisposition;

  public static final String SERIALIZED_NAME_BASE_WEEE_TAX_ROW_DISPOSITION = "base_weee_tax_row_disposition";
  @SerializedName(SERIALIZED_NAME_BASE_WEEE_TAX_ROW_DISPOSITION)
  private BigDecimal baseWeeeTaxRowDisposition;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISCOUNT_AMOUNT = "discount_amount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_AMOUNT)
  private BigDecimal discountAmount;

  public static final String SERIALIZED_NAME_DISCOUNT_TAX_COMPENSATION_AMOUNT = "discount_tax_compensation_amount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_TAX_COMPENSATION_AMOUNT)
  private BigDecimal discountTaxCompensationAmount;

  public static final String SERIALIZED_NAME_ENTITY_ID = "entity_id";
  @SerializedName(SERIALIZED_NAME_ENTITY_ID)
  private Integer entityId;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private SalesDataCreditmemoItemExtensionInterface extensionAttributes;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ORDER_ITEM_ID = "order_item_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ITEM_ID)
  private Integer orderItemId;

  public static final String SERIALIZED_NAME_PARENT_ID = "parent_id";
  @SerializedName(SERIALIZED_NAME_PARENT_ID)
  private Integer parentId;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private BigDecimal price;

  public static final String SERIALIZED_NAME_PRICE_INCL_TAX = "price_incl_tax";
  @SerializedName(SERIALIZED_NAME_PRICE_INCL_TAX)
  private BigDecimal priceInclTax;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "product_id";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private Integer productId;

  public static final String SERIALIZED_NAME_QTY = "qty";
  @SerializedName(SERIALIZED_NAME_QTY)
  private BigDecimal qty;

  public static final String SERIALIZED_NAME_ROW_TOTAL = "row_total";
  @SerializedName(SERIALIZED_NAME_ROW_TOTAL)
  private BigDecimal rowTotal;

  public static final String SERIALIZED_NAME_ROW_TOTAL_INCL_TAX = "row_total_incl_tax";
  @SerializedName(SERIALIZED_NAME_ROW_TOTAL_INCL_TAX)
  private BigDecimal rowTotalInclTax;

  public static final String SERIALIZED_NAME_SKU = "sku";
  @SerializedName(SERIALIZED_NAME_SKU)
  private String sku;

  public static final String SERIALIZED_NAME_TAX_AMOUNT = "tax_amount";
  @SerializedName(SERIALIZED_NAME_TAX_AMOUNT)
  private BigDecimal taxAmount;

  public static final String SERIALIZED_NAME_WEEE_TAX_APPLIED = "weee_tax_applied";
  @SerializedName(SERIALIZED_NAME_WEEE_TAX_APPLIED)
  private String weeeTaxApplied;

  public static final String SERIALIZED_NAME_WEEE_TAX_APPLIED_AMOUNT = "weee_tax_applied_amount";
  @SerializedName(SERIALIZED_NAME_WEEE_TAX_APPLIED_AMOUNT)
  private BigDecimal weeeTaxAppliedAmount;

  public static final String SERIALIZED_NAME_WEEE_TAX_APPLIED_ROW_AMOUNT = "weee_tax_applied_row_amount";
  @SerializedName(SERIALIZED_NAME_WEEE_TAX_APPLIED_ROW_AMOUNT)
  private BigDecimal weeeTaxAppliedRowAmount;

  public static final String SERIALIZED_NAME_WEEE_TAX_DISPOSITION = "weee_tax_disposition";
  @SerializedName(SERIALIZED_NAME_WEEE_TAX_DISPOSITION)
  private BigDecimal weeeTaxDisposition;

  public static final String SERIALIZED_NAME_WEEE_TAX_ROW_DISPOSITION = "weee_tax_row_disposition";
  @SerializedName(SERIALIZED_NAME_WEEE_TAX_ROW_DISPOSITION)
  private BigDecimal weeeTaxRowDisposition;

  public SalesDataCreditmemoItemInterface() {
  }

  public SalesDataCreditmemoItemInterface additionalData(String additionalData) {
    this.additionalData = additionalData;
    return this;
  }

  /**
   * Additional data.
   * @return additionalData
   */
  @javax.annotation.Nullable
  public String getAdditionalData() {
    return additionalData;
  }

  public void setAdditionalData(String additionalData) {
    this.additionalData = additionalData;
  }


  public SalesDataCreditmemoItemInterface baseCost(BigDecimal baseCost) {
    this.baseCost = baseCost;
    return this;
  }

  /**
   * The base cost for a credit memo item.
   * @return baseCost
   */
  @javax.annotation.Nonnull
  public BigDecimal getBaseCost() {
    return baseCost;
  }

  public void setBaseCost(BigDecimal baseCost) {
    this.baseCost = baseCost;
  }


  public SalesDataCreditmemoItemInterface baseDiscountAmount(BigDecimal baseDiscountAmount) {
    this.baseDiscountAmount = baseDiscountAmount;
    return this;
  }

  /**
   * The base discount amount for a credit memo item.
   * @return baseDiscountAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseDiscountAmount() {
    return baseDiscountAmount;
  }

  public void setBaseDiscountAmount(BigDecimal baseDiscountAmount) {
    this.baseDiscountAmount = baseDiscountAmount;
  }


  public SalesDataCreditmemoItemInterface baseDiscountTaxCompensationAmount(BigDecimal baseDiscountTaxCompensationAmount) {
    this.baseDiscountTaxCompensationAmount = baseDiscountTaxCompensationAmount;
    return this;
  }

  /**
   * The base discount tax compensation amount for a credit memo item.
   * @return baseDiscountTaxCompensationAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseDiscountTaxCompensationAmount() {
    return baseDiscountTaxCompensationAmount;
  }

  public void setBaseDiscountTaxCompensationAmount(BigDecimal baseDiscountTaxCompensationAmount) {
    this.baseDiscountTaxCompensationAmount = baseDiscountTaxCompensationAmount;
  }


  public SalesDataCreditmemoItemInterface basePrice(BigDecimal basePrice) {
    this.basePrice = basePrice;
    return this;
  }

  /**
   * The base price for a credit memo item.
   * @return basePrice
   */
  @javax.annotation.Nonnull
  public BigDecimal getBasePrice() {
    return basePrice;
  }

  public void setBasePrice(BigDecimal basePrice) {
    this.basePrice = basePrice;
  }


  public SalesDataCreditmemoItemInterface basePriceInclTax(BigDecimal basePriceInclTax) {
    this.basePriceInclTax = basePriceInclTax;
    return this;
  }

  /**
   * Base price including tax.
   * @return basePriceInclTax
   */
  @javax.annotation.Nullable
  public BigDecimal getBasePriceInclTax() {
    return basePriceInclTax;
  }

  public void setBasePriceInclTax(BigDecimal basePriceInclTax) {
    this.basePriceInclTax = basePriceInclTax;
  }


  public SalesDataCreditmemoItemInterface baseRowTotal(BigDecimal baseRowTotal) {
    this.baseRowTotal = baseRowTotal;
    return this;
  }

  /**
   * Base row total.
   * @return baseRowTotal
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseRowTotal() {
    return baseRowTotal;
  }

  public void setBaseRowTotal(BigDecimal baseRowTotal) {
    this.baseRowTotal = baseRowTotal;
  }


  public SalesDataCreditmemoItemInterface baseRowTotalInclTax(BigDecimal baseRowTotalInclTax) {
    this.baseRowTotalInclTax = baseRowTotalInclTax;
    return this;
  }

  /**
   * Base row total including tax.
   * @return baseRowTotalInclTax
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseRowTotalInclTax() {
    return baseRowTotalInclTax;
  }

  public void setBaseRowTotalInclTax(BigDecimal baseRowTotalInclTax) {
    this.baseRowTotalInclTax = baseRowTotalInclTax;
  }


  public SalesDataCreditmemoItemInterface baseTaxAmount(BigDecimal baseTaxAmount) {
    this.baseTaxAmount = baseTaxAmount;
    return this;
  }

  /**
   * Base tax amount.
   * @return baseTaxAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseTaxAmount() {
    return baseTaxAmount;
  }

  public void setBaseTaxAmount(BigDecimal baseTaxAmount) {
    this.baseTaxAmount = baseTaxAmount;
  }


  public SalesDataCreditmemoItemInterface baseWeeeTaxAppliedAmount(BigDecimal baseWeeeTaxAppliedAmount) {
    this.baseWeeeTaxAppliedAmount = baseWeeeTaxAppliedAmount;
    return this;
  }

  /**
   * Base WEEE tax applied amount.
   * @return baseWeeeTaxAppliedAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseWeeeTaxAppliedAmount() {
    return baseWeeeTaxAppliedAmount;
  }

  public void setBaseWeeeTaxAppliedAmount(BigDecimal baseWeeeTaxAppliedAmount) {
    this.baseWeeeTaxAppliedAmount = baseWeeeTaxAppliedAmount;
  }


  public SalesDataCreditmemoItemInterface baseWeeeTaxAppliedRowAmnt(BigDecimal baseWeeeTaxAppliedRowAmnt) {
    this.baseWeeeTaxAppliedRowAmnt = baseWeeeTaxAppliedRowAmnt;
    return this;
  }

  /**
   * Base WEEE tax applied row amount.
   * @return baseWeeeTaxAppliedRowAmnt
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseWeeeTaxAppliedRowAmnt() {
    return baseWeeeTaxAppliedRowAmnt;
  }

  public void setBaseWeeeTaxAppliedRowAmnt(BigDecimal baseWeeeTaxAppliedRowAmnt) {
    this.baseWeeeTaxAppliedRowAmnt = baseWeeeTaxAppliedRowAmnt;
  }


  public SalesDataCreditmemoItemInterface baseWeeeTaxDisposition(BigDecimal baseWeeeTaxDisposition) {
    this.baseWeeeTaxDisposition = baseWeeeTaxDisposition;
    return this;
  }

  /**
   * Base WEEE tax disposition.
   * @return baseWeeeTaxDisposition
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseWeeeTaxDisposition() {
    return baseWeeeTaxDisposition;
  }

  public void setBaseWeeeTaxDisposition(BigDecimal baseWeeeTaxDisposition) {
    this.baseWeeeTaxDisposition = baseWeeeTaxDisposition;
  }


  public SalesDataCreditmemoItemInterface baseWeeeTaxRowDisposition(BigDecimal baseWeeeTaxRowDisposition) {
    this.baseWeeeTaxRowDisposition = baseWeeeTaxRowDisposition;
    return this;
  }

  /**
   * Base WEEE tax row disposition.
   * @return baseWeeeTaxRowDisposition
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseWeeeTaxRowDisposition() {
    return baseWeeeTaxRowDisposition;
  }

  public void setBaseWeeeTaxRowDisposition(BigDecimal baseWeeeTaxRowDisposition) {
    this.baseWeeeTaxRowDisposition = baseWeeeTaxRowDisposition;
  }


  public SalesDataCreditmemoItemInterface description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public SalesDataCreditmemoItemInterface discountAmount(BigDecimal discountAmount) {
    this.discountAmount = discountAmount;
    return this;
  }

  /**
   * Discount amount.
   * @return discountAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getDiscountAmount() {
    return discountAmount;
  }

  public void setDiscountAmount(BigDecimal discountAmount) {
    this.discountAmount = discountAmount;
  }


  public SalesDataCreditmemoItemInterface discountTaxCompensationAmount(BigDecimal discountTaxCompensationAmount) {
    this.discountTaxCompensationAmount = discountTaxCompensationAmount;
    return this;
  }

  /**
   * Discount tax compensation amount.
   * @return discountTaxCompensationAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getDiscountTaxCompensationAmount() {
    return discountTaxCompensationAmount;
  }

  public void setDiscountTaxCompensationAmount(BigDecimal discountTaxCompensationAmount) {
    this.discountTaxCompensationAmount = discountTaxCompensationAmount;
  }


  public SalesDataCreditmemoItemInterface entityId(Integer entityId) {
    this.entityId = entityId;
    return this;
  }

  /**
   * Credit memo item ID.
   * @return entityId
   */
  @javax.annotation.Nonnull
  public Integer getEntityId() {
    return entityId;
  }

  public void setEntityId(Integer entityId) {
    this.entityId = entityId;
  }


  public SalesDataCreditmemoItemInterface extensionAttributes(SalesDataCreditmemoItemExtensionInterface extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * Get extensionAttributes
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public SalesDataCreditmemoItemExtensionInterface getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(SalesDataCreditmemoItemExtensionInterface extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public SalesDataCreditmemoItemInterface name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public SalesDataCreditmemoItemInterface orderItemId(Integer orderItemId) {
    this.orderItemId = orderItemId;
    return this;
  }

  /**
   * Order item ID.
   * @return orderItemId
   */
  @javax.annotation.Nonnull
  public Integer getOrderItemId() {
    return orderItemId;
  }

  public void setOrderItemId(Integer orderItemId) {
    this.orderItemId = orderItemId;
  }


  public SalesDataCreditmemoItemInterface parentId(Integer parentId) {
    this.parentId = parentId;
    return this;
  }

  /**
   * Parent ID.
   * @return parentId
   */
  @javax.annotation.Nullable
  public Integer getParentId() {
    return parentId;
  }

  public void setParentId(Integer parentId) {
    this.parentId = parentId;
  }


  public SalesDataCreditmemoItemInterface price(BigDecimal price) {
    this.price = price;
    return this;
  }

  /**
   * Price.
   * @return price
   */
  @javax.annotation.Nullable
  public BigDecimal getPrice() {
    return price;
  }

  public void setPrice(BigDecimal price) {
    this.price = price;
  }


  public SalesDataCreditmemoItemInterface priceInclTax(BigDecimal priceInclTax) {
    this.priceInclTax = priceInclTax;
    return this;
  }

  /**
   * Price including tax.
   * @return priceInclTax
   */
  @javax.annotation.Nullable
  public BigDecimal getPriceInclTax() {
    return priceInclTax;
  }

  public void setPriceInclTax(BigDecimal priceInclTax) {
    this.priceInclTax = priceInclTax;
  }


  public SalesDataCreditmemoItemInterface productId(Integer productId) {
    this.productId = productId;
    return this;
  }

  /**
   * Product ID.
   * @return productId
   */
  @javax.annotation.Nullable
  public Integer getProductId() {
    return productId;
  }

  public void setProductId(Integer productId) {
    this.productId = productId;
  }


  public SalesDataCreditmemoItemInterface qty(BigDecimal qty) {
    this.qty = qty;
    return this;
  }

  /**
   * Quantity.
   * @return qty
   */
  @javax.annotation.Nonnull
  public BigDecimal getQty() {
    return qty;
  }

  public void setQty(BigDecimal qty) {
    this.qty = qty;
  }


  public SalesDataCreditmemoItemInterface rowTotal(BigDecimal rowTotal) {
    this.rowTotal = rowTotal;
    return this;
  }

  /**
   * Row total.
   * @return rowTotal
   */
  @javax.annotation.Nullable
  public BigDecimal getRowTotal() {
    return rowTotal;
  }

  public void setRowTotal(BigDecimal rowTotal) {
    this.rowTotal = rowTotal;
  }


  public SalesDataCreditmemoItemInterface rowTotalInclTax(BigDecimal rowTotalInclTax) {
    this.rowTotalInclTax = rowTotalInclTax;
    return this;
  }

  /**
   * Row total including tax.
   * @return rowTotalInclTax
   */
  @javax.annotation.Nullable
  public BigDecimal getRowTotalInclTax() {
    return rowTotalInclTax;
  }

  public void setRowTotalInclTax(BigDecimal rowTotalInclTax) {
    this.rowTotalInclTax = rowTotalInclTax;
  }


  public SalesDataCreditmemoItemInterface sku(String sku) {
    this.sku = sku;
    return this;
  }

  /**
   * SKU.
   * @return sku
   */
  @javax.annotation.Nullable
  public String getSku() {
    return sku;
  }

  public void setSku(String sku) {
    this.sku = sku;
  }


  public SalesDataCreditmemoItemInterface taxAmount(BigDecimal taxAmount) {
    this.taxAmount = taxAmount;
    return this;
  }

  /**
   * Tax amount.
   * @return taxAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getTaxAmount() {
    return taxAmount;
  }

  public void setTaxAmount(BigDecimal taxAmount) {
    this.taxAmount = taxAmount;
  }


  public SalesDataCreditmemoItemInterface weeeTaxApplied(String weeeTaxApplied) {
    this.weeeTaxApplied = weeeTaxApplied;
    return this;
  }

  /**
   * WEEE tax applied.
   * @return weeeTaxApplied
   */
  @javax.annotation.Nullable
  public String getWeeeTaxApplied() {
    return weeeTaxApplied;
  }

  public void setWeeeTaxApplied(String weeeTaxApplied) {
    this.weeeTaxApplied = weeeTaxApplied;
  }


  public SalesDataCreditmemoItemInterface weeeTaxAppliedAmount(BigDecimal weeeTaxAppliedAmount) {
    this.weeeTaxAppliedAmount = weeeTaxAppliedAmount;
    return this;
  }

  /**
   * WEEE tax applied amount.
   * @return weeeTaxAppliedAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getWeeeTaxAppliedAmount() {
    return weeeTaxAppliedAmount;
  }

  public void setWeeeTaxAppliedAmount(BigDecimal weeeTaxAppliedAmount) {
    this.weeeTaxAppliedAmount = weeeTaxAppliedAmount;
  }


  public SalesDataCreditmemoItemInterface weeeTaxAppliedRowAmount(BigDecimal weeeTaxAppliedRowAmount) {
    this.weeeTaxAppliedRowAmount = weeeTaxAppliedRowAmount;
    return this;
  }

  /**
   * WEEE tax applied row amount.
   * @return weeeTaxAppliedRowAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getWeeeTaxAppliedRowAmount() {
    return weeeTaxAppliedRowAmount;
  }

  public void setWeeeTaxAppliedRowAmount(BigDecimal weeeTaxAppliedRowAmount) {
    this.weeeTaxAppliedRowAmount = weeeTaxAppliedRowAmount;
  }


  public SalesDataCreditmemoItemInterface weeeTaxDisposition(BigDecimal weeeTaxDisposition) {
    this.weeeTaxDisposition = weeeTaxDisposition;
    return this;
  }

  /**
   * WEEE tax disposition.
   * @return weeeTaxDisposition
   */
  @javax.annotation.Nullable
  public BigDecimal getWeeeTaxDisposition() {
    return weeeTaxDisposition;
  }

  public void setWeeeTaxDisposition(BigDecimal weeeTaxDisposition) {
    this.weeeTaxDisposition = weeeTaxDisposition;
  }


  public SalesDataCreditmemoItemInterface weeeTaxRowDisposition(BigDecimal weeeTaxRowDisposition) {
    this.weeeTaxRowDisposition = weeeTaxRowDisposition;
    return this;
  }

  /**
   * WEEE tax row disposition.
   * @return weeeTaxRowDisposition
   */
  @javax.annotation.Nullable
  public BigDecimal getWeeeTaxRowDisposition() {
    return weeeTaxRowDisposition;
  }

  public void setWeeeTaxRowDisposition(BigDecimal weeeTaxRowDisposition) {
    this.weeeTaxRowDisposition = weeeTaxRowDisposition;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SalesDataCreditmemoItemInterface salesDataCreditmemoItemInterface = (SalesDataCreditmemoItemInterface) o;
    return Objects.equals(this.additionalData, salesDataCreditmemoItemInterface.additionalData) &&
        Objects.equals(this.baseCost, salesDataCreditmemoItemInterface.baseCost) &&
        Objects.equals(this.baseDiscountAmount, salesDataCreditmemoItemInterface.baseDiscountAmount) &&
        Objects.equals(this.baseDiscountTaxCompensationAmount, salesDataCreditmemoItemInterface.baseDiscountTaxCompensationAmount) &&
        Objects.equals(this.basePrice, salesDataCreditmemoItemInterface.basePrice) &&
        Objects.equals(this.basePriceInclTax, salesDataCreditmemoItemInterface.basePriceInclTax) &&
        Objects.equals(this.baseRowTotal, salesDataCreditmemoItemInterface.baseRowTotal) &&
        Objects.equals(this.baseRowTotalInclTax, salesDataCreditmemoItemInterface.baseRowTotalInclTax) &&
        Objects.equals(this.baseTaxAmount, salesDataCreditmemoItemInterface.baseTaxAmount) &&
        Objects.equals(this.baseWeeeTaxAppliedAmount, salesDataCreditmemoItemInterface.baseWeeeTaxAppliedAmount) &&
        Objects.equals(this.baseWeeeTaxAppliedRowAmnt, salesDataCreditmemoItemInterface.baseWeeeTaxAppliedRowAmnt) &&
        Objects.equals(this.baseWeeeTaxDisposition, salesDataCreditmemoItemInterface.baseWeeeTaxDisposition) &&
        Objects.equals(this.baseWeeeTaxRowDisposition, salesDataCreditmemoItemInterface.baseWeeeTaxRowDisposition) &&
        Objects.equals(this.description, salesDataCreditmemoItemInterface.description) &&
        Objects.equals(this.discountAmount, salesDataCreditmemoItemInterface.discountAmount) &&
        Objects.equals(this.discountTaxCompensationAmount, salesDataCreditmemoItemInterface.discountTaxCompensationAmount) &&
        Objects.equals(this.entityId, salesDataCreditmemoItemInterface.entityId) &&
        Objects.equals(this.extensionAttributes, salesDataCreditmemoItemInterface.extensionAttributes) &&
        Objects.equals(this.name, salesDataCreditmemoItemInterface.name) &&
        Objects.equals(this.orderItemId, salesDataCreditmemoItemInterface.orderItemId) &&
        Objects.equals(this.parentId, salesDataCreditmemoItemInterface.parentId) &&
        Objects.equals(this.price, salesDataCreditmemoItemInterface.price) &&
        Objects.equals(this.priceInclTax, salesDataCreditmemoItemInterface.priceInclTax) &&
        Objects.equals(this.productId, salesDataCreditmemoItemInterface.productId) &&
        Objects.equals(this.qty, salesDataCreditmemoItemInterface.qty) &&
        Objects.equals(this.rowTotal, salesDataCreditmemoItemInterface.rowTotal) &&
        Objects.equals(this.rowTotalInclTax, salesDataCreditmemoItemInterface.rowTotalInclTax) &&
        Objects.equals(this.sku, salesDataCreditmemoItemInterface.sku) &&
        Objects.equals(this.taxAmount, salesDataCreditmemoItemInterface.taxAmount) &&
        Objects.equals(this.weeeTaxApplied, salesDataCreditmemoItemInterface.weeeTaxApplied) &&
        Objects.equals(this.weeeTaxAppliedAmount, salesDataCreditmemoItemInterface.weeeTaxAppliedAmount) &&
        Objects.equals(this.weeeTaxAppliedRowAmount, salesDataCreditmemoItemInterface.weeeTaxAppliedRowAmount) &&
        Objects.equals(this.weeeTaxDisposition, salesDataCreditmemoItemInterface.weeeTaxDisposition) &&
        Objects.equals(this.weeeTaxRowDisposition, salesDataCreditmemoItemInterface.weeeTaxRowDisposition);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalData, baseCost, baseDiscountAmount, baseDiscountTaxCompensationAmount, basePrice, basePriceInclTax, baseRowTotal, baseRowTotalInclTax, baseTaxAmount, baseWeeeTaxAppliedAmount, baseWeeeTaxAppliedRowAmnt, baseWeeeTaxDisposition, baseWeeeTaxRowDisposition, description, discountAmount, discountTaxCompensationAmount, entityId, extensionAttributes, name, orderItemId, parentId, price, priceInclTax, productId, qty, rowTotal, rowTotalInclTax, sku, taxAmount, weeeTaxApplied, weeeTaxAppliedAmount, weeeTaxAppliedRowAmount, weeeTaxDisposition, weeeTaxRowDisposition);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SalesDataCreditmemoItemInterface {\n");
    sb.append("    additionalData: ").append(toIndentedString(additionalData)).append("\n");
    sb.append("    baseCost: ").append(toIndentedString(baseCost)).append("\n");
    sb.append("    baseDiscountAmount: ").append(toIndentedString(baseDiscountAmount)).append("\n");
    sb.append("    baseDiscountTaxCompensationAmount: ").append(toIndentedString(baseDiscountTaxCompensationAmount)).append("\n");
    sb.append("    basePrice: ").append(toIndentedString(basePrice)).append("\n");
    sb.append("    basePriceInclTax: ").append(toIndentedString(basePriceInclTax)).append("\n");
    sb.append("    baseRowTotal: ").append(toIndentedString(baseRowTotal)).append("\n");
    sb.append("    baseRowTotalInclTax: ").append(toIndentedString(baseRowTotalInclTax)).append("\n");
    sb.append("    baseTaxAmount: ").append(toIndentedString(baseTaxAmount)).append("\n");
    sb.append("    baseWeeeTaxAppliedAmount: ").append(toIndentedString(baseWeeeTaxAppliedAmount)).append("\n");
    sb.append("    baseWeeeTaxAppliedRowAmnt: ").append(toIndentedString(baseWeeeTaxAppliedRowAmnt)).append("\n");
    sb.append("    baseWeeeTaxDisposition: ").append(toIndentedString(baseWeeeTaxDisposition)).append("\n");
    sb.append("    baseWeeeTaxRowDisposition: ").append(toIndentedString(baseWeeeTaxRowDisposition)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    discountAmount: ").append(toIndentedString(discountAmount)).append("\n");
    sb.append("    discountTaxCompensationAmount: ").append(toIndentedString(discountTaxCompensationAmount)).append("\n");
    sb.append("    entityId: ").append(toIndentedString(entityId)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    orderItemId: ").append(toIndentedString(orderItemId)).append("\n");
    sb.append("    parentId: ").append(toIndentedString(parentId)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    priceInclTax: ").append(toIndentedString(priceInclTax)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    qty: ").append(toIndentedString(qty)).append("\n");
    sb.append("    rowTotal: ").append(toIndentedString(rowTotal)).append("\n");
    sb.append("    rowTotalInclTax: ").append(toIndentedString(rowTotalInclTax)).append("\n");
    sb.append("    sku: ").append(toIndentedString(sku)).append("\n");
    sb.append("    taxAmount: ").append(toIndentedString(taxAmount)).append("\n");
    sb.append("    weeeTaxApplied: ").append(toIndentedString(weeeTaxApplied)).append("\n");
    sb.append("    weeeTaxAppliedAmount: ").append(toIndentedString(weeeTaxAppliedAmount)).append("\n");
    sb.append("    weeeTaxAppliedRowAmount: ").append(toIndentedString(weeeTaxAppliedRowAmount)).append("\n");
    sb.append("    weeeTaxDisposition: ").append(toIndentedString(weeeTaxDisposition)).append("\n");
    sb.append("    weeeTaxRowDisposition: ").append(toIndentedString(weeeTaxRowDisposition)).append("\n");
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
    openapiFields.add("additional_data");
    openapiFields.add("base_cost");
    openapiFields.add("base_discount_amount");
    openapiFields.add("base_discount_tax_compensation_amount");
    openapiFields.add("base_price");
    openapiFields.add("base_price_incl_tax");
    openapiFields.add("base_row_total");
    openapiFields.add("base_row_total_incl_tax");
    openapiFields.add("base_tax_amount");
    openapiFields.add("base_weee_tax_applied_amount");
    openapiFields.add("base_weee_tax_applied_row_amnt");
    openapiFields.add("base_weee_tax_disposition");
    openapiFields.add("base_weee_tax_row_disposition");
    openapiFields.add("description");
    openapiFields.add("discount_amount");
    openapiFields.add("discount_tax_compensation_amount");
    openapiFields.add("entity_id");
    openapiFields.add("extension_attributes");
    openapiFields.add("name");
    openapiFields.add("order_item_id");
    openapiFields.add("parent_id");
    openapiFields.add("price");
    openapiFields.add("price_incl_tax");
    openapiFields.add("product_id");
    openapiFields.add("qty");
    openapiFields.add("row_total");
    openapiFields.add("row_total_incl_tax");
    openapiFields.add("sku");
    openapiFields.add("tax_amount");
    openapiFields.add("weee_tax_applied");
    openapiFields.add("weee_tax_applied_amount");
    openapiFields.add("weee_tax_applied_row_amount");
    openapiFields.add("weee_tax_disposition");
    openapiFields.add("weee_tax_row_disposition");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("base_cost");
    openapiRequiredFields.add("base_price");
    openapiRequiredFields.add("entity_id");
    openapiRequiredFields.add("order_item_id");
    openapiRequiredFields.add("qty");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SalesDataCreditmemoItemInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SalesDataCreditmemoItemInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SalesDataCreditmemoItemInterface is not found in the empty JSON string", SalesDataCreditmemoItemInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SalesDataCreditmemoItemInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SalesDataCreditmemoItemInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SalesDataCreditmemoItemInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("additional_data") != null && !jsonObj.get("additional_data").isJsonNull()) && !jsonObj.get("additional_data").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `additional_data` to be a primitive type in the JSON string but got `%s`", jsonObj.get("additional_data").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `extension_attributes`
      if (jsonObj.get("extension_attributes") != null && !jsonObj.get("extension_attributes").isJsonNull()) {
        SalesDataCreditmemoItemExtensionInterface.validateJsonElement(jsonObj.get("extension_attributes"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("sku") != null && !jsonObj.get("sku").isJsonNull()) && !jsonObj.get("sku").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sku` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sku").toString()));
      }
      if ((jsonObj.get("weee_tax_applied") != null && !jsonObj.get("weee_tax_applied").isJsonNull()) && !jsonObj.get("weee_tax_applied").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `weee_tax_applied` to be a primitive type in the JSON string but got `%s`", jsonObj.get("weee_tax_applied").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SalesDataCreditmemoItemInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SalesDataCreditmemoItemInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SalesDataCreditmemoItemInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SalesDataCreditmemoItemInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<SalesDataCreditmemoItemInterface>() {
           @Override
           public void write(JsonWriter out, SalesDataCreditmemoItemInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SalesDataCreditmemoItemInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SalesDataCreditmemoItemInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SalesDataCreditmemoItemInterface
   * @throws IOException if the JSON string is invalid with respect to SalesDataCreditmemoItemInterface
   */
  public static SalesDataCreditmemoItemInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SalesDataCreditmemoItemInterface.class);
  }

  /**
   * Convert an instance of SalesDataCreditmemoItemInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

