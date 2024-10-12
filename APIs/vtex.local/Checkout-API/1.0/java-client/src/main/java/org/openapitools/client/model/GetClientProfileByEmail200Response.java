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
import org.openapitools.client.model.AddCoupons200ResponseAvailableAddressesInner;
import org.openapitools.client.model.GetClientProfileByEmail200ResponseUserProfile;

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
 * GetClientProfileByEmail200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetClientProfileByEmail200Response {
  public static final String SERIALIZED_NAME_AVAILABLE_ACCOUNTS = "availableAccounts";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ACCOUNTS)
  private List<String> availableAccounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_AVAILABLE_ADDRESSES = "availableAddresses";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ADDRESSES)
  private List<AddCoupons200ResponseAvailableAddressesInner> availableAddresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_COMPLETE = "isComplete";
  @SerializedName(SERIALIZED_NAME_IS_COMPLETE)
  private Boolean isComplete;

  public static final String SERIALIZED_NAME_PROFILE_PROVIDER = "profileProvider";
  @SerializedName(SERIALIZED_NAME_PROFILE_PROVIDER)
  private String profileProvider;

  public static final String SERIALIZED_NAME_USER_PROFILE = "userProfile";
  @SerializedName(SERIALIZED_NAME_USER_PROFILE)
  private GetClientProfileByEmail200ResponseUserProfile userProfile;

  public static final String SERIALIZED_NAME_USER_PROFILE_ID = "userProfileId";
  @SerializedName(SERIALIZED_NAME_USER_PROFILE_ID)
  private String userProfileId;

  public GetClientProfileByEmail200Response() {
  }

  public GetClientProfileByEmail200Response availableAccounts(List<String> availableAccounts) {
    this.availableAccounts = availableAccounts;
    return this;
  }

  public GetClientProfileByEmail200Response addAvailableAccountsItem(String availableAccountsItem) {
    if (this.availableAccounts == null) {
      this.availableAccounts = new ArrayList<>();
    }
    this.availableAccounts.add(availableAccountsItem);
    return this;
  }

  /**
   * Available accounts.
   * @return availableAccounts
   */
  @javax.annotation.Nullable
  public List<String> getAvailableAccounts() {
    return availableAccounts;
  }

  public void setAvailableAccounts(List<String> availableAccounts) {
    this.availableAccounts = availableAccounts;
  }


  public GetClientProfileByEmail200Response availableAddresses(List<AddCoupons200ResponseAvailableAddressesInner> availableAddresses) {
    this.availableAddresses = availableAddresses;
    return this;
  }

  public GetClientProfileByEmail200Response addAvailableAddressesItem(AddCoupons200ResponseAvailableAddressesInner availableAddressesItem) {
    if (this.availableAddresses == null) {
      this.availableAddresses = new ArrayList<>();
    }
    this.availableAddresses.add(availableAddressesItem);
    return this;
  }

  /**
   * Information on each available address.
   * @return availableAddresses
   */
  @javax.annotation.Nullable
  public List<AddCoupons200ResponseAvailableAddressesInner> getAvailableAddresses() {
    return availableAddresses;
  }

  public void setAvailableAddresses(List<AddCoupons200ResponseAvailableAddressesInner> availableAddresses) {
    this.availableAddresses = availableAddresses;
  }


  public GetClientProfileByEmail200Response isComplete(Boolean isComplete) {
    this.isComplete = isComplete;
    return this;
  }

  /**
   * Indicates whether customer profile is complete.
   * @return isComplete
   */
  @javax.annotation.Nullable
  public Boolean getIsComplete() {
    return isComplete;
  }

  public void setIsComplete(Boolean isComplete) {
    this.isComplete = isComplete;
  }


  public GetClientProfileByEmail200Response profileProvider(String profileProvider) {
    this.profileProvider = profileProvider;
    return this;
  }

  /**
   * Profile provider.
   * @return profileProvider
   */
  @javax.annotation.Nullable
  public String getProfileProvider() {
    return profileProvider;
  }

  public void setProfileProvider(String profileProvider) {
    this.profileProvider = profileProvider;
  }


  public GetClientProfileByEmail200Response userProfile(GetClientProfileByEmail200ResponseUserProfile userProfile) {
    this.userProfile = userProfile;
    return this;
  }

  /**
   * Get userProfile
   * @return userProfile
   */
  @javax.annotation.Nullable
  public GetClientProfileByEmail200ResponseUserProfile getUserProfile() {
    return userProfile;
  }

  public void setUserProfile(GetClientProfileByEmail200ResponseUserProfile userProfile) {
    this.userProfile = userProfile;
  }


  public GetClientProfileByEmail200Response userProfileId(String userProfileId) {
    this.userProfileId = userProfileId;
    return this;
  }

  /**
   * Unique ID associated with the customer profile.
   * @return userProfileId
   */
  @javax.annotation.Nullable
  public String getUserProfileId() {
    return userProfileId;
  }

  public void setUserProfileId(String userProfileId) {
    this.userProfileId = userProfileId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetClientProfileByEmail200Response getClientProfileByEmail200Response = (GetClientProfileByEmail200Response) o;
    return Objects.equals(this.availableAccounts, getClientProfileByEmail200Response.availableAccounts) &&
        Objects.equals(this.availableAddresses, getClientProfileByEmail200Response.availableAddresses) &&
        Objects.equals(this.isComplete, getClientProfileByEmail200Response.isComplete) &&
        Objects.equals(this.profileProvider, getClientProfileByEmail200Response.profileProvider) &&
        Objects.equals(this.userProfile, getClientProfileByEmail200Response.userProfile) &&
        Objects.equals(this.userProfileId, getClientProfileByEmail200Response.userProfileId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(availableAccounts, availableAddresses, isComplete, profileProvider, userProfile, userProfileId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetClientProfileByEmail200Response {\n");
    sb.append("    availableAccounts: ").append(toIndentedString(availableAccounts)).append("\n");
    sb.append("    availableAddresses: ").append(toIndentedString(availableAddresses)).append("\n");
    sb.append("    isComplete: ").append(toIndentedString(isComplete)).append("\n");
    sb.append("    profileProvider: ").append(toIndentedString(profileProvider)).append("\n");
    sb.append("    userProfile: ").append(toIndentedString(userProfile)).append("\n");
    sb.append("    userProfileId: ").append(toIndentedString(userProfileId)).append("\n");
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
    openapiFields.add("availableAccounts");
    openapiFields.add("availableAddresses");
    openapiFields.add("isComplete");
    openapiFields.add("profileProvider");
    openapiFields.add("userProfile");
    openapiFields.add("userProfileId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetClientProfileByEmail200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetClientProfileByEmail200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetClientProfileByEmail200Response is not found in the empty JSON string", GetClientProfileByEmail200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetClientProfileByEmail200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetClientProfileByEmail200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("availableAccounts") != null && !jsonObj.get("availableAccounts").isJsonNull() && !jsonObj.get("availableAccounts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `availableAccounts` to be an array in the JSON string but got `%s`", jsonObj.get("availableAccounts").toString()));
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
            AddCoupons200ResponseAvailableAddressesInner.validateJsonElement(jsonArrayavailableAddresses.get(i));
          };
        }
      }
      if ((jsonObj.get("profileProvider") != null && !jsonObj.get("profileProvider").isJsonNull()) && !jsonObj.get("profileProvider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profileProvider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profileProvider").toString()));
      }
      // validate the optional field `userProfile`
      if (jsonObj.get("userProfile") != null && !jsonObj.get("userProfile").isJsonNull()) {
        GetClientProfileByEmail200ResponseUserProfile.validateJsonElement(jsonObj.get("userProfile"));
      }
      if ((jsonObj.get("userProfileId") != null && !jsonObj.get("userProfileId").isJsonNull()) && !jsonObj.get("userProfileId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userProfileId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userProfileId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetClientProfileByEmail200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetClientProfileByEmail200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetClientProfileByEmail200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetClientProfileByEmail200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetClientProfileByEmail200Response>() {
           @Override
           public void write(JsonWriter out, GetClientProfileByEmail200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetClientProfileByEmail200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetClientProfileByEmail200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetClientProfileByEmail200Response
   * @throws IOException if the JSON string is invalid with respect to GetClientProfileByEmail200Response
   */
  public static GetClientProfileByEmail200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetClientProfileByEmail200Response.class);
  }

  /**
   * Convert an instance of GetClientProfileByEmail200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

