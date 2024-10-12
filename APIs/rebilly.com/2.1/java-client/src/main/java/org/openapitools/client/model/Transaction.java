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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.AcquirerName;
import org.openapitools.client.model.ContactObject;
import org.openapitools.client.model.GatewayName;
import org.openapitools.client.model.PaymentInstrument;
import org.openapitools.client.model.PaymentMethod;
import org.openapitools.client.model.PaymentRetry;
import org.openapitools.client.model.RiskMetadata;
import org.openapitools.client.model.ThreeDSecureResult;
import org.openapitools.client.model.TransactionAllOfBumpOffer;
import org.openapitools.client.model.TransactionAllOfDcc;
import org.openapitools.client.model.TransactionAllOfEmbedded;
import org.openapitools.client.model.TransactionAllOfGateway;
import org.openapitools.client.model.TransactionAllOfLinks;
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
 * Transaction
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Transaction {
  public static final String SERIALIZED_NAME_3DS = "3ds";
  @SerializedName(SERIALIZED_NAME_3DS)
  private ThreeDSecureResult _3ds;

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billingAddress";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private ContactObject billingAddress;

  public static final String SERIALIZED_NAME_BILLING_DESCRIPTOR = "billingDescriptor";
  @SerializedName(SERIALIZED_NAME_BILLING_DESCRIPTOR)
  private String billingDescriptor;

  public static final String SERIALIZED_NAME_CHILD_TRANSACTIONS = "childTransactions";
  @SerializedName(SERIALIZED_NAME_CHILD_TRANSACTIONS)
  private List<String> childTransactions = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

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

  public static final String SERIALIZED_NAME_GATEWAY_NAME = "gatewayName";
  @SerializedName(SERIALIZED_NAME_GATEWAY_NAME)
  private GatewayName gatewayName;

  public static final String SERIALIZED_NAME_HAS3DS = "has3ds";
  @SerializedName(SERIALIZED_NAME_HAS3DS)
  private Boolean has3ds;

  public static final String SERIALIZED_NAME_HAS_AMOUNT_ADJUSTMENT = "hasAmountAdjustment";
  @SerializedName(SERIALIZED_NAME_HAS_AMOUNT_ADJUSTMENT)
  private Boolean hasAmountAdjustment;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INVOICE_IDS = "invoiceIds";
  @SerializedName(SERIALIZED_NAME_INVOICE_IDS)
  private List<String> invoiceIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_REBILL = "isRebill";
  @SerializedName(SERIALIZED_NAME_IS_REBILL)
  private Boolean isRebill;

  public static final String SERIALIZED_NAME_IS_RETRY = "isRetry";
  @SerializedName(SERIALIZED_NAME_IS_RETRY)
  private Boolean isRetry;

  public static final String SERIALIZED_NAME_PARENT_TRANSACTION_ID = "parentTransactionId";
  @SerializedName(SERIALIZED_NAME_PARENT_TRANSACTION_ID)
  private String parentTransactionId;

  public static final String SERIALIZED_NAME_PAYMENT_INSTRUMENT = "paymentInstrument";
  @SerializedName(SERIALIZED_NAME_PAYMENT_INSTRUMENT)
  private PaymentInstrument paymentInstrument;

  public static final String SERIALIZED_NAME_PLAN_IDS = "planIds";
  @SerializedName(SERIALIZED_NAME_PLAN_IDS)
  private List<String> planIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROCESSED_TIME = "processedTime";
  @SerializedName(SERIALIZED_NAME_PROCESSED_TIME)
  private OffsetDateTime processedTime;

  public static final String SERIALIZED_NAME_PURCHASE_AMOUNT = "purchaseAmount";
  @SerializedName(SERIALIZED_NAME_PURCHASE_AMOUNT)
  private Double purchaseAmount;

  public static final String SERIALIZED_NAME_PURCHASE_CURRENCY = "purchaseCurrency";
  @SerializedName(SERIALIZED_NAME_PURCHASE_CURRENCY)
  private String purchaseCurrency;

  public static final String SERIALIZED_NAME_REBILL_NUMBER = "rebillNumber";
  @SerializedName(SERIALIZED_NAME_REBILL_NUMBER)
  private Integer rebillNumber;

  public static final String SERIALIZED_NAME_REDIRECT_URL = "redirectUrl";
  @SerializedName(SERIALIZED_NAME_REDIRECT_URL)
  private URI redirectUrl;

  public static final String SERIALIZED_NAME_REQUEST_AMOUNT = "requestAmount";
  @SerializedName(SERIALIZED_NAME_REQUEST_AMOUNT)
  private Double requestAmount;

  public static final String SERIALIZED_NAME_REQUEST_CURRENCY = "requestCurrency";
  @SerializedName(SERIALIZED_NAME_REQUEST_CURRENCY)
  private String requestCurrency;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private String requestId;

  /**
   * Transaction result.
   */
  @JsonAdapter(ResultEnum.Adapter.class)
  public enum ResultEnum {
    ABANDONED("abandoned"),
    
    APPROVED("approved"),
    
    CANCELED("canceled"),
    
    DECLINED("declined"),
    
    UNKNOWN("unknown");

    private String value;

    ResultEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ResultEnum fromValue(String value) {
      for (ResultEnum b : ResultEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ResultEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ResultEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ResultEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ResultEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ResultEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RESULT = "result";
  @SerializedName(SERIALIZED_NAME_RESULT)
  private ResultEnum result;

  public static final String SERIALIZED_NAME_RETRY_NUMBER = "retryNumber";
  @SerializedName(SERIALIZED_NAME_RETRY_NUMBER)
  private Integer retryNumber;

  /**
   * Transaction status.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    COMPLETED("completed"),
    
    CONN_ERROR("conn-error"),
    
    DISPUTED("disputed"),
    
    NEVER_SENT("never-sent"),
    
    OFFSITE("offsite"),
    
    PARTIALLY_REFUNDED("partially-refunded"),
    
    PENDING("pending"),
    
    REFUNDED("refunded"),
    
    SENDING("sending"),
    
    SUSPENDED("suspended"),
    
    TIMEOUT("timeout"),
    
    VOIDED("voided"),
    
    WAITING_APPROVAL("waiting-approval"),
    
    WAITING_CAPTURE("waiting-capture"),
    
    WAITING_GATEWAY("waiting-gateway"),
    
    WAITING_REFUND("waiting-refund");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_SUBSCRIPTION_IDS = "subscriptionIds";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTION_IDS)
  private List<String> subscriptionIds = new ArrayList<>();

  /**
   * Transaction type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    _3DS_AUTHENTICATION("3ds-authentication"),
    
    AUTHORIZE("authorize"),
    
    CAPTURE("capture"),
    
    CREDIT("credit"),
    
    REFUND("refund"),
    
    SALE("sale"),
    
    VOID("void");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_WEBSITE_ID = "websiteId";
  @SerializedName(SERIALIZED_NAME_WEBSITE_ID)
  private String websiteId;

  public static final String SERIALIZED_NAME_EMBEDDED = "_embedded";
  @SerializedName(SERIALIZED_NAME_EMBEDDED)
  private List<TransactionAllOfEmbedded> embedded = new ArrayList<>();

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<TransactionAllOfLinks> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_ACQUIRER_NAME = "acquirerName";
  @SerializedName(SERIALIZED_NAME_ACQUIRER_NAME)
  private AcquirerName acquirerName;

  public static final String SERIALIZED_NAME_ARN = "arn";
  @SerializedName(SERIALIZED_NAME_ARN)
  private String arn;

  public static final String SERIALIZED_NAME_BIN = "bin";
  @SerializedName(SERIALIZED_NAME_BIN)
  private String bin;

  public static final String SERIALIZED_NAME_BUMP_OFFER = "bumpOffer";
  @SerializedName(SERIALIZED_NAME_BUMP_OFFER)
  private TransactionAllOfBumpOffer bumpOffer;

  public static final String SERIALIZED_NAME_DCC = "dcc";
  @SerializedName(SERIALIZED_NAME_DCC)
  private TransactionAllOfDcc dcc;

  public static final String SERIALIZED_NAME_DISCREPANCY_TIME = "discrepancyTime";
  @SerializedName(SERIALIZED_NAME_DISCREPANCY_TIME)
  private OffsetDateTime discrepancyTime;

  /**
   * The dispute&#39;s status, else null.
   */
  @JsonAdapter(DisputeStatusEnum.Adapter.class)
  public enum DisputeStatusEnum {
    RESPONSE_NEEDED("response-needed"),
    
    UNDER_REVIEW("under-review"),
    
    FORFEITED("forfeited"),
    
    WON("won"),
    
    LOST("lost"),
    
    UNKNOWN("unknown");

    private String value;

    DisputeStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DisputeStatusEnum fromValue(String value) {
      for (DisputeStatusEnum b : DisputeStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<DisputeStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DisputeStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DisputeStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DisputeStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DisputeStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DISPUTE_STATUS = "disputeStatus";
  @SerializedName(SERIALIZED_NAME_DISPUTE_STATUS)
  private DisputeStatusEnum disputeStatus;

  public static final String SERIALIZED_NAME_DISPUTE_TIME = "disputeTime";
  @SerializedName(SERIALIZED_NAME_DISPUTE_TIME)
  private OffsetDateTime disputeTime;

  public static final String SERIALIZED_NAME_GATEWAY = "gateway";
  @SerializedName(SERIALIZED_NAME_GATEWAY)
  private TransactionAllOfGateway gateway;

  public static final String SERIALIZED_NAME_GATEWAY_ACCOUNT_ID = "gatewayAccountId";
  @SerializedName(SERIALIZED_NAME_GATEWAY_ACCOUNT_ID)
  private String gatewayAccountId;

  public static final String SERIALIZED_NAME_GATEWAY_TRANSACTION_ID = "gatewayTransactionId";
  @SerializedName(SERIALIZED_NAME_GATEWAY_TRANSACTION_ID)
  private String gatewayTransactionId;

  public static final String SERIALIZED_NAME_HAD_DISCREPANCY = "hadDiscrepancy";
  @SerializedName(SERIALIZED_NAME_HAD_DISCREPANCY)
  private Boolean hadDiscrepancy;

  public static final String SERIALIZED_NAME_HAS_BUMP_OFFER = "hasBumpOffer";
  @SerializedName(SERIALIZED_NAME_HAS_BUMP_OFFER)
  private Boolean hasBumpOffer;

  public static final String SERIALIZED_NAME_HAS_DCC = "hasDcc";
  @SerializedName(SERIALIZED_NAME_HAS_DCC)
  private Boolean hasDcc;

  public static final String SERIALIZED_NAME_IS_DISPUTED = "isDisputed";
  @SerializedName(SERIALIZED_NAME_IS_DISPUTED)
  private Boolean isDisputed;

  public static final String SERIALIZED_NAME_IS_MERCHANT_INITIATED = "isMerchantInitiated";
  @SerializedName(SERIALIZED_NAME_IS_MERCHANT_INITIATED)
  private Boolean isMerchantInitiated;

  public static final String SERIALIZED_NAME_IS_PROCESSED_OUTSIDE = "isProcessedOutside";
  @SerializedName(SERIALIZED_NAME_IS_PROCESSED_OUTSIDE)
  private Boolean isProcessedOutside;

  public static final String SERIALIZED_NAME_IS_RECONCILED = "isReconciled";
  @SerializedName(SERIALIZED_NAME_IS_RECONCILED)
  private Boolean isReconciled;

  public static final String SERIALIZED_NAME_METHOD = "method";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_METHOD)
  private PaymentMethod method;

  public static final String SERIALIZED_NAME_NOTIFICATION_URL = "notificationUrl";
  @SerializedName(SERIALIZED_NAME_NOTIFICATION_URL)
  private URI notificationUrl;

  public static final String SERIALIZED_NAME_ORDER_ID = "orderId";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_REFERENCE_DATA = "referenceData";
  @SerializedName(SERIALIZED_NAME_REFERENCE_DATA)
  private Map<String, String> referenceData;

  public static final String SERIALIZED_NAME_REPORT_AMOUNT = "reportAmount";
  @SerializedName(SERIALIZED_NAME_REPORT_AMOUNT)
  private Double reportAmount;

  public static final String SERIALIZED_NAME_REPORT_CURRENCY = "reportCurrency";
  @SerializedName(SERIALIZED_NAME_REPORT_CURRENCY)
  private String reportCurrency;

  public static final String SERIALIZED_NAME_RETRIED_TRANSACTION_ID = "retriedTransactionId";
  @SerializedName(SERIALIZED_NAME_RETRIED_TRANSACTION_ID)
  private String retriedTransactionId;

  /**
   * Retries sequence result.
   */
  @JsonAdapter(RetriesResultEnum.Adapter.class)
  public enum RetriesResultEnum {
    APPROVED("approved"),
    
    CANCELED("canceled"),
    
    DECLINED("declined"),
    
    SCHEDULED("scheduled");

    private String value;

    RetriesResultEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RetriesResultEnum fromValue(String value) {
      for (RetriesResultEnum b : RetriesResultEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RetriesResultEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RetriesResultEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RetriesResultEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RetriesResultEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RetriesResultEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RETRIES_RESULT = "retriesResult";
  @SerializedName(SERIALIZED_NAME_RETRIES_RESULT)
  private RetriesResultEnum retriesResult;

  public static final String SERIALIZED_NAME_RETRY_INSTRUCTION = "retryInstruction";
  @SerializedName(SERIALIZED_NAME_RETRY_INSTRUCTION)
  private PaymentRetry retryInstruction;

  public static final String SERIALIZED_NAME_REVISION = "revision";
  @SerializedName(SERIALIZED_NAME_REVISION)
  private Integer revision;

  public static final String SERIALIZED_NAME_RISK_METADATA = "riskMetadata";
  @SerializedName(SERIALIZED_NAME_RISK_METADATA)
  private RiskMetadata riskMetadata;

  public static final String SERIALIZED_NAME_RISK_SCORE = "riskScore";
  @SerializedName(SERIALIZED_NAME_RISK_SCORE)
  private Integer riskScore;

  public static final String SERIALIZED_NAME_SCHEDULED_TIME = "scheduledTime";
  @SerializedName(SERIALIZED_NAME_SCHEDULED_TIME)
  private OffsetDateTime scheduledTime;

  public static final String SERIALIZED_NAME_SETTLEMENT_TIME = "settlementTime";
  @SerializedName(SERIALIZED_NAME_SETTLEMENT_TIME)
  private OffsetDateTime settlementTime;

  public static final String SERIALIZED_NAME_VELOCITY = "velocity";
  @SerializedName(SERIALIZED_NAME_VELOCITY)
  private Integer velocity;

  public Transaction() {
  }

  public Transaction(
     Double amount, 
     String billingDescriptor, 
     List<String> childTransactions, 
     OffsetDateTime createdTime, 
     String currency, 
     GatewayName gatewayName, 
     Boolean has3ds, 
     Boolean hasAmountAdjustment, 
     String id, 
     List<String> invoiceIds, 
     Boolean isRebill, 
     Boolean isRetry, 
     String parentTransactionId, 
     List<String> planIds, 
     OffsetDateTime processedTime, 
     Double purchaseAmount, 
     String purchaseCurrency, 
     Integer rebillNumber, 
     Double requestAmount, 
     String requestCurrency, 
     ResultEnum result, 
     Integer retryNumber, 
     StatusEnum status, 
     List<String> subscriptionIds, 
     TypeEnum type, 
     OffsetDateTime updatedTime, 
     String websiteId, 
     List<TransactionAllOfEmbedded> embedded, 
     List<TransactionAllOfLinks> links, 
     AcquirerName acquirerName, 
     String arn, 
     String bin, 
     OffsetDateTime discrepancyTime, 
     DisputeStatusEnum disputeStatus, 
     OffsetDateTime disputeTime, 
     String gatewayAccountId, 
     String gatewayTransactionId, 
     Boolean hadDiscrepancy, 
     Boolean hasBumpOffer, 
     Boolean hasDcc, 
     Boolean isDisputed, 
     Boolean isReconciled, 
     Map<String, String> referenceData, 
     Double reportAmount, 
     String reportCurrency, 
     String retriedTransactionId, 
     RetriesResultEnum retriesResult, 
     Integer revision, 
     Integer riskScore, 
     OffsetDateTime settlementTime
  ) {
    this();
    this.amount = amount;
    this.billingDescriptor = billingDescriptor;
    this.childTransactions = childTransactions;
    this.createdTime = createdTime;
    this.currency = currency;
    this.gatewayName = gatewayName;
    this.has3ds = has3ds;
    this.hasAmountAdjustment = hasAmountAdjustment;
    this.id = id;
    this.invoiceIds = invoiceIds;
    this.isRebill = isRebill;
    this.isRetry = isRetry;
    this.parentTransactionId = parentTransactionId;
    this.planIds = planIds;
    this.processedTime = processedTime;
    this.purchaseAmount = purchaseAmount;
    this.purchaseCurrency = purchaseCurrency;
    this.rebillNumber = rebillNumber;
    this.requestAmount = requestAmount;
    this.requestCurrency = requestCurrency;
    this.result = result;
    this.retryNumber = retryNumber;
    this.status = status;
    this.subscriptionIds = subscriptionIds;
    this.type = type;
    this.updatedTime = updatedTime;
    this.websiteId = websiteId;
    this.embedded = embedded;
    this.links = links;
    this.acquirerName = acquirerName;
    this.arn = arn;
    this.bin = bin;
    this.discrepancyTime = discrepancyTime;
    this.disputeStatus = disputeStatus;
    this.disputeTime = disputeTime;
    this.gatewayAccountId = gatewayAccountId;
    this.gatewayTransactionId = gatewayTransactionId;
    this.hadDiscrepancy = hadDiscrepancy;
    this.hasBumpOffer = hasBumpOffer;
    this.hasDcc = hasDcc;
    this.isDisputed = isDisputed;
    this.isReconciled = isReconciled;
    this.referenceData = referenceData;
    this.reportAmount = reportAmount;
    this.reportCurrency = reportCurrency;
    this.retriedTransactionId = retriedTransactionId;
    this.retriesResult = retriesResult;
    this.revision = revision;
    this.riskScore = riskScore;
    this.settlementTime = settlementTime;
  }

  public Transaction _3ds(ThreeDSecureResult _3ds) {
    this._3ds = _3ds;
    return this;
  }

  /**
   * Get _3ds
   * @return _3ds
   */
  @javax.annotation.Nullable
  public ThreeDSecureResult get3ds() {
    return _3ds;
  }

  public void set3ds(ThreeDSecureResult _3ds) {
    this._3ds = _3ds;
  }


  /**
   * The transaction&#39;s amount.
   * @return amount
   */
  @javax.annotation.Nullable
  public Double getAmount() {
    return amount;
  }



  public Transaction billingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Billing address.
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public ContactObject getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
  }


  /**
   * The billing descriptor that appears on the periodic billing statement. Commonly 12 or fewer characters for a credit card statement. 
   * @return billingDescriptor
   */
  @javax.annotation.Nullable
  public String getBillingDescriptor() {
    return billingDescriptor;
  }



  /**
   * The child transaction IDs.
   * @return childTransactions
   */
  @javax.annotation.Nullable
  public List<String> getChildTransactions() {
    return childTransactions;
  }



  /**
   * Transaction created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  /**
   * ISO 4217 alphabetic currency code.
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }



  public Transaction customFields(Object customFields) {
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


  public Transaction customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * The сustomer&#39;s ID.
   * @return customerId
   */
  @javax.annotation.Nullable
  public String getCustomerId() {
    return customerId;
  }

  public void setCustomerId(String customerId) {
    this.customerId = customerId;
  }


  public Transaction description(String description) {
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


  /**
   * Payment Gateway name, available only after the gateway is selected for the transaction. 
   * @return gatewayName
   */
  @javax.annotation.Nullable
  public GatewayName getGatewayName() {
    return gatewayName;
  }



  /**
   * Get has3ds
   * @return has3ds
   */
  @javax.annotation.Nullable
  public Boolean getHas3ds() {
    return has3ds;
  }



  /**
   * True if transaction has amount adjustment.
   * @return hasAmountAdjustment
   */
  @javax.annotation.Nullable
  public Boolean getHasAmountAdjustment() {
    return hasAmountAdjustment;
  }



  /**
   * The transaction ID.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * The invoice IDs related to transaction.
   * @return invoiceIds
   */
  @javax.annotation.Nullable
  public List<String> getInvoiceIds() {
    return invoiceIds;
  }



  /**
   * Get isRebill
   * @return isRebill
   */
  @javax.annotation.Nullable
  public Boolean getIsRebill() {
    return isRebill;
  }



  /**
   * True if this transaction is retry.
   * @return isRetry
   */
  @javax.annotation.Nullable
  public Boolean getIsRetry() {
    return isRetry;
  }



  /**
   * The parent&#39;s transaction ID.
   * @return parentTransactionId
   */
  @javax.annotation.Nullable
  public String getParentTransactionId() {
    return parentTransactionId;
  }



  public Transaction paymentInstrument(PaymentInstrument paymentInstrument) {
    this.paymentInstrument = paymentInstrument;
    return this;
  }

  /**
   * Get paymentInstrument
   * @return paymentInstrument
   */
  @javax.annotation.Nullable
  public PaymentInstrument getPaymentInstrument() {
    return paymentInstrument;
  }

  public void setPaymentInstrument(PaymentInstrument paymentInstrument) {
    this.paymentInstrument = paymentInstrument;
  }


  /**
   * The plan IDs related to transaction&#39;s order(s).
   * @return planIds
   */
  @javax.annotation.Nullable
  public List<String> getPlanIds() {
    return planIds;
  }



  /**
   * Transaction processed time.
   * @return processedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getProcessedTime() {
    return processedTime;
  }



  /**
   * The amount actually purchased which may have differed from the originally requested amount in case of an adjustment.
   * @return purchaseAmount
   */
  @javax.annotation.Nullable
  public Double getPurchaseAmount() {
    return purchaseAmount;
  }



  /**
   * ISO 4217 alphabetic currency code.
   * @return purchaseCurrency
   */
  @javax.annotation.Nullable
  public String getPurchaseCurrency() {
    return purchaseCurrency;
  }



  /**
   * The transaction&#39;s rebill number.
   * @return rebillNumber
   */
  @javax.annotation.Nullable
  public Integer getRebillNumber() {
    return rebillNumber;
  }



  public Transaction redirectUrl(URI redirectUrl) {
    this.redirectUrl = redirectUrl;
    return this;
  }

  /**
   * The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website&#39;s configured URL.
   * @return redirectUrl
   */
  @javax.annotation.Nullable
  public URI getRedirectUrl() {
    return redirectUrl;
  }

  public void setRedirectUrl(URI redirectUrl) {
    this.redirectUrl = redirectUrl;
  }


  /**
   * The amount in the payment request. If adjusted, the purchase amount and billing amount may vary from it.
   * @return requestAmount
   */
  @javax.annotation.Nullable
  public Double getRequestAmount() {
    return requestAmount;
  }



  /**
   * ISO 4217 alphabetic currency code.
   * @return requestCurrency
   */
  @javax.annotation.Nullable
  public String getRequestCurrency() {
    return requestCurrency;
  }



  public Transaction requestId(String requestId) {
    this.requestId = requestId;
    return this;
  }

  /**
   * The transaction&#39;s request ID.  This ID must be unique within a 24 hour period. Use this field to prevent duplicated transactions.
   * @return requestId
   */
  @javax.annotation.Nullable
  public String getRequestId() {
    return requestId;
  }

  public void setRequestId(String requestId) {
    this.requestId = requestId;
  }


  /**
   * Transaction result.
   * @return result
   */
  @javax.annotation.Nullable
  public ResultEnum getResult() {
    return result;
  }



  /**
   * The position in the sequence of retries.
   * @return retryNumber
   */
  @javax.annotation.Nullable
  public Integer getRetryNumber() {
    return retryNumber;
  }



  /**
   * Transaction status.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  /**
   * The orders IDs related to transaction&#39;s invoice(s).
   * @return subscriptionIds
   */
  @javax.annotation.Nullable
  public List<String> getSubscriptionIds() {
    return subscriptionIds;
  }



  /**
   * Transaction type.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }



  /**
   * Transaction updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  /**
   * The website ID.
   * @return websiteId
   */
  @javax.annotation.Nullable
  public String getWebsiteId() {
    return websiteId;
  }



  /**
   * Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter.
   * @return embedded
   */
  @javax.annotation.Nullable
  public List<TransactionAllOfEmbedded> getEmbedded() {
    return embedded;
  }



  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<TransactionAllOfLinks> getLinks() {
    return links;
  }



  /**
   * Acquirer name, available only when transaction use gateway, else null.
   * @return acquirerName
   */
  @javax.annotation.Nullable
  public AcquirerName getAcquirerName() {
    return acquirerName;
  }



  /**
   * The acquirer reference number.
   * @return arn
   */
  @javax.annotation.Nullable
  public String getArn() {
    return arn;
  }



  /**
   * Payment Card BIN.
   * @return bin
   */
  @javax.annotation.Nullable
  public String getBin() {
    return bin;
  }



  public Transaction bumpOffer(TransactionAllOfBumpOffer bumpOffer) {
    this.bumpOffer = bumpOffer;
    return this;
  }

  /**
   * Get bumpOffer
   * @return bumpOffer
   */
  @javax.annotation.Nullable
  public TransactionAllOfBumpOffer getBumpOffer() {
    return bumpOffer;
  }

  public void setBumpOffer(TransactionAllOfBumpOffer bumpOffer) {
    this.bumpOffer = bumpOffer;
  }


  public Transaction dcc(TransactionAllOfDcc dcc) {
    this.dcc = dcc;
    return this;
  }

  /**
   * Get dcc
   * @return dcc
   */
  @javax.annotation.Nullable
  public TransactionAllOfDcc getDcc() {
    return dcc;
  }

  public void setDcc(TransactionAllOfDcc dcc) {
    this.dcc = dcc;
  }


  /**
   * The time of the most recent discrepancy on the transaction.
   * @return discrepancyTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDiscrepancyTime() {
    return discrepancyTime;
  }



  /**
   * The dispute&#39;s status, else null.
   * @return disputeStatus
   */
  @javax.annotation.Nullable
  public DisputeStatusEnum getDisputeStatus() {
    return disputeStatus;
  }



  /**
   * Time the dispute was created, else null.
   * @return disputeTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDisputeTime() {
    return disputeTime;
  }



  public Transaction gateway(TransactionAllOfGateway gateway) {
    this.gateway = gateway;
    return this;
  }

  /**
   * Get gateway
   * @return gateway
   */
  @javax.annotation.Nullable
  public TransactionAllOfGateway getGateway() {
    return gateway;
  }

  public void setGateway(TransactionAllOfGateway gateway) {
    this.gateway = gateway;
  }


  /**
   * The transaction&#39;s Gateway Account ID.
   * @return gatewayAccountId
   */
  @javax.annotation.Nullable
  public String getGatewayAccountId() {
    return gatewayAccountId;
  }



  /**
   * The gateway&#39;s transaction ID.
   * @return gatewayTransactionId
   */
  @javax.annotation.Nullable
  public String getGatewayTransactionId() {
    return gatewayTransactionId;
  }



  /**
   * True if the transaction has been updated due to a discrepancy with its. source of truth.
   * @return hadDiscrepancy
   */
  @javax.annotation.Nullable
  public Boolean getHadDiscrepancy() {
    return hadDiscrepancy;
  }



  /**
   * True if transaction has a Bump offer.
   * @return hasBumpOffer
   */
  @javax.annotation.Nullable
  public Boolean getHasBumpOffer() {
    return hasBumpOffer;
  }



  /**
   * True if transaction has Dynamic Currency Conversion applied.
   * @return hasDcc
   */
  @javax.annotation.Nullable
  public Boolean getHasDcc() {
    return hasDcc;
  }



  /**
   * True if transaction is disputed.
   * @return isDisputed
   */
  @javax.annotation.Nullable
  public Boolean getIsDisputed() {
    return isDisputed;
  }



  public Transaction isMerchantInitiated(Boolean isMerchantInitiated) {
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


  public Transaction isProcessedOutside(Boolean isProcessedOutside) {
    this.isProcessedOutside = isProcessedOutside;
    return this;
  }

  /**
   * True if the transaction was processed outside of Rebilly.
   * @return isProcessedOutside
   */
  @javax.annotation.Nullable
  public Boolean getIsProcessedOutside() {
    return isProcessedOutside;
  }

  public void setIsProcessedOutside(Boolean isProcessedOutside) {
    this.isProcessedOutside = isProcessedOutside;
  }


  /**
   * True if the transaction has been verified with gateway batch data.
   * @return isReconciled
   */
  @javax.annotation.Nullable
  public Boolean getIsReconciled() {
    return isReconciled;
  }



  @Deprecated
  public Transaction method(PaymentMethod method) {
    this.method = method;
    return this;
  }

  /**
   * Payment Method. Use &#x60;paymentInstrument.method&#x60; instead.
   * @return method
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public PaymentMethod getMethod() {
    return method;
  }

  @Deprecated
  public void setMethod(PaymentMethod method) {
    this.method = method;
  }


  public Transaction notificationUrl(URI notificationUrl) {
    this.notificationUrl = notificationUrl;
    return this;
  }

  /**
   * The URL where a server-to-server POST notification will be sent.  It  will be sent when the transaction&#39;s result is finalized after a timeout or an offsite interaction. Do not trust the notification; follow with a GET request to confirm the result of the transaction. Please respond with a 2xx HTTP status code, or we will reattempt the request again. The 2 placeholders are available to use in this URI: &#x60;{id}&#x60; and &#x60;{result}&#x60;. 
   * @return notificationUrl
   */
  @javax.annotation.Nullable
  public URI getNotificationUrl() {
    return notificationUrl;
  }

  public void setNotificationUrl(URI notificationUrl) {
    this.notificationUrl = notificationUrl;
  }


  @Deprecated
  public Transaction orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * The transaction&#39;s order ID.  This ID must be unique within a 24 hour period. This field was renamed to the &#x60;requestId&#x60;.
   * @return orderId
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getOrderId() {
    return orderId;
  }

  @Deprecated
  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  /**
   * Transaction reference data.
   * @return referenceData
   */
  @javax.annotation.Nullable
  public Map<String, String> getReferenceData() {
    return referenceData;
  }



  /**
   * Transaction amount converted to organization&amp;nbsp;selected report currency.
   * @return reportAmount
   */
  @javax.annotation.Nullable
  public Double getReportAmount() {
    return reportAmount;
  }



  /**
   * ISO 4217 alphabetic currency code.
   * @return reportCurrency
   */
  @javax.annotation.Nullable
  public String getReportCurrency() {
    return reportCurrency;
  }



  /**
   * The retried transaction ID.
   * @return retriedTransactionId
   */
  @javax.annotation.Nullable
  public String getRetriedTransactionId() {
    return retriedTransactionId;
  }



  /**
   * Retries sequence result.
   * @return retriesResult
   */
  @javax.annotation.Nullable
  public RetriesResultEnum getRetriesResult() {
    return retriesResult;
  }



  public Transaction retryInstruction(PaymentRetry retryInstruction) {
    this.retryInstruction = retryInstruction;
    return this;
  }

  /**
   * Get retryInstruction
   * @return retryInstruction
   */
  @javax.annotation.Nullable
  public PaymentRetry getRetryInstruction() {
    return retryInstruction;
  }

  public void setRetryInstruction(PaymentRetry retryInstruction) {
    this.retryInstruction = retryInstruction;
  }


  /**
   * The number of times the transaction data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
   * @return revision
   */
  @javax.annotation.Nullable
  public Integer getRevision() {
    return revision;
  }



  public Transaction riskMetadata(RiskMetadata riskMetadata) {
    this.riskMetadata = riskMetadata;
    return this;
  }

  /**
   * Risk metadata.
   * @return riskMetadata
   */
  @javax.annotation.Nullable
  public RiskMetadata getRiskMetadata() {
    return riskMetadata;
  }

  public void setRiskMetadata(RiskMetadata riskMetadata) {
    this.riskMetadata = riskMetadata;
  }


  /**
   * The transaction&#39;s risk score.
   * @return riskScore
   */
  @javax.annotation.Nullable
  public Integer getRiskScore() {
    return riskScore;
  }



  public Transaction scheduledTime(OffsetDateTime scheduledTime) {
    this.scheduledTime = scheduledTime;
    return this;
  }

  /**
   * The time the transaction is scheduled for collection.
   * @return scheduledTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getScheduledTime() {
    return scheduledTime;
  }

  public void setScheduledTime(OffsetDateTime scheduledTime) {
    this.scheduledTime = scheduledTime;
  }


  /**
   * The time that the transaction was settled by the banking instuition.
   * @return settlementTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getSettlementTime() {
    return settlementTime;
  }



  public Transaction velocity(Integer velocity) {
    this.velocity = velocity;
    return this;
  }

  /**
   * The number of transactions by the same customer in the past 24 hours.
   * @return velocity
   */
  @javax.annotation.Nullable
  public Integer getVelocity() {
    return velocity;
  }

  public void setVelocity(Integer velocity) {
    this.velocity = velocity;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Transaction transaction = (Transaction) o;
    return Objects.equals(this._3ds, transaction._3ds) &&
        Objects.equals(this.amount, transaction.amount) &&
        Objects.equals(this.billingAddress, transaction.billingAddress) &&
        Objects.equals(this.billingDescriptor, transaction.billingDescriptor) &&
        Objects.equals(this.childTransactions, transaction.childTransactions) &&
        Objects.equals(this.createdTime, transaction.createdTime) &&
        Objects.equals(this.currency, transaction.currency) &&
        Objects.equals(this.customFields, transaction.customFields) &&
        Objects.equals(this.customerId, transaction.customerId) &&
        Objects.equals(this.description, transaction.description) &&
        Objects.equals(this.gatewayName, transaction.gatewayName) &&
        Objects.equals(this.has3ds, transaction.has3ds) &&
        Objects.equals(this.hasAmountAdjustment, transaction.hasAmountAdjustment) &&
        Objects.equals(this.id, transaction.id) &&
        Objects.equals(this.invoiceIds, transaction.invoiceIds) &&
        Objects.equals(this.isRebill, transaction.isRebill) &&
        Objects.equals(this.isRetry, transaction.isRetry) &&
        Objects.equals(this.parentTransactionId, transaction.parentTransactionId) &&
        Objects.equals(this.paymentInstrument, transaction.paymentInstrument) &&
        Objects.equals(this.planIds, transaction.planIds) &&
        Objects.equals(this.processedTime, transaction.processedTime) &&
        Objects.equals(this.purchaseAmount, transaction.purchaseAmount) &&
        Objects.equals(this.purchaseCurrency, transaction.purchaseCurrency) &&
        Objects.equals(this.rebillNumber, transaction.rebillNumber) &&
        Objects.equals(this.redirectUrl, transaction.redirectUrl) &&
        Objects.equals(this.requestAmount, transaction.requestAmount) &&
        Objects.equals(this.requestCurrency, transaction.requestCurrency) &&
        Objects.equals(this.requestId, transaction.requestId) &&
        Objects.equals(this.result, transaction.result) &&
        Objects.equals(this.retryNumber, transaction.retryNumber) &&
        Objects.equals(this.status, transaction.status) &&
        Objects.equals(this.subscriptionIds, transaction.subscriptionIds) &&
        Objects.equals(this.type, transaction.type) &&
        Objects.equals(this.updatedTime, transaction.updatedTime) &&
        Objects.equals(this.websiteId, transaction.websiteId) &&
        Objects.equals(this.embedded, transaction.embedded) &&
        Objects.equals(this.links, transaction.links) &&
        Objects.equals(this.acquirerName, transaction.acquirerName) &&
        Objects.equals(this.arn, transaction.arn) &&
        Objects.equals(this.bin, transaction.bin) &&
        Objects.equals(this.bumpOffer, transaction.bumpOffer) &&
        Objects.equals(this.dcc, transaction.dcc) &&
        Objects.equals(this.discrepancyTime, transaction.discrepancyTime) &&
        Objects.equals(this.disputeStatus, transaction.disputeStatus) &&
        Objects.equals(this.disputeTime, transaction.disputeTime) &&
        Objects.equals(this.gateway, transaction.gateway) &&
        Objects.equals(this.gatewayAccountId, transaction.gatewayAccountId) &&
        Objects.equals(this.gatewayTransactionId, transaction.gatewayTransactionId) &&
        Objects.equals(this.hadDiscrepancy, transaction.hadDiscrepancy) &&
        Objects.equals(this.hasBumpOffer, transaction.hasBumpOffer) &&
        Objects.equals(this.hasDcc, transaction.hasDcc) &&
        Objects.equals(this.isDisputed, transaction.isDisputed) &&
        Objects.equals(this.isMerchantInitiated, transaction.isMerchantInitiated) &&
        Objects.equals(this.isProcessedOutside, transaction.isProcessedOutside) &&
        Objects.equals(this.isReconciled, transaction.isReconciled) &&
        Objects.equals(this.method, transaction.method) &&
        Objects.equals(this.notificationUrl, transaction.notificationUrl) &&
        Objects.equals(this.orderId, transaction.orderId) &&
        Objects.equals(this.referenceData, transaction.referenceData) &&
        Objects.equals(this.reportAmount, transaction.reportAmount) &&
        Objects.equals(this.reportCurrency, transaction.reportCurrency) &&
        Objects.equals(this.retriedTransactionId, transaction.retriedTransactionId) &&
        Objects.equals(this.retriesResult, transaction.retriesResult) &&
        Objects.equals(this.retryInstruction, transaction.retryInstruction) &&
        Objects.equals(this.revision, transaction.revision) &&
        Objects.equals(this.riskMetadata, transaction.riskMetadata) &&
        Objects.equals(this.riskScore, transaction.riskScore) &&
        Objects.equals(this.scheduledTime, transaction.scheduledTime) &&
        Objects.equals(this.settlementTime, transaction.settlementTime) &&
        Objects.equals(this.velocity, transaction.velocity);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(_3ds, amount, billingAddress, billingDescriptor, childTransactions, createdTime, currency, customFields, customerId, description, gatewayName, has3ds, hasAmountAdjustment, id, invoiceIds, isRebill, isRetry, parentTransactionId, paymentInstrument, planIds, processedTime, purchaseAmount, purchaseCurrency, rebillNumber, redirectUrl, requestAmount, requestCurrency, requestId, result, retryNumber, status, subscriptionIds, type, updatedTime, websiteId, embedded, links, acquirerName, arn, bin, bumpOffer, dcc, discrepancyTime, disputeStatus, disputeTime, gateway, gatewayAccountId, gatewayTransactionId, hadDiscrepancy, hasBumpOffer, hasDcc, isDisputed, isMerchantInitiated, isProcessedOutside, isReconciled, method, notificationUrl, orderId, referenceData, reportAmount, reportCurrency, retriedTransactionId, retriesResult, retryInstruction, revision, riskMetadata, riskScore, scheduledTime, settlementTime, velocity);
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
    sb.append("class Transaction {\n");
    sb.append("    _3ds: ").append(toIndentedString(_3ds)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    billingDescriptor: ").append(toIndentedString(billingDescriptor)).append("\n");
    sb.append("    childTransactions: ").append(toIndentedString(childTransactions)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    gatewayName: ").append(toIndentedString(gatewayName)).append("\n");
    sb.append("    has3ds: ").append(toIndentedString(has3ds)).append("\n");
    sb.append("    hasAmountAdjustment: ").append(toIndentedString(hasAmountAdjustment)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invoiceIds: ").append(toIndentedString(invoiceIds)).append("\n");
    sb.append("    isRebill: ").append(toIndentedString(isRebill)).append("\n");
    sb.append("    isRetry: ").append(toIndentedString(isRetry)).append("\n");
    sb.append("    parentTransactionId: ").append(toIndentedString(parentTransactionId)).append("\n");
    sb.append("    paymentInstrument: ").append(toIndentedString(paymentInstrument)).append("\n");
    sb.append("    planIds: ").append(toIndentedString(planIds)).append("\n");
    sb.append("    processedTime: ").append(toIndentedString(processedTime)).append("\n");
    sb.append("    purchaseAmount: ").append(toIndentedString(purchaseAmount)).append("\n");
    sb.append("    purchaseCurrency: ").append(toIndentedString(purchaseCurrency)).append("\n");
    sb.append("    rebillNumber: ").append(toIndentedString(rebillNumber)).append("\n");
    sb.append("    redirectUrl: ").append(toIndentedString(redirectUrl)).append("\n");
    sb.append("    requestAmount: ").append(toIndentedString(requestAmount)).append("\n");
    sb.append("    requestCurrency: ").append(toIndentedString(requestCurrency)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
    sb.append("    retryNumber: ").append(toIndentedString(retryNumber)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subscriptionIds: ").append(toIndentedString(subscriptionIds)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    websiteId: ").append(toIndentedString(websiteId)).append("\n");
    sb.append("    embedded: ").append(toIndentedString(embedded)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    acquirerName: ").append(toIndentedString(acquirerName)).append("\n");
    sb.append("    arn: ").append(toIndentedString(arn)).append("\n");
    sb.append("    bin: ").append(toIndentedString(bin)).append("\n");
    sb.append("    bumpOffer: ").append(toIndentedString(bumpOffer)).append("\n");
    sb.append("    dcc: ").append(toIndentedString(dcc)).append("\n");
    sb.append("    discrepancyTime: ").append(toIndentedString(discrepancyTime)).append("\n");
    sb.append("    disputeStatus: ").append(toIndentedString(disputeStatus)).append("\n");
    sb.append("    disputeTime: ").append(toIndentedString(disputeTime)).append("\n");
    sb.append("    gateway: ").append(toIndentedString(gateway)).append("\n");
    sb.append("    gatewayAccountId: ").append(toIndentedString(gatewayAccountId)).append("\n");
    sb.append("    gatewayTransactionId: ").append(toIndentedString(gatewayTransactionId)).append("\n");
    sb.append("    hadDiscrepancy: ").append(toIndentedString(hadDiscrepancy)).append("\n");
    sb.append("    hasBumpOffer: ").append(toIndentedString(hasBumpOffer)).append("\n");
    sb.append("    hasDcc: ").append(toIndentedString(hasDcc)).append("\n");
    sb.append("    isDisputed: ").append(toIndentedString(isDisputed)).append("\n");
    sb.append("    isMerchantInitiated: ").append(toIndentedString(isMerchantInitiated)).append("\n");
    sb.append("    isProcessedOutside: ").append(toIndentedString(isProcessedOutside)).append("\n");
    sb.append("    isReconciled: ").append(toIndentedString(isReconciled)).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    notificationUrl: ").append(toIndentedString(notificationUrl)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    referenceData: ").append(toIndentedString(referenceData)).append("\n");
    sb.append("    reportAmount: ").append(toIndentedString(reportAmount)).append("\n");
    sb.append("    reportCurrency: ").append(toIndentedString(reportCurrency)).append("\n");
    sb.append("    retriedTransactionId: ").append(toIndentedString(retriedTransactionId)).append("\n");
    sb.append("    retriesResult: ").append(toIndentedString(retriesResult)).append("\n");
    sb.append("    retryInstruction: ").append(toIndentedString(retryInstruction)).append("\n");
    sb.append("    revision: ").append(toIndentedString(revision)).append("\n");
    sb.append("    riskMetadata: ").append(toIndentedString(riskMetadata)).append("\n");
    sb.append("    riskScore: ").append(toIndentedString(riskScore)).append("\n");
    sb.append("    scheduledTime: ").append(toIndentedString(scheduledTime)).append("\n");
    sb.append("    settlementTime: ").append(toIndentedString(settlementTime)).append("\n");
    sb.append("    velocity: ").append(toIndentedString(velocity)).append("\n");
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
    openapiFields.add("3ds");
    openapiFields.add("amount");
    openapiFields.add("billingAddress");
    openapiFields.add("billingDescriptor");
    openapiFields.add("childTransactions");
    openapiFields.add("createdTime");
    openapiFields.add("currency");
    openapiFields.add("customFields");
    openapiFields.add("customerId");
    openapiFields.add("description");
    openapiFields.add("gatewayName");
    openapiFields.add("has3ds");
    openapiFields.add("hasAmountAdjustment");
    openapiFields.add("id");
    openapiFields.add("invoiceIds");
    openapiFields.add("isRebill");
    openapiFields.add("isRetry");
    openapiFields.add("parentTransactionId");
    openapiFields.add("paymentInstrument");
    openapiFields.add("planIds");
    openapiFields.add("processedTime");
    openapiFields.add("purchaseAmount");
    openapiFields.add("purchaseCurrency");
    openapiFields.add("rebillNumber");
    openapiFields.add("redirectUrl");
    openapiFields.add("requestAmount");
    openapiFields.add("requestCurrency");
    openapiFields.add("requestId");
    openapiFields.add("result");
    openapiFields.add("retryNumber");
    openapiFields.add("status");
    openapiFields.add("subscriptionIds");
    openapiFields.add("type");
    openapiFields.add("updatedTime");
    openapiFields.add("websiteId");
    openapiFields.add("_embedded");
    openapiFields.add("_links");
    openapiFields.add("acquirerName");
    openapiFields.add("arn");
    openapiFields.add("bin");
    openapiFields.add("bumpOffer");
    openapiFields.add("dcc");
    openapiFields.add("discrepancyTime");
    openapiFields.add("disputeStatus");
    openapiFields.add("disputeTime");
    openapiFields.add("gateway");
    openapiFields.add("gatewayAccountId");
    openapiFields.add("gatewayTransactionId");
    openapiFields.add("hadDiscrepancy");
    openapiFields.add("hasBumpOffer");
    openapiFields.add("hasDcc");
    openapiFields.add("isDisputed");
    openapiFields.add("isMerchantInitiated");
    openapiFields.add("isProcessedOutside");
    openapiFields.add("isReconciled");
    openapiFields.add("method");
    openapiFields.add("notificationUrl");
    openapiFields.add("orderId");
    openapiFields.add("referenceData");
    openapiFields.add("reportAmount");
    openapiFields.add("reportCurrency");
    openapiFields.add("retriedTransactionId");
    openapiFields.add("retriesResult");
    openapiFields.add("retryInstruction");
    openapiFields.add("revision");
    openapiFields.add("riskMetadata");
    openapiFields.add("riskScore");
    openapiFields.add("scheduledTime");
    openapiFields.add("settlementTime");
    openapiFields.add("velocity");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Transaction
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Transaction.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Transaction is not found in the empty JSON string", Transaction.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Transaction.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Transaction` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `3ds`
      if (jsonObj.get("3ds") != null && !jsonObj.get("3ds").isJsonNull()) {
        ThreeDSecureResult.validateJsonElement(jsonObj.get("3ds"));
      }
      // validate the optional field `billingAddress`
      if (jsonObj.get("billingAddress") != null && !jsonObj.get("billingAddress").isJsonNull()) {
        ContactObject.validateJsonElement(jsonObj.get("billingAddress"));
      }
      if ((jsonObj.get("billingDescriptor") != null && !jsonObj.get("billingDescriptor").isJsonNull()) && !jsonObj.get("billingDescriptor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billingDescriptor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billingDescriptor").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("childTransactions") != null && !jsonObj.get("childTransactions").isJsonNull() && !jsonObj.get("childTransactions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `childTransactions` to be an array in the JSON string but got `%s`", jsonObj.get("childTransactions").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if ((jsonObj.get("customerId") != null && !jsonObj.get("customerId").isJsonNull()) && !jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `gatewayName`
      if (jsonObj.get("gatewayName") != null && !jsonObj.get("gatewayName").isJsonNull()) {
        GatewayName.validateJsonElement(jsonObj.get("gatewayName"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("invoiceIds") != null && !jsonObj.get("invoiceIds").isJsonNull() && !jsonObj.get("invoiceIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoiceIds` to be an array in the JSON string but got `%s`", jsonObj.get("invoiceIds").toString()));
      }
      if ((jsonObj.get("parentTransactionId") != null && !jsonObj.get("parentTransactionId").isJsonNull()) && !jsonObj.get("parentTransactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parentTransactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parentTransactionId").toString()));
      }
      // validate the optional field `paymentInstrument`
      if (jsonObj.get("paymentInstrument") != null && !jsonObj.get("paymentInstrument").isJsonNull()) {
        PaymentInstrument.validateJsonElement(jsonObj.get("paymentInstrument"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("planIds") != null && !jsonObj.get("planIds").isJsonNull() && !jsonObj.get("planIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `planIds` to be an array in the JSON string but got `%s`", jsonObj.get("planIds").toString()));
      }
      if ((jsonObj.get("purchaseCurrency") != null && !jsonObj.get("purchaseCurrency").isJsonNull()) && !jsonObj.get("purchaseCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `purchaseCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("purchaseCurrency").toString()));
      }
      if ((jsonObj.get("redirectUrl") != null && !jsonObj.get("redirectUrl").isJsonNull()) && !jsonObj.get("redirectUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `redirectUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("redirectUrl").toString()));
      }
      if ((jsonObj.get("requestCurrency") != null && !jsonObj.get("requestCurrency").isJsonNull()) && !jsonObj.get("requestCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestCurrency").toString()));
      }
      if ((jsonObj.get("requestId") != null && !jsonObj.get("requestId").isJsonNull()) && !jsonObj.get("requestId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestId").toString()));
      }
      if ((jsonObj.get("result") != null && !jsonObj.get("result").isJsonNull()) && !jsonObj.get("result").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `result` to be a primitive type in the JSON string but got `%s`", jsonObj.get("result").toString()));
      }
      // validate the optional field `result`
      if (jsonObj.get("result") != null && !jsonObj.get("result").isJsonNull()) {
        ResultEnum.validateJsonElement(jsonObj.get("result"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("subscriptionIds") != null && !jsonObj.get("subscriptionIds").isJsonNull() && !jsonObj.get("subscriptionIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriptionIds` to be an array in the JSON string but got `%s`", jsonObj.get("subscriptionIds").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
      if ((jsonObj.get("websiteId") != null && !jsonObj.get("websiteId").isJsonNull()) && !jsonObj.get("websiteId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `websiteId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("websiteId").toString()));
      }
      if (jsonObj.get("_embedded") != null && !jsonObj.get("_embedded").isJsonNull()) {
        JsonArray jsonArrayembedded = jsonObj.getAsJsonArray("_embedded");
        if (jsonArrayembedded != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_embedded").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_embedded` to be an array in the JSON string but got `%s`", jsonObj.get("_embedded").toString()));
          }

          // validate the optional field `_embedded` (array)
          for (int i = 0; i < jsonArrayembedded.size(); i++) {
            TransactionAllOfEmbedded.validateJsonElement(jsonArrayembedded.get(i));
          };
        }
      }
      if (jsonObj.get("_links") != null && !jsonObj.get("_links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("_links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_links` to be an array in the JSON string but got `%s`", jsonObj.get("_links").toString()));
          }

          // validate the optional field `_links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            TransactionAllOfLinks.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      // validate the optional field `acquirerName`
      if (jsonObj.get("acquirerName") != null && !jsonObj.get("acquirerName").isJsonNull()) {
        AcquirerName.validateJsonElement(jsonObj.get("acquirerName"));
      }
      if ((jsonObj.get("arn") != null && !jsonObj.get("arn").isJsonNull()) && !jsonObj.get("arn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `arn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("arn").toString()));
      }
      if ((jsonObj.get("bin") != null && !jsonObj.get("bin").isJsonNull()) && !jsonObj.get("bin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bin").toString()));
      }
      // validate the optional field `bumpOffer`
      if (jsonObj.get("bumpOffer") != null && !jsonObj.get("bumpOffer").isJsonNull()) {
        TransactionAllOfBumpOffer.validateJsonElement(jsonObj.get("bumpOffer"));
      }
      // validate the optional field `dcc`
      if (jsonObj.get("dcc") != null && !jsonObj.get("dcc").isJsonNull()) {
        TransactionAllOfDcc.validateJsonElement(jsonObj.get("dcc"));
      }
      if ((jsonObj.get("disputeStatus") != null && !jsonObj.get("disputeStatus").isJsonNull()) && !jsonObj.get("disputeStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `disputeStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("disputeStatus").toString()));
      }
      // validate the optional field `disputeStatus`
      if (jsonObj.get("disputeStatus") != null && !jsonObj.get("disputeStatus").isJsonNull()) {
        DisputeStatusEnum.validateJsonElement(jsonObj.get("disputeStatus"));
      }
      // validate the optional field `gateway`
      if (jsonObj.get("gateway") != null && !jsonObj.get("gateway").isJsonNull()) {
        TransactionAllOfGateway.validateJsonElement(jsonObj.get("gateway"));
      }
      if ((jsonObj.get("gatewayAccountId") != null && !jsonObj.get("gatewayAccountId").isJsonNull()) && !jsonObj.get("gatewayAccountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gatewayAccountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gatewayAccountId").toString()));
      }
      if ((jsonObj.get("gatewayTransactionId") != null && !jsonObj.get("gatewayTransactionId").isJsonNull()) && !jsonObj.get("gatewayTransactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gatewayTransactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gatewayTransactionId").toString()));
      }
      // validate the optional field `method`
      if (jsonObj.get("method") != null && !jsonObj.get("method").isJsonNull()) {
        PaymentMethod.validateJsonElement(jsonObj.get("method"));
      }
      if ((jsonObj.get("notificationUrl") != null && !jsonObj.get("notificationUrl").isJsonNull()) && !jsonObj.get("notificationUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notificationUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notificationUrl").toString()));
      }
      if ((jsonObj.get("orderId") != null && !jsonObj.get("orderId").isJsonNull()) && !jsonObj.get("orderId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderId").toString()));
      }
      if ((jsonObj.get("reportCurrency") != null && !jsonObj.get("reportCurrency").isJsonNull()) && !jsonObj.get("reportCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reportCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reportCurrency").toString()));
      }
      if ((jsonObj.get("retriedTransactionId") != null && !jsonObj.get("retriedTransactionId").isJsonNull()) && !jsonObj.get("retriedTransactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `retriedTransactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("retriedTransactionId").toString()));
      }
      if ((jsonObj.get("retriesResult") != null && !jsonObj.get("retriesResult").isJsonNull()) && !jsonObj.get("retriesResult").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `retriesResult` to be a primitive type in the JSON string but got `%s`", jsonObj.get("retriesResult").toString()));
      }
      // validate the optional field `retriesResult`
      if (jsonObj.get("retriesResult") != null && !jsonObj.get("retriesResult").isJsonNull()) {
        RetriesResultEnum.validateJsonElement(jsonObj.get("retriesResult"));
      }
      // validate the optional field `retryInstruction`
      if (jsonObj.get("retryInstruction") != null && !jsonObj.get("retryInstruction").isJsonNull()) {
        PaymentRetry.validateJsonElement(jsonObj.get("retryInstruction"));
      }
      // validate the optional field `riskMetadata`
      if (jsonObj.get("riskMetadata") != null && !jsonObj.get("riskMetadata").isJsonNull()) {
        RiskMetadata.validateJsonElement(jsonObj.get("riskMetadata"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Transaction.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Transaction' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Transaction> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Transaction.class));

       return (TypeAdapter<T>) new TypeAdapter<Transaction>() {
           @Override
           public void write(JsonWriter out, Transaction value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Transaction read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Transaction given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Transaction
   * @throws IOException if the JSON string is invalid with respect to Transaction
   */
  public static Transaction fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Transaction.class);
  }

  /**
   * Convert an instance of Transaction to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

