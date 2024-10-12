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
import org.openapitools.client.model.AcquirerName;
import org.openapitools.client.model.DigitalWallets;
import org.openapitools.client.model.GatewayAccountLinksInner;
import org.openapitools.client.model.GatewayName;
import org.openapitools.client.model.PaymentCardBrand;
import org.openapitools.client.model.PaymentMethod;
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
 * GatewayAccount
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GatewayAccount {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<GatewayAccountLinksInner> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_ACCEPTED_CURRENCIES = "acceptedCurrencies";
  @SerializedName(SERIALIZED_NAME_ACCEPTED_CURRENCIES)
  private List<String> acceptedCurrencies = new ArrayList<>();

  public static final String SERIALIZED_NAME_ACQUIRER_NAME = "acquirerName";
  @SerializedName(SERIALIZED_NAME_ACQUIRER_NAME)
  private AcquirerName acquirerName = AcquirerName.OTHER;

  public static final String SERIALIZED_NAME_ADDITIONAL_FILTERS = "additionalFilters";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_FILTERS)
  private String additionalFilters;

  public static final String SERIALIZED_NAME_APPROVAL_WINDOW_TTL = "approvalWindowTtl";
  @SerializedName(SERIALIZED_NAME_APPROVAL_WINDOW_TTL)
  private Integer approvalWindowTtl = 3600;

  public static final String SERIALIZED_NAME_CITY_FIELD = "cityField";
  @SerializedName(SERIALIZED_NAME_CITY_FIELD)
  private String cityField;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_DCC_FORCE_CURRENCY = "dccForceCurrency";
  @SerializedName(SERIALIZED_NAME_DCC_FORCE_CURRENCY)
  private String dccForceCurrency;

  public static final String SERIALIZED_NAME_DCC_MARKUP = "dccMarkup";
  @SerializedName(SERIALIZED_NAME_DCC_MARKUP)
  private Integer dccMarkup;

  public static final String SERIALIZED_NAME_DESCRIPTOR = "descriptor";
  @SerializedName(SERIALIZED_NAME_DESCRIPTOR)
  private String descriptor;

  public static final String SERIALIZED_NAME_DIGITAL_WALLETS = "digitalWallets";
  @SerializedName(SERIALIZED_NAME_DIGITAL_WALLETS)
  private DigitalWallets digitalWallets;

  public static final String SERIALIZED_NAME_DYNAMIC_DESCRIPTOR = "dynamicDescriptor";
  @SerializedName(SERIALIZED_NAME_DYNAMIC_DESCRIPTOR)
  private Boolean dynamicDescriptor = false;

  public static final String SERIALIZED_NAME_EXCLUDED_DCC_QUOTE_CURRENCIES = "excludedDccQuoteCurrencies";
  @SerializedName(SERIALIZED_NAME_EXCLUDED_DCC_QUOTE_CURRENCIES)
  private List<String> excludedDccQuoteCurrencies = new ArrayList<>();

  public static final String SERIALIZED_NAME_GATEWAY_NAME = "gatewayName";
  @SerializedName(SERIALIZED_NAME_GATEWAY_NAME)
  protected GatewayName gatewayName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_DOWN = "isDown";
  @SerializedName(SERIALIZED_NAME_IS_DOWN)
  private Boolean isDown;

  public static final String SERIALIZED_NAME_MERCHANT_CATEGORY_CODE = "merchantCategoryCode";
  @SerializedName(SERIALIZED_NAME_MERCHANT_CATEGORY_CODE)
  private String merchantCategoryCode = "0000";

  public static final String SERIALIZED_NAME_METHOD = "method";
  @SerializedName(SERIALIZED_NAME_METHOD)
  private PaymentMethod method;

  public static final String SERIALIZED_NAME_MONTHLY_LIMIT = "monthlyLimit";
  @SerializedName(SERIALIZED_NAME_MONTHLY_LIMIT)
  private Double monthlyLimit;

  public static final String SERIALIZED_NAME_ORGANIZATION_ID = "organizationId";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_ORGANIZATION_ID)
  private String organizationId;

  public static final String SERIALIZED_NAME_PAYMENT_CARD_SCHEMES = "paymentCardSchemes";
  @SerializedName(SERIALIZED_NAME_PAYMENT_CARD_SCHEMES)
  private List<PaymentCardBrand> paymentCardSchemes = new ArrayList<>();

  public static final String SERIALIZED_NAME_RECONCILIATION_WINDOW_ENABLED = "reconciliationWindowEnabled";
  @SerializedName(SERIALIZED_NAME_RECONCILIATION_WINDOW_ENABLED)
  private Boolean reconciliationWindowEnabled = false;

  public static final String SERIALIZED_NAME_RECONCILIATION_WINDOW_TTL = "reconciliationWindowTtl";
  @SerializedName(SERIALIZED_NAME_RECONCILIATION_WINDOW_TTL)
  private Integer reconciliationWindowTtl;

  /**
   * The gateway account&#39;s status.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    ACTIVE("active"),
    
    INACTIVE("inactive"),
    
    PENDING("pending"),
    
    CLOSED("closed");

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

  public static final String SERIALIZED_NAME_STICKY = "sticky";
  @SerializedName(SERIALIZED_NAME_STICKY)
  private Boolean sticky = true;

  public static final String SERIALIZED_NAME_THREE_D_SECURE = "threeDSecure";
  @SerializedName(SERIALIZED_NAME_THREE_D_SECURE)
  private Boolean threeDSecure = false;

  public static final String SERIALIZED_NAME_TIMEOUT = "timeout";
  @SerializedName(SERIALIZED_NAME_TIMEOUT)
  private Integer timeout;

  public static final String SERIALIZED_NAME_TOKEN = "token";
  @SerializedName(SERIALIZED_NAME_TOKEN)
  private String token;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public GatewayAccount() {
    this.gatewayName = this.getClass().getSimpleName();
  }

  public GatewayAccount(
     List<GatewayAccountLinksInner> links, 
     OffsetDateTime createdTime, 
     String id, 
     Boolean isDown, 
     String organizationId, 
     StatusEnum status, 
     String token, 
     OffsetDateTime updatedTime
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.id = id;
    this.isDown = isDown;
    this.organizationId = organizationId;
    this.status = status;
    this.token = token;
    this.updatedTime = updatedTime;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<GatewayAccountLinksInner> getLinks() {
    return links;
  }



  public GatewayAccount acceptedCurrencies(List<String> acceptedCurrencies) {
    this.acceptedCurrencies = acceptedCurrencies;
    return this;
  }

  public GatewayAccount addAcceptedCurrenciesItem(String acceptedCurrenciesItem) {
    if (this.acceptedCurrencies == null) {
      this.acceptedCurrencies = new ArrayList<>();
    }
    this.acceptedCurrencies.add(acceptedCurrenciesItem);
    return this;
  }

  /**
   * Accepted currencies (array of the currency three letter codes).
   * @return acceptedCurrencies
   */
  @javax.annotation.Nonnull
  public List<String> getAcceptedCurrencies() {
    return acceptedCurrencies;
  }

  public void setAcceptedCurrencies(List<String> acceptedCurrencies) {
    this.acceptedCurrencies = acceptedCurrencies;
  }


  public GatewayAccount acquirerName(AcquirerName acquirerName) {
    this.acquirerName = acquirerName;
    return this;
  }

  /**
   * Get acquirerName
   * @return acquirerName
   */
  @javax.annotation.Nullable
  public AcquirerName getAcquirerName() {
    return acquirerName;
  }

  public void setAcquirerName(AcquirerName acquirerName) {
    this.acquirerName = acquirerName;
  }


  public GatewayAccount additionalFilters(String additionalFilters) {
    this.additionalFilters = additionalFilters;
    return this;
  }

  /**
   * The additional filters are used to determine whether the gateway account can be selected for the transaction to be processed. For example, the filter may put a maximum amount value. If the transaction is above that amount, this gateway account wouldn&#39;t be used. This follows our standard filter format. 
   * @return additionalFilters
   */
  @javax.annotation.Nullable
  public String getAdditionalFilters() {
    return additionalFilters;
  }

  public void setAdditionalFilters(String additionalFilters) {
    this.additionalFilters = additionalFilters;
  }


  public GatewayAccount approvalWindowTtl(Integer approvalWindowTtl) {
    this.approvalWindowTtl = approvalWindowTtl;
    return this;
  }

  /**
   * The time window (in seconds) allotted for approving an offsite transaction before it is automatically &#x60;abandoned&#x60;.
   * minimum: 300
   * maximum: 16777215
   * @return approvalWindowTtl
   */
  @javax.annotation.Nullable
  public Integer getApprovalWindowTtl() {
    return approvalWindowTtl;
  }

  public void setApprovalWindowTtl(Integer approvalWindowTtl) {
    this.approvalWindowTtl = approvalWindowTtl;
  }


  public GatewayAccount cityField(String cityField) {
    this.cityField = cityField;
    return this;
  }

  /**
   * The gateway account&#39;s city field (also known as line 2 descriptor).
   * @return cityField
   */
  @javax.annotation.Nullable
  public String getCityField() {
    return cityField;
  }

  public void setCityField(String cityField) {
    this.cityField = cityField;
  }


  /**
   * Gateway Account created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public GatewayAccount dccForceCurrency(String dccForceCurrency) {
    this.dccForceCurrency = dccForceCurrency;
    return this;
  }

  /**
   * Force dynamic currency conversion to the specified currency on each sale. Leave it empty to disable force DCC. 
   * @return dccForceCurrency
   */
  @javax.annotation.Nullable
  public String getDccForceCurrency() {
    return dccForceCurrency;
  }

  public void setDccForceCurrency(String dccForceCurrency) {
    this.dccForceCurrency = dccForceCurrency;
  }


  public GatewayAccount dccMarkup(Integer dccMarkup) {
    this.dccMarkup = dccMarkup;
    return this;
  }

  /**
   * Dynamic currency conversion markup in basis points.
   * minimum: -10000
   * maximum: 10000
   * @return dccMarkup
   */
  @javax.annotation.Nullable
  public Integer getDccMarkup() {
    return dccMarkup;
  }

  public void setDccMarkup(Integer dccMarkup) {
    this.dccMarkup = dccMarkup;
  }


  public GatewayAccount descriptor(String descriptor) {
    this.descriptor = descriptor;
    return this;
  }

  /**
   * The gateway account&#39;s descriptor.
   * @return descriptor
   */
  @javax.annotation.Nullable
  public String getDescriptor() {
    return descriptor;
  }

  public void setDescriptor(String descriptor) {
    this.descriptor = descriptor;
  }


  public GatewayAccount digitalWallets(DigitalWallets digitalWallets) {
    this.digitalWallets = digitalWallets;
    return this;
  }

  /**
   * Get digitalWallets
   * @return digitalWallets
   */
  @javax.annotation.Nullable
  public DigitalWallets getDigitalWallets() {
    return digitalWallets;
  }

  public void setDigitalWallets(DigitalWallets digitalWallets) {
    this.digitalWallets = digitalWallets;
  }


  public GatewayAccount dynamicDescriptor(Boolean dynamicDescriptor) {
    this.dynamicDescriptor = dynamicDescriptor;
    return this;
  }

  /**
   * True, if Gateway Account allows dynamic descriptor.
   * @return dynamicDescriptor
   */
  @javax.annotation.Nullable
  public Boolean getDynamicDescriptor() {
    return dynamicDescriptor;
  }

  public void setDynamicDescriptor(Boolean dynamicDescriptor) {
    this.dynamicDescriptor = dynamicDescriptor;
  }


  public GatewayAccount excludedDccQuoteCurrencies(List<String> excludedDccQuoteCurrencies) {
    this.excludedDccQuoteCurrencies = excludedDccQuoteCurrencies;
    return this;
  }

  public GatewayAccount addExcludedDccQuoteCurrenciesItem(String excludedDccQuoteCurrenciesItem) {
    if (this.excludedDccQuoteCurrencies == null) {
      this.excludedDccQuoteCurrencies = new ArrayList<>();
    }
    this.excludedDccQuoteCurrencies.add(excludedDccQuoteCurrenciesItem);
    return this;
  }

  /**
   * Excluded Dynamic Currency Conversion Quote Currencies.
   * @return excludedDccQuoteCurrencies
   */
  @javax.annotation.Nullable
  public List<String> getExcludedDccQuoteCurrencies() {
    return excludedDccQuoteCurrencies;
  }

  public void setExcludedDccQuoteCurrencies(List<String> excludedDccQuoteCurrencies) {
    this.excludedDccQuoteCurrencies = excludedDccQuoteCurrencies;
  }


  public GatewayAccount gatewayName(GatewayName gatewayName) {
    this.gatewayName = gatewayName;
    return this;
  }

  /**
   * Get gatewayName
   * @return gatewayName
   */
  @javax.annotation.Nonnull
  public GatewayName getGatewayName() {
    return gatewayName;
  }

  public void setGatewayName(GatewayName gatewayName) {
    this.gatewayName = gatewayName;
  }


  /**
   * The gateway identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * True if gateway is currently in downtime period.
   * @return isDown
   */
  @javax.annotation.Nullable
  public Boolean getIsDown() {
    return isDown;
  }



  public GatewayAccount merchantCategoryCode(String merchantCategoryCode) {
    this.merchantCategoryCode = merchantCategoryCode;
    return this;
  }

  /**
   * The gateway account&#39;s merchant category code.
   * @return merchantCategoryCode
   */
  @javax.annotation.Nullable
  public String getMerchantCategoryCode() {
    return merchantCategoryCode;
  }

  public void setMerchantCategoryCode(String merchantCategoryCode) {
    this.merchantCategoryCode = merchantCategoryCode;
  }


  public GatewayAccount method(PaymentMethod method) {
    this.method = method;
    return this;
  }

  /**
   * Get method
   * @return method
   */
  @javax.annotation.Nonnull
  public PaymentMethod getMethod() {
    return method;
  }

  public void setMethod(PaymentMethod method) {
    this.method = method;
  }


  public GatewayAccount monthlyLimit(Double monthlyLimit) {
    this.monthlyLimit = monthlyLimit;
    return this;
  }

  /**
   * Monthly Limit.
   * minimum: 0
   * @return monthlyLimit
   */
  @javax.annotation.Nullable
  public Double getMonthlyLimit() {
    return monthlyLimit;
  }

  public void setMonthlyLimit(Double monthlyLimit) {
    this.monthlyLimit = monthlyLimit;
  }


  /**
   * Organization ID.
   * @return organizationId
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getOrganizationId() {
    return organizationId;
  }



  public GatewayAccount paymentCardSchemes(List<PaymentCardBrand> paymentCardSchemes) {
    this.paymentCardSchemes = paymentCardSchemes;
    return this;
  }

  public GatewayAccount addPaymentCardSchemesItem(PaymentCardBrand paymentCardSchemesItem) {
    if (this.paymentCardSchemes == null) {
      this.paymentCardSchemes = new ArrayList<>();
    }
    this.paymentCardSchemes.add(paymentCardSchemesItem);
    return this;
  }

  /**
   * Accepted payment card brands.
   * @return paymentCardSchemes
   */
  @javax.annotation.Nullable
  public List<PaymentCardBrand> getPaymentCardSchemes() {
    return paymentCardSchemes;
  }

  public void setPaymentCardSchemes(List<PaymentCardBrand> paymentCardSchemes) {
    this.paymentCardSchemes = paymentCardSchemes;
  }


  public GatewayAccount reconciliationWindowEnabled(Boolean reconciliationWindowEnabled) {
    this.reconciliationWindowEnabled = reconciliationWindowEnabled;
    return this;
  }

  /**
   * If a transaction is not reconciled within the &#x60;reconciliationWindowTtl&#x60; time, then the transaction is marked as &#x60;abandoned&#x60;.
   * @return reconciliationWindowEnabled
   */
  @javax.annotation.Nullable
  public Boolean getReconciliationWindowEnabled() {
    return reconciliationWindowEnabled;
  }

  public void setReconciliationWindowEnabled(Boolean reconciliationWindowEnabled) {
    this.reconciliationWindowEnabled = reconciliationWindowEnabled;
  }


  public GatewayAccount reconciliationWindowTtl(Integer reconciliationWindowTtl) {
    this.reconciliationWindowTtl = reconciliationWindowTtl;
    return this;
  }

  /**
   * The time window (in seconds) allotted for a reconciliation to occur. If it is not reconciled in that time, then the transaction is marked as &#x60;abandoned&#x60;.
   * minimum: 300
   * maximum: 16777215
   * @return reconciliationWindowTtl
   */
  @javax.annotation.Nullable
  public Integer getReconciliationWindowTtl() {
    return reconciliationWindowTtl;
  }

  public void setReconciliationWindowTtl(Integer reconciliationWindowTtl) {
    this.reconciliationWindowTtl = reconciliationWindowTtl;
  }


  /**
   * The gateway account&#39;s status.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  public GatewayAccount sticky(Boolean sticky) {
    this.sticky = sticky;
    return this;
  }

  /**
   * Customer&#39;s payment instrument will \&quot;stick\&quot; to the gateway account for future transactions when enabled.
   * @return sticky
   */
  @javax.annotation.Nullable
  public Boolean getSticky() {
    return sticky;
  }

  public void setSticky(Boolean sticky) {
    this.sticky = sticky;
  }


  public GatewayAccount threeDSecure(Boolean threeDSecure) {
    this.threeDSecure = threeDSecure;
    return this;
  }

  /**
   * True, if Gateway Account allows 3DSecure.
   * @return threeDSecure
   */
  @javax.annotation.Nullable
  public Boolean getThreeDSecure() {
    return threeDSecure;
  }

  public void setThreeDSecure(Boolean threeDSecure) {
    this.threeDSecure = threeDSecure;
  }


  public GatewayAccount timeout(Integer timeout) {
    this.timeout = timeout;
    return this;
  }

  /**
   * Gateway Account request timeout in seconds.
   * minimum: 10
   * maximum: 120
   * @return timeout
   */
  @javax.annotation.Nullable
  public Integer getTimeout() {
    return timeout;
  }

  public void setTimeout(Integer timeout) {
    this.timeout = timeout;
  }


  /**
   * Gateway Account token.
   * @return token
   */
  @javax.annotation.Nullable
  public String getToken() {
    return token;
  }



  /**
   * Gateway Account updated time.
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
    GatewayAccount gatewayAccount = (GatewayAccount) o;
    return Objects.equals(this.links, gatewayAccount.links) &&
        Objects.equals(this.acceptedCurrencies, gatewayAccount.acceptedCurrencies) &&
        Objects.equals(this.acquirerName, gatewayAccount.acquirerName) &&
        Objects.equals(this.additionalFilters, gatewayAccount.additionalFilters) &&
        Objects.equals(this.approvalWindowTtl, gatewayAccount.approvalWindowTtl) &&
        Objects.equals(this.cityField, gatewayAccount.cityField) &&
        Objects.equals(this.createdTime, gatewayAccount.createdTime) &&
        Objects.equals(this.dccForceCurrency, gatewayAccount.dccForceCurrency) &&
        Objects.equals(this.dccMarkup, gatewayAccount.dccMarkup) &&
        Objects.equals(this.descriptor, gatewayAccount.descriptor) &&
        Objects.equals(this.digitalWallets, gatewayAccount.digitalWallets) &&
        Objects.equals(this.dynamicDescriptor, gatewayAccount.dynamicDescriptor) &&
        Objects.equals(this.excludedDccQuoteCurrencies, gatewayAccount.excludedDccQuoteCurrencies) &&
        Objects.equals(this.gatewayName, gatewayAccount.gatewayName) &&
        Objects.equals(this.id, gatewayAccount.id) &&
        Objects.equals(this.isDown, gatewayAccount.isDown) &&
        Objects.equals(this.merchantCategoryCode, gatewayAccount.merchantCategoryCode) &&
        Objects.equals(this.method, gatewayAccount.method) &&
        Objects.equals(this.monthlyLimit, gatewayAccount.monthlyLimit) &&
        Objects.equals(this.organizationId, gatewayAccount.organizationId) &&
        Objects.equals(this.paymentCardSchemes, gatewayAccount.paymentCardSchemes) &&
        Objects.equals(this.reconciliationWindowEnabled, gatewayAccount.reconciliationWindowEnabled) &&
        Objects.equals(this.reconciliationWindowTtl, gatewayAccount.reconciliationWindowTtl) &&
        Objects.equals(this.status, gatewayAccount.status) &&
        Objects.equals(this.sticky, gatewayAccount.sticky) &&
        Objects.equals(this.threeDSecure, gatewayAccount.threeDSecure) &&
        Objects.equals(this.timeout, gatewayAccount.timeout) &&
        Objects.equals(this.token, gatewayAccount.token) &&
        Objects.equals(this.updatedTime, gatewayAccount.updatedTime);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, acceptedCurrencies, acquirerName, additionalFilters, approvalWindowTtl, cityField, createdTime, dccForceCurrency, dccMarkup, descriptor, digitalWallets, dynamicDescriptor, excludedDccQuoteCurrencies, gatewayName, id, isDown, merchantCategoryCode, method, monthlyLimit, organizationId, paymentCardSchemes, reconciliationWindowEnabled, reconciliationWindowTtl, status, sticky, threeDSecure, timeout, token, updatedTime);
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
    sb.append("class GatewayAccount {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    acceptedCurrencies: ").append(toIndentedString(acceptedCurrencies)).append("\n");
    sb.append("    acquirerName: ").append(toIndentedString(acquirerName)).append("\n");
    sb.append("    additionalFilters: ").append(toIndentedString(additionalFilters)).append("\n");
    sb.append("    approvalWindowTtl: ").append(toIndentedString(approvalWindowTtl)).append("\n");
    sb.append("    cityField: ").append(toIndentedString(cityField)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    dccForceCurrency: ").append(toIndentedString(dccForceCurrency)).append("\n");
    sb.append("    dccMarkup: ").append(toIndentedString(dccMarkup)).append("\n");
    sb.append("    descriptor: ").append(toIndentedString(descriptor)).append("\n");
    sb.append("    digitalWallets: ").append(toIndentedString(digitalWallets)).append("\n");
    sb.append("    dynamicDescriptor: ").append(toIndentedString(dynamicDescriptor)).append("\n");
    sb.append("    excludedDccQuoteCurrencies: ").append(toIndentedString(excludedDccQuoteCurrencies)).append("\n");
    sb.append("    gatewayName: ").append(toIndentedString(gatewayName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isDown: ").append(toIndentedString(isDown)).append("\n");
    sb.append("    merchantCategoryCode: ").append(toIndentedString(merchantCategoryCode)).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    monthlyLimit: ").append(toIndentedString(monthlyLimit)).append("\n");
    sb.append("    organizationId: ").append(toIndentedString(organizationId)).append("\n");
    sb.append("    paymentCardSchemes: ").append(toIndentedString(paymentCardSchemes)).append("\n");
    sb.append("    reconciliationWindowEnabled: ").append(toIndentedString(reconciliationWindowEnabled)).append("\n");
    sb.append("    reconciliationWindowTtl: ").append(toIndentedString(reconciliationWindowTtl)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    sticky: ").append(toIndentedString(sticky)).append("\n");
    sb.append("    threeDSecure: ").append(toIndentedString(threeDSecure)).append("\n");
    sb.append("    timeout: ").append(toIndentedString(timeout)).append("\n");
    sb.append("    token: ").append(toIndentedString(token)).append("\n");
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
    openapiFields.add("_links");
    openapiFields.add("acceptedCurrencies");
    openapiFields.add("acquirerName");
    openapiFields.add("additionalFilters");
    openapiFields.add("approvalWindowTtl");
    openapiFields.add("cityField");
    openapiFields.add("createdTime");
    openapiFields.add("dccForceCurrency");
    openapiFields.add("dccMarkup");
    openapiFields.add("descriptor");
    openapiFields.add("digitalWallets");
    openapiFields.add("dynamicDescriptor");
    openapiFields.add("excludedDccQuoteCurrencies");
    openapiFields.add("gatewayName");
    openapiFields.add("id");
    openapiFields.add("isDown");
    openapiFields.add("merchantCategoryCode");
    openapiFields.add("method");
    openapiFields.add("monthlyLimit");
    openapiFields.add("organizationId");
    openapiFields.add("paymentCardSchemes");
    openapiFields.add("reconciliationWindowEnabled");
    openapiFields.add("reconciliationWindowTtl");
    openapiFields.add("status");
    openapiFields.add("sticky");
    openapiFields.add("threeDSecure");
    openapiFields.add("timeout");
    openapiFields.add("token");
    openapiFields.add("updatedTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("acceptedCurrencies");
    openapiRequiredFields.add("gatewayName");
    openapiRequiredFields.add("method");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GatewayAccount
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GatewayAccount.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GatewayAccount is not found in the empty JSON string", GatewayAccount.openapiRequiredFields.toString()));
        }
      }

      String discriminatorValue = jsonElement.getAsJsonObject().get("gatewayName").getAsString();
      switch (discriminatorValue) {
        case "A1Gateway":
          A1Gateway.validateJsonElement(jsonElement);
          break;
        case "Adyen":
          Adyen.validateJsonElement(jsonElement);
          break;
        case "Airpay":
          Airpay.validateJsonElement(jsonElement);
          break;
        case "AmexVPC":
          AmexVPC.validateJsonElement(jsonElement);
          break;
        case "ApcoPay":
          ApcoPay.validateJsonElement(jsonElement);
          break;
        case "AsiaPaymentGateway":
          AsiaPaymentGateway.validateJsonElement(jsonElement);
          break;
        case "AstroPayCard":
          AstroPayCard.validateJsonElement(jsonElement);
          break;
        case "AuthorizeNet":
          AuthorizeNet.validateJsonElement(jsonElement);
          break;
        case "Bambora":
          Bambora.validateJsonElement(jsonElement);
          break;
        case "BitPay":
          BitPay.validateJsonElement(jsonElement);
          break;
        case "BlueSnap":
          BlueSnap.validateJsonElement(jsonElement);
          break;
        case "BraintreePayments":
          BraintreePayments.validateJsonElement(jsonElement);
          break;
        case "CASHlib":
          CASHlib.validateJsonElement(jsonElement);
          break;
        case "CCAvenue":
          CCAvenue.validateJsonElement(jsonElement);
          break;
        case "CODVoucher":
          CODVoucher.validateJsonElement(jsonElement);
          break;
        case "Cardknox":
          Cardknox.validateJsonElement(jsonElement);
          break;
        case "CashToCode":
          CashToCode.validateJsonElement(jsonElement);
          break;
        case "Cashflows":
          Cashflows.validateJsonElement(jsonElement);
          break;
        case "CauriPayment":
          CauriPayment.validateJsonElement(jsonElement);
          break;
        case "Cayan":
          Cayan.validateJsonElement(jsonElement);
          break;
        case "Chase":
          Chase.validateJsonElement(jsonElement);
          break;
        case "Circle":
          Circle.validateJsonElement(jsonElement);
          break;
        case "Citadel":
          Citadel.validateJsonElement(jsonElement);
          break;
        case "Clearhaus":
          Clearhaus.validateJsonElement(jsonElement);
          break;
        case "CoinPayments":
          CoinPayments.validateJsonElement(jsonElement);
          break;
        case "Conekta":
          Conekta.validateJsonElement(jsonElement);
          break;
        case "Coppr":
          Coppr.validateJsonElement(jsonElement);
          break;
        case "Credorax":
          Credorax.validateJsonElement(jsonElement);
          break;
        case "Cryptonator":
          Cryptonator.validateJsonElement(jsonElement);
          break;
        case "CyberSource":
          CyberSource.validateJsonElement(jsonElement);
          break;
        case "DataCash":
          DataCash.validateJsonElement(jsonElement);
          break;
        case "Dengi":
          Dengi.validateJsonElement(jsonElement);
          break;
        case "Directa24":
          Directa24.validateJsonElement(jsonElement);
          break;
        case "Dragonphoenix":
          Dragonphoenix.validateJsonElement(jsonElement);
          break;
        case "EBANX":
          EBANX.validateJsonElement(jsonElement);
          break;
        case "EMS":
          EMS.validateJsonElement(jsonElement);
          break;
        case "EPG":
          EPG.validateJsonElement(jsonElement);
          break;
        case "EPro":
          EPro.validateJsonElement(jsonElement);
          break;
        case "EcorePay":
          EcorePay.validateJsonElement(jsonElement);
          break;
        case "Elavon":
          Elavon.validateJsonElement(jsonElement);
          break;
        case "Euteller":
          Euteller.validateJsonElement(jsonElement);
          break;
        case "FinTecSystems":
          FinTecSystems.validateJsonElement(jsonElement);
          break;
        case "Finrax":
          Finrax.validateJsonElement(jsonElement);
          break;
        case "Flexepin":
          Flexepin.validateJsonElement(jsonElement);
          break;
        case "Forte":
          Forte.validateJsonElement(jsonElement);
          break;
        case "FundSend":
          FundSend.validateJsonElement(jsonElement);
          break;
        case "GET":
          GET.validateJsonElement(jsonElement);
          break;
        case "Gigadat":
          Gigadat.validateJsonElement(jsonElement);
          break;
        case "GlobalOne":
          GlobalOne.validateJsonElement(jsonElement);
          break;
        case "Gooney":
          Gooney.validateJsonElement(jsonElement);
          break;
        case "Gpaysafe":
          Gpaysafe.validateJsonElement(jsonElement);
          break;
        case "Greenbox":
          Greenbox.validateJsonElement(jsonElement);
          break;
        case "HiPay":
          HiPay.validateJsonElement(jsonElement);
          break;
        case "ICEPAY":
          ICEPAY.validateJsonElement(jsonElement);
          break;
        case "INOVAPAY":
          INOVAPAY.validateJsonElement(jsonElement);
          break;
        case "Ilixium":
          Ilixium.validateJsonElement(jsonElement);
          break;
        case "Ingenico":
          Ingenico.validateJsonElement(jsonElement);
          break;
        case "Inovio":
          Inovio.validateJsonElement(jsonElement);
          break;
        case "InstaDebit":
          InstaDebit.validateJsonElement(jsonElement);
          break;
        case "Intuit":
          Intuit.validateJsonElement(jsonElement);
          break;
        case "IpayOptions":
          IpayOptions.validateJsonElement(jsonElement);
          break;
        case "JetPay":
          JetPay.validateJsonElement(jsonElement);
          break;
        case "Jeton":
          Jeton.validateJsonElement(jsonElement);
          break;
        case "Khelocard":
          Khelocard.validateJsonElement(jsonElement);
          break;
        case "Konnektive":
          Konnektive.validateJsonElement(jsonElement);
          break;
        case "LPG":
          LPG.validateJsonElement(jsonElement);
          break;
        case "MiFinity":
          MiFinity.validateJsonElement(jsonElement);
          break;
        case "Moneris":
          Moneris.validateJsonElement(jsonElement);
          break;
        case "MtaPay":
          MtaPay.validateJsonElement(jsonElement);
          break;
        case "MuchBetter":
          MuchBetter.validateJsonElement(jsonElement);
          break;
        case "MyFatoorah":
          MyFatoorah.validateJsonElement(jsonElement);
          break;
        case "NGenius":
          NGenius.validateJsonElement(jsonElement);
          break;
        case "NMI":
          NMI.validateJsonElement(jsonElement);
          break;
        case "Neosurf":
          Neosurf.validateJsonElement(jsonElement);
          break;
        case "Netbanking":
          Netbanking.validateJsonElement(jsonElement);
          break;
        case "Neteller":
          Neteller.validateJsonElement(jsonElement);
          break;
        case "NinjaWallet":
          NinjaWallet.validateJsonElement(jsonElement);
          break;
        case "NuaPay":
          NuaPay.validateJsonElement(jsonElement);
          break;
        case "OchaPay":
          OchaPay.validateJsonElement(jsonElement);
          break;
        case "OnRamp":
          OnRamp.validateJsonElement(jsonElement);
          break;
        case "Onlineueberweisen":
          Onlineueberweisen.validateJsonElement(jsonElement);
          break;
        case "Pagsmile":
          Pagsmile.validateJsonElement(jsonElement);
          break;
        case "Panamerican":
          Panamerican.validateJsonElement(jsonElement);
          break;
        case "PandaGateway":
          PandaGateway.validateJsonElement(jsonElement);
          break;
        case "ParamountEft":
          ParamountEft.validateJsonElement(jsonElement);
          break;
        case "ParamountInterac":
          ParamountInterac.validateJsonElement(jsonElement);
          break;
        case "Pay4Fun":
          Pay4Fun.validateJsonElement(jsonElement);
          break;
        case "PayCash":
          PayCash.validateJsonElement(jsonElement);
          break;
        case "PayClub":
          PayClub.validateJsonElement(jsonElement);
          break;
        case "PayPal":
          PayPal.validateJsonElement(jsonElement);
          break;
        case "PayTabs":
          PayTabs.validateJsonElement(jsonElement);
          break;
        case "PayULatam":
          PayULatam.validateJsonElement(jsonElement);
          break;
        case "Payeezy":
          Payeezy.validateJsonElement(jsonElement);
          break;
        case "Payflow":
          Payflow.validateJsonElement(jsonElement);
          break;
        case "PaymenTechnologies":
          PaymenTechnologies.validateJsonElement(jsonElement);
          break;
        case "PaymentAsia":
          PaymentAsia.validateJsonElement(jsonElement);
          break;
        case "PaymentsOS":
          PaymentsOS.validateJsonElement(jsonElement);
          break;
        case "Paymero":
          Paymero.validateJsonElement(jsonElement);
          break;
        case "Payr":
          Payr.validateJsonElement(jsonElement);
          break;
        case "Paysafe":
          Paysafe.validateJsonElement(jsonElement);
          break;
        case "Paysafecash":
          Paysafecash.validateJsonElement(jsonElement);
          break;
        case "Payvision":
          Payvision.validateJsonElement(jsonElement);
          break;
        case "Piastrix":
          Piastrix.validateJsonElement(jsonElement);
          break;
        case "Plugnpay":
          Plugnpay.validateJsonElement(jsonElement);
          break;
        case "PostFinance":
          PostFinance.validateJsonElement(jsonElement);
          break;
        case "Prosa":
          Prosa.validateJsonElement(jsonElement);
          break;
        case "RPN":
          RPN.validateJsonElement(jsonElement);
          break;
        case "Rapyd":
          Rapyd.validateJsonElement(jsonElement);
          break;
        case "Realex":
          Realex.validateJsonElement(jsonElement);
          break;
        case "Realtime":
          Realtime.validateJsonElement(jsonElement);
          break;
        case "Redsys":
          Redsys.validateJsonElement(jsonElement);
          break;
        case "Rotessa":
          Rotessa.validateJsonElement(jsonElement);
          break;
        case "SMSVoucher":
          SMSVoucher.validateJsonElement(jsonElement);
          break;
        case "Sagepay":
          Sagepay.validateJsonElement(jsonElement);
          break;
        case "SaltarPay":
          SaltarPay.validateJsonElement(jsonElement);
          break;
        case "SeamlessChex":
          SeamlessChex.validateJsonElement(jsonElement);
          break;
        case "SecureTrading":
          SecureTrading.validateJsonElement(jsonElement);
          break;
        case "SecurionPay":
          SecurionPay.validateJsonElement(jsonElement);
          break;
        case "Skrill":
          Skrill.validateJsonElement(jsonElement);
          break;
        case "SmartInvoice":
          SmartInvoice.validateJsonElement(jsonElement);
          break;
        case "Sofort":
          Sofort.validateJsonElement(jsonElement);
          break;
        case "SparkPay":
          SparkPay.validateJsonElement(jsonElement);
          break;
        case "StaticGateway":
          StaticGateway.validateJsonElement(jsonElement);
          break;
        case "Stripe":
          Stripe.validateJsonElement(jsonElement);
          break;
        case "TWINT":
          TWINT.validateJsonElement(jsonElement);
          break;
        case "TestProcessor":
          TestProcessor.validateJsonElement(jsonElement);
          break;
        case "ToditoCash":
          ToditoCash.validateJsonElement(jsonElement);
          break;
        case "TrustPay":
          TrustPay.validateJsonElement(jsonElement);
          break;
        case "Trustly":
          Trustly.validateJsonElement(jsonElement);
          break;
        case "TrustsPay":
          TrustsPay.validateJsonElement(jsonElement);
          break;
        case "UPayCard":
          UPayCard.validateJsonElement(jsonElement);
          break;
        case "USAePay":
          USAePay.validateJsonElement(jsonElement);
          break;
        case "VCreditos":
          VCreditos.validateJsonElement(jsonElement);
          break;
        case "VantivLitle":
          VantivLitle.validateJsonElement(jsonElement);
          break;
        case "Wallet88":
          Wallet88.validateJsonElement(jsonElement);
          break;
        case "Walpay":
          Walpay.validateJsonElement(jsonElement);
          break;
        case "Wirecard":
          Wirecard.validateJsonElement(jsonElement);
          break;
        case "WorldlineAtosFrankfurt":
          WorldlineAtosFrankfurt.validateJsonElement(jsonElement);
          break;
        case "Worldpay":
          Worldpay.validateJsonElement(jsonElement);
          break;
        case "XPay":
          XPay.validateJsonElement(jsonElement);
          break;
        case "Zimpler":
          Zimpler.validateJsonElement(jsonElement);
          break;
        case "Zotapay":
          Zotapay.validateJsonElement(jsonElement);
          break;
        case "dLocal":
          DLocal.validateJsonElement(jsonElement);
          break;
        case "eMerchantPay":
          EMerchantPay.validateJsonElement(jsonElement);
          break;
        case "eZeeWallet":
          EZeeWallet.validateJsonElement(jsonElement);
          break;
        case "ecoPayz":
          EcoPayz.validateJsonElement(jsonElement);
          break;
        case "ezyEFT":
          EzyEFT.validateJsonElement(jsonElement);
          break;
        case "iCanPay":
          ICanPay.validateJsonElement(jsonElement);
          break;
        case "iCheque":
          ICheque.validateJsonElement(jsonElement);
          break;
        case "iDebit":
          IDebit.validateJsonElement(jsonElement);
          break;
        case "loonie":
          Loonie.validateJsonElement(jsonElement);
          break;
        case "vegaaH":
          VegaaH.validateJsonElement(jsonElement);
          break;
        default:
          throw new IllegalArgumentException(String.format("The value of the `gatewayName` field `%s` does not match any key defined in the discriminator's mapping.", discriminatorValue));
      }
  }


  /**
   * Create an instance of GatewayAccount given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GatewayAccount
   * @throws IOException if the JSON string is invalid with respect to GatewayAccount
   */
  public static GatewayAccount fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GatewayAccount.class);
  }

  /**
   * Convert an instance of GatewayAccount to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

