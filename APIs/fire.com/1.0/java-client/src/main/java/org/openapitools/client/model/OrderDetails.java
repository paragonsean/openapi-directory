/*
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
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
 * OrderDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:07.131817-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderDetails {
  public static final String SERIALIZED_NAME_COMMENT1 = "comment1";
  @SerializedName(SERIALIZED_NAME_COMMENT1)
  private String comment1;

  public static final String SERIALIZED_NAME_COMMENT2 = "comment2";
  @SerializedName(SERIALIZED_NAME_COMMENT2)
  private String comment2;

  public static final String SERIALIZED_NAME_CUSTOMER_NUMBER = "customerNumber";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_NUMBER)
  private String customerNumber;

  public static final String SERIALIZED_NAME_DELIVERY_ADDRESS_LINE1 = "deliveryAddressLine1";
  @SerializedName(SERIALIZED_NAME_DELIVERY_ADDRESS_LINE1)
  private String deliveryAddressLine1;

  public static final String SERIALIZED_NAME_DELIVERY_ADDRESS_LINE2 = "deliveryAddressLine2";
  @SerializedName(SERIALIZED_NAME_DELIVERY_ADDRESS_LINE2)
  private String deliveryAddressLine2;

  public static final String SERIALIZED_NAME_DELIVERY_CITY = "deliveryCity";
  @SerializedName(SERIALIZED_NAME_DELIVERY_CITY)
  private String deliveryCity;

  public static final String SERIALIZED_NAME_DELIVERY_COUNTRY = "deliveryCountry";
  @SerializedName(SERIALIZED_NAME_DELIVERY_COUNTRY)
  private String deliveryCountry;

  public static final String SERIALIZED_NAME_DELIVERY_POST_CODE = "deliveryPostCode";
  @SerializedName(SERIALIZED_NAME_DELIVERY_POST_CODE)
  private String deliveryPostCode;

  public static final String SERIALIZED_NAME_MERCHANT_CUSTOMER_IDENTIFICATION = "merchantCustomerIdentification";
  @SerializedName(SERIALIZED_NAME_MERCHANT_CUSTOMER_IDENTIFICATION)
  private String merchantCustomerIdentification;

  public static final String SERIALIZED_NAME_MERCHANT_NUMBER = "merchantNumber";
  @SerializedName(SERIALIZED_NAME_MERCHANT_NUMBER)
  private String merchantNumber;

  public static final String SERIALIZED_NAME_ORDER_ID = "orderId";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "productId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private String productId;

  public static final String SERIALIZED_NAME_VARIABLE_REFERENCE = "variableReference";
  @SerializedName(SERIALIZED_NAME_VARIABLE_REFERENCE)
  private String variableReference;

  public OrderDetails() {
  }

  public OrderDetails comment1(String comment1) {
    this.comment1 = comment1;
    return this;
  }

  /**
   * This is your own comment for the transaction.
   * @return comment1
   */
  @javax.annotation.Nullable
  public String getComment1() {
    return comment1;
  }

  public void setComment1(String comment1) {
    this.comment1 = comment1;
  }


  public OrderDetails comment2(String comment2) {
    this.comment2 = comment2;
    return this;
  }

  /**
   * This is your own comment for the transaction.
   * @return comment2
   */
  @javax.annotation.Nullable
  public String getComment2() {
    return comment2;
  }

  public void setComment2(String comment2) {
    this.comment2 = comment2;
  }


  public OrderDetails customerNumber(String customerNumber) {
    this.customerNumber = customerNumber;
    return this;
  }

  /**
   * Use this field to store a customer number for the transaction (for example).
   * @return customerNumber
   */
  @javax.annotation.Nullable
  public String getCustomerNumber() {
    return customerNumber;
  }

  public void setCustomerNumber(String customerNumber) {
    this.customerNumber = customerNumber;
  }


  public OrderDetails deliveryAddressLine1(String deliveryAddressLine1) {
    this.deliveryAddressLine1 = deliveryAddressLine1;
    return this;
  }

  /**
   * The first line of the delivery address.
   * @return deliveryAddressLine1
   */
  @javax.annotation.Nullable
  public String getDeliveryAddressLine1() {
    return deliveryAddressLine1;
  }

  public void setDeliveryAddressLine1(String deliveryAddressLine1) {
    this.deliveryAddressLine1 = deliveryAddressLine1;
  }


  public OrderDetails deliveryAddressLine2(String deliveryAddressLine2) {
    this.deliveryAddressLine2 = deliveryAddressLine2;
    return this;
  }

  /**
   * The second line of the delivery address.
   * @return deliveryAddressLine2
   */
  @javax.annotation.Nullable
  public String getDeliveryAddressLine2() {
    return deliveryAddressLine2;
  }

  public void setDeliveryAddressLine2(String deliveryAddressLine2) {
    this.deliveryAddressLine2 = deliveryAddressLine2;
  }


  public OrderDetails deliveryCity(String deliveryCity) {
    this.deliveryCity = deliveryCity;
    return this;
  }

  /**
   * Delivery address city
   * @return deliveryCity
   */
  @javax.annotation.Nullable
  public String getDeliveryCity() {
    return deliveryCity;
  }

  public void setDeliveryCity(String deliveryCity) {
    this.deliveryCity = deliveryCity;
  }


  public OrderDetails deliveryCountry(String deliveryCountry) {
    this.deliveryCountry = deliveryCountry;
    return this;
  }

  /**
   * 2-digit code for the country
   * @return deliveryCountry
   */
  @javax.annotation.Nullable
  public String getDeliveryCountry() {
    return deliveryCountry;
  }

  public void setDeliveryCountry(String deliveryCountry) {
    this.deliveryCountry = deliveryCountry;
  }


  public OrderDetails deliveryPostCode(String deliveryPostCode) {
    this.deliveryPostCode = deliveryPostCode;
    return this;
  }

  /**
   * Delivery address post code
   * @return deliveryPostCode
   */
  @javax.annotation.Nullable
  public String getDeliveryPostCode() {
    return deliveryPostCode;
  }

  public void setDeliveryPostCode(String deliveryPostCode) {
    this.deliveryPostCode = deliveryPostCode;
  }


  public OrderDetails merchantCustomerIdentification(String merchantCustomerIdentification) {
    this.merchantCustomerIdentification = merchantCustomerIdentification;
    return this;
  }

  /**
   * This is a reference you use to uniquely identify each of your customers.
   * @return merchantCustomerIdentification
   */
  @javax.annotation.Nullable
  public String getMerchantCustomerIdentification() {
    return merchantCustomerIdentification;
  }

  public void setMerchantCustomerIdentification(String merchantCustomerIdentification) {
    this.merchantCustomerIdentification = merchantCustomerIdentification;
  }


  public OrderDetails merchantNumber(String merchantNumber) {
    this.merchantNumber = merchantNumber;
    return this;
  }

  /**
   * Your Merchant Number (if applicable).
   * @return merchantNumber
   */
  @javax.annotation.Nullable
  public String getMerchantNumber() {
    return merchantNumber;
  }

  public void setMerchantNumber(String merchantNumber) {
    this.merchantNumber = merchantNumber;
  }


  public OrderDetails orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * Use this field to store the order id for the transaction. The Order Id cannot be set unless the &#x60;maxNumberPayments&#x60; is 1.
   * @return orderId
   */
  @javax.annotation.Nullable
  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  public OrderDetails productId(String productId) {
    this.productId = productId;
    return this;
  }

  /**
   * Use this field to store a product id for the transaction (for example).
   * @return productId
   */
  @javax.annotation.Nullable
  public String getProductId() {
    return productId;
  }

  public void setProductId(String productId) {
    this.productId = productId;
  }


  public OrderDetails variableReference(String variableReference) {
    this.variableReference = variableReference;
    return this;
  }

  /**
   * Use this field to store any other reference for the transaction (for example, a phone number).
   * @return variableReference
   */
  @javax.annotation.Nullable
  public String getVariableReference() {
    return variableReference;
  }

  public void setVariableReference(String variableReference) {
    this.variableReference = variableReference;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderDetails orderDetails = (OrderDetails) o;
    return Objects.equals(this.comment1, orderDetails.comment1) &&
        Objects.equals(this.comment2, orderDetails.comment2) &&
        Objects.equals(this.customerNumber, orderDetails.customerNumber) &&
        Objects.equals(this.deliveryAddressLine1, orderDetails.deliveryAddressLine1) &&
        Objects.equals(this.deliveryAddressLine2, orderDetails.deliveryAddressLine2) &&
        Objects.equals(this.deliveryCity, orderDetails.deliveryCity) &&
        Objects.equals(this.deliveryCountry, orderDetails.deliveryCountry) &&
        Objects.equals(this.deliveryPostCode, orderDetails.deliveryPostCode) &&
        Objects.equals(this.merchantCustomerIdentification, orderDetails.merchantCustomerIdentification) &&
        Objects.equals(this.merchantNumber, orderDetails.merchantNumber) &&
        Objects.equals(this.orderId, orderDetails.orderId) &&
        Objects.equals(this.productId, orderDetails.productId) &&
        Objects.equals(this.variableReference, orderDetails.variableReference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(comment1, comment2, customerNumber, deliveryAddressLine1, deliveryAddressLine2, deliveryCity, deliveryCountry, deliveryPostCode, merchantCustomerIdentification, merchantNumber, orderId, productId, variableReference);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderDetails {\n");
    sb.append("    comment1: ").append(toIndentedString(comment1)).append("\n");
    sb.append("    comment2: ").append(toIndentedString(comment2)).append("\n");
    sb.append("    customerNumber: ").append(toIndentedString(customerNumber)).append("\n");
    sb.append("    deliveryAddressLine1: ").append(toIndentedString(deliveryAddressLine1)).append("\n");
    sb.append("    deliveryAddressLine2: ").append(toIndentedString(deliveryAddressLine2)).append("\n");
    sb.append("    deliveryCity: ").append(toIndentedString(deliveryCity)).append("\n");
    sb.append("    deliveryCountry: ").append(toIndentedString(deliveryCountry)).append("\n");
    sb.append("    deliveryPostCode: ").append(toIndentedString(deliveryPostCode)).append("\n");
    sb.append("    merchantCustomerIdentification: ").append(toIndentedString(merchantCustomerIdentification)).append("\n");
    sb.append("    merchantNumber: ").append(toIndentedString(merchantNumber)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    variableReference: ").append(toIndentedString(variableReference)).append("\n");
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
    openapiFields.add("comment1");
    openapiFields.add("comment2");
    openapiFields.add("customerNumber");
    openapiFields.add("deliveryAddressLine1");
    openapiFields.add("deliveryAddressLine2");
    openapiFields.add("deliveryCity");
    openapiFields.add("deliveryCountry");
    openapiFields.add("deliveryPostCode");
    openapiFields.add("merchantCustomerIdentification");
    openapiFields.add("merchantNumber");
    openapiFields.add("orderId");
    openapiFields.add("productId");
    openapiFields.add("variableReference");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderDetails is not found in the empty JSON string", OrderDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comment1") != null && !jsonObj.get("comment1").isJsonNull()) && !jsonObj.get("comment1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment1").toString()));
      }
      if ((jsonObj.get("comment2") != null && !jsonObj.get("comment2").isJsonNull()) && !jsonObj.get("comment2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment2").toString()));
      }
      if ((jsonObj.get("customerNumber") != null && !jsonObj.get("customerNumber").isJsonNull()) && !jsonObj.get("customerNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerNumber").toString()));
      }
      if ((jsonObj.get("deliveryAddressLine1") != null && !jsonObj.get("deliveryAddressLine1").isJsonNull()) && !jsonObj.get("deliveryAddressLine1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryAddressLine1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryAddressLine1").toString()));
      }
      if ((jsonObj.get("deliveryAddressLine2") != null && !jsonObj.get("deliveryAddressLine2").isJsonNull()) && !jsonObj.get("deliveryAddressLine2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryAddressLine2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryAddressLine2").toString()));
      }
      if ((jsonObj.get("deliveryCity") != null && !jsonObj.get("deliveryCity").isJsonNull()) && !jsonObj.get("deliveryCity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryCity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryCity").toString()));
      }
      if ((jsonObj.get("deliveryCountry") != null && !jsonObj.get("deliveryCountry").isJsonNull()) && !jsonObj.get("deliveryCountry").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryCountry` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryCountry").toString()));
      }
      if ((jsonObj.get("deliveryPostCode") != null && !jsonObj.get("deliveryPostCode").isJsonNull()) && !jsonObj.get("deliveryPostCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryPostCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryPostCode").toString()));
      }
      if ((jsonObj.get("merchantCustomerIdentification") != null && !jsonObj.get("merchantCustomerIdentification").isJsonNull()) && !jsonObj.get("merchantCustomerIdentification").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchantCustomerIdentification` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchantCustomerIdentification").toString()));
      }
      if ((jsonObj.get("merchantNumber") != null && !jsonObj.get("merchantNumber").isJsonNull()) && !jsonObj.get("merchantNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchantNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchantNumber").toString()));
      }
      if ((jsonObj.get("orderId") != null && !jsonObj.get("orderId").isJsonNull()) && !jsonObj.get("orderId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderId").toString()));
      }
      if ((jsonObj.get("productId") != null && !jsonObj.get("productId").isJsonNull()) && !jsonObj.get("productId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `productId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("productId").toString()));
      }
      if ((jsonObj.get("variableReference") != null && !jsonObj.get("variableReference").isJsonNull()) && !jsonObj.get("variableReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `variableReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("variableReference").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrderDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderDetails>() {
           @Override
           public void write(JsonWriter out, OrderDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderDetails
   * @throws IOException if the JSON string is invalid with respect to OrderDetails
   */
  public static OrderDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderDetails.class);
  }

  /**
   * Convert an instance of OrderDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

