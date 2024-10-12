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
import org.openapitools.client.model.AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo;
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
 * CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner {
  public static final String SERIALIZED_NAME_AVAILABLE_DELIVERY_WINDOWS = "availableDeliveryWindows";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_DELIVERY_WINDOWS)
  private CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows availableDeliveryWindows;

  public static final String SERIALIZED_NAME_DELIVERY_CHANNEL = "deliveryChannel";
  @SerializedName(SERIALIZED_NAME_DELIVERY_CHANNEL)
  private String deliveryChannel;

  public static final String SERIALIZED_NAME_DELIVERY_IDS = "deliveryIds";
  @SerializedName(SERIALIZED_NAME_DELIVERY_IDS)
  private List<AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner> deliveryIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_DELIVERY_WINDOW = "deliveryWindow";
  @SerializedName(SERIALIZED_NAME_DELIVERY_WINDOW)
  private CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow deliveryWindow;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LIST_PRICE = "listPrice";
  @SerializedName(SERIALIZED_NAME_LIST_PRICE)
  private Integer listPrice;

  public static final String SERIALIZED_NAME_LOCK_T_T_L = "lockTTL";
  @SerializedName(SERIALIZED_NAME_LOCK_T_T_L)
  private String lockTTL;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PICKUP_DISTANCE = "pickupDistance";
  @SerializedName(SERIALIZED_NAME_PICKUP_DISTANCE)
  private Integer pickupDistance;

  public static final String SERIALIZED_NAME_PICKUP_POINT_ID = "pickupPointId";
  @SerializedName(SERIALIZED_NAME_PICKUP_POINT_ID)
  private String pickupPointId;

  public static final String SERIALIZED_NAME_PICKUP_STORE_INFO = "pickupStoreInfo";
  @SerializedName(SERIALIZED_NAME_PICKUP_STORE_INFO)
  private CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo pickupStoreInfo;

  public static final String SERIALIZED_NAME_POLYGON_NAME = "polygonName";
  @SerializedName(SERIALIZED_NAME_POLYGON_NAME)
  private String polygonName;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Integer price;

  public static final String SERIALIZED_NAME_SHIPPING_ESTIMATE = "shippingEstimate";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ESTIMATE)
  private String shippingEstimate;

  public static final String SERIALIZED_NAME_SHIPPING_ESTIMATE_DATE = "shippingEstimateDate";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ESTIMATE_DATE)
  private String shippingEstimateDate;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private Integer tax;

  public static final String SERIALIZED_NAME_TRANSIT_TIME = "transitTime";
  @SerializedName(SERIALIZED_NAME_TRANSIT_TIME)
  private String transitTime;

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner() {
  }

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner availableDeliveryWindows(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows availableDeliveryWindows) {
    this.availableDeliveryWindows = availableDeliveryWindows;
    return this;
  }

  /**
   * Get availableDeliveryWindows
   * @return availableDeliveryWindows
   */
  @javax.annotation.Nullable
  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows getAvailableDeliveryWindows() {
    return availableDeliveryWindows;
  }

  public void setAvailableDeliveryWindows(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows availableDeliveryWindows) {
    this.availableDeliveryWindows = availableDeliveryWindows;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner deliveryChannel(String deliveryChannel) {
    this.deliveryChannel = deliveryChannel;
    return this;
  }

  /**
   * Delivery channel.
   * @return deliveryChannel
   */
  @javax.annotation.Nullable
  public String getDeliveryChannel() {
    return deliveryChannel;
  }

  public void setDeliveryChannel(String deliveryChannel) {
    this.deliveryChannel = deliveryChannel;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner deliveryIds(List<AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner> deliveryIds) {
    this.deliveryIds = deliveryIds;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner addDeliveryIdsItem(AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner deliveryIdsItem) {
    if (this.deliveryIds == null) {
      this.deliveryIds = new ArrayList<>();
    }
    this.deliveryIds.add(deliveryIdsItem);
    return this;
  }

  /**
   * Information on each delivery ID.
   * @return deliveryIds
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner> getDeliveryIds() {
    return deliveryIds;
  }

  public void setDeliveryIds(List<AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner> deliveryIds) {
    this.deliveryIds = deliveryIds;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner deliveryWindow(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow deliveryWindow) {
    this.deliveryWindow = deliveryWindow;
    return this;
  }

  /**
   * Get deliveryWindow
   * @return deliveryWindow
   */
  @javax.annotation.Nullable
  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow getDeliveryWindow() {
    return deliveryWindow;
  }

  public void setDeliveryWindow(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow deliveryWindow) {
    this.deliveryWindow = deliveryWindow;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * SLA ID.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner listPrice(Integer listPrice) {
    this.listPrice = listPrice;
    return this;
  }

  /**
   * List price in cents.
   * @return listPrice
   */
  @javax.annotation.Nullable
  public Integer getListPrice() {
    return listPrice;
  }

  public void setListPrice(Integer listPrice) {
    this.listPrice = listPrice;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner lockTTL(String lockTTL) {
    this.lockTTL = lockTTL;
    return this;
  }

  /**
   * Estimate date of delivery.
   * @return lockTTL
   */
  @javax.annotation.Nullable
  public String getLockTTL() {
    return lockTTL;
  }

  public void setLockTTL(String lockTTL) {
    this.lockTTL = lockTTL;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * SLA name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner pickupDistance(Integer pickupDistance) {
    this.pickupDistance = pickupDistance;
    return this;
  }

  /**
   * Pickup point distance.
   * @return pickupDistance
   */
  @javax.annotation.Nullable
  public Integer getPickupDistance() {
    return pickupDistance;
  }

  public void setPickupDistance(Integer pickupDistance) {
    this.pickupDistance = pickupDistance;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner pickupPointId(String pickupPointId) {
    this.pickupPointId = pickupPointId;
    return this;
  }

  /**
   * Pickup point ID.
   * @return pickupPointId
   */
  @javax.annotation.Nullable
  public String getPickupPointId() {
    return pickupPointId;
  }

  public void setPickupPointId(String pickupPointId) {
    this.pickupPointId = pickupPointId;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner pickupStoreInfo(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo pickupStoreInfo) {
    this.pickupStoreInfo = pickupStoreInfo;
    return this;
  }

  /**
   * Get pickupStoreInfo
   * @return pickupStoreInfo
   */
  @javax.annotation.Nullable
  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo getPickupStoreInfo() {
    return pickupStoreInfo;
  }

  public void setPickupStoreInfo(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo pickupStoreInfo) {
    this.pickupStoreInfo = pickupStoreInfo;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner polygonName(String polygonName) {
    this.polygonName = polygonName;
    return this;
  }

  /**
   * Polygon name.
   * @return polygonName
   */
  @javax.annotation.Nullable
  public String getPolygonName() {
    return polygonName;
  }

  public void setPolygonName(String polygonName) {
    this.polygonName = polygonName;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner price(Integer price) {
    this.price = price;
    return this;
  }

  /**
   * Price in cents.
   * @return price
   */
  @javax.annotation.Nullable
  public Integer getPrice() {
    return price;
  }

  public void setPrice(Integer price) {
    this.price = price;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner shippingEstimate(String shippingEstimate) {
    this.shippingEstimate = shippingEstimate;
    return this;
  }

  /**
   * Shipping estimate. For instance, \&quot;three business days\&quot; will be represented as &#x60;3bd&#x60;.
   * @return shippingEstimate
   */
  @javax.annotation.Nullable
  public String getShippingEstimate() {
    return shippingEstimate;
  }

  public void setShippingEstimate(String shippingEstimate) {
    this.shippingEstimate = shippingEstimate;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner shippingEstimateDate(String shippingEstimateDate) {
    this.shippingEstimateDate = shippingEstimateDate;
    return this;
  }

  /**
   * Shipping estimate date.
   * @return shippingEstimateDate
   */
  @javax.annotation.Nullable
  public String getShippingEstimateDate() {
    return shippingEstimateDate;
  }

  public void setShippingEstimateDate(String shippingEstimateDate) {
    this.shippingEstimateDate = shippingEstimateDate;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner tax(Integer tax) {
    this.tax = tax;
    return this;
  }

  /**
   * Tax in cents.
   * @return tax
   */
  @javax.annotation.Nullable
  public Integer getTax() {
    return tax;
  }

  public void setTax(Integer tax) {
    this.tax = tax;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner transitTime(String transitTime) {
    this.transitTime = transitTime;
    return this;
  }

  /**
   * Transit time. For instance, \&quot;three business days\&quot; is represented as &#x60;3bd&#x60;.
   * @return transitTime
   */
  @javax.annotation.Nullable
  public String getTransitTime() {
    return transitTime;
  }

  public void setTransitTime(String transitTime) {
    this.transitTime = transitTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner = (CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner) o;
    return Objects.equals(this.availableDeliveryWindows, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.availableDeliveryWindows) &&
        Objects.equals(this.deliveryChannel, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.deliveryChannel) &&
        Objects.equals(this.deliveryIds, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.deliveryIds) &&
        Objects.equals(this.deliveryWindow, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.deliveryWindow) &&
        Objects.equals(this.id, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.id) &&
        Objects.equals(this.listPrice, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.listPrice) &&
        Objects.equals(this.lockTTL, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.lockTTL) &&
        Objects.equals(this.name, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.name) &&
        Objects.equals(this.pickupDistance, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.pickupDistance) &&
        Objects.equals(this.pickupPointId, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.pickupPointId) &&
        Objects.equals(this.pickupStoreInfo, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.pickupStoreInfo) &&
        Objects.equals(this.polygonName, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.polygonName) &&
        Objects.equals(this.price, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.price) &&
        Objects.equals(this.shippingEstimate, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.shippingEstimate) &&
        Objects.equals(this.shippingEstimateDate, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.shippingEstimateDate) &&
        Objects.equals(this.tax, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.tax) &&
        Objects.equals(this.transitTime, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.transitTime);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(availableDeliveryWindows, deliveryChannel, deliveryIds, deliveryWindow, id, listPrice, lockTTL, name, pickupDistance, pickupPointId, pickupStoreInfo, polygonName, price, shippingEstimate, shippingEstimateDate, tax, transitTime);
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
    sb.append("class CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner {\n");
    sb.append("    availableDeliveryWindows: ").append(toIndentedString(availableDeliveryWindows)).append("\n");
    sb.append("    deliveryChannel: ").append(toIndentedString(deliveryChannel)).append("\n");
    sb.append("    deliveryIds: ").append(toIndentedString(deliveryIds)).append("\n");
    sb.append("    deliveryWindow: ").append(toIndentedString(deliveryWindow)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    listPrice: ").append(toIndentedString(listPrice)).append("\n");
    sb.append("    lockTTL: ").append(toIndentedString(lockTTL)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    pickupDistance: ").append(toIndentedString(pickupDistance)).append("\n");
    sb.append("    pickupPointId: ").append(toIndentedString(pickupPointId)).append("\n");
    sb.append("    pickupStoreInfo: ").append(toIndentedString(pickupStoreInfo)).append("\n");
    sb.append("    polygonName: ").append(toIndentedString(polygonName)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    shippingEstimate: ").append(toIndentedString(shippingEstimate)).append("\n");
    sb.append("    shippingEstimateDate: ").append(toIndentedString(shippingEstimateDate)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    transitTime: ").append(toIndentedString(transitTime)).append("\n");
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
    openapiFields.add("availableDeliveryWindows");
    openapiFields.add("deliveryChannel");
    openapiFields.add("deliveryIds");
    openapiFields.add("deliveryWindow");
    openapiFields.add("id");
    openapiFields.add("listPrice");
    openapiFields.add("lockTTL");
    openapiFields.add("name");
    openapiFields.add("pickupDistance");
    openapiFields.add("pickupPointId");
    openapiFields.add("pickupStoreInfo");
    openapiFields.add("polygonName");
    openapiFields.add("price");
    openapiFields.add("shippingEstimate");
    openapiFields.add("shippingEstimateDate");
    openapiFields.add("tax");
    openapiFields.add("transitTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner is not found in the empty JSON string", CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `availableDeliveryWindows`
      if (jsonObj.get("availableDeliveryWindows") != null && !jsonObj.get("availableDeliveryWindows").isJsonNull()) {
        CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.validateJsonElement(jsonObj.get("availableDeliveryWindows"));
      }
      if ((jsonObj.get("deliveryChannel") != null && !jsonObj.get("deliveryChannel").isJsonNull()) && !jsonObj.get("deliveryChannel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryChannel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryChannel").toString()));
      }
      if (jsonObj.get("deliveryIds") != null && !jsonObj.get("deliveryIds").isJsonNull()) {
        JsonArray jsonArraydeliveryIds = jsonObj.getAsJsonArray("deliveryIds");
        if (jsonArraydeliveryIds != null) {
          // ensure the json data is an array
          if (!jsonObj.get("deliveryIds").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `deliveryIds` to be an array in the JSON string but got `%s`", jsonObj.get("deliveryIds").toString()));
          }

          // validate the optional field `deliveryIds` (array)
          for (int i = 0; i < jsonArraydeliveryIds.size(); i++) {
            AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner.validateJsonElement(jsonArraydeliveryIds.get(i));
          };
        }
      }
      // validate the optional field `deliveryWindow`
      if (jsonObj.get("deliveryWindow") != null && !jsonObj.get("deliveryWindow").isJsonNull()) {
        CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow.validateJsonElement(jsonObj.get("deliveryWindow"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("lockTTL") != null && !jsonObj.get("lockTTL").isJsonNull()) && !jsonObj.get("lockTTL").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lockTTL` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lockTTL").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("pickupPointId") != null && !jsonObj.get("pickupPointId").isJsonNull()) && !jsonObj.get("pickupPointId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pickupPointId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pickupPointId").toString()));
      }
      // validate the optional field `pickupStoreInfo`
      if (jsonObj.get("pickupStoreInfo") != null && !jsonObj.get("pickupStoreInfo").isJsonNull()) {
        CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo.validateJsonElement(jsonObj.get("pickupStoreInfo"));
      }
      if ((jsonObj.get("polygonName") != null && !jsonObj.get("polygonName").isJsonNull()) && !jsonObj.get("polygonName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `polygonName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("polygonName").toString()));
      }
      if ((jsonObj.get("shippingEstimate") != null && !jsonObj.get("shippingEstimate").isJsonNull()) && !jsonObj.get("shippingEstimate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shippingEstimate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shippingEstimate").toString()));
      }
      if ((jsonObj.get("shippingEstimateDate") != null && !jsonObj.get("shippingEstimateDate").isJsonNull()) && !jsonObj.get("shippingEstimateDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shippingEstimateDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shippingEstimateDate").toString()));
      }
      if ((jsonObj.get("transitTime") != null && !jsonObj.get("transitTime").isJsonNull()) && !jsonObj.get("transitTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transitTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transitTime").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner>() {
           @Override
           public void write(JsonWriter out, CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner
   */
  public static CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.class);
  }

  /**
   * Convert an instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

