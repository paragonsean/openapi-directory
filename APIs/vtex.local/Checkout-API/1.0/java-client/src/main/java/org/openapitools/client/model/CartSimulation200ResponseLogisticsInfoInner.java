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
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerItemMetadata;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerTotalsInner;
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
 * CartSimulation200ResponseLogisticsInfoInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200ResponseLogisticsInfoInner {
  public static final String SERIALIZED_NAME_ADDRESS_ID = "addressId";
  @SerializedName(SERIALIZED_NAME_ADDRESS_ID)
  private String addressId;

  public static final String SERIALIZED_NAME_DELIVERY_CHANNELS = "deliveryChannels";
  @SerializedName(SERIALIZED_NAME_DELIVERY_CHANNELS)
  private List<AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner> deliveryChannels = new ArrayList<>();

  public static final String SERIALIZED_NAME_ITEM_INDEX = "itemIndex";
  @SerializedName(SERIALIZED_NAME_ITEM_INDEX)
  private Integer itemIndex;

  public static final String SERIALIZED_NAME_ITEM_METADATA = "itemMetadata";
  @SerializedName(SERIALIZED_NAME_ITEM_METADATA)
  private CartSimulation200ResponseLogisticsInfoInnerItemMetadata itemMetadata;

  public static final String SERIALIZED_NAME_MESSAGES = "messages";
  @SerializedName(SERIALIZED_NAME_MESSAGES)
  private List<Object> messages = new ArrayList<>();

  public static final String SERIALIZED_NAME_PICKUP_POINTS = "pickupPoints";
  @SerializedName(SERIALIZED_NAME_PICKUP_POINTS)
  private List<Object> pickupPoints = new ArrayList<>();

  public static final String SERIALIZED_NAME_PURCHASE_CONDITIONS = "purchaseConditions";
  @SerializedName(SERIALIZED_NAME_PURCHASE_CONDITIONS)
  private CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions purchaseConditions;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Integer quantity;

  public static final String SERIALIZED_NAME_SELECTED_DELIVERY_CHANNEL = "selectedDeliveryChannel";
  @SerializedName(SERIALIZED_NAME_SELECTED_DELIVERY_CHANNEL)
  private String selectedDeliveryChannel;

  public static final String SERIALIZED_NAME_SELECTED_SLA = "selectedSla";
  @SerializedName(SERIALIZED_NAME_SELECTED_SLA)
  private String selectedSla;

  public static final String SERIALIZED_NAME_SHIPS_TO = "shipsTo";
  @SerializedName(SERIALIZED_NAME_SHIPS_TO)
  private List<Object> shipsTo = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLAS = "slas";
  @SerializedName(SERIALIZED_NAME_SLAS)
  private List<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner> slas = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUBSCRIPTION_DATA = "subscriptionData";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTION_DATA)
  private Object subscriptionData;

  public static final String SERIALIZED_NAME_TOTALS = "totals";
  @SerializedName(SERIALIZED_NAME_TOTALS)
  private List<CartSimulation200ResponseLogisticsInfoInnerTotalsInner> totals = new ArrayList<>();

  public CartSimulation200ResponseLogisticsInfoInner() {
  }

  public CartSimulation200ResponseLogisticsInfoInner addressId(String addressId) {
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


  public CartSimulation200ResponseLogisticsInfoInner deliveryChannels(List<AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner> deliveryChannels) {
    this.deliveryChannels = deliveryChannels;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInner addDeliveryChannelsItem(AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner deliveryChannelsItem) {
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


  public CartSimulation200ResponseLogisticsInfoInner itemIndex(Integer itemIndex) {
    this.itemIndex = itemIndex;
    return this;
  }

  /**
   * Index of item in items array.
   * @return itemIndex
   */
  @javax.annotation.Nullable
  public Integer getItemIndex() {
    return itemIndex;
  }

  public void setItemIndex(Integer itemIndex) {
    this.itemIndex = itemIndex;
  }


  public CartSimulation200ResponseLogisticsInfoInner itemMetadata(CartSimulation200ResponseLogisticsInfoInnerItemMetadata itemMetadata) {
    this.itemMetadata = itemMetadata;
    return this;
  }

  /**
   * Get itemMetadata
   * @return itemMetadata
   */
  @javax.annotation.Nullable
  public CartSimulation200ResponseLogisticsInfoInnerItemMetadata getItemMetadata() {
    return itemMetadata;
  }

  public void setItemMetadata(CartSimulation200ResponseLogisticsInfoInnerItemMetadata itemMetadata) {
    this.itemMetadata = itemMetadata;
  }


  public CartSimulation200ResponseLogisticsInfoInner messages(List<Object> messages) {
    this.messages = messages;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInner addMessagesItem(Object messagesItem) {
    if (this.messages == null) {
      this.messages = new ArrayList<>();
    }
    this.messages.add(messagesItem);
    return this;
  }

  /**
   * Array containing an object for each message generated by our servers while processing the request.
   * @return messages
   */
  @javax.annotation.Nullable
  public List<Object> getMessages() {
    return messages;
  }

  public void setMessages(List<Object> messages) {
    this.messages = messages;
  }


  public CartSimulation200ResponseLogisticsInfoInner pickupPoints(List<Object> pickupPoints) {
    this.pickupPoints = pickupPoints;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInner addPickupPointsItem(Object pickupPointsItem) {
    if (this.pickupPoints == null) {
      this.pickupPoints = new ArrayList<>();
    }
    this.pickupPoints.add(pickupPointsItem);
    return this;
  }

  /**
   * Array containing pickup points information.
   * @return pickupPoints
   */
  @javax.annotation.Nullable
  public List<Object> getPickupPoints() {
    return pickupPoints;
  }

  public void setPickupPoints(List<Object> pickupPoints) {
    this.pickupPoints = pickupPoints;
  }


  public CartSimulation200ResponseLogisticsInfoInner purchaseConditions(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions purchaseConditions) {
    this.purchaseConditions = purchaseConditions;
    return this;
  }

  /**
   * Get purchaseConditions
   * @return purchaseConditions
   */
  @javax.annotation.Nullable
  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions getPurchaseConditions() {
    return purchaseConditions;
  }

  public void setPurchaseConditions(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions purchaseConditions) {
    this.purchaseConditions = purchaseConditions;
  }


  public CartSimulation200ResponseLogisticsInfoInner quantity(Integer quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * Quantity.
   * @return quantity
   */
  @javax.annotation.Nullable
  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }


  public CartSimulation200ResponseLogisticsInfoInner selectedDeliveryChannel(String selectedDeliveryChannel) {
    this.selectedDeliveryChannel = selectedDeliveryChannel;
    return this;
  }

  /**
   * Delivery channel selected by the customer. For example, &#x60;\&quot;delivery\&quot;&#x60; or &#x60;\&quot;pickup-in-point\&quot;&#x60;.
   * @return selectedDeliveryChannel
   */
  @javax.annotation.Nullable
  public String getSelectedDeliveryChannel() {
    return selectedDeliveryChannel;
  }

  public void setSelectedDeliveryChannel(String selectedDeliveryChannel) {
    this.selectedDeliveryChannel = selectedDeliveryChannel;
  }


  public CartSimulation200ResponseLogisticsInfoInner selectedSla(String selectedSla) {
    this.selectedSla = selectedSla;
    return this;
  }

  /**
   * Selected SLA. For example, &#x60;\&quot;normal\&quot;&#x60; or &#x60;\&quot;express\&quot;&#x60;.
   * @return selectedSla
   */
  @javax.annotation.Nullable
  public String getSelectedSla() {
    return selectedSla;
  }

  public void setSelectedSla(String selectedSla) {
    this.selectedSla = selectedSla;
  }


  public CartSimulation200ResponseLogisticsInfoInner shipsTo(List<Object> shipsTo) {
    this.shipsTo = shipsTo;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInner addShipsToItem(Object shipsToItem) {
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
  public List<Object> getShipsTo() {
    return shipsTo;
  }

  public void setShipsTo(List<Object> shipsTo) {
    this.shipsTo = shipsTo;
  }


  public CartSimulation200ResponseLogisticsInfoInner slas(List<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner> slas) {
    this.slas = slas;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInner addSlasItem(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner slasItem) {
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
  public List<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner> getSlas() {
    return slas;
  }

  public void setSlas(List<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner> slas) {
    this.slas = slas;
  }


  public CartSimulation200ResponseLogisticsInfoInner subscriptionData(Object subscriptionData) {
    this.subscriptionData = subscriptionData;
    return this;
  }

  /**
   * Subscription information.
   * @return subscriptionData
   */
  @javax.annotation.Nullable
  public Object getSubscriptionData() {
    return subscriptionData;
  }

  public void setSubscriptionData(Object subscriptionData) {
    this.subscriptionData = subscriptionData;
  }


  public CartSimulation200ResponseLogisticsInfoInner totals(List<CartSimulation200ResponseLogisticsInfoInnerTotalsInner> totals) {
    this.totals = totals;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInner addTotalsItem(CartSimulation200ResponseLogisticsInfoInnerTotalsInner totalsItem) {
    if (this.totals == null) {
      this.totals = new ArrayList<>();
    }
    this.totals.add(totalsItem);
    return this;
  }

  /**
   * Information on order totals.
   * @return totals
   */
  @javax.annotation.Nullable
  public List<CartSimulation200ResponseLogisticsInfoInnerTotalsInner> getTotals() {
    return totals;
  }

  public void setTotals(List<CartSimulation200ResponseLogisticsInfoInnerTotalsInner> totals) {
    this.totals = totals;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CartSimulation200ResponseLogisticsInfoInner cartSimulation200ResponseLogisticsInfoInner = (CartSimulation200ResponseLogisticsInfoInner) o;
    return Objects.equals(this.addressId, cartSimulation200ResponseLogisticsInfoInner.addressId) &&
        Objects.equals(this.deliveryChannels, cartSimulation200ResponseLogisticsInfoInner.deliveryChannels) &&
        Objects.equals(this.itemIndex, cartSimulation200ResponseLogisticsInfoInner.itemIndex) &&
        Objects.equals(this.itemMetadata, cartSimulation200ResponseLogisticsInfoInner.itemMetadata) &&
        Objects.equals(this.messages, cartSimulation200ResponseLogisticsInfoInner.messages) &&
        Objects.equals(this.pickupPoints, cartSimulation200ResponseLogisticsInfoInner.pickupPoints) &&
        Objects.equals(this.purchaseConditions, cartSimulation200ResponseLogisticsInfoInner.purchaseConditions) &&
        Objects.equals(this.quantity, cartSimulation200ResponseLogisticsInfoInner.quantity) &&
        Objects.equals(this.selectedDeliveryChannel, cartSimulation200ResponseLogisticsInfoInner.selectedDeliveryChannel) &&
        Objects.equals(this.selectedSla, cartSimulation200ResponseLogisticsInfoInner.selectedSla) &&
        Objects.equals(this.shipsTo, cartSimulation200ResponseLogisticsInfoInner.shipsTo) &&
        Objects.equals(this.slas, cartSimulation200ResponseLogisticsInfoInner.slas) &&
        Objects.equals(this.subscriptionData, cartSimulation200ResponseLogisticsInfoInner.subscriptionData) &&
        Objects.equals(this.totals, cartSimulation200ResponseLogisticsInfoInner.totals);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(addressId, deliveryChannels, itemIndex, itemMetadata, messages, pickupPoints, purchaseConditions, quantity, selectedDeliveryChannel, selectedSla, shipsTo, slas, subscriptionData, totals);
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
    sb.append("class CartSimulation200ResponseLogisticsInfoInner {\n");
    sb.append("    addressId: ").append(toIndentedString(addressId)).append("\n");
    sb.append("    deliveryChannels: ").append(toIndentedString(deliveryChannels)).append("\n");
    sb.append("    itemIndex: ").append(toIndentedString(itemIndex)).append("\n");
    sb.append("    itemMetadata: ").append(toIndentedString(itemMetadata)).append("\n");
    sb.append("    messages: ").append(toIndentedString(messages)).append("\n");
    sb.append("    pickupPoints: ").append(toIndentedString(pickupPoints)).append("\n");
    sb.append("    purchaseConditions: ").append(toIndentedString(purchaseConditions)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    selectedDeliveryChannel: ").append(toIndentedString(selectedDeliveryChannel)).append("\n");
    sb.append("    selectedSla: ").append(toIndentedString(selectedSla)).append("\n");
    sb.append("    shipsTo: ").append(toIndentedString(shipsTo)).append("\n");
    sb.append("    slas: ").append(toIndentedString(slas)).append("\n");
    sb.append("    subscriptionData: ").append(toIndentedString(subscriptionData)).append("\n");
    sb.append("    totals: ").append(toIndentedString(totals)).append("\n");
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
    openapiFields.add("itemIndex");
    openapiFields.add("itemMetadata");
    openapiFields.add("messages");
    openapiFields.add("pickupPoints");
    openapiFields.add("purchaseConditions");
    openapiFields.add("quantity");
    openapiFields.add("selectedDeliveryChannel");
    openapiFields.add("selectedSla");
    openapiFields.add("shipsTo");
    openapiFields.add("slas");
    openapiFields.add("subscriptionData");
    openapiFields.add("totals");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200ResponseLogisticsInfoInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200ResponseLogisticsInfoInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200ResponseLogisticsInfoInner is not found in the empty JSON string", CartSimulation200ResponseLogisticsInfoInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200ResponseLogisticsInfoInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200ResponseLogisticsInfoInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      // validate the optional field `itemMetadata`
      if (jsonObj.get("itemMetadata") != null && !jsonObj.get("itemMetadata").isJsonNull()) {
        CartSimulation200ResponseLogisticsInfoInnerItemMetadata.validateJsonElement(jsonObj.get("itemMetadata"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("messages") != null && !jsonObj.get("messages").isJsonNull() && !jsonObj.get("messages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `messages` to be an array in the JSON string but got `%s`", jsonObj.get("messages").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("pickupPoints") != null && !jsonObj.get("pickupPoints").isJsonNull() && !jsonObj.get("pickupPoints").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `pickupPoints` to be an array in the JSON string but got `%s`", jsonObj.get("pickupPoints").toString()));
      }
      // validate the optional field `purchaseConditions`
      if (jsonObj.get("purchaseConditions") != null && !jsonObj.get("purchaseConditions").isJsonNull()) {
        CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions.validateJsonElement(jsonObj.get("purchaseConditions"));
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
            CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.validateJsonElement(jsonArrayslas.get(i));
          };
        }
      }
      if (jsonObj.get("totals") != null && !jsonObj.get("totals").isJsonNull()) {
        JsonArray jsonArraytotals = jsonObj.getAsJsonArray("totals");
        if (jsonArraytotals != null) {
          // ensure the json data is an array
          if (!jsonObj.get("totals").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `totals` to be an array in the JSON string but got `%s`", jsonObj.get("totals").toString()));
          }

          // validate the optional field `totals` (array)
          for (int i = 0; i < jsonArraytotals.size(); i++) {
            CartSimulation200ResponseLogisticsInfoInnerTotalsInner.validateJsonElement(jsonArraytotals.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200ResponseLogisticsInfoInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200ResponseLogisticsInfoInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200ResponseLogisticsInfoInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200ResponseLogisticsInfoInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200ResponseLogisticsInfoInner>() {
           @Override
           public void write(JsonWriter out, CartSimulation200ResponseLogisticsInfoInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200ResponseLogisticsInfoInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200ResponseLogisticsInfoInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200ResponseLogisticsInfoInner
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200ResponseLogisticsInfoInner
   */
  public static CartSimulation200ResponseLogisticsInfoInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200ResponseLogisticsInfoInner.class);
  }

  /**
   * Convert an instance of CartSimulation200ResponseLogisticsInfoInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

