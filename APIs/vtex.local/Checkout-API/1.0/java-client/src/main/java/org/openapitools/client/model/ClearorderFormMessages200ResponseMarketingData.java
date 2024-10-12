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
 * Object containing promotion data such as coupon tracking information and internal or external UTMs.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ClearorderFormMessages200ResponseMarketingData {
  public static final String SERIALIZED_NAME_COUPON = "coupon";
  @SerializedName(SERIALIZED_NAME_COUPON)
  private String coupon = "free-shipping";

  public static final String SERIALIZED_NAME_UTM_CAMPAIGN = "utmCampaign";
  @SerializedName(SERIALIZED_NAME_UTM_CAMPAIGN)
  private String utmCampaign = "Black friday";

  public static final String SERIALIZED_NAME_UTM_MEDIUM = "utmMedium";
  @SerializedName(SERIALIZED_NAME_UTM_MEDIUM)
  private String utmMedium = "CPC";

  public static final String SERIALIZED_NAME_UTM_SOURCE = "utmSource";
  @SerializedName(SERIALIZED_NAME_UTM_SOURCE)
  private String utmSource = "Facebook";

  public static final String SERIALIZED_NAME_UTMI_CAMPAIGN = "utmiCampaign";
  @SerializedName(SERIALIZED_NAME_UTMI_CAMPAIGN)
  private String utmiCampaign = "utmi_campaign-example";

  public static final String SERIALIZED_NAME_UTMI_PAGE = "utmiPage";
  @SerializedName(SERIALIZED_NAME_UTMI_PAGE)
  private String utmiPage = "utmi_page-example";

  public static final String SERIALIZED_NAME_UTMI_PART = "utmiPart";
  @SerializedName(SERIALIZED_NAME_UTMI_PART)
  private String utmiPart = "utmi_part-example";

  public ClearorderFormMessages200ResponseMarketingData() {
  }

  public ClearorderFormMessages200ResponseMarketingData coupon(String coupon) {
    this.coupon = coupon;
    return this;
  }

  /**
   * Sending an existing coupon code in this field will return the corresponding discount in the purchase. Use the [cart simulation](https://developers.vtex.com/vtex-rest-api/reference/orderform#orderformsimulation) request to check which coupons might apply before placing the order.
   * @return coupon
   */
  @javax.annotation.Nullable
  public String getCoupon() {
    return coupon;
  }

  public void setCoupon(String coupon) {
    this.coupon = coupon;
  }


  public ClearorderFormMessages200ResponseMarketingData utmCampaign(String utmCampaign) {
    this.utmCampaign = utmCampaign;
    return this;
  }

  /**
   * UTM campaign
   * @return utmCampaign
   */
  @javax.annotation.Nullable
  public String getUtmCampaign() {
    return utmCampaign;
  }

  public void setUtmCampaign(String utmCampaign) {
    this.utmCampaign = utmCampaign;
  }


  public ClearorderFormMessages200ResponseMarketingData utmMedium(String utmMedium) {
    this.utmMedium = utmMedium;
    return this;
  }

  /**
   * UTM medium.
   * @return utmMedium
   */
  @javax.annotation.Nullable
  public String getUtmMedium() {
    return utmMedium;
  }

  public void setUtmMedium(String utmMedium) {
    this.utmMedium = utmMedium;
  }


  public ClearorderFormMessages200ResponseMarketingData utmSource(String utmSource) {
    this.utmSource = utmSource;
    return this;
  }

  /**
   * UTM source.
   * @return utmSource
   */
  @javax.annotation.Nullable
  public String getUtmSource() {
    return utmSource;
  }

  public void setUtmSource(String utmSource) {
    this.utmSource = utmSource;
  }


  public ClearorderFormMessages200ResponseMarketingData utmiCampaign(String utmiCampaign) {
    this.utmiCampaign = utmiCampaign;
    return this;
  }

  /**
   * utmi_campaign (internal utm).
   * @return utmiCampaign
   */
  @javax.annotation.Nullable
  public String getUtmiCampaign() {
    return utmiCampaign;
  }

  public void setUtmiCampaign(String utmiCampaign) {
    this.utmiCampaign = utmiCampaign;
  }


  public ClearorderFormMessages200ResponseMarketingData utmiPage(String utmiPage) {
    this.utmiPage = utmiPage;
    return this;
  }

  /**
   * utmi_page (internal utm)
   * @return utmiPage
   */
  @javax.annotation.Nullable
  public String getUtmiPage() {
    return utmiPage;
  }

  public void setUtmiPage(String utmiPage) {
    this.utmiPage = utmiPage;
  }


  public ClearorderFormMessages200ResponseMarketingData utmiPart(String utmiPart) {
    this.utmiPart = utmiPart;
    return this;
  }

  /**
   * utmi_part (internal utm).
   * @return utmiPart
   */
  @javax.annotation.Nullable
  public String getUtmiPart() {
    return utmiPart;
  }

  public void setUtmiPart(String utmiPart) {
    this.utmiPart = utmiPart;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ClearorderFormMessages200ResponseMarketingData clearorderFormMessages200ResponseMarketingData = (ClearorderFormMessages200ResponseMarketingData) o;
    return Objects.equals(this.coupon, clearorderFormMessages200ResponseMarketingData.coupon) &&
        Objects.equals(this.utmCampaign, clearorderFormMessages200ResponseMarketingData.utmCampaign) &&
        Objects.equals(this.utmMedium, clearorderFormMessages200ResponseMarketingData.utmMedium) &&
        Objects.equals(this.utmSource, clearorderFormMessages200ResponseMarketingData.utmSource) &&
        Objects.equals(this.utmiCampaign, clearorderFormMessages200ResponseMarketingData.utmiCampaign) &&
        Objects.equals(this.utmiPage, clearorderFormMessages200ResponseMarketingData.utmiPage) &&
        Objects.equals(this.utmiPart, clearorderFormMessages200ResponseMarketingData.utmiPart);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(coupon, utmCampaign, utmMedium, utmSource, utmiCampaign, utmiPage, utmiPart);
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
    sb.append("class ClearorderFormMessages200ResponseMarketingData {\n");
    sb.append("    coupon: ").append(toIndentedString(coupon)).append("\n");
    sb.append("    utmCampaign: ").append(toIndentedString(utmCampaign)).append("\n");
    sb.append("    utmMedium: ").append(toIndentedString(utmMedium)).append("\n");
    sb.append("    utmSource: ").append(toIndentedString(utmSource)).append("\n");
    sb.append("    utmiCampaign: ").append(toIndentedString(utmiCampaign)).append("\n");
    sb.append("    utmiPage: ").append(toIndentedString(utmiPage)).append("\n");
    sb.append("    utmiPart: ").append(toIndentedString(utmiPart)).append("\n");
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
    openapiFields.add("coupon");
    openapiFields.add("utmCampaign");
    openapiFields.add("utmMedium");
    openapiFields.add("utmSource");
    openapiFields.add("utmiCampaign");
    openapiFields.add("utmiPage");
    openapiFields.add("utmiPart");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ClearorderFormMessages200ResponseMarketingData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ClearorderFormMessages200ResponseMarketingData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ClearorderFormMessages200ResponseMarketingData is not found in the empty JSON string", ClearorderFormMessages200ResponseMarketingData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ClearorderFormMessages200ResponseMarketingData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ClearorderFormMessages200ResponseMarketingData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("coupon") != null && !jsonObj.get("coupon").isJsonNull()) && !jsonObj.get("coupon").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `coupon` to be a primitive type in the JSON string but got `%s`", jsonObj.get("coupon").toString()));
      }
      if ((jsonObj.get("utmCampaign") != null && !jsonObj.get("utmCampaign").isJsonNull()) && !jsonObj.get("utmCampaign").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `utmCampaign` to be a primitive type in the JSON string but got `%s`", jsonObj.get("utmCampaign").toString()));
      }
      if ((jsonObj.get("utmMedium") != null && !jsonObj.get("utmMedium").isJsonNull()) && !jsonObj.get("utmMedium").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `utmMedium` to be a primitive type in the JSON string but got `%s`", jsonObj.get("utmMedium").toString()));
      }
      if ((jsonObj.get("utmSource") != null && !jsonObj.get("utmSource").isJsonNull()) && !jsonObj.get("utmSource").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `utmSource` to be a primitive type in the JSON string but got `%s`", jsonObj.get("utmSource").toString()));
      }
      if ((jsonObj.get("utmiCampaign") != null && !jsonObj.get("utmiCampaign").isJsonNull()) && !jsonObj.get("utmiCampaign").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `utmiCampaign` to be a primitive type in the JSON string but got `%s`", jsonObj.get("utmiCampaign").toString()));
      }
      if ((jsonObj.get("utmiPage") != null && !jsonObj.get("utmiPage").isJsonNull()) && !jsonObj.get("utmiPage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `utmiPage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("utmiPage").toString()));
      }
      if ((jsonObj.get("utmiPart") != null && !jsonObj.get("utmiPart").isJsonNull()) && !jsonObj.get("utmiPart").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `utmiPart` to be a primitive type in the JSON string but got `%s`", jsonObj.get("utmiPart").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ClearorderFormMessages200ResponseMarketingData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ClearorderFormMessages200ResponseMarketingData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ClearorderFormMessages200ResponseMarketingData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ClearorderFormMessages200ResponseMarketingData.class));

       return (TypeAdapter<T>) new TypeAdapter<ClearorderFormMessages200ResponseMarketingData>() {
           @Override
           public void write(JsonWriter out, ClearorderFormMessages200ResponseMarketingData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ClearorderFormMessages200ResponseMarketingData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ClearorderFormMessages200ResponseMarketingData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ClearorderFormMessages200ResponseMarketingData
   * @throws IOException if the JSON string is invalid with respect to ClearorderFormMessages200ResponseMarketingData
   */
  public static ClearorderFormMessages200ResponseMarketingData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ClearorderFormMessages200ResponseMarketingData.class);
  }

  /**
   * Convert an instance of ClearorderFormMessages200ResponseMarketingData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

