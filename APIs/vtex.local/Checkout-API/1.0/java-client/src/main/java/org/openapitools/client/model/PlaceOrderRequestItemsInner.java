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
import org.openapitools.client.model.PlaceOrderRequestItemsInnerBundleItemsInner;
import org.openapitools.client.model.PlaceOrderRequestItemsInnerItemAttachment;
import org.openapitools.client.model.PlaceOrderRequestItemsInnerPriceTagsInner;

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
 * PlaceOrderRequestItemsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrderRequestItemsInner {
  public static final String SERIALIZED_NAME_ATTACHMENTS = "attachments";
  @SerializedName(SERIALIZED_NAME_ATTACHMENTS)
  private List<String> attachments = new ArrayList<>();

  public static final String SERIALIZED_NAME_BUNDLE_ITEMS = "bundleItems";
  @SerializedName(SERIALIZED_NAME_BUNDLE_ITEMS)
  private List<PlaceOrderRequestItemsInnerBundleItemsInner> bundleItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_COMMISSION = "commission";
  @SerializedName(SERIALIZED_NAME_COMMISSION)
  private Integer commission;

  public static final String SERIALIZED_NAME_FREIGHT_COMMISSION = "freightCommission";
  @SerializedName(SERIALIZED_NAME_FREIGHT_COMMISSION)
  private Integer freightCommission;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_GIFT = "isGift";
  @SerializedName(SERIALIZED_NAME_IS_GIFT)
  private Boolean isGift = false;

  public static final String SERIALIZED_NAME_ITEM_ATTACHMENT = "itemAttachment";
  @SerializedName(SERIALIZED_NAME_ITEM_ATTACHMENT)
  private PlaceOrderRequestItemsInnerItemAttachment itemAttachment;

  public static final String SERIALIZED_NAME_MEASUREMENT_UNIT = "measurementUnit";
  @SerializedName(SERIALIZED_NAME_MEASUREMENT_UNIT)
  private String measurementUnit = "g";

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Integer price;

  public static final String SERIALIZED_NAME_PRICE_TAGS = "priceTags";
  @SerializedName(SERIALIZED_NAME_PRICE_TAGS)
  private List<PlaceOrderRequestItemsInnerPriceTagsInner> priceTags = new ArrayList<>();

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Integer quantity;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private String seller;

  public static final String SERIALIZED_NAME_UNIT_MULTIPLIER = "unitMultiplier";
  @SerializedName(SERIALIZED_NAME_UNIT_MULTIPLIER)
  private Integer unitMultiplier = 1;

  public PlaceOrderRequestItemsInner() {
  }

  public PlaceOrderRequestItemsInner attachments(List<String> attachments) {
    this.attachments = attachments;
    return this;
  }

  public PlaceOrderRequestItemsInner addAttachmentsItem(String attachmentsItem) {
    if (this.attachments == null) {
      this.attachments = new ArrayList<>();
    }
    this.attachments.add(attachmentsItem);
    return this;
  }

  /**
   * Array containing information on attachments.
   * @return attachments
   */
  @javax.annotation.Nullable
  public List<String> getAttachments() {
    return attachments;
  }

  public void setAttachments(List<String> attachments) {
    this.attachments = attachments;
  }


  public PlaceOrderRequestItemsInner bundleItems(List<PlaceOrderRequestItemsInnerBundleItemsInner> bundleItems) {
    this.bundleItems = bundleItems;
    return this;
  }

  public PlaceOrderRequestItemsInner addBundleItemsItem(PlaceOrderRequestItemsInnerBundleItemsInner bundleItemsItem) {
    if (this.bundleItems == null) {
      this.bundleItems = new ArrayList<>();
    }
    this.bundleItems.add(bundleItemsItem);
    return this;
  }

  /**
   * Information on services sold along with the SKU. Example: a gift package.
   * @return bundleItems
   */
  @javax.annotation.Nullable
  public List<PlaceOrderRequestItemsInnerBundleItemsInner> getBundleItems() {
    return bundleItems;
  }

  public void setBundleItems(List<PlaceOrderRequestItemsInnerBundleItemsInner> bundleItems) {
    this.bundleItems = bundleItems;
  }


  public PlaceOrderRequestItemsInner commission(Integer commission) {
    this.commission = commission;
    return this;
  }

  /**
   * Comission.
   * @return commission
   */
  @javax.annotation.Nullable
  public Integer getCommission() {
    return commission;
  }

  public void setCommission(Integer commission) {
    this.commission = commission;
  }


  public PlaceOrderRequestItemsInner freightCommission(Integer freightCommission) {
    this.freightCommission = freightCommission;
    return this;
  }

  /**
   * Freight comission
   * @return freightCommission
   */
  @javax.annotation.Nullable
  public Integer getFreightCommission() {
    return freightCommission;
  }

  public void setFreightCommission(Integer freightCommission) {
    this.freightCommission = freightCommission;
  }


  public PlaceOrderRequestItemsInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The SKU ID.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public PlaceOrderRequestItemsInner isGift(Boolean isGift) {
    this.isGift = isGift;
    return this;
  }

  /**
   * Indicates whether the order is a gift.
   * @return isGift
   */
  @javax.annotation.Nullable
  public Boolean getIsGift() {
    return isGift;
  }

  public void setIsGift(Boolean isGift) {
    this.isGift = isGift;
  }


  public PlaceOrderRequestItemsInner itemAttachment(PlaceOrderRequestItemsInnerItemAttachment itemAttachment) {
    this.itemAttachment = itemAttachment;
    return this;
  }

  /**
   * Get itemAttachment
   * @return itemAttachment
   */
  @javax.annotation.Nullable
  public PlaceOrderRequestItemsInnerItemAttachment getItemAttachment() {
    return itemAttachment;
  }

  public void setItemAttachment(PlaceOrderRequestItemsInnerItemAttachment itemAttachment) {
    this.itemAttachment = itemAttachment;
  }


  public PlaceOrderRequestItemsInner measurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
    return this;
  }

  /**
   * SKU measurement unit.
   * @return measurementUnit
   */
  @javax.annotation.Nullable
  public String getMeasurementUnit() {
    return measurementUnit;
  }

  public void setMeasurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
  }


  public PlaceOrderRequestItemsInner price(Integer price) {
    this.price = price;
    return this;
  }

  /**
   * Item price within the context of the order without separating cents. For example, $24.99 is represented &#x60;2499&#x60;.
   * @return price
   */
  @javax.annotation.Nullable
  public Integer getPrice() {
    return price;
  }

  public void setPrice(Integer price) {
    this.price = price;
  }


  public PlaceOrderRequestItemsInner priceTags(List<PlaceOrderRequestItemsInnerPriceTagsInner> priceTags) {
    this.priceTags = priceTags;
    return this;
  }

  public PlaceOrderRequestItemsInner addPriceTagsItem(PlaceOrderRequestItemsInnerPriceTagsInner priceTagsItem) {
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
  public List<PlaceOrderRequestItemsInnerPriceTagsInner> getPriceTags() {
    return priceTags;
  }

  public void setPriceTags(List<PlaceOrderRequestItemsInnerPriceTagsInner> priceTags) {
    this.priceTags = priceTags;
  }


  public PlaceOrderRequestItemsInner quantity(Integer quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * The quantity of items of this specific SKU in the cart to be simulated.
   * @return quantity
   */
  @javax.annotation.Nonnull
  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }


  public PlaceOrderRequestItemsInner seller(String seller) {
    this.seller = seller;
    return this;
  }

  /**
   * The ID of the seller responsible for this SKU. This ID can be found in your VTEX Admin.
   * @return seller
   */
  @javax.annotation.Nonnull
  public String getSeller() {
    return seller;
  }

  public void setSeller(String seller) {
    this.seller = seller;
  }


  public PlaceOrderRequestItemsInner unitMultiplier(Integer unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
    return this;
  }

  /**
   * SKU unit multiplier.
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
    PlaceOrderRequestItemsInner placeOrderRequestItemsInner = (PlaceOrderRequestItemsInner) o;
    return Objects.equals(this.attachments, placeOrderRequestItemsInner.attachments) &&
        Objects.equals(this.bundleItems, placeOrderRequestItemsInner.bundleItems) &&
        Objects.equals(this.commission, placeOrderRequestItemsInner.commission) &&
        Objects.equals(this.freightCommission, placeOrderRequestItemsInner.freightCommission) &&
        Objects.equals(this.id, placeOrderRequestItemsInner.id) &&
        Objects.equals(this.isGift, placeOrderRequestItemsInner.isGift) &&
        Objects.equals(this.itemAttachment, placeOrderRequestItemsInner.itemAttachment) &&
        Objects.equals(this.measurementUnit, placeOrderRequestItemsInner.measurementUnit) &&
        Objects.equals(this.price, placeOrderRequestItemsInner.price) &&
        Objects.equals(this.priceTags, placeOrderRequestItemsInner.priceTags) &&
        Objects.equals(this.quantity, placeOrderRequestItemsInner.quantity) &&
        Objects.equals(this.seller, placeOrderRequestItemsInner.seller) &&
        Objects.equals(this.unitMultiplier, placeOrderRequestItemsInner.unitMultiplier);
  }

  @Override
  public int hashCode() {
    return Objects.hash(attachments, bundleItems, commission, freightCommission, id, isGift, itemAttachment, measurementUnit, price, priceTags, quantity, seller, unitMultiplier);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrderRequestItemsInner {\n");
    sb.append("    attachments: ").append(toIndentedString(attachments)).append("\n");
    sb.append("    bundleItems: ").append(toIndentedString(bundleItems)).append("\n");
    sb.append("    commission: ").append(toIndentedString(commission)).append("\n");
    sb.append("    freightCommission: ").append(toIndentedString(freightCommission)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isGift: ").append(toIndentedString(isGift)).append("\n");
    sb.append("    itemAttachment: ").append(toIndentedString(itemAttachment)).append("\n");
    sb.append("    measurementUnit: ").append(toIndentedString(measurementUnit)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    priceTags: ").append(toIndentedString(priceTags)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
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
    openapiFields.add("attachments");
    openapiFields.add("bundleItems");
    openapiFields.add("commission");
    openapiFields.add("freightCommission");
    openapiFields.add("id");
    openapiFields.add("isGift");
    openapiFields.add("itemAttachment");
    openapiFields.add("measurementUnit");
    openapiFields.add("price");
    openapiFields.add("priceTags");
    openapiFields.add("quantity");
    openapiFields.add("seller");
    openapiFields.add("unitMultiplier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("quantity");
    openapiRequiredFields.add("seller");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrderRequestItemsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrderRequestItemsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrderRequestItemsInner is not found in the empty JSON string", PlaceOrderRequestItemsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrderRequestItemsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrderRequestItemsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PlaceOrderRequestItemsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("attachments") != null && !jsonObj.get("attachments").isJsonNull() && !jsonObj.get("attachments").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `attachments` to be an array in the JSON string but got `%s`", jsonObj.get("attachments").toString()));
      }
      if (jsonObj.get("bundleItems") != null && !jsonObj.get("bundleItems").isJsonNull()) {
        JsonArray jsonArraybundleItems = jsonObj.getAsJsonArray("bundleItems");
        if (jsonArraybundleItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("bundleItems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `bundleItems` to be an array in the JSON string but got `%s`", jsonObj.get("bundleItems").toString()));
          }

          // validate the optional field `bundleItems` (array)
          for (int i = 0; i < jsonArraybundleItems.size(); i++) {
            PlaceOrderRequestItemsInnerBundleItemsInner.validateJsonElement(jsonArraybundleItems.get(i));
          };
        }
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `itemAttachment`
      if (jsonObj.get("itemAttachment") != null && !jsonObj.get("itemAttachment").isJsonNull()) {
        PlaceOrderRequestItemsInnerItemAttachment.validateJsonElement(jsonObj.get("itemAttachment"));
      }
      if ((jsonObj.get("measurementUnit") != null && !jsonObj.get("measurementUnit").isJsonNull()) && !jsonObj.get("measurementUnit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `measurementUnit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("measurementUnit").toString()));
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
            PlaceOrderRequestItemsInnerPriceTagsInner.validateJsonElement(jsonArraypriceTags.get(i));
          };
        }
      }
      if (!jsonObj.get("seller").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `seller` to be a primitive type in the JSON string but got `%s`", jsonObj.get("seller").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrderRequestItemsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrderRequestItemsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrderRequestItemsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrderRequestItemsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrderRequestItemsInner>() {
           @Override
           public void write(JsonWriter out, PlaceOrderRequestItemsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrderRequestItemsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrderRequestItemsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrderRequestItemsInner
   * @throws IOException if the JSON string is invalid with respect to PlaceOrderRequestItemsInner
   */
  public static PlaceOrderRequestItemsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrderRequestItemsInner.class);
  }

  /**
   * Convert an instance of PlaceOrderRequestItemsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

