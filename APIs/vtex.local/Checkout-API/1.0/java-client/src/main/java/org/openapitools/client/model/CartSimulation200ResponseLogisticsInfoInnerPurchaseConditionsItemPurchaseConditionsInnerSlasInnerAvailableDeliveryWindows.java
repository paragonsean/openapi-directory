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
 * This object contains information about the delivery window available to the shopper.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows {
  public static final String SERIALIZED_NAME_END_DATE_UTC = "endDateUtc";
  @SerializedName(SERIALIZED_NAME_END_DATE_UTC)
  private String endDateUtc;

  public static final String SERIALIZED_NAME_LIS_PRICE = "lisPrice";
  @SerializedName(SERIALIZED_NAME_LIS_PRICE)
  private Integer lisPrice;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Integer price;

  public static final String SERIALIZED_NAME_START_DATE_UTC = "startDateUtc";
  @SerializedName(SERIALIZED_NAME_START_DATE_UTC)
  private String startDateUtc;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private Integer tax;

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows() {
  }

  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows endDateUtc(String endDateUtc) {
    this.endDateUtc = endDateUtc;
    return this;
  }

  /**
   * Delivery window ending day and time in UTC.
   * @return endDateUtc
   */
  @javax.annotation.Nullable
  public String getEndDateUtc() {
    return endDateUtc;
  }

  public void setEndDateUtc(String endDateUtc) {
    this.endDateUtc = endDateUtc;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows lisPrice(Integer lisPrice) {
    this.lisPrice = lisPrice;
    return this;
  }

  /**
   * Delivery window list price.
   * @return lisPrice
   */
  @javax.annotation.Nullable
  public Integer getLisPrice() {
    return lisPrice;
  }

  public void setLisPrice(Integer lisPrice) {
    this.lisPrice = lisPrice;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows price(Integer price) {
    this.price = price;
    return this;
  }

  /**
   * Delivery window price.
   * @return price
   */
  @javax.annotation.Nullable
  public Integer getPrice() {
    return price;
  }

  public void setPrice(Integer price) {
    this.price = price;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows startDateUtc(String startDateUtc) {
    this.startDateUtc = startDateUtc;
    return this;
  }

  /**
   * Delivery window starting day and time in UTC.
   * @return startDateUtc
   */
  @javax.annotation.Nullable
  public String getStartDateUtc() {
    return startDateUtc;
  }

  public void setStartDateUtc(String startDateUtc) {
    this.startDateUtc = startDateUtc;
  }


  public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows tax(Integer tax) {
    this.tax = tax;
    return this;
  }

  /**
   * Delivery window tax.
   * @return tax
   */
  @javax.annotation.Nullable
  public Integer getTax() {
    return tax;
  }

  public void setTax(Integer tax) {
    this.tax = tax;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows = (CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows) o;
    return Objects.equals(this.endDateUtc, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.endDateUtc) &&
        Objects.equals(this.lisPrice, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.lisPrice) &&
        Objects.equals(this.price, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.price) &&
        Objects.equals(this.startDateUtc, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.startDateUtc) &&
        Objects.equals(this.tax, cartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.tax);
  }

  @Override
  public int hashCode() {
    return Objects.hash(endDateUtc, lisPrice, price, startDateUtc, tax);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows {\n");
    sb.append("    endDateUtc: ").append(toIndentedString(endDateUtc)).append("\n");
    sb.append("    lisPrice: ").append(toIndentedString(lisPrice)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    startDateUtc: ").append(toIndentedString(startDateUtc)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
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
    openapiFields.add("endDateUtc");
    openapiFields.add("lisPrice");
    openapiFields.add("price");
    openapiFields.add("startDateUtc");
    openapiFields.add("tax");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows is not found in the empty JSON string", CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("endDateUtc") != null && !jsonObj.get("endDateUtc").isJsonNull()) && !jsonObj.get("endDateUtc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endDateUtc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endDateUtc").toString()));
      }
      if ((jsonObj.get("startDateUtc") != null && !jsonObj.get("startDateUtc").isJsonNull()) && !jsonObj.get("startDateUtc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `startDateUtc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("startDateUtc").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows>() {
           @Override
           public void write(JsonWriter out, CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows
   */
  public static CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.class);
  }

  /**
   * Convert an instance of CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

