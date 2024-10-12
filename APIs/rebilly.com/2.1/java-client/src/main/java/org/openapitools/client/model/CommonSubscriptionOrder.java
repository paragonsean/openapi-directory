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
 * CommonSubscriptionOrder
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CommonSubscriptionOrder {
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

  public CommonSubscriptionOrder() {
  }

  public CommonSubscriptionOrder(
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
     StatusEnum status
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
  }

  /**
   * Order activation time.
   * @return activationTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getActivationTime() {
    return activationTime;
  }



  public CommonSubscriptionOrder billingAddress(ContactObject billingAddress) {
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



  public CommonSubscriptionOrder couponIds(List<String> couponIds) {
    this.couponIds = couponIds;
    return this;
  }

  public CommonSubscriptionOrder addCouponIdsItem(String couponIdsItem) {
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


  public CommonSubscriptionOrder deliveryAddress(ContactObject deliveryAddress) {
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



  public CommonSubscriptionOrder items(List<CommonSubscriptionItemsInner> items) {
    this.items = items;
    return this;
  }

  public CommonSubscriptionOrder addItemsItem(CommonSubscriptionItemsInner itemsItem) {
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
  @javax.annotation.Nullable
  public List<CommonSubscriptionItemsInner> getItems() {
    return items;
  }

  public void setItems(List<CommonSubscriptionItemsInner> items) {
    this.items = items;
  }


  public CommonSubscriptionOrder orderType(OrderTypeEnum orderType) {
    this.orderType = orderType;
    return this;
  }

  /**
   * Specifies the type of order, a subscription or a one-time purchase. 
   * @return orderType
   */
  @javax.annotation.Nullable
  public OrderTypeEnum getOrderType() {
    return orderType;
  }

  public void setOrderType(OrderTypeEnum orderType) {
    this.orderType = orderType;
  }


  public CommonSubscriptionOrder poNumber(String poNumber) {
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



  public CommonSubscriptionOrder websiteId(String websiteId) {
    this.websiteId = websiteId;
    return this;
  }

  /**
   * The website identifier string.
   * @return websiteId
   */
  @javax.annotation.Nullable
  public String getWebsiteId() {
    return websiteId;
  }

  public void setWebsiteId(String websiteId) {
    this.websiteId = websiteId;
  }


  public CommonSubscriptionOrder autopay(Boolean autopay) {
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



  public CommonSubscriptionOrder invoiceTimeShift(InvoiceTimeShift invoiceTimeShift) {
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


  public CommonSubscriptionOrder isTrialOnly(Boolean isTrialOnly) {
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


  public CommonSubscriptionOrder lineItemSubtotal(CommonSubscriptionOrderAllOfLineItemSubtotal lineItemSubtotal) {
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



  public CommonSubscriptionOrder recurringInterval(CommonSubscriptionOrderAllOfRecurringInterval recurringInterval) {
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


  public CommonSubscriptionOrder renewalTime(OffsetDateTime renewalTime) {
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


  public CommonSubscriptionOrder startTime(OffsetDateTime startTime) {
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



  public CommonSubscriptionOrder trial(CommonSubscriptionOrderAllOfTrial trial) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CommonSubscriptionOrder commonSubscriptionOrder = (CommonSubscriptionOrder) o;
    return Objects.equals(this.activationTime, commonSubscriptionOrder.activationTime) &&
        Objects.equals(this.billingAddress, commonSubscriptionOrder.billingAddress) &&
        Objects.equals(this.billingStatus, commonSubscriptionOrder.billingStatus) &&
        Objects.equals(this.couponIds, commonSubscriptionOrder.couponIds) &&
        Objects.equals(this.deliveryAddress, commonSubscriptionOrder.deliveryAddress) &&
        Objects.equals(this.id, commonSubscriptionOrder.id) &&
        Objects.equals(this.initialInvoiceId, commonSubscriptionOrder.initialInvoiceId) &&
        Objects.equals(this.items, commonSubscriptionOrder.items) &&
        Objects.equals(this.orderType, commonSubscriptionOrder.orderType) &&
        Objects.equals(this.poNumber, commonSubscriptionOrder.poNumber) &&
        Objects.equals(this.recentInvoiceId, commonSubscriptionOrder.recentInvoiceId) &&
        Objects.equals(this.voidTime, commonSubscriptionOrder.voidTime) &&
        Objects.equals(this.websiteId, commonSubscriptionOrder.websiteId) &&
        Objects.equals(this.autopay, commonSubscriptionOrder.autopay) &&
        Objects.equals(this.endTime, commonSubscriptionOrder.endTime) &&
        Objects.equals(this.inTrial, commonSubscriptionOrder.inTrial) &&
        Objects.equals(this.invoiceTimeShift, commonSubscriptionOrder.invoiceTimeShift) &&
        Objects.equals(this.isTrialOnly, commonSubscriptionOrder.isTrialOnly) &&
        Objects.equals(this.lineItemSubtotal, commonSubscriptionOrder.lineItemSubtotal) &&
        Objects.equals(this.lineItems, commonSubscriptionOrder.lineItems) &&
        Objects.equals(this.rebillNumber, commonSubscriptionOrder.rebillNumber) &&
        Objects.equals(this.recurringInterval, commonSubscriptionOrder.recurringInterval) &&
        Objects.equals(this.renewalTime, commonSubscriptionOrder.renewalTime) &&
        Objects.equals(this.startTime, commonSubscriptionOrder.startTime) &&
        Objects.equals(this.status, commonSubscriptionOrder.status) &&
        Objects.equals(this.trial, commonSubscriptionOrder.trial);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(activationTime, billingAddress, billingStatus, couponIds, deliveryAddress, id, initialInvoiceId, items, orderType, poNumber, recentInvoiceId, voidTime, websiteId, autopay, endTime, inTrial, invoiceTimeShift, isTrialOnly, lineItemSubtotal, lineItems, rebillNumber, recurringInterval, renewalTime, startTime, status, trial);
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
    sb.append("class CommonSubscriptionOrder {\n");
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

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CommonSubscriptionOrder
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CommonSubscriptionOrder.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CommonSubscriptionOrder is not found in the empty JSON string", CommonSubscriptionOrder.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CommonSubscriptionOrder.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CommonSubscriptionOrder` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            CommonSubscriptionItemsInner.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if ((jsonObj.get("orderType") != null && !jsonObj.get("orderType").isJsonNull()) && !jsonObj.get("orderType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orderType").toString()));
      }
      // validate the optional field `orderType`
      if (jsonObj.get("orderType") != null && !jsonObj.get("orderType").isJsonNull()) {
        OrderTypeEnum.validateJsonElement(jsonObj.get("orderType"));
      }
      if ((jsonObj.get("poNumber") != null && !jsonObj.get("poNumber").isJsonNull()) && !jsonObj.get("poNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `poNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("poNumber").toString()));
      }
      if ((jsonObj.get("recentInvoiceId") != null && !jsonObj.get("recentInvoiceId").isJsonNull()) && !jsonObj.get("recentInvoiceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `recentInvoiceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("recentInvoiceId").toString()));
      }
      if ((jsonObj.get("websiteId") != null && !jsonObj.get("websiteId").isJsonNull()) && !jsonObj.get("websiteId").isJsonPrimitive()) {
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
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CommonSubscriptionOrder.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CommonSubscriptionOrder' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CommonSubscriptionOrder> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CommonSubscriptionOrder.class));

       return (TypeAdapter<T>) new TypeAdapter<CommonSubscriptionOrder>() {
           @Override
           public void write(JsonWriter out, CommonSubscriptionOrder value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CommonSubscriptionOrder read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CommonSubscriptionOrder given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CommonSubscriptionOrder
   * @throws IOException if the JSON string is invalid with respect to CommonSubscriptionOrder
   */
  public static CommonSubscriptionOrder fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CommonSubscriptionOrder.class);
  }

  /**
   * Convert an instance of CommonSubscriptionOrder to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

