/*
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
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
import java.util.UUID;
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
 * PaymentDeltaV1
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:55.204956-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PaymentDeltaV1 {
  public static final String SERIALIZED_NAME_PAYMENT_AMOUNT = "paymentAmount";
  @SerializedName(SERIALIZED_NAME_PAYMENT_AMOUNT)
  private Integer paymentAmount;

  public static final String SERIALIZED_NAME_PAYMENT_CURRENCY = "paymentCurrency";
  @SerializedName(SERIALIZED_NAME_PAYMENT_CURRENCY)
  private String paymentCurrency;

  public static final String SERIALIZED_NAME_PAYMENT_ID = "paymentId";
  @SerializedName(SERIALIZED_NAME_PAYMENT_ID)
  private UUID paymentId;

  public static final String SERIALIZED_NAME_PAYOR_PAYMENT_ID = "payorPaymentId";
  @SerializedName(SERIALIZED_NAME_PAYOR_PAYMENT_ID)
  private String payorPaymentId;

  public static final String SERIALIZED_NAME_PAYOUT_ID = "payoutId";
  @SerializedName(SERIALIZED_NAME_PAYOUT_ID)
  private UUID payoutId;

  public static final String SERIALIZED_NAME_SOURCE_AMOUNT = "sourceAmount";
  @SerializedName(SERIALIZED_NAME_SOURCE_AMOUNT)
  private Integer sourceAmount;

  public static final String SERIALIZED_NAME_SOURCE_CURRENCY = "sourceCurrency";
  @SerializedName(SERIALIZED_NAME_SOURCE_CURRENCY)
  private String sourceCurrency;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public PaymentDeltaV1() {
  }

  public PaymentDeltaV1(
     UUID paymentId, 
     UUID payoutId
  ) {
    this();
    this.paymentId = paymentId;
    this.payoutId = payoutId;
  }

  public PaymentDeltaV1 paymentAmount(Integer paymentAmount) {
    this.paymentAmount = paymentAmount;
    return this;
  }

  /**
   * Get paymentAmount
   * @return paymentAmount
   */
  @javax.annotation.Nullable
  public Integer getPaymentAmount() {
    return paymentAmount;
  }

  public void setPaymentAmount(Integer paymentAmount) {
    this.paymentAmount = paymentAmount;
  }


  public PaymentDeltaV1 paymentCurrency(String paymentCurrency) {
    this.paymentCurrency = paymentCurrency;
    return this;
  }

  /**
   * Get paymentCurrency
   * @return paymentCurrency
   */
  @javax.annotation.Nullable
  public String getPaymentCurrency() {
    return paymentCurrency;
  }

  public void setPaymentCurrency(String paymentCurrency) {
    this.paymentCurrency = paymentCurrency;
  }


  /**
   * Get paymentId
   * @return paymentId
   */
  @javax.annotation.Nonnull
  public UUID getPaymentId() {
    return paymentId;
  }



  public PaymentDeltaV1 payorPaymentId(String payorPaymentId) {
    this.payorPaymentId = payorPaymentId;
    return this;
  }

  /**
   * Get payorPaymentId
   * @return payorPaymentId
   */
  @javax.annotation.Nullable
  public String getPayorPaymentId() {
    return payorPaymentId;
  }

  public void setPayorPaymentId(String payorPaymentId) {
    this.payorPaymentId = payorPaymentId;
  }


  /**
   * Get payoutId
   * @return payoutId
   */
  @javax.annotation.Nonnull
  public UUID getPayoutId() {
    return payoutId;
  }



  public PaymentDeltaV1 sourceAmount(Integer sourceAmount) {
    this.sourceAmount = sourceAmount;
    return this;
  }

  /**
   * Get sourceAmount
   * @return sourceAmount
   */
  @javax.annotation.Nullable
  public Integer getSourceAmount() {
    return sourceAmount;
  }

  public void setSourceAmount(Integer sourceAmount) {
    this.sourceAmount = sourceAmount;
  }


  public PaymentDeltaV1 sourceCurrency(String sourceCurrency) {
    this.sourceCurrency = sourceCurrency;
    return this;
  }

  /**
   * Get sourceCurrency
   * @return sourceCurrency
   */
  @javax.annotation.Nullable
  public String getSourceCurrency() {
    return sourceCurrency;
  }

  public void setSourceCurrency(String sourceCurrency) {
    this.sourceCurrency = sourceCurrency;
  }


  public PaymentDeltaV1 status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PaymentDeltaV1 paymentDeltaV1 = (PaymentDeltaV1) o;
    return Objects.equals(this.paymentAmount, paymentDeltaV1.paymentAmount) &&
        Objects.equals(this.paymentCurrency, paymentDeltaV1.paymentCurrency) &&
        Objects.equals(this.paymentId, paymentDeltaV1.paymentId) &&
        Objects.equals(this.payorPaymentId, paymentDeltaV1.payorPaymentId) &&
        Objects.equals(this.payoutId, paymentDeltaV1.payoutId) &&
        Objects.equals(this.sourceAmount, paymentDeltaV1.sourceAmount) &&
        Objects.equals(this.sourceCurrency, paymentDeltaV1.sourceCurrency) &&
        Objects.equals(this.status, paymentDeltaV1.status);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(paymentAmount, paymentCurrency, paymentId, payorPaymentId, payoutId, sourceAmount, sourceCurrency, status);
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
    sb.append("class PaymentDeltaV1 {\n");
    sb.append("    paymentAmount: ").append(toIndentedString(paymentAmount)).append("\n");
    sb.append("    paymentCurrency: ").append(toIndentedString(paymentCurrency)).append("\n");
    sb.append("    paymentId: ").append(toIndentedString(paymentId)).append("\n");
    sb.append("    payorPaymentId: ").append(toIndentedString(payorPaymentId)).append("\n");
    sb.append("    payoutId: ").append(toIndentedString(payoutId)).append("\n");
    sb.append("    sourceAmount: ").append(toIndentedString(sourceAmount)).append("\n");
    sb.append("    sourceCurrency: ").append(toIndentedString(sourceCurrency)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("paymentAmount");
    openapiFields.add("paymentCurrency");
    openapiFields.add("paymentId");
    openapiFields.add("payorPaymentId");
    openapiFields.add("payoutId");
    openapiFields.add("sourceAmount");
    openapiFields.add("sourceCurrency");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("paymentId");
    openapiRequiredFields.add("payoutId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PaymentDeltaV1
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PaymentDeltaV1.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PaymentDeltaV1 is not found in the empty JSON string", PaymentDeltaV1.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PaymentDeltaV1.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PaymentDeltaV1` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PaymentDeltaV1.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("paymentCurrency") != null && !jsonObj.get("paymentCurrency").isJsonNull()) && !jsonObj.get("paymentCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentCurrency").toString()));
      }
      if (!jsonObj.get("paymentId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentId").toString()));
      }
      if ((jsonObj.get("payorPaymentId") != null && !jsonObj.get("payorPaymentId").isJsonNull()) && !jsonObj.get("payorPaymentId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payorPaymentId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payorPaymentId").toString()));
      }
      if (!jsonObj.get("payoutId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payoutId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payoutId").toString()));
      }
      if ((jsonObj.get("sourceCurrency") != null && !jsonObj.get("sourceCurrency").isJsonNull()) && !jsonObj.get("sourceCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceCurrency").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PaymentDeltaV1.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PaymentDeltaV1' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PaymentDeltaV1> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PaymentDeltaV1.class));

       return (TypeAdapter<T>) new TypeAdapter<PaymentDeltaV1>() {
           @Override
           public void write(JsonWriter out, PaymentDeltaV1 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PaymentDeltaV1 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PaymentDeltaV1 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PaymentDeltaV1
   * @throws IOException if the JSON string is invalid with respect to PaymentDeltaV1
   */
  public static PaymentDeltaV1 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PaymentDeltaV1.class);
  }

  /**
   * Convert an instance of PaymentDeltaV1 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

