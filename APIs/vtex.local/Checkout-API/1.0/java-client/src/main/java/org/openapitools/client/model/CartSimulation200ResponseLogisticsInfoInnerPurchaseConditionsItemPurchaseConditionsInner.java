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
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner;

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
 * CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LIST_PRICE = "listPrice";
  @SerializedName(SERIALIZED_NAME_LIST_PRICE)
  private Integer listPrice;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Integer price;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private String seller;

  public static final String SERIALIZED_NAME_SELLER_CHAIN = "sellerChain";
  @SerializedName(SERIALIZED_NAME_SELLER_CHAIN)
  private List<Object> sellerChain = new ArrayList<>();

  public static final String SERIALIZED_NAME_SLAS = "slas";
  @SerializedName(SERIALIZED_NAME_SLAS)
  private List<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner> slas = new ArrayList<>();

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner() {
  }

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Item ID.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner listPrice(Integer listPrice) {
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


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner price(Integer price) {
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


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner seller(String seller) {
    this.seller = seller;
    return this;
  }

  /**
   * Seller.
   * @return seller
   */
  @javax.annotation.Nullable
  public String getSeller() {
    return seller;
  }

  public void setSeller(String seller) {
    this.seller = seller;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner sellerChain(List<Object> sellerChain) {
    this.sellerChain = sellerChain;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner addSellerChainItem(Object sellerChainItem) {
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
  public List<Object> getSellerChain() {
    return sellerChain;
  }

  public void setSellerChain(List<Object> sellerChain) {
    this.sellerChain = sellerChain;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner slas(List<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner> slas) {
    this.slas = slas;
    return this;
  }

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner addSlasItem(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner slasItem) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner = (CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner) o;
    return Objects.equals(this.id, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.id) &&
        Objects.equals(this.listPrice, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.listPrice) &&
        Objects.equals(this.price, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.price) &&
        Objects.equals(this.seller, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.seller) &&
        Objects.equals(this.sellerChain, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.sellerChain) &&
        Objects.equals(this.slas, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.slas);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, listPrice, price, seller, sellerChain, slas);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    listPrice: ").append(toIndentedString(listPrice)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    sellerChain: ").append(toIndentedString(sellerChain)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("listPrice");
    openapiFields.add("price");
    openapiFields.add("seller");
    openapiFields.add("sellerChain");
    openapiFields.add("slas");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner is not found in the empty JSON string", CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("seller") != null && !jsonObj.get("seller").isJsonNull()) && !jsonObj.get("seller").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `seller` to be a primitive type in the JSON string but got `%s`", jsonObj.get("seller").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("sellerChain") != null && !jsonObj.get("sellerChain").isJsonNull() && !jsonObj.get("sellerChain").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellerChain` to be an array in the JSON string but got `%s`", jsonObj.get("sellerChain").toString()));
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
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner>() {
           @Override
           public void write(JsonWriter out, CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner
   */
  public static CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.class);
  }

  /**
   * Convert an instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

