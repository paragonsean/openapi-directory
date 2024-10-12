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
import org.openapitools.client.model.AddCoupons200ResponseAvailableAddressesInner;
import org.openapitools.client.model.AddCoupons200ResponseClientProfileData;
import org.openapitools.client.model.AddCoupons200ResponseItemMetadata;
import org.openapitools.client.model.AddCoupons200ResponseItemsOrdination;
import org.openapitools.client.model.AddCoupons200ResponsePaymentData;
import org.openapitools.client.model.AddCoupons200ResponseRatesAndBenefitsData;
import org.openapitools.client.model.AddCoupons200ResponseSellersInner;
import org.openapitools.client.model.AddCoupons200ResponseShippingData;
import org.openapitools.client.model.Items200ResponseClientPreferencesData;
import org.openapitools.client.model.Items200ResponseItemsInner;
import org.openapitools.client.model.Items200ResponseMarketingData;
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
 * Items200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Items200Response {
  public static final String SERIALIZED_NAME_ALLOW_MANUAL_PRICE = "allowManualPrice";
  @SerializedName(SERIALIZED_NAME_ALLOW_MANUAL_PRICE)
  private Boolean allowManualPrice;

  public static final String SERIALIZED_NAME_AVAILABLE_ACCOUNTS = "availableAccounts";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ACCOUNTS)
  private List<String> availableAccounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_AVAILABLE_ADDRESSES = "availableAddresses";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ADDRESSES)
  private List<AddCoupons200ResponseAvailableAddressesInner> availableAddresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_CAN_EDIT_DATA = "canEditData";
  @SerializedName(SERIALIZED_NAME_CAN_EDIT_DATA)
  private Boolean canEditData;

  public static final String SERIALIZED_NAME_CLIENT_PREFERENCES_DATA = "clientPreferencesData";
  @SerializedName(SERIALIZED_NAME_CLIENT_PREFERENCES_DATA)
  private Items200ResponseClientPreferencesData clientPreferencesData;

  public static final String SERIALIZED_NAME_CLIENT_PROFILE_DATA = "clientProfileData";
  @SerializedName(SERIALIZED_NAME_CLIENT_PROFILE_DATA)
  private AddCoupons200ResponseClientProfileData clientProfileData;

  public static final String SERIALIZED_NAME_COMMERCIAL_CONDITION_DATA = "commercialConditionData";
  @SerializedName(SERIALIZED_NAME_COMMERCIAL_CONDITION_DATA)
  private Object commercialConditionData;

  public static final String SERIALIZED_NAME_CUSTOM_DATA = "customData";
  @SerializedName(SERIALIZED_NAME_CUSTOM_DATA)
  private Object customData;

  public static final String SERIALIZED_NAME_GIFT_REGISTRY_DATA = "giftRegistryData";
  @SerializedName(SERIALIZED_NAME_GIFT_REGISTRY_DATA)
  private Object giftRegistryData;

  public static final String SERIALIZED_NAME_HOOKS_DATA = "hooksData";
  @SerializedName(SERIALIZED_NAME_HOOKS_DATA)
  private Object hooksData;

  public static final String SERIALIZED_NAME_IGNORE_PROFILE_DATA = "ignoreProfileData";
  @SerializedName(SERIALIZED_NAME_IGNORE_PROFILE_DATA)
  private Boolean ignoreProfileData;

  public static final String SERIALIZED_NAME_INVOICE_DATA = "invoiceData";
  @SerializedName(SERIALIZED_NAME_INVOICE_DATA)
  private Object invoiceData;

  public static final String SERIALIZED_NAME_IS_CHECKED_IN = "isCheckedIn";
  @SerializedName(SERIALIZED_NAME_IS_CHECKED_IN)
  private Boolean isCheckedIn;

  public static final String SERIALIZED_NAME_ITEM_METADATA = "itemMetadata";
  @SerializedName(SERIALIZED_NAME_ITEM_METADATA)
  private AddCoupons200ResponseItemMetadata itemMetadata;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<Items200ResponseItemsInner> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_ITEMS_ORDINATION = "itemsOrdination";
  @SerializedName(SERIALIZED_NAME_ITEMS_ORDINATION)
  private AddCoupons200ResponseItemsOrdination itemsOrdination;

  public static final String SERIALIZED_NAME_LOGGED_IN = "loggedIn";
  @SerializedName(SERIALIZED_NAME_LOGGED_IN)
  private Boolean loggedIn;

  public static final String SERIALIZED_NAME_MARKETING_DATA = "marketingData";
  @SerializedName(SERIALIZED_NAME_MARKETING_DATA)
  private Items200ResponseMarketingData marketingData;

  public static final String SERIALIZED_NAME_MESSAGES = "messages";
  @SerializedName(SERIALIZED_NAME_MESSAGES)
  private List<Object> messages = new ArrayList<>();

  public static final String SERIALIZED_NAME_OPEN_TEXT_FIELD = "openTextField";
  @SerializedName(SERIALIZED_NAME_OPEN_TEXT_FIELD)
  private String openTextField = "open-text-example";

  public static final String SERIALIZED_NAME_ORDER_FORM_ID = "orderFormId";
  @SerializedName(SERIALIZED_NAME_ORDER_FORM_ID)
  private String orderFormId;

  public static final String SERIALIZED_NAME_PAYMENT_DATA = "paymentData";
  @SerializedName(SERIALIZED_NAME_PAYMENT_DATA)
  private AddCoupons200ResponsePaymentData paymentData;

  public static final String SERIALIZED_NAME_PROFILE_PROVIDER = "profileProvider";
  @SerializedName(SERIALIZED_NAME_PROFILE_PROVIDER)
  private String profileProvider;

  public static final String SERIALIZED_NAME_RATES_AND_BENEFITS_DATA = "ratesAndBenefitsData";
  @SerializedName(SERIALIZED_NAME_RATES_AND_BENEFITS_DATA)
  private AddCoupons200ResponseRatesAndBenefitsData ratesAndBenefitsData;

  public static final String SERIALIZED_NAME_SALES_CHANNEL = "salesChannel";
  @SerializedName(SERIALIZED_NAME_SALES_CHANNEL)
  private String salesChannel;

  public static final String SERIALIZED_NAME_SELECTABLE_GIFTS = "selectableGifts";
  @SerializedName(SERIALIZED_NAME_SELECTABLE_GIFTS)
  private List<Object> selectableGifts = new ArrayList<>();

  public static final String SERIALIZED_NAME_SELLERS = "sellers";
  @SerializedName(SERIALIZED_NAME_SELLERS)
  private List<AddCoupons200ResponseSellersInner> sellers = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHIPPING_DATA = "shippingData";
  @SerializedName(SERIALIZED_NAME_SHIPPING_DATA)
  private AddCoupons200ResponseShippingData shippingData;

  public static final String SERIALIZED_NAME_STORE_ID = "storeId";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private String storeId;

  public static final String SERIALIZED_NAME_STORE_PREFERENCES_DATA = "storePreferencesData";
  @SerializedName(SERIALIZED_NAME_STORE_PREFERENCES_DATA)
  private Object storePreferencesData;

  public static final String SERIALIZED_NAME_SUBSCRIPTION_DATA = "subscriptionData";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTION_DATA)
  private Object subscriptionData;

  public static final String SERIALIZED_NAME_TOTALIZERS = "totalizers";
  @SerializedName(SERIALIZED_NAME_TOTALIZERS)
  private List<Object> totalizers = new ArrayList<>();

  public static final String SERIALIZED_NAME_USER_PROFILE_ID = "userProfileId";
  @SerializedName(SERIALIZED_NAME_USER_PROFILE_ID)
  private String userProfileId;

  public static final String SERIALIZED_NAME_USER_TYPE = "userType";
  @SerializedName(SERIALIZED_NAME_USER_TYPE)
  private String userType;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Integer value;

  public Items200Response() {
  }

  public Items200Response allowManualPrice(Boolean allowManualPrice) {
    this.allowManualPrice = allowManualPrice;
    return this;
  }

  /**
   * Permission to modify item price manually.
   * @return allowManualPrice
   */
  @javax.annotation.Nullable
  public Boolean getAllowManualPrice() {
    return allowManualPrice;
  }

  public void setAllowManualPrice(Boolean allowManualPrice) {
    this.allowManualPrice = allowManualPrice;
  }


  public Items200Response availableAccounts(List<String> availableAccounts) {
    this.availableAccounts = availableAccounts;
    return this;
  }

  public Items200Response addAvailableAccountsItem(String availableAccountsItem) {
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
  public List<String> getAvailableAccounts() {
    return availableAccounts;
  }

  public void setAvailableAccounts(List<String> availableAccounts) {
    this.availableAccounts = availableAccounts;
  }


  public Items200Response availableAddresses(List<AddCoupons200ResponseAvailableAddressesInner> availableAddresses) {
    this.availableAddresses = availableAddresses;
    return this;
  }

  public Items200Response addAvailableAddressesItem(AddCoupons200ResponseAvailableAddressesInner availableAddressesItem) {
    if (this.availableAddresses == null) {
      this.availableAddresses = new ArrayList<>();
    }
    this.availableAddresses.add(availableAddressesItem);
    return this;
  }

  /**
   * Information on each available address.
   * @return availableAddresses
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseAvailableAddressesInner> getAvailableAddresses() {
    return availableAddresses;
  }

  public void setAvailableAddresses(List<AddCoupons200ResponseAvailableAddressesInner> availableAddresses) {
    this.availableAddresses = availableAddresses;
  }


  public Items200Response canEditData(Boolean canEditData) {
    this.canEditData = canEditData;
    return this;
  }

  /**
   * Data can be edited.
   * @return canEditData
   */
  @javax.annotation.Nullable
  public Boolean getCanEditData() {
    return canEditData;
  }

  public void setCanEditData(Boolean canEditData) {
    this.canEditData = canEditData;
  }


  public Items200Response clientPreferencesData(Items200ResponseClientPreferencesData clientPreferencesData) {
    this.clientPreferencesData = clientPreferencesData;
    return this;
  }

  /**
   * Get clientPreferencesData
   * @return clientPreferencesData
   */
  @javax.annotation.Nullable
  public Items200ResponseClientPreferencesData getClientPreferencesData() {
    return clientPreferencesData;
  }

  public void setClientPreferencesData(Items200ResponseClientPreferencesData clientPreferencesData) {
    this.clientPreferencesData = clientPreferencesData;
  }


  public Items200Response clientProfileData(AddCoupons200ResponseClientProfileData clientProfileData) {
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


  public Items200Response commercialConditionData(Object commercialConditionData) {
    this.commercialConditionData = commercialConditionData;
    return this;
  }

  /**
   * Object containing commercial condition information.
   * @return commercialConditionData
   */
  @javax.annotation.Nullable
  public Object getCommercialConditionData() {
    return commercialConditionData;
  }

  public void setCommercialConditionData(Object commercialConditionData) {
    this.commercialConditionData = commercialConditionData;
  }


  public Items200Response customData(Object customData) {
    this.customData = customData;
    return this;
  }

  /**
   * Customer additional information.
   * @return customData
   */
  @javax.annotation.Nullable
  public Object getCustomData() {
    return customData;
  }

  public void setCustomData(Object customData) {
    this.customData = customData;
  }


  public Items200Response giftRegistryData(Object giftRegistryData) {
    this.giftRegistryData = giftRegistryData;
    return this;
  }

  /**
   * Gift registry list information.
   * @return giftRegistryData
   */
  @javax.annotation.Nullable
  public Object getGiftRegistryData() {
    return giftRegistryData;
  }

  public void setGiftRegistryData(Object giftRegistryData) {
    this.giftRegistryData = giftRegistryData;
  }


  public Items200Response hooksData(Object hooksData) {
    this.hooksData = hooksData;
    return this;
  }

  /**
   * Hooks information.
   * @return hooksData
   */
  @javax.annotation.Nullable
  public Object getHooksData() {
    return hooksData;
  }

  public void setHooksData(Object hooksData) {
    this.hooksData = hooksData;
  }


  public Items200Response ignoreProfileData(Boolean ignoreProfileData) {
    this.ignoreProfileData = ignoreProfileData;
    return this;
  }

  /**
   * Ignore customer profile data.
   * @return ignoreProfileData
   */
  @javax.annotation.Nullable
  public Boolean getIgnoreProfileData() {
    return ignoreProfileData;
  }

  public void setIgnoreProfileData(Boolean ignoreProfileData) {
    this.ignoreProfileData = ignoreProfileData;
  }


  public Items200Response invoiceData(Object invoiceData) {
    this.invoiceData = invoiceData;
    return this;
  }

  /**
   * Object containing information pertinent to the order&#39;s invoice.
   * @return invoiceData
   */
  @javax.annotation.Nullable
  public Object getInvoiceData() {
    return invoiceData;
  }

  public void setInvoiceData(Object invoiceData) {
    this.invoiceData = invoiceData;
  }


  public Items200Response isCheckedIn(Boolean isCheckedIn) {
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


  public Items200Response itemMetadata(AddCoupons200ResponseItemMetadata itemMetadata) {
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


  public Items200Response items(List<Items200ResponseItemsInner> items) {
    this.items = items;
    return this;
  }

  public Items200Response addItemsItem(Items200ResponseItemsInner itemsItem) {
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
  public List<Items200ResponseItemsInner> getItems() {
    return items;
  }

  public void setItems(List<Items200ResponseItemsInner> items) {
    this.items = items;
  }


  public Items200Response itemsOrdination(AddCoupons200ResponseItemsOrdination itemsOrdination) {
    this.itemsOrdination = itemsOrdination;
    return this;
  }

  /**
   * Get itemsOrdination
   * @return itemsOrdination
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponseItemsOrdination getItemsOrdination() {
    return itemsOrdination;
  }

  public void setItemsOrdination(AddCoupons200ResponseItemsOrdination itemsOrdination) {
    this.itemsOrdination = itemsOrdination;
  }


  public Items200Response loggedIn(Boolean loggedIn) {
    this.loggedIn = loggedIn;
    return this;
  }

  /**
   * Indicates whether the user is logged into the store.
   * @return loggedIn
   */
  @javax.annotation.Nullable
  public Boolean getLoggedIn() {
    return loggedIn;
  }

  public void setLoggedIn(Boolean loggedIn) {
    this.loggedIn = loggedIn;
  }


  public Items200Response marketingData(Items200ResponseMarketingData marketingData) {
    this.marketingData = marketingData;
    return this;
  }

  /**
   * Get marketingData
   * @return marketingData
   */
  @javax.annotation.Nullable
  public Items200ResponseMarketingData getMarketingData() {
    return marketingData;
  }

  public void setMarketingData(Items200ResponseMarketingData marketingData) {
    this.marketingData = marketingData;
  }


  public Items200Response messages(List<Object> messages) {
    this.messages = messages;
    return this;
  }

  public Items200Response addMessagesItem(Object messagesItem) {
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


  public Items200Response openTextField(String openTextField) {
    this.openTextField = openTextField;
    return this;
  }

  /**
   * Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as &#x60;JSON&#x60; even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1).
   * @return openTextField
   */
  @javax.annotation.Nullable
  public String getOpenTextField() {
    return openTextField;
  }

  public void setOpenTextField(String openTextField) {
    this.openTextField = openTextField;
  }


  public Items200Response orderFormId(String orderFormId) {
    this.orderFormId = orderFormId;
    return this;
  }

  /**
   * ID of the orderForm corresponding to a specific cart.
   * @return orderFormId
   */
  @javax.annotation.Nullable
  public String getOrderFormId() {
    return orderFormId;
  }

  public void setOrderFormId(String orderFormId) {
    this.orderFormId = orderFormId;
  }


  public Items200Response paymentData(AddCoupons200ResponsePaymentData paymentData) {
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


  public Items200Response profileProvider(String profileProvider) {
    this.profileProvider = profileProvider;
    return this;
  }

  /**
   * Profile provider.
   * @return profileProvider
   */
  @javax.annotation.Nullable
  public String getProfileProvider() {
    return profileProvider;
  }

  public void setProfileProvider(String profileProvider) {
    this.profileProvider = profileProvider;
  }


  public Items200Response ratesAndBenefitsData(AddCoupons200ResponseRatesAndBenefitsData ratesAndBenefitsData) {
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


  public Items200Response salesChannel(String salesChannel) {
    this.salesChannel = salesChannel;
    return this;
  }

  /**
   * Attribute created by the seller, in their VTEX store configuration.
   * @return salesChannel
   */
  @javax.annotation.Nullable
  public String getSalesChannel() {
    return salesChannel;
  }

  public void setSalesChannel(String salesChannel) {
    this.salesChannel = salesChannel;
  }


  public Items200Response selectableGifts(List<Object> selectableGifts) {
    this.selectableGifts = selectableGifts;
    return this;
  }

  public Items200Response addSelectableGiftsItem(Object selectableGiftsItem) {
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


  public Items200Response sellers(List<AddCoupons200ResponseSellersInner> sellers) {
    this.sellers = sellers;
    return this;
  }

  public Items200Response addSellersItem(AddCoupons200ResponseSellersInner sellersItem) {
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


  public Items200Response shippingData(AddCoupons200ResponseShippingData shippingData) {
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


  public Items200Response storeId(String storeId) {
    this.storeId = storeId;
    return this;
  }

  /**
   * ID of the store.
   * @return storeId
   */
  @javax.annotation.Nullable
  public String getStoreId() {
    return storeId;
  }

  public void setStoreId(String storeId) {
    this.storeId = storeId;
  }


  public Items200Response storePreferencesData(Object storePreferencesData) {
    this.storePreferencesData = storePreferencesData;
    return this;
  }

  /**
   * Object containing data from the store&#39;s configuration (stored in VTEX&#39;s License Manager).
   * @return storePreferencesData
   */
  @javax.annotation.Nullable
  public Object getStorePreferencesData() {
    return storePreferencesData;
  }

  public void setStorePreferencesData(Object storePreferencesData) {
    this.storePreferencesData = storePreferencesData;
  }


  public Items200Response subscriptionData(Object subscriptionData) {
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


  public Items200Response totalizers(List<Object> totalizers) {
    this.totalizers = totalizers;
    return this;
  }

  public Items200Response addTotalizersItem(Object totalizersItem) {
    if (this.totalizers == null) {
      this.totalizers = new ArrayList<>();
    }
    this.totalizers.add(totalizersItem);
    return this;
  }

  /**
   * Array containing an object for each totalizer for the purchase. Totalizers contain the sum of values for a specific part of the order (e.g. Total item value, Total shipping value).
   * @return totalizers
   */
  @javax.annotation.Nullable
  public List<Object> getTotalizers() {
    return totalizers;
  }

  public void setTotalizers(List<Object> totalizers) {
    this.totalizers = totalizers;
  }


  public Items200Response userProfileId(String userProfileId) {
    this.userProfileId = userProfileId;
    return this;
  }

  /**
   * Unique ID associated with the customer profile.
   * @return userProfileId
   */
  @javax.annotation.Nullable
  public String getUserProfileId() {
    return userProfileId;
  }

  public void setUserProfileId(String userProfileId) {
    this.userProfileId = userProfileId;
  }


  public Items200Response userType(String userType) {
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


  public Items200Response value(Integer value) {
    this.value = value;
    return this;
  }

  /**
   * Total value of the order without separating cents. For example, $24.99 is represented &#x60;2499&#x60;.
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
    Items200Response items200Response = (Items200Response) o;
    return Objects.equals(this.allowManualPrice, items200Response.allowManualPrice) &&
        Objects.equals(this.availableAccounts, items200Response.availableAccounts) &&
        Objects.equals(this.availableAddresses, items200Response.availableAddresses) &&
        Objects.equals(this.canEditData, items200Response.canEditData) &&
        Objects.equals(this.clientPreferencesData, items200Response.clientPreferencesData) &&
        Objects.equals(this.clientProfileData, items200Response.clientProfileData) &&
        Objects.equals(this.commercialConditionData, items200Response.commercialConditionData) &&
        Objects.equals(this.customData, items200Response.customData) &&
        Objects.equals(this.giftRegistryData, items200Response.giftRegistryData) &&
        Objects.equals(this.hooksData, items200Response.hooksData) &&
        Objects.equals(this.ignoreProfileData, items200Response.ignoreProfileData) &&
        Objects.equals(this.invoiceData, items200Response.invoiceData) &&
        Objects.equals(this.isCheckedIn, items200Response.isCheckedIn) &&
        Objects.equals(this.itemMetadata, items200Response.itemMetadata) &&
        Objects.equals(this.items, items200Response.items) &&
        Objects.equals(this.itemsOrdination, items200Response.itemsOrdination) &&
        Objects.equals(this.loggedIn, items200Response.loggedIn) &&
        Objects.equals(this.marketingData, items200Response.marketingData) &&
        Objects.equals(this.messages, items200Response.messages) &&
        Objects.equals(this.openTextField, items200Response.openTextField) &&
        Objects.equals(this.orderFormId, items200Response.orderFormId) &&
        Objects.equals(this.paymentData, items200Response.paymentData) &&
        Objects.equals(this.profileProvider, items200Response.profileProvider) &&
        Objects.equals(this.ratesAndBenefitsData, items200Response.ratesAndBenefitsData) &&
        Objects.equals(this.salesChannel, items200Response.salesChannel) &&
        Objects.equals(this.selectableGifts, items200Response.selectableGifts) &&
        Objects.equals(this.sellers, items200Response.sellers) &&
        Objects.equals(this.shippingData, items200Response.shippingData) &&
        Objects.equals(this.storeId, items200Response.storeId) &&
        Objects.equals(this.storePreferencesData, items200Response.storePreferencesData) &&
        Objects.equals(this.subscriptionData, items200Response.subscriptionData) &&
        Objects.equals(this.totalizers, items200Response.totalizers) &&
        Objects.equals(this.userProfileId, items200Response.userProfileId) &&
        Objects.equals(this.userType, items200Response.userType) &&
        Objects.equals(this.value, items200Response.value);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowManualPrice, availableAccounts, availableAddresses, canEditData, clientPreferencesData, clientProfileData, commercialConditionData, customData, giftRegistryData, hooksData, ignoreProfileData, invoiceData, isCheckedIn, itemMetadata, items, itemsOrdination, loggedIn, marketingData, messages, openTextField, orderFormId, paymentData, profileProvider, ratesAndBenefitsData, salesChannel, selectableGifts, sellers, shippingData, storeId, storePreferencesData, subscriptionData, totalizers, userProfileId, userType, value);
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
    sb.append("class Items200Response {\n");
    sb.append("    allowManualPrice: ").append(toIndentedString(allowManualPrice)).append("\n");
    sb.append("    availableAccounts: ").append(toIndentedString(availableAccounts)).append("\n");
    sb.append("    availableAddresses: ").append(toIndentedString(availableAddresses)).append("\n");
    sb.append("    canEditData: ").append(toIndentedString(canEditData)).append("\n");
    sb.append("    clientPreferencesData: ").append(toIndentedString(clientPreferencesData)).append("\n");
    sb.append("    clientProfileData: ").append(toIndentedString(clientProfileData)).append("\n");
    sb.append("    commercialConditionData: ").append(toIndentedString(commercialConditionData)).append("\n");
    sb.append("    customData: ").append(toIndentedString(customData)).append("\n");
    sb.append("    giftRegistryData: ").append(toIndentedString(giftRegistryData)).append("\n");
    sb.append("    hooksData: ").append(toIndentedString(hooksData)).append("\n");
    sb.append("    ignoreProfileData: ").append(toIndentedString(ignoreProfileData)).append("\n");
    sb.append("    invoiceData: ").append(toIndentedString(invoiceData)).append("\n");
    sb.append("    isCheckedIn: ").append(toIndentedString(isCheckedIn)).append("\n");
    sb.append("    itemMetadata: ").append(toIndentedString(itemMetadata)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    itemsOrdination: ").append(toIndentedString(itemsOrdination)).append("\n");
    sb.append("    loggedIn: ").append(toIndentedString(loggedIn)).append("\n");
    sb.append("    marketingData: ").append(toIndentedString(marketingData)).append("\n");
    sb.append("    messages: ").append(toIndentedString(messages)).append("\n");
    sb.append("    openTextField: ").append(toIndentedString(openTextField)).append("\n");
    sb.append("    orderFormId: ").append(toIndentedString(orderFormId)).append("\n");
    sb.append("    paymentData: ").append(toIndentedString(paymentData)).append("\n");
    sb.append("    profileProvider: ").append(toIndentedString(profileProvider)).append("\n");
    sb.append("    ratesAndBenefitsData: ").append(toIndentedString(ratesAndBenefitsData)).append("\n");
    sb.append("    salesChannel: ").append(toIndentedString(salesChannel)).append("\n");
    sb.append("    selectableGifts: ").append(toIndentedString(selectableGifts)).append("\n");
    sb.append("    sellers: ").append(toIndentedString(sellers)).append("\n");
    sb.append("    shippingData: ").append(toIndentedString(shippingData)).append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
    sb.append("    storePreferencesData: ").append(toIndentedString(storePreferencesData)).append("\n");
    sb.append("    subscriptionData: ").append(toIndentedString(subscriptionData)).append("\n");
    sb.append("    totalizers: ").append(toIndentedString(totalizers)).append("\n");
    sb.append("    userProfileId: ").append(toIndentedString(userProfileId)).append("\n");
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
    openapiFields.add("allowManualPrice");
    openapiFields.add("availableAccounts");
    openapiFields.add("availableAddresses");
    openapiFields.add("canEditData");
    openapiFields.add("clientPreferencesData");
    openapiFields.add("clientProfileData");
    openapiFields.add("commercialConditionData");
    openapiFields.add("customData");
    openapiFields.add("giftRegistryData");
    openapiFields.add("hooksData");
    openapiFields.add("ignoreProfileData");
    openapiFields.add("invoiceData");
    openapiFields.add("isCheckedIn");
    openapiFields.add("itemMetadata");
    openapiFields.add("items");
    openapiFields.add("itemsOrdination");
    openapiFields.add("loggedIn");
    openapiFields.add("marketingData");
    openapiFields.add("messages");
    openapiFields.add("openTextField");
    openapiFields.add("orderFormId");
    openapiFields.add("paymentData");
    openapiFields.add("profileProvider");
    openapiFields.add("ratesAndBenefitsData");
    openapiFields.add("salesChannel");
    openapiFields.add("selectableGifts");
    openapiFields.add("sellers");
    openapiFields.add("shippingData");
    openapiFields.add("storeId");
    openapiFields.add("storePreferencesData");
    openapiFields.add("subscriptionData");
    openapiFields.add("totalizers");
    openapiFields.add("userProfileId");
    openapiFields.add("userType");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Items200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Items200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Items200Response is not found in the empty JSON string", Items200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Items200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Items200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("availableAccounts") != null && !jsonObj.get("availableAccounts").isJsonNull() && !jsonObj.get("availableAccounts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `availableAccounts` to be an array in the JSON string but got `%s`", jsonObj.get("availableAccounts").toString()));
      }
      if (jsonObj.get("availableAddresses") != null && !jsonObj.get("availableAddresses").isJsonNull()) {
        JsonArray jsonArrayavailableAddresses = jsonObj.getAsJsonArray("availableAddresses");
        if (jsonArrayavailableAddresses != null) {
          // ensure the json data is an array
          if (!jsonObj.get("availableAddresses").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `availableAddresses` to be an array in the JSON string but got `%s`", jsonObj.get("availableAddresses").toString()));
          }

          // validate the optional field `availableAddresses` (array)
          for (int i = 0; i < jsonArrayavailableAddresses.size(); i++) {
            AddCoupons200ResponseAvailableAddressesInner.validateJsonElement(jsonArrayavailableAddresses.get(i));
          };
        }
      }
      // validate the optional field `clientPreferencesData`
      if (jsonObj.get("clientPreferencesData") != null && !jsonObj.get("clientPreferencesData").isJsonNull()) {
        Items200ResponseClientPreferencesData.validateJsonElement(jsonObj.get("clientPreferencesData"));
      }
      // validate the optional field `clientProfileData`
      if (jsonObj.get("clientProfileData") != null && !jsonObj.get("clientProfileData").isJsonNull()) {
        AddCoupons200ResponseClientProfileData.validateJsonElement(jsonObj.get("clientProfileData"));
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
            Items200ResponseItemsInner.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      // validate the optional field `itemsOrdination`
      if (jsonObj.get("itemsOrdination") != null && !jsonObj.get("itemsOrdination").isJsonNull()) {
        AddCoupons200ResponseItemsOrdination.validateJsonElement(jsonObj.get("itemsOrdination"));
      }
      // validate the optional field `marketingData`
      if (jsonObj.get("marketingData") != null && !jsonObj.get("marketingData").isJsonNull()) {
        Items200ResponseMarketingData.validateJsonElement(jsonObj.get("marketingData"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("messages") != null && !jsonObj.get("messages").isJsonNull() && !jsonObj.get("messages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `messages` to be an array in the JSON string but got `%s`", jsonObj.get("messages").toString()));
      }
      if ((jsonObj.get("openTextField") != null && !jsonObj.get("openTextField").isJsonNull()) && !jsonObj.get("openTextField").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `openTextField` to be a primitive type in the JSON string but got `%s`", jsonObj.get("openTextField").toString()));
      }
      if ((jsonObj.get("orderFormId") != null && !jsonObj.get("orderFormId").isJsonNull()) && !jsonObj.get("orderFormId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderFormId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderFormId").toString()));
      }
      // validate the optional field `paymentData`
      if (jsonObj.get("paymentData") != null && !jsonObj.get("paymentData").isJsonNull()) {
        AddCoupons200ResponsePaymentData.validateJsonElement(jsonObj.get("paymentData"));
      }
      if ((jsonObj.get("profileProvider") != null && !jsonObj.get("profileProvider").isJsonNull()) && !jsonObj.get("profileProvider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profileProvider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profileProvider").toString()));
      }
      // validate the optional field `ratesAndBenefitsData`
      if (jsonObj.get("ratesAndBenefitsData") != null && !jsonObj.get("ratesAndBenefitsData").isJsonNull()) {
        AddCoupons200ResponseRatesAndBenefitsData.validateJsonElement(jsonObj.get("ratesAndBenefitsData"));
      }
      if ((jsonObj.get("salesChannel") != null && !jsonObj.get("salesChannel").isJsonNull()) && !jsonObj.get("salesChannel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `salesChannel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("salesChannel").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("selectableGifts") != null && !jsonObj.get("selectableGifts").isJsonNull() && !jsonObj.get("selectableGifts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `selectableGifts` to be an array in the JSON string but got `%s`", jsonObj.get("selectableGifts").toString()));
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
      if ((jsonObj.get("storeId") != null && !jsonObj.get("storeId").isJsonNull()) && !jsonObj.get("storeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `storeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("storeId").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("totalizers") != null && !jsonObj.get("totalizers").isJsonNull() && !jsonObj.get("totalizers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `totalizers` to be an array in the JSON string but got `%s`", jsonObj.get("totalizers").toString()));
      }
      if ((jsonObj.get("userProfileId") != null && !jsonObj.get("userProfileId").isJsonNull()) && !jsonObj.get("userProfileId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userProfileId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userProfileId").toString()));
      }
      if ((jsonObj.get("userType") != null && !jsonObj.get("userType").isJsonNull()) && !jsonObj.get("userType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userType").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Items200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Items200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Items200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Items200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<Items200Response>() {
           @Override
           public void write(JsonWriter out, Items200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Items200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Items200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Items200Response
   * @throws IOException if the JSON string is invalid with respect to Items200Response
   */
  public static Items200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Items200Response.class);
  }

  /**
   * Convert an instance of Items200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

