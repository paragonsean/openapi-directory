/*
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
import org.openapitools.client.model.EndpointGetUsersIDSynergiesDataInnerMeetPayment;

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
 * EndpointGetUsersIDSynergiesDataInnerMeet
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:21.899808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EndpointGetUsersIDSynergiesDataInnerMeet {
  public static final String SERIALIZED_NAME_PAYMENT = "payment";
  @SerializedName(SERIALIZED_NAME_PAYMENT)
  private EndpointGetUsersIDSynergiesDataInnerMeetPayment payment;

  public static final String SERIALIZED_NAME_PRICE_USD = "price_usd";
  @SerializedName(SERIALIZED_NAME_PRICE_USD)
  private Float priceUsd;

  public EndpointGetUsersIDSynergiesDataInnerMeet() {
  }

  public EndpointGetUsersIDSynergiesDataInnerMeet payment(EndpointGetUsersIDSynergiesDataInnerMeetPayment payment) {
    this.payment = payment;
    return this;
  }

  /**
   * Get payment
   * @return payment
   */
  @javax.annotation.Nullable
  public EndpointGetUsersIDSynergiesDataInnerMeetPayment getPayment() {
    return payment;
  }

  public void setPayment(EndpointGetUsersIDSynergiesDataInnerMeetPayment payment) {
    this.payment = payment;
  }


  public EndpointGetUsersIDSynergiesDataInnerMeet priceUsd(Float priceUsd) {
    this.priceUsd = priceUsd;
    return this;
  }

  /**
   * Get priceUsd
   * @return priceUsd
   */
  @javax.annotation.Nullable
  public Float getPriceUsd() {
    return priceUsd;
  }

  public void setPriceUsd(Float priceUsd) {
    this.priceUsd = priceUsd;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EndpointGetUsersIDSynergiesDataInnerMeet endpointGetUsersIDSynergiesDataInnerMeet = (EndpointGetUsersIDSynergiesDataInnerMeet) o;
    return Objects.equals(this.payment, endpointGetUsersIDSynergiesDataInnerMeet.payment) &&
        Objects.equals(this.priceUsd, endpointGetUsersIDSynergiesDataInnerMeet.priceUsd);
  }

  @Override
  public int hashCode() {
    return Objects.hash(payment, priceUsd);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EndpointGetUsersIDSynergiesDataInnerMeet {\n");
    sb.append("    payment: ").append(toIndentedString(payment)).append("\n");
    sb.append("    priceUsd: ").append(toIndentedString(priceUsd)).append("\n");
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
    openapiFields.add("payment");
    openapiFields.add("price_usd");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EndpointGetUsersIDSynergiesDataInnerMeet
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EndpointGetUsersIDSynergiesDataInnerMeet.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EndpointGetUsersIDSynergiesDataInnerMeet is not found in the empty JSON string", EndpointGetUsersIDSynergiesDataInnerMeet.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EndpointGetUsersIDSynergiesDataInnerMeet.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EndpointGetUsersIDSynergiesDataInnerMeet` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `payment`
      if (jsonObj.get("payment") != null && !jsonObj.get("payment").isJsonNull()) {
        EndpointGetUsersIDSynergiesDataInnerMeetPayment.validateJsonElement(jsonObj.get("payment"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EndpointGetUsersIDSynergiesDataInnerMeet.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EndpointGetUsersIDSynergiesDataInnerMeet' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EndpointGetUsersIDSynergiesDataInnerMeet> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EndpointGetUsersIDSynergiesDataInnerMeet.class));

       return (TypeAdapter<T>) new TypeAdapter<EndpointGetUsersIDSynergiesDataInnerMeet>() {
           @Override
           public void write(JsonWriter out, EndpointGetUsersIDSynergiesDataInnerMeet value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EndpointGetUsersIDSynergiesDataInnerMeet read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EndpointGetUsersIDSynergiesDataInnerMeet given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EndpointGetUsersIDSynergiesDataInnerMeet
   * @throws IOException if the JSON string is invalid with respect to EndpointGetUsersIDSynergiesDataInnerMeet
   */
  public static EndpointGetUsersIDSynergiesDataInnerMeet fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EndpointGetUsersIDSynergiesDataInnerMeet.class);
  }

  /**
   * Convert an instance of EndpointGetUsersIDSynergiesDataInnerMeet to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

