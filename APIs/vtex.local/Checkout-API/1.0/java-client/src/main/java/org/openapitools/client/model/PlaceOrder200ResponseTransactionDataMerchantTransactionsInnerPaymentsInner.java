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
import java.util.Arrays;
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
 * PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner {
  public static final String SERIALIZED_NAME_ACCOUNT_ID = "accountId";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_ID)
  private String accountId;

  public static final String SERIALIZED_NAME_BIN = "bin";
  @SerializedName(SERIALIZED_NAME_BIN)
  private String bin;

  public static final String SERIALIZED_NAME_GIFT_CARD_ID = "giftCardId";
  @SerializedName(SERIALIZED_NAME_GIFT_CARD_ID)
  private String giftCardId;

  public static final String SERIALIZED_NAME_GIFT_CARD_PROVIDER = "giftCardProvider";
  @SerializedName(SERIALIZED_NAME_GIFT_CARD_PROVIDER)
  private String giftCardProvider;

  public static final String SERIALIZED_NAME_GIFT_CARD_REDEMPTION_CODE = "giftCardRedemptionCode";
  @SerializedName(SERIALIZED_NAME_GIFT_CARD_REDEMPTION_CODE)
  private String giftCardRedemptionCode;

  public static final String SERIALIZED_NAME_PAYMENT_SYSTEM = "paymentSystem";
  @SerializedName(SERIALIZED_NAME_PAYMENT_SYSTEM)
  private String paymentSystem;

  public static final String SERIALIZED_NAME_REFERENCE_VALUE = "referenceValue";
  @SerializedName(SERIALIZED_NAME_REFERENCE_VALUE)
  private Integer referenceValue;

  public static final String SERIALIZED_NAME_TOKEN_ID = "tokenId";
  @SerializedName(SERIALIZED_NAME_TOKEN_ID)
  private String tokenId;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Integer value;

  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner() {
  }

  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner accountId(String accountId) {
    this.accountId = accountId;
    return this;
  }

  /**
   * Account ID.
   * @return accountId
   */
  @javax.annotation.Nullable
  public String getAccountId() {
    return accountId;
  }

  public void setAccountId(String accountId) {
    this.accountId = accountId;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner bin(String bin) {
    this.bin = bin;
    return this;
  }

  /**
   * Payment bin.
   * @return bin
   */
  @javax.annotation.Nullable
  public String getBin() {
    return bin;
  }

  public void setBin(String bin) {
    this.bin = bin;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner giftCardId(String giftCardId) {
    this.giftCardId = giftCardId;
    return this;
  }

  /**
   * Gift card ID.
   * @return giftCardId
   */
  @javax.annotation.Nullable
  public String getGiftCardId() {
    return giftCardId;
  }

  public void setGiftCardId(String giftCardId) {
    this.giftCardId = giftCardId;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner giftCardProvider(String giftCardProvider) {
    this.giftCardProvider = giftCardProvider;
    return this;
  }

  /**
   * Gift card provider.
   * @return giftCardProvider
   */
  @javax.annotation.Nullable
  public String getGiftCardProvider() {
    return giftCardProvider;
  }

  public void setGiftCardProvider(String giftCardProvider) {
    this.giftCardProvider = giftCardProvider;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner giftCardRedemptionCode(String giftCardRedemptionCode) {
    this.giftCardRedemptionCode = giftCardRedemptionCode;
    return this;
  }

  /**
   * Gift card redemption code.
   * @return giftCardRedemptionCode
   */
  @javax.annotation.Nullable
  public String getGiftCardRedemptionCode() {
    return giftCardRedemptionCode;
  }

  public void setGiftCardRedemptionCode(String giftCardRedemptionCode) {
    this.giftCardRedemptionCode = giftCardRedemptionCode;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner paymentSystem(String paymentSystem) {
    this.paymentSystem = paymentSystem;
    return this;
  }

  /**
   * Payment system.
   * @return paymentSystem
   */
  @javax.annotation.Nullable
  public String getPaymentSystem() {
    return paymentSystem;
  }

  public void setPaymentSystem(String paymentSystem) {
    this.paymentSystem = paymentSystem;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner referenceValue(Integer referenceValue) {
    this.referenceValue = referenceValue;
    return this;
  }

  /**
   * Reference value over which interests may be applied.
   * @return referenceValue
   */
  @javax.annotation.Nullable
  public Integer getReferenceValue() {
    return referenceValue;
  }

  public void setReferenceValue(Integer referenceValue) {
    this.referenceValue = referenceValue;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner tokenId(String tokenId) {
    this.tokenId = tokenId;
    return this;
  }

  /**
   * Token ID.
   * @return tokenId
   */
  @javax.annotation.Nullable
  public String getTokenId() {
    return tokenId;
  }

  public void setTokenId(String tokenId) {
    this.tokenId = tokenId;
  }


  public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner value(Integer value) {
    this.value = value;
    return this;
  }

  /**
   * Total value to be paid in this payment.
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
    PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner = (PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner) o;
    return Objects.equals(this.accountId, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.accountId) &&
        Objects.equals(this.bin, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.bin) &&
        Objects.equals(this.giftCardId, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.giftCardId) &&
        Objects.equals(this.giftCardProvider, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.giftCardProvider) &&
        Objects.equals(this.giftCardRedemptionCode, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.giftCardRedemptionCode) &&
        Objects.equals(this.paymentSystem, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.paymentSystem) &&
        Objects.equals(this.referenceValue, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.referenceValue) &&
        Objects.equals(this.tokenId, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.tokenId) &&
        Objects.equals(this.value, placeOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.value);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountId, bin, giftCardId, giftCardProvider, giftCardRedemptionCode, paymentSystem, referenceValue, tokenId, value);
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
    sb.append("class PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner {\n");
    sb.append("    accountId: ").append(toIndentedString(accountId)).append("\n");
    sb.append("    bin: ").append(toIndentedString(bin)).append("\n");
    sb.append("    giftCardId: ").append(toIndentedString(giftCardId)).append("\n");
    sb.append("    giftCardProvider: ").append(toIndentedString(giftCardProvider)).append("\n");
    sb.append("    giftCardRedemptionCode: ").append(toIndentedString(giftCardRedemptionCode)).append("\n");
    sb.append("    paymentSystem: ").append(toIndentedString(paymentSystem)).append("\n");
    sb.append("    referenceValue: ").append(toIndentedString(referenceValue)).append("\n");
    sb.append("    tokenId: ").append(toIndentedString(tokenId)).append("\n");
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
    openapiFields.add("accountId");
    openapiFields.add("bin");
    openapiFields.add("giftCardId");
    openapiFields.add("giftCardProvider");
    openapiFields.add("giftCardRedemptionCode");
    openapiFields.add("paymentSystem");
    openapiFields.add("referenceValue");
    openapiFields.add("tokenId");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner is not found in the empty JSON string", PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("accountId") != null && !jsonObj.get("accountId").isJsonNull()) && !jsonObj.get("accountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountId").toString()));
      }
      if ((jsonObj.get("bin") != null && !jsonObj.get("bin").isJsonNull()) && !jsonObj.get("bin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bin").toString()));
      }
      if ((jsonObj.get("giftCardId") != null && !jsonObj.get("giftCardId").isJsonNull()) && !jsonObj.get("giftCardId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftCardId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("giftCardId").toString()));
      }
      if ((jsonObj.get("giftCardProvider") != null && !jsonObj.get("giftCardProvider").isJsonNull()) && !jsonObj.get("giftCardProvider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftCardProvider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("giftCardProvider").toString()));
      }
      if ((jsonObj.get("giftCardRedemptionCode") != null && !jsonObj.get("giftCardRedemptionCode").isJsonNull()) && !jsonObj.get("giftCardRedemptionCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftCardRedemptionCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("giftCardRedemptionCode").toString()));
      }
      if ((jsonObj.get("paymentSystem") != null && !jsonObj.get("paymentSystem").isJsonNull()) && !jsonObj.get("paymentSystem").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentSystem` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentSystem").toString()));
      }
      if ((jsonObj.get("tokenId") != null && !jsonObj.get("tokenId").isJsonNull()) && !jsonObj.get("tokenId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tokenId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tokenId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner>() {
           @Override
           public void write(JsonWriter out, PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner
   * @throws IOException if the JSON string is invalid with respect to PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner
   */
  public static PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.class);
  }

  /**
   * Convert an instance of PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

