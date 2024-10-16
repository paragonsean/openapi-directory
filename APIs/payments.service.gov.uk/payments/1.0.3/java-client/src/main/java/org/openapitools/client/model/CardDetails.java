/*
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
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
import org.openapitools.client.model.Address;

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
 * A structure representing the payment card
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:25.328324-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CardDetails {
  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billing_address";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private Address billingAddress;

  public static final String SERIALIZED_NAME_CARD_BRAND = "card_brand";
  @SerializedName(SERIALIZED_NAME_CARD_BRAND)
  private String cardBrand;

  /**
   * The card type, &#x60;debit&#x60; or &#x60;credit&#x60; or &#x60;null&#x60; if not able to determine
   */
  @JsonAdapter(CardTypeEnum.Adapter.class)
  public enum CardTypeEnum {
    DEBIT("debit"),
    
    CREDIT("credit"),
    
    NULL("null");

    private String value;

    CardTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CardTypeEnum fromValue(String value) {
      for (CardTypeEnum b : CardTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CardTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CardTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CardTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CardTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CardTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CARD_TYPE = "card_type";
  @SerializedName(SERIALIZED_NAME_CARD_TYPE)
  private CardTypeEnum cardType;

  public static final String SERIALIZED_NAME_CARDHOLDER_NAME = "cardholder_name";
  @SerializedName(SERIALIZED_NAME_CARDHOLDER_NAME)
  private String cardholderName;

  public static final String SERIALIZED_NAME_EXPIRY_DATE = "expiry_date";
  @SerializedName(SERIALIZED_NAME_EXPIRY_DATE)
  private String expiryDate;

  public static final String SERIALIZED_NAME_FIRST_DIGITS_CARD_NUMBER = "first_digits_card_number";
  @SerializedName(SERIALIZED_NAME_FIRST_DIGITS_CARD_NUMBER)
  private String firstDigitsCardNumber;

  public static final String SERIALIZED_NAME_LAST_DIGITS_CARD_NUMBER = "last_digits_card_number";
  @SerializedName(SERIALIZED_NAME_LAST_DIGITS_CARD_NUMBER)
  private String lastDigitsCardNumber;

  public CardDetails() {
  }

  public CardDetails(
     String cardBrand, 
     CardTypeEnum cardType, 
     String cardholderName, 
     String expiryDate, 
     String firstDigitsCardNumber, 
     String lastDigitsCardNumber
  ) {
    this();
    this.cardBrand = cardBrand;
    this.cardType = cardType;
    this.cardholderName = cardholderName;
    this.expiryDate = expiryDate;
    this.firstDigitsCardNumber = firstDigitsCardNumber;
    this.lastDigitsCardNumber = lastDigitsCardNumber;
  }

  public CardDetails billingAddress(Address billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Get billingAddress
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public Address getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(Address billingAddress) {
    this.billingAddress = billingAddress;
  }


  /**
   * Get cardBrand
   * @return cardBrand
   */
  @javax.annotation.Nullable
  public String getCardBrand() {
    return cardBrand;
  }



  /**
   * The card type, &#x60;debit&#x60; or &#x60;credit&#x60; or &#x60;null&#x60; if not able to determine
   * @return cardType
   */
  @javax.annotation.Nullable
  public CardTypeEnum getCardType() {
    return cardType;
  }



  /**
   * Get cardholderName
   * @return cardholderName
   */
  @javax.annotation.Nullable
  public String getCardholderName() {
    return cardholderName;
  }



  /**
   * The expiry date of the card in MM/yy format
   * @return expiryDate
   */
  @javax.annotation.Nullable
  public String getExpiryDate() {
    return expiryDate;
  }



  /**
   * Get firstDigitsCardNumber
   * @return firstDigitsCardNumber
   */
  @javax.annotation.Nullable
  public String getFirstDigitsCardNumber() {
    return firstDigitsCardNumber;
  }



  /**
   * Get lastDigitsCardNumber
   * @return lastDigitsCardNumber
   */
  @javax.annotation.Nullable
  public String getLastDigitsCardNumber() {
    return lastDigitsCardNumber;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CardDetails cardDetails = (CardDetails) o;
    return Objects.equals(this.billingAddress, cardDetails.billingAddress) &&
        Objects.equals(this.cardBrand, cardDetails.cardBrand) &&
        Objects.equals(this.cardType, cardDetails.cardType) &&
        Objects.equals(this.cardholderName, cardDetails.cardholderName) &&
        Objects.equals(this.expiryDate, cardDetails.expiryDate) &&
        Objects.equals(this.firstDigitsCardNumber, cardDetails.firstDigitsCardNumber) &&
        Objects.equals(this.lastDigitsCardNumber, cardDetails.lastDigitsCardNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(billingAddress, cardBrand, cardType, cardholderName, expiryDate, firstDigitsCardNumber, lastDigitsCardNumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CardDetails {\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    cardBrand: ").append(toIndentedString(cardBrand)).append("\n");
    sb.append("    cardType: ").append(toIndentedString(cardType)).append("\n");
    sb.append("    cardholderName: ").append(toIndentedString(cardholderName)).append("\n");
    sb.append("    expiryDate: ").append(toIndentedString(expiryDate)).append("\n");
    sb.append("    firstDigitsCardNumber: ").append(toIndentedString(firstDigitsCardNumber)).append("\n");
    sb.append("    lastDigitsCardNumber: ").append(toIndentedString(lastDigitsCardNumber)).append("\n");
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
    openapiFields.add("billing_address");
    openapiFields.add("card_brand");
    openapiFields.add("card_type");
    openapiFields.add("cardholder_name");
    openapiFields.add("expiry_date");
    openapiFields.add("first_digits_card_number");
    openapiFields.add("last_digits_card_number");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CardDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CardDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CardDetails is not found in the empty JSON string", CardDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CardDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CardDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `billing_address`
      if (jsonObj.get("billing_address") != null && !jsonObj.get("billing_address").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("billing_address"));
      }
      if ((jsonObj.get("card_brand") != null && !jsonObj.get("card_brand").isJsonNull()) && !jsonObj.get("card_brand").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `card_brand` to be a primitive type in the JSON string but got `%s`", jsonObj.get("card_brand").toString()));
      }
      if ((jsonObj.get("card_type") != null && !jsonObj.get("card_type").isJsonNull()) && !jsonObj.get("card_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `card_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("card_type").toString()));
      }
      // validate the optional field `card_type`
      if (jsonObj.get("card_type") != null && !jsonObj.get("card_type").isJsonNull()) {
        CardTypeEnum.validateJsonElement(jsonObj.get("card_type"));
      }
      if ((jsonObj.get("cardholder_name") != null && !jsonObj.get("cardholder_name").isJsonNull()) && !jsonObj.get("cardholder_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cardholder_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cardholder_name").toString()));
      }
      if ((jsonObj.get("expiry_date") != null && !jsonObj.get("expiry_date").isJsonNull()) && !jsonObj.get("expiry_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `expiry_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("expiry_date").toString()));
      }
      if ((jsonObj.get("first_digits_card_number") != null && !jsonObj.get("first_digits_card_number").isJsonNull()) && !jsonObj.get("first_digits_card_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_digits_card_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_digits_card_number").toString()));
      }
      if ((jsonObj.get("last_digits_card_number") != null && !jsonObj.get("last_digits_card_number").isJsonNull()) && !jsonObj.get("last_digits_card_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_digits_card_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_digits_card_number").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CardDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CardDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CardDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CardDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<CardDetails>() {
           @Override
           public void write(JsonWriter out, CardDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CardDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CardDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CardDetails
   * @throws IOException if the JSON string is invalid with respect to CardDetails
   */
  public static CardDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CardDetails.class);
  }

  /**
   * Convert an instance of CardDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

