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
import org.openapitools.client.model.InvoiceItemSimpleVO;
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
 * Java type: com.noosh.nooshapi.vo.InvoiceSimpleVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InvoiceSimpleVO {
  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<PropertyPaAndAttVO> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_GRAND_TOTAL = "grand_total";
  @SerializedName(SERIALIZED_NAME_GRAND_TOTAL)
  private Object grandTotal = null;

  public static final String SERIALIZED_NAME_INVOICE_DATE = "invoice_date";
  @SerializedName(SERIALIZED_NAME_INVOICE_DATE)
  private LocalDate invoiceDate;

  public static final String SERIALIZED_NAME_INVOICE_DUE_DATE = "invoice_due_date";
  @SerializedName(SERIALIZED_NAME_INVOICE_DUE_DATE)
  private LocalDate invoiceDueDate;

  public static final String SERIALIZED_NAME_INVOICE_ID = "invoice_id";
  @SerializedName(SERIALIZED_NAME_INVOICE_ID)
  private Long invoiceId;

  public static final String SERIALIZED_NAME_INVOICE_NUMBER = "invoice_number";
  @SerializedName(SERIALIZED_NAME_INVOICE_NUMBER)
  private String invoiceNumber;

  public static final String SERIALIZED_NAME_INVOICE_TO = "invoice_to";
  @SerializedName(SERIALIZED_NAME_INVOICE_TO)
  private String invoiceTo;

  public static final String SERIALIZED_NAME_IS_FINAL = "is_final";
  @SerializedName(SERIALIZED_NAME_IS_FINAL)
  private Integer isFinal;

  public static final String SERIALIZED_NAME_IS_NON_BILLABLE = "is_nonBillable";
  @SerializedName(SERIALIZED_NAME_IS_NON_BILLABLE)
  private Integer isNonBillable;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<InvoiceItemSimpleVO> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_ORDER_REFERENCE = "order_reference";
  @SerializedName(SERIALIZED_NAME_ORDER_REFERENCE)
  private String orderReference;

  public static final String SERIALIZED_NAME_ORDER_TITLE = "order_title";
  @SerializedName(SERIALIZED_NAME_ORDER_TITLE)
  private String orderTitle;

  public static final String SERIALIZED_NAME_PAYMENT_METHOD = "payment_method";
  @SerializedName(SERIALIZED_NAME_PAYMENT_METHOD)
  private String paymentMethod;

  public static final String SERIALIZED_NAME_PREPARED_BY = "prepared_by";
  @SerializedName(SERIALIZED_NAME_PREPARED_BY)
  private String preparedBy;

  public static final String SERIALIZED_NAME_PROJECT_NUMBER = "project_number";
  @SerializedName(SERIALIZED_NAME_PROJECT_NUMBER)
  private Long projectNumber;

  public static final String SERIALIZED_NAME_REFERENCE_NUMBER = "reference_number";
  @SerializedName(SERIALIZED_NAME_REFERENCE_NUMBER)
  private String referenceNumber;

  public static final String SERIALIZED_NAME_SHIPPING = "shipping";
  @SerializedName(SERIALIZED_NAME_SHIPPING)
  private Object shipping = null;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_SUB_TOTAL = "sub_total";
  @SerializedName(SERIALIZED_NAME_SUB_TOTAL)
  private Object subTotal = null;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private Object tax = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_CURRENCY = "transactional_currency";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_CURRENCY)
  private String transactionalCurrency;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_GRAND_TOTAL = "transactional_grand_total";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_GRAND_TOTAL)
  private Object transactionalGrandTotal = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_SHIPPING = "transactional_shipping";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_SHIPPING)
  private Object transactionalShipping = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_SUB_TOTAL = "transactional_sub_total";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_SUB_TOTAL)
  private Object transactionalSubTotal = null;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_TAX = "transactional_tax";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_TAX)
  private Object transactionalTax = null;

  public InvoiceSimpleVO() {
  }

  public InvoiceSimpleVO comments(String comments) {
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


  public InvoiceSimpleVO currency(String currency) {
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


  public InvoiceSimpleVO customFields(List<PropertyPaAndAttVO> customFields) {
    this.customFields = customFields;
    return this;
  }

  public InvoiceSimpleVO addCustomFieldsItem(PropertyPaAndAttVO customFieldsItem) {
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


  public InvoiceSimpleVO grandTotal(Object grandTotal) {
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


  public InvoiceSimpleVO invoiceDate(LocalDate invoiceDate) {
    this.invoiceDate = invoiceDate;
    return this;
  }

  /**
   * 
   * @return invoiceDate
   */
  @javax.annotation.Nullable
  public LocalDate getInvoiceDate() {
    return invoiceDate;
  }

  public void setInvoiceDate(LocalDate invoiceDate) {
    this.invoiceDate = invoiceDate;
  }


  public InvoiceSimpleVO invoiceDueDate(LocalDate invoiceDueDate) {
    this.invoiceDueDate = invoiceDueDate;
    return this;
  }

  /**
   * 
   * @return invoiceDueDate
   */
  @javax.annotation.Nullable
  public LocalDate getInvoiceDueDate() {
    return invoiceDueDate;
  }

  public void setInvoiceDueDate(LocalDate invoiceDueDate) {
    this.invoiceDueDate = invoiceDueDate;
  }


  public InvoiceSimpleVO invoiceId(Long invoiceId) {
    this.invoiceId = invoiceId;
    return this;
  }

  /**
   * 
   * @return invoiceId
   */
  @javax.annotation.Nullable
  public Long getInvoiceId() {
    return invoiceId;
  }

  public void setInvoiceId(Long invoiceId) {
    this.invoiceId = invoiceId;
  }


  public InvoiceSimpleVO invoiceNumber(String invoiceNumber) {
    this.invoiceNumber = invoiceNumber;
    return this;
  }

  /**
   * 
   * @return invoiceNumber
   */
  @javax.annotation.Nullable
  public String getInvoiceNumber() {
    return invoiceNumber;
  }

  public void setInvoiceNumber(String invoiceNumber) {
    this.invoiceNumber = invoiceNumber;
  }


  public InvoiceSimpleVO invoiceTo(String invoiceTo) {
    this.invoiceTo = invoiceTo;
    return this;
  }

  /**
   * 
   * @return invoiceTo
   */
  @javax.annotation.Nullable
  public String getInvoiceTo() {
    return invoiceTo;
  }

  public void setInvoiceTo(String invoiceTo) {
    this.invoiceTo = invoiceTo;
  }


  public InvoiceSimpleVO isFinal(Integer isFinal) {
    this.isFinal = isFinal;
    return this;
  }

  /**
   * 
   * @return isFinal
   */
  @javax.annotation.Nullable
  public Integer getIsFinal() {
    return isFinal;
  }

  public void setIsFinal(Integer isFinal) {
    this.isFinal = isFinal;
  }


  public InvoiceSimpleVO isNonBillable(Integer isNonBillable) {
    this.isNonBillable = isNonBillable;
    return this;
  }

  /**
   * 
   * @return isNonBillable
   */
  @javax.annotation.Nullable
  public Integer getIsNonBillable() {
    return isNonBillable;
  }

  public void setIsNonBillable(Integer isNonBillable) {
    this.isNonBillable = isNonBillable;
  }


  public InvoiceSimpleVO items(List<InvoiceItemSimpleVO> items) {
    this.items = items;
    return this;
  }

  public InvoiceSimpleVO addItemsItem(InvoiceItemSimpleVO itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * 
   * @return items
   */
  @javax.annotation.Nullable
  public List<InvoiceItemSimpleVO> getItems() {
    return items;
  }

  public void setItems(List<InvoiceItemSimpleVO> items) {
    this.items = items;
  }


  public InvoiceSimpleVO orderReference(String orderReference) {
    this.orderReference = orderReference;
    return this;
  }

  /**
   * 
   * @return orderReference
   */
  @javax.annotation.Nullable
  public String getOrderReference() {
    return orderReference;
  }

  public void setOrderReference(String orderReference) {
    this.orderReference = orderReference;
  }


  public InvoiceSimpleVO orderTitle(String orderTitle) {
    this.orderTitle = orderTitle;
    return this;
  }

  /**
   * 
   * @return orderTitle
   */
  @javax.annotation.Nullable
  public String getOrderTitle() {
    return orderTitle;
  }

  public void setOrderTitle(String orderTitle) {
    this.orderTitle = orderTitle;
  }


  public InvoiceSimpleVO paymentMethod(String paymentMethod) {
    this.paymentMethod = paymentMethod;
    return this;
  }

  /**
   * 
   * @return paymentMethod
   */
  @javax.annotation.Nullable
  public String getPaymentMethod() {
    return paymentMethod;
  }

  public void setPaymentMethod(String paymentMethod) {
    this.paymentMethod = paymentMethod;
  }


  public InvoiceSimpleVO preparedBy(String preparedBy) {
    this.preparedBy = preparedBy;
    return this;
  }

  /**
   * 
   * @return preparedBy
   */
  @javax.annotation.Nullable
  public String getPreparedBy() {
    return preparedBy;
  }

  public void setPreparedBy(String preparedBy) {
    this.preparedBy = preparedBy;
  }


  public InvoiceSimpleVO projectNumber(Long projectNumber) {
    this.projectNumber = projectNumber;
    return this;
  }

  /**
   * 
   * @return projectNumber
   */
  @javax.annotation.Nullable
  public Long getProjectNumber() {
    return projectNumber;
  }

  public void setProjectNumber(Long projectNumber) {
    this.projectNumber = projectNumber;
  }


  public InvoiceSimpleVO referenceNumber(String referenceNumber) {
    this.referenceNumber = referenceNumber;
    return this;
  }

  /**
   * 
   * @return referenceNumber
   */
  @javax.annotation.Nullable
  public String getReferenceNumber() {
    return referenceNumber;
  }

  public void setReferenceNumber(String referenceNumber) {
    this.referenceNumber = referenceNumber;
  }


  public InvoiceSimpleVO shipping(Object shipping) {
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


  public InvoiceSimpleVO status(String status) {
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


  public InvoiceSimpleVO subTotal(Object subTotal) {
    this.subTotal = subTotal;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return subTotal
   */
  @javax.annotation.Nullable
  public Object getSubTotal() {
    return subTotal;
  }

  public void setSubTotal(Object subTotal) {
    this.subTotal = subTotal;
  }


  public InvoiceSimpleVO tax(Object tax) {
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


  public InvoiceSimpleVO transactionalCurrency(String transactionalCurrency) {
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


  public InvoiceSimpleVO transactionalGrandTotal(Object transactionalGrandTotal) {
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


  public InvoiceSimpleVO transactionalShipping(Object transactionalShipping) {
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


  public InvoiceSimpleVO transactionalSubTotal(Object transactionalSubTotal) {
    this.transactionalSubTotal = transactionalSubTotal;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return transactionalSubTotal
   */
  @javax.annotation.Nullable
  public Object getTransactionalSubTotal() {
    return transactionalSubTotal;
  }

  public void setTransactionalSubTotal(Object transactionalSubTotal) {
    this.transactionalSubTotal = transactionalSubTotal;
  }


  public InvoiceSimpleVO transactionalTax(Object transactionalTax) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InvoiceSimpleVO invoiceSimpleVO = (InvoiceSimpleVO) o;
    return Objects.equals(this.comments, invoiceSimpleVO.comments) &&
        Objects.equals(this.currency, invoiceSimpleVO.currency) &&
        Objects.equals(this.customFields, invoiceSimpleVO.customFields) &&
        Objects.equals(this.grandTotal, invoiceSimpleVO.grandTotal) &&
        Objects.equals(this.invoiceDate, invoiceSimpleVO.invoiceDate) &&
        Objects.equals(this.invoiceDueDate, invoiceSimpleVO.invoiceDueDate) &&
        Objects.equals(this.invoiceId, invoiceSimpleVO.invoiceId) &&
        Objects.equals(this.invoiceNumber, invoiceSimpleVO.invoiceNumber) &&
        Objects.equals(this.invoiceTo, invoiceSimpleVO.invoiceTo) &&
        Objects.equals(this.isFinal, invoiceSimpleVO.isFinal) &&
        Objects.equals(this.isNonBillable, invoiceSimpleVO.isNonBillable) &&
        Objects.equals(this.items, invoiceSimpleVO.items) &&
        Objects.equals(this.orderReference, invoiceSimpleVO.orderReference) &&
        Objects.equals(this.orderTitle, invoiceSimpleVO.orderTitle) &&
        Objects.equals(this.paymentMethod, invoiceSimpleVO.paymentMethod) &&
        Objects.equals(this.preparedBy, invoiceSimpleVO.preparedBy) &&
        Objects.equals(this.projectNumber, invoiceSimpleVO.projectNumber) &&
        Objects.equals(this.referenceNumber, invoiceSimpleVO.referenceNumber) &&
        Objects.equals(this.shipping, invoiceSimpleVO.shipping) &&
        Objects.equals(this.status, invoiceSimpleVO.status) &&
        Objects.equals(this.subTotal, invoiceSimpleVO.subTotal) &&
        Objects.equals(this.tax, invoiceSimpleVO.tax) &&
        Objects.equals(this.transactionalCurrency, invoiceSimpleVO.transactionalCurrency) &&
        Objects.equals(this.transactionalGrandTotal, invoiceSimpleVO.transactionalGrandTotal) &&
        Objects.equals(this.transactionalShipping, invoiceSimpleVO.transactionalShipping) &&
        Objects.equals(this.transactionalSubTotal, invoiceSimpleVO.transactionalSubTotal) &&
        Objects.equals(this.transactionalTax, invoiceSimpleVO.transactionalTax);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(comments, currency, customFields, grandTotal, invoiceDate, invoiceDueDate, invoiceId, invoiceNumber, invoiceTo, isFinal, isNonBillable, items, orderReference, orderTitle, paymentMethod, preparedBy, projectNumber, referenceNumber, shipping, status, subTotal, tax, transactionalCurrency, transactionalGrandTotal, transactionalShipping, transactionalSubTotal, transactionalTax);
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
    sb.append("class InvoiceSimpleVO {\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    grandTotal: ").append(toIndentedString(grandTotal)).append("\n");
    sb.append("    invoiceDate: ").append(toIndentedString(invoiceDate)).append("\n");
    sb.append("    invoiceDueDate: ").append(toIndentedString(invoiceDueDate)).append("\n");
    sb.append("    invoiceId: ").append(toIndentedString(invoiceId)).append("\n");
    sb.append("    invoiceNumber: ").append(toIndentedString(invoiceNumber)).append("\n");
    sb.append("    invoiceTo: ").append(toIndentedString(invoiceTo)).append("\n");
    sb.append("    isFinal: ").append(toIndentedString(isFinal)).append("\n");
    sb.append("    isNonBillable: ").append(toIndentedString(isNonBillable)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    orderReference: ").append(toIndentedString(orderReference)).append("\n");
    sb.append("    orderTitle: ").append(toIndentedString(orderTitle)).append("\n");
    sb.append("    paymentMethod: ").append(toIndentedString(paymentMethod)).append("\n");
    sb.append("    preparedBy: ").append(toIndentedString(preparedBy)).append("\n");
    sb.append("    projectNumber: ").append(toIndentedString(projectNumber)).append("\n");
    sb.append("    referenceNumber: ").append(toIndentedString(referenceNumber)).append("\n");
    sb.append("    shipping: ").append(toIndentedString(shipping)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subTotal: ").append(toIndentedString(subTotal)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    transactionalCurrency: ").append(toIndentedString(transactionalCurrency)).append("\n");
    sb.append("    transactionalGrandTotal: ").append(toIndentedString(transactionalGrandTotal)).append("\n");
    sb.append("    transactionalShipping: ").append(toIndentedString(transactionalShipping)).append("\n");
    sb.append("    transactionalSubTotal: ").append(toIndentedString(transactionalSubTotal)).append("\n");
    sb.append("    transactionalTax: ").append(toIndentedString(transactionalTax)).append("\n");
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
    openapiFields.add("comments");
    openapiFields.add("currency");
    openapiFields.add("custom_fields");
    openapiFields.add("grand_total");
    openapiFields.add("invoice_date");
    openapiFields.add("invoice_due_date");
    openapiFields.add("invoice_id");
    openapiFields.add("invoice_number");
    openapiFields.add("invoice_to");
    openapiFields.add("is_final");
    openapiFields.add("is_nonBillable");
    openapiFields.add("items");
    openapiFields.add("order_reference");
    openapiFields.add("order_title");
    openapiFields.add("payment_method");
    openapiFields.add("prepared_by");
    openapiFields.add("project_number");
    openapiFields.add("reference_number");
    openapiFields.add("shipping");
    openapiFields.add("status");
    openapiFields.add("sub_total");
    openapiFields.add("tax");
    openapiFields.add("transactional_currency");
    openapiFields.add("transactional_grand_total");
    openapiFields.add("transactional_shipping");
    openapiFields.add("transactional_sub_total");
    openapiFields.add("transactional_tax");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InvoiceSimpleVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InvoiceSimpleVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InvoiceSimpleVO is not found in the empty JSON string", InvoiceSimpleVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InvoiceSimpleVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InvoiceSimpleVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
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
      if ((jsonObj.get("invoice_number") != null && !jsonObj.get("invoice_number").isJsonNull()) && !jsonObj.get("invoice_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoice_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("invoice_number").toString()));
      }
      if ((jsonObj.get("invoice_to") != null && !jsonObj.get("invoice_to").isJsonNull()) && !jsonObj.get("invoice_to").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoice_to` to be a primitive type in the JSON string but got `%s`", jsonObj.get("invoice_to").toString()));
      }
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            InvoiceItemSimpleVO.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if ((jsonObj.get("order_reference") != null && !jsonObj.get("order_reference").isJsonNull()) && !jsonObj.get("order_reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_reference").toString()));
      }
      if ((jsonObj.get("order_title") != null && !jsonObj.get("order_title").isJsonNull()) && !jsonObj.get("order_title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_title").toString()));
      }
      if ((jsonObj.get("payment_method") != null && !jsonObj.get("payment_method").isJsonNull()) && !jsonObj.get("payment_method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_method").toString()));
      }
      if ((jsonObj.get("prepared_by") != null && !jsonObj.get("prepared_by").isJsonNull()) && !jsonObj.get("prepared_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `prepared_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("prepared_by").toString()));
      }
      if ((jsonObj.get("reference_number") != null && !jsonObj.get("reference_number").isJsonNull()) && !jsonObj.get("reference_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference_number").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("transactional_currency") != null && !jsonObj.get("transactional_currency").isJsonNull()) && !jsonObj.get("transactional_currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactional_currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactional_currency").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InvoiceSimpleVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InvoiceSimpleVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InvoiceSimpleVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InvoiceSimpleVO.class));

       return (TypeAdapter<T>) new TypeAdapter<InvoiceSimpleVO>() {
           @Override
           public void write(JsonWriter out, InvoiceSimpleVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InvoiceSimpleVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InvoiceSimpleVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InvoiceSimpleVO
   * @throws IOException if the JSON string is invalid with respect to InvoiceSimpleVO
   */
  public static InvoiceSimpleVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InvoiceSimpleVO.class);
  }

  /**
   * Convert an instance of InvoiceSimpleVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

