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
import org.openapitools.client.model.WorkgroupBaseVO;
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
 * Java type: com.noosh.nooshapi.vo.OrderSimpleBaseVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderSimpleBaseVO {
  public static final String SERIALIZED_NAME_BUYER_WORKGROUP = "buyer_workgroup";
  @SerializedName(SERIALIZED_NAME_BUYER_WORKGROUP)
  private WorkgroupBaseVO buyerWorkgroup;

  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_COMPLETION_DATE = "completion_date";
  @SerializedName(SERIALIZED_NAME_COMPLETION_DATE)
  private LocalDate completionDate;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_GRAND_TOTAL = "grand_total";
  @SerializedName(SERIALIZED_NAME_GRAND_TOTAL)
  private Object grandTotal = null;

  public static final String SERIALIZED_NAME_LAST_CHANGED = "last_changed";
  @SerializedName(SERIALIZED_NAME_LAST_CHANGED)
  private LocalDate lastChanged;

  public static final String SERIALIZED_NAME_LAST_STATUS_CHANGE = "last_status_change";
  @SerializedName(SERIALIZED_NAME_LAST_STATUS_CHANGE)
  private LocalDate lastStatusChange;

  public static final String SERIALIZED_NAME_ORDER_ID = "order_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private Long orderId;

  public static final String SERIALIZED_NAME_ORDER_NUMBER = "order_number";
  @SerializedName(SERIALIZED_NAME_ORDER_NUMBER)
  private String orderNumber;

  public static final String SERIALIZED_NAME_ORDER_TITLE = "order_title";
  @SerializedName(SERIALIZED_NAME_ORDER_TITLE)
  private String orderTitle;

  public static final String SERIALIZED_NAME_PAYMENT_REFERENCE = "payment_reference";
  @SerializedName(SERIALIZED_NAME_PAYMENT_REFERENCE)
  private String paymentReference;

  public static final String SERIALIZED_NAME_PRINT_ORDER_IDS = "print_order_ids";
  @SerializedName(SERIALIZED_NAME_PRINT_ORDER_IDS)
  private List<Long> printOrderIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_STATUS_COMMENTS = "status_comments";
  @SerializedName(SERIALIZED_NAME_STATUS_COMMENTS)
  private String statusComments;

  public static final String SERIALIZED_NAME_SUPPLIER_REFERENCE = "supplier_reference";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_REFERENCE)
  private String supplierReference;

  public static final String SERIALIZED_NAME_SUPPLIER_WORKGROUP = "supplier_workgroup";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_WORKGROUP)
  private WorkgroupBaseVO supplierWorkgroup;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_CURRENCY = "transactional_currency";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_CURRENCY)
  private String transactionalCurrency;

  public static final String SERIALIZED_NAME_TRANSACTIONAL_GRAND_TOTAL = "transactional_grand_total";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONAL_GRAND_TOTAL)
  private Object transactionalGrandTotal = null;

  public OrderSimpleBaseVO() {
  }

  public OrderSimpleBaseVO buyerWorkgroup(WorkgroupBaseVO buyerWorkgroup) {
    this.buyerWorkgroup = buyerWorkgroup;
    return this;
  }

  /**
   * Get buyerWorkgroup
   * @return buyerWorkgroup
   */
  @javax.annotation.Nullable
  public WorkgroupBaseVO getBuyerWorkgroup() {
    return buyerWorkgroup;
  }

  public void setBuyerWorkgroup(WorkgroupBaseVO buyerWorkgroup) {
    this.buyerWorkgroup = buyerWorkgroup;
  }


  public OrderSimpleBaseVO comments(String comments) {
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


  public OrderSimpleBaseVO completionDate(LocalDate completionDate) {
    this.completionDate = completionDate;
    return this;
  }

  /**
   * 
   * @return completionDate
   */
  @javax.annotation.Nullable
  public LocalDate getCompletionDate() {
    return completionDate;
  }

  public void setCompletionDate(LocalDate completionDate) {
    this.completionDate = completionDate;
  }


  public OrderSimpleBaseVO currency(String currency) {
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


  public OrderSimpleBaseVO grandTotal(Object grandTotal) {
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


  public OrderSimpleBaseVO lastChanged(LocalDate lastChanged) {
    this.lastChanged = lastChanged;
    return this;
  }

  /**
   * 
   * @return lastChanged
   */
  @javax.annotation.Nullable
  public LocalDate getLastChanged() {
    return lastChanged;
  }

  public void setLastChanged(LocalDate lastChanged) {
    this.lastChanged = lastChanged;
  }


  public OrderSimpleBaseVO lastStatusChange(LocalDate lastStatusChange) {
    this.lastStatusChange = lastStatusChange;
    return this;
  }

  /**
   * 
   * @return lastStatusChange
   */
  @javax.annotation.Nullable
  public LocalDate getLastStatusChange() {
    return lastStatusChange;
  }

  public void setLastStatusChange(LocalDate lastStatusChange) {
    this.lastStatusChange = lastStatusChange;
  }


  public OrderSimpleBaseVO orderId(Long orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * 
   * @return orderId
   */
  @javax.annotation.Nullable
  public Long getOrderId() {
    return orderId;
  }

  public void setOrderId(Long orderId) {
    this.orderId = orderId;
  }


  public OrderSimpleBaseVO orderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
    return this;
  }

  /**
   * 
   * @return orderNumber
   */
  @javax.annotation.Nullable
  public String getOrderNumber() {
    return orderNumber;
  }

  public void setOrderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
  }


  public OrderSimpleBaseVO orderTitle(String orderTitle) {
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


  public OrderSimpleBaseVO paymentReference(String paymentReference) {
    this.paymentReference = paymentReference;
    return this;
  }

  /**
   * 
   * @return paymentReference
   */
  @javax.annotation.Nullable
  public String getPaymentReference() {
    return paymentReference;
  }

  public void setPaymentReference(String paymentReference) {
    this.paymentReference = paymentReference;
  }


  public OrderSimpleBaseVO printOrderIds(List<Long> printOrderIds) {
    this.printOrderIds = printOrderIds;
    return this;
  }

  public OrderSimpleBaseVO addPrintOrderIdsItem(Long printOrderIdsItem) {
    if (this.printOrderIds == null) {
      this.printOrderIds = new ArrayList<>();
    }
    this.printOrderIds.add(printOrderIdsItem);
    return this;
  }

  /**
   * 
   * @return printOrderIds
   */
  @javax.annotation.Nullable
  public List<Long> getPrintOrderIds() {
    return printOrderIds;
  }

  public void setPrintOrderIds(List<Long> printOrderIds) {
    this.printOrderIds = printOrderIds;
  }


  public OrderSimpleBaseVO status(String status) {
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


  public OrderSimpleBaseVO statusComments(String statusComments) {
    this.statusComments = statusComments;
    return this;
  }

  /**
   * 
   * @return statusComments
   */
  @javax.annotation.Nullable
  public String getStatusComments() {
    return statusComments;
  }

  public void setStatusComments(String statusComments) {
    this.statusComments = statusComments;
  }


  public OrderSimpleBaseVO supplierReference(String supplierReference) {
    this.supplierReference = supplierReference;
    return this;
  }

  /**
   * 
   * @return supplierReference
   */
  @javax.annotation.Nullable
  public String getSupplierReference() {
    return supplierReference;
  }

  public void setSupplierReference(String supplierReference) {
    this.supplierReference = supplierReference;
  }


  public OrderSimpleBaseVO supplierWorkgroup(WorkgroupBaseVO supplierWorkgroup) {
    this.supplierWorkgroup = supplierWorkgroup;
    return this;
  }

  /**
   * Get supplierWorkgroup
   * @return supplierWorkgroup
   */
  @javax.annotation.Nullable
  public WorkgroupBaseVO getSupplierWorkgroup() {
    return supplierWorkgroup;
  }

  public void setSupplierWorkgroup(WorkgroupBaseVO supplierWorkgroup) {
    this.supplierWorkgroup = supplierWorkgroup;
  }


  public OrderSimpleBaseVO transactionalCurrency(String transactionalCurrency) {
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


  public OrderSimpleBaseVO transactionalGrandTotal(Object transactionalGrandTotal) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderSimpleBaseVO orderSimpleBaseVO = (OrderSimpleBaseVO) o;
    return Objects.equals(this.buyerWorkgroup, orderSimpleBaseVO.buyerWorkgroup) &&
        Objects.equals(this.comments, orderSimpleBaseVO.comments) &&
        Objects.equals(this.completionDate, orderSimpleBaseVO.completionDate) &&
        Objects.equals(this.currency, orderSimpleBaseVO.currency) &&
        Objects.equals(this.grandTotal, orderSimpleBaseVO.grandTotal) &&
        Objects.equals(this.lastChanged, orderSimpleBaseVO.lastChanged) &&
        Objects.equals(this.lastStatusChange, orderSimpleBaseVO.lastStatusChange) &&
        Objects.equals(this.orderId, orderSimpleBaseVO.orderId) &&
        Objects.equals(this.orderNumber, orderSimpleBaseVO.orderNumber) &&
        Objects.equals(this.orderTitle, orderSimpleBaseVO.orderTitle) &&
        Objects.equals(this.paymentReference, orderSimpleBaseVO.paymentReference) &&
        Objects.equals(this.printOrderIds, orderSimpleBaseVO.printOrderIds) &&
        Objects.equals(this.status, orderSimpleBaseVO.status) &&
        Objects.equals(this.statusComments, orderSimpleBaseVO.statusComments) &&
        Objects.equals(this.supplierReference, orderSimpleBaseVO.supplierReference) &&
        Objects.equals(this.supplierWorkgroup, orderSimpleBaseVO.supplierWorkgroup) &&
        Objects.equals(this.transactionalCurrency, orderSimpleBaseVO.transactionalCurrency) &&
        Objects.equals(this.transactionalGrandTotal, orderSimpleBaseVO.transactionalGrandTotal);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(buyerWorkgroup, comments, completionDate, currency, grandTotal, lastChanged, lastStatusChange, orderId, orderNumber, orderTitle, paymentReference, printOrderIds, status, statusComments, supplierReference, supplierWorkgroup, transactionalCurrency, transactionalGrandTotal);
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
    sb.append("class OrderSimpleBaseVO {\n");
    sb.append("    buyerWorkgroup: ").append(toIndentedString(buyerWorkgroup)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    completionDate: ").append(toIndentedString(completionDate)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    grandTotal: ").append(toIndentedString(grandTotal)).append("\n");
    sb.append("    lastChanged: ").append(toIndentedString(lastChanged)).append("\n");
    sb.append("    lastStatusChange: ").append(toIndentedString(lastStatusChange)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    orderNumber: ").append(toIndentedString(orderNumber)).append("\n");
    sb.append("    orderTitle: ").append(toIndentedString(orderTitle)).append("\n");
    sb.append("    paymentReference: ").append(toIndentedString(paymentReference)).append("\n");
    sb.append("    printOrderIds: ").append(toIndentedString(printOrderIds)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statusComments: ").append(toIndentedString(statusComments)).append("\n");
    sb.append("    supplierReference: ").append(toIndentedString(supplierReference)).append("\n");
    sb.append("    supplierWorkgroup: ").append(toIndentedString(supplierWorkgroup)).append("\n");
    sb.append("    transactionalCurrency: ").append(toIndentedString(transactionalCurrency)).append("\n");
    sb.append("    transactionalGrandTotal: ").append(toIndentedString(transactionalGrandTotal)).append("\n");
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
    openapiFields.add("buyer_workgroup");
    openapiFields.add("comments");
    openapiFields.add("completion_date");
    openapiFields.add("currency");
    openapiFields.add("grand_total");
    openapiFields.add("last_changed");
    openapiFields.add("last_status_change");
    openapiFields.add("order_id");
    openapiFields.add("order_number");
    openapiFields.add("order_title");
    openapiFields.add("payment_reference");
    openapiFields.add("print_order_ids");
    openapiFields.add("status");
    openapiFields.add("status_comments");
    openapiFields.add("supplier_reference");
    openapiFields.add("supplier_workgroup");
    openapiFields.add("transactional_currency");
    openapiFields.add("transactional_grand_total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderSimpleBaseVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderSimpleBaseVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderSimpleBaseVO is not found in the empty JSON string", OrderSimpleBaseVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderSimpleBaseVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderSimpleBaseVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `buyer_workgroup`
      if (jsonObj.get("buyer_workgroup") != null && !jsonObj.get("buyer_workgroup").isJsonNull()) {
        WorkgroupBaseVO.validateJsonElement(jsonObj.get("buyer_workgroup"));
      }
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if ((jsonObj.get("order_number") != null && !jsonObj.get("order_number").isJsonNull()) && !jsonObj.get("order_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_number").toString()));
      }
      if ((jsonObj.get("order_title") != null && !jsonObj.get("order_title").isJsonNull()) && !jsonObj.get("order_title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_title").toString()));
      }
      if ((jsonObj.get("payment_reference") != null && !jsonObj.get("payment_reference").isJsonNull()) && !jsonObj.get("payment_reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_reference").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("print_order_ids") != null && !jsonObj.get("print_order_ids").isJsonNull() && !jsonObj.get("print_order_ids").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `print_order_ids` to be an array in the JSON string but got `%s`", jsonObj.get("print_order_ids").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("status_comments") != null && !jsonObj.get("status_comments").isJsonNull()) && !jsonObj.get("status_comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status_comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status_comments").toString()));
      }
      if ((jsonObj.get("supplier_reference") != null && !jsonObj.get("supplier_reference").isJsonNull()) && !jsonObj.get("supplier_reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supplier_reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supplier_reference").toString()));
      }
      // validate the optional field `supplier_workgroup`
      if (jsonObj.get("supplier_workgroup") != null && !jsonObj.get("supplier_workgroup").isJsonNull()) {
        WorkgroupBaseVO.validateJsonElement(jsonObj.get("supplier_workgroup"));
      }
      if ((jsonObj.get("transactional_currency") != null && !jsonObj.get("transactional_currency").isJsonNull()) && !jsonObj.get("transactional_currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactional_currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactional_currency").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrderSimpleBaseVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderSimpleBaseVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderSimpleBaseVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderSimpleBaseVO.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderSimpleBaseVO>() {
           @Override
           public void write(JsonWriter out, OrderSimpleBaseVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderSimpleBaseVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderSimpleBaseVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderSimpleBaseVO
   * @throws IOException if the JSON string is invalid with respect to OrderSimpleBaseVO
   */
  public static OrderSimpleBaseVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderSimpleBaseVO.class);
  }

  /**
   * Convert an instance of OrderSimpleBaseVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

