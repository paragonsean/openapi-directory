/*
 * POS API
 * Welcome to the POS API.  You can use this API to access all POS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
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
import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CashDetails;
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.PosBankAccount;
import org.openapitools.client.model.PosPaymentCardDetails;
import org.openapitools.client.model.PosPaymentExternalDetails;
import org.openapitools.client.model.PosPaymentProcessingFeesInner;
import org.openapitools.client.model.ServiceCharge;
import org.openapitools.client.model.WalletDetails;
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
 * PosPayment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:35.267625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PosPayment {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_APP_FEE = "app_fee";
  @SerializedName(SERIALIZED_NAME_APP_FEE)
  private BigDecimal appFee;

  public static final String SERIALIZED_NAME_APPROVED = "approved";
  @SerializedName(SERIALIZED_NAME_APPROVED)
  private BigDecimal approved;

  public static final String SERIALIZED_NAME_BANK_ACCOUNT = "bank_account";
  @SerializedName(SERIALIZED_NAME_BANK_ACCOUNT)
  private PosBankAccount bankAccount;

  public static final String SERIALIZED_NAME_CARD_DETAILS = "card_details";
  @SerializedName(SERIALIZED_NAME_CARD_DETAILS)
  private PosPaymentCardDetails cardDetails;

  public static final String SERIALIZED_NAME_CASH = "cash";
  @SerializedName(SERIALIZED_NAME_CASH)
  private CashDetails cash;

  public static final String SERIALIZED_NAME_CHANGE_BACK_CASH_AMOUNT = "change_back_cash_amount";
  @SerializedName(SERIALIZED_NAME_CHANGE_BACK_CASH_AMOUNT)
  private BigDecimal changeBackCashAmount;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private Currency currency;

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customer_id";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_DEVICE_ID = "device_id";
  @SerializedName(SERIALIZED_NAME_DEVICE_ID)
  private String deviceId;

  public static final String SERIALIZED_NAME_EMPLOYEE_ID = "employee_id";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE_ID)
  private String employeeId;

  public static final String SERIALIZED_NAME_EXTERNAL_DETAILS = "external_details";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DETAILS)
  private PosPaymentExternalDetails externalDetails;

  public static final String SERIALIZED_NAME_EXTERNAL_PAYMENT_ID = "external_payment_id";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_PAYMENT_ID)
  private String externalPaymentId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IDEMPOTENCY_KEY = "idempotency_key";
  @SerializedName(SERIALIZED_NAME_IDEMPOTENCY_KEY)
  private String idempotencyKey;

  public static final String SERIALIZED_NAME_LOCATION_ID = "location_id";
  @SerializedName(SERIALIZED_NAME_LOCATION_ID)
  private String locationId;

  public static final String SERIALIZED_NAME_MERCHANT_ID = "merchant_id";
  @SerializedName(SERIALIZED_NAME_MERCHANT_ID)
  private String merchantId;

  public static final String SERIALIZED_NAME_ORDER_ID = "order_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_PROCESSING_FEES = "processing_fees";
  @SerializedName(SERIALIZED_NAME_PROCESSING_FEES)
  private List<PosPaymentProcessingFeesInner> processingFees = new ArrayList<>();

  public static final String SERIALIZED_NAME_REFUNDED = "refunded";
  @SerializedName(SERIALIZED_NAME_REFUNDED)
  private BigDecimal refunded;

  public static final String SERIALIZED_NAME_SERVICE_CHARGES = "service_charges";
  @SerializedName(SERIALIZED_NAME_SERVICE_CHARGES)
  private List<ServiceCharge> serviceCharges = new ArrayList<>();

  /**
   * Source of this payment.
   */
  @JsonAdapter(SourceEnum.Adapter.class)
  public enum SourceEnum {
    CARD("card"),
    
    BANK_ACCOUNT("bank_account"),
    
    WALLET("wallet"),
    
    BNPL("bnpl"),
    
    CASH("cash"),
    
    EXTERNAL("external"),
    
    OTHER("other");

    private String value;

    SourceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SourceEnum fromValue(String value) {
      for (SourceEnum b : SourceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SourceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SourceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SourceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SourceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SourceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private SourceEnum source;

  public static final String SERIALIZED_NAME_SOURCE_ID = "source_id";
  @SerializedName(SERIALIZED_NAME_SOURCE_ID)
  private String sourceId;

  /**
   * Status of this payment.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    APPROVED("approved"),
    
    PENDING("pending"),
    
    COMPLETED("completed"),
    
    CANCELED("canceled"),
    
    FAILED("failed"),
    
    OTHER("other");

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

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private BigDecimal tax;

  public static final String SERIALIZED_NAME_TENDER_ID = "tender_id";
  @SerializedName(SERIALIZED_NAME_TENDER_ID)
  private String tenderId;

  public static final String SERIALIZED_NAME_TIP = "tip";
  @SerializedName(SERIALIZED_NAME_TIP)
  private BigDecimal tip;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private BigDecimal total;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_WALLET = "wallet";
  @SerializedName(SERIALIZED_NAME_WALLET)
  private WalletDetails wallet;

  public PosPayment() {
  }

  public PosPayment(
     OffsetDateTime createdAt, 
     String createdBy, 
     String id, 
     OffsetDateTime updatedAt, 
     String updatedBy
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.id = id;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
  }

  public PosPayment amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Get amount
   * @return amount
   */
  @javax.annotation.Nonnull
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public PosPayment appFee(BigDecimal appFee) {
    this.appFee = appFee;
    return this;
  }

  /**
   * The amount the developer is taking as a fee for facilitating the payment on behalf of the seller.
   * @return appFee
   */
  @javax.annotation.Nullable
  public BigDecimal getAppFee() {
    return appFee;
  }

  public void setAppFee(BigDecimal appFee) {
    this.appFee = appFee;
  }


  public PosPayment approved(BigDecimal approved) {
    this.approved = approved;
    return this;
  }

  /**
   * The initial amount of money approved for this payment.
   * @return approved
   */
  @javax.annotation.Nullable
  public BigDecimal getApproved() {
    return approved;
  }

  public void setApproved(BigDecimal approved) {
    this.approved = approved;
  }


  public PosPayment bankAccount(PosBankAccount bankAccount) {
    this.bankAccount = bankAccount;
    return this;
  }

  /**
   * Get bankAccount
   * @return bankAccount
   */
  @javax.annotation.Nullable
  public PosBankAccount getBankAccount() {
    return bankAccount;
  }

  public void setBankAccount(PosBankAccount bankAccount) {
    this.bankAccount = bankAccount;
  }


  public PosPayment cardDetails(PosPaymentCardDetails cardDetails) {
    this.cardDetails = cardDetails;
    return this;
  }

  /**
   * Get cardDetails
   * @return cardDetails
   */
  @javax.annotation.Nullable
  public PosPaymentCardDetails getCardDetails() {
    return cardDetails;
  }

  public void setCardDetails(PosPaymentCardDetails cardDetails) {
    this.cardDetails = cardDetails;
  }


  public PosPayment cash(CashDetails cash) {
    this.cash = cash;
    return this;
  }

  /**
   * Get cash
   * @return cash
   */
  @javax.annotation.Nullable
  public CashDetails getCash() {
    return cash;
  }

  public void setCash(CashDetails cash) {
    this.cash = cash;
  }


  public PosPayment changeBackCashAmount(BigDecimal changeBackCashAmount) {
    this.changeBackCashAmount = changeBackCashAmount;
    return this;
  }

  /**
   * Get changeBackCashAmount
   * @return changeBackCashAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getChangeBackCashAmount() {
    return changeBackCashAmount;
  }

  public void setChangeBackCashAmount(BigDecimal changeBackCashAmount) {
    this.changeBackCashAmount = changeBackCashAmount;
  }


  /**
   * The date and time when the object was created.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



  /**
   * The user who created the object.
   * @return createdBy
   */
  @javax.annotation.Nullable
  public String getCreatedBy() {
    return createdBy;
  }



  public PosPayment currency(Currency currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Get currency
   * @return currency
   */
  @javax.annotation.Nullable
  public Currency getCurrency() {
    return currency;
  }

  public void setCurrency(Currency currency) {
    this.currency = currency;
  }


  public PosPayment customMappings(Object customMappings) {
    this.customMappings = customMappings;
    return this;
  }

  /**
   * When custom mappings are configured on the resource, the result is included here.
   * @return customMappings
   */
  @javax.annotation.Nullable
  public Object getCustomMappings() {
    return customMappings;
  }

  public void setCustomMappings(Object customMappings) {
    this.customMappings = customMappings;
  }


  public PosPayment customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * Get customerId
   * @return customerId
   */
  @javax.annotation.Nonnull
  public String getCustomerId() {
    return customerId;
  }

  public void setCustomerId(String customerId) {
    this.customerId = customerId;
  }


  public PosPayment deviceId(String deviceId) {
    this.deviceId = deviceId;
    return this;
  }

  /**
   * Get deviceId
   * @return deviceId
   */
  @javax.annotation.Nullable
  public String getDeviceId() {
    return deviceId;
  }

  public void setDeviceId(String deviceId) {
    this.deviceId = deviceId;
  }


  public PosPayment employeeId(String employeeId) {
    this.employeeId = employeeId;
    return this;
  }

  /**
   * Get employeeId
   * @return employeeId
   */
  @javax.annotation.Nullable
  public String getEmployeeId() {
    return employeeId;
  }

  public void setEmployeeId(String employeeId) {
    this.employeeId = employeeId;
  }


  public PosPayment externalDetails(PosPaymentExternalDetails externalDetails) {
    this.externalDetails = externalDetails;
    return this;
  }

  /**
   * Get externalDetails
   * @return externalDetails
   */
  @javax.annotation.Nullable
  public PosPaymentExternalDetails getExternalDetails() {
    return externalDetails;
  }

  public void setExternalDetails(PosPaymentExternalDetails externalDetails) {
    this.externalDetails = externalDetails;
  }


  public PosPayment externalPaymentId(String externalPaymentId) {
    this.externalPaymentId = externalPaymentId;
    return this;
  }

  /**
   * Get externalPaymentId
   * @return externalPaymentId
   */
  @javax.annotation.Nullable
  public String getExternalPaymentId() {
    return externalPaymentId;
  }

  public void setExternalPaymentId(String externalPaymentId) {
    this.externalPaymentId = externalPaymentId;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public PosPayment idempotencyKey(String idempotencyKey) {
    this.idempotencyKey = idempotencyKey;
    return this;
  }

  /**
   * A value you specify that uniquely identifies this request among requests you have sent.
   * @return idempotencyKey
   */
  @javax.annotation.Nullable
  public String getIdempotencyKey() {
    return idempotencyKey;
  }

  public void setIdempotencyKey(String idempotencyKey) {
    this.idempotencyKey = idempotencyKey;
  }


  public PosPayment locationId(String locationId) {
    this.locationId = locationId;
    return this;
  }

  /**
   * Get locationId
   * @return locationId
   */
  @javax.annotation.Nullable
  public String getLocationId() {
    return locationId;
  }

  public void setLocationId(String locationId) {
    this.locationId = locationId;
  }


  public PosPayment merchantId(String merchantId) {
    this.merchantId = merchantId;
    return this;
  }

  /**
   * Get merchantId
   * @return merchantId
   */
  @javax.annotation.Nullable
  public String getMerchantId() {
    return merchantId;
  }

  public void setMerchantId(String merchantId) {
    this.merchantId = merchantId;
  }


  public PosPayment orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * Get orderId
   * @return orderId
   */
  @javax.annotation.Nonnull
  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  public PosPayment processingFees(List<PosPaymentProcessingFeesInner> processingFees) {
    this.processingFees = processingFees;
    return this;
  }

  public PosPayment addProcessingFeesItem(PosPaymentProcessingFeesInner processingFeesItem) {
    if (this.processingFees == null) {
      this.processingFees = new ArrayList<>();
    }
    this.processingFees.add(processingFeesItem);
    return this;
  }

  /**
   * Get processingFees
   * @return processingFees
   */
  @javax.annotation.Nullable
  public List<PosPaymentProcessingFeesInner> getProcessingFees() {
    return processingFees;
  }

  public void setProcessingFees(List<PosPaymentProcessingFeesInner> processingFees) {
    this.processingFees = processingFees;
  }


  public PosPayment refunded(BigDecimal refunded) {
    this.refunded = refunded;
    return this;
  }

  /**
   * The initial amount of money approved for this payment.
   * @return refunded
   */
  @javax.annotation.Nullable
  public BigDecimal getRefunded() {
    return refunded;
  }

  public void setRefunded(BigDecimal refunded) {
    this.refunded = refunded;
  }


  public PosPayment serviceCharges(List<ServiceCharge> serviceCharges) {
    this.serviceCharges = serviceCharges;
    return this;
  }

  public PosPayment addServiceChargesItem(ServiceCharge serviceChargesItem) {
    if (this.serviceCharges == null) {
      this.serviceCharges = new ArrayList<>();
    }
    this.serviceCharges.add(serviceChargesItem);
    return this;
  }

  /**
   * Optional service charges or gratuity tip applied to the order.
   * @return serviceCharges
   */
  @javax.annotation.Nullable
  public List<ServiceCharge> getServiceCharges() {
    return serviceCharges;
  }

  public void setServiceCharges(List<ServiceCharge> serviceCharges) {
    this.serviceCharges = serviceCharges;
  }


  public PosPayment source(SourceEnum source) {
    this.source = source;
    return this;
  }

  /**
   * Source of this payment.
   * @return source
   */
  @javax.annotation.Nullable
  public SourceEnum getSource() {
    return source;
  }

  public void setSource(SourceEnum source) {
    this.source = source;
  }


  public PosPayment sourceId(String sourceId) {
    this.sourceId = sourceId;
    return this;
  }

  /**
   * The ID for the source of funds for this payment. Square-only: This can be a payment token (card nonce) generated by the payment form or a card on file made linked to the customer. if recording a payment that the seller received outside of Square, specify either &#x60;CASH&#x60; or &#x60;EXTERNAL&#x60;.
   * @return sourceId
   */
  @javax.annotation.Nonnull
  public String getSourceId() {
    return sourceId;
  }

  public void setSourceId(String sourceId) {
    this.sourceId = sourceId;
  }


  public PosPayment status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Status of this payment.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public PosPayment tax(BigDecimal tax) {
    this.tax = tax;
    return this;
  }

  /**
   * Get tax
   * @return tax
   */
  @javax.annotation.Nullable
  public BigDecimal getTax() {
    return tax;
  }

  public void setTax(BigDecimal tax) {
    this.tax = tax;
  }


  public PosPayment tenderId(String tenderId) {
    this.tenderId = tenderId;
    return this;
  }

  /**
   * Get tenderId
   * @return tenderId
   */
  @javax.annotation.Nonnull
  public String getTenderId() {
    return tenderId;
  }

  public void setTenderId(String tenderId) {
    this.tenderId = tenderId;
  }


  public PosPayment tip(BigDecimal tip) {
    this.tip = tip;
    return this;
  }

  /**
   * Get tip
   * @return tip
   */
  @javax.annotation.Nullable
  public BigDecimal getTip() {
    return tip;
  }

  public void setTip(BigDecimal tip) {
    this.tip = tip;
  }


  public PosPayment total(BigDecimal total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public BigDecimal getTotal() {
    return total;
  }

  public void setTotal(BigDecimal total) {
    this.total = total;
  }


  /**
   * The date and time when the object was last updated.
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }



  /**
   * The user who last updated the object.
   * @return updatedBy
   */
  @javax.annotation.Nullable
  public String getUpdatedBy() {
    return updatedBy;
  }



  public PosPayment wallet(WalletDetails wallet) {
    this.wallet = wallet;
    return this;
  }

  /**
   * Get wallet
   * @return wallet
   */
  @javax.annotation.Nullable
  public WalletDetails getWallet() {
    return wallet;
  }

  public void setWallet(WalletDetails wallet) {
    this.wallet = wallet;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PosPayment posPayment = (PosPayment) o;
    return Objects.equals(this.amount, posPayment.amount) &&
        Objects.equals(this.appFee, posPayment.appFee) &&
        Objects.equals(this.approved, posPayment.approved) &&
        Objects.equals(this.bankAccount, posPayment.bankAccount) &&
        Objects.equals(this.cardDetails, posPayment.cardDetails) &&
        Objects.equals(this.cash, posPayment.cash) &&
        Objects.equals(this.changeBackCashAmount, posPayment.changeBackCashAmount) &&
        Objects.equals(this.createdAt, posPayment.createdAt) &&
        Objects.equals(this.createdBy, posPayment.createdBy) &&
        Objects.equals(this.currency, posPayment.currency) &&
        Objects.equals(this.customMappings, posPayment.customMappings) &&
        Objects.equals(this.customerId, posPayment.customerId) &&
        Objects.equals(this.deviceId, posPayment.deviceId) &&
        Objects.equals(this.employeeId, posPayment.employeeId) &&
        Objects.equals(this.externalDetails, posPayment.externalDetails) &&
        Objects.equals(this.externalPaymentId, posPayment.externalPaymentId) &&
        Objects.equals(this.id, posPayment.id) &&
        Objects.equals(this.idempotencyKey, posPayment.idempotencyKey) &&
        Objects.equals(this.locationId, posPayment.locationId) &&
        Objects.equals(this.merchantId, posPayment.merchantId) &&
        Objects.equals(this.orderId, posPayment.orderId) &&
        Objects.equals(this.processingFees, posPayment.processingFees) &&
        Objects.equals(this.refunded, posPayment.refunded) &&
        Objects.equals(this.serviceCharges, posPayment.serviceCharges) &&
        Objects.equals(this.source, posPayment.source) &&
        Objects.equals(this.sourceId, posPayment.sourceId) &&
        Objects.equals(this.status, posPayment.status) &&
        Objects.equals(this.tax, posPayment.tax) &&
        Objects.equals(this.tenderId, posPayment.tenderId) &&
        Objects.equals(this.tip, posPayment.tip) &&
        Objects.equals(this.total, posPayment.total) &&
        Objects.equals(this.updatedAt, posPayment.updatedAt) &&
        Objects.equals(this.updatedBy, posPayment.updatedBy) &&
        Objects.equals(this.wallet, posPayment.wallet);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, appFee, approved, bankAccount, cardDetails, cash, changeBackCashAmount, createdAt, createdBy, currency, customMappings, customerId, deviceId, employeeId, externalDetails, externalPaymentId, id, idempotencyKey, locationId, merchantId, orderId, processingFees, refunded, serviceCharges, source, sourceId, status, tax, tenderId, tip, total, updatedAt, updatedBy, wallet);
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
    sb.append("class PosPayment {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    appFee: ").append(toIndentedString(appFee)).append("\n");
    sb.append("    approved: ").append(toIndentedString(approved)).append("\n");
    sb.append("    bankAccount: ").append(toIndentedString(bankAccount)).append("\n");
    sb.append("    cardDetails: ").append(toIndentedString(cardDetails)).append("\n");
    sb.append("    cash: ").append(toIndentedString(cash)).append("\n");
    sb.append("    changeBackCashAmount: ").append(toIndentedString(changeBackCashAmount)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    deviceId: ").append(toIndentedString(deviceId)).append("\n");
    sb.append("    employeeId: ").append(toIndentedString(employeeId)).append("\n");
    sb.append("    externalDetails: ").append(toIndentedString(externalDetails)).append("\n");
    sb.append("    externalPaymentId: ").append(toIndentedString(externalPaymentId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    idempotencyKey: ").append(toIndentedString(idempotencyKey)).append("\n");
    sb.append("    locationId: ").append(toIndentedString(locationId)).append("\n");
    sb.append("    merchantId: ").append(toIndentedString(merchantId)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    processingFees: ").append(toIndentedString(processingFees)).append("\n");
    sb.append("    refunded: ").append(toIndentedString(refunded)).append("\n");
    sb.append("    serviceCharges: ").append(toIndentedString(serviceCharges)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    sourceId: ").append(toIndentedString(sourceId)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    tenderId: ").append(toIndentedString(tenderId)).append("\n");
    sb.append("    tip: ").append(toIndentedString(tip)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    wallet: ").append(toIndentedString(wallet)).append("\n");
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
    openapiFields.add("app_fee");
    openapiFields.add("approved");
    openapiFields.add("bank_account");
    openapiFields.add("card_details");
    openapiFields.add("cash");
    openapiFields.add("change_back_cash_amount");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("currency");
    openapiFields.add("custom_mappings");
    openapiFields.add("customer_id");
    openapiFields.add("device_id");
    openapiFields.add("employee_id");
    openapiFields.add("external_details");
    openapiFields.add("external_payment_id");
    openapiFields.add("id");
    openapiFields.add("idempotency_key");
    openapiFields.add("location_id");
    openapiFields.add("merchant_id");
    openapiFields.add("order_id");
    openapiFields.add("processing_fees");
    openapiFields.add("refunded");
    openapiFields.add("service_charges");
    openapiFields.add("source");
    openapiFields.add("source_id");
    openapiFields.add("status");
    openapiFields.add("tax");
    openapiFields.add("tender_id");
    openapiFields.add("tip");
    openapiFields.add("total");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("wallet");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("amount");
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("customer_id");
    openapiRequiredFields.add("order_id");
    openapiRequiredFields.add("source_id");
    openapiRequiredFields.add("tender_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PosPayment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PosPayment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PosPayment is not found in the empty JSON string", PosPayment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PosPayment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PosPayment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PosPayment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `bank_account`
      if (jsonObj.get("bank_account") != null && !jsonObj.get("bank_account").isJsonNull()) {
        PosBankAccount.validateJsonElement(jsonObj.get("bank_account"));
      }
      // validate the optional field `card_details`
      if (jsonObj.get("card_details") != null && !jsonObj.get("card_details").isJsonNull()) {
        PosPaymentCardDetails.validateJsonElement(jsonObj.get("card_details"));
      }
      // validate the optional field `cash`
      if (jsonObj.get("cash") != null && !jsonObj.get("cash").isJsonNull()) {
        CashDetails.validateJsonElement(jsonObj.get("cash"));
      }
      if ((jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) && !jsonObj.get("created_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by").toString()));
      }
      // validate the required field `currency`
      Currency.validateJsonElement(jsonObj.get("currency"));
      if (!jsonObj.get("customer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customer_id").toString()));
      }
      if ((jsonObj.get("device_id") != null && !jsonObj.get("device_id").isJsonNull()) && !jsonObj.get("device_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `device_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("device_id").toString()));
      }
      if ((jsonObj.get("employee_id") != null && !jsonObj.get("employee_id").isJsonNull()) && !jsonObj.get("employee_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employee_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employee_id").toString()));
      }
      // validate the optional field `external_details`
      if (jsonObj.get("external_details") != null && !jsonObj.get("external_details").isJsonNull()) {
        PosPaymentExternalDetails.validateJsonElement(jsonObj.get("external_details"));
      }
      if ((jsonObj.get("external_payment_id") != null && !jsonObj.get("external_payment_id").isJsonNull()) && !jsonObj.get("external_payment_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `external_payment_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("external_payment_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("idempotency_key") != null && !jsonObj.get("idempotency_key").isJsonNull()) && !jsonObj.get("idempotency_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `idempotency_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("idempotency_key").toString()));
      }
      if ((jsonObj.get("location_id") != null && !jsonObj.get("location_id").isJsonNull()) && !jsonObj.get("location_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location_id").toString()));
      }
      if ((jsonObj.get("merchant_id") != null && !jsonObj.get("merchant_id").isJsonNull()) && !jsonObj.get("merchant_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchant_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchant_id").toString()));
      }
      if (!jsonObj.get("order_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_id").toString()));
      }
      if (jsonObj.get("processing_fees") != null && !jsonObj.get("processing_fees").isJsonNull()) {
        JsonArray jsonArrayprocessingFees = jsonObj.getAsJsonArray("processing_fees");
        if (jsonArrayprocessingFees != null) {
          // ensure the json data is an array
          if (!jsonObj.get("processing_fees").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `processing_fees` to be an array in the JSON string but got `%s`", jsonObj.get("processing_fees").toString()));
          }

          // validate the optional field `processing_fees` (array)
          for (int i = 0; i < jsonArrayprocessingFees.size(); i++) {
            PosPaymentProcessingFeesInner.validateJsonElement(jsonArrayprocessingFees.get(i));
          };
        }
      }
      if (jsonObj.get("service_charges") != null && !jsonObj.get("service_charges").isJsonNull()) {
        JsonArray jsonArrayserviceCharges = jsonObj.getAsJsonArray("service_charges");
        if (jsonArrayserviceCharges != null) {
          // ensure the json data is an array
          if (!jsonObj.get("service_charges").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `service_charges` to be an array in the JSON string but got `%s`", jsonObj.get("service_charges").toString()));
          }

          // validate the optional field `service_charges` (array)
          for (int i = 0; i < jsonArrayserviceCharges.size(); i++) {
            ServiceCharge.validateJsonElement(jsonArrayserviceCharges.get(i));
          };
        }
      }
      if ((jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) && !jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      // validate the optional field `source`
      if (jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) {
        SourceEnum.validateJsonElement(jsonObj.get("source"));
      }
      if (!jsonObj.get("source_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_id").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if (!jsonObj.get("tender_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tender_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tender_id").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
      // validate the optional field `wallet`
      if (jsonObj.get("wallet") != null && !jsonObj.get("wallet").isJsonNull()) {
        WalletDetails.validateJsonElement(jsonObj.get("wallet"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PosPayment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PosPayment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PosPayment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PosPayment.class));

       return (TypeAdapter<T>) new TypeAdapter<PosPayment>() {
           @Override
           public void write(JsonWriter out, PosPayment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PosPayment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PosPayment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PosPayment
   * @throws IOException if the JSON string is invalid with respect to PosPayment
   */
  public static PosPayment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PosPayment.class);
  }

  /**
   * Convert an instance of PosPayment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

