/*
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
 * CustomerUpdateAddressInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CustomerUpdateAddressInner {
  public static final String SERIALIZED_NAME_ADDRESS_BOOK_ADDRESS1 = "address_book_address1";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_ADDRESS1)
  private String addressBookAddress1;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_ADDRESS2 = "address_book_address2";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_ADDRESS2)
  private String addressBookAddress2;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_CITY = "address_book_city";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_CITY)
  private String addressBookCity;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_COMPANY = "address_book_company";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_COMPANY)
  private String addressBookCompany;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_COUNTRY = "address_book_country";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_COUNTRY)
  private String addressBookCountry;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_DEFAULT = "address_book_default";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_DEFAULT)
  private Boolean addressBookDefault;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_FAX = "address_book_fax";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_FAX)
  private String addressBookFax;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_FIRST_NAME = "address_book_first_name";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_FIRST_NAME)
  private String addressBookFirstName;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_ID = "address_book_id";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_ID)
  private String addressBookId;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_IDENTIFICATION_NUMBER = "address_book_identification_number";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_IDENTIFICATION_NUMBER)
  private String addressBookIdentificationNumber;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_LAST_NAME = "address_book_last_name";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_LAST_NAME)
  private String addressBookLastName;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_PHONE = "address_book_phone";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_PHONE)
  private String addressBookPhone;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_PHONE_MOBILE = "address_book_phone_mobile";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_PHONE_MOBILE)
  private String addressBookPhoneMobile;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_POSTCODE = "address_book_postcode";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_POSTCODE)
  private String addressBookPostcode;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_STATE = "address_book_state";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_STATE)
  private String addressBookState;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_TAX_ID = "address_book_tax_id";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_TAX_ID)
  private String addressBookTaxId;

  public static final String SERIALIZED_NAME_ADDRESS_BOOK_TYPE = "address_book_type";
  @SerializedName(SERIALIZED_NAME_ADDRESS_BOOK_TYPE)
  private String addressBookType;

  public CustomerUpdateAddressInner() {
  }

  public CustomerUpdateAddressInner addressBookAddress1(String addressBookAddress1) {
    this.addressBookAddress1 = addressBookAddress1;
    return this;
  }

  /**
   * Specifies customer&#39;s first address in the address book
   * @return addressBookAddress1
   */
  @javax.annotation.Nullable
  public String getAddressBookAddress1() {
    return addressBookAddress1;
  }

  public void setAddressBookAddress1(String addressBookAddress1) {
    this.addressBookAddress1 = addressBookAddress1;
  }


  public CustomerUpdateAddressInner addressBookAddress2(String addressBookAddress2) {
    this.addressBookAddress2 = addressBookAddress2;
    return this;
  }

  /**
   * Specifies customer&#39;s second address in the address book
   * @return addressBookAddress2
   */
  @javax.annotation.Nullable
  public String getAddressBookAddress2() {
    return addressBookAddress2;
  }

  public void setAddressBookAddress2(String addressBookAddress2) {
    this.addressBookAddress2 = addressBookAddress2;
  }


  public CustomerUpdateAddressInner addressBookCity(String addressBookCity) {
    this.addressBookCity = addressBookCity;
    return this;
  }

  /**
   * Specifies customer&#39;s city in the address book
   * @return addressBookCity
   */
  @javax.annotation.Nullable
  public String getAddressBookCity() {
    return addressBookCity;
  }

  public void setAddressBookCity(String addressBookCity) {
    this.addressBookCity = addressBookCity;
  }


  public CustomerUpdateAddressInner addressBookCompany(String addressBookCompany) {
    this.addressBookCompany = addressBookCompany;
    return this;
  }

  /**
   * Specifies customer&#39;s company name in the address book
   * @return addressBookCompany
   */
  @javax.annotation.Nullable
  public String getAddressBookCompany() {
    return addressBookCompany;
  }

  public void setAddressBookCompany(String addressBookCompany) {
    this.addressBookCompany = addressBookCompany;
  }


  public CustomerUpdateAddressInner addressBookCountry(String addressBookCountry) {
    this.addressBookCountry = addressBookCountry;
    return this;
  }

  /**
   * ISO code or name of country
   * @return addressBookCountry
   */
  @javax.annotation.Nullable
  public String getAddressBookCountry() {
    return addressBookCountry;
  }

  public void setAddressBookCountry(String addressBookCountry) {
    this.addressBookCountry = addressBookCountry;
  }


  public CustomerUpdateAddressInner addressBookDefault(Boolean addressBookDefault) {
    this.addressBookDefault = addressBookDefault;
    return this;
  }

  /**
   * Defines whether the address is used by default
   * @return addressBookDefault
   */
  @javax.annotation.Nullable
  public Boolean getAddressBookDefault() {
    return addressBookDefault;
  }

  public void setAddressBookDefault(Boolean addressBookDefault) {
    this.addressBookDefault = addressBookDefault;
  }


  public CustomerUpdateAddressInner addressBookFax(String addressBookFax) {
    this.addressBookFax = addressBookFax;
    return this;
  }

  /**
   * Specifies customer&#39;s fax in the address book
   * @return addressBookFax
   */
  @javax.annotation.Nullable
  public String getAddressBookFax() {
    return addressBookFax;
  }

  public void setAddressBookFax(String addressBookFax) {
    this.addressBookFax = addressBookFax;
  }


  public CustomerUpdateAddressInner addressBookFirstName(String addressBookFirstName) {
    this.addressBookFirstName = addressBookFirstName;
    return this;
  }

  /**
   * Specifies customer&#39;s first name in the address book
   * @return addressBookFirstName
   */
  @javax.annotation.Nullable
  public String getAddressBookFirstName() {
    return addressBookFirstName;
  }

  public void setAddressBookFirstName(String addressBookFirstName) {
    this.addressBookFirstName = addressBookFirstName;
  }


  public CustomerUpdateAddressInner addressBookId(String addressBookId) {
    this.addressBookId = addressBookId;
    return this;
  }

  /**
   * The ID of the address.
   * @return addressBookId
   */
  @javax.annotation.Nullable
  public String getAddressBookId() {
    return addressBookId;
  }

  public void setAddressBookId(String addressBookId) {
    this.addressBookId = addressBookId;
  }


  public CustomerUpdateAddressInner addressBookIdentificationNumber(String addressBookIdentificationNumber) {
    this.addressBookIdentificationNumber = addressBookIdentificationNumber;
    return this;
  }

  /**
   * The national ID card number of this person, or a unique tax identification number.
   * @return addressBookIdentificationNumber
   */
  @javax.annotation.Nullable
  public String getAddressBookIdentificationNumber() {
    return addressBookIdentificationNumber;
  }

  public void setAddressBookIdentificationNumber(String addressBookIdentificationNumber) {
    this.addressBookIdentificationNumber = addressBookIdentificationNumber;
  }


  public CustomerUpdateAddressInner addressBookLastName(String addressBookLastName) {
    this.addressBookLastName = addressBookLastName;
    return this;
  }

  /**
   * Specifies customer&#39;s last name in the address book
   * @return addressBookLastName
   */
  @javax.annotation.Nullable
  public String getAddressBookLastName() {
    return addressBookLastName;
  }

  public void setAddressBookLastName(String addressBookLastName) {
    this.addressBookLastName = addressBookLastName;
  }


  public CustomerUpdateAddressInner addressBookPhone(String addressBookPhone) {
    this.addressBookPhone = addressBookPhone;
    return this;
  }

  /**
   * Specifies customer&#39;s phone number in the address book
   * @return addressBookPhone
   */
  @javax.annotation.Nullable
  public String getAddressBookPhone() {
    return addressBookPhone;
  }

  public void setAddressBookPhone(String addressBookPhone) {
    this.addressBookPhone = addressBookPhone;
  }


  public CustomerUpdateAddressInner addressBookPhoneMobile(String addressBookPhoneMobile) {
    this.addressBookPhoneMobile = addressBookPhoneMobile;
    return this;
  }

  /**
   * Specifies customer&#39;s mobile phone number in the address book
   * @return addressBookPhoneMobile
   */
  @javax.annotation.Nullable
  public String getAddressBookPhoneMobile() {
    return addressBookPhoneMobile;
  }

  public void setAddressBookPhoneMobile(String addressBookPhoneMobile) {
    this.addressBookPhoneMobile = addressBookPhoneMobile;
  }


  public CustomerUpdateAddressInner addressBookPostcode(String addressBookPostcode) {
    this.addressBookPostcode = addressBookPostcode;
    return this;
  }

  /**
   * Specifies customer&#39;s postcode
   * @return addressBookPostcode
   */
  @javax.annotation.Nullable
  public String getAddressBookPostcode() {
    return addressBookPostcode;
  }

  public void setAddressBookPostcode(String addressBookPostcode) {
    this.addressBookPostcode = addressBookPostcode;
  }


  public CustomerUpdateAddressInner addressBookState(String addressBookState) {
    this.addressBookState = addressBookState;
    return this;
  }

  /**
   * ISO code or name of state.
   * @return addressBookState
   */
  @javax.annotation.Nullable
  public String getAddressBookState() {
    return addressBookState;
  }

  public void setAddressBookState(String addressBookState) {
    this.addressBookState = addressBookState;
  }


  public CustomerUpdateAddressInner addressBookTaxId(String addressBookTaxId) {
    this.addressBookTaxId = addressBookTaxId;
    return this;
  }

  /**
   * Add Tax Id
   * @return addressBookTaxId
   */
  @javax.annotation.Nullable
  public String getAddressBookTaxId() {
    return addressBookTaxId;
  }

  public void setAddressBookTaxId(String addressBookTaxId) {
    this.addressBookTaxId = addressBookTaxId;
  }


  public CustomerUpdateAddressInner addressBookType(String addressBookType) {
    this.addressBookType = addressBookType;
    return this;
  }

  /**
   * Specifies customer&#39;s address type
   * @return addressBookType
   */
  @javax.annotation.Nullable
  public String getAddressBookType() {
    return addressBookType;
  }

  public void setAddressBookType(String addressBookType) {
    this.addressBookType = addressBookType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CustomerUpdateAddressInner customerUpdateAddressInner = (CustomerUpdateAddressInner) o;
    return Objects.equals(this.addressBookAddress1, customerUpdateAddressInner.addressBookAddress1) &&
        Objects.equals(this.addressBookAddress2, customerUpdateAddressInner.addressBookAddress2) &&
        Objects.equals(this.addressBookCity, customerUpdateAddressInner.addressBookCity) &&
        Objects.equals(this.addressBookCompany, customerUpdateAddressInner.addressBookCompany) &&
        Objects.equals(this.addressBookCountry, customerUpdateAddressInner.addressBookCountry) &&
        Objects.equals(this.addressBookDefault, customerUpdateAddressInner.addressBookDefault) &&
        Objects.equals(this.addressBookFax, customerUpdateAddressInner.addressBookFax) &&
        Objects.equals(this.addressBookFirstName, customerUpdateAddressInner.addressBookFirstName) &&
        Objects.equals(this.addressBookId, customerUpdateAddressInner.addressBookId) &&
        Objects.equals(this.addressBookIdentificationNumber, customerUpdateAddressInner.addressBookIdentificationNumber) &&
        Objects.equals(this.addressBookLastName, customerUpdateAddressInner.addressBookLastName) &&
        Objects.equals(this.addressBookPhone, customerUpdateAddressInner.addressBookPhone) &&
        Objects.equals(this.addressBookPhoneMobile, customerUpdateAddressInner.addressBookPhoneMobile) &&
        Objects.equals(this.addressBookPostcode, customerUpdateAddressInner.addressBookPostcode) &&
        Objects.equals(this.addressBookState, customerUpdateAddressInner.addressBookState) &&
        Objects.equals(this.addressBookTaxId, customerUpdateAddressInner.addressBookTaxId) &&
        Objects.equals(this.addressBookType, customerUpdateAddressInner.addressBookType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(addressBookAddress1, addressBookAddress2, addressBookCity, addressBookCompany, addressBookCountry, addressBookDefault, addressBookFax, addressBookFirstName, addressBookId, addressBookIdentificationNumber, addressBookLastName, addressBookPhone, addressBookPhoneMobile, addressBookPostcode, addressBookState, addressBookTaxId, addressBookType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CustomerUpdateAddressInner {\n");
    sb.append("    addressBookAddress1: ").append(toIndentedString(addressBookAddress1)).append("\n");
    sb.append("    addressBookAddress2: ").append(toIndentedString(addressBookAddress2)).append("\n");
    sb.append("    addressBookCity: ").append(toIndentedString(addressBookCity)).append("\n");
    sb.append("    addressBookCompany: ").append(toIndentedString(addressBookCompany)).append("\n");
    sb.append("    addressBookCountry: ").append(toIndentedString(addressBookCountry)).append("\n");
    sb.append("    addressBookDefault: ").append(toIndentedString(addressBookDefault)).append("\n");
    sb.append("    addressBookFax: ").append(toIndentedString(addressBookFax)).append("\n");
    sb.append("    addressBookFirstName: ").append(toIndentedString(addressBookFirstName)).append("\n");
    sb.append("    addressBookId: ").append(toIndentedString(addressBookId)).append("\n");
    sb.append("    addressBookIdentificationNumber: ").append(toIndentedString(addressBookIdentificationNumber)).append("\n");
    sb.append("    addressBookLastName: ").append(toIndentedString(addressBookLastName)).append("\n");
    sb.append("    addressBookPhone: ").append(toIndentedString(addressBookPhone)).append("\n");
    sb.append("    addressBookPhoneMobile: ").append(toIndentedString(addressBookPhoneMobile)).append("\n");
    sb.append("    addressBookPostcode: ").append(toIndentedString(addressBookPostcode)).append("\n");
    sb.append("    addressBookState: ").append(toIndentedString(addressBookState)).append("\n");
    sb.append("    addressBookTaxId: ").append(toIndentedString(addressBookTaxId)).append("\n");
    sb.append("    addressBookType: ").append(toIndentedString(addressBookType)).append("\n");
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
    openapiFields.add("address_book_address1");
    openapiFields.add("address_book_address2");
    openapiFields.add("address_book_city");
    openapiFields.add("address_book_company");
    openapiFields.add("address_book_country");
    openapiFields.add("address_book_default");
    openapiFields.add("address_book_fax");
    openapiFields.add("address_book_first_name");
    openapiFields.add("address_book_id");
    openapiFields.add("address_book_identification_number");
    openapiFields.add("address_book_last_name");
    openapiFields.add("address_book_phone");
    openapiFields.add("address_book_phone_mobile");
    openapiFields.add("address_book_postcode");
    openapiFields.add("address_book_state");
    openapiFields.add("address_book_tax_id");
    openapiFields.add("address_book_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CustomerUpdateAddressInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CustomerUpdateAddressInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CustomerUpdateAddressInner is not found in the empty JSON string", CustomerUpdateAddressInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CustomerUpdateAddressInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CustomerUpdateAddressInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address_book_address1") != null && !jsonObj.get("address_book_address1").isJsonNull()) && !jsonObj.get("address_book_address1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_address1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_address1").toString()));
      }
      if ((jsonObj.get("address_book_address2") != null && !jsonObj.get("address_book_address2").isJsonNull()) && !jsonObj.get("address_book_address2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_address2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_address2").toString()));
      }
      if ((jsonObj.get("address_book_city") != null && !jsonObj.get("address_book_city").isJsonNull()) && !jsonObj.get("address_book_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_city").toString()));
      }
      if ((jsonObj.get("address_book_company") != null && !jsonObj.get("address_book_company").isJsonNull()) && !jsonObj.get("address_book_company").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_company` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_company").toString()));
      }
      if ((jsonObj.get("address_book_country") != null && !jsonObj.get("address_book_country").isJsonNull()) && !jsonObj.get("address_book_country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_country").toString()));
      }
      if ((jsonObj.get("address_book_fax") != null && !jsonObj.get("address_book_fax").isJsonNull()) && !jsonObj.get("address_book_fax").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_fax` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_fax").toString()));
      }
      if ((jsonObj.get("address_book_first_name") != null && !jsonObj.get("address_book_first_name").isJsonNull()) && !jsonObj.get("address_book_first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_first_name").toString()));
      }
      if ((jsonObj.get("address_book_id") != null && !jsonObj.get("address_book_id").isJsonNull()) && !jsonObj.get("address_book_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_id").toString()));
      }
      if ((jsonObj.get("address_book_identification_number") != null && !jsonObj.get("address_book_identification_number").isJsonNull()) && !jsonObj.get("address_book_identification_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_identification_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_identification_number").toString()));
      }
      if ((jsonObj.get("address_book_last_name") != null && !jsonObj.get("address_book_last_name").isJsonNull()) && !jsonObj.get("address_book_last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_last_name").toString()));
      }
      if ((jsonObj.get("address_book_phone") != null && !jsonObj.get("address_book_phone").isJsonNull()) && !jsonObj.get("address_book_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_phone").toString()));
      }
      if ((jsonObj.get("address_book_phone_mobile") != null && !jsonObj.get("address_book_phone_mobile").isJsonNull()) && !jsonObj.get("address_book_phone_mobile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_phone_mobile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_phone_mobile").toString()));
      }
      if ((jsonObj.get("address_book_postcode") != null && !jsonObj.get("address_book_postcode").isJsonNull()) && !jsonObj.get("address_book_postcode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_postcode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_postcode").toString()));
      }
      if ((jsonObj.get("address_book_state") != null && !jsonObj.get("address_book_state").isJsonNull()) && !jsonObj.get("address_book_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_state").toString()));
      }
      if ((jsonObj.get("address_book_tax_id") != null && !jsonObj.get("address_book_tax_id").isJsonNull()) && !jsonObj.get("address_book_tax_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_tax_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_tax_id").toString()));
      }
      if ((jsonObj.get("address_book_type") != null && !jsonObj.get("address_book_type").isJsonNull()) && !jsonObj.get("address_book_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address_book_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address_book_type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CustomerUpdateAddressInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CustomerUpdateAddressInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CustomerUpdateAddressInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CustomerUpdateAddressInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CustomerUpdateAddressInner>() {
           @Override
           public void write(JsonWriter out, CustomerUpdateAddressInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CustomerUpdateAddressInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CustomerUpdateAddressInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CustomerUpdateAddressInner
   * @throws IOException if the JSON string is invalid with respect to CustomerUpdateAddressInner
   */
  public static CustomerUpdateAddressInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CustomerUpdateAddressInner.class);
  }

  /**
   * Convert an instance of CustomerUpdateAddressInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

