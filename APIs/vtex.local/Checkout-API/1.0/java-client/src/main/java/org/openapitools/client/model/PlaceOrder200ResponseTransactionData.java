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
import org.openapitools.client.model.PlaceOrder200ResponseTransactionDataMerchantTransactionsInner;

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
 * Information on each transaction pertinent to the order placed.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrder200ResponseTransactionData {
  public static final String SERIALIZED_NAME_GATEWAY_CALLBACK_TEMPLATE_PATH = "gatewayCallbackTemplatePath";
  @SerializedName(SERIALIZED_NAME_GATEWAY_CALLBACK_TEMPLATE_PATH)
  private String gatewayCallbackTemplatePath;

  public static final String SERIALIZED_NAME_MERCHANT_TRANSACTIONS = "merchantTransactions";
  @SerializedName(SERIALIZED_NAME_MERCHANT_TRANSACTIONS)
  private List<PlaceOrder200ResponseTransactionDataMerchantTransactionsInner> merchantTransactions = new ArrayList<>();

  public static final String SERIALIZED_NAME_RECEIVER_URI = "receiverUri";
  @SerializedName(SERIALIZED_NAME_RECEIVER_URI)
  private String receiverUri;

  public PlaceOrder200ResponseTransactionData() {
  }

  public PlaceOrder200ResponseTransactionData gatewayCallbackTemplatePath(String gatewayCallbackTemplatePath) {
    this.gatewayCallbackTemplatePath = gatewayCallbackTemplatePath;
    return this;
  }

  /**
   * Template of the gateway callback path, which may later be used to send information about the transaction.
   * @return gatewayCallbackTemplatePath
   */
  @javax.annotation.Nullable
  public String getGatewayCallbackTemplatePath() {
    return gatewayCallbackTemplatePath;
  }

  public void setGatewayCallbackTemplatePath(String gatewayCallbackTemplatePath) {
    this.gatewayCallbackTemplatePath = gatewayCallbackTemplatePath;
  }


  public PlaceOrder200ResponseTransactionData merchantTransactions(List<PlaceOrder200ResponseTransactionDataMerchantTransactionsInner> merchantTransactions) {
    this.merchantTransactions = merchantTransactions;
    return this;
  }

  public PlaceOrder200ResponseTransactionData addMerchantTransactionsItem(PlaceOrder200ResponseTransactionDataMerchantTransactionsInner merchantTransactionsItem) {
    if (this.merchantTransactions == null) {
      this.merchantTransactions = new ArrayList<>();
    }
    this.merchantTransactions.add(merchantTransactionsItem);
    return this;
  }

  /**
   * Information on each merchant transaction.
   * @return merchantTransactions
   */
  @javax.annotation.Nullable
  public List<PlaceOrder200ResponseTransactionDataMerchantTransactionsInner> getMerchantTransactions() {
    return merchantTransactions;
  }

  public void setMerchantTransactions(List<PlaceOrder200ResponseTransactionDataMerchantTransactionsInner> merchantTransactions) {
    this.merchantTransactions = merchantTransactions;
  }


  public PlaceOrder200ResponseTransactionData receiverUri(String receiverUri) {
    this.receiverUri = receiverUri;
    return this;
  }

  /**
   * Receiver URI.
   * @return receiverUri
   */
  @javax.annotation.Nullable
  public String getReceiverUri() {
    return receiverUri;
  }

  public void setReceiverUri(String receiverUri) {
    this.receiverUri = receiverUri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaceOrder200ResponseTransactionData placeOrder200ResponseTransactionData = (PlaceOrder200ResponseTransactionData) o;
    return Objects.equals(this.gatewayCallbackTemplatePath, placeOrder200ResponseTransactionData.gatewayCallbackTemplatePath) &&
        Objects.equals(this.merchantTransactions, placeOrder200ResponseTransactionData.merchantTransactions) &&
        Objects.equals(this.receiverUri, placeOrder200ResponseTransactionData.receiverUri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(gatewayCallbackTemplatePath, merchantTransactions, receiverUri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrder200ResponseTransactionData {\n");
    sb.append("    gatewayCallbackTemplatePath: ").append(toIndentedString(gatewayCallbackTemplatePath)).append("\n");
    sb.append("    merchantTransactions: ").append(toIndentedString(merchantTransactions)).append("\n");
    sb.append("    receiverUri: ").append(toIndentedString(receiverUri)).append("\n");
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
    openapiFields.add("gatewayCallbackTemplatePath");
    openapiFields.add("merchantTransactions");
    openapiFields.add("receiverUri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrder200ResponseTransactionData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrder200ResponseTransactionData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrder200ResponseTransactionData is not found in the empty JSON string", PlaceOrder200ResponseTransactionData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrder200ResponseTransactionData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrder200ResponseTransactionData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("gatewayCallbackTemplatePath") != null && !jsonObj.get("gatewayCallbackTemplatePath").isJsonNull()) && !jsonObj.get("gatewayCallbackTemplatePath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gatewayCallbackTemplatePath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gatewayCallbackTemplatePath").toString()));
      }
      if (jsonObj.get("merchantTransactions") != null && !jsonObj.get("merchantTransactions").isJsonNull()) {
        JsonArray jsonArraymerchantTransactions = jsonObj.getAsJsonArray("merchantTransactions");
        if (jsonArraymerchantTransactions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("merchantTransactions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `merchantTransactions` to be an array in the JSON string but got `%s`", jsonObj.get("merchantTransactions").toString()));
          }

          // validate the optional field `merchantTransactions` (array)
          for (int i = 0; i < jsonArraymerchantTransactions.size(); i++) {
            PlaceOrder200ResponseTransactionDataMerchantTransactionsInner.validateJsonElement(jsonArraymerchantTransactions.get(i));
          };
        }
      }
      if ((jsonObj.get("receiverUri") != null && !jsonObj.get("receiverUri").isJsonNull()) && !jsonObj.get("receiverUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `receiverUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("receiverUri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrder200ResponseTransactionData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrder200ResponseTransactionData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrder200ResponseTransactionData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrder200ResponseTransactionData.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrder200ResponseTransactionData>() {
           @Override
           public void write(JsonWriter out, PlaceOrder200ResponseTransactionData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrder200ResponseTransactionData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrder200ResponseTransactionData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrder200ResponseTransactionData
   * @throws IOException if the JSON string is invalid with respect to PlaceOrder200ResponseTransactionData
   */
  public static PlaceOrder200ResponseTransactionData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrder200ResponseTransactionData.class);
  }

  /**
   * Convert an instance of PlaceOrder200ResponseTransactionData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

