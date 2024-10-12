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
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.UUID;

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
 * QuoteFxSummaryV3
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:55.204956-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QuoteFxSummaryV3 {
  public static final String SERIALIZED_NAME_CREATION_TIME = "creationTime";
  @SerializedName(SERIALIZED_NAME_CREATION_TIME)
  private OffsetDateTime creationTime;

  public static final String SERIALIZED_NAME_EXPIRY_TIME = "expiryTime";
  @SerializedName(SERIALIZED_NAME_EXPIRY_TIME)
  private OffsetDateTime expiryTime;

  public static final String SERIALIZED_NAME_FUNDING_STATUS = "fundingStatus";
  @SerializedName(SERIALIZED_NAME_FUNDING_STATUS)
  private String fundingStatus;

  public static final String SERIALIZED_NAME_INVERTED_RATE = "invertedRate";
  @SerializedName(SERIALIZED_NAME_INVERTED_RATE)
  private Float invertedRate;

  public static final String SERIALIZED_NAME_PAYMENT_CURRENCY = "paymentCurrency";
  @SerializedName(SERIALIZED_NAME_PAYMENT_CURRENCY)
  private String paymentCurrency;

  public static final String SERIALIZED_NAME_QUOTE_ID = "quoteId";
  @SerializedName(SERIALIZED_NAME_QUOTE_ID)
  private UUID quoteId;

  public static final String SERIALIZED_NAME_RATE = "rate";
  @SerializedName(SERIALIZED_NAME_RATE)
  private Float rate;

  public static final String SERIALIZED_NAME_SOURCE_CURRENCY = "sourceCurrency";
  @SerializedName(SERIALIZED_NAME_SOURCE_CURRENCY)
  private String sourceCurrency;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TOTAL_PAYMENT_AMOUNT = "totalPaymentAmount";
  @SerializedName(SERIALIZED_NAME_TOTAL_PAYMENT_AMOUNT)
  private Integer totalPaymentAmount;

  public static final String SERIALIZED_NAME_TOTAL_SOURCE_AMOUNT = "totalSourceAmount";
  @SerializedName(SERIALIZED_NAME_TOTAL_SOURCE_AMOUNT)
  private Integer totalSourceAmount;

  public QuoteFxSummaryV3() {
  }

  public QuoteFxSummaryV3 creationTime(OffsetDateTime creationTime) {
    this.creationTime = creationTime;
    return this;
  }

  /**
   * Timestamp of when the quote was created
   * @return creationTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreationTime() {
    return creationTime;
  }

  public void setCreationTime(OffsetDateTime creationTime) {
    this.creationTime = creationTime;
  }


  public QuoteFxSummaryV3 expiryTime(OffsetDateTime expiryTime) {
    this.expiryTime = expiryTime;
    return this;
  }

  /**
   * The timestamp for when the quote will expire
   * @return expiryTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiryTime() {
    return expiryTime;
  }

  public void setExpiryTime(OffsetDateTime expiryTime) {
    this.expiryTime = expiryTime;
  }


  public QuoteFxSummaryV3 fundingStatus(String fundingStatus) {
    this.fundingStatus = fundingStatus;
    return this;
  }

  /**
   * Current status of the funding associated with this quote. One of the following values: UNFUNDED, INSTRUCTED, FUNDED
   * @return fundingStatus
   */
  @javax.annotation.Nonnull
  public String getFundingStatus() {
    return fundingStatus;
  }

  public void setFundingStatus(String fundingStatus) {
    this.fundingStatus = fundingStatus;
  }


  public QuoteFxSummaryV3 invertedRate(Float invertedRate) {
    this.invertedRate = invertedRate;
    return this;
  }

  /**
   * The inverse conversion rate (from paymnent currency to source currency)
   * @return invertedRate
   */
  @javax.annotation.Nullable
  public Float getInvertedRate() {
    return invertedRate;
  }

  public void setInvertedRate(Float invertedRate) {
    this.invertedRate = invertedRate;
  }


  public QuoteFxSummaryV3 paymentCurrency(String paymentCurrency) {
    this.paymentCurrency = paymentCurrency;
    return this;
  }

  /**
   * Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details.
   * @return paymentCurrency
   */
  @javax.annotation.Nonnull
  public String getPaymentCurrency() {
    return paymentCurrency;
  }

  public void setPaymentCurrency(String paymentCurrency) {
    this.paymentCurrency = paymentCurrency;
  }


  public QuoteFxSummaryV3 quoteId(UUID quoteId) {
    this.quoteId = quoteId;
    return this;
  }

  /**
   * The id of the created quote
   * @return quoteId
   */
  @javax.annotation.Nonnull
  public UUID getQuoteId() {
    return quoteId;
  }

  public void setQuoteId(UUID quoteId) {
    this.quoteId = quoteId;
  }


  public QuoteFxSummaryV3 rate(Float rate) {
    this.rate = rate;
    return this;
  }

  /**
   * The conversion rate (from the source currency to the payment currency)
   * @return rate
   */
  @javax.annotation.Nonnull
  public Float getRate() {
    return rate;
  }

  public void setRate(Float rate) {
    this.rate = rate;
  }


  public QuoteFxSummaryV3 sourceCurrency(String sourceCurrency) {
    this.sourceCurrency = sourceCurrency;
    return this;
  }

  /**
   * Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details.
   * @return sourceCurrency
   */
  @javax.annotation.Nonnull
  public String getSourceCurrency() {
    return sourceCurrency;
  }

  public void setSourceCurrency(String sourceCurrency) {
    this.sourceCurrency = sourceCurrency;
  }


  public QuoteFxSummaryV3 status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Current status of the fx quote. One of the following values: UNQUOTED, QUOTED, EXPIRED, EXECUTED, REJECTED
   * @return status
   */
  @javax.annotation.Nonnull
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public QuoteFxSummaryV3 totalPaymentAmount(Integer totalPaymentAmount) {
    this.totalPaymentAmount = totalPaymentAmount;
    return this;
  }

  /**
   * The amount (in minor units) that the payee will receive
   * @return totalPaymentAmount
   */
  @javax.annotation.Nonnull
  public Integer getTotalPaymentAmount() {
    return totalPaymentAmount;
  }

  public void setTotalPaymentAmount(Integer totalPaymentAmount) {
    this.totalPaymentAmount = totalPaymentAmount;
  }


  public QuoteFxSummaryV3 totalSourceAmount(Integer totalSourceAmount) {
    this.totalSourceAmount = totalSourceAmount;
    return this;
  }

  /**
   * The amount (in minor units) that will be paid from the source account
   * @return totalSourceAmount
   */
  @javax.annotation.Nonnull
  public Integer getTotalSourceAmount() {
    return totalSourceAmount;
  }

  public void setTotalSourceAmount(Integer totalSourceAmount) {
    this.totalSourceAmount = totalSourceAmount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QuoteFxSummaryV3 quoteFxSummaryV3 = (QuoteFxSummaryV3) o;
    return Objects.equals(this.creationTime, quoteFxSummaryV3.creationTime) &&
        Objects.equals(this.expiryTime, quoteFxSummaryV3.expiryTime) &&
        Objects.equals(this.fundingStatus, quoteFxSummaryV3.fundingStatus) &&
        Objects.equals(this.invertedRate, quoteFxSummaryV3.invertedRate) &&
        Objects.equals(this.paymentCurrency, quoteFxSummaryV3.paymentCurrency) &&
        Objects.equals(this.quoteId, quoteFxSummaryV3.quoteId) &&
        Objects.equals(this.rate, quoteFxSummaryV3.rate) &&
        Objects.equals(this.sourceCurrency, quoteFxSummaryV3.sourceCurrency) &&
        Objects.equals(this.status, quoteFxSummaryV3.status) &&
        Objects.equals(this.totalPaymentAmount, quoteFxSummaryV3.totalPaymentAmount) &&
        Objects.equals(this.totalSourceAmount, quoteFxSummaryV3.totalSourceAmount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(creationTime, expiryTime, fundingStatus, invertedRate, paymentCurrency, quoteId, rate, sourceCurrency, status, totalPaymentAmount, totalSourceAmount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QuoteFxSummaryV3 {\n");
    sb.append("    creationTime: ").append(toIndentedString(creationTime)).append("\n");
    sb.append("    expiryTime: ").append(toIndentedString(expiryTime)).append("\n");
    sb.append("    fundingStatus: ").append(toIndentedString(fundingStatus)).append("\n");
    sb.append("    invertedRate: ").append(toIndentedString(invertedRate)).append("\n");
    sb.append("    paymentCurrency: ").append(toIndentedString(paymentCurrency)).append("\n");
    sb.append("    quoteId: ").append(toIndentedString(quoteId)).append("\n");
    sb.append("    rate: ").append(toIndentedString(rate)).append("\n");
    sb.append("    sourceCurrency: ").append(toIndentedString(sourceCurrency)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    totalPaymentAmount: ").append(toIndentedString(totalPaymentAmount)).append("\n");
    sb.append("    totalSourceAmount: ").append(toIndentedString(totalSourceAmount)).append("\n");
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
    openapiFields.add("creationTime");
    openapiFields.add("expiryTime");
    openapiFields.add("fundingStatus");
    openapiFields.add("invertedRate");
    openapiFields.add("paymentCurrency");
    openapiFields.add("quoteId");
    openapiFields.add("rate");
    openapiFields.add("sourceCurrency");
    openapiFields.add("status");
    openapiFields.add("totalPaymentAmount");
    openapiFields.add("totalSourceAmount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("creationTime");
    openapiRequiredFields.add("fundingStatus");
    openapiRequiredFields.add("paymentCurrency");
    openapiRequiredFields.add("quoteId");
    openapiRequiredFields.add("rate");
    openapiRequiredFields.add("sourceCurrency");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("totalPaymentAmount");
    openapiRequiredFields.add("totalSourceAmount");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QuoteFxSummaryV3
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QuoteFxSummaryV3.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QuoteFxSummaryV3 is not found in the empty JSON string", QuoteFxSummaryV3.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QuoteFxSummaryV3.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QuoteFxSummaryV3` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : QuoteFxSummaryV3.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("fundingStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fundingStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fundingStatus").toString()));
      }
      if (!jsonObj.get("paymentCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentCurrency").toString()));
      }
      if (!jsonObj.get("quoteId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `quoteId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("quoteId").toString()));
      }
      if (!jsonObj.get("sourceCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceCurrency").toString()));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QuoteFxSummaryV3.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QuoteFxSummaryV3' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QuoteFxSummaryV3> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QuoteFxSummaryV3.class));

       return (TypeAdapter<T>) new TypeAdapter<QuoteFxSummaryV3>() {
           @Override
           public void write(JsonWriter out, QuoteFxSummaryV3 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QuoteFxSummaryV3 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QuoteFxSummaryV3 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QuoteFxSummaryV3
   * @throws IOException if the JSON string is invalid with respect to QuoteFxSummaryV3
   */
  public static QuoteFxSummaryV3 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QuoteFxSummaryV3.class);
  }

  /**
   * Convert an instance of QuoteFxSummaryV3 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

