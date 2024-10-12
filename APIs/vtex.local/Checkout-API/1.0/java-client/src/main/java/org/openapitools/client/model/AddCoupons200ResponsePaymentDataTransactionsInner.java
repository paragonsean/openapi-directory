/*
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
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
import org.openapitools.client.model.AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner;

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
 * AddCoupons200ResponsePaymentDataTransactionsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddCoupons200ResponsePaymentDataTransactionsInner {
  public static final String SERIALIZED_NAME_IS_ACTIVE = "isActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_MERCHANT_NAME = "merchantName";
  @SerializedName(SERIALIZED_NAME_MERCHANT_NAME)
  private String merchantName;

  public static final String SERIALIZED_NAME_PAYMENTS = "payments";
  @SerializedName(SERIALIZED_NAME_PAYMENTS)
  private List<AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner> payments = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHARED_TRANSACTION = "sharedTransaction";
  @SerializedName(SERIALIZED_NAME_SHARED_TRANSACTION)
  private Boolean sharedTransaction;

  public static final String SERIALIZED_NAME_TRANSACTION_ID = "transactionId";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_ID)
  private String transactionId;

  public AddCoupons200ResponsePaymentDataTransactionsInner() {
  }

  public AddCoupons200ResponsePaymentDataTransactionsInner isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Indicates whether transaction is active.
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public AddCoupons200ResponsePaymentDataTransactionsInner merchantName(String merchantName) {
    this.merchantName = merchantName;
    return this;
  }

  /**
   * Merchant name.
   * @return merchantName
   */
  @javax.annotation.Nullable
  public String getMerchantName() {
    return merchantName;
  }

  public void setMerchantName(String merchantName) {
    this.merchantName = merchantName;
  }


  public AddCoupons200ResponsePaymentDataTransactionsInner payments(List<AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner> payments) {
    this.payments = payments;
    return this;
  }

  public AddCoupons200ResponsePaymentDataTransactionsInner addPaymentsItem(AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner paymentsItem) {
    if (this.payments == null) {
      this.payments = new ArrayList<>();
    }
    this.payments.add(paymentsItem);
    return this;
  }

  /**
   * Information on each payment.
   * @return payments
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner> getPayments() {
    return payments;
  }

  public void setPayments(List<AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner> payments) {
    this.payments = payments;
  }


  public AddCoupons200ResponsePaymentDataTransactionsInner sharedTransaction(Boolean sharedTransaction) {
    this.sharedTransaction = sharedTransaction;
    return this;
  }

  /**
   * Indicates whather transaction is shared.
   * @return sharedTransaction
   */
  @javax.annotation.Nullable
  public Boolean getSharedTransaction() {
    return sharedTransaction;
  }

  public void setSharedTransaction(Boolean sharedTransaction) {
    this.sharedTransaction = sharedTransaction;
  }


  public AddCoupons200ResponsePaymentDataTransactionsInner transactionId(String transactionId) {
    this.transactionId = transactionId;
    return this;
  }

  /**
   * Transaction ID.
   * @return transactionId
   */
  @javax.annotation.Nullable
  public String getTransactionId() {
    return transactionId;
  }

  public void setTransactionId(String transactionId) {
    this.transactionId = transactionId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddCoupons200ResponsePaymentDataTransactionsInner addCoupons200ResponsePaymentDataTransactionsInner = (AddCoupons200ResponsePaymentDataTransactionsInner) o;
    return Objects.equals(this.isActive, addCoupons200ResponsePaymentDataTransactionsInner.isActive) &&
        Objects.equals(this.merchantName, addCoupons200ResponsePaymentDataTransactionsInner.merchantName) &&
        Objects.equals(this.payments, addCoupons200ResponsePaymentDataTransactionsInner.payments) &&
        Objects.equals(this.sharedTransaction, addCoupons200ResponsePaymentDataTransactionsInner.sharedTransaction) &&
        Objects.equals(this.transactionId, addCoupons200ResponsePaymentDataTransactionsInner.transactionId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isActive, merchantName, payments, sharedTransaction, transactionId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddCoupons200ResponsePaymentDataTransactionsInner {\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    merchantName: ").append(toIndentedString(merchantName)).append("\n");
    sb.append("    payments: ").append(toIndentedString(payments)).append("\n");
    sb.append("    sharedTransaction: ").append(toIndentedString(sharedTransaction)).append("\n");
    sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
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
    openapiFields.add("isActive");
    openapiFields.add("merchantName");
    openapiFields.add("payments");
    openapiFields.add("sharedTransaction");
    openapiFields.add("transactionId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddCoupons200ResponsePaymentDataTransactionsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddCoupons200ResponsePaymentDataTransactionsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddCoupons200ResponsePaymentDataTransactionsInner is not found in the empty JSON string", AddCoupons200ResponsePaymentDataTransactionsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddCoupons200ResponsePaymentDataTransactionsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddCoupons200ResponsePaymentDataTransactionsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("merchantName") != null && !jsonObj.get("merchantName").isJsonNull()) && !jsonObj.get("merchantName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchantName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchantName").toString()));
      }
      if (jsonObj.get("payments") != null && !jsonObj.get("payments").isJsonNull()) {
        JsonArray jsonArraypayments = jsonObj.getAsJsonArray("payments");
        if (jsonArraypayments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("payments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `payments` to be an array in the JSON string but got `%s`", jsonObj.get("payments").toString()));
          }

          // validate the optional field `payments` (array)
          for (int i = 0; i < jsonArraypayments.size(); i++) {
            AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner.validateJsonElement(jsonArraypayments.get(i));
          };
        }
      }
      if ((jsonObj.get("transactionId") != null && !jsonObj.get("transactionId").isJsonNull()) && !jsonObj.get("transactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactionId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddCoupons200ResponsePaymentDataTransactionsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddCoupons200ResponsePaymentDataTransactionsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddCoupons200ResponsePaymentDataTransactionsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddCoupons200ResponsePaymentDataTransactionsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AddCoupons200ResponsePaymentDataTransactionsInner>() {
           @Override
           public void write(JsonWriter out, AddCoupons200ResponsePaymentDataTransactionsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddCoupons200ResponsePaymentDataTransactionsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddCoupons200ResponsePaymentDataTransactionsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddCoupons200ResponsePaymentDataTransactionsInner
   * @throws IOException if the JSON string is invalid with respect to AddCoupons200ResponsePaymentDataTransactionsInner
   */
  public static AddCoupons200ResponsePaymentDataTransactionsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddCoupons200ResponsePaymentDataTransactionsInner.class);
  }

  /**
   * Convert an instance of AddCoupons200ResponsePaymentDataTransactionsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

