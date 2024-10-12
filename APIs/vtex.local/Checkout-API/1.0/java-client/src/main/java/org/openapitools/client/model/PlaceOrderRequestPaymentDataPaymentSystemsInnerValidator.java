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
 * Payment system validator.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator {
  public static final String SERIALIZED_NAME_CARD_CODE_MASK = "cardCodeMask";
  @SerializedName(SERIALIZED_NAME_CARD_CODE_MASK)
  private String cardCodeMask;

  public static final String SERIALIZED_NAME_CARD_CODE_REGEX = "cardCodeRegex";
  @SerializedName(SERIALIZED_NAME_CARD_CODE_REGEX)
  private String cardCodeRegex;

  public static final String SERIALIZED_NAME_MASK = "mask";
  @SerializedName(SERIALIZED_NAME_MASK)
  private String mask;

  public static final String SERIALIZED_NAME_REGEX = "regex";
  @SerializedName(SERIALIZED_NAME_REGEX)
  private String regex;

  public static final String SERIALIZED_NAME_WEIGHTS = "weights";
  @SerializedName(SERIALIZED_NAME_WEIGHTS)
  private List<Integer> weights = new ArrayList<>(Arrays.asList(2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2));

  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator() {
  }

  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator cardCodeMask(String cardCodeMask) {
    this.cardCodeMask = cardCodeMask;
    return this;
  }

  /**
   * Card code mask.
   * @return cardCodeMask
   */
  @javax.annotation.Nullable
  public String getCardCodeMask() {
    return cardCodeMask;
  }

  public void setCardCodeMask(String cardCodeMask) {
    this.cardCodeMask = cardCodeMask;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator cardCodeRegex(String cardCodeRegex) {
    this.cardCodeRegex = cardCodeRegex;
    return this;
  }

  /**
   * Card code regular expression.
   * @return cardCodeRegex
   */
  @javax.annotation.Nullable
  public String getCardCodeRegex() {
    return cardCodeRegex;
  }

  public void setCardCodeRegex(String cardCodeRegex) {
    this.cardCodeRegex = cardCodeRegex;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator mask(String mask) {
    this.mask = mask;
    return this;
  }

  /**
   * Validator mask.
   * @return mask
   */
  @javax.annotation.Nullable
  public String getMask() {
    return mask;
  }

  public void setMask(String mask) {
    this.mask = mask;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator regex(String regex) {
    this.regex = regex;
    return this;
  }

  /**
   * 
   * @return regex
   */
  @javax.annotation.Nullable
  public String getRegex() {
    return regex;
  }

  public void setRegex(String regex) {
    this.regex = regex;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator weights(List<Integer> weights) {
    this.weights = weights;
    return this;
  }

  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator addWeightsItem(Integer weightsItem) {
    if (this.weights == null) {
      this.weights = new ArrayList<>(Arrays.asList(2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2));
    }
    this.weights.add(weightsItem);
    return this;
  }

  /**
   * Weights.
   * @return weights
   */
  @javax.annotation.Nullable
  public List<Integer> getWeights() {
    return weights;
  }

  public void setWeights(List<Integer> weights) {
    this.weights = weights;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator placeOrderRequestPaymentDataPaymentSystemsInnerValidator = (PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator) o;
    return Objects.equals(this.cardCodeMask, placeOrderRequestPaymentDataPaymentSystemsInnerValidator.cardCodeMask) &&
        Objects.equals(this.cardCodeRegex, placeOrderRequestPaymentDataPaymentSystemsInnerValidator.cardCodeRegex) &&
        Objects.equals(this.mask, placeOrderRequestPaymentDataPaymentSystemsInnerValidator.mask) &&
        Objects.equals(this.regex, placeOrderRequestPaymentDataPaymentSystemsInnerValidator.regex) &&
        Objects.equals(this.weights, placeOrderRequestPaymentDataPaymentSystemsInnerValidator.weights);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cardCodeMask, cardCodeRegex, mask, regex, weights);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator {\n");
    sb.append("    cardCodeMask: ").append(toIndentedString(cardCodeMask)).append("\n");
    sb.append("    cardCodeRegex: ").append(toIndentedString(cardCodeRegex)).append("\n");
    sb.append("    mask: ").append(toIndentedString(mask)).append("\n");
    sb.append("    regex: ").append(toIndentedString(regex)).append("\n");
    sb.append("    weights: ").append(toIndentedString(weights)).append("\n");
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
    openapiFields.add("cardCodeMask");
    openapiFields.add("cardCodeRegex");
    openapiFields.add("mask");
    openapiFields.add("regex");
    openapiFields.add("weights");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator is not found in the empty JSON string", PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("cardCodeMask") != null && !jsonObj.get("cardCodeMask").isJsonNull()) && !jsonObj.get("cardCodeMask").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cardCodeMask` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cardCodeMask").toString()));
      }
      if ((jsonObj.get("cardCodeRegex") != null && !jsonObj.get("cardCodeRegex").isJsonNull()) && !jsonObj.get("cardCodeRegex").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cardCodeRegex` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cardCodeRegex").toString()));
      }
      if ((jsonObj.get("mask") != null && !jsonObj.get("mask").isJsonNull()) && !jsonObj.get("mask").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mask` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mask").toString()));
      }
      if ((jsonObj.get("regex") != null && !jsonObj.get("regex").isJsonNull()) && !jsonObj.get("regex").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `regex` to be a primitive type in the JSON string but got `%s`", jsonObj.get("regex").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("weights") != null && !jsonObj.get("weights").isJsonNull() && !jsonObj.get("weights").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `weights` to be an array in the JSON string but got `%s`", jsonObj.get("weights").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator>() {
           @Override
           public void write(JsonWriter out, PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator
   * @throws IOException if the JSON string is invalid with respect to PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator
   */
  public static PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.class);
  }

  /**
   * Convert an instance of PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

