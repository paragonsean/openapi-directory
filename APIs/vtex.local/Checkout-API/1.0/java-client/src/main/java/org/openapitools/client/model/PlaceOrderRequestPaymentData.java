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
import org.openapitools.client.model.PlaceOrderRequestPaymentDataGiftCardsInner;
import org.openapitools.client.model.PlaceOrderRequestPaymentDataPaymentSystemsInner;
import org.openapitools.client.model.PlaceOrderRequestPaymentDataPaymentsInner;

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
 * Payment infomation.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrderRequestPaymentData {
  public static final String SERIALIZED_NAME_GIFT_CARD_MESSAGES = "giftCardMessages";
  @SerializedName(SERIALIZED_NAME_GIFT_CARD_MESSAGES)
  private List<Object> giftCardMessages = new ArrayList<>();

  public static final String SERIALIZED_NAME_GIFT_CARDS = "giftCards";
  @SerializedName(SERIALIZED_NAME_GIFT_CARDS)
  private List<PlaceOrderRequestPaymentDataGiftCardsInner> giftCards = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAYMENT_SYSTEMS = "paymentSystems";
  @SerializedName(SERIALIZED_NAME_PAYMENT_SYSTEMS)
  private List<PlaceOrderRequestPaymentDataPaymentSystemsInner> paymentSystems = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAYMENTS = "payments";
  @SerializedName(SERIALIZED_NAME_PAYMENTS)
  private List<PlaceOrderRequestPaymentDataPaymentsInner> payments = new ArrayList<>();

  public static final String SERIALIZED_NAME_UPDATE_STATUS = "updateStatus";
  @SerializedName(SERIALIZED_NAME_UPDATE_STATUS)
  private String updateStatus = "updated";

  public PlaceOrderRequestPaymentData() {
  }

  public PlaceOrderRequestPaymentData giftCardMessages(List<Object> giftCardMessages) {
    this.giftCardMessages = giftCardMessages;
    return this;
  }

  public PlaceOrderRequestPaymentData addGiftCardMessagesItem(Object giftCardMessagesItem) {
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


  public PlaceOrderRequestPaymentData giftCards(List<PlaceOrderRequestPaymentDataGiftCardsInner> giftCards) {
    this.giftCards = giftCards;
    return this;
  }

  public PlaceOrderRequestPaymentData addGiftCardsItem(PlaceOrderRequestPaymentDataGiftCardsInner giftCardsItem) {
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
  public List<PlaceOrderRequestPaymentDataGiftCardsInner> getGiftCards() {
    return giftCards;
  }

  public void setGiftCards(List<PlaceOrderRequestPaymentDataGiftCardsInner> giftCards) {
    this.giftCards = giftCards;
  }


  public PlaceOrderRequestPaymentData paymentSystems(List<PlaceOrderRequestPaymentDataPaymentSystemsInner> paymentSystems) {
    this.paymentSystems = paymentSystems;
    return this;
  }

  public PlaceOrderRequestPaymentData addPaymentSystemsItem(PlaceOrderRequestPaymentDataPaymentSystemsInner paymentSystemsItem) {
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
  public List<PlaceOrderRequestPaymentDataPaymentSystemsInner> getPaymentSystems() {
    return paymentSystems;
  }

  public void setPaymentSystems(List<PlaceOrderRequestPaymentDataPaymentSystemsInner> paymentSystems) {
    this.paymentSystems = paymentSystems;
  }


  public PlaceOrderRequestPaymentData payments(List<PlaceOrderRequestPaymentDataPaymentsInner> payments) {
    this.payments = payments;
    return this;
  }

  public PlaceOrderRequestPaymentData addPaymentsItem(PlaceOrderRequestPaymentDataPaymentsInner paymentsItem) {
    if (this.payments == null) {
      this.payments = new ArrayList<>();
    }
    this.payments.add(paymentsItem);
    return this;
  }

  /**
   * Payment information.
   * @return payments
   */
  @javax.annotation.Nonnull
  public List<PlaceOrderRequestPaymentDataPaymentsInner> getPayments() {
    return payments;
  }

  public void setPayments(List<PlaceOrderRequestPaymentDataPaymentsInner> payments) {
    this.payments = payments;
  }


  public PlaceOrderRequestPaymentData updateStatus(String updateStatus) {
    this.updateStatus = updateStatus;
    return this;
  }

  /**
   * Indicates whether this object&#39;s information is up to date according to the order&#39;s items. An order can not be placed if &#x60;\&quot;outdated\&quot;&#x60;
   * @return updateStatus
   */
  @javax.annotation.Nullable
  public String getUpdateStatus() {
    return updateStatus;
  }

  public void setUpdateStatus(String updateStatus) {
    this.updateStatus = updateStatus;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaceOrderRequestPaymentData placeOrderRequestPaymentData = (PlaceOrderRequestPaymentData) o;
    return Objects.equals(this.giftCardMessages, placeOrderRequestPaymentData.giftCardMessages) &&
        Objects.equals(this.giftCards, placeOrderRequestPaymentData.giftCards) &&
        Objects.equals(this.paymentSystems, placeOrderRequestPaymentData.paymentSystems) &&
        Objects.equals(this.payments, placeOrderRequestPaymentData.payments) &&
        Objects.equals(this.updateStatus, placeOrderRequestPaymentData.updateStatus);
  }

  @Override
  public int hashCode() {
    return Objects.hash(giftCardMessages, giftCards, paymentSystems, payments, updateStatus);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrderRequestPaymentData {\n");
    sb.append("    giftCardMessages: ").append(toIndentedString(giftCardMessages)).append("\n");
    sb.append("    giftCards: ").append(toIndentedString(giftCards)).append("\n");
    sb.append("    paymentSystems: ").append(toIndentedString(paymentSystems)).append("\n");
    sb.append("    payments: ").append(toIndentedString(payments)).append("\n");
    sb.append("    updateStatus: ").append(toIndentedString(updateStatus)).append("\n");
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
    openapiFields.add("giftCardMessages");
    openapiFields.add("giftCards");
    openapiFields.add("paymentSystems");
    openapiFields.add("payments");
    openapiFields.add("updateStatus");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("payments");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrderRequestPaymentData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrderRequestPaymentData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrderRequestPaymentData is not found in the empty JSON string", PlaceOrderRequestPaymentData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrderRequestPaymentData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrderRequestPaymentData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PlaceOrderRequestPaymentData.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("giftCardMessages") != null && !jsonObj.get("giftCardMessages").isJsonNull() && !jsonObj.get("giftCardMessages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftCardMessages` to be an array in the JSON string but got `%s`", jsonObj.get("giftCardMessages").toString()));
      }
      if (jsonObj.get("giftCards") != null && !jsonObj.get("giftCards").isJsonNull()) {
        JsonArray jsonArraygiftCards = jsonObj.getAsJsonArray("giftCards");
        if (jsonArraygiftCards != null) {
          // ensure the json data is an array
          if (!jsonObj.get("giftCards").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `giftCards` to be an array in the JSON string but got `%s`", jsonObj.get("giftCards").toString()));
          }

          // validate the optional field `giftCards` (array)
          for (int i = 0; i < jsonArraygiftCards.size(); i++) {
            PlaceOrderRequestPaymentDataGiftCardsInner.validateJsonElement(jsonArraygiftCards.get(i));
          };
        }
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
            PlaceOrderRequestPaymentDataPaymentSystemsInner.validateJsonElement(jsonArraypaymentSystems.get(i));
          };
        }
      }
      // ensure the json data is an array
      if (!jsonObj.get("payments").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `payments` to be an array in the JSON string but got `%s`", jsonObj.get("payments").toString()));
      }

      JsonArray jsonArraypayments = jsonObj.getAsJsonArray("payments");
      // validate the required field `payments` (array)
      for (int i = 0; i < jsonArraypayments.size(); i++) {
        PlaceOrderRequestPaymentDataPaymentsInner.validateJsonElement(jsonArraypayments.get(i));
      };
      if ((jsonObj.get("updateStatus") != null && !jsonObj.get("updateStatus").isJsonNull()) && !jsonObj.get("updateStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updateStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updateStatus").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrderRequestPaymentData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrderRequestPaymentData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrderRequestPaymentData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrderRequestPaymentData.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrderRequestPaymentData>() {
           @Override
           public void write(JsonWriter out, PlaceOrderRequestPaymentData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrderRequestPaymentData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrderRequestPaymentData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrderRequestPaymentData
   * @throws IOException if the JSON string is invalid with respect to PlaceOrderRequestPaymentData
   */
  public static PlaceOrderRequestPaymentData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrderRequestPaymentData.class);
  }

  /**
   * Convert an instance of PlaceOrderRequestPaymentData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

