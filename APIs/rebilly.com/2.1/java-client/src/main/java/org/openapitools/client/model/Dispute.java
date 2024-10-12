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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.DisputeEmbeddedInner;
import org.openapitools.client.model.DisputeLinksInner;

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
 * Dispute
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Dispute {
  public static final String SERIALIZED_NAME_EMBEDDED = "_embedded";
  @SerializedName(SERIALIZED_NAME_EMBEDDED)
  private List<DisputeEmbeddedInner> embedded = new ArrayList<>();

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<DisputeLinksInner> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_ACQUIRER_REFERENCE_NUMBER = "acquirerReferenceNumber";
  @SerializedName(SERIALIZED_NAME_ACQUIRER_REFERENCE_NUMBER)
  private String acquirerReferenceNumber;

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_CASE_ID = "caseId";
  @SerializedName(SERIALIZED_NAME_CASE_ID)
  private String caseId;

  /**
   * The dispute&#39;s category.
   */
  @JsonAdapter(CategoryEnum.Adapter.class)
  public enum CategoryEnum {
    FRAUD("fraud"),
    
    UNRECOGNIZED("unrecognized"),
    
    PRODUCT_NOT_RECEIVED("product-not-received"),
    
    PRODUCT_UNACCEPTABLE("product-unacceptable"),
    
    PRODUCT_NOT_REFUNDED("product-not-refunded"),
    
    DUPLICATE("duplicate"),
    
    SUBSCRIPTION_CANCELED("subscription-canceled"),
    
    UNCATEGORIZED("uncategorized");

    private String value;

    CategoryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CategoryEnum fromValue(String value) {
      for (CategoryEnum b : CategoryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CategoryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CategoryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CategoryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CategoryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CategoryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CATEGORY = "category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private CategoryEnum category;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_DEADLINE_TIME = "deadlineTime";
  @SerializedName(SERIALIZED_NAME_DEADLINE_TIME)
  private OffsetDateTime deadlineTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_POSTED_TIME = "postedTime";
  @SerializedName(SERIALIZED_NAME_POSTED_TIME)
  private OffsetDateTime postedTime;

  public static final String SERIALIZED_NAME_RAW_RESPONSE = "rawResponse";
  @SerializedName(SERIALIZED_NAME_RAW_RESPONSE)
  private String rawResponse;

  /**
   * The dispute&#39;s reason code.
   */
  @JsonAdapter(ReasonCodeEnum.Adapter.class)
  public enum ReasonCodeEnum {
    _1000("1000"),
    
    _10_1("10.1"),
    
    _10_2("10.2"),
    
    _10_3("10.3"),
    
    _10_4("10.4"),
    
    _10_5("10.5"),
    
    _11_1("11.1"),
    
    _11_2("11.2"),
    
    _11_3("11.3"),
    
    _12("12"),
    
    _12_1("12.1"),
    
    _12_2("12.2"),
    
    _12_3("12.3"),
    
    _12_4("12.4"),
    
    _12_5("12.5"),
    
    _12_6("12.6"),
    
    _12_7("12.7"),
    
    _13_1("13.1"),
    
    _13_2("13.2"),
    
    _13_3("13.3"),
    
    _13_4("13.4"),
    
    _13_5("13.5"),
    
    _13_6("13.6"),
    
    _13_7("13.7"),
    
    _13_8("13.8"),
    
    _13_9("13.9"),
    
    _2("2"),
    
    _30("30"),
    
    _31("31"),
    
    _35("35"),
    
    _37("37"),
    
    _40("40"),
    
    _41("41"),
    
    _42("42"),
    
    _46("46"),
    
    _47("47"),
    
    _49("49"),
    
    _50("50"),
    
    _53("53"),
    
    _54("54"),
    
    _55("55"),
    
    _57("57"),
    
    _59("59"),
    
    _60("60"),
    
    _62("62"),
    
    _7("7"),
    
    _70("70"),
    
    _71("71"),
    
    _722("72"),
    
    _73("73"),
    
    _74("74"),
    
    _75("75"),
    
    _76("76"),
    
    _77("77"),
    
    _79("79"),
    
    _8("8"),
    
    _80("80"),
    
    _81("81"),
    
    _82("82"),
    
    _83("83"),
    
    _85("85"),
    
    _86("86"),
    
    _93("93"),
    
    _00("00"),
    
    _63("63"),
    
    A01("A01"),
    
    A02("A02"),
    
    A08("A08"),
    
    F10("F10"),
    
    F14("F14"),
    
    F22("F22"),
    
    F24("F24"),
    
    F29("F29"),
    
    C02("C02"),
    
    C04("C04"),
    
    C05("C05"),
    
    C08("C08"),
    
    C14("C14"),
    
    C18("C18"),
    
    C28("C28"),
    
    C31("C31"),
    
    C32("C32"),
    
    M10("M10"),
    
    M49("M49"),
    
    P01("P01"),
    
    P03("P03"),
    
    P04("P04"),
    
    P05("P05"),
    
    P07("P07"),
    
    P08("P08"),
    
    P22("P22"),
    
    P23("P23"),
    
    R03("R03"),
    
    R13("R13"),
    
    M01("M01"),
    
    FR1("FR1"),
    
    FR4("FR4"),
    
    FR6("FR6"),
    
    AL("AL"),
    
    AP("AP"),
    
    AW("AW"),
    
    CA("CA"),
    
    CD("CD"),
    
    CR("CR"),
    
    DA("DA"),
    
    DP("DP"),
    
    DP1("DP1"),
    
    EX("EX"),
    
    IC("IC"),
    
    IN("IN"),
    
    IS("IS"),
    
    LP("LP"),
    
    N("N"),
    
    NA("NA"),
    
    NC("NC"),
    
    P("P"),
    
    RG("RG"),
    
    RM("RM"),
    
    RN1("RN1"),
    
    RN2("RN2"),
    
    SV("SV"),
    
    TF("TF"),
    
    TNM("TNM"),
    
    UA01("UA01"),
    
    UA02("UA02"),
    
    UA32("UA32"),
    
    UA99("UA99"),
    
    UA03("UA03"),
    
    UA10("UA10"),
    
    UA11("UA11"),
    
    UA12("UA12"),
    
    UA18("UA18"),
    
    UA20("UA20"),
    
    UA21("UA21"),
    
    UA22("UA22"),
    
    UA23("UA23"),
    
    UA28("UA28"),
    
    UA30("UA30"),
    
    UA31("UA31"),
    
    UA38("UA38"),
    
    DUPLICATE("duplicate"),
    
    FRAUDULENT("fraudulent"),
    
    SUBSCRIPTION_CANCELED("subscription_canceled"),
    
    PRODUCT_UNACCEPTABLE("product_unacceptable"),
    
    PRODUCT_NOT_RECEIVED("product_not_received"),
    
    UNRECOGNIZED("unrecognized"),
    
    CREDIT_NOT_PROCESSED("credit_not_processed"),
    
    CUSTOMER_INITIATED("customer_initiated"),
    
    INCORRECT_ACCOUNT_DETAILS("incorrect_account_details"),
    
    INSUFFICIENT_FUNDS("insufficient_funds"),
    
    BANK_CANNOT_PROCESS("bank_cannot_process"),
    
    DEBIT_NOT_AUTHORIZED("debit_not_authorized"),
    
    GENERAL("general"),
    
    PRE_CHARGEBACK_ALERT("pre-chargeback-alert"),
    
    _0("0"),
    
    _1("1"),
    
    _22("2"),
    
    _3("3"),
    
    _4("4"),
    
    _5("5"),
    
    _6("6"),
    
    _72("7"),
    
    _9("9"),
    
    _51("51"),
    
    A("A"),
    
    B("B");

    private String value;

    ReasonCodeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ReasonCodeEnum fromValue(String value) {
      for (ReasonCodeEnum b : ReasonCodeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ReasonCodeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ReasonCodeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ReasonCodeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ReasonCodeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ReasonCodeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REASON_CODE = "reasonCode";
  @SerializedName(SERIALIZED_NAME_REASON_CODE)
  private ReasonCodeEnum reasonCode;

  public static final String SERIALIZED_NAME_RESOLVED_TIME = "resolvedTime";
  @SerializedName(SERIALIZED_NAME_RESOLVED_TIME)
  private OffsetDateTime resolvedTime;

  /**
   * The dispute&#39;s status.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    RESPONSE_NEEDED("response-needed"),
    
    UNDER_REVIEW("under-review"),
    
    FORFEITED("forfeited"),
    
    WON("won"),
    
    LOST("lost"),
    
    UNKNOWN("unknown");

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

  public static final String SERIALIZED_NAME_TRANSACTION_ID = "transactionId";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_ID)
  private String transactionId;

  /**
   * The dispute&#39;s type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    INFORMATION_REQUEST("information-request"),
    
    FIRST_CHARGEBACK("first-chargeback"),
    
    SECOND_CHARGEBACK("second-chargeback"),
    
    ARBITRATION("arbitration"),
    
    FRAUD("fraud"),
    
    ETHOCA_ALERT("ethoca-alert"),
    
    VERIFI_ALERT("verifi-alert");

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

  public Dispute() {
  }

  public Dispute(
     List<DisputeEmbeddedInner> embedded, 
     List<DisputeLinksInner> links, 
     CategoryEnum category, 
     OffsetDateTime createdTime, 
     String customerId, 
     String id, 
     String rawResponse, 
     OffsetDateTime resolvedTime, 
     OffsetDateTime updatedTime
  ) {
    this();
    this.embedded = embedded;
    this.links = links;
    this.category = category;
    this.createdTime = createdTime;
    this.customerId = customerId;
    this.id = id;
    this.rawResponse = rawResponse;
    this.resolvedTime = resolvedTime;
    this.updatedTime = updatedTime;
  }

  /**
   * Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter.
   * @return embedded
   */
  @javax.annotation.Nullable
  public List<DisputeEmbeddedInner> getEmbedded() {
    return embedded;
  }



  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<DisputeLinksInner> getLinks() {
    return links;
  }



  public Dispute acquirerReferenceNumber(String acquirerReferenceNumber) {
    this.acquirerReferenceNumber = acquirerReferenceNumber;
    return this;
  }

  /**
   * The dispute&#39;s acquirer reference number.
   * @return acquirerReferenceNumber
   */
  @javax.annotation.Nullable
  public String getAcquirerReferenceNumber() {
    return acquirerReferenceNumber;
  }

  public void setAcquirerReferenceNumber(String acquirerReferenceNumber) {
    this.acquirerReferenceNumber = acquirerReferenceNumber;
  }


  public Dispute amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * The dispute amount.
   * @return amount
   */
  @javax.annotation.Nonnull
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public Dispute caseId(String caseId) {
    this.caseId = caseId;
    return this;
  }

  /**
   * The case ID for the dispute.
   * @return caseId
   */
  @javax.annotation.Nullable
  public String getCaseId() {
    return caseId;
  }

  public void setCaseId(String caseId) {
    this.caseId = caseId;
  }


  /**
   * The dispute&#39;s category.
   * @return category
   */
  @javax.annotation.Nullable
  public CategoryEnum getCategory() {
    return category;
  }



  /**
   * Dispute created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public Dispute currency(String currency) {
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


  /**
   * The dispute&#39;s customer ID.
   * @return customerId
   */
  @javax.annotation.Nullable
  public String getCustomerId() {
    return customerId;
  }



  public Dispute deadlineTime(OffsetDateTime deadlineTime) {
    this.deadlineTime = deadlineTime;
    return this;
  }

  /**
   * Dispute deadline time.
   * @return deadlineTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDeadlineTime() {
    return deadlineTime;
  }

  public void setDeadlineTime(OffsetDateTime deadlineTime) {
    this.deadlineTime = deadlineTime;
  }


  /**
   * The dispute identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Dispute postedTime(OffsetDateTime postedTime) {
    this.postedTime = postedTime;
    return this;
  }

  /**
   * Dispute posted time.
   * @return postedTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getPostedTime() {
    return postedTime;
  }

  public void setPostedTime(OffsetDateTime postedTime) {
    this.postedTime = postedTime;
  }


  /**
   * Dispute raw response from gateway.
   * @return rawResponse
   */
  @javax.annotation.Nullable
  public String getRawResponse() {
    return rawResponse;
  }



  public Dispute reasonCode(ReasonCodeEnum reasonCode) {
    this.reasonCode = reasonCode;
    return this;
  }

  /**
   * The dispute&#39;s reason code.
   * @return reasonCode
   */
  @javax.annotation.Nonnull
  public ReasonCodeEnum getReasonCode() {
    return reasonCode;
  }

  public void setReasonCode(ReasonCodeEnum reasonCode) {
    this.reasonCode = reasonCode;
  }


  /**
   * Dispute resolved time.
   * @return resolvedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getResolvedTime() {
    return resolvedTime;
  }



  public Dispute status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * The dispute&#39;s status.
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public Dispute transactionId(String transactionId) {
    this.transactionId = transactionId;
    return this;
  }

  /**
   * The dispute&#39;s transaction ID.
   * @return transactionId
   */
  @javax.annotation.Nonnull
  public String getTransactionId() {
    return transactionId;
  }

  public void setTransactionId(String transactionId) {
    this.transactionId = transactionId;
  }


  public Dispute type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The dispute&#39;s type.
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  /**
   * Dispute updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Dispute dispute = (Dispute) o;
    return Objects.equals(this.embedded, dispute.embedded) &&
        Objects.equals(this.links, dispute.links) &&
        Objects.equals(this.acquirerReferenceNumber, dispute.acquirerReferenceNumber) &&
        Objects.equals(this.amount, dispute.amount) &&
        Objects.equals(this.caseId, dispute.caseId) &&
        Objects.equals(this.category, dispute.category) &&
        Objects.equals(this.createdTime, dispute.createdTime) &&
        Objects.equals(this.currency, dispute.currency) &&
        Objects.equals(this.customerId, dispute.customerId) &&
        Objects.equals(this.deadlineTime, dispute.deadlineTime) &&
        Objects.equals(this.id, dispute.id) &&
        Objects.equals(this.postedTime, dispute.postedTime) &&
        Objects.equals(this.rawResponse, dispute.rawResponse) &&
        Objects.equals(this.reasonCode, dispute.reasonCode) &&
        Objects.equals(this.resolvedTime, dispute.resolvedTime) &&
        Objects.equals(this.status, dispute.status) &&
        Objects.equals(this.transactionId, dispute.transactionId) &&
        Objects.equals(this.type, dispute.type) &&
        Objects.equals(this.updatedTime, dispute.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(embedded, links, acquirerReferenceNumber, amount, caseId, category, createdTime, currency, customerId, deadlineTime, id, postedTime, rawResponse, reasonCode, resolvedTime, status, transactionId, type, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Dispute {\n");
    sb.append("    embedded: ").append(toIndentedString(embedded)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    acquirerReferenceNumber: ").append(toIndentedString(acquirerReferenceNumber)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    caseId: ").append(toIndentedString(caseId)).append("\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    deadlineTime: ").append(toIndentedString(deadlineTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    postedTime: ").append(toIndentedString(postedTime)).append("\n");
    sb.append("    rawResponse: ").append(toIndentedString(rawResponse)).append("\n");
    sb.append("    reasonCode: ").append(toIndentedString(reasonCode)).append("\n");
    sb.append("    resolvedTime: ").append(toIndentedString(resolvedTime)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
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
    openapiFields.add("_embedded");
    openapiFields.add("_links");
    openapiFields.add("acquirerReferenceNumber");
    openapiFields.add("amount");
    openapiFields.add("caseId");
    openapiFields.add("category");
    openapiFields.add("createdTime");
    openapiFields.add("currency");
    openapiFields.add("customerId");
    openapiFields.add("deadlineTime");
    openapiFields.add("id");
    openapiFields.add("postedTime");
    openapiFields.add("rawResponse");
    openapiFields.add("reasonCode");
    openapiFields.add("resolvedTime");
    openapiFields.add("status");
    openapiFields.add("transactionId");
    openapiFields.add("type");
    openapiFields.add("updatedTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("amount");
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("postedTime");
    openapiRequiredFields.add("reasonCode");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("transactionId");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Dispute
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Dispute.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Dispute is not found in the empty JSON string", Dispute.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Dispute.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Dispute` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Dispute.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("_embedded") != null && !jsonObj.get("_embedded").isJsonNull()) {
        JsonArray jsonArrayembedded = jsonObj.getAsJsonArray("_embedded");
        if (jsonArrayembedded != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_embedded").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_embedded` to be an array in the JSON string but got `%s`", jsonObj.get("_embedded").toString()));
          }

          // validate the optional field `_embedded` (array)
          for (int i = 0; i < jsonArrayembedded.size(); i++) {
            DisputeEmbeddedInner.validateJsonElement(jsonArrayembedded.get(i));
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
            DisputeLinksInner.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if ((jsonObj.get("acquirerReferenceNumber") != null && !jsonObj.get("acquirerReferenceNumber").isJsonNull()) && !jsonObj.get("acquirerReferenceNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `acquirerReferenceNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("acquirerReferenceNumber").toString()));
      }
      if ((jsonObj.get("caseId") != null && !jsonObj.get("caseId").isJsonNull()) && !jsonObj.get("caseId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `caseId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("caseId").toString()));
      }
      if ((jsonObj.get("category") != null && !jsonObj.get("category").isJsonNull()) && !jsonObj.get("category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("category").toString()));
      }
      // validate the optional field `category`
      if (jsonObj.get("category") != null && !jsonObj.get("category").isJsonNull()) {
        CategoryEnum.validateJsonElement(jsonObj.get("category"));
      }
      if (!jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if ((jsonObj.get("customerId") != null && !jsonObj.get("customerId").isJsonNull()) && !jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("rawResponse") != null && !jsonObj.get("rawResponse").isJsonNull()) && !jsonObj.get("rawResponse").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rawResponse` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rawResponse").toString()));
      }
      if (!jsonObj.get("reasonCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reasonCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reasonCode").toString()));
      }
      // validate the required field `reasonCode`
      ReasonCodeEnum.validateJsonElement(jsonObj.get("reasonCode"));
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      if (!jsonObj.get("transactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactionId").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Dispute.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Dispute' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Dispute> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Dispute.class));

       return (TypeAdapter<T>) new TypeAdapter<Dispute>() {
           @Override
           public void write(JsonWriter out, Dispute value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Dispute read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Dispute given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Dispute
   * @throws IOException if the JSON string is invalid with respect to Dispute
   */
  public static Dispute fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Dispute.class);
  }

  /**
   * Convert an instance of Dispute to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

