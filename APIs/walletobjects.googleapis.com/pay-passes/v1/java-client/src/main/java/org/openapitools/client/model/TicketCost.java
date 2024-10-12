/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
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
import org.openapitools.client.model.LocalizedString;
import org.openapitools.client.model.Money;

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
 * TicketCost
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TicketCost {
  public static final String SERIALIZED_NAME_DISCOUNT_MESSAGE = "discountMessage";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_MESSAGE)
  private LocalizedString discountMessage;

  public static final String SERIALIZED_NAME_FACE_VALUE = "faceValue";
  @SerializedName(SERIALIZED_NAME_FACE_VALUE)
  private Money faceValue;

  public static final String SERIALIZED_NAME_PURCHASE_PRICE = "purchasePrice";
  @SerializedName(SERIALIZED_NAME_PURCHASE_PRICE)
  private Money purchasePrice;

  public TicketCost() {
  }

  public TicketCost discountMessage(LocalizedString discountMessage) {
    this.discountMessage = discountMessage;
    return this;
  }

  /**
   * Get discountMessage
   * @return discountMessage
   */
  @javax.annotation.Nullable
  public LocalizedString getDiscountMessage() {
    return discountMessage;
  }

  public void setDiscountMessage(LocalizedString discountMessage) {
    this.discountMessage = discountMessage;
  }


  public TicketCost faceValue(Money faceValue) {
    this.faceValue = faceValue;
    return this;
  }

  /**
   * Get faceValue
   * @return faceValue
   */
  @javax.annotation.Nullable
  public Money getFaceValue() {
    return faceValue;
  }

  public void setFaceValue(Money faceValue) {
    this.faceValue = faceValue;
  }


  public TicketCost purchasePrice(Money purchasePrice) {
    this.purchasePrice = purchasePrice;
    return this;
  }

  /**
   * Get purchasePrice
   * @return purchasePrice
   */
  @javax.annotation.Nullable
  public Money getPurchasePrice() {
    return purchasePrice;
  }

  public void setPurchasePrice(Money purchasePrice) {
    this.purchasePrice = purchasePrice;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TicketCost ticketCost = (TicketCost) o;
    return Objects.equals(this.discountMessage, ticketCost.discountMessage) &&
        Objects.equals(this.faceValue, ticketCost.faceValue) &&
        Objects.equals(this.purchasePrice, ticketCost.purchasePrice);
  }

  @Override
  public int hashCode() {
    return Objects.hash(discountMessage, faceValue, purchasePrice);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TicketCost {\n");
    sb.append("    discountMessage: ").append(toIndentedString(discountMessage)).append("\n");
    sb.append("    faceValue: ").append(toIndentedString(faceValue)).append("\n");
    sb.append("    purchasePrice: ").append(toIndentedString(purchasePrice)).append("\n");
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
    openapiFields.add("discountMessage");
    openapiFields.add("faceValue");
    openapiFields.add("purchasePrice");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TicketCost
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TicketCost.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TicketCost is not found in the empty JSON string", TicketCost.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TicketCost.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TicketCost` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `discountMessage`
      if (jsonObj.get("discountMessage") != null && !jsonObj.get("discountMessage").isJsonNull()) {
        LocalizedString.validateJsonElement(jsonObj.get("discountMessage"));
      }
      // validate the optional field `faceValue`
      if (jsonObj.get("faceValue") != null && !jsonObj.get("faceValue").isJsonNull()) {
        Money.validateJsonElement(jsonObj.get("faceValue"));
      }
      // validate the optional field `purchasePrice`
      if (jsonObj.get("purchasePrice") != null && !jsonObj.get("purchasePrice").isJsonNull()) {
        Money.validateJsonElement(jsonObj.get("purchasePrice"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TicketCost.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TicketCost' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TicketCost> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TicketCost.class));

       return (TypeAdapter<T>) new TypeAdapter<TicketCost>() {
           @Override
           public void write(JsonWriter out, TicketCost value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TicketCost read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TicketCost given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TicketCost
   * @throws IOException if the JSON string is invalid with respect to TicketCost
   */
  public static TicketCost fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TicketCost.class);
  }

  /**
   * Convert an instance of TicketCost to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

