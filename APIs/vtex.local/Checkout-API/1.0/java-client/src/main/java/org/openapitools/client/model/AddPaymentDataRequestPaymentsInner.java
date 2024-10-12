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
 * AddPaymentDataRequestPaymentsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddPaymentDataRequestPaymentsInner {
  public static final String SERIALIZED_NAME_GROUP = "group";
  @SerializedName(SERIALIZED_NAME_GROUP)
  private String group = "bankInvoicePaymentGroup";

  public static final String SERIALIZED_NAME_HAS_DEFAULT_BILLING_ADDRESS = "hasDefaultBillingAddress";
  @SerializedName(SERIALIZED_NAME_HAS_DEFAULT_BILLING_ADDRESS)
  private Boolean hasDefaultBillingAddress = false;

  public static final String SERIALIZED_NAME_INSTALLMENTS = "installments";
  @SerializedName(SERIALIZED_NAME_INSTALLMENTS)
  private Integer installments = 1;

  public static final String SERIALIZED_NAME_INSTALLMENTS_INTEREST_RATE = "installmentsInterestRate";
  @SerializedName(SERIALIZED_NAME_INSTALLMENTS_INTEREST_RATE)
  private BigDecimal installmentsInterestRate = new BigDecimal("0");

  public static final String SERIALIZED_NAME_INSTALLMENTS_VALUE = "installmentsValue";
  @SerializedName(SERIALIZED_NAME_INSTALLMENTS_VALUE)
  private Integer installmentsValue = 1;

  public static final String SERIALIZED_NAME_PAYMENT_SYSTEM = "paymentSystem";
  @SerializedName(SERIALIZED_NAME_PAYMENT_SYSTEM)
  private Integer paymentSystem = 1;

  public static final String SERIALIZED_NAME_PAYMENT_SYSTEM_NAME = "paymentSystemName";
  @SerializedName(SERIALIZED_NAME_PAYMENT_SYSTEM_NAME)
  private String paymentSystemName = "Boleto Bancário";

  public static final String SERIALIZED_NAME_REFERENCE_VALUE = "referenceValue";
  @SerializedName(SERIALIZED_NAME_REFERENCE_VALUE)
  private Integer referenceValue = 100;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Integer value = 100;

  public AddPaymentDataRequestPaymentsInner() {
  }

  public AddPaymentDataRequestPaymentsInner group(String group) {
    this.group = group;
    return this;
  }

  /**
   * Payment system group.
   * @return group
   */
  @javax.annotation.Nullable
  public String getGroup() {
    return group;
  }

  public void setGroup(String group) {
    this.group = group;
  }


  public AddPaymentDataRequestPaymentsInner hasDefaultBillingAddress(Boolean hasDefaultBillingAddress) {
    this.hasDefaultBillingAddress = hasDefaultBillingAddress;
    return this;
  }

  /**
   * Indicates whether billing address for this payment is the default address.
   * @return hasDefaultBillingAddress
   */
  @javax.annotation.Nullable
  public Boolean getHasDefaultBillingAddress() {
    return hasDefaultBillingAddress;
  }

  public void setHasDefaultBillingAddress(Boolean hasDefaultBillingAddress) {
    this.hasDefaultBillingAddress = hasDefaultBillingAddress;
  }


  public AddPaymentDataRequestPaymentsInner installments(Integer installments) {
    this.installments = installments;
    return this;
  }

  /**
   * Selected number of installments.
   * @return installments
   */
  @javax.annotation.Nullable
  public Integer getInstallments() {
    return installments;
  }

  public void setInstallments(Integer installments) {
    this.installments = installments;
  }


  public AddPaymentDataRequestPaymentsInner installmentsInterestRate(BigDecimal installmentsInterestRate) {
    this.installmentsInterestRate = installmentsInterestRate;
    return this;
  }

  /**
   * Installments&#39; interest rate.
   * @return installmentsInterestRate
   */
  @javax.annotation.Nullable
  public BigDecimal getInstallmentsInterestRate() {
    return installmentsInterestRate;
  }

  public void setInstallmentsInterestRate(BigDecimal installmentsInterestRate) {
    this.installmentsInterestRate = installmentsInterestRate;
  }


  public AddPaymentDataRequestPaymentsInner installmentsValue(Integer installmentsValue) {
    this.installmentsValue = installmentsValue;
    return this;
  }

  /**
   * Value of the installments.
   * @return installmentsValue
   */
  @javax.annotation.Nullable
  public Integer getInstallmentsValue() {
    return installmentsValue;
  }

  public void setInstallmentsValue(Integer installmentsValue) {
    this.installmentsValue = installmentsValue;
  }


  public AddPaymentDataRequestPaymentsInner paymentSystem(Integer paymentSystem) {
    this.paymentSystem = paymentSystem;
    return this;
  }

  /**
   * Payment system ID.
   * @return paymentSystem
   */
  @javax.annotation.Nullable
  public Integer getPaymentSystem() {
    return paymentSystem;
  }

  public void setPaymentSystem(Integer paymentSystem) {
    this.paymentSystem = paymentSystem;
  }


  public AddPaymentDataRequestPaymentsInner paymentSystemName(String paymentSystemName) {
    this.paymentSystemName = paymentSystemName;
    return this;
  }

  /**
   * Payment system name.
   * @return paymentSystemName
   */
  @javax.annotation.Nullable
  public String getPaymentSystemName() {
    return paymentSystemName;
  }

  public void setPaymentSystemName(String paymentSystemName) {
    this.paymentSystemName = paymentSystemName;
  }


  public AddPaymentDataRequestPaymentsInner referenceValue(Integer referenceValue) {
    this.referenceValue = referenceValue;
    return this;
  }

  /**
   * Reference value used to calculate total order value with interest.
   * @return referenceValue
   */
  @javax.annotation.Nullable
  public Integer getReferenceValue() {
    return referenceValue;
  }

  public void setReferenceValue(Integer referenceValue) {
    this.referenceValue = referenceValue;
  }


  public AddPaymentDataRequestPaymentsInner value(Integer value) {
    this.value = value;
    return this;
  }

  /**
   * Total value assigned to this payment.
   * @return value
   */
  @javax.annotation.Nullable
  public Integer getValue() {
    return value;
  }

  public void setValue(Integer value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddPaymentDataRequestPaymentsInner addPaymentDataRequestPaymentsInner = (AddPaymentDataRequestPaymentsInner) o;
    return Objects.equals(this.group, addPaymentDataRequestPaymentsInner.group) &&
        Objects.equals(this.hasDefaultBillingAddress, addPaymentDataRequestPaymentsInner.hasDefaultBillingAddress) &&
        Objects.equals(this.installments, addPaymentDataRequestPaymentsInner.installments) &&
        Objects.equals(this.installmentsInterestRate, addPaymentDataRequestPaymentsInner.installmentsInterestRate) &&
        Objects.equals(this.installmentsValue, addPaymentDataRequestPaymentsInner.installmentsValue) &&
        Objects.equals(this.paymentSystem, addPaymentDataRequestPaymentsInner.paymentSystem) &&
        Objects.equals(this.paymentSystemName, addPaymentDataRequestPaymentsInner.paymentSystemName) &&
        Objects.equals(this.referenceValue, addPaymentDataRequestPaymentsInner.referenceValue) &&
        Objects.equals(this.value, addPaymentDataRequestPaymentsInner.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(group, hasDefaultBillingAddress, installments, installmentsInterestRate, installmentsValue, paymentSystem, paymentSystemName, referenceValue, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddPaymentDataRequestPaymentsInner {\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    hasDefaultBillingAddress: ").append(toIndentedString(hasDefaultBillingAddress)).append("\n");
    sb.append("    installments: ").append(toIndentedString(installments)).append("\n");
    sb.append("    installmentsInterestRate: ").append(toIndentedString(installmentsInterestRate)).append("\n");
    sb.append("    installmentsValue: ").append(toIndentedString(installmentsValue)).append("\n");
    sb.append("    paymentSystem: ").append(toIndentedString(paymentSystem)).append("\n");
    sb.append("    paymentSystemName: ").append(toIndentedString(paymentSystemName)).append("\n");
    sb.append("    referenceValue: ").append(toIndentedString(referenceValue)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("group");
    openapiFields.add("hasDefaultBillingAddress");
    openapiFields.add("installments");
    openapiFields.add("installmentsInterestRate");
    openapiFields.add("installmentsValue");
    openapiFields.add("paymentSystem");
    openapiFields.add("paymentSystemName");
    openapiFields.add("referenceValue");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddPaymentDataRequestPaymentsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddPaymentDataRequestPaymentsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddPaymentDataRequestPaymentsInner is not found in the empty JSON string", AddPaymentDataRequestPaymentsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddPaymentDataRequestPaymentsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddPaymentDataRequestPaymentsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("group") != null && !jsonObj.get("group").isJsonNull()) && !jsonObj.get("group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group").toString()));
      }
      if ((jsonObj.get("paymentSystemName") != null && !jsonObj.get("paymentSystemName").isJsonNull()) && !jsonObj.get("paymentSystemName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentSystemName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentSystemName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddPaymentDataRequestPaymentsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddPaymentDataRequestPaymentsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddPaymentDataRequestPaymentsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddPaymentDataRequestPaymentsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AddPaymentDataRequestPaymentsInner>() {
           @Override
           public void write(JsonWriter out, AddPaymentDataRequestPaymentsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddPaymentDataRequestPaymentsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddPaymentDataRequestPaymentsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddPaymentDataRequestPaymentsInner
   * @throws IOException if the JSON string is invalid with respect to AddPaymentDataRequestPaymentsInner
   */
  public static AddPaymentDataRequestPaymentsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddPaymentDataRequestPaymentsInner.class);
  }

  /**
   * Convert an instance of AddPaymentDataRequestPaymentsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

