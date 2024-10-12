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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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
 * AddCoupons200ResponseAvailableAddressesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddCoupons200ResponseAvailableAddressesInner {
  public static final String SERIALIZED_NAME_ADDRESS_ID = "addressId";
  @SerializedName(SERIALIZED_NAME_ADDRESS_ID)
  private String addressId;

  public static final String SERIALIZED_NAME_ADDRESS_TYPE = "addressType";
  @SerializedName(SERIALIZED_NAME_ADDRESS_TYPE)
  private String addressType;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COMPLEMENT = "complement";
  @SerializedName(SERIALIZED_NAME_COMPLEMENT)
  private String complement;

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_GEO_COORDINATES = "geoCoordinates";
  @SerializedName(SERIALIZED_NAME_GEO_COORDINATES)
  private List<BigDecimal> geoCoordinates = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_DISPOSABLE = "isDisposable";
  @SerializedName(SERIALIZED_NAME_IS_DISPOSABLE)
  private Boolean isDisposable;

  public static final String SERIALIZED_NAME_NEIGHBORHOOD = "neighborhood";
  @SerializedName(SERIALIZED_NAME_NEIGHBORHOOD)
  private String neighborhood;

  public static final String SERIALIZED_NAME_NUMBER = "number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private String number;

  public static final String SERIALIZED_NAME_RECEIVER_NAME = "receiverName";
  @SerializedName(SERIALIZED_NAME_RECEIVER_NAME)
  private String receiverName;

  public static final String SERIALIZED_NAME_REFERENCE = "reference";
  @SerializedName(SERIALIZED_NAME_REFERENCE)
  private String reference;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private String state;

  public static final String SERIALIZED_NAME_STREET = "street";
  @SerializedName(SERIALIZED_NAME_STREET)
  private String street;

  public AddCoupons200ResponseAvailableAddressesInner() {
  }

  public AddCoupons200ResponseAvailableAddressesInner addressId(String addressId) {
    this.addressId = addressId;
    return this;
  }

  /**
   * Address ID.
   * @return addressId
   */
  @javax.annotation.Nullable
  public String getAddressId() {
    return addressId;
  }

  public void setAddressId(String addressId) {
    this.addressId = addressId;
  }


  public AddCoupons200ResponseAvailableAddressesInner addressType(String addressType) {
    this.addressType = addressType;
    return this;
  }

  /**
   * Address type.
   * @return addressType
   */
  @javax.annotation.Nullable
  public String getAddressType() {
    return addressType;
  }

  public void setAddressType(String addressType) {
    this.addressType = addressType;
  }


  public AddCoupons200ResponseAvailableAddressesInner city(String city) {
    this.city = city;
    return this;
  }

  /**
   * City of the address.
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public AddCoupons200ResponseAvailableAddressesInner complement(String complement) {
    this.complement = complement;
    return this;
  }

  /**
   * Complement to the address.
   * @return complement
   */
  @javax.annotation.Nullable
  public String getComplement() {
    return complement;
  }

  public void setComplement(String complement) {
    this.complement = complement;
  }


  public AddCoupons200ResponseAvailableAddressesInner country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Country of the address. ISO three-letter code.
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public AddCoupons200ResponseAvailableAddressesInner geoCoordinates(List<BigDecimal> geoCoordinates) {
    this.geoCoordinates = geoCoordinates;
    return this;
  }

  public AddCoupons200ResponseAvailableAddressesInner addGeoCoordinatesItem(BigDecimal geoCoordinatesItem) {
    if (this.geoCoordinates == null) {
      this.geoCoordinates = new ArrayList<>();
    }
    this.geoCoordinates.add(geoCoordinatesItem);
    return this;
  }

  /**
   * Array containing two floats with geocoordinates, first longitude, then latitude.
   * @return geoCoordinates
   */
  @javax.annotation.Nullable
  public List<BigDecimal> getGeoCoordinates() {
    return geoCoordinates;
  }

  public void setGeoCoordinates(List<BigDecimal> geoCoordinates) {
    this.geoCoordinates = geoCoordinates;
  }


  public AddCoupons200ResponseAvailableAddressesInner isDisposable(Boolean isDisposable) {
    this.isDisposable = isDisposable;
    return this;
  }

  /**
   * Indicates whether address is disposable.
   * @return isDisposable
   */
  @javax.annotation.Nullable
  public Boolean getIsDisposable() {
    return isDisposable;
  }

  public void setIsDisposable(Boolean isDisposable) {
    this.isDisposable = isDisposable;
  }


  public AddCoupons200ResponseAvailableAddressesInner neighborhood(String neighborhood) {
    this.neighborhood = neighborhood;
    return this;
  }

  /**
   * Neighborhood of the address.
   * @return neighborhood
   */
  @javax.annotation.Nullable
  public String getNeighborhood() {
    return neighborhood;
  }

  public void setNeighborhood(String neighborhood) {
    this.neighborhood = neighborhood;
  }


  public AddCoupons200ResponseAvailableAddressesInner number(String number) {
    this.number = number;
    return this;
  }

  /**
   * Number of the address.
   * @return number
   */
  @javax.annotation.Nullable
  public String getNumber() {
    return number;
  }

  public void setNumber(String number) {
    this.number = number;
  }


  public AddCoupons200ResponseAvailableAddressesInner receiverName(String receiverName) {
    this.receiverName = receiverName;
    return this;
  }

  /**
   * Name of the receiver.
   * @return receiverName
   */
  @javax.annotation.Nullable
  public String getReceiverName() {
    return receiverName;
  }

  public void setReceiverName(String receiverName) {
    this.receiverName = receiverName;
  }


  public AddCoupons200ResponseAvailableAddressesInner reference(String reference) {
    this.reference = reference;
    return this;
  }

  /**
   * Reference that may help in the location of the address.
   * @return reference
   */
  @javax.annotation.Nullable
  public String getReference() {
    return reference;
  }

  public void setReference(String reference) {
    this.reference = reference;
  }


  public AddCoupons200ResponseAvailableAddressesInner state(String state) {
    this.state = state;
    return this;
  }

  /**
   * State of the address.
   * @return state
   */
  @javax.annotation.Nullable
  public String getState() {
    return state;
  }

  public void setState(String state) {
    this.state = state;
  }


  public AddCoupons200ResponseAvailableAddressesInner street(String street) {
    this.street = street;
    return this;
  }

  /**
   * Street of the address.
   * @return street
   */
  @javax.annotation.Nullable
  public String getStreet() {
    return street;
  }

  public void setStreet(String street) {
    this.street = street;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddCoupons200ResponseAvailableAddressesInner addCoupons200ResponseAvailableAddressesInner = (AddCoupons200ResponseAvailableAddressesInner) o;
    return Objects.equals(this.addressId, addCoupons200ResponseAvailableAddressesInner.addressId) &&
        Objects.equals(this.addressType, addCoupons200ResponseAvailableAddressesInner.addressType) &&
        Objects.equals(this.city, addCoupons200ResponseAvailableAddressesInner.city) &&
        Objects.equals(this.complement, addCoupons200ResponseAvailableAddressesInner.complement) &&
        Objects.equals(this.country, addCoupons200ResponseAvailableAddressesInner.country) &&
        Objects.equals(this.geoCoordinates, addCoupons200ResponseAvailableAddressesInner.geoCoordinates) &&
        Objects.equals(this.isDisposable, addCoupons200ResponseAvailableAddressesInner.isDisposable) &&
        Objects.equals(this.neighborhood, addCoupons200ResponseAvailableAddressesInner.neighborhood) &&
        Objects.equals(this.number, addCoupons200ResponseAvailableAddressesInner.number) &&
        Objects.equals(this.receiverName, addCoupons200ResponseAvailableAddressesInner.receiverName) &&
        Objects.equals(this.reference, addCoupons200ResponseAvailableAddressesInner.reference) &&
        Objects.equals(this.state, addCoupons200ResponseAvailableAddressesInner.state) &&
        Objects.equals(this.street, addCoupons200ResponseAvailableAddressesInner.street);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(addressId, addressType, city, complement, country, geoCoordinates, isDisposable, neighborhood, number, receiverName, reference, state, street);
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
    sb.append("class AddCoupons200ResponseAvailableAddressesInner {\n");
    sb.append("    addressId: ").append(toIndentedString(addressId)).append("\n");
    sb.append("    addressType: ").append(toIndentedString(addressType)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    complement: ").append(toIndentedString(complement)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    geoCoordinates: ").append(toIndentedString(geoCoordinates)).append("\n");
    sb.append("    isDisposable: ").append(toIndentedString(isDisposable)).append("\n");
    sb.append("    neighborhood: ").append(toIndentedString(neighborhood)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    receiverName: ").append(toIndentedString(receiverName)).append("\n");
    sb.append("    reference: ").append(toIndentedString(reference)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    street: ").append(toIndentedString(street)).append("\n");
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
    openapiFields.add("addressId");
    openapiFields.add("addressType");
    openapiFields.add("city");
    openapiFields.add("complement");
    openapiFields.add("country");
    openapiFields.add("geoCoordinates");
    openapiFields.add("isDisposable");
    openapiFields.add("neighborhood");
    openapiFields.add("number");
    openapiFields.add("receiverName");
    openapiFields.add("reference");
    openapiFields.add("state");
    openapiFields.add("street");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddCoupons200ResponseAvailableAddressesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddCoupons200ResponseAvailableAddressesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddCoupons200ResponseAvailableAddressesInner is not found in the empty JSON string", AddCoupons200ResponseAvailableAddressesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddCoupons200ResponseAvailableAddressesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddCoupons200ResponseAvailableAddressesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("addressId") != null && !jsonObj.get("addressId").isJsonNull()) && !jsonObj.get("addressId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `addressId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("addressId").toString()));
      }
      if ((jsonObj.get("addressType") != null && !jsonObj.get("addressType").isJsonNull()) && !jsonObj.get("addressType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `addressType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("addressType").toString()));
      }
      if ((jsonObj.get("city") != null && !jsonObj.get("city").isJsonNull()) && !jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if ((jsonObj.get("complement") != null && !jsonObj.get("complement").isJsonNull()) && !jsonObj.get("complement").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `complement` to be a primitive type in the JSON string but got `%s`", jsonObj.get("complement").toString()));
      }
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("geoCoordinates") != null && !jsonObj.get("geoCoordinates").isJsonNull() && !jsonObj.get("geoCoordinates").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `geoCoordinates` to be an array in the JSON string but got `%s`", jsonObj.get("geoCoordinates").toString()));
      }
      if ((jsonObj.get("neighborhood") != null && !jsonObj.get("neighborhood").isJsonNull()) && !jsonObj.get("neighborhood").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `neighborhood` to be a primitive type in the JSON string but got `%s`", jsonObj.get("neighborhood").toString()));
      }
      if ((jsonObj.get("number") != null && !jsonObj.get("number").isJsonNull()) && !jsonObj.get("number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number").toString()));
      }
      if ((jsonObj.get("receiverName") != null && !jsonObj.get("receiverName").isJsonNull()) && !jsonObj.get("receiverName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `receiverName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("receiverName").toString()));
      }
      if ((jsonObj.get("reference") != null && !jsonObj.get("reference").isJsonNull()) && !jsonObj.get("reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      if ((jsonObj.get("street") != null && !jsonObj.get("street").isJsonNull()) && !jsonObj.get("street").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `street` to be a primitive type in the JSON string but got `%s`", jsonObj.get("street").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddCoupons200ResponseAvailableAddressesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddCoupons200ResponseAvailableAddressesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddCoupons200ResponseAvailableAddressesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddCoupons200ResponseAvailableAddressesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AddCoupons200ResponseAvailableAddressesInner>() {
           @Override
           public void write(JsonWriter out, AddCoupons200ResponseAvailableAddressesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddCoupons200ResponseAvailableAddressesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddCoupons200ResponseAvailableAddressesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddCoupons200ResponseAvailableAddressesInner
   * @throws IOException if the JSON string is invalid with respect to AddCoupons200ResponseAvailableAddressesInner
   */
  public static AddCoupons200ResponseAvailableAddressesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddCoupons200ResponseAvailableAddressesInner.class);
  }

  /**
   * Convert an instance of AddCoupons200ResponseAvailableAddressesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

