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
import org.openapitools.client.model.PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow;

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
 * PlaceOrderRequestShippingDataLogisticsInfoInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrderRequestShippingDataLogisticsInfoInner {
  public static final String SERIALIZED_NAME_DELIVERY_WINDOW = "deliveryWindow";
  @SerializedName(SERIALIZED_NAME_DELIVERY_WINDOW)
  private PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow deliveryWindow;

  public static final String SERIALIZED_NAME_ITEM_INDEX = "itemIndex";
  @SerializedName(SERIALIZED_NAME_ITEM_INDEX)
  private Integer itemIndex = 0;

  public static final String SERIALIZED_NAME_LOCK_T_T_L = "lockTTL";
  @SerializedName(SERIALIZED_NAME_LOCK_T_T_L)
  private String lockTTL = "8d";

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Integer price = 1099;

  public static final String SERIALIZED_NAME_SELECTED_SLA = "selectedSla";
  @SerializedName(SERIALIZED_NAME_SELECTED_SLA)
  private String selectedSla = "Express";

  public static final String SERIALIZED_NAME_SHIPPING_ESTIMATE = "shippingEstimate";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ESTIMATE)
  private String shippingEstimate = "7d";

  public PlaceOrderRequestShippingDataLogisticsInfoInner() {
  }

  public PlaceOrderRequestShippingDataLogisticsInfoInner deliveryWindow(PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow deliveryWindow) {
    this.deliveryWindow = deliveryWindow;
    return this;
  }

  /**
   * Get deliveryWindow
   * @return deliveryWindow
   */
  @javax.annotation.Nullable
  public PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow getDeliveryWindow() {
    return deliveryWindow;
  }

  public void setDeliveryWindow(PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow deliveryWindow) {
    this.deliveryWindow = deliveryWindow;
  }


  public PlaceOrderRequestShippingDataLogisticsInfoInner itemIndex(Integer itemIndex) {
    this.itemIndex = itemIndex;
    return this;
  }

  /**
   * Index of the item in the &#x60;items&#x60; array, starting from 0.
   * @return itemIndex
   */
  @javax.annotation.Nonnull
  public Integer getItemIndex() {
    return itemIndex;
  }

  public void setItemIndex(Integer itemIndex) {
    this.itemIndex = itemIndex;
  }


  public PlaceOrderRequestShippingDataLogisticsInfoInner lockTTL(String lockTTL) {
    this.lockTTL = lockTTL;
    return this;
  }

  /**
   * Logistics reservation waiting time.
   * @return lockTTL
   */
  @javax.annotation.Nullable
  public String getLockTTL() {
    return lockTTL;
  }

  public void setLockTTL(String lockTTL) {
    this.lockTTL = lockTTL;
  }


  public PlaceOrderRequestShippingDataLogisticsInfoInner price(Integer price) {
    this.price = price;
    return this;
  }

  /**
   * Shipping price for the item. Does not account for the whole order&#39;s shipping price.
   * @return price
   */
  @javax.annotation.Nonnull
  public Integer getPrice() {
    return price;
  }

  public void setPrice(Integer price) {
    this.price = price;
  }


  public PlaceOrderRequestShippingDataLogisticsInfoInner selectedSla(String selectedSla) {
    this.selectedSla = selectedSla;
    return this;
  }

  /**
   * Selected shipping option
   * @return selectedSla
   */
  @javax.annotation.Nonnull
  public String getSelectedSla() {
    return selectedSla;
  }

  public void setSelectedSla(String selectedSla) {
    this.selectedSla = selectedSla;
  }


  public PlaceOrderRequestShippingDataLogisticsInfoInner shippingEstimate(String shippingEstimate) {
    this.shippingEstimate = shippingEstimate;
    return this;
  }

  /**
   * Estimated time until delivery for the item.
   * @return shippingEstimate
   */
  @javax.annotation.Nullable
  public String getShippingEstimate() {
    return shippingEstimate;
  }

  public void setShippingEstimate(String shippingEstimate) {
    this.shippingEstimate = shippingEstimate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaceOrderRequestShippingDataLogisticsInfoInner placeOrderRequestShippingDataLogisticsInfoInner = (PlaceOrderRequestShippingDataLogisticsInfoInner) o;
    return Objects.equals(this.deliveryWindow, placeOrderRequestShippingDataLogisticsInfoInner.deliveryWindow) &&
        Objects.equals(this.itemIndex, placeOrderRequestShippingDataLogisticsInfoInner.itemIndex) &&
        Objects.equals(this.lockTTL, placeOrderRequestShippingDataLogisticsInfoInner.lockTTL) &&
        Objects.equals(this.price, placeOrderRequestShippingDataLogisticsInfoInner.price) &&
        Objects.equals(this.selectedSla, placeOrderRequestShippingDataLogisticsInfoInner.selectedSla) &&
        Objects.equals(this.shippingEstimate, placeOrderRequestShippingDataLogisticsInfoInner.shippingEstimate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(deliveryWindow, itemIndex, lockTTL, price, selectedSla, shippingEstimate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrderRequestShippingDataLogisticsInfoInner {\n");
    sb.append("    deliveryWindow: ").append(toIndentedString(deliveryWindow)).append("\n");
    sb.append("    itemIndex: ").append(toIndentedString(itemIndex)).append("\n");
    sb.append("    lockTTL: ").append(toIndentedString(lockTTL)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    selectedSla: ").append(toIndentedString(selectedSla)).append("\n");
    sb.append("    shippingEstimate: ").append(toIndentedString(shippingEstimate)).append("\n");
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
    openapiFields.add("deliveryWindow");
    openapiFields.add("itemIndex");
    openapiFields.add("lockTTL");
    openapiFields.add("price");
    openapiFields.add("selectedSla");
    openapiFields.add("shippingEstimate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("itemIndex");
    openapiRequiredFields.add("price");
    openapiRequiredFields.add("selectedSla");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrderRequestShippingDataLogisticsInfoInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrderRequestShippingDataLogisticsInfoInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrderRequestShippingDataLogisticsInfoInner is not found in the empty JSON string", PlaceOrderRequestShippingDataLogisticsInfoInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrderRequestShippingDataLogisticsInfoInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrderRequestShippingDataLogisticsInfoInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PlaceOrderRequestShippingDataLogisticsInfoInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `deliveryWindow`
      if (jsonObj.get("deliveryWindow") != null && !jsonObj.get("deliveryWindow").isJsonNull()) {
        PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow.validateJsonElement(jsonObj.get("deliveryWindow"));
      }
      if ((jsonObj.get("lockTTL") != null && !jsonObj.get("lockTTL").isJsonNull()) && !jsonObj.get("lockTTL").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lockTTL` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lockTTL").toString()));
      }
      if (!jsonObj.get("selectedSla").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `selectedSla` to be a primitive type in the JSON string but got `%s`", jsonObj.get("selectedSla").toString()));
      }
      if ((jsonObj.get("shippingEstimate") != null && !jsonObj.get("shippingEstimate").isJsonNull()) && !jsonObj.get("shippingEstimate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shippingEstimate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shippingEstimate").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrderRequestShippingDataLogisticsInfoInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrderRequestShippingDataLogisticsInfoInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrderRequestShippingDataLogisticsInfoInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrderRequestShippingDataLogisticsInfoInner.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrderRequestShippingDataLogisticsInfoInner>() {
           @Override
           public void write(JsonWriter out, PlaceOrderRequestShippingDataLogisticsInfoInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrderRequestShippingDataLogisticsInfoInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrderRequestShippingDataLogisticsInfoInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrderRequestShippingDataLogisticsInfoInner
   * @throws IOException if the JSON string is invalid with respect to PlaceOrderRequestShippingDataLogisticsInfoInner
   */
  public static PlaceOrderRequestShippingDataLogisticsInfoInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrderRequestShippingDataLogisticsInfoInner.class);
  }

  /**
   * Convert an instance of PlaceOrderRequestShippingDataLogisticsInfoInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

