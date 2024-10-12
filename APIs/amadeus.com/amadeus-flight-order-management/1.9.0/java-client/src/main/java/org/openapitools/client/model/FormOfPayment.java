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
import org.openapitools.client.model.B2bWallet;
import org.openapitools.client.model.CreditCard;
import org.openapitools.client.model.OtherMethod;

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
 * form of payment used
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:54.608298-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FormOfPayment {
  public static final String SERIALIZED_NAME_B2B_WALLET = "b2bWallet";
  @SerializedName(SERIALIZED_NAME_B2B_WALLET)
  private B2bWallet b2bWallet;

  public static final String SERIALIZED_NAME_CREDIT_CARD = "creditCard";
  @SerializedName(SERIALIZED_NAME_CREDIT_CARD)
  private CreditCard creditCard;

  public static final String SERIALIZED_NAME_OTHER = "other";
  @SerializedName(SERIALIZED_NAME_OTHER)
  private OtherMethod other;

  public FormOfPayment() {
  }

  public FormOfPayment b2bWallet(B2bWallet b2bWallet) {
    this.b2bWallet = b2bWallet;
    return this;
  }

  /**
   * Get b2bWallet
   * @return b2bWallet
   */
  @javax.annotation.Nullable
  public B2bWallet getB2bWallet() {
    return b2bWallet;
  }

  public void setB2bWallet(B2bWallet b2bWallet) {
    this.b2bWallet = b2bWallet;
  }


  public FormOfPayment creditCard(CreditCard creditCard) {
    this.creditCard = creditCard;
    return this;
  }

  /**
   * Get creditCard
   * @return creditCard
   */
  @javax.annotation.Nullable
  public CreditCard getCreditCard() {
    return creditCard;
  }

  public void setCreditCard(CreditCard creditCard) {
    this.creditCard = creditCard;
  }


  public FormOfPayment other(OtherMethod other) {
    this.other = other;
    return this;
  }

  /**
   * Get other
   * @return other
   */
  @javax.annotation.Nullable
  public OtherMethod getOther() {
    return other;
  }

  public void setOther(OtherMethod other) {
    this.other = other;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FormOfPayment formOfPayment = (FormOfPayment) o;
    return Objects.equals(this.b2bWallet, formOfPayment.b2bWallet) &&
        Objects.equals(this.creditCard, formOfPayment.creditCard) &&
        Objects.equals(this.other, formOfPayment.other);
  }

  @Override
  public int hashCode() {
    return Objects.hash(b2bWallet, creditCard, other);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FormOfPayment {\n");
    sb.append("    b2bWallet: ").append(toIndentedString(b2bWallet)).append("\n");
    sb.append("    creditCard: ").append(toIndentedString(creditCard)).append("\n");
    sb.append("    other: ").append(toIndentedString(other)).append("\n");
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
    openapiFields.add("b2bWallet");
    openapiFields.add("creditCard");
    openapiFields.add("other");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FormOfPayment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FormOfPayment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FormOfPayment is not found in the empty JSON string", FormOfPayment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FormOfPayment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FormOfPayment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `b2bWallet`
      if (jsonObj.get("b2bWallet") != null && !jsonObj.get("b2bWallet").isJsonNull()) {
        B2bWallet.validateJsonElement(jsonObj.get("b2bWallet"));
      }
      // validate the optional field `creditCard`
      if (jsonObj.get("creditCard") != null && !jsonObj.get("creditCard").isJsonNull()) {
        CreditCard.validateJsonElement(jsonObj.get("creditCard"));
      }
      // validate the optional field `other`
      if (jsonObj.get("other") != null && !jsonObj.get("other").isJsonNull()) {
        OtherMethod.validateJsonElement(jsonObj.get("other"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FormOfPayment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FormOfPayment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FormOfPayment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FormOfPayment.class));

       return (TypeAdapter<T>) new TypeAdapter<FormOfPayment>() {
           @Override
           public void write(JsonWriter out, FormOfPayment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FormOfPayment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FormOfPayment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FormOfPayment
   * @throws IOException if the JSON string is invalid with respect to FormOfPayment
   */
  public static FormOfPayment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FormOfPayment.class);
  }

  /**
   * Convert an instance of FormOfPayment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

