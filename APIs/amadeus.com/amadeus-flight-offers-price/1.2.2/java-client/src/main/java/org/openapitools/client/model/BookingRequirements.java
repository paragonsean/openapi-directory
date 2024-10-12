/*
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
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
import org.openapitools.client.model.PassengerConditions;

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
 * pricing condition at booking level
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:43.662685-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BookingRequirements {
  public static final String SERIALIZED_NAME_EMAIL_ADDRESS_REQUIRED = "emailAddressRequired";
  @SerializedName(SERIALIZED_NAME_EMAIL_ADDRESS_REQUIRED)
  private Boolean emailAddressRequired;

  public static final String SERIALIZED_NAME_INVOICE_ADDRESS_REQUIRED = "invoiceAddressRequired";
  @SerializedName(SERIALIZED_NAME_INVOICE_ADDRESS_REQUIRED)
  private Boolean invoiceAddressRequired;

  public static final String SERIALIZED_NAME_MAILING_ADDRESS_REQUIRED = "mailingAddressRequired";
  @SerializedName(SERIALIZED_NAME_MAILING_ADDRESS_REQUIRED)
  private Boolean mailingAddressRequired;

  public static final String SERIALIZED_NAME_MOBILE_PHONE_NUMBER_REQUIRED = "mobilePhoneNumberRequired";
  @SerializedName(SERIALIZED_NAME_MOBILE_PHONE_NUMBER_REQUIRED)
  private Boolean mobilePhoneNumberRequired;

  public static final String SERIALIZED_NAME_PHONE_COUNTRY_CODE_REQUIRED = "phoneCountryCodeRequired";
  @SerializedName(SERIALIZED_NAME_PHONE_COUNTRY_CODE_REQUIRED)
  private Boolean phoneCountryCodeRequired;

  public static final String SERIALIZED_NAME_PHONE_NUMBER_REQUIRED = "phoneNumberRequired";
  @SerializedName(SERIALIZED_NAME_PHONE_NUMBER_REQUIRED)
  private Boolean phoneNumberRequired;

  public static final String SERIALIZED_NAME_POSTAL_CODE_REQUIRED = "postalCodeRequired";
  @SerializedName(SERIALIZED_NAME_POSTAL_CODE_REQUIRED)
  private Boolean postalCodeRequired;

  public static final String SERIALIZED_NAME_TRAVELER_REQUIREMENTS = "travelerRequirements";
  @SerializedName(SERIALIZED_NAME_TRAVELER_REQUIREMENTS)
  private List<PassengerConditions> travelerRequirements = new ArrayList<>();

  public BookingRequirements() {
  }

  public BookingRequirements emailAddressRequired(Boolean emailAddressRequired) {
    this.emailAddressRequired = emailAddressRequired;
    return this;
  }

  /**
   * If true, an email address is required for the creation of the flight-order
   * @return emailAddressRequired
   */
  @javax.annotation.Nullable
  public Boolean getEmailAddressRequired() {
    return emailAddressRequired;
  }

  public void setEmailAddressRequired(Boolean emailAddressRequired) {
    this.emailAddressRequired = emailAddressRequired;
  }


  public BookingRequirements invoiceAddressRequired(Boolean invoiceAddressRequired) {
    this.invoiceAddressRequired = invoiceAddressRequired;
    return this;
  }

  /**
   * If true, an invoice address is required for the creation of the flight-order
   * @return invoiceAddressRequired
   */
  @javax.annotation.Nullable
  public Boolean getInvoiceAddressRequired() {
    return invoiceAddressRequired;
  }

  public void setInvoiceAddressRequired(Boolean invoiceAddressRequired) {
    this.invoiceAddressRequired = invoiceAddressRequired;
  }


  public BookingRequirements mailingAddressRequired(Boolean mailingAddressRequired) {
    this.mailingAddressRequired = mailingAddressRequired;
    return this;
  }

  /**
   * If true, a postal address is required for the creation of the flight-order
   * @return mailingAddressRequired
   */
  @javax.annotation.Nullable
  public Boolean getMailingAddressRequired() {
    return mailingAddressRequired;
  }

  public void setMailingAddressRequired(Boolean mailingAddressRequired) {
    this.mailingAddressRequired = mailingAddressRequired;
  }


  public BookingRequirements mobilePhoneNumberRequired(Boolean mobilePhoneNumberRequired) {
    this.mobilePhoneNumberRequired = mobilePhoneNumberRequired;
    return this;
  }

  /**
   * If true, a mobile phone number is required for the creation of the flight-order
   * @return mobilePhoneNumberRequired
   */
  @javax.annotation.Nullable
  public Boolean getMobilePhoneNumberRequired() {
    return mobilePhoneNumberRequired;
  }

  public void setMobilePhoneNumberRequired(Boolean mobilePhoneNumberRequired) {
    this.mobilePhoneNumberRequired = mobilePhoneNumberRequired;
  }


  public BookingRequirements phoneCountryCodeRequired(Boolean phoneCountryCodeRequired) {
    this.phoneCountryCodeRequired = phoneCountryCodeRequired;
    return this;
  }

  /**
   * If true, the phone country code (e.g. &#39;33&#39;) associated for each phone number is required for the creation of the flight-order
   * @return phoneCountryCodeRequired
   */
  @javax.annotation.Nullable
  public Boolean getPhoneCountryCodeRequired() {
    return phoneCountryCodeRequired;
  }

  public void setPhoneCountryCodeRequired(Boolean phoneCountryCodeRequired) {
    this.phoneCountryCodeRequired = phoneCountryCodeRequired;
  }


  public BookingRequirements phoneNumberRequired(Boolean phoneNumberRequired) {
    this.phoneNumberRequired = phoneNumberRequired;
    return this;
  }

  /**
   * If true, a phone number is required for the creation of the flight-order
   * @return phoneNumberRequired
   */
  @javax.annotation.Nullable
  public Boolean getPhoneNumberRequired() {
    return phoneNumberRequired;
  }

  public void setPhoneNumberRequired(Boolean phoneNumberRequired) {
    this.phoneNumberRequired = phoneNumberRequired;
  }


  public BookingRequirements postalCodeRequired(Boolean postalCodeRequired) {
    this.postalCodeRequired = postalCodeRequired;
    return this;
  }

  /**
   * If true, a postal code is required for the creation of the flight-order
   * @return postalCodeRequired
   */
  @javax.annotation.Nullable
  public Boolean getPostalCodeRequired() {
    return postalCodeRequired;
  }

  public void setPostalCodeRequired(Boolean postalCodeRequired) {
    this.postalCodeRequired = postalCodeRequired;
  }


  public BookingRequirements travelerRequirements(List<PassengerConditions> travelerRequirements) {
    this.travelerRequirements = travelerRequirements;
    return this;
  }

  public BookingRequirements addTravelerRequirementsItem(PassengerConditions travelerRequirementsItem) {
    if (this.travelerRequirements == null) {
      this.travelerRequirements = new ArrayList<>();
    }
    this.travelerRequirements.add(travelerRequirementsItem);
    return this;
  }

  /**
   * traveler pricing condition
   * @return travelerRequirements
   */
  @javax.annotation.Nullable
  public List<PassengerConditions> getTravelerRequirements() {
    return travelerRequirements;
  }

  public void setTravelerRequirements(List<PassengerConditions> travelerRequirements) {
    this.travelerRequirements = travelerRequirements;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BookingRequirements bookingRequirements = (BookingRequirements) o;
    return Objects.equals(this.emailAddressRequired, bookingRequirements.emailAddressRequired) &&
        Objects.equals(this.invoiceAddressRequired, bookingRequirements.invoiceAddressRequired) &&
        Objects.equals(this.mailingAddressRequired, bookingRequirements.mailingAddressRequired) &&
        Objects.equals(this.mobilePhoneNumberRequired, bookingRequirements.mobilePhoneNumberRequired) &&
        Objects.equals(this.phoneCountryCodeRequired, bookingRequirements.phoneCountryCodeRequired) &&
        Objects.equals(this.phoneNumberRequired, bookingRequirements.phoneNumberRequired) &&
        Objects.equals(this.postalCodeRequired, bookingRequirements.postalCodeRequired) &&
        Objects.equals(this.travelerRequirements, bookingRequirements.travelerRequirements);
  }

  @Override
  public int hashCode() {
    return Objects.hash(emailAddressRequired, invoiceAddressRequired, mailingAddressRequired, mobilePhoneNumberRequired, phoneCountryCodeRequired, phoneNumberRequired, postalCodeRequired, travelerRequirements);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BookingRequirements {\n");
    sb.append("    emailAddressRequired: ").append(toIndentedString(emailAddressRequired)).append("\n");
    sb.append("    invoiceAddressRequired: ").append(toIndentedString(invoiceAddressRequired)).append("\n");
    sb.append("    mailingAddressRequired: ").append(toIndentedString(mailingAddressRequired)).append("\n");
    sb.append("    mobilePhoneNumberRequired: ").append(toIndentedString(mobilePhoneNumberRequired)).append("\n");
    sb.append("    phoneCountryCodeRequired: ").append(toIndentedString(phoneCountryCodeRequired)).append("\n");
    sb.append("    phoneNumberRequired: ").append(toIndentedString(phoneNumberRequired)).append("\n");
    sb.append("    postalCodeRequired: ").append(toIndentedString(postalCodeRequired)).append("\n");
    sb.append("    travelerRequirements: ").append(toIndentedString(travelerRequirements)).append("\n");
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
    openapiFields.add("emailAddressRequired");
    openapiFields.add("invoiceAddressRequired");
    openapiFields.add("mailingAddressRequired");
    openapiFields.add("mobilePhoneNumberRequired");
    openapiFields.add("phoneCountryCodeRequired");
    openapiFields.add("phoneNumberRequired");
    openapiFields.add("postalCodeRequired");
    openapiFields.add("travelerRequirements");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BookingRequirements
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BookingRequirements.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BookingRequirements is not found in the empty JSON string", BookingRequirements.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BookingRequirements.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BookingRequirements` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("travelerRequirements") != null && !jsonObj.get("travelerRequirements").isJsonNull()) {
        JsonArray jsonArraytravelerRequirements = jsonObj.getAsJsonArray("travelerRequirements");
        if (jsonArraytravelerRequirements != null) {
          // ensure the json data is an array
          if (!jsonObj.get("travelerRequirements").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `travelerRequirements` to be an array in the JSON string but got `%s`", jsonObj.get("travelerRequirements").toString()));
          }

          // validate the optional field `travelerRequirements` (array)
          for (int i = 0; i < jsonArraytravelerRequirements.size(); i++) {
            PassengerConditions.validateJsonElement(jsonArraytravelerRequirements.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BookingRequirements.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BookingRequirements' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BookingRequirements> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BookingRequirements.class));

       return (TypeAdapter<T>) new TypeAdapter<BookingRequirements>() {
           @Override
           public void write(JsonWriter out, BookingRequirements value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BookingRequirements read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BookingRequirements given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BookingRequirements
   * @throws IOException if the JSON string is invalid with respect to BookingRequirements
   */
  public static BookingRequirements fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BookingRequirements.class);
  }

  /**
   * Convert an instance of BookingRequirements to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

