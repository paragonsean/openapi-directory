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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.PropertyPaAndAttVO;
import org.openapitools.client.model.QuoteItemDetailVO;
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
 * Java type: com.noosh.nooshapi.vo.QuoteDetailVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QuoteDetailVO {
  public static final String SERIALIZED_NAME_CLIENT = "client";
  @SerializedName(SERIALIZED_NAME_CLIENT)
  private String client;

  public static final String SERIALIZED_NAME_CLIENT_USER_ID = "client_user_id";
  @SerializedName(SERIALIZED_NAME_CLIENT_USER_ID)
  private Long clientUserId;

  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_CREATOR_USER_ID = "creator_user_id";
  @SerializedName(SERIALIZED_NAME_CREATOR_USER_ID)
  private Long creatorUserId;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<PropertyPaAndAttVO> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_GRAND_TOTAL = "grand_total";
  @SerializedName(SERIALIZED_NAME_GRAND_TOTAL)
  private Object grandTotal = null;

  public static final String SERIALIZED_NAME_IS_SHOW_SUPPLIER_INFORMATION = "is_show_supplier_information";
  @SerializedName(SERIALIZED_NAME_IS_SHOW_SUPPLIER_INFORMATION)
  private Boolean isShowSupplierInformation;

  public static final String SERIALIZED_NAME_LAST_UPDATE_BY_USER_ID = "last_update_by_user_id";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE_BY_USER_ID)
  private Long lastUpdateByUserId;

  public static final String SERIALIZED_NAME_PROPOSED_ORDER_COMPLETION_DATE = "proposed_order_completion_date";
  @SerializedName(SERIALIZED_NAME_PROPOSED_ORDER_COMPLETION_DATE)
  private LocalDate proposedOrderCompletionDate;

  public static final String SERIALIZED_NAME_QUOTE_EXPIRATION_DATE = "quote_expiration_date";
  @SerializedName(SERIALIZED_NAME_QUOTE_EXPIRATION_DATE)
  private LocalDate quoteExpirationDate;

  public static final String SERIALIZED_NAME_QUOTE_ID = "quote_id";
  @SerializedName(SERIALIZED_NAME_QUOTE_ID)
  private Long quoteId;

  public static final String SERIALIZED_NAME_QUOTE_ITEMS = "quote_items";
  @SerializedName(SERIALIZED_NAME_QUOTE_ITEMS)
  private List<QuoteItemDetailVO> quoteItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_QUOTE_ITEMS_TOTAL = "quote_items_total";
  @SerializedName(SERIALIZED_NAME_QUOTE_ITEMS_TOTAL)
  private Object quoteItemsTotal = null;

  public static final String SERIALIZED_NAME_QUOTE_TITLE = "quote_title";
  @SerializedName(SERIALIZED_NAME_QUOTE_TITLE)
  private String quoteTitle;

  public static final String SERIALIZED_NAME_SHIPPING = "shipping";
  @SerializedName(SERIALIZED_NAME_SHIPPING)
  private Object shipping = null;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_SUBMIT_DATE = "submit_date";
  @SerializedName(SERIALIZED_NAME_SUBMIT_DATE)
  private LocalDate submitDate;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private Object tax = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_CURRENCY = "transactional_currency";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_CURRENCY)
  private String transactionalCurrency;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_GRAND_TOTAL = "transactional_grand_total";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_GRAND_TOTAL)
  private Object transactionalGrandTotal = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_QUOTE_ITEMS_TOTAL = "transactional_quote_items_total";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_QUOTE_ITEMS_TOTAL)
  private Object transactionalQuoteItemsTotal = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_SHIPPING = "transactional_shipping";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_SHIPPING)
  private Object transactionalShipping = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_TAX = "transactional_tax";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_TAX)
  private Object transactionalTax = null;

  public static final String SERIALIZED_NAME_VAT_CODE = "vat_code";
  @SerializedName(SERIALIZED_NAME_VAT_CODE)
  private String vatCode;

  public static final String SERIALIZED_NAME_VAT_RATE = "vat_rate";
  @SerializedName(SERIALIZED_NAME_VAT_RATE)
  private Object vatRate = null;

  public QuoteDetailVO() {
  }

  public QuoteDetailVO client(String client) {
    this.client = client;
    return this;
  }

  /**
   * 
   * @return client
   */
  @javax.annotation.Nullable
  public String getClient() {
    return client;
  }

  public void setClient(String client) {
    this.client = client;
  }


  public QuoteDetailVO clientUserId(Long clientUserId) {
    this.clientUserId = clientUserId;
    return this;
  }

  /**
   * 
   * @return clientUserId
   */
  @javax.annotation.Nullable
  public Long getClientUserId() {
    return clientUserId;
  }

  public void setClientUserId(Long clientUserId) {
    this.clientUserId = clientUserId;
  }


  public QuoteDetailVO comments(String comments) {
    this.comments = comments;
    return this;
  }

  /**
   * 
   * @return comments
   */
  @javax.annotation.Nullable
  public String getComments() {
    return comments;
  }

  public void setComments(String comments) {
    this.comments = comments;
  }


  public QuoteDetailVO creatorUserId(Long creatorUserId) {
    this.creatorUserId = creatorUserId;
    return this;
  }

  /**
   * 
   * @return creatorUserId
   */
  @javax.annotation.Nullable
  public Long getCreatorUserId() {
    return creatorUserId;
  }

  public void setCreatorUserId(Long creatorUserId) {
    this.creatorUserId = creatorUserId;
  }


  public QuoteDetailVO currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * 
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public QuoteDetailVO customFields(List<PropertyPaAndAttVO> customFields) {
    this.customFields = customFields;
    return this;
  }

  public QuoteDetailVO addCustomFieldsItem(PropertyPaAndAttVO customFieldsItem) {
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


  public QuoteDetailVO description(String description) {
    this.description = description;
    return this;
  }

  /**
   * 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public QuoteDetailVO grandTotal(Object grandTotal) {
    this.grandTotal = grandTotal;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return grandTotal
   */
  @javax.annotation.Nullable
  public Object getGrandTotal() {
    return grandTotal;
  }

  public void setGrandTotal(Object grandTotal) {
    this.grandTotal = grandTotal;
  }


  public QuoteDetailVO isShowSupplierInformation(Boolean isShowSupplierInformation) {
    this.isShowSupplierInformation = isShowSupplierInformation;
    return this;
  }

  /**
   * 
   * @return isShowSupplierInformation
   */
  @javax.annotation.Nullable
  public Boolean getIsShowSupplierInformation() {
    return isShowSupplierInformation;
  }

  public void setIsShowSupplierInformation(Boolean isShowSupplierInformation) {
    this.isShowSupplierInformation = isShowSupplierInformation;
  }


  public QuoteDetailVO lastUpdateByUserId(Long lastUpdateByUserId) {
    this.lastUpdateByUserId = lastUpdateByUserId;
    return this;
  }

  /**
   * 
   * @return lastUpdateByUserId
   */
  @javax.annotation.Nullable
  public Long getLastUpdateByUserId() {
    return lastUpdateByUserId;
  }

  public void setLastUpdateByUserId(Long lastUpdateByUserId) {
    this.lastUpdateByUserId = lastUpdateByUserId;
  }


  public QuoteDetailVO proposedOrderCompletionDate(LocalDate proposedOrderCompletionDate) {
    this.proposedOrderCompletionDate = proposedOrderCompletionDate;
    return this;
  }

  /**
   * 
   * @return proposedOrderCompletionDate
   */
  @javax.annotation.Nullable
  public LocalDate getProposedOrderCompletionDate() {
    return proposedOrderCompletionDate;
  }

  public void setProposedOrderCompletionDate(LocalDate proposedOrderCompletionDate) {
    this.proposedOrderCompletionDate = proposedOrderCompletionDate;
  }


  public QuoteDetailVO quoteExpirationDate(LocalDate quoteExpirationDate) {
    this.quoteExpirationDate = quoteExpirationDate;
    return this;
  }

  /**
   * 
   * @return quoteExpirationDate
   */
  @javax.annotation.Nullable
  public LocalDate getQuoteExpirationDate() {
    return quoteExpirationDate;
  }

  public void setQuoteExpirationDate(LocalDate quoteExpirationDate) {
    this.quoteExpirationDate = quoteExpirationDate;
  }


  public QuoteDetailVO quoteId(Long quoteId) {
    this.quoteId = quoteId;
    return this;
  }

  /**
   * 
   * @return quoteId
   */
  @javax.annotation.Nullable
  public Long getQuoteId() {
    return quoteId;
  }

  public void setQuoteId(Long quoteId) {
    this.quoteId = quoteId;
  }


  public QuoteDetailVO quoteItems(List<QuoteItemDetailVO> quoteItems) {
    this.quoteItems = quoteItems;
    return this;
  }

  public QuoteDetailVO addQuoteItemsItem(QuoteItemDetailVO quoteItemsItem) {
    if (this.quoteItems == null) {
      this.quoteItems = new ArrayList<>();
    }
    this.quoteItems.add(quoteItemsItem);
    return this;
  }

  /**
   * 
   * @return quoteItems
   */
  @javax.annotation.Nullable
  public List<QuoteItemDetailVO> getQuoteItems() {
    return quoteItems;
  }

  public void setQuoteItems(List<QuoteItemDetailVO> quoteItems) {
    this.quoteItems = quoteItems;
  }


  public QuoteDetailVO quoteItemsTotal(Object quoteItemsTotal) {
    this.quoteItemsTotal = quoteItemsTotal;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return quoteItemsTotal
   */
  @javax.annotation.Nullable
  public Object getQuoteItemsTotal() {
    return quoteItemsTotal;
  }

  public void setQuoteItemsTotal(Object quoteItemsTotal) {
    this.quoteItemsTotal = quoteItemsTotal;
  }


  public QuoteDetailVO quoteTitle(String quoteTitle) {
    this.quoteTitle = quoteTitle;
    return this;
  }

  /**
   * 
   * @return quoteTitle
   */
  @javax.annotation.Nullable
  public String getQuoteTitle() {
    return quoteTitle;
  }

  public void setQuoteTitle(String quoteTitle) {
    this.quoteTitle = quoteTitle;
  }


  public QuoteDetailVO shipping(Object shipping) {
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


  public QuoteDetailVO status(String status) {
    this.status = status;
    return this;
  }

  /**
   * 
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public QuoteDetailVO submitDate(LocalDate submitDate) {
    this.submitDate = submitDate;
    return this;
  }

  /**
   * 
   * @return submitDate
   */
  @javax.annotation.Nullable
  public LocalDate getSubmitDate() {
    return submitDate;
  }

  public void setSubmitDate(LocalDate submitDate) {
    this.submitDate = submitDate;
  }


  public QuoteDetailVO tax(Object tax) {
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


  public QuoteDetailVO transactionalCurrency(String transactionalCurrency) {
    this.transactionalCurrency = transactionalCurrency;
    return this;
  }

  /**
   * 
   * @return transactionalCurrency
   */
  @javax.annotation.Nullable
  public String getTransactionalCurrency() {
    return transactionalCurrency;
  }

  public void setTransactionalCurrency(String transactionalCurrency) {
    this.transactionalCurrency = transactionalCurrency;
  }


  public QuoteDetailVO transactionalGrandTotal(Object transactionalGrandTotal) {
    this.transactionalGrandTotal = transactionalGrandTotal;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalGrandTotal
   */
  @javax.annotation.Nullable
  public Object getTransactionalGrandTotal() {
    return transactionalGrandTotal;
  }

  public void setTransactionalGrandTotal(Object transactionalGrandTotal) {
    this.transactionalGrandTotal = transactionalGrandTotal;
  }


  public QuoteDetailVO transactionalQuoteItemsTotal(Object transactionalQuoteItemsTotal) {
    this.transactionalQuoteItemsTotal = transactionalQuoteItemsTotal;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalQuoteItemsTotal
   */
  @javax.annotation.Nullable
  public Object getTransactionalQuoteItemsTotal() {
    return transactionalQuoteItemsTotal;
  }

  public void setTransactionalQuoteItemsTotal(Object transactionalQuoteItemsTotal) {
    this.transactionalQuoteItemsTotal = transactionalQuoteItemsTotal;
  }


  public QuoteDetailVO transactionalShipping(Object transactionalShipping) {
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


  public QuoteDetailVO transactionalTax(Object transactionalTax) {
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


  public QuoteDetailVO vatCode(String vatCode) {
    this.vatCode = vatCode;
    return this;
  }

  /**
   * 
   * @return vatCode
   */
  @javax.annotation.Nullable
  public String getVatCode() {
    return vatCode;
  }

  public void setVatCode(String vatCode) {
    this.vatCode = vatCode;
  }


  public QuoteDetailVO vatRate(Object vatRate) {
    this.vatRate = vatRate;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return vatRate
   */
  @javax.annotation.Nullable
  public Object getVatRate() {
    return vatRate;
  }

  public void setVatRate(Object vatRate) {
    this.vatRate = vatRate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QuoteDetailVO quoteDetailVO = (QuoteDetailVO) o;
    return Objects.equals(this.client, quoteDetailVO.client) &&
        Objects.equals(this.clientUserId, quoteDetailVO.clientUserId) &&
        Objects.equals(this.comments, quoteDetailVO.comments) &&
        Objects.equals(this.creatorUserId, quoteDetailVO.creatorUserId) &&
        Objects.equals(this.currency, quoteDetailVO.currency) &&
        Objects.equals(this.customFields, quoteDetailVO.customFields) &&
        Objects.equals(this.description, quoteDetailVO.description) &&
        Objects.equals(this.grandTotal, quoteDetailVO.grandTotal) &&
        Objects.equals(this.isShowSupplierInformation, quoteDetailVO.isShowSupplierInformation) &&
        Objects.equals(this.lastUpdateByUserId, quoteDetailVO.lastUpdateByUserId) &&
        Objects.equals(this.proposedOrderCompletionDate, quoteDetailVO.proposedOrderCompletionDate) &&
        Objects.equals(this.quoteExpirationDate, quoteDetailVO.quoteExpirationDate) &&
        Objects.equals(this.quoteId, quoteDetailVO.quoteId) &&
        Objects.equals(this.quoteItems, quoteDetailVO.quoteItems) &&
        Objects.equals(this.quoteItemsTotal, quoteDetailVO.quoteItemsTotal) &&
        Objects.equals(this.quoteTitle, quoteDetailVO.quoteTitle) &&
        Objects.equals(this.shipping, quoteDetailVO.shipping) &&
        Objects.equals(this.status, quoteDetailVO.status) &&
        Objects.equals(this.submitDate, quoteDetailVO.submitDate) &&
        Objects.equals(this.tax, quoteDetailVO.tax) &&
        Objects.equals(this.transactionalCurrency, quoteDetailVO.transactionalCurrency) &&
        Objects.equals(this.transactionalGrandTotal, quoteDetailVO.transactionalGrandTotal) &&
        Objects.equals(this.transactionalQuoteItemsTotal, quoteDetailVO.transactionalQuoteItemsTotal) &&
        Objects.equals(this.transactionalShipping, quoteDetailVO.transactionalShipping) &&
        Objects.equals(this.transactionalTax, quoteDetailVO.transactionalTax) &&
        Objects.equals(this.vatCode, quoteDetailVO.vatCode) &&
        Objects.equals(this.vatRate, quoteDetailVO.vatRate);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(client, clientUserId, comments, creatorUserId, currency, customFields, description, grandTotal, isShowSupplierInformation, lastUpdateByUserId, proposedOrderCompletionDate, quoteExpirationDate, quoteId, quoteItems, quoteItemsTotal, quoteTitle, shipping, status, submitDate, tax, transactionalCurrency, transactionalGrandTotal, transactionalQuoteItemsTotal, transactionalShipping, transactionalTax, vatCode, vatRate);
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
    sb.append("class QuoteDetailVO {\n");
    sb.append("    client: ").append(toIndentedString(client)).append("\n");
    sb.append("    clientUserId: ").append(toIndentedString(clientUserId)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    creatorUserId: ").append(toIndentedString(creatorUserId)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    grandTotal: ").append(toIndentedString(grandTotal)).append("\n");
    sb.append("    isShowSupplierInformation: ").append(toIndentedString(isShowSupplierInformation)).append("\n");
    sb.append("    lastUpdateByUserId: ").append(toIndentedString(lastUpdateByUserId)).append("\n");
    sb.append("    proposedOrderCompletionDate: ").append(toIndentedString(proposedOrderCompletionDate)).append("\n");
    sb.append("    quoteExpirationDate: ").append(toIndentedString(quoteExpirationDate)).append("\n");
    sb.append("    quoteId: ").append(toIndentedString(quoteId)).append("\n");
    sb.append("    quoteItems: ").append(toIndentedString(quoteItems)).append("\n");
    sb.append("    quoteItemsTotal: ").append(toIndentedString(quoteItemsTotal)).append("\n");
    sb.append("    quoteTitle: ").append(toIndentedString(quoteTitle)).append("\n");
    sb.append("    shipping: ").append(toIndentedString(shipping)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    submitDate: ").append(toIndentedString(submitDate)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    transactionalCurrency: ").append(toIndentedString(transactionalCurrency)).append("\n");
    sb.append("    transactionalGrandTotal: ").append(toIndentedString(transactionalGrandTotal)).append("\n");
    sb.append("    transactionalQuoteItemsTotal: ").append(toIndentedString(transactionalQuoteItemsTotal)).append("\n");
    sb.append("    transactionalShipping: ").append(toIndentedString(transactionalShipping)).append("\n");
    sb.append("    transactionalTax: ").append(toIndentedString(transactionalTax)).append("\n");
    sb.append("    vatCode: ").append(toIndentedString(vatCode)).append("\n");
    sb.append("    vatRate: ").append(toIndentedString(vatRate)).append("\n");
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
    openapiFields.add("client");
    openapiFields.add("client_user_id");
    openapiFields.add("comments");
    openapiFields.add("creator_user_id");
    openapiFields.add("currency");
    openapiFields.add("custom_fields");
    openapiFields.add("description");
    openapiFields.add("grand_total");
    openapiFields.add("is_show_supplier_information");
    openapiFields.add("last_update_by_user_id");
    openapiFields.add("proposed_order_completion_date");
    openapiFields.add("quote_expiration_date");
    openapiFields.add("quote_id");
    openapiFields.add("quote_items");
    openapiFields.add("quote_items_total");
    openapiFields.add("quote_title");
    openapiFields.add("shipping");
    openapiFields.add("status");
    openapiFields.add("submit_date");
    openapiFields.add("tax");
    openapiFields.add("transactional_currency");
    openapiFields.add("transactional_grand_total");
    openapiFields.add("transactional_quote_items_total");
    openapiFields.add("transactional_shipping");
    openapiFields.add("transactional_tax");
    openapiFields.add("vat_code");
    openapiFields.add("vat_rate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QuoteDetailVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QuoteDetailVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QuoteDetailVO is not found in the empty JSON string", QuoteDetailVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QuoteDetailVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QuoteDetailVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("client") != null && !jsonObj.get("client").isJsonNull()) && !jsonObj.get("client").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `client` to be a primitive type in the JSON string but got `%s`", jsonObj.get("client").toString()));
      }
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
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
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("quote_items") != null && !jsonObj.get("quote_items").isJsonNull()) {
        JsonArray jsonArrayquoteItems = jsonObj.getAsJsonArray("quote_items");
        if (jsonArrayquoteItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("quote_items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `quote_items` to be an array in the JSON string but got `%s`", jsonObj.get("quote_items").toString()));
          }

          // validate the optional field `quote_items` (array)
          for (int i = 0; i < jsonArrayquoteItems.size(); i++) {
            QuoteItemDetailVO.validateJsonElement(jsonArrayquoteItems.get(i));
          };
        }
      }
      if ((jsonObj.get("quote_title") != null && !jsonObj.get("quote_title").isJsonNull()) && !jsonObj.get("quote_title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `quote_title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("quote_title").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("transactional_currency") != null && !jsonObj.get("transactional_currency").isJsonNull()) && !jsonObj.get("transactional_currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactional_currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactional_currency").toString()));
      }
      if ((jsonObj.get("vat_code") != null && !jsonObj.get("vat_code").isJsonNull()) && !jsonObj.get("vat_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vat_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vat_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QuoteDetailVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QuoteDetailVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QuoteDetailVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QuoteDetailVO.class));

       return (TypeAdapter<T>) new TypeAdapter<QuoteDetailVO>() {
           @Override
           public void write(JsonWriter out, QuoteDetailVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QuoteDetailVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QuoteDetailVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QuoteDetailVO
   * @throws IOException if the JSON string is invalid with respect to QuoteDetailVO
   */
  public static QuoteDetailVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QuoteDetailVO.class);
  }

  /**
   * Convert an instance of QuoteDetailVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

