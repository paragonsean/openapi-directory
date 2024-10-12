/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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
import java.net.URI;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ContactObject;
import org.openapitools.client.model.PaymentInstruction;
import org.openapitools.client.model.PaymentInstrument;
import org.openapitools.client.model.RiskMetadata;
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
 * PayoutRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PayoutRequest {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billingAddress";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private ContactObject billingAddress;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "customFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields = {};

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_GATEWAY_ACCOUNT_ID = "gatewayAccountId";
  @SerializedName(SERIALIZED_NAME_GATEWAY_ACCOUNT_ID)
  private String gatewayAccountId;

  public static final String SERIALIZED_NAME_INVOICE_IDS = "invoiceIds";
  @SerializedName(SERIALIZED_NAME_INVOICE_IDS)
  private List<String> invoiceIds;

  public static final String SERIALIZED_NAME_IS_MERCHANT_INITIATED = "isMerchantInitiated";
  @SerializedName(SERIALIZED_NAME_IS_MERCHANT_INITIATED)
  private Boolean isMerchantInitiated = false;

  public static final String SERIALIZED_NAME_IS_PROCESSED_OUTSIDE = "isProcessedOutside";
  @SerializedName(SERIALIZED_NAME_IS_PROCESSED_OUTSIDE)
  private Boolean isProcessedOutside = false;

  public static final String SERIALIZED_NAME_NOTIFICATION_URL = "notificationUrl";
  @SerializedName(SERIALIZED_NAME_NOTIFICATION_URL)
  private URI notificationUrl;

  public static final String SERIALIZED_NAME_PAYMENT_INSTRUCTION = "paymentInstruction";
  @SerializedName(SERIALIZED_NAME_PAYMENT_INSTRUCTION)
  private PaymentInstruction paymentInstruction;

  public static final String SERIALIZED_NAME_PAYMENT_INSTRUMENT = "paymentInstrument";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_PAYMENT_INSTRUMENT)
  private PaymentInstrument paymentInstrument;

  public static final String SERIALIZED_NAME_PROCESSED_TIME = "processedTime";
  @SerializedName(SERIALIZED_NAME_PROCESSED_TIME)
  private OffsetDateTime processedTime;

  public static final String SERIALIZED_NAME_REDIRECT_URL = "redirectUrl";
  @SerializedName(SERIALIZED_NAME_REDIRECT_URL)
  private URI redirectUrl;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private String requestId;

  public static final String SERIALIZED_NAME_RISK_METADATA = "riskMetadata";
  @SerializedName(SERIALIZED_NAME_RISK_METADATA)
  private RiskMetadata riskMetadata;

  public static final String SERIALIZED_NAME_WEBSITE_ID = "websiteId";
  @SerializedName(SERIALIZED_NAME_WEBSITE_ID)
  private String websiteId;

  public PayoutRequest() {
  }

  public PayoutRequest amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * The transaction amount.
   * @return amount
   */
  @javax.annotation.Nonnull
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public PayoutRequest billingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Billing address. If not supplied, we use the billing address associated with the payment instrument, and then customer.
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public ContactObject getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
  }


  public PayoutRequest currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * ISO 4217 alphabetic currency code.
   * @return currency
   */
  @javax.annotation.Nonnull
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public PayoutRequest customFields(Object customFields) {
    this.customFields = customFields;
    return this;
  }

  /**
   * Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats). 
   * @return customFields
   */
  @javax.annotation.Nullable
  public Object getCustomFields() {
    return customFields;
  }

  public void setCustomFields(Object customFields) {
    this.customFields = customFields;
  }


  public PayoutRequest customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * The customer identifier string.
   * @return customerId
   */
  @javax.annotation.Nonnull
  public String getCustomerId() {
    return customerId;
  }

  public void setCustomerId(String customerId) {
    this.customerId = customerId;
  }


  public PayoutRequest description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The payment description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public PayoutRequest gatewayAccountId(String gatewayAccountId) {
    this.gatewayAccountId = gatewayAccountId;
    return this;
  }

  /**
   * Rebilly will select the appropriate payment gateway account for the transaction based on the properties of the transaction and the &#x60;gateway-account-requested&#x60; event rules configurations. If you wish to prevent Rebilly from making the gateway account selection, you may supply a gateway account id here, and it will be used instead. Only use this field if you intend to override the settings.
   * @return gatewayAccountId
   */
  @javax.annotation.Nullable
  public String getGatewayAccountId() {
    return gatewayAccountId;
  }

  public void setGatewayAccountId(String gatewayAccountId) {
    this.gatewayAccountId = gatewayAccountId;
  }


  public PayoutRequest invoiceIds(List<String> invoiceIds) {
    this.invoiceIds = invoiceIds;
    return this;
  }

  public PayoutRequest addInvoiceIdsItem(String invoiceIdsItem) {
    if (this.invoiceIds == null) {
      this.invoiceIds = new ArrayList<>();
    }
    this.invoiceIds.add(invoiceIdsItem);
    return this;
  }

  /**
   * The array of invoice identifiers.
   * @return invoiceIds
   */
  @javax.annotation.Nullable
  public List<String> getInvoiceIds() {
    return invoiceIds;
  }

  public void setInvoiceIds(List<String> invoiceIds) {
    this.invoiceIds = invoiceIds;
  }


  public PayoutRequest isMerchantInitiated(Boolean isMerchantInitiated) {
    this.isMerchantInitiated = isMerchantInitiated;
    return this;
  }

  /**
   * True if the transaction was initiated by the merchant.
   * @return isMerchantInitiated
   */
  @javax.annotation.Nullable
  public Boolean getIsMerchantInitiated() {
    return isMerchantInitiated;
  }

  public void setIsMerchantInitiated(Boolean isMerchantInitiated) {
    this.isMerchantInitiated = isMerchantInitiated;
  }


  public PayoutRequest isProcessedOutside(Boolean isProcessedOutside) {
    this.isProcessedOutside = isProcessedOutside;
    return this;
  }

  /**
   * True if transaction was processed outside Rebilly.
   * @return isProcessedOutside
   */
  @javax.annotation.Nullable
  public Boolean getIsProcessedOutside() {
    return isProcessedOutside;
  }

  public void setIsProcessedOutside(Boolean isProcessedOutside) {
    this.isProcessedOutside = isProcessedOutside;
  }


  public PayoutRequest notificationUrl(URI notificationUrl) {
    this.notificationUrl = notificationUrl;
    return this;
  }

  /**
   * The URL where a server-to-server notification request type &#x60;POST&#x60; with a transaction payload will be sent when the transaction&#39;s result is finalized. Do not trust the notification; follow with a &#x60;GET&#x60; request to confirm the result of the transaction. Please respond with a &#x60;2xx&#x60; HTTP status code, or we will reattempt the request again. You may use &#x60;{id}&#x60; or &#x60;{result}&#x60; as placeholders in the URL and we will replace them with the transaction&#39;s id and result accordingly. 
   * @return notificationUrl
   */
  @javax.annotation.Nullable
  public URI getNotificationUrl() {
    return notificationUrl;
  }

  public void setNotificationUrl(URI notificationUrl) {
    this.notificationUrl = notificationUrl;
  }


  public PayoutRequest paymentInstruction(PaymentInstruction paymentInstruction) {
    this.paymentInstruction = paymentInstruction;
    return this;
  }

  /**
   * Payment instruction. If not supplied, customer&#39;s default payment instrument will be used.
   * @return paymentInstruction
   */
  @javax.annotation.Nullable
  public PaymentInstruction getPaymentInstruction() {
    return paymentInstruction;
  }

  public void setPaymentInstruction(PaymentInstruction paymentInstruction) {
    this.paymentInstruction = paymentInstruction;
  }


  @Deprecated
  public PayoutRequest paymentInstrument(PaymentInstrument paymentInstrument) {
    this.paymentInstrument = paymentInstrument;
    return this;
  }

  /**
   * Get paymentInstrument
   * @return paymentInstrument
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public PaymentInstrument getPaymentInstrument() {
    return paymentInstrument;
  }

  @Deprecated
  public void setPaymentInstrument(PaymentInstrument paymentInstrument) {
    this.paymentInstrument = paymentInstrument;
  }


  public PayoutRequest processedTime(OffsetDateTime processedTime) {
    this.processedTime = processedTime;
    return this;
  }

  /**
   * The time the transaction was processed. Can be specified only if transaction was processed outside Rebilly.
   * @return processedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getProcessedTime() {
    return processedTime;
  }

  public void setProcessedTime(OffsetDateTime processedTime) {
    this.processedTime = processedTime;
  }


  public PayoutRequest redirectUrl(URI redirectUrl) {
    this.redirectUrl = redirectUrl;
    return this;
  }

  /**
   * The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website&#39;s configured URL. You may use &#x60;{id}&#x60; or &#x60;{result}&#x60; as placeholders in the URL and we will replace them with the transaction&#39;s id and result accordingly.
   * @return redirectUrl
   */
  @javax.annotation.Nullable
  public URI getRedirectUrl() {
    return redirectUrl;
  }

  public void setRedirectUrl(URI redirectUrl) {
    this.redirectUrl = redirectUrl;
  }


  public PayoutRequest requestId(String requestId) {
    this.requestId = requestId;
    return this;
  }

  /**
   * The request id is **recommended**. It prevents duplicate transaction requests within a short period of time. If a duplicate request is sent with the same &#x60;requestId&#x60; it will be ignored to prevent double-billing anyone.  It must be unique within a 24-hour period.  We recommend generating a UUID v4 as its value.
   * @return requestId
   */
  @javax.annotation.Nullable
  public String getRequestId() {
    return requestId;
  }

  public void setRequestId(String requestId) {
    this.requestId = requestId;
  }


  public PayoutRequest riskMetadata(RiskMetadata riskMetadata) {
    this.riskMetadata = riskMetadata;
    return this;
  }

  /**
   * Get riskMetadata
   * @return riskMetadata
   */
  @javax.annotation.Nullable
  public RiskMetadata getRiskMetadata() {
    return riskMetadata;
  }

  public void setRiskMetadata(RiskMetadata riskMetadata) {
    this.riskMetadata = riskMetadata;
  }


  public PayoutRequest websiteId(String websiteId) {
    this.websiteId = websiteId;
    return this;
  }

  /**
   * The website identifier string.
   * @return websiteId
   */
  @javax.annotation.Nonnull
  public String getWebsiteId() {
    return websiteId;
  }

  public void setWebsiteId(String websiteId) {
    this.websiteId = websiteId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PayoutRequest payoutRequest = (PayoutRequest) o;
    return Objects.equals(this.amount, payoutRequest.amount) &&
        Objects.equals(this.billingAddress, payoutRequest.billingAddress) &&
        Objects.equals(this.currency, payoutRequest.currency) &&
        Objects.equals(this.customFields, payoutRequest.customFields) &&
        Objects.equals(this.customerId, payoutRequest.customerId) &&
        Objects.equals(this.description, payoutRequest.description) &&
        Objects.equals(this.gatewayAccountId, payoutRequest.gatewayAccountId) &&
        Objects.equals(this.invoiceIds, payoutRequest.invoiceIds) &&
        Objects.equals(this.isMerchantInitiated, payoutRequest.isMerchantInitiated) &&
        Objects.equals(this.isProcessedOutside, payoutRequest.isProcessedOutside) &&
        Objects.equals(this.notificationUrl, payoutRequest.notificationUrl) &&
        Objects.equals(this.paymentInstruction, payoutRequest.paymentInstruction) &&
        Objects.equals(this.paymentInstrument, payoutRequest.paymentInstrument) &&
        Objects.equals(this.processedTime, payoutRequest.processedTime) &&
        Objects.equals(this.redirectUrl, payoutRequest.redirectUrl) &&
        Objects.equals(this.requestId, payoutRequest.requestId) &&
        Objects.equals(this.riskMetadata, payoutRequest.riskMetadata) &&
        Objects.equals(this.websiteId, payoutRequest.websiteId);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, billingAddress, currency, customFields, customerId, description, gatewayAccountId, invoiceIds, isMerchantInitiated, isProcessedOutside, notificationUrl, paymentInstruction, paymentInstrument, processedTime, redirectUrl, requestId, riskMetadata, websiteId);
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
    sb.append("class PayoutRequest {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    gatewayAccountId: ").append(toIndentedString(gatewayAccountId)).append("\n");
    sb.append("    invoiceIds: ").append(toIndentedString(invoiceIds)).append("\n");
    sb.append("    isMerchantInitiated: ").append(toIndentedString(isMerchantInitiated)).append("\n");
    sb.append("    isProcessedOutside: ").append(toIndentedString(isProcessedOutside)).append("\n");
    sb.append("    notificationUrl: ").append(toIndentedString(notificationUrl)).append("\n");
    sb.append("    paymentInstruction: ").append(toIndentedString(paymentInstruction)).append("\n");
    sb.append("    paymentInstrument: ").append(toIndentedString(paymentInstrument)).append("\n");
    sb.append("    processedTime: ").append(toIndentedString(processedTime)).append("\n");
    sb.append("    redirectUrl: ").append(toIndentedString(redirectUrl)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    riskMetadata: ").append(toIndentedString(riskMetadata)).append("\n");
    sb.append("    websiteId: ").append(toIndentedString(websiteId)).append("\n");
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
    openapiFields.add("billingAddress");
    openapiFields.add("currency");
    openapiFields.add("customFields");
    openapiFields.add("customerId");
    openapiFields.add("description");
    openapiFields.add("gatewayAccountId");
    openapiFields.add("invoiceIds");
    openapiFields.add("isMerchantInitiated");
    openapiFields.add("isProcessedOutside");
    openapiFields.add("notificationUrl");
    openapiFields.add("paymentInstruction");
    openapiFields.add("paymentInstrument");
    openapiFields.add("processedTime");
    openapiFields.add("redirectUrl");
    openapiFields.add("requestId");
    openapiFields.add("riskMetadata");
    openapiFields.add("websiteId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("amount");
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("customerId");
    openapiRequiredFields.add("websiteId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PayoutRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PayoutRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PayoutRequest is not found in the empty JSON string", PayoutRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PayoutRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PayoutRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PayoutRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `billingAddress`
      if (jsonObj.get("billingAddress") != null && !jsonObj.get("billingAddress").isJsonNull()) {
        ContactObject.validateJsonElement(jsonObj.get("billingAddress"));
      }
      if (!jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (!jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("gatewayAccountId") != null && !jsonObj.get("gatewayAccountId").isJsonNull()) && !jsonObj.get("gatewayAccountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gatewayAccountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gatewayAccountId").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("invoiceIds") != null && !jsonObj.get("invoiceIds").isJsonNull() && !jsonObj.get("invoiceIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoiceIds` to be an array in the JSON string but got `%s`", jsonObj.get("invoiceIds").toString()));
      }
      if ((jsonObj.get("notificationUrl") != null && !jsonObj.get("notificationUrl").isJsonNull()) && !jsonObj.get("notificationUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notificationUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notificationUrl").toString()));
      }
      // validate the optional field `paymentInstruction`
      if (jsonObj.get("paymentInstruction") != null && !jsonObj.get("paymentInstruction").isJsonNull()) {
        PaymentInstruction.validateJsonElement(jsonObj.get("paymentInstruction"));
      }
      // validate the optional field `paymentInstrument`
      if (jsonObj.get("paymentInstrument") != null && !jsonObj.get("paymentInstrument").isJsonNull()) {
        PaymentInstrument.validateJsonElement(jsonObj.get("paymentInstrument"));
      }
      if ((jsonObj.get("redirectUrl") != null && !jsonObj.get("redirectUrl").isJsonNull()) && !jsonObj.get("redirectUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `redirectUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("redirectUrl").toString()));
      }
      if ((jsonObj.get("requestId") != null && !jsonObj.get("requestId").isJsonNull()) && !jsonObj.get("requestId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestId").toString()));
      }
      // validate the optional field `riskMetadata`
      if (jsonObj.get("riskMetadata") != null && !jsonObj.get("riskMetadata").isJsonNull()) {
        RiskMetadata.validateJsonElement(jsonObj.get("riskMetadata"));
      }
      if (!jsonObj.get("websiteId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `websiteId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("websiteId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PayoutRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PayoutRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PayoutRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PayoutRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<PayoutRequest>() {
           @Override
           public void write(JsonWriter out, PayoutRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PayoutRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PayoutRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PayoutRequest
   * @throws IOException if the JSON string is invalid with respect to PayoutRequest
   */
  public static PayoutRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PayoutRequest.class);
  }

  /**
   * Convert an instance of PayoutRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

