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
 * AddCoupons200ResponseItemMetadataItemsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddCoupons200ResponseItemMetadataItemsInner {
  public static final String SERIALIZED_NAME_DETAIL_URL = "detailUrl";
  @SerializedName(SERIALIZED_NAME_DETAIL_URL)
  private String detailUrl;

  public static final String SERIALIZED_NAME_EAN = "ean";
  @SerializedName(SERIALIZED_NAME_EAN)
  private String ean;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IMAGE_URL = "imageUrl";
  @SerializedName(SERIALIZED_NAME_IMAGE_URL)
  private String imageUrl;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "productId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private String productId;

  public static final String SERIALIZED_NAME_REF_ID = "refId";
  @SerializedName(SERIALIZED_NAME_REF_ID)
  private String refId;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private String seller;

  public static final String SERIALIZED_NAME_SKU_NAME = "skuName";
  @SerializedName(SERIALIZED_NAME_SKU_NAME)
  private String skuName;

  public AddCoupons200ResponseItemMetadataItemsInner() {
  }

  public AddCoupons200ResponseItemMetadataItemsInner detailUrl(String detailUrl) {
    this.detailUrl = detailUrl;
    return this;
  }

  /**
   * Detail URL.
   * @return detailUrl
   */
  @javax.annotation.Nullable
  public String getDetailUrl() {
    return detailUrl;
  }

  public void setDetailUrl(String detailUrl) {
    this.detailUrl = detailUrl;
  }


  public AddCoupons200ResponseItemMetadataItemsInner ean(String ean) {
    this.ean = ean;
    return this;
  }

  /**
   * European Article Number.
   * @return ean
   */
  @javax.annotation.Nullable
  public String getEan() {
    return ean;
  }

  public void setEan(String ean) {
    this.ean = ean;
  }


  public AddCoupons200ResponseItemMetadataItemsInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Item ID.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public AddCoupons200ResponseItemMetadataItemsInner imageUrl(String imageUrl) {
    this.imageUrl = imageUrl;
    return this;
  }

  /**
   * Image URL.
   * @return imageUrl
   */
  @javax.annotation.Nullable
  public String getImageUrl() {
    return imageUrl;
  }

  public void setImageUrl(String imageUrl) {
    this.imageUrl = imageUrl;
  }


  public AddCoupons200ResponseItemMetadataItemsInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Product name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public AddCoupons200ResponseItemMetadataItemsInner productId(String productId) {
    this.productId = productId;
    return this;
  }

  /**
   * Product ID.
   * @return productId
   */
  @javax.annotation.Nullable
  public String getProductId() {
    return productId;
  }

  public void setProductId(String productId) {
    this.productId = productId;
  }


  public AddCoupons200ResponseItemMetadataItemsInner refId(String refId) {
    this.refId = refId;
    return this;
  }

  /**
   * Ref ID.
   * @return refId
   */
  @javax.annotation.Nullable
  public String getRefId() {
    return refId;
  }

  public void setRefId(String refId) {
    this.refId = refId;
  }


  public AddCoupons200ResponseItemMetadataItemsInner seller(String seller) {
    this.seller = seller;
    return this;
  }

  /**
   * Seller.
   * @return seller
   */
  @javax.annotation.Nullable
  public String getSeller() {
    return seller;
  }

  public void setSeller(String seller) {
    this.seller = seller;
  }


  public AddCoupons200ResponseItemMetadataItemsInner skuName(String skuName) {
    this.skuName = skuName;
    return this;
  }

  /**
   * SKU name.
   * @return skuName
   */
  @javax.annotation.Nullable
  public String getSkuName() {
    return skuName;
  }

  public void setSkuName(String skuName) {
    this.skuName = skuName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddCoupons200ResponseItemMetadataItemsInner addCoupons200ResponseItemMetadataItemsInner = (AddCoupons200ResponseItemMetadataItemsInner) o;
    return Objects.equals(this.detailUrl, addCoupons200ResponseItemMetadataItemsInner.detailUrl) &&
        Objects.equals(this.ean, addCoupons200ResponseItemMetadataItemsInner.ean) &&
        Objects.equals(this.id, addCoupons200ResponseItemMetadataItemsInner.id) &&
        Objects.equals(this.imageUrl, addCoupons200ResponseItemMetadataItemsInner.imageUrl) &&
        Objects.equals(this.name, addCoupons200ResponseItemMetadataItemsInner.name) &&
        Objects.equals(this.productId, addCoupons200ResponseItemMetadataItemsInner.productId) &&
        Objects.equals(this.refId, addCoupons200ResponseItemMetadataItemsInner.refId) &&
        Objects.equals(this.seller, addCoupons200ResponseItemMetadataItemsInner.seller) &&
        Objects.equals(this.skuName, addCoupons200ResponseItemMetadataItemsInner.skuName);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(detailUrl, ean, id, imageUrl, name, productId, refId, seller, skuName);
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
    sb.append("class AddCoupons200ResponseItemMetadataItemsInner {\n");
    sb.append("    detailUrl: ").append(toIndentedString(detailUrl)).append("\n");
    sb.append("    ean: ").append(toIndentedString(ean)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    imageUrl: ").append(toIndentedString(imageUrl)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    refId: ").append(toIndentedString(refId)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    skuName: ").append(toIndentedString(skuName)).append("\n");
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
    openapiFields.add("detailUrl");
    openapiFields.add("ean");
    openapiFields.add("id");
    openapiFields.add("imageUrl");
    openapiFields.add("name");
    openapiFields.add("productId");
    openapiFields.add("refId");
    openapiFields.add("seller");
    openapiFields.add("skuName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddCoupons200ResponseItemMetadataItemsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddCoupons200ResponseItemMetadataItemsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddCoupons200ResponseItemMetadataItemsInner is not found in the empty JSON string", AddCoupons200ResponseItemMetadataItemsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddCoupons200ResponseItemMetadataItemsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddCoupons200ResponseItemMetadataItemsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("detailUrl") != null && !jsonObj.get("detailUrl").isJsonNull()) && !jsonObj.get("detailUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `detailUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("detailUrl").toString()));
      }
      if ((jsonObj.get("ean") != null && !jsonObj.get("ean").isJsonNull()) && !jsonObj.get("ean").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ean` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ean").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("imageUrl") != null && !jsonObj.get("imageUrl").isJsonNull()) && !jsonObj.get("imageUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `imageUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("imageUrl").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("productId") != null && !jsonObj.get("productId").isJsonNull()) && !jsonObj.get("productId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `productId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("productId").toString()));
      }
      if ((jsonObj.get("refId") != null && !jsonObj.get("refId").isJsonNull()) && !jsonObj.get("refId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `refId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("refId").toString()));
      }
      if ((jsonObj.get("seller") != null && !jsonObj.get("seller").isJsonNull()) && !jsonObj.get("seller").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `seller` to be a primitive type in the JSON string but got `%s`", jsonObj.get("seller").toString()));
      }
      if ((jsonObj.get("skuName") != null && !jsonObj.get("skuName").isJsonNull()) && !jsonObj.get("skuName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `skuName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("skuName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddCoupons200ResponseItemMetadataItemsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddCoupons200ResponseItemMetadataItemsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddCoupons200ResponseItemMetadataItemsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddCoupons200ResponseItemMetadataItemsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AddCoupons200ResponseItemMetadataItemsInner>() {
           @Override
           public void write(JsonWriter out, AddCoupons200ResponseItemMetadataItemsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddCoupons200ResponseItemMetadataItemsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddCoupons200ResponseItemMetadataItemsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddCoupons200ResponseItemMetadataItemsInner
   * @throws IOException if the JSON string is invalid with respect to AddCoupons200ResponseItemMetadataItemsInner
   */
  public static AddCoupons200ResponseItemMetadataItemsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddCoupons200ResponseItemMetadataItemsInner.class);
  }

  /**
   * Convert an instance of AddCoupons200ResponseItemMetadataItemsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

