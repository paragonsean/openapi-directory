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
import org.openapitools.client.model.ContactObject;
import org.openapitools.client.model.InvoiceAllOfEmbedded;
import org.openapitools.client.model.InvoiceAllOfLinks;
import org.openapitools.client.model.InvoiceAllOfRetryInstruction;
import org.openapitools.client.model.InvoiceDiscount;
import org.openapitools.client.model.InvoiceItem;
import org.openapitools.client.model.InvoiceShipping;
import org.openapitools.client.model.InvoiceTax;
import org.openapitools.client.model.Transaction;
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
 * Invoice
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Invoice {
  public static final String SERIALIZED_NAME_ABANDONED_TIME = "abandonedTime";
  @SerializedName(SERIALIZED_NAME_ABANDONED_TIME)
  private OffsetDateTime abandonedTime;

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_AMOUNT_DUE = "amountDue";
  @SerializedName(SERIALIZED_NAME_AMOUNT_DUE)
  private Double amountDue;

  public static final String SERIALIZED_NAME_AUTOPAY_RETRY_NUMBER = "autopayRetryNumber";
  @SerializedName(SERIALIZED_NAME_AUTOPAY_RETRY_NUMBER)
  private Integer autopayRetryNumber = 0;

  public static final String SERIALIZED_NAME_AUTOPAY_SCHEDULED_TIME = "autopayScheduledTime";
  @SerializedName(SERIALIZED_NAME_AUTOPAY_SCHEDULED_TIME)
  private OffsetDateTime autopayScheduledTime;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billingAddress";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private ContactObject billingAddress;

  public static final String SERIALIZED_NAME_COLLECTION_PERIOD = "collectionPeriod";
  @SerializedName(SERIALIZED_NAME_COLLECTION_PERIOD)
  private Integer collectionPeriod;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_DELINQUENT_COLLECTION_PERIOD = "delinquentCollectionPeriod";
  @SerializedName(SERIALIZED_NAME_DELINQUENT_COLLECTION_PERIOD)
  private Integer delinquentCollectionPeriod;

  public static final String SERIALIZED_NAME_DELIVERY_ADDRESS = "deliveryAddress";
  @SerializedName(SERIALIZED_NAME_DELIVERY_ADDRESS)
  private ContactObject deliveryAddress;

  public static final String SERIALIZED_NAME_DISCOUNT_AMOUNT = "discountAmount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_AMOUNT)
  private Double discountAmount;

  public static final String SERIALIZED_NAME_DISCOUNTS = "discounts";
  @SerializedName(SERIALIZED_NAME_DISCOUNTS)
  private List<InvoiceDiscount> discounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_DUE_TIME = "dueTime";
  @SerializedName(SERIALIZED_NAME_DUE_TIME)
  private OffsetDateTime dueTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INVOICE_NUMBER = "invoiceNumber";
  @SerializedName(SERIALIZED_NAME_INVOICE_NUMBER)
  private Integer invoiceNumber;

  public static final String SERIALIZED_NAME_ISSUED_TIME = "issuedTime";
  @SerializedName(SERIALIZED_NAME_ISSUED_TIME)
  private OffsetDateTime issuedTime;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<InvoiceItem> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PAID_TIME = "paidTime";
  @SerializedName(SERIALIZED_NAME_PAID_TIME)
  private OffsetDateTime paidTime;

  public static final String SERIALIZED_NAME_PAYMENT_FORM_URL = "paymentFormUrl";
  @SerializedName(SERIALIZED_NAME_PAYMENT_FORM_URL)
  private String paymentFormUrl;

  public static final String SERIALIZED_NAME_PO_NUMBER = "poNumber";
  @SerializedName(SERIALIZED_NAME_PO_NUMBER)
  private String poNumber;

  public static final String SERIALIZED_NAME_SHIPPING = "shipping";
  @SerializedName(SERIALIZED_NAME_SHIPPING)
  private InvoiceShipping shipping;

  /**
   * Invoice status.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    DRAFT("draft"),
    
    UNPAID("unpaid"),
    
    PAID("paid"),
    
    PAST_DUE("past-due"),
    
    DELINQUENT("delinquent"),
    
    ABANDONED("abandoned"),
    
    VOIDED("voided"),
    
    PARTIALLY_REFUNDED("partially-refunded"),
    
    REFUNDED("refunded"),
    
    DISPUTED("disputed");

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

  public static final String SERIALIZED_NAME_SUBSCRIPTION_ID = "subscriptionId";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTION_ID)
  private String subscriptionId;

  public static final String SERIALIZED_NAME_SUBTOTAL_AMOUNT = "subtotalAmount";
  @SerializedName(SERIALIZED_NAME_SUBTOTAL_AMOUNT)
  private Double subtotalAmount;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private InvoiceTax tax;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_VOIDED_TIME = "voidedTime";
  @SerializedName(SERIALIZED_NAME_VOIDED_TIME)
  private OffsetDateTime voidedTime;

  public static final String SERIALIZED_NAME_WEBSITE_ID = "websiteId";
  @SerializedName(SERIALIZED_NAME_WEBSITE_ID)
  private String websiteId;

  public static final String SERIALIZED_NAME_EMBEDDED = "_embedded";
  @SerializedName(SERIALIZED_NAME_EMBEDDED)
  private List<InvoiceAllOfEmbedded> embedded = new ArrayList<>();

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<InvoiceAllOfLinks> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_DUE_REMINDER_NUMBER = "dueReminderNumber";
  @SerializedName(SERIALIZED_NAME_DUE_REMINDER_NUMBER)
  private Integer dueReminderNumber;

  public static final String SERIALIZED_NAME_DUE_REMINDER_TIME = "dueReminderTime";
  @SerializedName(SERIALIZED_NAME_DUE_REMINDER_TIME)
  private OffsetDateTime dueReminderTime;

  public static final String SERIALIZED_NAME_RETRY_INSTRUCTION = "retryInstruction";
  @SerializedName(SERIALIZED_NAME_RETRY_INSTRUCTION)
  private InvoiceAllOfRetryInstruction retryInstruction;

  public static final String SERIALIZED_NAME_REVISION = "revision";
  @SerializedName(SERIALIZED_NAME_REVISION)
  private Integer revision;

  public static final String SERIALIZED_NAME_TRANSACTIONS = "transactions";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONS)
  private List<Transaction> transactions = new ArrayList<>();

  /**
   * Invoice type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    INITIAL("initial"),
    
    RENEWAL("renewal"),
    
    INTERIM("interim"),
    
    CANCELLATION("cancellation"),
    
    ONE_TIME("one-time"),
    
    REFUND("refund"),
    
    CHARGE("charge");

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

  public Invoice() {
  }

  public Invoice(
     OffsetDateTime abandonedTime, 
     Double amount, 
     Double amountDue, 
     Integer autopayRetryNumber, 
     Integer collectionPeriod, 
     OffsetDateTime createdTime, 
     Integer delinquentCollectionPeriod, 
     Double discountAmount, 
     List<InvoiceDiscount> discounts, 
     OffsetDateTime dueTime, 
     String id, 
     Integer invoiceNumber, 
     OffsetDateTime issuedTime, 
     List<InvoiceItem> items, 
     OffsetDateTime paidTime, 
     String paymentFormUrl, 
     StatusEnum status, 
     String subscriptionId, 
     Double subtotalAmount, 
     OffsetDateTime updatedTime, 
     OffsetDateTime voidedTime, 
     List<InvoiceAllOfEmbedded> embedded, 
     List<InvoiceAllOfLinks> links, 
     Integer dueReminderNumber, 
     OffsetDateTime dueReminderTime, 
     Integer revision, 
     List<Transaction> transactions, 
     TypeEnum type
  ) {
    this();
    this.abandonedTime = abandonedTime;
    this.amount = amount;
    this.amountDue = amountDue;
    this.autopayRetryNumber = autopayRetryNumber;
    this.collectionPeriod = collectionPeriod;
    this.createdTime = createdTime;
    this.delinquentCollectionPeriod = delinquentCollectionPeriod;
    this.discountAmount = discountAmount;
    this.discounts = discounts;
    this.dueTime = dueTime;
    this.id = id;
    this.invoiceNumber = invoiceNumber;
    this.issuedTime = issuedTime;
    this.items = items;
    this.paidTime = paidTime;
    this.paymentFormUrl = paymentFormUrl;
    this.status = status;
    this.subscriptionId = subscriptionId;
    this.subtotalAmount = subtotalAmount;
    this.updatedTime = updatedTime;
    this.voidedTime = voidedTime;
    this.embedded = embedded;
    this.links = links;
    this.dueReminderNumber = dueReminderNumber;
    this.dueReminderTime = dueReminderTime;
    this.revision = revision;
    this.transactions = transactions;
    this.type = type;
  }

  /**
   * Invoice abandoned time.
   * @return abandonedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getAbandonedTime() {
    return abandonedTime;
  }



  /**
   * The invoice&#39;s amount.
   * @return amount
   */
  @javax.annotation.Nullable
  public Double getAmount() {
    return amount;
  }



  /**
   * The invoice&#39;s due amount.
   * @return amountDue
   */
  @javax.annotation.Nullable
  public Double getAmountDue() {
    return amountDue;
  }



  /**
   * Invoice autopay retry number.
   * minimum: 0
   * @return autopayRetryNumber
   */
  @javax.annotation.Nullable
  public Integer getAutopayRetryNumber() {
    return autopayRetryNumber;
  }



  public Invoice autopayScheduledTime(OffsetDateTime autopayScheduledTime) {
    this.autopayScheduledTime = autopayScheduledTime;
    return this;
  }

  /**
   * Invoice autopay scheduled time.
   * @return autopayScheduledTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getAutopayScheduledTime() {
    return autopayScheduledTime;
  }

  public void setAutopayScheduledTime(OffsetDateTime autopayScheduledTime) {
    this.autopayScheduledTime = autopayScheduledTime;
  }


  public Invoice billingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Invoice&#39;s billing address.
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
   * Collection period - difference between paidTime and issuedTime in days.
   * @return collectionPeriod
   */
  @javax.annotation.Nullable
  public Integer getCollectionPeriod() {
    return collectionPeriod;
  }



  /**
   * Invoice created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public Invoice currency(String currency) {
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
   * Delinquent collection period - difference between paidTime and dueTime in days.
   * @return delinquentCollectionPeriod
   */
  @javax.annotation.Nullable
  public Integer getDelinquentCollectionPeriod() {
    return delinquentCollectionPeriod;
  }



  public Invoice deliveryAddress(ContactObject deliveryAddress) {
    this.deliveryAddress = deliveryAddress;
    return this;
  }

  /**
   * Invoice&#39;s delivery address.
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
   * The invoice&#39;s discounts amount.
   * @return discountAmount
   */
  @javax.annotation.Nullable
  public Double getDiscountAmount() {
    return discountAmount;
  }



  /**
   * Discounts applied.
   * @return discounts
   */
  @javax.annotation.Nullable
  public List<InvoiceDiscount> getDiscounts() {
    return discounts;
  }



  /**
   * Invoice due time.
   * @return dueTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDueTime() {
    return dueTime;
  }



  /**
   * The invoice ID.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * An auto-incrementing number based on the sequence of invoices for any particular customer.
   * @return invoiceNumber
   */
  @javax.annotation.Nullable
  public Integer getInvoiceNumber() {
    return invoiceNumber;
  }



  /**
   * Invoice issued time.
   * @return issuedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getIssuedTime() {
    return issuedTime;
  }



  /**
   * Invoice items array.
   * @return items
   */
  @javax.annotation.Nullable
  public List<InvoiceItem> getItems() {
    return items;
  }



  public Invoice notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Notes for the customer which will be displayed on the invoice.
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  /**
   * Invoice paid time.
   * @return paidTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPaidTime() {
    return paidTime;
  }



  /**
   * URL where the customer can be redirected to pay for the invoice with one of the methods which are available for this customer. It&#39;s an alternative to creating a new transaction with empty &#x60;methods&#x60;. 
   * @return paymentFormUrl
   */
  @javax.annotation.Nullable
  public String getPaymentFormUrl() {
    return paymentFormUrl;
  }



  public Invoice poNumber(String poNumber) {
    this.poNumber = poNumber;
    return this;
  }

  /**
   * Purchase order number which will be displayed on the invoice.
   * @return poNumber
   */
  @javax.annotation.Nullable
  public String getPoNumber() {
    return poNumber;
  }

  public void setPoNumber(String poNumber) {
    this.poNumber = poNumber;
  }


  public Invoice shipping(InvoiceShipping shipping) {
    this.shipping = shipping;
    return this;
  }

  /**
   * Get shipping
   * @return shipping
   */
  @javax.annotation.Nullable
  public InvoiceShipping getShipping() {
    return shipping;
  }

  public void setShipping(InvoiceShipping shipping) {
    this.shipping = shipping;
  }


  /**
   * Invoice status.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  /**
   * The related order&#39;s ID if available, otherwise null.
   * @return subscriptionId
   */
  @javax.annotation.Nullable
  public String getSubscriptionId() {
    return subscriptionId;
  }



  /**
   * The invoice&#39;s subtotal amount.
   * @return subtotalAmount
   */
  @javax.annotation.Nullable
  public Double getSubtotalAmount() {
    return subtotalAmount;
  }



  public Invoice tax(InvoiceTax tax) {
    this.tax = tax;
    return this;
  }

  /**
   * Get tax
   * @return tax
   */
  @javax.annotation.Nullable
  public InvoiceTax getTax() {
    return tax;
  }

  public void setTax(InvoiceTax tax) {
    this.tax = tax;
  }


  /**
   * Invoice updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  /**
   * Invoice voided time.
   * @return voidedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getVoidedTime() {
    return voidedTime;
  }



  public Invoice websiteId(String websiteId) {
    this.websiteId = websiteId;
    return this;
  }

  /**
   * The website ID.
   * @return websiteId
   */
  @javax.annotation.Nonnull
  public String getWebsiteId() {
    return websiteId;
  }

  public void setWebsiteId(String websiteId) {
    this.websiteId = websiteId;
  }


  /**
   * Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter.
   * @return embedded
   */
  @javax.annotation.Nullable
  public List<InvoiceAllOfEmbedded> getEmbedded() {
    return embedded;
  }



  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<InvoiceAllOfLinks> getLinks() {
    return links;
  }



  public Invoice customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * The сustomer&#39;s ID.
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
   * Number of past due reminder events triggered.
   * @return dueReminderNumber
   */
  @javax.annotation.Nullable
  public Integer getDueReminderNumber() {
    return dueReminderNumber;
  }



  /**
   * Time past due reminder event will be triggered.
   * @return dueReminderTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDueReminderTime() {
    return dueReminderTime;
  }



  public Invoice retryInstruction(InvoiceAllOfRetryInstruction retryInstruction) {
    this.retryInstruction = retryInstruction;
    return this;
  }

  /**
   * Get retryInstruction
   * @return retryInstruction
   */
  @javax.annotation.Nullable
  public InvoiceAllOfRetryInstruction getRetryInstruction() {
    return retryInstruction;
  }

  public void setRetryInstruction(InvoiceAllOfRetryInstruction retryInstruction) {
    this.retryInstruction = retryInstruction;
  }


  /**
   * The number of times the invoice data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
   * @return revision
   */
  @javax.annotation.Nullable
  public Integer getRevision() {
    return revision;
  }



  /**
   * Invoice transactions array.
   * @return transactions
   */
  @javax.annotation.Nullable
  public List<Transaction> getTransactions() {
    return transactions;
  }



  /**
   * Invoice type.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Invoice invoice = (Invoice) o;
    return Objects.equals(this.abandonedTime, invoice.abandonedTime) &&
        Objects.equals(this.amount, invoice.amount) &&
        Objects.equals(this.amountDue, invoice.amountDue) &&
        Objects.equals(this.autopayRetryNumber, invoice.autopayRetryNumber) &&
        Objects.equals(this.autopayScheduledTime, invoice.autopayScheduledTime) &&
        Objects.equals(this.billingAddress, invoice.billingAddress) &&
        Objects.equals(this.collectionPeriod, invoice.collectionPeriod) &&
        Objects.equals(this.createdTime, invoice.createdTime) &&
        Objects.equals(this.currency, invoice.currency) &&
        Objects.equals(this.delinquentCollectionPeriod, invoice.delinquentCollectionPeriod) &&
        Objects.equals(this.deliveryAddress, invoice.deliveryAddress) &&
        Objects.equals(this.discountAmount, invoice.discountAmount) &&
        Objects.equals(this.discounts, invoice.discounts) &&
        Objects.equals(this.dueTime, invoice.dueTime) &&
        Objects.equals(this.id, invoice.id) &&
        Objects.equals(this.invoiceNumber, invoice.invoiceNumber) &&
        Objects.equals(this.issuedTime, invoice.issuedTime) &&
        Objects.equals(this.items, invoice.items) &&
        Objects.equals(this.notes, invoice.notes) &&
        Objects.equals(this.paidTime, invoice.paidTime) &&
        Objects.equals(this.paymentFormUrl, invoice.paymentFormUrl) &&
        Objects.equals(this.poNumber, invoice.poNumber) &&
        Objects.equals(this.shipping, invoice.shipping) &&
        Objects.equals(this.status, invoice.status) &&
        Objects.equals(this.subscriptionId, invoice.subscriptionId) &&
        Objects.equals(this.subtotalAmount, invoice.subtotalAmount) &&
        Objects.equals(this.tax, invoice.tax) &&
        Objects.equals(this.updatedTime, invoice.updatedTime) &&
        Objects.equals(this.voidedTime, invoice.voidedTime) &&
        Objects.equals(this.websiteId, invoice.websiteId) &&
        Objects.equals(this.embedded, invoice.embedded) &&
        Objects.equals(this.links, invoice.links) &&
        Objects.equals(this.customerId, invoice.customerId) &&
        Objects.equals(this.dueReminderNumber, invoice.dueReminderNumber) &&
        Objects.equals(this.dueReminderTime, invoice.dueReminderTime) &&
        Objects.equals(this.retryInstruction, invoice.retryInstruction) &&
        Objects.equals(this.revision, invoice.revision) &&
        Objects.equals(this.transactions, invoice.transactions) &&
        Objects.equals(this.type, invoice.type);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(abandonedTime, amount, amountDue, autopayRetryNumber, autopayScheduledTime, billingAddress, collectionPeriod, createdTime, currency, delinquentCollectionPeriod, deliveryAddress, discountAmount, discounts, dueTime, id, invoiceNumber, issuedTime, items, notes, paidTime, paymentFormUrl, poNumber, shipping, status, subscriptionId, subtotalAmount, tax, updatedTime, voidedTime, websiteId, embedded, links, customerId, dueReminderNumber, dueReminderTime, retryInstruction, revision, transactions, type);
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
    sb.append("class Invoice {\n");
    sb.append("    abandonedTime: ").append(toIndentedString(abandonedTime)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    amountDue: ").append(toIndentedString(amountDue)).append("\n");
    sb.append("    autopayRetryNumber: ").append(toIndentedString(autopayRetryNumber)).append("\n");
    sb.append("    autopayScheduledTime: ").append(toIndentedString(autopayScheduledTime)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    collectionPeriod: ").append(toIndentedString(collectionPeriod)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    delinquentCollectionPeriod: ").append(toIndentedString(delinquentCollectionPeriod)).append("\n");
    sb.append("    deliveryAddress: ").append(toIndentedString(deliveryAddress)).append("\n");
    sb.append("    discountAmount: ").append(toIndentedString(discountAmount)).append("\n");
    sb.append("    discounts: ").append(toIndentedString(discounts)).append("\n");
    sb.append("    dueTime: ").append(toIndentedString(dueTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invoiceNumber: ").append(toIndentedString(invoiceNumber)).append("\n");
    sb.append("    issuedTime: ").append(toIndentedString(issuedTime)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    paidTime: ").append(toIndentedString(paidTime)).append("\n");
    sb.append("    paymentFormUrl: ").append(toIndentedString(paymentFormUrl)).append("\n");
    sb.append("    poNumber: ").append(toIndentedString(poNumber)).append("\n");
    sb.append("    shipping: ").append(toIndentedString(shipping)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subscriptionId: ").append(toIndentedString(subscriptionId)).append("\n");
    sb.append("    subtotalAmount: ").append(toIndentedString(subtotalAmount)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    voidedTime: ").append(toIndentedString(voidedTime)).append("\n");
    sb.append("    websiteId: ").append(toIndentedString(websiteId)).append("\n");
    sb.append("    embedded: ").append(toIndentedString(embedded)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    dueReminderNumber: ").append(toIndentedString(dueReminderNumber)).append("\n");
    sb.append("    dueReminderTime: ").append(toIndentedString(dueReminderTime)).append("\n");
    sb.append("    retryInstruction: ").append(toIndentedString(retryInstruction)).append("\n");
    sb.append("    revision: ").append(toIndentedString(revision)).append("\n");
    sb.append("    transactions: ").append(toIndentedString(transactions)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("abandonedTime");
    openapiFields.add("amount");
    openapiFields.add("amountDue");
    openapiFields.add("autopayRetryNumber");
    openapiFields.add("autopayScheduledTime");
    openapiFields.add("billingAddress");
    openapiFields.add("collectionPeriod");
    openapiFields.add("createdTime");
    openapiFields.add("currency");
    openapiFields.add("delinquentCollectionPeriod");
    openapiFields.add("deliveryAddress");
    openapiFields.add("discountAmount");
    openapiFields.add("discounts");
    openapiFields.add("dueTime");
    openapiFields.add("id");
    openapiFields.add("invoiceNumber");
    openapiFields.add("issuedTime");
    openapiFields.add("items");
    openapiFields.add("notes");
    openapiFields.add("paidTime");
    openapiFields.add("paymentFormUrl");
    openapiFields.add("poNumber");
    openapiFields.add("shipping");
    openapiFields.add("status");
    openapiFields.add("subscriptionId");
    openapiFields.add("subtotalAmount");
    openapiFields.add("tax");
    openapiFields.add("updatedTime");
    openapiFields.add("voidedTime");
    openapiFields.add("websiteId");
    openapiFields.add("_embedded");
    openapiFields.add("_links");
    openapiFields.add("customerId");
    openapiFields.add("dueReminderNumber");
    openapiFields.add("dueReminderTime");
    openapiFields.add("retryInstruction");
    openapiFields.add("revision");
    openapiFields.add("transactions");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("websiteId");
    openapiRequiredFields.add("customerId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Invoice
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Invoice.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Invoice is not found in the empty JSON string", Invoice.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Invoice.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Invoice` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Invoice.openapiRequiredFields) {
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
      // validate the optional field `deliveryAddress`
      if (jsonObj.get("deliveryAddress") != null && !jsonObj.get("deliveryAddress").isJsonNull()) {
        ContactObject.validateJsonElement(jsonObj.get("deliveryAddress"));
      }
      if (jsonObj.get("discounts") != null && !jsonObj.get("discounts").isJsonNull()) {
        JsonArray jsonArraydiscounts = jsonObj.getAsJsonArray("discounts");
        if (jsonArraydiscounts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("discounts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `discounts` to be an array in the JSON string but got `%s`", jsonObj.get("discounts").toString()));
          }

          // validate the optional field `discounts` (array)
          for (int i = 0; i < jsonArraydiscounts.size(); i++) {
            InvoiceDiscount.validateJsonElement(jsonArraydiscounts.get(i));
          };
        }
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
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
            InvoiceItem.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("paymentFormUrl") != null && !jsonObj.get("paymentFormUrl").isJsonNull()) && !jsonObj.get("paymentFormUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentFormUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentFormUrl").toString()));
      }
      if ((jsonObj.get("poNumber") != null && !jsonObj.get("poNumber").isJsonNull()) && !jsonObj.get("poNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `poNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("poNumber").toString()));
      }
      // validate the optional field `shipping`
      if (jsonObj.get("shipping") != null && !jsonObj.get("shipping").isJsonNull()) {
        InvoiceShipping.validateJsonElement(jsonObj.get("shipping"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("subscriptionId") != null && !jsonObj.get("subscriptionId").isJsonNull()) && !jsonObj.get("subscriptionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriptionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriptionId").toString()));
      }
      // validate the optional field `tax`
      if (jsonObj.get("tax") != null && !jsonObj.get("tax").isJsonNull()) {
        InvoiceTax.validateJsonElement(jsonObj.get("tax"));
      }
      if (!jsonObj.get("websiteId").isJsonPrimitive()) {
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
            InvoiceAllOfEmbedded.validateJsonElement(jsonArrayembedded.get(i));
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
            InvoiceAllOfLinks.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if (!jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      // validate the optional field `retryInstruction`
      if (jsonObj.get("retryInstruction") != null && !jsonObj.get("retryInstruction").isJsonNull()) {
        InvoiceAllOfRetryInstruction.validateJsonElement(jsonObj.get("retryInstruction"));
      }
      if (jsonObj.get("transactions") != null && !jsonObj.get("transactions").isJsonNull()) {
        JsonArray jsonArraytransactions = jsonObj.getAsJsonArray("transactions");
        if (jsonArraytransactions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("transactions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `transactions` to be an array in the JSON string but got `%s`", jsonObj.get("transactions").toString()));
          }

          // validate the optional field `transactions` (array)
          for (int i = 0; i < jsonArraytransactions.size(); i++) {
            Transaction.validateJsonElement(jsonArraytransactions.get(i));
          };
        }
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Invoice.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Invoice' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Invoice> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Invoice.class));

       return (TypeAdapter<T>) new TypeAdapter<Invoice>() {
           @Override
           public void write(JsonWriter out, Invoice value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Invoice read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Invoice given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Invoice
   * @throws IOException if the JSON string is invalid with respect to Invoice
   */
  public static Invoice fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Invoice.class);
  }

  /**
   * Convert an instance of Invoice to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

