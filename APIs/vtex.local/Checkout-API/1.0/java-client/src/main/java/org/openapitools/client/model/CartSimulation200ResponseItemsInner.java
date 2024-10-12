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
import org.openapitools.client.model.AddCoupons200ResponseItemsInnerPriceDefinition;
import org.openapitools.client.model.CartSimulation200ResponseItemsInnerPriceTagsInner;
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
 * CartSimulation200ResponseItemsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200ResponseItemsInner {
  public static final String SERIALIZED_NAME_AVAILABILITY = "availability";
  @SerializedName(SERIALIZED_NAME_AVAILABILITY)
  private String availability;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LIST_PRICE = "listPrice";
  @SerializedName(SERIALIZED_NAME_LIST_PRICE)
  private Integer listPrice;

  public static final String SERIALIZED_NAME_MEASUREMENT_UNIT = "measurementUnit";
  @SerializedName(SERIALIZED_NAME_MEASUREMENT_UNIT)
  private String measurementUnit;

  public static final String SERIALIZED_NAME_OFFERINGS = "offerings";
  @SerializedName(SERIALIZED_NAME_OFFERINGS)
  private List<Object> offerings = new ArrayList<>();

  public static final String SERIALIZED_NAME_PARENT_ASSEMBLY_BINDING = "parentAssemblyBinding";
  @SerializedName(SERIALIZED_NAME_PARENT_ASSEMBLY_BINDING)
  private String parentAssemblyBinding;

  public static final String SERIALIZED_NAME_PARENT_ITEM_INDEX = "parentItemIndex";
  @SerializedName(SERIALIZED_NAME_PARENT_ITEM_INDEX)
  private Integer parentItemIndex;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Integer price;

  public static final String SERIALIZED_NAME_PRICE_DEFINITION = "priceDefinition";
  @SerializedName(SERIALIZED_NAME_PRICE_DEFINITION)
  private AddCoupons200ResponseItemsInnerPriceDefinition priceDefinition;

  public static final String SERIALIZED_NAME_PRICE_TAGS = "priceTags";
  @SerializedName(SERIALIZED_NAME_PRICE_TAGS)
  private List<CartSimulation200ResponseItemsInnerPriceTagsInner> priceTags = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRICE_VALID_UNTIL = "priceValidUntil";
  @SerializedName(SERIALIZED_NAME_PRICE_VALID_UNTIL)
  private String priceValidUntil;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Integer quantity;

  public static final String SERIALIZED_NAME_REQUEST_INDEX = "requestIndex";
  @SerializedName(SERIALIZED_NAME_REQUEST_INDEX)
  private Integer requestIndex;

  public static final String SERIALIZED_NAME_REWARD_VALUE = "rewardValue";
  @SerializedName(SERIALIZED_NAME_REWARD_VALUE)
  private Integer rewardValue;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private String seller;

  public static final String SERIALIZED_NAME_SELLER_CHAIN = "sellerChain";
  @SerializedName(SERIALIZED_NAME_SELLER_CHAIN)
  private List<String> sellerChain = new ArrayList<>();

  public static final String SERIALIZED_NAME_SELLING_PRICE = "sellingPrice";
  @SerializedName(SERIALIZED_NAME_SELLING_PRICE)
  private Integer sellingPrice;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private Integer tax;

  public static final String SERIALIZED_NAME_UNIT_MULTIPLIER = "unitMultiplier";
  @SerializedName(SERIALIZED_NAME_UNIT_MULTIPLIER)
  private Integer unitMultiplier;

  public CartSimulation200ResponseItemsInner() {
  }

  public CartSimulation200ResponseItemsInner availability(String availability) {
    this.availability = availability;
    return this;
  }

  /**
   * Availability.
   * @return availability
   */
  @javax.annotation.Nullable
  public String getAvailability() {
    return availability;
  }

  public void setAvailability(String availability) {
    this.availability = availability;
  }


  public CartSimulation200ResponseItemsInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * ID of the item.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public CartSimulation200ResponseItemsInner listPrice(Integer listPrice) {
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


  public CartSimulation200ResponseItemsInner measurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
    return this;
  }

  /**
   * Measurement unit.
   * @return measurementUnit
   */
  @javax.annotation.Nullable
  public String getMeasurementUnit() {
    return measurementUnit;
  }

  public void setMeasurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
  }


  public CartSimulation200ResponseItemsInner offerings(List<Object> offerings) {
    this.offerings = offerings;
    return this;
  }

  public CartSimulation200ResponseItemsInner addOfferingsItem(Object offeringsItem) {
    if (this.offerings == null) {
      this.offerings = new ArrayList<>();
    }
    this.offerings.add(offeringsItem);
    return this;
  }

  /**
   * Array containing offering information.
   * @return offerings
   */
  @javax.annotation.Nullable
  public List<Object> getOfferings() {
    return offerings;
  }

  public void setOfferings(List<Object> offerings) {
    this.offerings = offerings;
  }


  public CartSimulation200ResponseItemsInner parentAssemblyBinding(String parentAssemblyBinding) {
    this.parentAssemblyBinding = parentAssemblyBinding;
    return this;
  }

  /**
   * Parent assembly binding.
   * @return parentAssemblyBinding
   */
  @javax.annotation.Nullable
  public String getParentAssemblyBinding() {
    return parentAssemblyBinding;
  }

  public void setParentAssemblyBinding(String parentAssemblyBinding) {
    this.parentAssemblyBinding = parentAssemblyBinding;
  }


  public CartSimulation200ResponseItemsInner parentItemIndex(Integer parentItemIndex) {
    this.parentItemIndex = parentItemIndex;
    return this;
  }

  /**
   * Parent item index.
   * @return parentItemIndex
   */
  @javax.annotation.Nullable
  public Integer getParentItemIndex() {
    return parentItemIndex;
  }

  public void setParentItemIndex(Integer parentItemIndex) {
    this.parentItemIndex = parentItemIndex;
  }


  public CartSimulation200ResponseItemsInner price(Integer price) {
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


  public CartSimulation200ResponseItemsInner priceDefinition(AddCoupons200ResponseItemsInnerPriceDefinition priceDefinition) {
    this.priceDefinition = priceDefinition;
    return this;
  }

  /**
   * Get priceDefinition
   * @return priceDefinition
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponseItemsInnerPriceDefinition getPriceDefinition() {
    return priceDefinition;
  }

  public void setPriceDefinition(AddCoupons200ResponseItemsInnerPriceDefinition priceDefinition) {
    this.priceDefinition = priceDefinition;
  }


  public CartSimulation200ResponseItemsInner priceTags(List<CartSimulation200ResponseItemsInnerPriceTagsInner> priceTags) {
    this.priceTags = priceTags;
    return this;
  }

  public CartSimulation200ResponseItemsInner addPriceTagsItem(CartSimulation200ResponseItemsInnerPriceTagsInner priceTagsItem) {
    if (this.priceTags == null) {
      this.priceTags = new ArrayList<>();
    }
    this.priceTags.add(priceTagsItem);
    return this;
  }

  /**
   * Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.
   * @return priceTags
   */
  @javax.annotation.Nullable
  public List<CartSimulation200ResponseItemsInnerPriceTagsInner> getPriceTags() {
    return priceTags;
  }

  public void setPriceTags(List<CartSimulation200ResponseItemsInnerPriceTagsInner> priceTags) {
    this.priceTags = priceTags;
  }


  public CartSimulation200ResponseItemsInner priceValidUntil(String priceValidUntil) {
    this.priceValidUntil = priceValidUntil;
    return this;
  }

  /**
   * Price expiration date and time.
   * @return priceValidUntil
   */
  @javax.annotation.Nullable
  public String getPriceValidUntil() {
    return priceValidUntil;
  }

  public void setPriceValidUntil(String priceValidUntil) {
    this.priceValidUntil = priceValidUntil;
  }


  public CartSimulation200ResponseItemsInner quantity(Integer quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * The quantity of the item the cart.
   * @return quantity
   */
  @javax.annotation.Nullable
  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }


  public CartSimulation200ResponseItemsInner requestIndex(Integer requestIndex) {
    this.requestIndex = requestIndex;
    return this;
  }

  /**
   * Request index information.
   * @return requestIndex
   */
  @javax.annotation.Nullable
  public Integer getRequestIndex() {
    return requestIndex;
  }

  public void setRequestIndex(Integer requestIndex) {
    this.requestIndex = requestIndex;
  }


  public CartSimulation200ResponseItemsInner rewardValue(Integer rewardValue) {
    this.rewardValue = rewardValue;
    return this;
  }

  /**
   * Reward value in cents.
   * @return rewardValue
   */
  @javax.annotation.Nullable
  public Integer getRewardValue() {
    return rewardValue;
  }

  public void setRewardValue(Integer rewardValue) {
    this.rewardValue = rewardValue;
  }


  public CartSimulation200ResponseItemsInner seller(String seller) {
    this.seller = seller;
    return this;
  }

  /**
   * The seller responsible for the SKU.
   * @return seller
   */
  @javax.annotation.Nullable
  public String getSeller() {
    return seller;
  }

  public void setSeller(String seller) {
    this.seller = seller;
  }


  public CartSimulation200ResponseItemsInner sellerChain(List<String> sellerChain) {
    this.sellerChain = sellerChain;
    return this;
  }

  public CartSimulation200ResponseItemsInner addSellerChainItem(String sellerChainItem) {
    if (this.sellerChain == null) {
      this.sellerChain = new ArrayList<>();
    }
    this.sellerChain.add(sellerChainItem);
    return this;
  }

  /**
   * Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.
   * @return sellerChain
   */
  @javax.annotation.Nullable
  public List<String> getSellerChain() {
    return sellerChain;
  }

  public void setSellerChain(List<String> sellerChain) {
    this.sellerChain = sellerChain;
  }


  public CartSimulation200ResponseItemsInner sellingPrice(Integer sellingPrice) {
    this.sellingPrice = sellingPrice;
    return this;
  }

  /**
   * Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the &#x60;priceDefinition&#x60; data structure instead.
   * @return sellingPrice
   */
  @javax.annotation.Nullable
  public Integer getSellingPrice() {
    return sellingPrice;
  }

  public void setSellingPrice(Integer sellingPrice) {
    this.sellingPrice = sellingPrice;
  }


  public CartSimulation200ResponseItemsInner tax(Integer tax) {
    this.tax = tax;
    return this;
  }

  /**
   * Tax value in cents.
   * @return tax
   */
  @javax.annotation.Nullable
  public Integer getTax() {
    return tax;
  }

  public void setTax(Integer tax) {
    this.tax = tax;
  }


  public CartSimulation200ResponseItemsInner unitMultiplier(Integer unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
    return this;
  }

  /**
   * Unit multiplier.
   * @return unitMultiplier
   */
  @javax.annotation.Nullable
  public Integer getUnitMultiplier() {
    return unitMultiplier;
  }

  public void setUnitMultiplier(Integer unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CartSimulation200ResponseItemsInner cartSimulation200ResponseItemsInner = (CartSimulation200ResponseItemsInner) o;
    return Objects.equals(this.availability, cartSimulation200ResponseItemsInner.availability) &&
        Objects.equals(this.id, cartSimulation200ResponseItemsInner.id) &&
        Objects.equals(this.listPrice, cartSimulation200ResponseItemsInner.listPrice) &&
        Objects.equals(this.measurementUnit, cartSimulation200ResponseItemsInner.measurementUnit) &&
        Objects.equals(this.offerings, cartSimulation200ResponseItemsInner.offerings) &&
        Objects.equals(this.parentAssemblyBinding, cartSimulation200ResponseItemsInner.parentAssemblyBinding) &&
        Objects.equals(this.parentItemIndex, cartSimulation200ResponseItemsInner.parentItemIndex) &&
        Objects.equals(this.price, cartSimulation200ResponseItemsInner.price) &&
        Objects.equals(this.priceDefinition, cartSimulation200ResponseItemsInner.priceDefinition) &&
        Objects.equals(this.priceTags, cartSimulation200ResponseItemsInner.priceTags) &&
        Objects.equals(this.priceValidUntil, cartSimulation200ResponseItemsInner.priceValidUntil) &&
        Objects.equals(this.quantity, cartSimulation200ResponseItemsInner.quantity) &&
        Objects.equals(this.requestIndex, cartSimulation200ResponseItemsInner.requestIndex) &&
        Objects.equals(this.rewardValue, cartSimulation200ResponseItemsInner.rewardValue) &&
        Objects.equals(this.seller, cartSimulation200ResponseItemsInner.seller) &&
        Objects.equals(this.sellerChain, cartSimulation200ResponseItemsInner.sellerChain) &&
        Objects.equals(this.sellingPrice, cartSimulation200ResponseItemsInner.sellingPrice) &&
        Objects.equals(this.tax, cartSimulation200ResponseItemsInner.tax) &&
        Objects.equals(this.unitMultiplier, cartSimulation200ResponseItemsInner.unitMultiplier);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(availability, id, listPrice, measurementUnit, offerings, parentAssemblyBinding, parentItemIndex, price, priceDefinition, priceTags, priceValidUntil, quantity, requestIndex, rewardValue, seller, sellerChain, sellingPrice, tax, unitMultiplier);
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
    sb.append("class CartSimulation200ResponseItemsInner {\n");
    sb.append("    availability: ").append(toIndentedString(availability)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    listPrice: ").append(toIndentedString(listPrice)).append("\n");
    sb.append("    measurementUnit: ").append(toIndentedString(measurementUnit)).append("\n");
    sb.append("    offerings: ").append(toIndentedString(offerings)).append("\n");
    sb.append("    parentAssemblyBinding: ").append(toIndentedString(parentAssemblyBinding)).append("\n");
    sb.append("    parentItemIndex: ").append(toIndentedString(parentItemIndex)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    priceDefinition: ").append(toIndentedString(priceDefinition)).append("\n");
    sb.append("    priceTags: ").append(toIndentedString(priceTags)).append("\n");
    sb.append("    priceValidUntil: ").append(toIndentedString(priceValidUntil)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    requestIndex: ").append(toIndentedString(requestIndex)).append("\n");
    sb.append("    rewardValue: ").append(toIndentedString(rewardValue)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    sellerChain: ").append(toIndentedString(sellerChain)).append("\n");
    sb.append("    sellingPrice: ").append(toIndentedString(sellingPrice)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    unitMultiplier: ").append(toIndentedString(unitMultiplier)).append("\n");
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
    openapiFields.add("availability");
    openapiFields.add("id");
    openapiFields.add("listPrice");
    openapiFields.add("measurementUnit");
    openapiFields.add("offerings");
    openapiFields.add("parentAssemblyBinding");
    openapiFields.add("parentItemIndex");
    openapiFields.add("price");
    openapiFields.add("priceDefinition");
    openapiFields.add("priceTags");
    openapiFields.add("priceValidUntil");
    openapiFields.add("quantity");
    openapiFields.add("requestIndex");
    openapiFields.add("rewardValue");
    openapiFields.add("seller");
    openapiFields.add("sellerChain");
    openapiFields.add("sellingPrice");
    openapiFields.add("tax");
    openapiFields.add("unitMultiplier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200ResponseItemsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200ResponseItemsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200ResponseItemsInner is not found in the empty JSON string", CartSimulation200ResponseItemsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200ResponseItemsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200ResponseItemsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("availability") != null && !jsonObj.get("availability").isJsonNull()) && !jsonObj.get("availability").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `availability` to be a primitive type in the JSON string but got `%s`", jsonObj.get("availability").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("measurementUnit") != null && !jsonObj.get("measurementUnit").isJsonNull()) && !jsonObj.get("measurementUnit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `measurementUnit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("measurementUnit").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("offerings") != null && !jsonObj.get("offerings").isJsonNull() && !jsonObj.get("offerings").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `offerings` to be an array in the JSON string but got `%s`", jsonObj.get("offerings").toString()));
      }
      if ((jsonObj.get("parentAssemblyBinding") != null && !jsonObj.get("parentAssemblyBinding").isJsonNull()) && !jsonObj.get("parentAssemblyBinding").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parentAssemblyBinding` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parentAssemblyBinding").toString()));
      }
      // validate the optional field `priceDefinition`
      if (jsonObj.get("priceDefinition") != null && !jsonObj.get("priceDefinition").isJsonNull()) {
        AddCoupons200ResponseItemsInnerPriceDefinition.validateJsonElement(jsonObj.get("priceDefinition"));
      }
      if (jsonObj.get("priceTags") != null && !jsonObj.get("priceTags").isJsonNull()) {
        JsonArray jsonArraypriceTags = jsonObj.getAsJsonArray("priceTags");
        if (jsonArraypriceTags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("priceTags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `priceTags` to be an array in the JSON string but got `%s`", jsonObj.get("priceTags").toString()));
          }

          // validate the optional field `priceTags` (array)
          for (int i = 0; i < jsonArraypriceTags.size(); i++) {
            CartSimulation200ResponseItemsInnerPriceTagsInner.validateJsonElement(jsonArraypriceTags.get(i));
          };
        }
      }
      if ((jsonObj.get("priceValidUntil") != null && !jsonObj.get("priceValidUntil").isJsonNull()) && !jsonObj.get("priceValidUntil").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `priceValidUntil` to be a primitive type in the JSON string but got `%s`", jsonObj.get("priceValidUntil").toString()));
      }
      if ((jsonObj.get("seller") != null && !jsonObj.get("seller").isJsonNull()) && !jsonObj.get("seller").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `seller` to be a primitive type in the JSON string but got `%s`", jsonObj.get("seller").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("sellerChain") != null && !jsonObj.get("sellerChain").isJsonNull() && !jsonObj.get("sellerChain").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellerChain` to be an array in the JSON string but got `%s`", jsonObj.get("sellerChain").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200ResponseItemsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200ResponseItemsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200ResponseItemsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200ResponseItemsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200ResponseItemsInner>() {
           @Override
           public void write(JsonWriter out, CartSimulation200ResponseItemsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200ResponseItemsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200ResponseItemsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200ResponseItemsInner
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200ResponseItemsInner
   */
  public static CartSimulation200ResponseItemsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200ResponseItemsInner.class);
  }

  /**
   * Convert an instance of CartSimulation200ResponseItemsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

