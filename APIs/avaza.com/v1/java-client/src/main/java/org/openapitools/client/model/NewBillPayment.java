/*
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.NewBillPaymentAllocation;

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
 * NewBillPayment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NewBillPayment {
  public static final String SERIALIZED_NAME_AMOUNT = "Amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_COMPANY_I_D_F_K = "CompanyIDFK";
  @SerializedName(SERIALIZED_NAME_COMPANY_I_D_F_K)
  private Integer companyIDFK;

  public static final String SERIALIZED_NAME_CURRENCY_CODE = "CurrencyCode";
  @SerializedName(SERIALIZED_NAME_CURRENCY_CODE)
  private String currencyCode;

  public static final String SERIALIZED_NAME_DATE_ISSUED = "DateIssued";
  @SerializedName(SERIALIZED_NAME_DATE_ISSUED)
  private OffsetDateTime dateIssued;

  public static final String SERIALIZED_NAME_EXCHANGE_RATE = "ExchangeRate";
  @SerializedName(SERIALIZED_NAME_EXCHANGE_RATE)
  private Double exchangeRate;

  public static final String SERIALIZED_NAME_NOTES = "Notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PAYMENT_ALLOCATIONS = "PaymentAllocations";
  @SerializedName(SERIALIZED_NAME_PAYMENT_ALLOCATIONS)
  private List<NewBillPaymentAllocation> paymentAllocations = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAYMENT_NUMBER = "PaymentNumber";
  @SerializedName(SERIALIZED_NAME_PAYMENT_NUMBER)
  private String paymentNumber;

  public static final String SERIALIZED_NAME_PAYMENT_PROVIDER_CODE = "PaymentProviderCode";
  @SerializedName(SERIALIZED_NAME_PAYMENT_PROVIDER_CODE)
  private String paymentProviderCode;

  public static final String SERIALIZED_NAME_TRANSACTION_PREFIX = "TransactionPrefix";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_PREFIX)
  private String transactionPrefix;

  public static final String SERIALIZED_NAME_TRANSACTION_REFERENCE = "TransactionReference";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_REFERENCE)
  private String transactionReference;

  public NewBillPayment() {
  }

  public NewBillPayment amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Get amount
   * @return amount
   */
  @javax.annotation.Nullable
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public NewBillPayment companyIDFK(Integer companyIDFK) {
    this.companyIDFK = companyIDFK;
    return this;
  }

  /**
   * Only required if no invoice allocations specified.
   * @return companyIDFK
   */
  @javax.annotation.Nullable
  public Integer getCompanyIDFK() {
    return companyIDFK;
  }

  public void setCompanyIDFK(Integer companyIDFK) {
    this.companyIDFK = companyIDFK;
  }


  public NewBillPayment currencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
    return this;
  }

  /**
   * Optional for specifying the Bill Payment&#39;s Currency (3 letter ISO Currency Code).
   * @return currencyCode
   */
  @javax.annotation.Nullable
  public String getCurrencyCode() {
    return currencyCode;
  }

  public void setCurrencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
  }


  public NewBillPayment dateIssued(OffsetDateTime dateIssued) {
    this.dateIssued = dateIssued;
    return this;
  }

  /**
   * Date of Payment. If not specified, assumes today.
   * @return dateIssued
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateIssued() {
    return dateIssued;
  }

  public void setDateIssued(OffsetDateTime dateIssued) {
    this.dateIssued = dateIssued;
  }


  public NewBillPayment exchangeRate(Double exchangeRate) {
    this.exchangeRate = exchangeRate;
    return this;
  }

  /**
   * Optional. Only used when the Company&#39;s currency is different from the Avaza account&#39;s base currency. Specifies the exchange rate that should apply between the Company currency and base currency. If not provided we will obtain an up to date exchange rate for the Payment Issue Date.
   * @return exchangeRate
   */
  @javax.annotation.Nullable
  public Double getExchangeRate() {
    return exchangeRate;
  }

  public void setExchangeRate(Double exchangeRate) {
    this.exchangeRate = exchangeRate;
  }


  public NewBillPayment notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Get notes
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public NewBillPayment paymentAllocations(List<NewBillPaymentAllocation> paymentAllocations) {
    this.paymentAllocations = paymentAllocations;
    return this;
  }

  public NewBillPayment addPaymentAllocationsItem(NewBillPaymentAllocation paymentAllocationsItem) {
    if (this.paymentAllocations == null) {
      this.paymentAllocations = new ArrayList<>();
    }
    this.paymentAllocations.add(paymentAllocationsItem);
    return this;
  }

  /**
   * List of amounts within this payment that are allocated to invoices. The sum of these be less than or equal to the payment amount.
   * @return paymentAllocations
   */
  @javax.annotation.Nullable
  public List<NewBillPaymentAllocation> getPaymentAllocations() {
    return paymentAllocations;
  }

  public void setPaymentAllocations(List<NewBillPaymentAllocation> paymentAllocations) {
    this.paymentAllocations = paymentAllocations;
  }


  public NewBillPayment paymentNumber(String paymentNumber) {
    this.paymentNumber = paymentNumber;
    return this;
  }

  /**
   * Optional. If not specified will be automatically generated
   * @return paymentNumber
   */
  @javax.annotation.Nullable
  public String getPaymentNumber() {
    return paymentNumber;
  }

  public void setPaymentNumber(String paymentNumber) {
    this.paymentNumber = paymentNumber;
  }


  public NewBillPayment paymentProviderCode(String paymentProviderCode) {
    this.paymentProviderCode = paymentProviderCode;
    return this;
  }

  /**
   * Optional for storing the payment provider who was the source of funds.
   * @return paymentProviderCode
   */
  @javax.annotation.Nullable
  public String getPaymentProviderCode() {
    return paymentProviderCode;
  }

  public void setPaymentProviderCode(String paymentProviderCode) {
    this.paymentProviderCode = paymentProviderCode;
  }


  public NewBillPayment transactionPrefix(String transactionPrefix) {
    this.transactionPrefix = transactionPrefix;
    return this;
  }

  /**
   * Optional to override the default prefix added to Payment Numbers
   * @return transactionPrefix
   */
  @javax.annotation.Nullable
  public String getTransactionPrefix() {
    return transactionPrefix;
  }

  public void setTransactionPrefix(String transactionPrefix) {
    this.transactionPrefix = transactionPrefix;
  }


  public NewBillPayment transactionReference(String transactionReference) {
    this.transactionReference = transactionReference;
    return this;
  }

  /**
   * Optional for storing the reference # of the payment method.
   * @return transactionReference
   */
  @javax.annotation.Nullable
  public String getTransactionReference() {
    return transactionReference;
  }

  public void setTransactionReference(String transactionReference) {
    this.transactionReference = transactionReference;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NewBillPayment newBillPayment = (NewBillPayment) o;
    return Objects.equals(this.amount, newBillPayment.amount) &&
        Objects.equals(this.companyIDFK, newBillPayment.companyIDFK) &&
        Objects.equals(this.currencyCode, newBillPayment.currencyCode) &&
        Objects.equals(this.dateIssued, newBillPayment.dateIssued) &&
        Objects.equals(this.exchangeRate, newBillPayment.exchangeRate) &&
        Objects.equals(this.notes, newBillPayment.notes) &&
        Objects.equals(this.paymentAllocations, newBillPayment.paymentAllocations) &&
        Objects.equals(this.paymentNumber, newBillPayment.paymentNumber) &&
        Objects.equals(this.paymentProviderCode, newBillPayment.paymentProviderCode) &&
        Objects.equals(this.transactionPrefix, newBillPayment.transactionPrefix) &&
        Objects.equals(this.transactionReference, newBillPayment.transactionReference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, companyIDFK, currencyCode, dateIssued, exchangeRate, notes, paymentAllocations, paymentNumber, paymentProviderCode, transactionPrefix, transactionReference);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NewBillPayment {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    companyIDFK: ").append(toIndentedString(companyIDFK)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    dateIssued: ").append(toIndentedString(dateIssued)).append("\n");
    sb.append("    exchangeRate: ").append(toIndentedString(exchangeRate)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    paymentAllocations: ").append(toIndentedString(paymentAllocations)).append("\n");
    sb.append("    paymentNumber: ").append(toIndentedString(paymentNumber)).append("\n");
    sb.append("    paymentProviderCode: ").append(toIndentedString(paymentProviderCode)).append("\n");
    sb.append("    transactionPrefix: ").append(toIndentedString(transactionPrefix)).append("\n");
    sb.append("    transactionReference: ").append(toIndentedString(transactionReference)).append("\n");
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
    openapiFields.add("Amount");
    openapiFields.add("CompanyIDFK");
    openapiFields.add("CurrencyCode");
    openapiFields.add("DateIssued");
    openapiFields.add("ExchangeRate");
    openapiFields.add("Notes");
    openapiFields.add("PaymentAllocations");
    openapiFields.add("PaymentNumber");
    openapiFields.add("PaymentProviderCode");
    openapiFields.add("TransactionPrefix");
    openapiFields.add("TransactionReference");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NewBillPayment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NewBillPayment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NewBillPayment is not found in the empty JSON string", NewBillPayment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NewBillPayment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NewBillPayment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("CurrencyCode") != null && !jsonObj.get("CurrencyCode").isJsonNull()) && !jsonObj.get("CurrencyCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CurrencyCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CurrencyCode").toString()));
      }
      if ((jsonObj.get("Notes") != null && !jsonObj.get("Notes").isJsonNull()) && !jsonObj.get("Notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Notes").toString()));
      }
      if (jsonObj.get("PaymentAllocations") != null && !jsonObj.get("PaymentAllocations").isJsonNull()) {
        JsonArray jsonArraypaymentAllocations = jsonObj.getAsJsonArray("PaymentAllocations");
        if (jsonArraypaymentAllocations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("PaymentAllocations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `PaymentAllocations` to be an array in the JSON string but got `%s`", jsonObj.get("PaymentAllocations").toString()));
          }

          // validate the optional field `PaymentAllocations` (array)
          for (int i = 0; i < jsonArraypaymentAllocations.size(); i++) {
            NewBillPaymentAllocation.validateJsonElement(jsonArraypaymentAllocations.get(i));
          };
        }
      }
      if ((jsonObj.get("PaymentNumber") != null && !jsonObj.get("PaymentNumber").isJsonNull()) && !jsonObj.get("PaymentNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PaymentNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PaymentNumber").toString()));
      }
      if ((jsonObj.get("PaymentProviderCode") != null && !jsonObj.get("PaymentProviderCode").isJsonNull()) && !jsonObj.get("PaymentProviderCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PaymentProviderCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PaymentProviderCode").toString()));
      }
      if ((jsonObj.get("TransactionPrefix") != null && !jsonObj.get("TransactionPrefix").isJsonNull()) && !jsonObj.get("TransactionPrefix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TransactionPrefix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TransactionPrefix").toString()));
      }
      if ((jsonObj.get("TransactionReference") != null && !jsonObj.get("TransactionReference").isJsonNull()) && !jsonObj.get("TransactionReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TransactionReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TransactionReference").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NewBillPayment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NewBillPayment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NewBillPayment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NewBillPayment.class));

       return (TypeAdapter<T>) new TypeAdapter<NewBillPayment>() {
           @Override
           public void write(JsonWriter out, NewBillPayment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NewBillPayment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NewBillPayment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NewBillPayment
   * @throws IOException if the JSON string is invalid with respect to NewBillPayment
   */
  public static NewBillPayment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NewBillPayment.class);
  }

  /**
   * Convert an instance of NewBillPayment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

