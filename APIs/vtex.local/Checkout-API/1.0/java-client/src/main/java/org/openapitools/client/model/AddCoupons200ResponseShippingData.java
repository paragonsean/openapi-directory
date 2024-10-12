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
import org.openapitools.client.model.AddCoupons200ResponseShippingDataAddress;
import org.openapitools.client.model.AddCoupons200ResponseShippingDataAvailableAddressesInner;
import org.openapitools.client.model.AddCoupons200ResponseShippingDataLogisticsInfoInner;

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
 * Shipping information pertinent to the order.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddCoupons200ResponseShippingData {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private AddCoupons200ResponseShippingDataAddress address;

  public static final String SERIALIZED_NAME_AVAILABLE_ADDRESSES = "availableAddresses";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ADDRESSES)
  private List<AddCoupons200ResponseShippingDataAvailableAddressesInner> availableAddresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOGISTICS_INFO = "logisticsInfo";
  @SerializedName(SERIALIZED_NAME_LOGISTICS_INFO)
  private List<AddCoupons200ResponseShippingDataLogisticsInfoInner> logisticsInfo = new ArrayList<>();

  public static final String SERIALIZED_NAME_SELECTED_ADDRESSES = "selectedAddresses";
  @SerializedName(SERIALIZED_NAME_SELECTED_ADDRESSES)
  private List<AddCoupons200ResponseShippingDataAvailableAddressesInner> selectedAddresses = new ArrayList<>();

  public AddCoupons200ResponseShippingData() {
  }

  public AddCoupons200ResponseShippingData address(AddCoupons200ResponseShippingDataAddress address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public AddCoupons200ResponseShippingDataAddress getAddress() {
    return address;
  }

  public void setAddress(AddCoupons200ResponseShippingDataAddress address) {
    this.address = address;
  }


  public AddCoupons200ResponseShippingData availableAddresses(List<AddCoupons200ResponseShippingDataAvailableAddressesInner> availableAddresses) {
    this.availableAddresses = availableAddresses;
    return this;
  }

  public AddCoupons200ResponseShippingData addAvailableAddressesItem(AddCoupons200ResponseShippingDataAvailableAddressesInner availableAddressesItem) {
    if (this.availableAddresses == null) {
      this.availableAddresses = new ArrayList<>();
    }
    this.availableAddresses.add(availableAddressesItem);
    return this;
  }

  /**
   * Array with information on the available addresses for the order.
   * @return availableAddresses
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseShippingDataAvailableAddressesInner> getAvailableAddresses() {
    return availableAddresses;
  }

  public void setAvailableAddresses(List<AddCoupons200ResponseShippingDataAvailableAddressesInner> availableAddresses) {
    this.availableAddresses = availableAddresses;
  }


  public AddCoupons200ResponseShippingData logisticsInfo(List<AddCoupons200ResponseShippingDataLogisticsInfoInner> logisticsInfo) {
    this.logisticsInfo = logisticsInfo;
    return this;
  }

  public AddCoupons200ResponseShippingData addLogisticsInfoItem(AddCoupons200ResponseShippingDataLogisticsInfoInner logisticsInfoItem) {
    if (this.logisticsInfo == null) {
      this.logisticsInfo = new ArrayList<>();
    }
    this.logisticsInfo.add(logisticsInfoItem);
    return this;
  }

  /**
   * Array with logistics information. Each object in this array corresponds to an object in the &#x60;items&#x60; array, based on the respective &#x60;itemIndex&#x60;.
   * @return logisticsInfo
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseShippingDataLogisticsInfoInner> getLogisticsInfo() {
    return logisticsInfo;
  }

  public void setLogisticsInfo(List<AddCoupons200ResponseShippingDataLogisticsInfoInner> logisticsInfo) {
    this.logisticsInfo = logisticsInfo;
  }


  public AddCoupons200ResponseShippingData selectedAddresses(List<AddCoupons200ResponseShippingDataAvailableAddressesInner> selectedAddresses) {
    this.selectedAddresses = selectedAddresses;
    return this;
  }

  public AddCoupons200ResponseShippingData addSelectedAddressesItem(AddCoupons200ResponseShippingDataAvailableAddressesInner selectedAddressesItem) {
    if (this.selectedAddresses == null) {
      this.selectedAddresses = new ArrayList<>();
    }
    this.selectedAddresses.add(selectedAddressesItem);
    return this;
  }

  /**
   * Array with information on the selected addresses for the order.
   * @return selectedAddresses
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseShippingDataAvailableAddressesInner> getSelectedAddresses() {
    return selectedAddresses;
  }

  public void setSelectedAddresses(List<AddCoupons200ResponseShippingDataAvailableAddressesInner> selectedAddresses) {
    this.selectedAddresses = selectedAddresses;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddCoupons200ResponseShippingData addCoupons200ResponseShippingData = (AddCoupons200ResponseShippingData) o;
    return Objects.equals(this.address, addCoupons200ResponseShippingData.address) &&
        Objects.equals(this.availableAddresses, addCoupons200ResponseShippingData.availableAddresses) &&
        Objects.equals(this.logisticsInfo, addCoupons200ResponseShippingData.logisticsInfo) &&
        Objects.equals(this.selectedAddresses, addCoupons200ResponseShippingData.selectedAddresses);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, availableAddresses, logisticsInfo, selectedAddresses);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddCoupons200ResponseShippingData {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    availableAddresses: ").append(toIndentedString(availableAddresses)).append("\n");
    sb.append("    logisticsInfo: ").append(toIndentedString(logisticsInfo)).append("\n");
    sb.append("    selectedAddresses: ").append(toIndentedString(selectedAddresses)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("availableAddresses");
    openapiFields.add("logisticsInfo");
    openapiFields.add("selectedAddresses");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddCoupons200ResponseShippingData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddCoupons200ResponseShippingData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddCoupons200ResponseShippingData is not found in the empty JSON string", AddCoupons200ResponseShippingData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddCoupons200ResponseShippingData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddCoupons200ResponseShippingData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `address`
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) {
        AddCoupons200ResponseShippingDataAddress.validateJsonElement(jsonObj.get("address"));
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
            AddCoupons200ResponseShippingDataAvailableAddressesInner.validateJsonElement(jsonArrayavailableAddresses.get(i));
          };
        }
      }
      if (jsonObj.get("logisticsInfo") != null && !jsonObj.get("logisticsInfo").isJsonNull()) {
        JsonArray jsonArraylogisticsInfo = jsonObj.getAsJsonArray("logisticsInfo");
        if (jsonArraylogisticsInfo != null) {
          // ensure the json data is an array
          if (!jsonObj.get("logisticsInfo").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `logisticsInfo` to be an array in the JSON string but got `%s`", jsonObj.get("logisticsInfo").toString()));
          }

          // validate the optional field `logisticsInfo` (array)
          for (int i = 0; i < jsonArraylogisticsInfo.size(); i++) {
            AddCoupons200ResponseShippingDataLogisticsInfoInner.validateJsonElement(jsonArraylogisticsInfo.get(i));
          };
        }
      }
      if (jsonObj.get("selectedAddresses") != null && !jsonObj.get("selectedAddresses").isJsonNull()) {
        JsonArray jsonArrayselectedAddresses = jsonObj.getAsJsonArray("selectedAddresses");
        if (jsonArrayselectedAddresses != null) {
          // ensure the json data is an array
          if (!jsonObj.get("selectedAddresses").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `selectedAddresses` to be an array in the JSON string but got `%s`", jsonObj.get("selectedAddresses").toString()));
          }

          // validate the optional field `selectedAddresses` (array)
          for (int i = 0; i < jsonArrayselectedAddresses.size(); i++) {
            AddCoupons200ResponseShippingDataAvailableAddressesInner.validateJsonElement(jsonArrayselectedAddresses.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddCoupons200ResponseShippingData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddCoupons200ResponseShippingData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddCoupons200ResponseShippingData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddCoupons200ResponseShippingData.class));

       return (TypeAdapter<T>) new TypeAdapter<AddCoupons200ResponseShippingData>() {
           @Override
           public void write(JsonWriter out, AddCoupons200ResponseShippingData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddCoupons200ResponseShippingData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddCoupons200ResponseShippingData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddCoupons200ResponseShippingData
   * @throws IOException if the JSON string is invalid with respect to AddCoupons200ResponseShippingData
   */
  public static AddCoupons200ResponseShippingData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddCoupons200ResponseShippingData.class);
  }

  /**
   * Convert an instance of AddCoupons200ResponseShippingData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

