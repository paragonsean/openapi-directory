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
import org.openapitools.client.model.CartSimulation200ResponsePaymentDataPaymentSystemsInner;

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
 * Payment data information.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200ResponsePaymentData {
  public static final String SERIALIZED_NAME_AVAILABLE_ACCOUNTS = "availableAccounts";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ACCOUNTS)
  private List<Object> availableAccounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_AVAILABLE_ASSOCIATIONS = "availableAssociations";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ASSOCIATIONS)
  private Object availableAssociations;

  public static final String SERIALIZED_NAME_AVAILABLE_TOKENS = "availableTokens";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_TOKENS)
  private List<Object> availableTokens = new ArrayList<>();

  public static final String SERIALIZED_NAME_GIFT_CARD_MESSAGES = "giftCardMessages";
  @SerializedName(SERIALIZED_NAME_GIFT_CARD_MESSAGES)
  private List<Object> giftCardMessages = new ArrayList<>();

  public static final String SERIALIZED_NAME_GIFT_CARDS = "giftCards";
  @SerializedName(SERIALIZED_NAME_GIFT_CARDS)
  private List<Object> giftCards = new ArrayList<>();

  public static final String SERIALIZED_NAME_INSTALLMENT_OPTIONS = "installmentOptions";
  @SerializedName(SERIALIZED_NAME_INSTALLMENT_OPTIONS)
  private List<Object> installmentOptions = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAYMENT_SYSTEMS = "paymentSystems";
  @SerializedName(SERIALIZED_NAME_PAYMENT_SYSTEMS)
  private List<CartSimulation200ResponsePaymentDataPaymentSystemsInner> paymentSystems = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAYMENTS = "payments";
  @SerializedName(SERIALIZED_NAME_PAYMENTS)
  private List<Object> payments = new ArrayList<>();

  public CartSimulation200ResponsePaymentData() {
  }

  public CartSimulation200ResponsePaymentData availableAccounts(List<Object> availableAccounts) {
    this.availableAccounts = availableAccounts;
    return this;
  }

  public CartSimulation200ResponsePaymentData addAvailableAccountsItem(Object availableAccountsItem) {
    if (this.availableAccounts == null) {
      this.availableAccounts = new ArrayList<>();
    }
    this.availableAccounts.add(availableAccountsItem);
    return this;
  }

  /**
   * Available accounts.
   * @return availableAccounts
   */
  @javax.annotation.Nullable
  public List<Object> getAvailableAccounts() {
    return availableAccounts;
  }

  public void setAvailableAccounts(List<Object> availableAccounts) {
    this.availableAccounts = availableAccounts;
  }


  public CartSimulation200ResponsePaymentData availableAssociations(Object availableAssociations) {
    this.availableAssociations = availableAssociations;
    return this;
  }

  /**
   * Available associations.
   * @return availableAssociations
   */
  @javax.annotation.Nullable
  public Object getAvailableAssociations() {
    return availableAssociations;
  }

  public void setAvailableAssociations(Object availableAssociations) {
    this.availableAssociations = availableAssociations;
  }


  public CartSimulation200ResponsePaymentData availableTokens(List<Object> availableTokens) {
    this.availableTokens = availableTokens;
    return this;
  }

  public CartSimulation200ResponsePaymentData addAvailableTokensItem(Object availableTokensItem) {
    if (this.availableTokens == null) {
      this.availableTokens = new ArrayList<>();
    }
    this.availableTokens.add(availableTokensItem);
    return this;
  }

  /**
   * Available tokens.
   * @return availableTokens
   */
  @javax.annotation.Nullable
  public List<Object> getAvailableTokens() {
    return availableTokens;
  }

  public void setAvailableTokens(List<Object> availableTokens) {
    this.availableTokens = availableTokens;
  }


  public CartSimulation200ResponsePaymentData giftCardMessages(List<Object> giftCardMessages) {
    this.giftCardMessages = giftCardMessages;
    return this;
  }

  public CartSimulation200ResponsePaymentData addGiftCardMessagesItem(Object giftCardMessagesItem) {
    if (this.giftCardMessages == null) {
      this.giftCardMessages = new ArrayList<>();
    }
    this.giftCardMessages.add(giftCardMessagesItem);
    return this;
  }

  /**
   * Array of gift card messages.
   * @return giftCardMessages
   */
  @javax.annotation.Nullable
  public List<Object> getGiftCardMessages() {
    return giftCardMessages;
  }

  public void setGiftCardMessages(List<Object> giftCardMessages) {
    this.giftCardMessages = giftCardMessages;
  }


  public CartSimulation200ResponsePaymentData giftCards(List<Object> giftCards) {
    this.giftCards = giftCards;
    return this;
  }

  public CartSimulation200ResponsePaymentData addGiftCardsItem(Object giftCardsItem) {
    if (this.giftCards == null) {
      this.giftCards = new ArrayList<>();
    }
    this.giftCards.add(giftCardsItem);
    return this;
  }

  /**
   * Gift card information, if it applies to the order.
   * @return giftCards
   */
  @javax.annotation.Nullable
  public List<Object> getGiftCards() {
    return giftCards;
  }

  public void setGiftCards(List<Object> giftCards) {
    this.giftCards = giftCards;
  }


  public CartSimulation200ResponsePaymentData installmentOptions(List<Object> installmentOptions) {
    this.installmentOptions = installmentOptions;
    return this;
  }

  /**
   * Installment options information.
   * @return installmentOptions
   */
  @javax.annotation.Nullable
  public List<Object> getInstallmentOptions() {
    return installmentOptions;
  }

  public void setInstallmentOptions(List<Object> installmentOptions) {
    this.installmentOptions = installmentOptions;
  }


  public CartSimulation200ResponsePaymentData paymentSystems(List<CartSimulation200ResponsePaymentDataPaymentSystemsInner> paymentSystems) {
    this.paymentSystems = paymentSystems;
    return this;
  }

  public CartSimulation200ResponsePaymentData addPaymentSystemsItem(CartSimulation200ResponsePaymentDataPaymentSystemsInner paymentSystemsItem) {
    if (this.paymentSystems == null) {
      this.paymentSystems = new ArrayList<>();
    }
    this.paymentSystems.add(paymentSystemsItem);
    return this;
  }

  /**
   * Information on payment systems.
   * @return paymentSystems
   */
  @javax.annotation.Nullable
  public List<CartSimulation200ResponsePaymentDataPaymentSystemsInner> getPaymentSystems() {
    return paymentSystems;
  }

  public void setPaymentSystems(List<CartSimulation200ResponsePaymentDataPaymentSystemsInner> paymentSystems) {
    this.paymentSystems = paymentSystems;
  }


  public CartSimulation200ResponsePaymentData payments(List<Object> payments) {
    this.payments = payments;
    return this;
  }

  public CartSimulation200ResponsePaymentData addPaymentsItem(Object paymentsItem) {
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
  public List<Object> getPayments() {
    return payments;
  }

  public void setPayments(List<Object> payments) {
    this.payments = payments;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CartSimulation200ResponsePaymentData cartSimulation200ResponsePaymentData = (CartSimulation200ResponsePaymentData) o;
    return Objects.equals(this.availableAccounts, cartSimulation200ResponsePaymentData.availableAccounts) &&
        Objects.equals(this.availableAssociations, cartSimulation200ResponsePaymentData.availableAssociations) &&
        Objects.equals(this.availableTokens, cartSimulation200ResponsePaymentData.availableTokens) &&
        Objects.equals(this.giftCardMessages, cartSimulation200ResponsePaymentData.giftCardMessages) &&
        Objects.equals(this.giftCards, cartSimulation200ResponsePaymentData.giftCards) &&
        Objects.equals(this.installmentOptions, cartSimulation200ResponsePaymentData.installmentOptions) &&
        Objects.equals(this.paymentSystems, cartSimulation200ResponsePaymentData.paymentSystems) &&
        Objects.equals(this.payments, cartSimulation200ResponsePaymentData.payments);
  }

  @Override
  public int hashCode() {
    return Objects.hash(availableAccounts, availableAssociations, availableTokens, giftCardMessages, giftCards, installmentOptions, paymentSystems, payments);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CartSimulation200ResponsePaymentData {\n");
    sb.append("    availableAccounts: ").append(toIndentedString(availableAccounts)).append("\n");
    sb.append("    availableAssociations: ").append(toIndentedString(availableAssociations)).append("\n");
    sb.append("    availableTokens: ").append(toIndentedString(availableTokens)).append("\n");
    sb.append("    giftCardMessages: ").append(toIndentedString(giftCardMessages)).append("\n");
    sb.append("    giftCards: ").append(toIndentedString(giftCards)).append("\n");
    sb.append("    installmentOptions: ").append(toIndentedString(installmentOptions)).append("\n");
    sb.append("    paymentSystems: ").append(toIndentedString(paymentSystems)).append("\n");
    sb.append("    payments: ").append(toIndentedString(payments)).append("\n");
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
    openapiFields.add("availableAccounts");
    openapiFields.add("availableAssociations");
    openapiFields.add("availableTokens");
    openapiFields.add("giftCardMessages");
    openapiFields.add("giftCards");
    openapiFields.add("installmentOptions");
    openapiFields.add("paymentSystems");
    openapiFields.add("payments");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200ResponsePaymentData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200ResponsePaymentData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200ResponsePaymentData is not found in the empty JSON string", CartSimulation200ResponsePaymentData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200ResponsePaymentData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200ResponsePaymentData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("availableAccounts") != null && !jsonObj.get("availableAccounts").isJsonNull() && !jsonObj.get("availableAccounts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `availableAccounts` to be an array in the JSON string but got `%s`", jsonObj.get("availableAccounts").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("availableTokens") != null && !jsonObj.get("availableTokens").isJsonNull() && !jsonObj.get("availableTokens").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `availableTokens` to be an array in the JSON string but got `%s`", jsonObj.get("availableTokens").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("giftCardMessages") != null && !jsonObj.get("giftCardMessages").isJsonNull() && !jsonObj.get("giftCardMessages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftCardMessages` to be an array in the JSON string but got `%s`", jsonObj.get("giftCardMessages").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("giftCards") != null && !jsonObj.get("giftCards").isJsonNull() && !jsonObj.get("giftCards").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftCards` to be an array in the JSON string but got `%s`", jsonObj.get("giftCards").toString()));
      }
      if (jsonObj.get("paymentSystems") != null && !jsonObj.get("paymentSystems").isJsonNull()) {
        JsonArray jsonArraypaymentSystems = jsonObj.getAsJsonArray("paymentSystems");
        if (jsonArraypaymentSystems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("paymentSystems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `paymentSystems` to be an array in the JSON string but got `%s`", jsonObj.get("paymentSystems").toString()));
          }

          // validate the optional field `paymentSystems` (array)
          for (int i = 0; i < jsonArraypaymentSystems.size(); i++) {
            CartSimulation200ResponsePaymentDataPaymentSystemsInner.validateJsonElement(jsonArraypaymentSystems.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("payments") != null && !jsonObj.get("payments").isJsonNull() && !jsonObj.get("payments").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `payments` to be an array in the JSON string but got `%s`", jsonObj.get("payments").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200ResponsePaymentData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200ResponsePaymentData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200ResponsePaymentData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200ResponsePaymentData.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200ResponsePaymentData>() {
           @Override
           public void write(JsonWriter out, CartSimulation200ResponsePaymentData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200ResponsePaymentData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200ResponsePaymentData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200ResponsePaymentData
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200ResponsePaymentData
   */
  public static CartSimulation200ResponsePaymentData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200ResponsePaymentData.class);
  }

  /**
   * Convert an instance of CartSimulation200ResponsePaymentData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

