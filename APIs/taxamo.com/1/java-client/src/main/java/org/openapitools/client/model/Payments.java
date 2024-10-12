/*
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
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
import java.math.BigDecimal;
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
 * Payments
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Payments {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_PAYMENT_INFORMATION = "payment_information";
  @SerializedName(SERIALIZED_NAME_PAYMENT_INFORMATION)
  private String paymentInformation;

  public static final String SERIALIZED_NAME_PAYMENT_TIMESTAMP = "payment_timestamp";
  @SerializedName(SERIALIZED_NAME_PAYMENT_TIMESTAMP)
  private String paymentTimestamp;

  public Payments() {
  }

  public Payments amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Amount that has been paid. Use negative value to register refunds.
   * @return amount
   */
  @javax.annotation.Nullable
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public Payments paymentInformation(String paymentInformation) {
    this.paymentInformation = paymentInformation;
    return this;
  }

  /**
   * Additional payment information.
   * @return paymentInformation
   */
  @javax.annotation.Nullable
  public String getPaymentInformation() {
    return paymentInformation;
  }

  public void setPaymentInformation(String paymentInformation) {
    this.paymentInformation = paymentInformation;
  }


  public Payments paymentTimestamp(String paymentTimestamp) {
    this.paymentTimestamp = paymentTimestamp;
    return this;
  }

  /**
   * When the payment was received in yyyy-MM-dd HH:mm:ss (24 hour format, UTC+0 timezone).
   * @return paymentTimestamp
   */
  @javax.annotation.Nullable
  public String getPaymentTimestamp() {
    return paymentTimestamp;
  }

  public void setPaymentTimestamp(String paymentTimestamp) {
    this.paymentTimestamp = paymentTimestamp;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Payments payments = (Payments) o;
    return Objects.equals(this.amount, payments.amount) &&
        Objects.equals(this.paymentInformation, payments.paymentInformation) &&
        Objects.equals(this.paymentTimestamp, payments.paymentTimestamp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, paymentInformation, paymentTimestamp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Payments {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    paymentInformation: ").append(toIndentedString(paymentInformation)).append("\n");
    sb.append("    paymentTimestamp: ").append(toIndentedString(paymentTimestamp)).append("\n");
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
    openapiFields.add("amount");
    openapiFields.add("payment_information");
    openapiFields.add("payment_timestamp");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Payments
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Payments.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Payments is not found in the empty JSON string", Payments.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Payments.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Payments` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("payment_information") != null && !jsonObj.get("payment_information").isJsonNull()) && !jsonObj.get("payment_information").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_information` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_information").toString()));
      }
      if ((jsonObj.get("payment_timestamp") != null && !jsonObj.get("payment_timestamp").isJsonNull()) && !jsonObj.get("payment_timestamp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_timestamp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_timestamp").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Payments.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Payments' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Payments> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Payments.class));

       return (TypeAdapter<T>) new TypeAdapter<Payments>() {
           @Override
           public void write(JsonWriter out, Payments value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Payments read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Payments given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Payments
   * @throws IOException if the JSON string is invalid with respect to Payments
   */
  public static Payments fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Payments.class);
  }

  /**
   * Convert an instance of Payments to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

