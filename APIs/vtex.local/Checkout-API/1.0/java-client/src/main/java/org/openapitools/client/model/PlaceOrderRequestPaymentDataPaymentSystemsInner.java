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
import org.openapitools.client.model.PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator;

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
 * PlaceOrderRequestPaymentDataPaymentSystemsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaceOrderRequestPaymentDataPaymentSystemsInner {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description = "description-example";

  public static final String SERIALIZED_NAME_GROUP_NAME = "groupName";
  @SerializedName(SERIALIZED_NAME_GROUP_NAME)
  private String groupName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_CUSTOM = "isCustom";
  @SerializedName(SERIALIZED_NAME_IS_CUSTOM)
  private Boolean isCustom = false;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_REQUIRES_DOCUMENT = "requiresDocument";
  @SerializedName(SERIALIZED_NAME_REQUIRES_DOCUMENT)
  private Boolean requiresDocument = false;

  public static final String SERIALIZED_NAME_SELECTED = "selected";
  @SerializedName(SERIALIZED_NAME_SELECTED)
  private Boolean selected = false;

  public static final String SERIALIZED_NAME_STRING_ID = "stringId";
  @SerializedName(SERIALIZED_NAME_STRING_ID)
  private String stringId = "12345abc";

  public static final String SERIALIZED_NAME_TEMPLATE = "template";
  @SerializedName(SERIALIZED_NAME_TEMPLATE)
  private String template = "creditCardPaymentGroup-template";

  public static final String SERIALIZED_NAME_VALIDATOR = "validator";
  @SerializedName(SERIALIZED_NAME_VALIDATOR)
  private PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator validator;

  public PlaceOrderRequestPaymentDataPaymentSystemsInner() {
  }

  public PlaceOrderRequestPaymentDataPaymentSystemsInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner groupName(String groupName) {
    this.groupName = groupName;
    return this;
  }

  /**
   * Payment group name.
   * @return groupName
   */
  @javax.annotation.Nullable
  public String getGroupName() {
    return groupName;
  }

  public void setGroupName(String groupName) {
    this.groupName = groupName;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Payment system ID.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner isCustom(Boolean isCustom) {
    this.isCustom = isCustom;
    return this;
  }

  /**
   * Indicates whether it is custom.
   * @return isCustom
   */
  @javax.annotation.Nullable
  public Boolean getIsCustom() {
    return isCustom;
  }

  public void setIsCustom(Boolean isCustom) {
    this.isCustom = isCustom;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Payment system name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner requiresDocument(Boolean requiresDocument) {
    this.requiresDocument = requiresDocument;
    return this;
  }

  /**
   * Indicates whether a document is required.
   * @return requiresDocument
   */
  @javax.annotation.Nullable
  public Boolean getRequiresDocument() {
    return requiresDocument;
  }

  public void setRequiresDocument(Boolean requiresDocument) {
    this.requiresDocument = requiresDocument;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner selected(Boolean selected) {
    this.selected = selected;
    return this;
  }

  /**
   * Indicates whether this payment system has been selected.
   * @return selected
   */
  @javax.annotation.Nullable
  public Boolean getSelected() {
    return selected;
  }

  public void setSelected(Boolean selected) {
    this.selected = selected;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner stringId(String stringId) {
    this.stringId = stringId;
    return this;
  }

  /**
   * String ID.
   * @return stringId
   */
  @javax.annotation.Nullable
  public String getStringId() {
    return stringId;
  }

  public void setStringId(String stringId) {
    this.stringId = stringId;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner template(String template) {
    this.template = template;
    return this;
  }

  /**
   * Template.
   * @return template
   */
  @javax.annotation.Nullable
  public String getTemplate() {
    return template;
  }

  public void setTemplate(String template) {
    this.template = template;
  }


  public PlaceOrderRequestPaymentDataPaymentSystemsInner validator(PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator validator) {
    this.validator = validator;
    return this;
  }

  /**
   * Get validator
   * @return validator
   */
  @javax.annotation.Nullable
  public PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator getValidator() {
    return validator;
  }

  public void setValidator(PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator validator) {
    this.validator = validator;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaceOrderRequestPaymentDataPaymentSystemsInner placeOrderRequestPaymentDataPaymentSystemsInner = (PlaceOrderRequestPaymentDataPaymentSystemsInner) o;
    return Objects.equals(this.description, placeOrderRequestPaymentDataPaymentSystemsInner.description) &&
        Objects.equals(this.groupName, placeOrderRequestPaymentDataPaymentSystemsInner.groupName) &&
        Objects.equals(this.id, placeOrderRequestPaymentDataPaymentSystemsInner.id) &&
        Objects.equals(this.isCustom, placeOrderRequestPaymentDataPaymentSystemsInner.isCustom) &&
        Objects.equals(this.name, placeOrderRequestPaymentDataPaymentSystemsInner.name) &&
        Objects.equals(this.requiresDocument, placeOrderRequestPaymentDataPaymentSystemsInner.requiresDocument) &&
        Objects.equals(this.selected, placeOrderRequestPaymentDataPaymentSystemsInner.selected) &&
        Objects.equals(this.stringId, placeOrderRequestPaymentDataPaymentSystemsInner.stringId) &&
        Objects.equals(this.template, placeOrderRequestPaymentDataPaymentSystemsInner.template) &&
        Objects.equals(this.validator, placeOrderRequestPaymentDataPaymentSystemsInner.validator);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, groupName, id, isCustom, name, requiresDocument, selected, stringId, template, validator);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaceOrderRequestPaymentDataPaymentSystemsInner {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    groupName: ").append(toIndentedString(groupName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isCustom: ").append(toIndentedString(isCustom)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    requiresDocument: ").append(toIndentedString(requiresDocument)).append("\n");
    sb.append("    selected: ").append(toIndentedString(selected)).append("\n");
    sb.append("    stringId: ").append(toIndentedString(stringId)).append("\n");
    sb.append("    template: ").append(toIndentedString(template)).append("\n");
    sb.append("    validator: ").append(toIndentedString(validator)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("groupName");
    openapiFields.add("id");
    openapiFields.add("isCustom");
    openapiFields.add("name");
    openapiFields.add("requiresDocument");
    openapiFields.add("selected");
    openapiFields.add("stringId");
    openapiFields.add("template");
    openapiFields.add("validator");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaceOrderRequestPaymentDataPaymentSystemsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaceOrderRequestPaymentDataPaymentSystemsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaceOrderRequestPaymentDataPaymentSystemsInner is not found in the empty JSON string", PlaceOrderRequestPaymentDataPaymentSystemsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaceOrderRequestPaymentDataPaymentSystemsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaceOrderRequestPaymentDataPaymentSystemsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("groupName") != null && !jsonObj.get("groupName").isJsonNull()) && !jsonObj.get("groupName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupName").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("stringId") != null && !jsonObj.get("stringId").isJsonNull()) && !jsonObj.get("stringId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `stringId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("stringId").toString()));
      }
      if ((jsonObj.get("template") != null && !jsonObj.get("template").isJsonNull()) && !jsonObj.get("template").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `template` to be a primitive type in the JSON string but got `%s`", jsonObj.get("template").toString()));
      }
      // validate the optional field `validator`
      if (jsonObj.get("validator") != null && !jsonObj.get("validator").isJsonNull()) {
        PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.validateJsonElement(jsonObj.get("validator"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaceOrderRequestPaymentDataPaymentSystemsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaceOrderRequestPaymentDataPaymentSystemsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaceOrderRequestPaymentDataPaymentSystemsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaceOrderRequestPaymentDataPaymentSystemsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaceOrderRequestPaymentDataPaymentSystemsInner>() {
           @Override
           public void write(JsonWriter out, PlaceOrderRequestPaymentDataPaymentSystemsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaceOrderRequestPaymentDataPaymentSystemsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaceOrderRequestPaymentDataPaymentSystemsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaceOrderRequestPaymentDataPaymentSystemsInner
   * @throws IOException if the JSON string is invalid with respect to PlaceOrderRequestPaymentDataPaymentSystemsInner
   */
  public static PlaceOrderRequestPaymentDataPaymentSystemsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaceOrderRequestPaymentDataPaymentSystemsInner.class);
  }

  /**
   * Convert an instance of PlaceOrderRequestPaymentDataPaymentSystemsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

