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
import org.openapitools.client.model.AddMerchantContextDataRequestSalesAssociateData;
import org.openapitools.client.model.PlaceOrderRequestClientProfileData;
import org.openapitools.client.model.PlaceOrderRequestItemsInner;
import org.openapitools.client.model.PlaceOrderRequestMarketingData;
import org.openapitools.client.model.PlaceOrderRequestPaymentData;
import org.openapitools.client.model.PlaceOrderRequestShippingData;

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
 * PlaceOrderRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrderRequest {
  public static final String SERIALIZED_NAME_CLIENT_PROFILE_DATA = "clientProfileData";
  @SerializedName(SERIALIZED_NAME_CLIENT_PROFILE_DATA)
  private PlaceOrderRequestClientProfileData clientProfileData;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<PlaceOrderRequestItemsInner> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_MARKETING_DATA = "marketingData";
  @SerializedName(SERIALIZED_NAME_MARKETING_DATA)
  private PlaceOrderRequestMarketingData marketingData;

  public static final String SERIALIZED_NAME_OPEN_TEXT_FIELD = "openTextField";
  @SerializedName(SERIALIZED_NAME_OPEN_TEXT_FIELD)
  private String openTextField = "open-text-example";

  public static final String SERIALIZED_NAME_PAYMENT_DATA = "paymentData";
  @SerializedName(SERIALIZED_NAME_PAYMENT_DATA)
  private PlaceOrderRequestPaymentData paymentData;

  public static final String SERIALIZED_NAME_SALES_ASSOCIATE_DATA = "salesAssociateData";
  @SerializedName(SERIALIZED_NAME_SALES_ASSOCIATE_DATA)
  private AddMerchantContextDataRequestSalesAssociateData salesAssociateData;

  public static final String SERIALIZED_NAME_SHIPPING_DATA = "shippingData";
  @SerializedName(SERIALIZED_NAME_SHIPPING_DATA)
  private PlaceOrderRequestShippingData shippingData;

  public PlaceOrderRequest() {
  }

  public PlaceOrderRequest clientProfileData(PlaceOrderRequestClientProfileData clientProfileData) {
    this.clientProfileData = clientProfileData;
    return this;
  }

  /**
   * Get clientProfileData
   * @return clientProfileData
   */
  @javax.annotation.Nonnull
  public PlaceOrderRequestClientProfileData getClientProfileData() {
    return clientProfileData;
  }

  public void setClientProfileData(PlaceOrderRequestClientProfileData clientProfileData) {
    this.clientProfileData = clientProfileData;
  }


  public PlaceOrderRequest items(List<PlaceOrderRequestItemsInner> items) {
    this.items = items;
    return this;
  }

  public PlaceOrderRequest addItemsItem(PlaceOrderRequestItemsInner itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Array of objects containing information on each of the order&#39;s items.
   * @return items
   */
  @javax.annotation.Nonnull
  public List<PlaceOrderRequestItemsInner> getItems() {
    return items;
  }

  public void setItems(List<PlaceOrderRequestItemsInner> items) {
    this.items = items;
  }


  public PlaceOrderRequest marketingData(PlaceOrderRequestMarketingData marketingData) {
    this.marketingData = marketingData;
    return this;
  }

  /**
   * Get marketingData
   * @return marketingData
   */
  @javax.annotation.Nullable
  public PlaceOrderRequestMarketingData getMarketingData() {
    return marketingData;
  }

  public void setMarketingData(PlaceOrderRequestMarketingData marketingData) {
    this.marketingData = marketingData;
  }


  public PlaceOrderRequest openTextField(String openTextField) {
    this.openTextField = openTextField;
    return this;
  }

  /**
   * Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as &#x60;JSON&#x60; even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)
   * @return openTextField
   */
  @javax.annotation.Nullable
  public String getOpenTextField() {
    return openTextField;
  }

  public void setOpenTextField(String openTextField) {
    this.openTextField = openTextField;
  }


  public PlaceOrderRequest paymentData(PlaceOrderRequestPaymentData paymentData) {
    this.paymentData = paymentData;
    return this;
  }

  /**
   * Get paymentData
   * @return paymentData
   */
  @javax.annotation.Nonnull
  public PlaceOrderRequestPaymentData getPaymentData() {
    return paymentData;
  }

  public void setPaymentData(PlaceOrderRequestPaymentData paymentData) {
    this.paymentData = paymentData;
  }


  public PlaceOrderRequest salesAssociateData(AddMerchantContextDataRequestSalesAssociateData salesAssociateData) {
    this.salesAssociateData = salesAssociateData;
    return this;
  }

  /**
   * Get salesAssociateData
   * @return salesAssociateData
   */
  @javax.annotation.Nullable
  public AddMerchantContextDataRequestSalesAssociateData getSalesAssociateData() {
    return salesAssociateData;
  }

  public void setSalesAssociateData(AddMerchantContextDataRequestSalesAssociateData salesAssociateData) {
    this.salesAssociateData = salesAssociateData;
  }


  public PlaceOrderRequest shippingData(PlaceOrderRequestShippingData shippingData) {
    this.shippingData = shippingData;
    return this;
  }

  /**
   * Get shippingData
   * @return shippingData
   */
  @javax.annotation.Nonnull
  public PlaceOrderRequestShippingData getShippingData() {
    return shippingData;
  }

  public void setShippingData(PlaceOrderRequestShippingData shippingData) {
    this.shippingData = shippingData;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaceOrderRequest placeOrderRequest = (PlaceOrderRequest) o;
    return Objects.equals(this.clientProfileData, placeOrderRequest.clientProfileData) &&
        Objects.equals(this.items, placeOrderRequest.items) &&
        Objects.equals(this.marketingData, placeOrderRequest.marketingData) &&
        Objects.equals(this.openTextField, placeOrderRequest.openTextField) &&
        Objects.equals(this.paymentData, placeOrderRequest.paymentData) &&
        Objects.equals(this.salesAssociateData, placeOrderRequest.salesAssociateData) &&
        Objects.equals(this.shippingData, placeOrderRequest.shippingData);
  }

  @Override
  public int hashCode() {
    return Objects.hash(clientProfileData, items, marketingData, openTextField, paymentData, salesAssociateData, shippingData);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrderRequest {\n");
    sb.append("    clientProfileData: ").append(toIndentedString(clientProfileData)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    marketingData: ").append(toIndentedString(marketingData)).append("\n");
    sb.append("    openTextField: ").append(toIndentedString(openTextField)).append("\n");
    sb.append("    paymentData: ").append(toIndentedString(paymentData)).append("\n");
    sb.append("    salesAssociateData: ").append(toIndentedString(salesAssociateData)).append("\n");
    sb.append("    shippingData: ").append(toIndentedString(shippingData)).append("\n");
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
    openapiFields.add("clientProfileData");
    openapiFields.add("items");
    openapiFields.add("marketingData");
    openapiFields.add("openTextField");
    openapiFields.add("paymentData");
    openapiFields.add("salesAssociateData");
    openapiFields.add("shippingData");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("clientProfileData");
    openapiRequiredFields.add("items");
    openapiRequiredFields.add("paymentData");
    openapiRequiredFields.add("shippingData");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrderRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrderRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrderRequest is not found in the empty JSON string", PlaceOrderRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrderRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrderRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PlaceOrderRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `clientProfileData`
      PlaceOrderRequestClientProfileData.validateJsonElement(jsonObj.get("clientProfileData"));
      // ensure the json data is an array
      if (!jsonObj.get("items").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
      }

      JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
      // validate the required field `items` (array)
      for (int i = 0; i < jsonArrayitems.size(); i++) {
        PlaceOrderRequestItemsInner.validateJsonElement(jsonArrayitems.get(i));
      };
      // validate the optional field `marketingData`
      if (jsonObj.get("marketingData") != null && !jsonObj.get("marketingData").isJsonNull()) {
        PlaceOrderRequestMarketingData.validateJsonElement(jsonObj.get("marketingData"));
      }
      if ((jsonObj.get("openTextField") != null && !jsonObj.get("openTextField").isJsonNull()) && !jsonObj.get("openTextField").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `openTextField` to be a primitive type in the JSON string but got `%s`", jsonObj.get("openTextField").toString()));
      }
      // validate the required field `paymentData`
      PlaceOrderRequestPaymentData.validateJsonElement(jsonObj.get("paymentData"));
      // validate the optional field `salesAssociateData`
      if (jsonObj.get("salesAssociateData") != null && !jsonObj.get("salesAssociateData").isJsonNull()) {
        AddMerchantContextDataRequestSalesAssociateData.validateJsonElement(jsonObj.get("salesAssociateData"));
      }
      // validate the required field `shippingData`
      PlaceOrderRequestShippingData.validateJsonElement(jsonObj.get("shippingData"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrderRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrderRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrderRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrderRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrderRequest>() {
           @Override
           public void write(JsonWriter out, PlaceOrderRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrderRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrderRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrderRequest
   * @throws IOException if the JSON string is invalid with respect to PlaceOrderRequest
   */
  public static PlaceOrderRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrderRequest.class);
  }

  /**
   * Convert an instance of PlaceOrderRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

