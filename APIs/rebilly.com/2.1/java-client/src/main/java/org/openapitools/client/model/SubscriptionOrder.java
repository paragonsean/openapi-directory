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
import org.openapitools.client.model.CommonSubscriptionItemsInner;
import org.openapitools.client.model.CommonSubscriptionOrderAllOfLineItemSubtotal;
import org.openapitools.client.model.CommonSubscriptionOrderAllOfRecurringInterval;
import org.openapitools.client.model.CommonSubscriptionOrderAllOfTrial;
import org.openapitools.client.model.ContactObject;
import org.openapitools.client.model.InvoiceTimeShift;
import org.openapitools.client.model.RiskMetadata;
import org.openapitools.client.model.SubscriptionMetadataEmbeddedInner;
import org.openapitools.client.model.SubscriptionMetadataLinksInner;
import org.openapitools.client.model.UpcomingInvoiceItem;
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
 * SubscriptionOrder
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SubscriptionOrder {
  public static final String SERIALIZED_NAME_ACTIVATION_TIME = "activationTime";
  @SerializedName(SERIALIZED_NAME_ACTIVATION_TIME)
  private OffsetDateTime activationTime;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billingAddress";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private ContactObject billingAddress;

  /**
   * The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service. 
   */
  @JsonAdapter(BillingStatusEnum.Adapter.class)
  public enum BillingStatusEnum {
    UNPAID("unpaid"),
    
    PAST_DUE("past-due"),
    
    DELINQUENT("delinquent"),
    
    PAID("paid"),
    
    VOIDED("voided"),
    
    REFUNDED("refunded"),
    
    DISPUTED("disputed"),
    
    VOIDED2("voided");

    private String value;

    BillingStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BillingStatusEnum fromValue(String value) {
      for (BillingStatusEnum b : BillingStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BillingStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BillingStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BillingStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BillingStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BillingStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BILLING_STATUS = "billingStatus";
  @SerializedName(SERIALIZED_NAME_BILLING_STATUS)
  private BillingStatusEnum billingStatus;

  public static final String SERIALIZED_NAME_COUPON_IDS = "couponIds";
  @SerializedName(SERIALIZED_NAME_COUPON_IDS)
  private List<String> couponIds;

  public static final String SERIALIZED_NAME_DELIVERY_ADDRESS = "deliveryAddress";
  @SerializedName(SERIALIZED_NAME_DELIVERY_ADDRESS)
  private ContactObject deliveryAddress;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INITIAL_INVOICE_ID = "initialInvoiceId";
  @SerializedName(SERIALIZED_NAME_INITIAL_INVOICE_ID)
  private String initialInvoiceId;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<CommonSubscriptionItemsInner> items = new ArrayList<>();

  /**
   * Specifies the type of order, a subscription or a one-time purchase. 
   */
  @JsonAdapter(OrderTypeEnum.Adapter.class)
  public enum OrderTypeEnum {
    SUBSCRIPTION_ORDER("subscription-order"),
    
    ONE_TIME_ORDER("one-time-order");

    private String value;

    OrderTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OrderTypeEnum fromValue(String value) {
      for (OrderTypeEnum b : OrderTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OrderTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OrderTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OrderTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OrderTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OrderTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ORDER_TYPE = "orderType";
  @SerializedName(SERIALIZED_NAME_ORDER_TYPE)
  private OrderTypeEnum orderType = OrderTypeEnum.SUBSCRIPTION_ORDER;

  public static final String SERIALIZED_NAME_PO_NUMBER = "poNumber";
  @SerializedName(SERIALIZED_NAME_PO_NUMBER)
  private String poNumber;

  public static final String SERIALIZED_NAME_RECENT_INVOICE_ID = "recentInvoiceId";
  @SerializedName(SERIALIZED_NAME_RECENT_INVOICE_ID)
  private String recentInvoiceId;

  public static final String SERIALIZED_NAME_VOID_TIME = "voidTime";
  @SerializedName(SERIALIZED_NAME_VOID_TIME)
  private OffsetDateTime voidTime;

  public static final String SERIALIZED_NAME_WEBSITE_ID = "websiteId";
  @SerializedName(SERIALIZED_NAME_WEBSITE_ID)
  private String websiteId;

  public static final String SERIALIZED_NAME_AUTOPAY = "autopay";
  @SerializedName(SERIALIZED_NAME_AUTOPAY)
  private Boolean autopay = true;

  public static final String SERIALIZED_NAME_END_TIME = "endTime";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private OffsetDateTime endTime;

  public static final String SERIALIZED_NAME_IN_TRIAL = "inTrial";
  @SerializedName(SERIALIZED_NAME_IN_TRIAL)
  private Boolean inTrial;

  public static final String SERIALIZED_NAME_INVOICE_TIME_SHIFT = "invoiceTimeShift";
  @SerializedName(SERIALIZED_NAME_INVOICE_TIME_SHIFT)
  private InvoiceTimeShift invoiceTimeShift;

  public static final String SERIALIZED_NAME_IS_TRIAL_ONLY = "isTrialOnly";
  @SerializedName(SERIALIZED_NAME_IS_TRIAL_ONLY)
  private Boolean isTrialOnly = false;

  public static final String SERIALIZED_NAME_LINE_ITEM_SUBTOTAL = "lineItemSubtotal";
  @SerializedName(SERIALIZED_NAME_LINE_ITEM_SUBTOTAL)
  private CommonSubscriptionOrderAllOfLineItemSubtotal lineItemSubtotal;

  public static final String SERIALIZED_NAME_LINE_ITEMS = "lineItems";
  @SerializedName(SERIALIZED_NAME_LINE_ITEMS)
  private List<UpcomingInvoiceItem> lineItems;

  public static final String SERIALIZED_NAME_REBILL_NUMBER = "rebillNumber";
  @SerializedName(SERIALIZED_NAME_REBILL_NUMBER)
  private Integer rebillNumber;

  public static final String SERIALIZED_NAME_RECURRING_INTERVAL = "recurringInterval";
  @SerializedName(SERIALIZED_NAME_RECURRING_INTERVAL)
  private CommonSubscriptionOrderAllOfRecurringInterval recurringInterval;

  public static final String SERIALIZED_NAME_RENEWAL_TIME = "renewalTime";
  @SerializedName(SERIALIZED_NAME_RENEWAL_TIME)
  private OffsetDateTime renewalTime;

  public static final String SERIALIZED_NAME_START_TIME = "startTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private OffsetDateTime startTime;

  /**
   * The status of the subscription service. A subscription starts in the &#x60;pending&#x60; status, and will become &#x60;active&#x60; when the service period begins. 
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    PENDING("pending"),
    
    ACTIVE("active"),
    
    CANCELED("canceled"),
    
    CHURNED("churned"),
    
    SUSPENDED("suspended"),
    
    PAUSED("paused"),
    
    ABANDONED("abandoned"),
    
    TRIAL_ENDED("trial-ended");

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

  public static final String SERIALIZED_NAME_TRIAL = "trial";
  @SerializedName(SERIALIZED_NAME_TRIAL)
  private CommonSubscriptionOrderAllOfTrial trial;

  /**
   * Cancel category.
   */
  @JsonAdapter(CancelCategoryEnum.Adapter.class)
  public enum CancelCategoryEnum {
    BILLING_FAILURE("billing-failure"),
    
    DID_NOT_USE("did-not-use"),
    
    DID_NOT_WANT("did-not-want"),
    
    MISSING_FEATURES("missing-features"),
    
    BUGS_OR_PROBLEMS("bugs-or-problems"),
    
    DO_NOT_REMEMBER("do-not-remember"),
    
    RISK_WARNING("risk-warning"),
    
    CONTRACT_EXPIRED("contract-expired"),
    
    TOO_EXPENSIVE("too-expensive"),
    
    NEVER_STARTED("never-started"),
    
    SWITCHED_PLAN("switched-plan"),
    
    OTHER("other");

    private String value;

    CancelCategoryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CancelCategoryEnum fromValue(String value) {
      for (CancelCategoryEnum b : CancelCategoryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CancelCategoryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CancelCategoryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CancelCategoryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CancelCategoryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CancelCategoryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CANCEL_CATEGORY = "cancelCategory";
  @SerializedName(SERIALIZED_NAME_CANCEL_CATEGORY)
  private CancelCategoryEnum cancelCategory;

  public static final String SERIALIZED_NAME_CANCEL_DESCRIPTION = "cancelDescription";
  @SerializedName(SERIALIZED_NAME_CANCEL_DESCRIPTION)
  private String cancelDescription;

  /**
   * Canceled by.
   */
  @JsonAdapter(CanceledByEnum.Adapter.class)
  public enum CanceledByEnum {
    MERCHANT("merchant"),
    
    CUSTOMER("customer"),
    
    REBILLY("rebilly");

    private String value;

    CanceledByEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CanceledByEnum fromValue(String value) {
      for (CanceledByEnum b : CanceledByEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CanceledByEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CanceledByEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CanceledByEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CanceledByEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CanceledByEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CANCELED_BY = "canceledBy";
  @SerializedName(SERIALIZED_NAME_CANCELED_BY)
  private CanceledByEnum canceledBy;

  public static final String SERIALIZED_NAME_CANCELED_TIME = "canceledTime";
  @SerializedName(SERIALIZED_NAME_CANCELED_TIME)
  private OffsetDateTime canceledTime;

  public static final String SERIALIZED_NAME_EMBEDDED = "_embedded";
  @SerializedName(SERIALIZED_NAME_EMBEDDED)
  private List<SubscriptionMetadataEmbeddedInner> embedded = new ArrayList<>();

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SubscriptionMetadataLinksInner> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "customFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields = {};

  public static final String SERIALIZED_NAME_REVISION = "revision";
  @SerializedName(SERIALIZED_NAME_REVISION)
  private Integer revision;

  public static final String SERIALIZED_NAME_RISK_METADATA = "riskMetadata";
  @SerializedName(SERIALIZED_NAME_RISK_METADATA)
  private RiskMetadata riskMetadata;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_RENEWAL_REMINDER_NUMBER = "renewalReminderNumber";
  @SerializedName(SERIALIZED_NAME_RENEWAL_REMINDER_NUMBER)
  private Integer renewalReminderNumber;

  public static final String SERIALIZED_NAME_RENEWAL_REMINDER_TIME = "renewalReminderTime";
  @SerializedName(SERIALIZED_NAME_RENEWAL_REMINDER_TIME)
  private OffsetDateTime renewalReminderTime;

  public static final String SERIALIZED_NAME_TRIAL_REMINDER_NUMBER = "trialReminderNumber";
  @SerializedName(SERIALIZED_NAME_TRIAL_REMINDER_NUMBER)
  private Integer trialReminderNumber;

  public static final String SERIALIZED_NAME_TRIAL_REMINDER_TIME = "trialReminderTime";
  @SerializedName(SERIALIZED_NAME_TRIAL_REMINDER_TIME)
  private OffsetDateTime trialReminderTime;

  public SubscriptionOrder() {
  }

  public SubscriptionOrder(
     OffsetDateTime activationTime, 
     BillingStatusEnum billingStatus, 
     String id, 
     String initialInvoiceId, 
     String recentInvoiceId, 
     OffsetDateTime voidTime, 
     OffsetDateTime endTime, 
     Boolean inTrial, 
     List<UpcomingInvoiceItem> lineItems, 
     Integer rebillNumber, 
     StatusEnum status, 
     CancelCategoryEnum cancelCategory, 
     String cancelDescription, 
     CanceledByEnum canceledBy, 
     OffsetDateTime canceledTime, 
     List<SubscriptionMetadataEmbeddedInner> embedded, 
     List<SubscriptionMetadataLinksInner> links, 
     OffsetDateTime createdTime, 
     Integer revision, 
     OffsetDateTime updatedTime, 
     Integer renewalReminderNumber, 
     OffsetDateTime renewalReminderTime, 
     Integer trialReminderNumber, 
     OffsetDateTime trialReminderTime
  ) {
    this();
    this.activationTime = activationTime;
    this.billingStatus = billingStatus;
    this.id = id;
    this.initialInvoiceId = initialInvoiceId;
    this.recentInvoiceId = recentInvoiceId;
    this.voidTime = voidTime;
    this.endTime = endTime;
    this.inTrial = inTrial;
    this.lineItems = lineItems;
    this.rebillNumber = rebillNumber;
    this.status = status;
    this.cancelCategory = cancelCategory;
    this.cancelDescription = cancelDescription;
    this.canceledBy = canceledBy;
    this.canceledTime = canceledTime;
    this.embedded = embedded;
    this.links = links;
    this.createdTime = createdTime;
    this.revision = revision;
    this.updatedTime = updatedTime;
    this.renewalReminderNumber = renewalReminderNumber;
    this.renewalReminderTime = renewalReminderTime;
    this.trialReminderNumber = trialReminderNumber;
    this.trialReminderTime = trialReminderTime;
  }

  /**
   * Order activation time.
   * @return activationTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getActivationTime() {
    return activationTime;
  }



  public SubscriptionOrder billingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Order billing address.
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
   * The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service. 
   * @return billingStatus
   */
  @javax.annotation.Nullable
  public BillingStatusEnum getBillingStatus() {
    return billingStatus;
  }



  public SubscriptionOrder couponIds(List<String> couponIds) {
    this.couponIds = couponIds;
    return this;
  }

  public SubscriptionOrder addCouponIdsItem(String couponIdsItem) {
    if (this.couponIds == null) {
      this.couponIds = new ArrayList<>();
    }
    this.couponIds.add(couponIdsItem);
    return this;
  }

  /**
   * A list of coupons to redeem on the customer and restrict to this subscription. Read more about [coupons here](https://docs.rebilly.com/docs/dashboard/marketing/coupons-and-discounts/).  This parameter respects the following logic:  - When not passed then applied coupons will not be changed.  - When empty array passed then all applied coupon redemptions will be canceled.  - When list of coupons is passed then not applied yet coupons will be applied, already applied coupons will not change their state, applied coupons that are not presented in passed list will be canceled.  If list of applied coupons on pending order will be changed due to this param during update order,  Invoice for the order will be reissued. 
   * @return couponIds
   */
  @javax.annotation.Nullable
  public List<String> getCouponIds() {
    return couponIds;
  }

  public void setCouponIds(List<String> couponIds) {
    this.couponIds = couponIds;
  }


  public SubscriptionOrder deliveryAddress(ContactObject deliveryAddress) {
    this.deliveryAddress = deliveryAddress;
    return this;
  }

  /**
   * Order delivery address.
   * @return deliveryAddress
   */
  @javax.annotation.Nullable
  public ContactObject getDeliveryAddress() {
    return deliveryAddress;
  }

  public void setDeliveryAddress(ContactObject deliveryAddress) {
    this.deliveryAddress = deliveryAddress;
  }


  /**
   * The order identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * The initial invoice identifier string.
   * @return initialInvoiceId
   */
  @javax.annotation.Nullable
  public String getInitialInvoiceId() {
    return initialInvoiceId;
  }



  public SubscriptionOrder items(List<CommonSubscriptionItemsInner> items) {
    this.items = items;
    return this;
  }

  public SubscriptionOrder addItemsItem(CommonSubscriptionItemsInner itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Get items
   * @return items
   */
  @javax.annotation.Nonnull
  public List<CommonSubscriptionItemsInner> getItems() {
    return items;
  }

  public void setItems(List<CommonSubscriptionItemsInner> items) {
    this.items = items;
  }


  public SubscriptionOrder orderType(OrderTypeEnum orderType) {
    this.orderType = orderType;
    return this;
  }

  /**
   * Specifies the type of order, a subscription or a one-time purchase. 
   * @return orderType
   */
  @javax.annotation.Nonnull
  public OrderTypeEnum getOrderType() {
    return orderType;
  }

  public void setOrderType(OrderTypeEnum orderType) {
    this.orderType = orderType;
  }


  public SubscriptionOrder poNumber(String poNumber) {
    this.poNumber = poNumber;
    return this;
  }

  /**
   * Purchase order number, will be displayed on the issued invoices.
   * @return poNumber
   */
  @javax.annotation.Nullable
  public String getPoNumber() {
    return poNumber;
  }

  public void setPoNumber(String poNumber) {
    this.poNumber = poNumber;
  }


  /**
   * Most recently issued invoice identifier string. It might not be &#x60;paid&#x60; yet.
   * @return recentInvoiceId
   */
  @javax.annotation.Nullable
  public String getRecentInvoiceId() {
    return recentInvoiceId;
  }



  /**
   * Order void time.
   * @return voidTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getVoidTime() {
    return voidTime;
  }



  public SubscriptionOrder websiteId(String websiteId) {
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


  public SubscriptionOrder autopay(Boolean autopay) {
    this.autopay = autopay;
    return this;
  }

  /**
   * Autopay determines if a payment attempt will be automatic.
   * @return autopay
   */
  @javax.annotation.Nullable
  public Boolean getAutopay() {
    return autopay;
  }

  public void setAutopay(Boolean autopay) {
    this.autopay = autopay;
  }


  /**
   * Subscription end time.
   * @return endTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndTime() {
    return endTime;
  }



  /**
   * True if the subscription is currently in a trial period.
   * @return inTrial
   */
  @javax.annotation.Nullable
  public Boolean getInTrial() {
    return inTrial;
  }



  public SubscriptionOrder invoiceTimeShift(InvoiceTimeShift invoiceTimeShift) {
    this.invoiceTimeShift = invoiceTimeShift;
    return this;
  }

  /**
   * You can shift issue time and due time of invoices for this subscription. This setting overrides plan settings. To use plan settings, set &#x60;null&#x60;. To use multiple plans in one subscription they all must have the same billing period, this property allows to subscribe to different plans. 
   * @return invoiceTimeShift
   */
  @javax.annotation.Nullable
  public InvoiceTimeShift getInvoiceTimeShift() {
    return invoiceTimeShift;
  }

  public void setInvoiceTimeShift(InvoiceTimeShift invoiceTimeShift) {
    this.invoiceTimeShift = invoiceTimeShift;
  }


  public SubscriptionOrder isTrialOnly(Boolean isTrialOnly) {
    this.isTrialOnly = isTrialOnly;
    return this;
  }

  /**
   * Whether a subscription ends after a trial period. Recurring settings are ignored if it&#39;s &#x60;true&#x60;.
   * @return isTrialOnly
   */
  @javax.annotation.Nullable
  public Boolean getIsTrialOnly() {
    return isTrialOnly;
  }

  public void setIsTrialOnly(Boolean isTrialOnly) {
    this.isTrialOnly = isTrialOnly;
  }


  public SubscriptionOrder lineItemSubtotal(CommonSubscriptionOrderAllOfLineItemSubtotal lineItemSubtotal) {
    this.lineItemSubtotal = lineItemSubtotal;
    return this;
  }

  /**
   * Get lineItemSubtotal
   * @return lineItemSubtotal
   */
  @javax.annotation.Nullable
  public CommonSubscriptionOrderAllOfLineItemSubtotal getLineItemSubtotal() {
    return lineItemSubtotal;
  }

  public void setLineItemSubtotal(CommonSubscriptionOrderAllOfLineItemSubtotal lineItemSubtotal) {
    this.lineItemSubtotal = lineItemSubtotal;
  }


  /**
   * Subscription line items which queue until the next renewal (or interim) invoice is issued for the subscription.
   * @return lineItems
   */
  @javax.annotation.Nullable
  public List<UpcomingInvoiceItem> getLineItems() {
    return lineItems;
  }



  /**
   * The current period number.
   * @return rebillNumber
   */
  @javax.annotation.Nullable
  public Integer getRebillNumber() {
    return rebillNumber;
  }



  public SubscriptionOrder recurringInterval(CommonSubscriptionOrderAllOfRecurringInterval recurringInterval) {
    this.recurringInterval = recurringInterval;
    return this;
  }

  /**
   * Get recurringInterval
   * @return recurringInterval
   */
  @javax.annotation.Nullable
  public CommonSubscriptionOrderAllOfRecurringInterval getRecurringInterval() {
    return recurringInterval;
  }

  public void setRecurringInterval(CommonSubscriptionOrderAllOfRecurringInterval recurringInterval) {
    this.recurringInterval = recurringInterval;
  }


  public SubscriptionOrder renewalTime(OffsetDateTime renewalTime) {
    this.renewalTime = renewalTime;
    return this;
  }

  /**
   * Subscription renewal time.
   * @return renewalTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getRenewalTime() {
    return renewalTime;
  }

  public void setRenewalTime(OffsetDateTime renewalTime) {
    this.renewalTime = renewalTime;
  }


  public SubscriptionOrder startTime(OffsetDateTime startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Subscription start time.  When the value is sent as null, it will use the current time. This value can&#39;t be in past more than one service period.
   * @return startTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartTime() {
    return startTime;
  }

  public void setStartTime(OffsetDateTime startTime) {
    this.startTime = startTime;
  }


  /**
   * The status of the subscription service. A subscription starts in the &#x60;pending&#x60; status, and will become &#x60;active&#x60; when the service period begins. 
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  public SubscriptionOrder trial(CommonSubscriptionOrderAllOfTrial trial) {
    this.trial = trial;
    return this;
  }

  /**
   * Get trial
   * @return trial
   */
  @javax.annotation.Nullable
  public CommonSubscriptionOrderAllOfTrial getTrial() {
    return trial;
  }

  public void setTrial(CommonSubscriptionOrderAllOfTrial trial) {
    this.trial = trial;
  }


  /**
   * Cancel category.
   * @return cancelCategory
   */
  @javax.annotation.Nullable
  public CancelCategoryEnum getCancelCategory() {
    return cancelCategory;
  }



  /**
   * Cancel reason description in free form.
   * @return cancelDescription
   */
  @javax.annotation.Nullable
  public String getCancelDescription() {
    return cancelDescription;
  }



  /**
   * Canceled by.
   * @return canceledBy
   */
  @javax.annotation.Nullable
  public CanceledByEnum getCanceledBy() {
    return canceledBy;
  }



  /**
   * Subscription order canceled time.
   * @return canceledTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCanceledTime() {
    return canceledTime;
  }



  /**
   * Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter.
   * @return embedded
   */
  @javax.annotation.Nullable
  public List<SubscriptionMetadataEmbeddedInner> getEmbedded() {
    return embedded;
  }



  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<SubscriptionMetadataLinksInner> getLinks() {
    return links;
  }



  /**
   * Order created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public SubscriptionOrder customFields(Object customFields) {
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


  /**
   * The number of times the order data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
   * @return revision
   */
  @javax.annotation.Nullable
  public Integer getRevision() {
    return revision;
  }



  public SubscriptionOrder riskMetadata(RiskMetadata riskMetadata) {
    this.riskMetadata = riskMetadata;
    return this;
  }

  /**
   * Risk metadata. If null, the value would coalesce to the risk metadata captured when creating the payment token.
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
   * Order updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  public SubscriptionOrder customerId(String customerId) {
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


  /**
   * Number of renewal reminder events triggered.
   * @return renewalReminderNumber
   */
  @javax.annotation.Nullable
  public Integer getRenewalReminderNumber() {
    return renewalReminderNumber;
  }



  /**
   * Time renewal reminder event will be triggered.
   * @return renewalReminderTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getRenewalReminderTime() {
    return renewalReminderTime;
  }



  /**
   * Number of renewal reminder events triggered.
   * @return trialReminderNumber
   */
  @javax.annotation.Nullable
  public Integer getTrialReminderNumber() {
    return trialReminderNumber;
  }



  /**
   * Time renewal reminder event will be triggered.
   * @return trialReminderTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTrialReminderTime() {
    return trialReminderTime;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SubscriptionOrder subscriptionOrder = (SubscriptionOrder) o;
    return Objects.equals(this.activationTime, subscriptionOrder.activationTime) &&
        Objects.equals(this.billingAddress, subscriptionOrder.billingAddress) &&
        Objects.equals(this.billingStatus, subscriptionOrder.billingStatus) &&
        Objects.equals(this.couponIds, subscriptionOrder.couponIds) &&
        Objects.equals(this.deliveryAddress, subscriptionOrder.deliveryAddress) &&
        Objects.equals(this.id, subscriptionOrder.id) &&
        Objects.equals(this.initialInvoiceId, subscriptionOrder.initialInvoiceId) &&
        Objects.equals(this.items, subscriptionOrder.items) &&
        Objects.equals(this.orderType, subscriptionOrder.orderType) &&
        Objects.equals(this.poNumber, subscriptionOrder.poNumber) &&
        Objects.equals(this.recentInvoiceId, subscriptionOrder.recentInvoiceId) &&
        Objects.equals(this.voidTime, subscriptionOrder.voidTime) &&
        Objects.equals(this.websiteId, subscriptionOrder.websiteId) &&
        Objects.equals(this.autopay, subscriptionOrder.autopay) &&
        Objects.equals(this.endTime, subscriptionOrder.endTime) &&
        Objects.equals(this.inTrial, subscriptionOrder.inTrial) &&
        Objects.equals(this.invoiceTimeShift, subscriptionOrder.invoiceTimeShift) &&
        Objects.equals(this.isTrialOnly, subscriptionOrder.isTrialOnly) &&
        Objects.equals(this.lineItemSubtotal, subscriptionOrder.lineItemSubtotal) &&
        Objects.equals(this.lineItems, subscriptionOrder.lineItems) &&
        Objects.equals(this.rebillNumber, subscriptionOrder.rebillNumber) &&
        Objects.equals(this.recurringInterval, subscriptionOrder.recurringInterval) &&
        Objects.equals(this.renewalTime, subscriptionOrder.renewalTime) &&
        Objects.equals(this.startTime, subscriptionOrder.startTime) &&
        Objects.equals(this.status, subscriptionOrder.status) &&
        Objects.equals(this.trial, subscriptionOrder.trial) &&
        Objects.equals(this.cancelCategory, subscriptionOrder.cancelCategory) &&
        Objects.equals(this.cancelDescription, subscriptionOrder.cancelDescription) &&
        Objects.equals(this.canceledBy, subscriptionOrder.canceledBy) &&
        Objects.equals(this.canceledTime, subscriptionOrder.canceledTime) &&
        Objects.equals(this.embedded, subscriptionOrder.embedded) &&
        Objects.equals(this.links, subscriptionOrder.links) &&
        Objects.equals(this.createdTime, subscriptionOrder.createdTime) &&
        Objects.equals(this.customFields, subscriptionOrder.customFields) &&
        Objects.equals(this.revision, subscriptionOrder.revision) &&
        Objects.equals(this.riskMetadata, subscriptionOrder.riskMetadata) &&
        Objects.equals(this.updatedTime, subscriptionOrder.updatedTime) &&
        Objects.equals(this.customerId, subscriptionOrder.customerId) &&
        Objects.equals(this.renewalReminderNumber, subscriptionOrder.renewalReminderNumber) &&
        Objects.equals(this.renewalReminderTime, subscriptionOrder.renewalReminderTime) &&
        Objects.equals(this.trialReminderNumber, subscriptionOrder.trialReminderNumber) &&
        Objects.equals(this.trialReminderTime, subscriptionOrder.trialReminderTime);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(activationTime, billingAddress, billingStatus, couponIds, deliveryAddress, id, initialInvoiceId, items, orderType, poNumber, recentInvoiceId, voidTime, websiteId, autopay, endTime, inTrial, invoiceTimeShift, isTrialOnly, lineItemSubtotal, lineItems, rebillNumber, recurringInterval, renewalTime, startTime, status, trial, cancelCategory, cancelDescription, canceledBy, canceledTime, embedded, links, createdTime, customFields, revision, riskMetadata, updatedTime, customerId, renewalReminderNumber, renewalReminderTime, trialReminderNumber, trialReminderTime);
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
    sb.append("class SubscriptionOrder {\n");
    sb.append("    activationTime: ").append(toIndentedString(activationTime)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    billingStatus: ").append(toIndentedString(billingStatus)).append("\n");
    sb.append("    couponIds: ").append(toIndentedString(couponIds)).append("\n");
    sb.append("    deliveryAddress: ").append(toIndentedString(deliveryAddress)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    initialInvoiceId: ").append(toIndentedString(initialInvoiceId)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    orderType: ").append(toIndentedString(orderType)).append("\n");
    sb.append("    poNumber: ").append(toIndentedString(poNumber)).append("\n");
    sb.append("    recentInvoiceId: ").append(toIndentedString(recentInvoiceId)).append("\n");
    sb.append("    voidTime: ").append(toIndentedString(voidTime)).append("\n");
    sb.append("    websiteId: ").append(toIndentedString(websiteId)).append("\n");
    sb.append("    autopay: ").append(toIndentedString(autopay)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    inTrial: ").append(toIndentedString(inTrial)).append("\n");
    sb.append("    invoiceTimeShift: ").append(toIndentedString(invoiceTimeShift)).append("\n");
    sb.append("    isTrialOnly: ").append(toIndentedString(isTrialOnly)).append("\n");
    sb.append("    lineItemSubtotal: ").append(toIndentedString(lineItemSubtotal)).append("\n");
    sb.append("    lineItems: ").append(toIndentedString(lineItems)).append("\n");
    sb.append("    rebillNumber: ").append(toIndentedString(rebillNumber)).append("\n");
    sb.append("    recurringInterval: ").append(toIndentedString(recurringInterval)).append("\n");
    sb.append("    renewalTime: ").append(toIndentedString(renewalTime)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    trial: ").append(toIndentedString(trial)).append("\n");
    sb.append("    cancelCategory: ").append(toIndentedString(cancelCategory)).append("\n");
    sb.append("    cancelDescription: ").append(toIndentedString(cancelDescription)).append("\n");
    sb.append("    canceledBy: ").append(toIndentedString(canceledBy)).append("\n");
    sb.append("    canceledTime: ").append(toIndentedString(canceledTime)).append("\n");
    sb.append("    embedded: ").append(toIndentedString(embedded)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    revision: ").append(toIndentedString(revision)).append("\n");
    sb.append("    riskMetadata: ").append(toIndentedString(riskMetadata)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    renewalReminderNumber: ").append(toIndentedString(renewalReminderNumber)).append("\n");
    sb.append("    renewalReminderTime: ").append(toIndentedString(renewalReminderTime)).append("\n");
    sb.append("    trialReminderNumber: ").append(toIndentedString(trialReminderNumber)).append("\n");
    sb.append("    trialReminderTime: ").append(toIndentedString(trialReminderTime)).append("\n");
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
    openapiFields.add("activationTime");
    openapiFields.add("billingAddress");
    openapiFields.add("billingStatus");
    openapiFields.add("couponIds");
    openapiFields.add("deliveryAddress");
    openapiFields.add("id");
    openapiFields.add("initialInvoiceId");
    openapiFields.add("items");
    openapiFields.add("orderType");
    openapiFields.add("poNumber");
    openapiFields.add("recentInvoiceId");
    openapiFields.add("voidTime");
    openapiFields.add("websiteId");
    openapiFields.add("autopay");
    openapiFields.add("endTime");
    openapiFields.add("inTrial");
    openapiFields.add("invoiceTimeShift");
    openapiFields.add("isTrialOnly");
    openapiFields.add("lineItemSubtotal");
    openapiFields.add("lineItems");
    openapiFields.add("rebillNumber");
    openapiFields.add("recurringInterval");
    openapiFields.add("renewalTime");
    openapiFields.add("startTime");
    openapiFields.add("status");
    openapiFields.add("trial");
    openapiFields.add("cancelCategory");
    openapiFields.add("cancelDescription");
    openapiFields.add("canceledBy");
    openapiFields.add("canceledTime");
    openapiFields.add("_embedded");
    openapiFields.add("_links");
    openapiFields.add("createdTime");
    openapiFields.add("customFields");
    openapiFields.add("revision");
    openapiFields.add("riskMetadata");
    openapiFields.add("updatedTime");
    openapiFields.add("customerId");
    openapiFields.add("renewalReminderNumber");
    openapiFields.add("renewalReminderTime");
    openapiFields.add("trialReminderNumber");
    openapiFields.add("trialReminderTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("items");
    openapiRequiredFields.add("orderType");
    openapiRequiredFields.add("websiteId");
    openapiRequiredFields.add("customerId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SubscriptionOrder
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SubscriptionOrder.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SubscriptionOrder is not found in the empty JSON string", SubscriptionOrder.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SubscriptionOrder.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SubscriptionOrder` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SubscriptionOrder.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `billingAddress`
      if (jsonObj.get("billingAddress") != null && !jsonObj.get("billingAddress").isJsonNull()) {
        ContactObject.validateJsonElement(jsonObj.get("billingAddress"));
      }
      if ((jsonObj.get("billingStatus") != null && !jsonObj.get("billingStatus").isJsonNull()) && !jsonObj.get("billingStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billingStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billingStatus").toString()));
      }
      // validate the optional field `billingStatus`
      if (jsonObj.get("billingStatus") != null && !jsonObj.get("billingStatus").isJsonNull()) {
        BillingStatusEnum.validateJsonElement(jsonObj.get("billingStatus"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("couponIds") != null && !jsonObj.get("couponIds").isJsonNull() && !jsonObj.get("couponIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `couponIds` to be an array in the JSON string but got `%s`", jsonObj.get("couponIds").toString()));
      }
      // validate the optional field `deliveryAddress`
      if (jsonObj.get("deliveryAddress") != null && !jsonObj.get("deliveryAddress").isJsonNull()) {
        ContactObject.validateJsonElement(jsonObj.get("deliveryAddress"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("initialInvoiceId") != null && !jsonObj.get("initialInvoiceId").isJsonNull()) && !jsonObj.get("initialInvoiceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `initialInvoiceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("initialInvoiceId").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("items").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
      }

      JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
      // validate the required field `items` (array)
      for (int i = 0; i < jsonArrayitems.size(); i++) {
        CommonSubscriptionItemsInner.validateJsonElement(jsonArrayitems.get(i));
      };
      if (!jsonObj.get("orderType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderType").toString()));
      }
      // validate the required field `orderType`
      OrderTypeEnum.validateJsonElement(jsonObj.get("orderType"));
      if ((jsonObj.get("poNumber") != null && !jsonObj.get("poNumber").isJsonNull()) && !jsonObj.get("poNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `poNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("poNumber").toString()));
      }
      if ((jsonObj.get("recentInvoiceId") != null && !jsonObj.get("recentInvoiceId").isJsonNull()) && !jsonObj.get("recentInvoiceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `recentInvoiceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("recentInvoiceId").toString()));
      }
      if (!jsonObj.get("websiteId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `websiteId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("websiteId").toString()));
      }
      // validate the optional field `invoiceTimeShift`
      if (jsonObj.get("invoiceTimeShift") != null && !jsonObj.get("invoiceTimeShift").isJsonNull()) {
        InvoiceTimeShift.validateJsonElement(jsonObj.get("invoiceTimeShift"));
      }
      // validate the optional field `lineItemSubtotal`
      if (jsonObj.get("lineItemSubtotal") != null && !jsonObj.get("lineItemSubtotal").isJsonNull()) {
        CommonSubscriptionOrderAllOfLineItemSubtotal.validateJsonElement(jsonObj.get("lineItemSubtotal"));
      }
      if (jsonObj.get("lineItems") != null && !jsonObj.get("lineItems").isJsonNull()) {
        JsonArray jsonArraylineItems = jsonObj.getAsJsonArray("lineItems");
        if (jsonArraylineItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("lineItems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `lineItems` to be an array in the JSON string but got `%s`", jsonObj.get("lineItems").toString()));
          }

          // validate the optional field `lineItems` (array)
          for (int i = 0; i < jsonArraylineItems.size(); i++) {
            UpcomingInvoiceItem.validateJsonElement(jsonArraylineItems.get(i));
          };
        }
      }
      // validate the optional field `recurringInterval`
      if (jsonObj.get("recurringInterval") != null && !jsonObj.get("recurringInterval").isJsonNull()) {
        CommonSubscriptionOrderAllOfRecurringInterval.validateJsonElement(jsonObj.get("recurringInterval"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      // validate the optional field `trial`
      if (jsonObj.get("trial") != null && !jsonObj.get("trial").isJsonNull()) {
        CommonSubscriptionOrderAllOfTrial.validateJsonElement(jsonObj.get("trial"));
      }
      if ((jsonObj.get("cancelCategory") != null && !jsonObj.get("cancelCategory").isJsonNull()) && !jsonObj.get("cancelCategory").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cancelCategory` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cancelCategory").toString()));
      }
      // validate the optional field `cancelCategory`
      if (jsonObj.get("cancelCategory") != null && !jsonObj.get("cancelCategory").isJsonNull()) {
        CancelCategoryEnum.validateJsonElement(jsonObj.get("cancelCategory"));
      }
      if ((jsonObj.get("cancelDescription") != null && !jsonObj.get("cancelDescription").isJsonNull()) && !jsonObj.get("cancelDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cancelDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cancelDescription").toString()));
      }
      if ((jsonObj.get("canceledBy") != null && !jsonObj.get("canceledBy").isJsonNull()) && !jsonObj.get("canceledBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `canceledBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("canceledBy").toString()));
      }
      // validate the optional field `canceledBy`
      if (jsonObj.get("canceledBy") != null && !jsonObj.get("canceledBy").isJsonNull()) {
        CanceledByEnum.validateJsonElement(jsonObj.get("canceledBy"));
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
            SubscriptionMetadataEmbeddedInner.validateJsonElement(jsonArrayembedded.get(i));
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
            SubscriptionMetadataLinksInner.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      // validate the optional field `riskMetadata`
      if (jsonObj.get("riskMetadata") != null && !jsonObj.get("riskMetadata").isJsonNull()) {
        RiskMetadata.validateJsonElement(jsonObj.get("riskMetadata"));
      }
      if (!jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SubscriptionOrder.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SubscriptionOrder' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SubscriptionOrder> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SubscriptionOrder.class));

       return (TypeAdapter<T>) new TypeAdapter<SubscriptionOrder>() {
           @Override
           public void write(JsonWriter out, SubscriptionOrder value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SubscriptionOrder read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SubscriptionOrder given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SubscriptionOrder
   * @throws IOException if the JSON string is invalid with respect to SubscriptionOrder
   */
  public static SubscriptionOrder fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SubscriptionOrder.class);
  }

  /**
   * Convert an instance of SubscriptionOrder to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

