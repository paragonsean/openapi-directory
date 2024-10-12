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
import org.openapitools.client.model.AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner;
import org.openapitools.client.model.ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner;

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
 * ItemsUpdate200ResponseShippingDataLogisticsInfoInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ItemsUpdate200ResponseShippingDataLogisticsInfoInner {
  public static final String SERIALIZED_NAME_ADDRESS_ID = "addressId";
  @SerializedName(SERIALIZED_NAME_ADDRESS_ID)
  private String addressId;

  public static final String SERIALIZED_NAME_DELIVERY_CHANNELS = "deliveryChannels";
  @SerializedName(SERIALIZED_NAME_DELIVERY_CHANNELS)
  private List<AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner> deliveryChannels = new ArrayList<>();

  public static final String SERIALIZED_NAME_ITEM_ID = "itemId";
  @SerializedName(SERIALIZED_NAME_ITEM_ID)
  private String itemId;

  public static final String SERIALIZED_NAME_ITEM_INDEX = "itemIndex";
  @SerializedName(SERIALIZED_NAME_ITEM_INDEX)
  private Integer itemIndex;

  public static final String SERIALIZED_NAME_SELECTED_DELIVERY_CHANNEL = "selectedDeliveryChannel";
  @SerializedName(SERIALIZED_NAME_SELECTED_DELIVERY_CHANNEL)
  private String selectedDeliveryChannel;

  public static final String SERIALIZED_NAME_SELECTED_SLA = "selectedSla";
  @SerializedName(SERIALIZED_NAME_SELECTED_SLA)
  private String selectedSla;

  public static final String SERIALIZED_NAME_SHIPS_TO = "shipsTo";
  @SerializedName(SERIALIZED_NAME_SHIPS_TO)
  private List<String> shipsTo = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLAS = "slas";
  @SerializedName(SERIALIZED_NAME_SLAS)
  private List<ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner> slas = new ArrayList<>();

  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner() {
  }

  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner addressId(String addressId) {
    this.addressId = addressId;
    return this;
  }

  /**
   * Address ID.
   * @return addressId
   */
  @javax.annotation.Nullable
  public String getAddressId() {
    return addressId;
  }

  public void setAddressId(String addressId) {
    this.addressId = addressId;
  }


  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner deliveryChannels(List<AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner> deliveryChannels) {
    this.deliveryChannels = deliveryChannels;
    return this;
  }

  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner addDeliveryChannelsItem(AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner deliveryChannelsItem) {
    if (this.deliveryChannels == null) {
      this.deliveryChannels = new ArrayList<>();
    }
    this.deliveryChannels.add(deliveryChannelsItem);
    return this;
  }

  /**
   * List of available delivery channels.
   * @return deliveryChannels
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner> getDeliveryChannels() {
    return deliveryChannels;
  }

  public void setDeliveryChannels(List<AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner> deliveryChannels) {
    this.deliveryChannels = deliveryChannels;
  }


  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner itemId(String itemId) {
    this.itemId = itemId;
    return this;
  }

  /**
   * Item ID.
   * @return itemId
   */
  @javax.annotation.Nullable
  public String getItemId() {
    return itemId;
  }

  public void setItemId(String itemId) {
    this.itemId = itemId;
  }


  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner itemIndex(Integer itemIndex) {
    this.itemIndex = itemIndex;
    return this;
  }

  /**
   * Index corresponding to the position of the object in the &#x60;items&#x60; array.
   * @return itemIndex
   */
  @javax.annotation.Nullable
  public Integer getItemIndex() {
    return itemIndex;
  }

  public void setItemIndex(Integer itemIndex) {
    this.itemIndex = itemIndex;
  }


  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner selectedDeliveryChannel(String selectedDeliveryChannel) {
    this.selectedDeliveryChannel = selectedDeliveryChannel;
    return this;
  }

  /**
   * Delivery channel selected by the customer.
   * @return selectedDeliveryChannel
   */
  @javax.annotation.Nullable
  public String getSelectedDeliveryChannel() {
    return selectedDeliveryChannel;
  }

  public void setSelectedDeliveryChannel(String selectedDeliveryChannel) {
    this.selectedDeliveryChannel = selectedDeliveryChannel;
  }


  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner selectedSla(String selectedSla) {
    this.selectedSla = selectedSla;
    return this;
  }

  /**
   * SLA selected by the customer.
   * @return selectedSla
   */
  @javax.annotation.Nullable
  public String getSelectedSla() {
    return selectedSla;
  }

  public void setSelectedSla(String selectedSla) {
    this.selectedSla = selectedSla;
  }


  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner shipsTo(List<String> shipsTo) {
    this.shipsTo = shipsTo;
    return this;
  }

  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner addShipsToItem(String shipsToItem) {
    if (this.shipsTo == null) {
      this.shipsTo = new ArrayList<>();
    }
    this.shipsTo.add(shipsToItem);
    return this;
  }

  /**
   * List of countries that the item may be shipped to.
   * @return shipsTo
   */
  @javax.annotation.Nullable
  public List<String> getShipsTo() {
    return shipsTo;
  }

  public void setShipsTo(List<String> shipsTo) {
    this.shipsTo = shipsTo;
  }


  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner slas(List<ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner> slas) {
    this.slas = slas;
    return this;
  }

  public ItemsUpdate200ResponseShippingDataLogisticsInfoInner addSlasItem(ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner slasItem) {
    if (this.slas == null) {
      this.slas = new ArrayList<>();
    }
    this.slas.add(slasItem);
    return this;
  }

  /**
   * Information on available SLAs.
   * @return slas
   */
  @javax.annotation.Nullable
  public List<ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner> getSlas() {
    return slas;
  }

  public void setSlas(List<ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner> slas) {
    this.slas = slas;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ItemsUpdate200ResponseShippingDataLogisticsInfoInner itemsUpdate200ResponseShippingDataLogisticsInfoInner = (ItemsUpdate200ResponseShippingDataLogisticsInfoInner) o;
    return Objects.equals(this.addressId, itemsUpdate200ResponseShippingDataLogisticsInfoInner.addressId) &&
        Objects.equals(this.deliveryChannels, itemsUpdate200ResponseShippingDataLogisticsInfoInner.deliveryChannels) &&
        Objects.equals(this.itemId, itemsUpdate200ResponseShippingDataLogisticsInfoInner.itemId) &&
        Objects.equals(this.itemIndex, itemsUpdate200ResponseShippingDataLogisticsInfoInner.itemIndex) &&
        Objects.equals(this.selectedDeliveryChannel, itemsUpdate200ResponseShippingDataLogisticsInfoInner.selectedDeliveryChannel) &&
        Objects.equals(this.selectedSla, itemsUpdate200ResponseShippingDataLogisticsInfoInner.selectedSla) &&
        Objects.equals(this.shipsTo, itemsUpdate200ResponseShippingDataLogisticsInfoInner.shipsTo) &&
        Objects.equals(this.slas, itemsUpdate200ResponseShippingDataLogisticsInfoInner.slas);
  }

  @Override
  public int hashCode() {
    return Objects.hash(addressId, deliveryChannels, itemId, itemIndex, selectedDeliveryChannel, selectedSla, shipsTo, slas);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ItemsUpdate200ResponseShippingDataLogisticsInfoInner {\n");
    sb.append("    addressId: ").append(toIndentedString(addressId)).append("\n");
    sb.append("    deliveryChannels: ").append(toIndentedString(deliveryChannels)).append("\n");
    sb.append("    itemId: ").append(toIndentedString(itemId)).append("\n");
    sb.append("    itemIndex: ").append(toIndentedString(itemIndex)).append("\n");
    sb.append("    selectedDeliveryChannel: ").append(toIndentedString(selectedDeliveryChannel)).append("\n");
    sb.append("    selectedSla: ").append(toIndentedString(selectedSla)).append("\n");
    sb.append("    shipsTo: ").append(toIndentedString(shipsTo)).append("\n");
    sb.append("    slas: ").append(toIndentedString(slas)).append("\n");
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
    openapiFields.add("addressId");
    openapiFields.add("deliveryChannels");
    openapiFields.add("itemId");
    openapiFields.add("itemIndex");
    openapiFields.add("selectedDeliveryChannel");
    openapiFields.add("selectedSla");
    openapiFields.add("shipsTo");
    openapiFields.add("slas");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ItemsUpdate200ResponseShippingDataLogisticsInfoInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ItemsUpdate200ResponseShippingDataLogisticsInfoInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ItemsUpdate200ResponseShippingDataLogisticsInfoInner is not found in the empty JSON string", ItemsUpdate200ResponseShippingDataLogisticsInfoInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ItemsUpdate200ResponseShippingDataLogisticsInfoInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ItemsUpdate200ResponseShippingDataLogisticsInfoInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("addressId") != null && !jsonObj.get("addressId").isJsonNull()) && !jsonObj.get("addressId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `addressId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("addressId").toString()));
      }
      if (jsonObj.get("deliveryChannels") != null && !jsonObj.get("deliveryChannels").isJsonNull()) {
        JsonArray jsonArraydeliveryChannels = jsonObj.getAsJsonArray("deliveryChannels");
        if (jsonArraydeliveryChannels != null) {
          // ensure the json data is an array
          if (!jsonObj.get("deliveryChannels").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `deliveryChannels` to be an array in the JSON string but got `%s`", jsonObj.get("deliveryChannels").toString()));
          }

          // validate the optional field `deliveryChannels` (array)
          for (int i = 0; i < jsonArraydeliveryChannels.size(); i++) {
            AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner.validateJsonElement(jsonArraydeliveryChannels.get(i));
          };
        }
      }
      if ((jsonObj.get("itemId") != null && !jsonObj.get("itemId").isJsonNull()) && !jsonObj.get("itemId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `itemId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("itemId").toString()));
      }
      if ((jsonObj.get("selectedDeliveryChannel") != null && !jsonObj.get("selectedDeliveryChannel").isJsonNull()) && !jsonObj.get("selectedDeliveryChannel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `selectedDeliveryChannel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("selectedDeliveryChannel").toString()));
      }
      if ((jsonObj.get("selectedSla") != null && !jsonObj.get("selectedSla").isJsonNull()) && !jsonObj.get("selectedSla").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `selectedSla` to be a primitive type in the JSON string but got `%s`", jsonObj.get("selectedSla").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("shipsTo") != null && !jsonObj.get("shipsTo").isJsonNull() && !jsonObj.get("shipsTo").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipsTo` to be an array in the JSON string but got `%s`", jsonObj.get("shipsTo").toString()));
      }
      if (jsonObj.get("slas") != null && !jsonObj.get("slas").isJsonNull()) {
        JsonArray jsonArrayslas = jsonObj.getAsJsonArray("slas");
        if (jsonArrayslas != null) {
          // ensure the json data is an array
          if (!jsonObj.get("slas").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `slas` to be an array in the JSON string but got `%s`", jsonObj.get("slas").toString()));
          }

          // validate the optional field `slas` (array)
          for (int i = 0; i < jsonArrayslas.size(); i++) {
            ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner.validateJsonElement(jsonArrayslas.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ItemsUpdate200ResponseShippingDataLogisticsInfoInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ItemsUpdate200ResponseShippingDataLogisticsInfoInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ItemsUpdate200ResponseShippingDataLogisticsInfoInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ItemsUpdate200ResponseShippingDataLogisticsInfoInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ItemsUpdate200ResponseShippingDataLogisticsInfoInner>() {
           @Override
           public void write(JsonWriter out, ItemsUpdate200ResponseShippingDataLogisticsInfoInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ItemsUpdate200ResponseShippingDataLogisticsInfoInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ItemsUpdate200ResponseShippingDataLogisticsInfoInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ItemsUpdate200ResponseShippingDataLogisticsInfoInner
   * @throws IOException if the JSON string is invalid with respect to ItemsUpdate200ResponseShippingDataLogisticsInfoInner
   */
  public static ItemsUpdate200ResponseShippingDataLogisticsInfoInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ItemsUpdate200ResponseShippingDataLogisticsInfoInner.class);
  }

  /**
   * Convert an instance of ItemsUpdate200ResponseShippingDataLogisticsInfoInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

