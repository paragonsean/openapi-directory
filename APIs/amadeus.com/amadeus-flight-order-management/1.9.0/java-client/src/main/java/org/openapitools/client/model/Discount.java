/*
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
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
import org.openapitools.client.model.DiscountTravelerType;
import org.openapitools.client.model.DiscountType;

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
 * traveler discount
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:54.608298-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Discount {
  public static final String SERIALIZED_NAME_CARD_NUMBER = "cardNumber";
  @SerializedName(SERIALIZED_NAME_CARD_NUMBER)
  private String cardNumber;

  public static final String SERIALIZED_NAME_CERTIFICATE_NUMBER = "certificateNumber";
  @SerializedName(SERIALIZED_NAME_CERTIFICATE_NUMBER)
  private String certificateNumber;

  public static final String SERIALIZED_NAME_CITY_NAME = "cityName";
  @SerializedName(SERIALIZED_NAME_CITY_NAME)
  private String cityName;

  public static final String SERIALIZED_NAME_SUB_TYPE = "subType";
  @SerializedName(SERIALIZED_NAME_SUB_TYPE)
  private DiscountType subType;

  public static final String SERIALIZED_NAME_TRAVELER_TYPE = "travelerType";
  @SerializedName(SERIALIZED_NAME_TRAVELER_TYPE)
  private DiscountTravelerType travelerType;

  public Discount() {
  }

  public Discount cardNumber(String cardNumber) {
    this.cardNumber = cardNumber;
    return this;
  }

  /**
   * resident card number
   * @return cardNumber
   */
  @javax.annotation.Nullable
  public String getCardNumber() {
    return cardNumber;
  }

  public void setCardNumber(String cardNumber) {
    this.cardNumber = cardNumber;
  }


  public Discount certificateNumber(String certificateNumber) {
    this.certificateNumber = certificateNumber;
    return this;
  }

  /**
   * resident certificate number
   * @return certificateNumber
   */
  @javax.annotation.Nullable
  public String getCertificateNumber() {
    return certificateNumber;
  }

  public void setCertificateNumber(String certificateNumber) {
    this.certificateNumber = certificateNumber;
  }


  public Discount cityName(String cityName) {
    this.cityName = cityName;
    return this;
  }

  /**
   * city of residence
   * @return cityName
   */
  @javax.annotation.Nullable
  public String getCityName() {
    return cityName;
  }

  public void setCityName(String cityName) {
    this.cityName = cityName;
  }


  public Discount subType(DiscountType subType) {
    this.subType = subType;
    return this;
  }

  /**
   * Get subType
   * @return subType
   */
  @javax.annotation.Nullable
  public DiscountType getSubType() {
    return subType;
  }

  public void setSubType(DiscountType subType) {
    this.subType = subType;
  }


  public Discount travelerType(DiscountTravelerType travelerType) {
    this.travelerType = travelerType;
    return this;
  }

  /**
   * Get travelerType
   * @return travelerType
   */
  @javax.annotation.Nullable
  public DiscountTravelerType getTravelerType() {
    return travelerType;
  }

  public void setTravelerType(DiscountTravelerType travelerType) {
    this.travelerType = travelerType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Discount discount = (Discount) o;
    return Objects.equals(this.cardNumber, discount.cardNumber) &&
        Objects.equals(this.certificateNumber, discount.certificateNumber) &&
        Objects.equals(this.cityName, discount.cityName) &&
        Objects.equals(this.subType, discount.subType) &&
        Objects.equals(this.travelerType, discount.travelerType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cardNumber, certificateNumber, cityName, subType, travelerType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Discount {\n");
    sb.append("    cardNumber: ").append(toIndentedString(cardNumber)).append("\n");
    sb.append("    certificateNumber: ").append(toIndentedString(certificateNumber)).append("\n");
    sb.append("    cityName: ").append(toIndentedString(cityName)).append("\n");
    sb.append("    subType: ").append(toIndentedString(subType)).append("\n");
    sb.append("    travelerType: ").append(toIndentedString(travelerType)).append("\n");
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
    openapiFields.add("cardNumber");
    openapiFields.add("certificateNumber");
    openapiFields.add("cityName");
    openapiFields.add("subType");
    openapiFields.add("travelerType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Discount
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Discount.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Discount is not found in the empty JSON string", Discount.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Discount.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Discount` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("cardNumber") != null && !jsonObj.get("cardNumber").isJsonNull()) && !jsonObj.get("cardNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cardNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cardNumber").toString()));
      }
      if ((jsonObj.get("certificateNumber") != null && !jsonObj.get("certificateNumber").isJsonNull()) && !jsonObj.get("certificateNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `certificateNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("certificateNumber").toString()));
      }
      if ((jsonObj.get("cityName") != null && !jsonObj.get("cityName").isJsonNull()) && !jsonObj.get("cityName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cityName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cityName").toString()));
      }
      // validate the optional field `subType`
      if (jsonObj.get("subType") != null && !jsonObj.get("subType").isJsonNull()) {
        DiscountType.validateJsonElement(jsonObj.get("subType"));
      }
      // validate the optional field `travelerType`
      if (jsonObj.get("travelerType") != null && !jsonObj.get("travelerType").isJsonNull()) {
        DiscountTravelerType.validateJsonElement(jsonObj.get("travelerType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Discount.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Discount' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Discount> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Discount.class));

       return (TypeAdapter<T>) new TypeAdapter<Discount>() {
           @Override
           public void write(JsonWriter out, Discount value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Discount read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Discount given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Discount
   * @throws IOException if the JSON string is invalid with respect to Discount
   */
  public static Discount fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Discount.class);
  }

  /**
   * Convert an instance of Discount to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

