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
import org.openapitools.client.model.CartSimulation200ResponseItemsInner;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInner;
import org.openapitools.client.model.CartSimulation200ResponsePaymentData;
import org.openapitools.client.model.CartSimulation200ResponseRatesAndBenefitsData;
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
 * CartSimulation200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200Response {
  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<CartSimulation200ResponseItemsInner> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOGISTICS_INFO = "logisticsInfo";
  @SerializedName(SERIALIZED_NAME_LOGISTICS_INFO)
  private List<CartSimulation200ResponseLogisticsInfoInner> logisticsInfo = new ArrayList<>();

  public static final String SERIALIZED_NAME_MARKETING_DATA = "marketingData";
  @SerializedName(SERIALIZED_NAME_MARKETING_DATA)
  private Object marketingData;

  public static final String SERIALIZED_NAME_PAYMENT_DATA = "paymentData";
  @SerializedName(SERIALIZED_NAME_PAYMENT_DATA)
  private CartSimulation200ResponsePaymentData paymentData;

  public static final String SERIALIZED_NAME_POSTAL_CODE = "postalCode";
  @SerializedName(SERIALIZED_NAME_POSTAL_CODE)
  private String postalCode;

  public static final String SERIALIZED_NAME_RATES_AND_BENEFITS_DATA = "ratesAndBenefitsData";
  @SerializedName(SERIALIZED_NAME_RATES_AND_BENEFITS_DATA)
  private CartSimulation200ResponseRatesAndBenefitsData ratesAndBenefitsData;

  public static final String SERIALIZED_NAME_SELECTABLE_GIFTS = "selectableGifts";
  @SerializedName(SERIALIZED_NAME_SELECTABLE_GIFTS)
  private List<Object> selectableGifts = new ArrayList<>();

  public CartSimulation200Response() {
  }

  public CartSimulation200Response country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Three letter ISO code of the country of the shipping address.
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public CartSimulation200Response items(List<CartSimulation200ResponseItemsInner> items) {
    this.items = items;
    return this;
  }

  public CartSimulation200Response addItemsItem(CartSimulation200ResponseItemsInner itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Information on each item in the cart.
   * @return items
   */
  @javax.annotation.Nullable
  public List<CartSimulation200ResponseItemsInner> getItems() {
    return items;
  }

  public void setItems(List<CartSimulation200ResponseItemsInner> items) {
    this.items = items;
  }


  public CartSimulation200Response logisticsInfo(List<CartSimulation200ResponseLogisticsInfoInner> logisticsInfo) {
    this.logisticsInfo = logisticsInfo;
    return this;
  }

  public CartSimulation200Response addLogisticsInfoItem(CartSimulation200ResponseLogisticsInfoInner logisticsInfoItem) {
    if (this.logisticsInfo == null) {
      this.logisticsInfo = new ArrayList<>();
    }
    this.logisticsInfo.add(logisticsInfoItem);
    return this;
  }

  /**
   * Array with logistics information on each item of the &#x60;items&#x60; array in the &#x60;orderForm&#x60;.
   * @return logisticsInfo
   */
  @javax.annotation.Nullable
  public List<CartSimulation200ResponseLogisticsInfoInner> getLogisticsInfo() {
    return logisticsInfo;
  }

  public void setLogisticsInfo(List<CartSimulation200ResponseLogisticsInfoInner> logisticsInfo) {
    this.logisticsInfo = logisticsInfo;
  }


  public CartSimulation200Response marketingData(Object marketingData) {
    this.marketingData = marketingData;
    return this;
  }

  /**
   * Object containing promotion data such as coupon tracking information and internal or external UTMs.
   * @return marketingData
   */
  @javax.annotation.Nullable
  public Object getMarketingData() {
    return marketingData;
  }

  public void setMarketingData(Object marketingData) {
    this.marketingData = marketingData;
  }


  public CartSimulation200Response paymentData(CartSimulation200ResponsePaymentData paymentData) {
    this.paymentData = paymentData;
    return this;
  }

  /**
   * Get paymentData
   * @return paymentData
   */
  @javax.annotation.Nullable
  public CartSimulation200ResponsePaymentData getPaymentData() {
    return paymentData;
  }

  public void setPaymentData(CartSimulation200ResponsePaymentData paymentData) {
    this.paymentData = paymentData;
  }


  public CartSimulation200Response postalCode(String postalCode) {
    this.postalCode = postalCode;
    return this;
  }

  /**
   * Postal Code.
   * @return postalCode
   */
  @javax.annotation.Nullable
  public String getPostalCode() {
    return postalCode;
  }

  public void setPostalCode(String postalCode) {
    this.postalCode = postalCode;
  }


  public CartSimulation200Response ratesAndBenefitsData(CartSimulation200ResponseRatesAndBenefitsData ratesAndBenefitsData) {
    this.ratesAndBenefitsData = ratesAndBenefitsData;
    return this;
  }

  /**
   * Get ratesAndBenefitsData
   * @return ratesAndBenefitsData
   */
  @javax.annotation.Nullable
  public CartSimulation200ResponseRatesAndBenefitsData getRatesAndBenefitsData() {
    return ratesAndBenefitsData;
  }

  public void setRatesAndBenefitsData(CartSimulation200ResponseRatesAndBenefitsData ratesAndBenefitsData) {
    this.ratesAndBenefitsData = ratesAndBenefitsData;
  }


  public CartSimulation200Response selectableGifts(List<Object> selectableGifts) {
    this.selectableGifts = selectableGifts;
    return this;
  }

  public CartSimulation200Response addSelectableGiftsItem(Object selectableGiftsItem) {
    if (this.selectableGifts == null) {
      this.selectableGifts = new ArrayList<>();
    }
    this.selectableGifts.add(selectableGiftsItem);
    return this;
  }

  /**
   * Array containing the data of the item selected as a gift.
   * @return selectableGifts
   */
  @javax.annotation.Nullable
  public List<Object> getSelectableGifts() {
    return selectableGifts;
  }

  public void setSelectableGifts(List<Object> selectableGifts) {
    this.selectableGifts = selectableGifts;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CartSimulation200Response cartSimulation200Response = (CartSimulation200Response) o;
    return Objects.equals(this.country, cartSimulation200Response.country) &&
        Objects.equals(this.items, cartSimulation200Response.items) &&
        Objects.equals(this.logisticsInfo, cartSimulation200Response.logisticsInfo) &&
        Objects.equals(this.marketingData, cartSimulation200Response.marketingData) &&
        Objects.equals(this.paymentData, cartSimulation200Response.paymentData) &&
        Objects.equals(this.postalCode, cartSimulation200Response.postalCode) &&
        Objects.equals(this.ratesAndBenefitsData, cartSimulation200Response.ratesAndBenefitsData) &&
        Objects.equals(this.selectableGifts, cartSimulation200Response.selectableGifts);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(country, items, logisticsInfo, marketingData, paymentData, postalCode, ratesAndBenefitsData, selectableGifts);
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
    sb.append("class CartSimulation200Response {\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    logisticsInfo: ").append(toIndentedString(logisticsInfo)).append("\n");
    sb.append("    marketingData: ").append(toIndentedString(marketingData)).append("\n");
    sb.append("    paymentData: ").append(toIndentedString(paymentData)).append("\n");
    sb.append("    postalCode: ").append(toIndentedString(postalCode)).append("\n");
    sb.append("    ratesAndBenefitsData: ").append(toIndentedString(ratesAndBenefitsData)).append("\n");
    sb.append("    selectableGifts: ").append(toIndentedString(selectableGifts)).append("\n");
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
    openapiFields.add("country");
    openapiFields.add("items");
    openapiFields.add("logisticsInfo");
    openapiFields.add("marketingData");
    openapiFields.add("paymentData");
    openapiFields.add("postalCode");
    openapiFields.add("ratesAndBenefitsData");
    openapiFields.add("selectableGifts");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200Response is not found in the empty JSON string", CartSimulation200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
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
            CartSimulation200ResponseItemsInner.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if (jsonObj.get("logisticsInfo") != null && !jsonObj.get("logisticsInfo").isJsonNull()) {
        JsonArray jsonArraylogisticsInfo = jsonObj.getAsJsonArray("logisticsInfo");
        if (jsonArraylogisticsInfo != null) {
          // ensure the json data is an array
          if (!jsonObj.get("logisticsInfo").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `logisticsInfo` to be an array in the JSON string but got `%s`", jsonObj.get("logisticsInfo").toString()));
          }

          // validate the optional field `logisticsInfo` (array)
          for (int i = 0; i < jsonArraylogisticsInfo.size(); i++) {
            CartSimulation200ResponseLogisticsInfoInner.validateJsonElement(jsonArraylogisticsInfo.get(i));
          };
        }
      }
      // validate the optional field `paymentData`
      if (jsonObj.get("paymentData") != null && !jsonObj.get("paymentData").isJsonNull()) {
        CartSimulation200ResponsePaymentData.validateJsonElement(jsonObj.get("paymentData"));
      }
      if ((jsonObj.get("postalCode") != null && !jsonObj.get("postalCode").isJsonNull()) && !jsonObj.get("postalCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `postalCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("postalCode").toString()));
      }
      // validate the optional field `ratesAndBenefitsData`
      if (jsonObj.get("ratesAndBenefitsData") != null && !jsonObj.get("ratesAndBenefitsData").isJsonNull()) {
        CartSimulation200ResponseRatesAndBenefitsData.validateJsonElement(jsonObj.get("ratesAndBenefitsData"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("selectableGifts") != null && !jsonObj.get("selectableGifts").isJsonNull() && !jsonObj.get("selectableGifts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `selectableGifts` to be an array in the JSON string but got `%s`", jsonObj.get("selectableGifts").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200Response>() {
           @Override
           public void write(JsonWriter out, CartSimulation200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200Response
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200Response
   */
  public static CartSimulation200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200Response.class);
  }

  /**
   * Convert an instance of CartSimulation200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

