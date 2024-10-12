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
 * Customer&#39;s profile information.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddClientProfileRequest {
  public static final String SERIALIZED_NAME_CORPORATE_DOCUMENT = "corporateDocument";
  @SerializedName(SERIALIZED_NAME_CORPORATE_DOCUMENT)
  private String corporateDocument = "12345678000100";

  public static final String SERIALIZED_NAME_CORPORATE_NAME = "corporateName";
  @SerializedName(SERIALIZED_NAME_CORPORATE_NAME)
  private String corporateName = "company-name";

  public static final String SERIALIZED_NAME_CORPORATE_PHONE = "corporatePhone";
  @SerializedName(SERIALIZED_NAME_CORPORATE_PHONE)
  private String corporatePhone = "+551100988887777";

  public static final String SERIALIZED_NAME_DOCUMENT = "document";
  @SerializedName(SERIALIZED_NAME_DOCUMENT)
  private String document = "123456789";

  public static final String SERIALIZED_NAME_DOCUMENT_TYPE = "documentType";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_TYPE)
  private String documentType = "cpf";

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email = "customer@examplemail.com";

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName = "first-name";

  public static final String SERIALIZED_NAME_IS_CORPORATE = "isCorporate";
  @SerializedName(SERIALIZED_NAME_IS_CORPORATE)
  private Boolean isCorporate = false;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName = "last-name";

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone = "+55110988887777";

  public static final String SERIALIZED_NAME_STATE_INSCRIPTION = "stateInscription";
  @SerializedName(SERIALIZED_NAME_STATE_INSCRIPTION)
  private String stateInscription = "12345678";

  public static final String SERIALIZED_NAME_TRADE_NAME = "tradeName";
  @SerializedName(SERIALIZED_NAME_TRADE_NAME)
  private String tradeName = "trade-name";

  public AddClientProfileRequest() {
  }

  public AddClientProfileRequest corporateDocument(String corporateDocument) {
    this.corporateDocument = corporateDocument;
    return this;
  }

  /**
   * Corporate document, if the customer is a legal entity.
   * @return corporateDocument
   */
  @javax.annotation.Nullable
  public String getCorporateDocument() {
    return corporateDocument;
  }

  public void setCorporateDocument(String corporateDocument) {
    this.corporateDocument = corporateDocument;
  }


  public AddClientProfileRequest corporateName(String corporateName) {
    this.corporateName = corporateName;
    return this;
  }

  /**
   * Company name, if the customer is a legal entity.
   * @return corporateName
   */
  @javax.annotation.Nullable
  public String getCorporateName() {
    return corporateName;
  }

  public void setCorporateName(String corporateName) {
    this.corporateName = corporateName;
  }


  public AddClientProfileRequest corporatePhone(String corporatePhone) {
    this.corporatePhone = corporatePhone;
    return this;
  }

  /**
   * Corporate phone number, if the customer is a legal entity.
   * @return corporatePhone
   */
  @javax.annotation.Nullable
  public String getCorporatePhone() {
    return corporatePhone;
  }

  public void setCorporatePhone(String corporatePhone) {
    this.corporatePhone = corporatePhone;
  }


  public AddClientProfileRequest document(String document) {
    this.document = document;
    return this;
  }

  /**
   * Document number informed by the customer.
   * @return document
   */
  @javax.annotation.Nonnull
  public String getDocument() {
    return document;
  }

  public void setDocument(String document) {
    this.document = document;
  }


  public AddClientProfileRequest documentType(String documentType) {
    this.documentType = documentType;
    return this;
  }

  /**
   * Type of the document informed by the customer.
   * @return documentType
   */
  @javax.annotation.Nonnull
  public String getDocumentType() {
    return documentType;
  }

  public void setDocumentType(String documentType) {
    this.documentType = documentType;
  }


  public AddClientProfileRequest email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Customer&#39;s email address.
   * @return email
   */
  @javax.annotation.Nonnull
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public AddClientProfileRequest firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * Customer&#39;s first name.
   * @return firstName
   */
  @javax.annotation.Nonnull
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public AddClientProfileRequest isCorporate(Boolean isCorporate) {
    this.isCorporate = isCorporate;
    return this;
  }

  /**
   * &#x60;true&#x60; if the customer is a legal entity.
   * @return isCorporate
   */
  @javax.annotation.Nullable
  public Boolean getIsCorporate() {
    return isCorporate;
  }

  public void setIsCorporate(Boolean isCorporate) {
    this.isCorporate = isCorporate;
  }


  public AddClientProfileRequest lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * Customer&#39;s last name.
   * @return lastName
   */
  @javax.annotation.Nonnull
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public AddClientProfileRequest phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Customer&#39;s phone number.
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public AddClientProfileRequest stateInscription(String stateInscription) {
    this.stateInscription = stateInscription;
    return this;
  }

  /**
   * State inscription, if the customer is a legal entity.
   * @return stateInscription
   */
  @javax.annotation.Nullable
  public String getStateInscription() {
    return stateInscription;
  }

  public void setStateInscription(String stateInscription) {
    this.stateInscription = stateInscription;
  }


  public AddClientProfileRequest tradeName(String tradeName) {
    this.tradeName = tradeName;
    return this;
  }

  /**
   * Trade name, if the customer is a legal entity.
   * @return tradeName
   */
  @javax.annotation.Nullable
  public String getTradeName() {
    return tradeName;
  }

  public void setTradeName(String tradeName) {
    this.tradeName = tradeName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddClientProfileRequest addClientProfileRequest = (AddClientProfileRequest) o;
    return Objects.equals(this.corporateDocument, addClientProfileRequest.corporateDocument) &&
        Objects.equals(this.corporateName, addClientProfileRequest.corporateName) &&
        Objects.equals(this.corporatePhone, addClientProfileRequest.corporatePhone) &&
        Objects.equals(this.document, addClientProfileRequest.document) &&
        Objects.equals(this.documentType, addClientProfileRequest.documentType) &&
        Objects.equals(this.email, addClientProfileRequest.email) &&
        Objects.equals(this.firstName, addClientProfileRequest.firstName) &&
        Objects.equals(this.isCorporate, addClientProfileRequest.isCorporate) &&
        Objects.equals(this.lastName, addClientProfileRequest.lastName) &&
        Objects.equals(this.phone, addClientProfileRequest.phone) &&
        Objects.equals(this.stateInscription, addClientProfileRequest.stateInscription) &&
        Objects.equals(this.tradeName, addClientProfileRequest.tradeName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(corporateDocument, corporateName, corporatePhone, document, documentType, email, firstName, isCorporate, lastName, phone, stateInscription, tradeName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddClientProfileRequest {\n");
    sb.append("    corporateDocument: ").append(toIndentedString(corporateDocument)).append("\n");
    sb.append("    corporateName: ").append(toIndentedString(corporateName)).append("\n");
    sb.append("    corporatePhone: ").append(toIndentedString(corporatePhone)).append("\n");
    sb.append("    document: ").append(toIndentedString(document)).append("\n");
    sb.append("    documentType: ").append(toIndentedString(documentType)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    isCorporate: ").append(toIndentedString(isCorporate)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    stateInscription: ").append(toIndentedString(stateInscription)).append("\n");
    sb.append("    tradeName: ").append(toIndentedString(tradeName)).append("\n");
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
    openapiFields.add("corporateDocument");
    openapiFields.add("corporateName");
    openapiFields.add("corporatePhone");
    openapiFields.add("document");
    openapiFields.add("documentType");
    openapiFields.add("email");
    openapiFields.add("firstName");
    openapiFields.add("isCorporate");
    openapiFields.add("lastName");
    openapiFields.add("phone");
    openapiFields.add("stateInscription");
    openapiFields.add("tradeName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("document");
    openapiRequiredFields.add("documentType");
    openapiRequiredFields.add("email");
    openapiRequiredFields.add("firstName");
    openapiRequiredFields.add("lastName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddClientProfileRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddClientProfileRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddClientProfileRequest is not found in the empty JSON string", AddClientProfileRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddClientProfileRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddClientProfileRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AddClientProfileRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("corporateDocument") != null && !jsonObj.get("corporateDocument").isJsonNull()) && !jsonObj.get("corporateDocument").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `corporateDocument` to be a primitive type in the JSON string but got `%s`", jsonObj.get("corporateDocument").toString()));
      }
      if ((jsonObj.get("corporateName") != null && !jsonObj.get("corporateName").isJsonNull()) && !jsonObj.get("corporateName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `corporateName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("corporateName").toString()));
      }
      if ((jsonObj.get("corporatePhone") != null && !jsonObj.get("corporatePhone").isJsonNull()) && !jsonObj.get("corporatePhone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `corporatePhone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("corporatePhone").toString()));
      }
      if (!jsonObj.get("document").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `document` to be a primitive type in the JSON string but got `%s`", jsonObj.get("document").toString()));
      }
      if (!jsonObj.get("documentType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `documentType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("documentType").toString()));
      }
      if (!jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if (!jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if (!jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      if ((jsonObj.get("stateInscription") != null && !jsonObj.get("stateInscription").isJsonNull()) && !jsonObj.get("stateInscription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `stateInscription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("stateInscription").toString()));
      }
      if ((jsonObj.get("tradeName") != null && !jsonObj.get("tradeName").isJsonNull()) && !jsonObj.get("tradeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tradeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tradeName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddClientProfileRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddClientProfileRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddClientProfileRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddClientProfileRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AddClientProfileRequest>() {
           @Override
           public void write(JsonWriter out, AddClientProfileRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddClientProfileRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddClientProfileRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddClientProfileRequest
   * @throws IOException if the JSON string is invalid with respect to AddClientProfileRequest
   */
  public static AddClientProfileRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddClientProfileRequest.class);
  }

  /**
   * Convert an instance of AddClientProfileRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

