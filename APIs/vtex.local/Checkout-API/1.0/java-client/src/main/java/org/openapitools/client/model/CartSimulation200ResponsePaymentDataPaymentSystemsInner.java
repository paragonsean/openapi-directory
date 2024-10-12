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
 * CartSimulation200ResponsePaymentDataPaymentSystemsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CartSimulation200ResponsePaymentDataPaymentSystemsInner {
  public static final String SERIALIZED_NAME_AVAILABLE_PAYMENTS = "availablePayments";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_PAYMENTS)
  private String availablePayments;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISPLAY_DOCUMENT = "displayDocument";
  @SerializedName(SERIALIZED_NAME_DISPLAY_DOCUMENT)
  private Boolean displayDocument;

  public static final String SERIALIZED_NAME_DUE_DATE = "dueDate";
  @SerializedName(SERIALIZED_NAME_DUE_DATE)
  private String dueDate;

  public static final String SERIALIZED_NAME_GROUP_NAME = "groupName";
  @SerializedName(SERIALIZED_NAME_GROUP_NAME)
  private String groupName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_CUSTOM = "isCustom";
  @SerializedName(SERIALIZED_NAME_IS_CUSTOM)
  private Boolean isCustom;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_REQUIRES_AUTHENTICATION = "requiresAuthentication";
  @SerializedName(SERIALIZED_NAME_REQUIRES_AUTHENTICATION)
  private Boolean requiresAuthentication;

  public static final String SERIALIZED_NAME_REQUIRES_DOCUMENT = "requiresDocument";
  @SerializedName(SERIALIZED_NAME_REQUIRES_DOCUMENT)
  private Boolean requiresDocument;

  public static final String SERIALIZED_NAME_STRING_ID = "stringId";
  @SerializedName(SERIALIZED_NAME_STRING_ID)
  private String stringId;

  public static final String SERIALIZED_NAME_TEMPLATE = "template";
  @SerializedName(SERIALIZED_NAME_TEMPLATE)
  private String template;

  public static final String SERIALIZED_NAME_VALIDATOR = "validator";
  @SerializedName(SERIALIZED_NAME_VALIDATOR)
  private Object validator;

  public CartSimulation200ResponsePaymentDataPaymentSystemsInner() {
  }

  public CartSimulation200ResponsePaymentDataPaymentSystemsInner availablePayments(String availablePayments) {
    this.availablePayments = availablePayments;
    return this;
  }

  /**
   * Availability of payment.
   * @return availablePayments
   */
  @javax.annotation.Nullable
  public String getAvailablePayments() {
    return availablePayments;
  }

  public void setAvailablePayments(String availablePayments) {
    this.availablePayments = availablePayments;
  }


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner description(String description) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner displayDocument(Boolean displayDocument) {
    this.displayDocument = displayDocument;
    return this;
  }

  /**
   * Indicates whether a document is shown.
   * @return displayDocument
   */
  @javax.annotation.Nullable
  public Boolean getDisplayDocument() {
    return displayDocument;
  }

  public void setDisplayDocument(Boolean displayDocument) {
    this.displayDocument = displayDocument;
  }


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner dueDate(String dueDate) {
    this.dueDate = dueDate;
    return this;
  }

  /**
   * Payment due date.
   * @return dueDate
   */
  @javax.annotation.Nullable
  public String getDueDate() {
    return dueDate;
  }

  public void setDueDate(String dueDate) {
    this.dueDate = dueDate;
  }


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner groupName(String groupName) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner id(Integer id) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner isCustom(Boolean isCustom) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner name(String name) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner requiresAuthentication(Boolean requiresAuthentication) {
    this.requiresAuthentication = requiresAuthentication;
    return this;
  }

  /**
   * Indicates whether a authentication is required.
   * @return requiresAuthentication
   */
  @javax.annotation.Nullable
  public Boolean getRequiresAuthentication() {
    return requiresAuthentication;
  }

  public void setRequiresAuthentication(Boolean requiresAuthentication) {
    this.requiresAuthentication = requiresAuthentication;
  }


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner requiresDocument(Boolean requiresDocument) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner stringId(String stringId) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner template(String template) {
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


  public CartSimulation200ResponsePaymentDataPaymentSystemsInner validator(Object validator) {
    this.validator = validator;
    return this;
  }

  /**
   * Payment system validator.
   * @return validator
   */
  @javax.annotation.Nullable
  public Object getValidator() {
    return validator;
  }

  public void setValidator(Object validator) {
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
    CartSimulation200ResponsePaymentDataPaymentSystemsInner cartSimulation200ResponsePaymentDataPaymentSystemsInner = (CartSimulation200ResponsePaymentDataPaymentSystemsInner) o;
    return Objects.equals(this.availablePayments, cartSimulation200ResponsePaymentDataPaymentSystemsInner.availablePayments) &&
        Objects.equals(this.description, cartSimulation200ResponsePaymentDataPaymentSystemsInner.description) &&
        Objects.equals(this.displayDocument, cartSimulation200ResponsePaymentDataPaymentSystemsInner.displayDocument) &&
        Objects.equals(this.dueDate, cartSimulation200ResponsePaymentDataPaymentSystemsInner.dueDate) &&
        Objects.equals(this.groupName, cartSimulation200ResponsePaymentDataPaymentSystemsInner.groupName) &&
        Objects.equals(this.id, cartSimulation200ResponsePaymentDataPaymentSystemsInner.id) &&
        Objects.equals(this.isCustom, cartSimulation200ResponsePaymentDataPaymentSystemsInner.isCustom) &&
        Objects.equals(this.name, cartSimulation200ResponsePaymentDataPaymentSystemsInner.name) &&
        Objects.equals(this.requiresAuthentication, cartSimulation200ResponsePaymentDataPaymentSystemsInner.requiresAuthentication) &&
        Objects.equals(this.requiresDocument, cartSimulation200ResponsePaymentDataPaymentSystemsInner.requiresDocument) &&
        Objects.equals(this.stringId, cartSimulation200ResponsePaymentDataPaymentSystemsInner.stringId) &&
        Objects.equals(this.template, cartSimulation200ResponsePaymentDataPaymentSystemsInner.template) &&
        Objects.equals(this.validator, cartSimulation200ResponsePaymentDataPaymentSystemsInner.validator);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(availablePayments, description, displayDocument, dueDate, groupName, id, isCustom, name, requiresAuthentication, requiresDocument, stringId, template, validator);
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
    sb.append("class CartSimulation200ResponsePaymentDataPaymentSystemsInner {\n");
    sb.append("    availablePayments: ").append(toIndentedString(availablePayments)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    displayDocument: ").append(toIndentedString(displayDocument)).append("\n");
    sb.append("    dueDate: ").append(toIndentedString(dueDate)).append("\n");
    sb.append("    groupName: ").append(toIndentedString(groupName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isCustom: ").append(toIndentedString(isCustom)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    requiresAuthentication: ").append(toIndentedString(requiresAuthentication)).append("\n");
    sb.append("    requiresDocument: ").append(toIndentedString(requiresDocument)).append("\n");
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
    openapiFields.add("availablePayments");
    openapiFields.add("description");
    openapiFields.add("displayDocument");
    openapiFields.add("dueDate");
    openapiFields.add("groupName");
    openapiFields.add("id");
    openapiFields.add("isCustom");
    openapiFields.add("name");
    openapiFields.add("requiresAuthentication");
    openapiFields.add("requiresDocument");
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
   * @throws IOException if the JSON Element is invalid with respect to CartSimulation200ResponsePaymentDataPaymentSystemsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CartSimulation200ResponsePaymentDataPaymentSystemsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CartSimulation200ResponsePaymentDataPaymentSystemsInner is not found in the empty JSON string", CartSimulation200ResponsePaymentDataPaymentSystemsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CartSimulation200ResponsePaymentDataPaymentSystemsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CartSimulation200ResponsePaymentDataPaymentSystemsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("availablePayments") != null && !jsonObj.get("availablePayments").isJsonNull()) && !jsonObj.get("availablePayments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `availablePayments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("availablePayments").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("dueDate") != null && !jsonObj.get("dueDate").isJsonNull()) && !jsonObj.get("dueDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dueDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dueDate").toString()));
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
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CartSimulation200ResponsePaymentDataPaymentSystemsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CartSimulation200ResponsePaymentDataPaymentSystemsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CartSimulation200ResponsePaymentDataPaymentSystemsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CartSimulation200ResponsePaymentDataPaymentSystemsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CartSimulation200ResponsePaymentDataPaymentSystemsInner>() {
           @Override
           public void write(JsonWriter out, CartSimulation200ResponsePaymentDataPaymentSystemsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CartSimulation200ResponsePaymentDataPaymentSystemsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CartSimulation200ResponsePaymentDataPaymentSystemsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CartSimulation200ResponsePaymentDataPaymentSystemsInner
   * @throws IOException if the JSON string is invalid with respect to CartSimulation200ResponsePaymentDataPaymentSystemsInner
   */
  public static CartSimulation200ResponsePaymentDataPaymentSystemsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CartSimulation200ResponsePaymentDataPaymentSystemsInner.class);
  }

  /**
   * Convert an instance of CartSimulation200ResponsePaymentDataPaymentSystemsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

