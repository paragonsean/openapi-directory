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
 * Information on rates and benefits that apply to the order.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddCoupons200ResponseRatesAndBenefitsData {
  public static final String SERIALIZED_NAME_RATE_AND_BENEFITS_IDENTIFIERS = "rateAndBenefitsIdentifiers";
  @SerializedName(SERIALIZED_NAME_RATE_AND_BENEFITS_IDENTIFIERS)
  private List<String> rateAndBenefitsIdentifiers = new ArrayList<>();

  public static final String SERIALIZED_NAME_TEASER = "teaser";
  @SerializedName(SERIALIZED_NAME_TEASER)
  private List<String> teaser = new ArrayList<>();

  public AddCoupons200ResponseRatesAndBenefitsData() {
  }

  public AddCoupons200ResponseRatesAndBenefitsData rateAndBenefitsIdentifiers(List<String> rateAndBenefitsIdentifiers) {
    this.rateAndBenefitsIdentifiers = rateAndBenefitsIdentifiers;
    return this;
  }

  public AddCoupons200ResponseRatesAndBenefitsData addRateAndBenefitsIdentifiersItem(String rateAndBenefitsIdentifiersItem) {
    if (this.rateAndBenefitsIdentifiers == null) {
      this.rateAndBenefitsIdentifiers = new ArrayList<>();
    }
    this.rateAndBenefitsIdentifiers.add(rateAndBenefitsIdentifiersItem);
    return this;
  }

  /**
   * List with rates and benefits identifiers.
   * @return rateAndBenefitsIdentifiers
   */
  @javax.annotation.Nullable
  public List<String> getRateAndBenefitsIdentifiers() {
    return rateAndBenefitsIdentifiers;
  }

  public void setRateAndBenefitsIdentifiers(List<String> rateAndBenefitsIdentifiers) {
    this.rateAndBenefitsIdentifiers = rateAndBenefitsIdentifiers;
  }


  public AddCoupons200ResponseRatesAndBenefitsData teaser(List<String> teaser) {
    this.teaser = teaser;
    return this;
  }

  public AddCoupons200ResponseRatesAndBenefitsData addTeaserItem(String teaserItem) {
    if (this.teaser == null) {
      this.teaser = new ArrayList<>();
    }
    this.teaser.add(teaserItem);
    return this;
  }

  /**
   * List with rates and benefits teasers.
   * @return teaser
   */
  @javax.annotation.Nullable
  public List<String> getTeaser() {
    return teaser;
  }

  public void setTeaser(List<String> teaser) {
    this.teaser = teaser;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddCoupons200ResponseRatesAndBenefitsData addCoupons200ResponseRatesAndBenefitsData = (AddCoupons200ResponseRatesAndBenefitsData) o;
    return Objects.equals(this.rateAndBenefitsIdentifiers, addCoupons200ResponseRatesAndBenefitsData.rateAndBenefitsIdentifiers) &&
        Objects.equals(this.teaser, addCoupons200ResponseRatesAndBenefitsData.teaser);
  }

  @Override
  public int hashCode() {
    return Objects.hash(rateAndBenefitsIdentifiers, teaser);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddCoupons200ResponseRatesAndBenefitsData {\n");
    sb.append("    rateAndBenefitsIdentifiers: ").append(toIndentedString(rateAndBenefitsIdentifiers)).append("\n");
    sb.append("    teaser: ").append(toIndentedString(teaser)).append("\n");
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
    openapiFields.add("rateAndBenefitsIdentifiers");
    openapiFields.add("teaser");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddCoupons200ResponseRatesAndBenefitsData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddCoupons200ResponseRatesAndBenefitsData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddCoupons200ResponseRatesAndBenefitsData is not found in the empty JSON string", AddCoupons200ResponseRatesAndBenefitsData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddCoupons200ResponseRatesAndBenefitsData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddCoupons200ResponseRatesAndBenefitsData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("rateAndBenefitsIdentifiers") != null && !jsonObj.get("rateAndBenefitsIdentifiers").isJsonNull() && !jsonObj.get("rateAndBenefitsIdentifiers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `rateAndBenefitsIdentifiers` to be an array in the JSON string but got `%s`", jsonObj.get("rateAndBenefitsIdentifiers").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("teaser") != null && !jsonObj.get("teaser").isJsonNull() && !jsonObj.get("teaser").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `teaser` to be an array in the JSON string but got `%s`", jsonObj.get("teaser").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddCoupons200ResponseRatesAndBenefitsData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddCoupons200ResponseRatesAndBenefitsData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddCoupons200ResponseRatesAndBenefitsData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddCoupons200ResponseRatesAndBenefitsData.class));

       return (TypeAdapter<T>) new TypeAdapter<AddCoupons200ResponseRatesAndBenefitsData>() {
           @Override
           public void write(JsonWriter out, AddCoupons200ResponseRatesAndBenefitsData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddCoupons200ResponseRatesAndBenefitsData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddCoupons200ResponseRatesAndBenefitsData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddCoupons200ResponseRatesAndBenefitsData
   * @throws IOException if the JSON string is invalid with respect to AddCoupons200ResponseRatesAndBenefitsData
   */
  public static AddCoupons200ResponseRatesAndBenefitsData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddCoupons200ResponseRatesAndBenefitsData.class);
  }

  /**
   * Convert an instance of AddCoupons200ResponseRatesAndBenefitsData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

