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
 * PlaceOrderFromExistingOrderFormRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrderFromExistingOrderFormRequest {
  public static final String SERIALIZED_NAME_INTEREST_VALUE = "interestValue";
  @SerializedName(SERIALIZED_NAME_INTEREST_VALUE)
  private Integer interestValue = 0;

  public static final String SERIALIZED_NAME_OPTIN_NEWS_LETTER = "optinNewsLetter";
  @SerializedName(SERIALIZED_NAME_OPTIN_NEWS_LETTER)
  private Boolean optinNewsLetter = false;

  public static final String SERIALIZED_NAME_REFERENCE_ID = "referenceId";
  @SerializedName(SERIALIZED_NAME_REFERENCE_ID)
  private String referenceId = "41a22925298a4ddca95318131a25b000";

  public static final String SERIALIZED_NAME_REFERENCE_VALUE = "referenceValue";
  @SerializedName(SERIALIZED_NAME_REFERENCE_VALUE)
  private Integer referenceValue = 6800;

  public static final String SERIALIZED_NAME_SAVE_PERSONAL_DATA = "savePersonalData";
  @SerializedName(SERIALIZED_NAME_SAVE_PERSONAL_DATA)
  private Boolean savePersonalData = false;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Integer value = 6800;

  public PlaceOrderFromExistingOrderFormRequest() {
  }

  public PlaceOrderFromExistingOrderFormRequest interestValue(Integer interestValue) {
    this.interestValue = interestValue;
    return this;
  }

  /**
   * Interest rate to be used in case it applies.
   * @return interestValue
   */
  @javax.annotation.Nonnull
  public Integer getInterestValue() {
    return interestValue;
  }

  public void setInterestValue(Integer interestValue) {
    this.interestValue = interestValue;
  }


  public PlaceOrderFromExistingOrderFormRequest optinNewsLetter(Boolean optinNewsLetter) {
    this.optinNewsLetter = optinNewsLetter;
    return this;
  }

  /**
   * True if the shopper opted to receive the newsletter.
   * @return optinNewsLetter
   */
  @javax.annotation.Nullable
  public Boolean getOptinNewsLetter() {
    return optinNewsLetter;
  }

  public void setOptinNewsLetter(Boolean optinNewsLetter) {
    this.optinNewsLetter = optinNewsLetter;
  }


  public PlaceOrderFromExistingOrderFormRequest referenceId(String referenceId) {
    this.referenceId = referenceId;
    return this;
  }

  /**
   * ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. This is the same as the &#x60;orderFormId&#x60; parameter.
   * @return referenceId
   */
  @javax.annotation.Nonnull
  public String getReferenceId() {
    return referenceId;
  }

  public void setReferenceId(String referenceId) {
    this.referenceId = referenceId;
  }


  public PlaceOrderFromExistingOrderFormRequest referenceValue(Integer referenceValue) {
    this.referenceValue = referenceValue;
    return this;
  }

  /**
   * Reference value of the order for calculating interest if that is the case. Can be equal to the total value and does not separate cents. For example, $24.99 is represented &#x60;2499&#x60;.
   * @return referenceValue
   */
  @javax.annotation.Nonnull
  public Integer getReferenceValue() {
    return referenceValue;
  }

  public void setReferenceValue(Integer referenceValue) {
    this.referenceValue = referenceValue;
  }


  public PlaceOrderFromExistingOrderFormRequest savePersonalData(Boolean savePersonalData) {
    this.savePersonalData = savePersonalData;
    return this;
  }

  /**
   * &#x60;true&#x60; if the shopper&#39;s data provided during checkout should be saved for future reference.
   * @return savePersonalData
   */
  @javax.annotation.Nullable
  public Boolean getSavePersonalData() {
    return savePersonalData;
  }

  public void setSavePersonalData(Boolean savePersonalData) {
    this.savePersonalData = savePersonalData;
  }


  public PlaceOrderFromExistingOrderFormRequest value(Integer value) {
    this.value = value;
    return this;
  }

  /**
   * Total value of the order without separating cents. For example, $24.99 is represented &#x60;2499&#x60;.
   * @return value
   */
  @javax.annotation.Nonnull
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
    PlaceOrderFromExistingOrderFormRequest placeOrderFromExistingOrderFormRequest = (PlaceOrderFromExistingOrderFormRequest) o;
    return Objects.equals(this.interestValue, placeOrderFromExistingOrderFormRequest.interestValue) &&
        Objects.equals(this.optinNewsLetter, placeOrderFromExistingOrderFormRequest.optinNewsLetter) &&
        Objects.equals(this.referenceId, placeOrderFromExistingOrderFormRequest.referenceId) &&
        Objects.equals(this.referenceValue, placeOrderFromExistingOrderFormRequest.referenceValue) &&
        Objects.equals(this.savePersonalData, placeOrderFromExistingOrderFormRequest.savePersonalData) &&
        Objects.equals(this.value, placeOrderFromExistingOrderFormRequest.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(interestValue, optinNewsLetter, referenceId, referenceValue, savePersonalData, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrderFromExistingOrderFormRequest {\n");
    sb.append("    interestValue: ").append(toIndentedString(interestValue)).append("\n");
    sb.append("    optinNewsLetter: ").append(toIndentedString(optinNewsLetter)).append("\n");
    sb.append("    referenceId: ").append(toIndentedString(referenceId)).append("\n");
    sb.append("    referenceValue: ").append(toIndentedString(referenceValue)).append("\n");
    sb.append("    savePersonalData: ").append(toIndentedString(savePersonalData)).append("\n");
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
    openapiFields.add("interestValue");
    openapiFields.add("optinNewsLetter");
    openapiFields.add("referenceId");
    openapiFields.add("referenceValue");
    openapiFields.add("savePersonalData");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("interestValue");
    openapiRequiredFields.add("referenceId");
    openapiRequiredFields.add("referenceValue");
    openapiRequiredFields.add("value");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrderFromExistingOrderFormRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrderFromExistingOrderFormRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrderFromExistingOrderFormRequest is not found in the empty JSON string", PlaceOrderFromExistingOrderFormRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrderFromExistingOrderFormRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrderFromExistingOrderFormRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PlaceOrderFromExistingOrderFormRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("referenceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referenceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referenceId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrderFromExistingOrderFormRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrderFromExistingOrderFormRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrderFromExistingOrderFormRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrderFromExistingOrderFormRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrderFromExistingOrderFormRequest>() {
           @Override
           public void write(JsonWriter out, PlaceOrderFromExistingOrderFormRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrderFromExistingOrderFormRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrderFromExistingOrderFormRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrderFromExistingOrderFormRequest
   * @throws IOException if the JSON string is invalid with respect to PlaceOrderFromExistingOrderFormRequest
   */
  public static PlaceOrderFromExistingOrderFormRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrderFromExistingOrderFormRequest.class);
  }

  /**
   * Convert an instance of PlaceOrderFromExistingOrderFormRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

