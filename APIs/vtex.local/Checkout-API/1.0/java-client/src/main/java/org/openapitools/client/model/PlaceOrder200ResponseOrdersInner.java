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
import org.openapitools.client.model.AddCoupons200ResponseClientProfileData;
import org.openapitools.client.model.AddCoupons200ResponseItemMetadata;
import org.openapitools.client.model.AddCoupons200ResponsePaymentData;
import org.openapitools.client.model.AddCoupons200ResponseRatesAndBenefitsData;
import org.openapitools.client.model.AddCoupons200ResponseSellersInner;
import org.openapitools.client.model.AddCoupons200ResponseShippingData;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerTotalsInner;
import org.openapitools.client.model.PlaceOrder200ResponseOrdersInnerItemsInner;
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
 * PlaceOrder200ResponseOrdersInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrder200ResponseOrdersInner {
  public static final String SERIALIZED_NAME_ALLOW_CANCELATION = "allowCancelation";
  @SerializedName(SERIALIZED_NAME_ALLOW_CANCELATION)
  private Boolean allowCancelation;

  public static final String SERIALIZED_NAME_ALLOW_CHANGE_SELLER = "allowChangeSeller";
  @SerializedName(SERIALIZED_NAME_ALLOW_CHANGE_SELLER)
  private Boolean allowChangeSeller;

  public static final String SERIALIZED_NAME_ALLOW_EDITION = "allowEdition";
  @SerializedName(SERIALIZED_NAME_ALLOW_EDITION)
  private Boolean allowEdition;

  public static final String SERIALIZED_NAME_CHECKED_IN_PICKUP_POINT_ID = "checkedInPickupPointId";
  @SerializedName(SERIALIZED_NAME_CHECKED_IN_PICKUP_POINT_ID)
  private String checkedInPickupPointId;

  public static final String SERIALIZED_NAME_CLIENT_PROFILE_DATA = "clientProfileData";
  @SerializedName(SERIALIZED_NAME_CLIENT_PROFILE_DATA)
  private AddCoupons200ResponseClientProfileData clientProfileData;

  public static final String SERIALIZED_NAME_CREATION_DATE = "creationDate";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private String creationDate;

  public static final String SERIALIZED_NAME_FOLLOW_UP_EMAIL = "followUpEmail";
  @SerializedName(SERIALIZED_NAME_FOLLOW_UP_EMAIL)
  private String followUpEmail;

  public static final String SERIALIZED_NAME_HOST_NAME = "hostName";
  @SerializedName(SERIALIZED_NAME_HOST_NAME)
  private String hostName;

  public static final String SERIALIZED_NAME_IS_CHECKED_IN = "isCheckedIn";
  @SerializedName(SERIALIZED_NAME_IS_CHECKED_IN)
  private Boolean isCheckedIn = false;

  public static final String SERIALIZED_NAME_IS_COMPLETED = "isCompleted";
  @SerializedName(SERIALIZED_NAME_IS_COMPLETED)
  private Boolean isCompleted;

  public static final String SERIALIZED_NAME_IS_USER_DATA_VISIBLE = "isUserDataVisible";
  @SerializedName(SERIALIZED_NAME_IS_USER_DATA_VISIBLE)
  private Boolean isUserDataVisible;

  public static final String SERIALIZED_NAME_ITEM_METADATA = "itemMetadata";
  @SerializedName(SERIALIZED_NAME_ITEM_METADATA)
  private AddCoupons200ResponseItemMetadata itemMetadata;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<PlaceOrder200ResponseOrdersInnerItemsInner> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_LAST_CHANGE = "lastChange";
  @SerializedName(SERIALIZED_NAME_LAST_CHANGE)
  private String lastChange;

  public static final String SERIALIZED_NAME_MERCHANT_NAME = "merchantName";
  @SerializedName(SERIALIZED_NAME_MERCHANT_NAME)
  private String merchantName;

  public static final String SERIALIZED_NAME_ORDER_FORM_CREATION_DATE = "orderFormCreationDate";
  @SerializedName(SERIALIZED_NAME_ORDER_FORM_CREATION_DATE)
  private String orderFormCreationDate;

  public static final String SERIALIZED_NAME_ORDER_GROUP = "orderGroup";
  @SerializedName(SERIALIZED_NAME_ORDER_GROUP)
  private String orderGroup;

  public static final String SERIALIZED_NAME_ORDER_ID = "orderId";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_PAYMENT_DATA = "paymentData";
  @SerializedName(SERIALIZED_NAME_PAYMENT_DATA)
  private AddCoupons200ResponsePaymentData paymentData;

  public static final String SERIALIZED_NAME_RATES_AND_BENEFITS_DATA = "ratesAndBenefitsData";
  @SerializedName(SERIALIZED_NAME_RATES_AND_BENEFITS_DATA)
  private AddCoupons200ResponseRatesAndBenefitsData ratesAndBenefitsData;

  public static final String SERIALIZED_NAME_ROUNDING_ERROR = "roundingError";
  @SerializedName(SERIALIZED_NAME_ROUNDING_ERROR)
  private Integer roundingError;

  public static final String SERIALIZED_NAME_SALES_ASSOCIATE_ID = "salesAssociateId";
  @SerializedName(SERIALIZED_NAME_SALES_ASSOCIATE_ID)
  private String salesAssociateId;

  public static final String SERIALIZED_NAME_SALES_CHANNEL = "salesChannel";
  @SerializedName(SERIALIZED_NAME_SALES_CHANNEL)
  private String salesChannel;

  public static final String SERIALIZED_NAME_SELLER_ORDER_ID = "sellerOrderId";
  @SerializedName(SERIALIZED_NAME_SELLER_ORDER_ID)
  private String sellerOrderId;

  public static final String SERIALIZED_NAME_SELLERS = "sellers";
  @SerializedName(SERIALIZED_NAME_SELLERS)
  private List<AddCoupons200ResponseSellersInner> sellers = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHIPPING_DATA = "shippingData";
  @SerializedName(SERIALIZED_NAME_SHIPPING_DATA)
  private AddCoupons200ResponseShippingData shippingData;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private String state;

  public static final String SERIALIZED_NAME_STORE_ID = "storeId";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private String storeId;

  public static final String SERIALIZED_NAME_TIME_ZONE_CREATION_DATE = "timeZoneCreationDate";
  @SerializedName(SERIALIZED_NAME_TIME_ZONE_CREATION_DATE)
  private String timeZoneCreationDate;

  public static final String SERIALIZED_NAME_TIME_ZONE_LAST_CHANGE = "timeZoneLastChange";
  @SerializedName(SERIALIZED_NAME_TIME_ZONE_LAST_CHANGE)
  private String timeZoneLastChange;

  public static final String SERIALIZED_NAME_TOTALS = "totals";
  @SerializedName(SERIALIZED_NAME_TOTALS)
  private List<CartSimulation200ResponseLogisticsInfoInnerTotalsInner> totals = new ArrayList<>();

  public static final String SERIALIZED_NAME_USER_TYPE = "userType";
  @SerializedName(SERIALIZED_NAME_USER_TYPE)
  private String userType;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Integer value;

  public PlaceOrder200ResponseOrdersInner() {
  }

  public PlaceOrder200ResponseOrdersInner allowCancelation(Boolean allowCancelation) {
    this.allowCancelation = allowCancelation;
    return this;
  }

  /**
   * Indicates whether cancelation is allowed.
   * @return allowCancelation
   */
  @javax.annotation.Nullable
  public Boolean getAllowCancelation() {
    return allowCancelation;
  }

  public void setAllowCancelation(Boolean allowCancelation) {
    this.allowCancelation = allowCancelation;
  }


  public PlaceOrder200ResponseOrdersInner allowChangeSeller(Boolean allowChangeSeller) {
    this.allowChangeSeller = allowChangeSeller;
    return this;
  }

  /**
   * Indicates whether seller changing is allowed.
   * @return allowChangeSeller
   */
  @javax.annotation.Nullable
  public Boolean getAllowChangeSeller() {
    return allowChangeSeller;
  }

  public void setAllowChangeSeller(Boolean allowChangeSeller) {
    this.allowChangeSeller = allowChangeSeller;
  }


  public PlaceOrder200ResponseOrdersInner allowEdition(Boolean allowEdition) {
    this.allowEdition = allowEdition;
    return this;
  }

  /**
   * Indicates whether edition is allowed.
   * @return allowEdition
   */
  @javax.annotation.Nullable
  public Boolean getAllowEdition() {
    return allowEdition;
  }

  public void setAllowEdition(Boolean allowEdition) {
    this.allowEdition = allowEdition;
  }


  public PlaceOrder200ResponseOrdersInner checkedInPickupPointId(String checkedInPickupPointId) {
    this.checkedInPickupPointId = checkedInPickupPointId;
    return this;
  }

  /**
   * Checked in pickuppoint.
   * @return checkedInPickupPointId
   */
  @javax.annotation.Nullable
  public String getCheckedInPickupPointId() {
    return checkedInPickupPointId;
  }

  public void setCheckedInPickupPointId(String checkedInPickupPointId) {
    this.checkedInPickupPointId = checkedInPickupPointId;
  }


  public PlaceOrder200ResponseOrdersInner clientProfileData(AddCoupons200ResponseClientProfileData clientProfileData) {
    this.clientProfileData = clientProfileData;
    return this;
  }

  /**
   * Get clientProfileData
   * @return clientProfileData
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponseClientProfileData getClientProfileData() {
    return clientProfileData;
  }

  public void setClientProfileData(AddCoupons200ResponseClientProfileData clientProfileData) {
    this.clientProfileData = clientProfileData;
  }


  public PlaceOrder200ResponseOrdersInner creationDate(String creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * Creation date.
   * @return creationDate
   */
  @javax.annotation.Nullable
  public String getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(String creationDate) {
    this.creationDate = creationDate;
  }


  public PlaceOrder200ResponseOrdersInner followUpEmail(String followUpEmail) {
    this.followUpEmail = followUpEmail;
    return this;
  }

  /**
   * Follow up email address.
   * @return followUpEmail
   */
  @javax.annotation.Nullable
  public String getFollowUpEmail() {
    return followUpEmail;
  }

  public void setFollowUpEmail(String followUpEmail) {
    this.followUpEmail = followUpEmail;
  }


  public PlaceOrder200ResponseOrdersInner hostName(String hostName) {
    this.hostName = hostName;
    return this;
  }

  /**
   * Host name.
   * @return hostName
   */
  @javax.annotation.Nullable
  public String getHostName() {
    return hostName;
  }

  public void setHostName(String hostName) {
    this.hostName = hostName;
  }


  public PlaceOrder200ResponseOrdersInner isCheckedIn(Boolean isCheckedIn) {
    this.isCheckedIn = isCheckedIn;
    return this;
  }

  /**
   * Indicates whether order is checked in.
   * @return isCheckedIn
   */
  @javax.annotation.Nullable
  public Boolean getIsCheckedIn() {
    return isCheckedIn;
  }

  public void setIsCheckedIn(Boolean isCheckedIn) {
    this.isCheckedIn = isCheckedIn;
  }


  public PlaceOrder200ResponseOrdersInner isCompleted(Boolean isCompleted) {
    this.isCompleted = isCompleted;
    return this;
  }

  /**
   * Indicates whether order is completed.
   * @return isCompleted
   */
  @javax.annotation.Nullable
  public Boolean getIsCompleted() {
    return isCompleted;
  }

  public void setIsCompleted(Boolean isCompleted) {
    this.isCompleted = isCompleted;
  }


  public PlaceOrder200ResponseOrdersInner isUserDataVisible(Boolean isUserDataVisible) {
    this.isUserDataVisible = isUserDataVisible;
    return this;
  }

  /**
   * Indicates whether user data is visible.
   * @return isUserDataVisible
   */
  @javax.annotation.Nullable
  public Boolean getIsUserDataVisible() {
    return isUserDataVisible;
  }

  public void setIsUserDataVisible(Boolean isUserDataVisible) {
    this.isUserDataVisible = isUserDataVisible;
  }


  public PlaceOrder200ResponseOrdersInner itemMetadata(AddCoupons200ResponseItemMetadata itemMetadata) {
    this.itemMetadata = itemMetadata;
    return this;
  }

  /**
   * Get itemMetadata
   * @return itemMetadata
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponseItemMetadata getItemMetadata() {
    return itemMetadata;
  }

  public void setItemMetadata(AddCoupons200ResponseItemMetadata itemMetadata) {
    this.itemMetadata = itemMetadata;
  }


  public PlaceOrder200ResponseOrdersInner items(List<PlaceOrder200ResponseOrdersInnerItemsInner> items) {
    this.items = items;
    return this;
  }

  public PlaceOrder200ResponseOrdersInner addItemsItem(PlaceOrder200ResponseOrdersInnerItemsInner itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Information on each item in the order.
   * @return items
   */
  @javax.annotation.Nullable
  public List<PlaceOrder200ResponseOrdersInnerItemsInner> getItems() {
    return items;
  }

  public void setItems(List<PlaceOrder200ResponseOrdersInnerItemsInner> items) {
    this.items = items;
  }


  public PlaceOrder200ResponseOrdersInner lastChange(String lastChange) {
    this.lastChange = lastChange;
    return this;
  }

  /**
   * Last change.
   * @return lastChange
   */
  @javax.annotation.Nullable
  public String getLastChange() {
    return lastChange;
  }

  public void setLastChange(String lastChange) {
    this.lastChange = lastChange;
  }


  public PlaceOrder200ResponseOrdersInner merchantName(String merchantName) {
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


  public PlaceOrder200ResponseOrdersInner orderFormCreationDate(String orderFormCreationDate) {
    this.orderFormCreationDate = orderFormCreationDate;
    return this;
  }

  /**
   * &#x60;orderForm&#x60; creation date.
   * @return orderFormCreationDate
   */
  @javax.annotation.Nullable
  public String getOrderFormCreationDate() {
    return orderFormCreationDate;
  }

  public void setOrderFormCreationDate(String orderFormCreationDate) {
    this.orderFormCreationDate = orderFormCreationDate;
  }


  public PlaceOrder200ResponseOrdersInner orderGroup(String orderGroup) {
    this.orderGroup = orderGroup;
    return this;
  }

  /**
   * Order group. Orders that involve different sellers are split into different orders of a same order group.
   * @return orderGroup
   */
  @javax.annotation.Nullable
  public String getOrderGroup() {
    return orderGroup;
  }

  public void setOrderGroup(String orderGroup) {
    this.orderGroup = orderGroup;
  }


  public PlaceOrder200ResponseOrdersInner orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * ID of the order in the Order Management System (OMS).
   * @return orderId
   */
  @javax.annotation.Nullable
  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  public PlaceOrder200ResponseOrdersInner paymentData(AddCoupons200ResponsePaymentData paymentData) {
    this.paymentData = paymentData;
    return this;
  }

  /**
   * Get paymentData
   * @return paymentData
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponsePaymentData getPaymentData() {
    return paymentData;
  }

  public void setPaymentData(AddCoupons200ResponsePaymentData paymentData) {
    this.paymentData = paymentData;
  }


  public PlaceOrder200ResponseOrdersInner ratesAndBenefitsData(AddCoupons200ResponseRatesAndBenefitsData ratesAndBenefitsData) {
    this.ratesAndBenefitsData = ratesAndBenefitsData;
    return this;
  }

  /**
   * Get ratesAndBenefitsData
   * @return ratesAndBenefitsData
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponseRatesAndBenefitsData getRatesAndBenefitsData() {
    return ratesAndBenefitsData;
  }

  public void setRatesAndBenefitsData(AddCoupons200ResponseRatesAndBenefitsData ratesAndBenefitsData) {
    this.ratesAndBenefitsData = ratesAndBenefitsData;
  }


  public PlaceOrder200ResponseOrdersInner roundingError(Integer roundingError) {
    this.roundingError = roundingError;
    return this;
  }

  /**
   * Rounding error.
   * @return roundingError
   */
  @javax.annotation.Nullable
  public Integer getRoundingError() {
    return roundingError;
  }

  public void setRoundingError(Integer roundingError) {
    this.roundingError = roundingError;
  }


  public PlaceOrder200ResponseOrdersInner salesAssociateId(String salesAssociateId) {
    this.salesAssociateId = salesAssociateId;
    return this;
  }

  /**
   * Sales Associate (Seller) identification code.
   * @return salesAssociateId
   */
  @javax.annotation.Nullable
  public String getSalesAssociateId() {
    return salesAssociateId;
  }

  public void setSalesAssociateId(String salesAssociateId) {
    this.salesAssociateId = salesAssociateId;
  }


  public PlaceOrder200ResponseOrdersInner salesChannel(String salesChannel) {
    this.salesChannel = salesChannel;
    return this;
  }

  /**
   * Sales channel.
   * @return salesChannel
   */
  @javax.annotation.Nullable
  public String getSalesChannel() {
    return salesChannel;
  }

  public void setSalesChannel(String salesChannel) {
    this.salesChannel = salesChannel;
  }


  public PlaceOrder200ResponseOrdersInner sellerOrderId(String sellerOrderId) {
    this.sellerOrderId = sellerOrderId;
    return this;
  }

  /**
   * ID of the order in the seller.
   * @return sellerOrderId
   */
  @javax.annotation.Nullable
  public String getSellerOrderId() {
    return sellerOrderId;
  }

  public void setSellerOrderId(String sellerOrderId) {
    this.sellerOrderId = sellerOrderId;
  }


  public PlaceOrder200ResponseOrdersInner sellers(List<AddCoupons200ResponseSellersInner> sellers) {
    this.sellers = sellers;
    return this;
  }

  public PlaceOrder200ResponseOrdersInner addSellersItem(AddCoupons200ResponseSellersInner sellersItem) {
    if (this.sellers == null) {
      this.sellers = new ArrayList<>();
    }
    this.sellers.add(sellersItem);
    return this;
  }

  /**
   * Information on each seller.
   * @return sellers
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseSellersInner> getSellers() {
    return sellers;
  }

  public void setSellers(List<AddCoupons200ResponseSellersInner> sellers) {
    this.sellers = sellers;
  }


  public PlaceOrder200ResponseOrdersInner shippingData(AddCoupons200ResponseShippingData shippingData) {
    this.shippingData = shippingData;
    return this;
  }

  /**
   * Get shippingData
   * @return shippingData
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponseShippingData getShippingData() {
    return shippingData;
  }

  public void setShippingData(AddCoupons200ResponseShippingData shippingData) {
    this.shippingData = shippingData;
  }


  public PlaceOrder200ResponseOrdersInner state(String state) {
    this.state = state;
    return this;
  }

  /**
   * State.
   * @return state
   */
  @javax.annotation.Nullable
  public String getState() {
    return state;
  }

  public void setState(String state) {
    this.state = state;
  }


  public PlaceOrder200ResponseOrdersInner storeId(String storeId) {
    this.storeId = storeId;
    return this;
  }

  /**
   * Store ID.
   * @return storeId
   */
  @javax.annotation.Nullable
  public String getStoreId() {
    return storeId;
  }

  public void setStoreId(String storeId) {
    this.storeId = storeId;
  }


  public PlaceOrder200ResponseOrdersInner timeZoneCreationDate(String timeZoneCreationDate) {
    this.timeZoneCreationDate = timeZoneCreationDate;
    return this;
  }

  /**
   * Time zone creation date.
   * @return timeZoneCreationDate
   */
  @javax.annotation.Nullable
  public String getTimeZoneCreationDate() {
    return timeZoneCreationDate;
  }

  public void setTimeZoneCreationDate(String timeZoneCreationDate) {
    this.timeZoneCreationDate = timeZoneCreationDate;
  }


  public PlaceOrder200ResponseOrdersInner timeZoneLastChange(String timeZoneLastChange) {
    this.timeZoneLastChange = timeZoneLastChange;
    return this;
  }

  /**
   * Time zone last change.
   * @return timeZoneLastChange
   */
  @javax.annotation.Nullable
  public String getTimeZoneLastChange() {
    return timeZoneLastChange;
  }

  public void setTimeZoneLastChange(String timeZoneLastChange) {
    this.timeZoneLastChange = timeZoneLastChange;
  }


  public PlaceOrder200ResponseOrdersInner totals(List<CartSimulation200ResponseLogisticsInfoInnerTotalsInner> totals) {
    this.totals = totals;
    return this;
  }

  public PlaceOrder200ResponseOrdersInner addTotalsItem(CartSimulation200ResponseLogisticsInfoInnerTotalsInner totalsItem) {
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


  public PlaceOrder200ResponseOrdersInner userType(String userType) {
    this.userType = userType;
    return this;
  }

  /**
   * User type.
   * @return userType
   */
  @javax.annotation.Nullable
  public String getUserType() {
    return userType;
  }

  public void setUserType(String userType) {
    this.userType = userType;
  }


  public PlaceOrder200ResponseOrdersInner value(Integer value) {
    this.value = value;
    return this;
  }

  /**
   * Value of the order.
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
    PlaceOrder200ResponseOrdersInner placeOrder200ResponseOrdersInner = (PlaceOrder200ResponseOrdersInner) o;
    return Objects.equals(this.allowCancelation, placeOrder200ResponseOrdersInner.allowCancelation) &&
        Objects.equals(this.allowChangeSeller, placeOrder200ResponseOrdersInner.allowChangeSeller) &&
        Objects.equals(this.allowEdition, placeOrder200ResponseOrdersInner.allowEdition) &&
        Objects.equals(this.checkedInPickupPointId, placeOrder200ResponseOrdersInner.checkedInPickupPointId) &&
        Objects.equals(this.clientProfileData, placeOrder200ResponseOrdersInner.clientProfileData) &&
        Objects.equals(this.creationDate, placeOrder200ResponseOrdersInner.creationDate) &&
        Objects.equals(this.followUpEmail, placeOrder200ResponseOrdersInner.followUpEmail) &&
        Objects.equals(this.hostName, placeOrder200ResponseOrdersInner.hostName) &&
        Objects.equals(this.isCheckedIn, placeOrder200ResponseOrdersInner.isCheckedIn) &&
        Objects.equals(this.isCompleted, placeOrder200ResponseOrdersInner.isCompleted) &&
        Objects.equals(this.isUserDataVisible, placeOrder200ResponseOrdersInner.isUserDataVisible) &&
        Objects.equals(this.itemMetadata, placeOrder200ResponseOrdersInner.itemMetadata) &&
        Objects.equals(this.items, placeOrder200ResponseOrdersInner.items) &&
        Objects.equals(this.lastChange, placeOrder200ResponseOrdersInner.lastChange) &&
        Objects.equals(this.merchantName, placeOrder200ResponseOrdersInner.merchantName) &&
        Objects.equals(this.orderFormCreationDate, placeOrder200ResponseOrdersInner.orderFormCreationDate) &&
        Objects.equals(this.orderGroup, placeOrder200ResponseOrdersInner.orderGroup) &&
        Objects.equals(this.orderId, placeOrder200ResponseOrdersInner.orderId) &&
        Objects.equals(this.paymentData, placeOrder200ResponseOrdersInner.paymentData) &&
        Objects.equals(this.ratesAndBenefitsData, placeOrder200ResponseOrdersInner.ratesAndBenefitsData) &&
        Objects.equals(this.roundingError, placeOrder200ResponseOrdersInner.roundingError) &&
        Objects.equals(this.salesAssociateId, placeOrder200ResponseOrdersInner.salesAssociateId) &&
        Objects.equals(this.salesChannel, placeOrder200ResponseOrdersInner.salesChannel) &&
        Objects.equals(this.sellerOrderId, placeOrder200ResponseOrdersInner.sellerOrderId) &&
        Objects.equals(this.sellers, placeOrder200ResponseOrdersInner.sellers) &&
        Objects.equals(this.shippingData, placeOrder200ResponseOrdersInner.shippingData) &&
        Objects.equals(this.state, placeOrder200ResponseOrdersInner.state) &&
        Objects.equals(this.storeId, placeOrder200ResponseOrdersInner.storeId) &&
        Objects.equals(this.timeZoneCreationDate, placeOrder200ResponseOrdersInner.timeZoneCreationDate) &&
        Objects.equals(this.timeZoneLastChange, placeOrder200ResponseOrdersInner.timeZoneLastChange) &&
        Objects.equals(this.totals, placeOrder200ResponseOrdersInner.totals) &&
        Objects.equals(this.userType, placeOrder200ResponseOrdersInner.userType) &&
        Objects.equals(this.value, placeOrder200ResponseOrdersInner.value);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowCancelation, allowChangeSeller, allowEdition, checkedInPickupPointId, clientProfileData, creationDate, followUpEmail, hostName, isCheckedIn, isCompleted, isUserDataVisible, itemMetadata, items, lastChange, merchantName, orderFormCreationDate, orderGroup, orderId, paymentData, ratesAndBenefitsData, roundingError, salesAssociateId, salesChannel, sellerOrderId, sellers, shippingData, state, storeId, timeZoneCreationDate, timeZoneLastChange, totals, userType, value);
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
    sb.append("class PlaceOrder200ResponseOrdersInner {\n");
    sb.append("    allowCancelation: ").append(toIndentedString(allowCancelation)).append("\n");
    sb.append("    allowChangeSeller: ").append(toIndentedString(allowChangeSeller)).append("\n");
    sb.append("    allowEdition: ").append(toIndentedString(allowEdition)).append("\n");
    sb.append("    checkedInPickupPointId: ").append(toIndentedString(checkedInPickupPointId)).append("\n");
    sb.append("    clientProfileData: ").append(toIndentedString(clientProfileData)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    followUpEmail: ").append(toIndentedString(followUpEmail)).append("\n");
    sb.append("    hostName: ").append(toIndentedString(hostName)).append("\n");
    sb.append("    isCheckedIn: ").append(toIndentedString(isCheckedIn)).append("\n");
    sb.append("    isCompleted: ").append(toIndentedString(isCompleted)).append("\n");
    sb.append("    isUserDataVisible: ").append(toIndentedString(isUserDataVisible)).append("\n");
    sb.append("    itemMetadata: ").append(toIndentedString(itemMetadata)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    lastChange: ").append(toIndentedString(lastChange)).append("\n");
    sb.append("    merchantName: ").append(toIndentedString(merchantName)).append("\n");
    sb.append("    orderFormCreationDate: ").append(toIndentedString(orderFormCreationDate)).append("\n");
    sb.append("    orderGroup: ").append(toIndentedString(orderGroup)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    paymentData: ").append(toIndentedString(paymentData)).append("\n");
    sb.append("    ratesAndBenefitsData: ").append(toIndentedString(ratesAndBenefitsData)).append("\n");
    sb.append("    roundingError: ").append(toIndentedString(roundingError)).append("\n");
    sb.append("    salesAssociateId: ").append(toIndentedString(salesAssociateId)).append("\n");
    sb.append("    salesChannel: ").append(toIndentedString(salesChannel)).append("\n");
    sb.append("    sellerOrderId: ").append(toIndentedString(sellerOrderId)).append("\n");
    sb.append("    sellers: ").append(toIndentedString(sellers)).append("\n");
    sb.append("    shippingData: ").append(toIndentedString(shippingData)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
    sb.append("    timeZoneCreationDate: ").append(toIndentedString(timeZoneCreationDate)).append("\n");
    sb.append("    timeZoneLastChange: ").append(toIndentedString(timeZoneLastChange)).append("\n");
    sb.append("    totals: ").append(toIndentedString(totals)).append("\n");
    sb.append("    userType: ").append(toIndentedString(userType)).append("\n");
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
    openapiFields.add("allowCancelation");
    openapiFields.add("allowChangeSeller");
    openapiFields.add("allowEdition");
    openapiFields.add("checkedInPickupPointId");
    openapiFields.add("clientProfileData");
    openapiFields.add("creationDate");
    openapiFields.add("followUpEmail");
    openapiFields.add("hostName");
    openapiFields.add("isCheckedIn");
    openapiFields.add("isCompleted");
    openapiFields.add("isUserDataVisible");
    openapiFields.add("itemMetadata");
    openapiFields.add("items");
    openapiFields.add("lastChange");
    openapiFields.add("merchantName");
    openapiFields.add("orderFormCreationDate");
    openapiFields.add("orderGroup");
    openapiFields.add("orderId");
    openapiFields.add("paymentData");
    openapiFields.add("ratesAndBenefitsData");
    openapiFields.add("roundingError");
    openapiFields.add("salesAssociateId");
    openapiFields.add("salesChannel");
    openapiFields.add("sellerOrderId");
    openapiFields.add("sellers");
    openapiFields.add("shippingData");
    openapiFields.add("state");
    openapiFields.add("storeId");
    openapiFields.add("timeZoneCreationDate");
    openapiFields.add("timeZoneLastChange");
    openapiFields.add("totals");
    openapiFields.add("userType");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrder200ResponseOrdersInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrder200ResponseOrdersInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrder200ResponseOrdersInner is not found in the empty JSON string", PlaceOrder200ResponseOrdersInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrder200ResponseOrdersInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrder200ResponseOrdersInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("checkedInPickupPointId") != null && !jsonObj.get("checkedInPickupPointId").isJsonNull()) && !jsonObj.get("checkedInPickupPointId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checkedInPickupPointId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checkedInPickupPointId").toString()));
      }
      // validate the optional field `clientProfileData`
      if (jsonObj.get("clientProfileData") != null && !jsonObj.get("clientProfileData").isJsonNull()) {
        AddCoupons200ResponseClientProfileData.validateJsonElement(jsonObj.get("clientProfileData"));
      }
      if ((jsonObj.get("creationDate") != null && !jsonObj.get("creationDate").isJsonNull()) && !jsonObj.get("creationDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creationDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creationDate").toString()));
      }
      if ((jsonObj.get("followUpEmail") != null && !jsonObj.get("followUpEmail").isJsonNull()) && !jsonObj.get("followUpEmail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `followUpEmail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("followUpEmail").toString()));
      }
      if ((jsonObj.get("hostName") != null && !jsonObj.get("hostName").isJsonNull()) && !jsonObj.get("hostName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hostName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hostName").toString()));
      }
      // validate the optional field `itemMetadata`
      if (jsonObj.get("itemMetadata") != null && !jsonObj.get("itemMetadata").isJsonNull()) {
        AddCoupons200ResponseItemMetadata.validateJsonElement(jsonObj.get("itemMetadata"));
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
            PlaceOrder200ResponseOrdersInnerItemsInner.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if ((jsonObj.get("lastChange") != null && !jsonObj.get("lastChange").isJsonNull()) && !jsonObj.get("lastChange").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastChange` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastChange").toString()));
      }
      if ((jsonObj.get("merchantName") != null && !jsonObj.get("merchantName").isJsonNull()) && !jsonObj.get("merchantName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchantName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchantName").toString()));
      }
      if ((jsonObj.get("orderFormCreationDate") != null && !jsonObj.get("orderFormCreationDate").isJsonNull()) && !jsonObj.get("orderFormCreationDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderFormCreationDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderFormCreationDate").toString()));
      }
      if ((jsonObj.get("orderGroup") != null && !jsonObj.get("orderGroup").isJsonNull()) && !jsonObj.get("orderGroup").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderGroup` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderGroup").toString()));
      }
      if ((jsonObj.get("orderId") != null && !jsonObj.get("orderId").isJsonNull()) && !jsonObj.get("orderId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderId").toString()));
      }
      // validate the optional field `paymentData`
      if (jsonObj.get("paymentData") != null && !jsonObj.get("paymentData").isJsonNull()) {
        AddCoupons200ResponsePaymentData.validateJsonElement(jsonObj.get("paymentData"));
      }
      // validate the optional field `ratesAndBenefitsData`
      if (jsonObj.get("ratesAndBenefitsData") != null && !jsonObj.get("ratesAndBenefitsData").isJsonNull()) {
        AddCoupons200ResponseRatesAndBenefitsData.validateJsonElement(jsonObj.get("ratesAndBenefitsData"));
      }
      if ((jsonObj.get("salesAssociateId") != null && !jsonObj.get("salesAssociateId").isJsonNull()) && !jsonObj.get("salesAssociateId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `salesAssociateId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("salesAssociateId").toString()));
      }
      if ((jsonObj.get("salesChannel") != null && !jsonObj.get("salesChannel").isJsonNull()) && !jsonObj.get("salesChannel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `salesChannel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("salesChannel").toString()));
      }
      if ((jsonObj.get("sellerOrderId") != null && !jsonObj.get("sellerOrderId").isJsonNull()) && !jsonObj.get("sellerOrderId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellerOrderId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sellerOrderId").toString()));
      }
      if (jsonObj.get("sellers") != null && !jsonObj.get("sellers").isJsonNull()) {
        JsonArray jsonArraysellers = jsonObj.getAsJsonArray("sellers");
        if (jsonArraysellers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("sellers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `sellers` to be an array in the JSON string but got `%s`", jsonObj.get("sellers").toString()));
          }

          // validate the optional field `sellers` (array)
          for (int i = 0; i < jsonArraysellers.size(); i++) {
            AddCoupons200ResponseSellersInner.validateJsonElement(jsonArraysellers.get(i));
          };
        }
      }
      // validate the optional field `shippingData`
      if (jsonObj.get("shippingData") != null && !jsonObj.get("shippingData").isJsonNull()) {
        AddCoupons200ResponseShippingData.validateJsonElement(jsonObj.get("shippingData"));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      if ((jsonObj.get("storeId") != null && !jsonObj.get("storeId").isJsonNull()) && !jsonObj.get("storeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `storeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("storeId").toString()));
      }
      if ((jsonObj.get("timeZoneCreationDate") != null && !jsonObj.get("timeZoneCreationDate").isJsonNull()) && !jsonObj.get("timeZoneCreationDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timeZoneCreationDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timeZoneCreationDate").toString()));
      }
      if ((jsonObj.get("timeZoneLastChange") != null && !jsonObj.get("timeZoneLastChange").isJsonNull()) && !jsonObj.get("timeZoneLastChange").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timeZoneLastChange` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timeZoneLastChange").toString()));
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
      if ((jsonObj.get("userType") != null && !jsonObj.get("userType").isJsonNull()) && !jsonObj.get("userType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userType").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrder200ResponseOrdersInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrder200ResponseOrdersInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrder200ResponseOrdersInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrder200ResponseOrdersInner.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrder200ResponseOrdersInner>() {
           @Override
           public void write(JsonWriter out, PlaceOrder200ResponseOrdersInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrder200ResponseOrdersInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrder200ResponseOrdersInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrder200ResponseOrdersInner
   * @throws IOException if the JSON string is invalid with respect to PlaceOrder200ResponseOrdersInner
   */
  public static PlaceOrder200ResponseOrdersInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrder200ResponseOrdersInner.class);
  }

  /**
   * Convert an instance of PlaceOrder200ResponseOrdersInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

