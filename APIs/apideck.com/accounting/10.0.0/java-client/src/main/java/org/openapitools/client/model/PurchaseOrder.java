/*
 * Accounting API
 * Welcome to the Accounting API.  You can use this API to access all Accounting API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Address;
import org.openapitools.client.model.BankAccount;
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.InvoiceLineItem;
import org.openapitools.client.model.LinkedLedgerAccount;
import org.openapitools.client.model.LinkedSupplier;
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
 * PurchaseOrder
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:31.900974-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PurchaseOrder {
  public static final String SERIALIZED_NAME_ACCOUNTING_BY_ROW = "accounting_by_row";
  @SerializedName(SERIALIZED_NAME_ACCOUNTING_BY_ROW)
  private Boolean accountingByRow;

  public static final String SERIALIZED_NAME_BANK_ACCOUNT = "bank_account";
  @SerializedName(SERIALIZED_NAME_BANK_ACCOUNT)
  private BankAccount bankAccount;

  public static final String SERIALIZED_NAME_CHANNEL = "channel";
  @SerializedName(SERIALIZED_NAME_CHANNEL)
  private String channel;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private Currency currency;

  public static final String SERIALIZED_NAME_CURRENCY_RATE = "currency_rate";
  @SerializedName(SERIALIZED_NAME_CURRENCY_RATE)
  private BigDecimal currencyRate;

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_DELIVERY_DATE = "delivery_date";
  @SerializedName(SERIALIZED_NAME_DELIVERY_DATE)
  private LocalDate deliveryDate;

  public static final String SERIALIZED_NAME_DISCOUNT_PERCENTAGE = "discount_percentage";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_PERCENTAGE)
  private BigDecimal discountPercentage;

  public static final String SERIALIZED_NAME_DOWNSTREAM_ID = "downstream_id";
  @SerializedName(SERIALIZED_NAME_DOWNSTREAM_ID)
  private String downstreamId;

  public static final String SERIALIZED_NAME_DUE_DATE = "due_date";
  @SerializedName(SERIALIZED_NAME_DUE_DATE)
  private LocalDate dueDate;

  public static final String SERIALIZED_NAME_EXPECTED_ARRIVAL_DATE = "expected_arrival_date";
  @SerializedName(SERIALIZED_NAME_EXPECTED_ARRIVAL_DATE)
  private LocalDate expectedArrivalDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_ISSUED_DATE = "issued_date";
  @SerializedName(SERIALIZED_NAME_ISSUED_DATE)
  private LocalDate issuedDate;

  public static final String SERIALIZED_NAME_LEDGER_ACCOUNT = "ledger_account";
  @SerializedName(SERIALIZED_NAME_LEDGER_ACCOUNT)
  private LinkedLedgerAccount ledgerAccount;

  public static final String SERIALIZED_NAME_LINE_ITEMS = "line_items";
  @SerializedName(SERIALIZED_NAME_LINE_ITEMS)
  private List<InvoiceLineItem> lineItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_MEMO = "memo";
  @SerializedName(SERIALIZED_NAME_MEMO)
  private String memo;

  public static final String SERIALIZED_NAME_PAYMENT_METHOD = "payment_method";
  @SerializedName(SERIALIZED_NAME_PAYMENT_METHOD)
  private String paymentMethod;

  public static final String SERIALIZED_NAME_PO_NUMBER = "po_number";
  @SerializedName(SERIALIZED_NAME_PO_NUMBER)
  private String poNumber;

  public static final String SERIALIZED_NAME_REFERENCE = "reference";
  @SerializedName(SERIALIZED_NAME_REFERENCE)
  private String reference;

  public static final String SERIALIZED_NAME_ROW_VERSION = "row_version";
  @SerializedName(SERIALIZED_NAME_ROW_VERSION)
  private String rowVersion;

  public static final String SERIALIZED_NAME_SHIPPING_ADDRESS = "shipping_address";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ADDRESS)
  private Address shippingAddress;

  /**
   * Gets or Sets status
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    DRAFT("draft"),
    
    OPEN("open"),
    
    CLOSED("closed"),
    
    DELETED("deleted"),
    
    BILLED("billed"),
    
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
      return null;
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

  public static final String SERIALIZED_NAME_SUB_TOTAL = "sub_total";
  @SerializedName(SERIALIZED_NAME_SUB_TOTAL)
  private BigDecimal subTotal;

  public static final String SERIALIZED_NAME_SUPPLIER = "supplier";
  @SerializedName(SERIALIZED_NAME_SUPPLIER)
  private LinkedSupplier supplier;

  public static final String SERIALIZED_NAME_TAX_CODE = "tax_code";
  @SerializedName(SERIALIZED_NAME_TAX_CODE)
  private String taxCode;

  public static final String SERIALIZED_NAME_TAX_INCLUSIVE = "tax_inclusive";
  @SerializedName(SERIALIZED_NAME_TAX_INCLUSIVE)
  private Boolean taxInclusive;

  public static final String SERIALIZED_NAME_TEMPLATE_ID = "template_id";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_ID)
  private String templateId;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private BigDecimal total;

  public static final String SERIALIZED_NAME_TOTAL_TAX = "total_tax";
  @SerializedName(SERIALIZED_NAME_TOTAL_TAX)
  private BigDecimal totalTax;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public PurchaseOrder() {
  }

  public PurchaseOrder(
     OffsetDateTime createdAt, 
     String createdBy, 
     String downstreamId, 
     String id, 
     OffsetDateTime updatedAt, 
     String updatedBy
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.downstreamId = downstreamId;
    this.id = id;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
  }

  public PurchaseOrder accountingByRow(Boolean accountingByRow) {
    this.accountingByRow = accountingByRow;
    return this;
  }

  /**
   * Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.
   * @return accountingByRow
   */
  @javax.annotation.Nullable
  public Boolean getAccountingByRow() {
    return accountingByRow;
  }

  public void setAccountingByRow(Boolean accountingByRow) {
    this.accountingByRow = accountingByRow;
  }


  public PurchaseOrder bankAccount(BankAccount bankAccount) {
    this.bankAccount = bankAccount;
    return this;
  }

  /**
   * Get bankAccount
   * @return bankAccount
   */
  @javax.annotation.Nullable
  public BankAccount getBankAccount() {
    return bankAccount;
  }

  public void setBankAccount(BankAccount bankAccount) {
    this.bankAccount = bankAccount;
  }


  public PurchaseOrder channel(String channel) {
    this.channel = channel;
    return this;
  }

  /**
   * The channel through which the transaction is processed.
   * @return channel
   */
  @javax.annotation.Nullable
  public String getChannel() {
    return channel;
  }

  public void setChannel(String channel) {
    this.channel = channel;
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



  public PurchaseOrder currency(Currency currency) {
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


  public PurchaseOrder currencyRate(BigDecimal currencyRate) {
    this.currencyRate = currencyRate;
    return this;
  }

  /**
   * Currency Exchange Rate at the time entity was recorded/generated.
   * @return currencyRate
   */
  @javax.annotation.Nullable
  public BigDecimal getCurrencyRate() {
    return currencyRate;
  }

  public void setCurrencyRate(BigDecimal currencyRate) {
    this.currencyRate = currencyRate;
  }


  public PurchaseOrder customMappings(Object customMappings) {
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


  public PurchaseOrder deliveryDate(LocalDate deliveryDate) {
    this.deliveryDate = deliveryDate;
    return this;
  }

  /**
   * The date on which the purchase order is to be delivered - YYYY-MM-DD.
   * @return deliveryDate
   */
  @javax.annotation.Nullable
  public LocalDate getDeliveryDate() {
    return deliveryDate;
  }

  public void setDeliveryDate(LocalDate deliveryDate) {
    this.deliveryDate = deliveryDate;
  }


  public PurchaseOrder discountPercentage(BigDecimal discountPercentage) {
    this.discountPercentage = discountPercentage;
    return this;
  }

  /**
   * Discount percentage applied to this transaction.
   * @return discountPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getDiscountPercentage() {
    return discountPercentage;
  }

  public void setDiscountPercentage(BigDecimal discountPercentage) {
    this.discountPercentage = discountPercentage;
  }


  /**
   * The third-party API ID of original entity
   * @return downstreamId
   */
  @javax.annotation.Nullable
  public String getDownstreamId() {
    return downstreamId;
  }



  public PurchaseOrder dueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
    return this;
  }

  /**
   * The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD.
   * @return dueDate
   */
  @javax.annotation.Nullable
  public LocalDate getDueDate() {
    return dueDate;
  }

  public void setDueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
  }


  public PurchaseOrder expectedArrivalDate(LocalDate expectedArrivalDate) {
    this.expectedArrivalDate = expectedArrivalDate;
    return this;
  }

  /**
   * The date on which the order is expected to arrive - YYYY-MM-DD.
   * @return expectedArrivalDate
   */
  @javax.annotation.Nullable
  public LocalDate getExpectedArrivalDate() {
    return expectedArrivalDate;
  }

  public void setExpectedArrivalDate(LocalDate expectedArrivalDate) {
    this.expectedArrivalDate = expectedArrivalDate;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public PurchaseOrder issuedDate(LocalDate issuedDate) {
    this.issuedDate = issuedDate;
    return this;
  }

  /**
   * Date purchase order was issued - YYYY-MM-DD.
   * @return issuedDate
   */
  @javax.annotation.Nullable
  public LocalDate getIssuedDate() {
    return issuedDate;
  }

  public void setIssuedDate(LocalDate issuedDate) {
    this.issuedDate = issuedDate;
  }


  public PurchaseOrder ledgerAccount(LinkedLedgerAccount ledgerAccount) {
    this.ledgerAccount = ledgerAccount;
    return this;
  }

  /**
   * Get ledgerAccount
   * @return ledgerAccount
   */
  @javax.annotation.Nullable
  public LinkedLedgerAccount getLedgerAccount() {
    return ledgerAccount;
  }

  public void setLedgerAccount(LinkedLedgerAccount ledgerAccount) {
    this.ledgerAccount = ledgerAccount;
  }


  public PurchaseOrder lineItems(List<InvoiceLineItem> lineItems) {
    this.lineItems = lineItems;
    return this;
  }

  public PurchaseOrder addLineItemsItem(InvoiceLineItem lineItemsItem) {
    if (this.lineItems == null) {
      this.lineItems = new ArrayList<>();
    }
    this.lineItems.add(lineItemsItem);
    return this;
  }

  /**
   * Get lineItems
   * @return lineItems
   */
  @javax.annotation.Nullable
  public List<InvoiceLineItem> getLineItems() {
    return lineItems;
  }

  public void setLineItems(List<InvoiceLineItem> lineItems) {
    this.lineItems = lineItems;
  }


  public PurchaseOrder memo(String memo) {
    this.memo = memo;
    return this;
  }

  /**
   * Message for the supplier. This text appears on the Purchase Order.
   * @return memo
   */
  @javax.annotation.Nullable
  public String getMemo() {
    return memo;
  }

  public void setMemo(String memo) {
    this.memo = memo;
  }


  public PurchaseOrder paymentMethod(String paymentMethod) {
    this.paymentMethod = paymentMethod;
    return this;
  }

  /**
   * Payment method used for the transaction, such as cash, credit card, bank transfer, or check
   * @return paymentMethod
   */
  @javax.annotation.Nullable
  public String getPaymentMethod() {
    return paymentMethod;
  }

  public void setPaymentMethod(String paymentMethod) {
    this.paymentMethod = paymentMethod;
  }


  public PurchaseOrder poNumber(String poNumber) {
    this.poNumber = poNumber;
    return this;
  }

  /**
   * A PO Number uniquely identifies a purchase order and is generally defined by the buyer.
   * @return poNumber
   */
  @javax.annotation.Nullable
  public String getPoNumber() {
    return poNumber;
  }

  public void setPoNumber(String poNumber) {
    this.poNumber = poNumber;
  }


  public PurchaseOrder reference(String reference) {
    this.reference = reference;
    return this;
  }

  /**
   * Optional purchase order reference.
   * @return reference
   */
  @javax.annotation.Nullable
  public String getReference() {
    return reference;
  }

  public void setReference(String reference) {
    this.reference = reference;
  }


  public PurchaseOrder rowVersion(String rowVersion) {
    this.rowVersion = rowVersion;
    return this;
  }

  /**
   * A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.
   * @return rowVersion
   */
  @javax.annotation.Nullable
  public String getRowVersion() {
    return rowVersion;
  }

  public void setRowVersion(String rowVersion) {
    this.rowVersion = rowVersion;
  }


  public PurchaseOrder shippingAddress(Address shippingAddress) {
    this.shippingAddress = shippingAddress;
    return this;
  }

  /**
   * Get shippingAddress
   * @return shippingAddress
   */
  @javax.annotation.Nullable
  public Address getShippingAddress() {
    return shippingAddress;
  }

  public void setShippingAddress(Address shippingAddress) {
    this.shippingAddress = shippingAddress;
  }


  public PurchaseOrder status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public PurchaseOrder subTotal(BigDecimal subTotal) {
    this.subTotal = subTotal;
    return this;
  }

  /**
   * Sub-total amount, normally before tax.
   * @return subTotal
   */
  @javax.annotation.Nullable
  public BigDecimal getSubTotal() {
    return subTotal;
  }

  public void setSubTotal(BigDecimal subTotal) {
    this.subTotal = subTotal;
  }


  public PurchaseOrder supplier(LinkedSupplier supplier) {
    this.supplier = supplier;
    return this;
  }

  /**
   * Get supplier
   * @return supplier
   */
  @javax.annotation.Nullable
  public LinkedSupplier getSupplier() {
    return supplier;
  }

  public void setSupplier(LinkedSupplier supplier) {
    this.supplier = supplier;
  }


  public PurchaseOrder taxCode(String taxCode) {
    this.taxCode = taxCode;
    return this;
  }

  /**
   * Applicable tax id/code override if tax is not supplied on a line item basis.
   * @return taxCode
   */
  @javax.annotation.Nullable
  public String getTaxCode() {
    return taxCode;
  }

  public void setTaxCode(String taxCode) {
    this.taxCode = taxCode;
  }


  public PurchaseOrder taxInclusive(Boolean taxInclusive) {
    this.taxInclusive = taxInclusive;
    return this;
  }

  /**
   * Amounts are including tax
   * @return taxInclusive
   */
  @javax.annotation.Nullable
  public Boolean getTaxInclusive() {
    return taxInclusive;
  }

  public void setTaxInclusive(Boolean taxInclusive) {
    this.taxInclusive = taxInclusive;
  }


  public PurchaseOrder templateId(String templateId) {
    this.templateId = templateId;
    return this;
  }

  /**
   * Optional purchase order template
   * @return templateId
   */
  @javax.annotation.Nullable
  public String getTemplateId() {
    return templateId;
  }

  public void setTemplateId(String templateId) {
    this.templateId = templateId;
  }


  public PurchaseOrder total(BigDecimal total) {
    this.total = total;
    return this;
  }

  /**
   * Total amount of invoice, including tax.
   * @return total
   */
  @javax.annotation.Nullable
  public BigDecimal getTotal() {
    return total;
  }

  public void setTotal(BigDecimal total) {
    this.total = total;
  }


  public PurchaseOrder totalTax(BigDecimal totalTax) {
    this.totalTax = totalTax;
    return this;
  }

  /**
   * Total tax amount applied to this invoice.
   * @return totalTax
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalTax() {
    return totalTax;
  }

  public void setTotalTax(BigDecimal totalTax) {
    this.totalTax = totalTax;
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




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PurchaseOrder purchaseOrder = (PurchaseOrder) o;
    return Objects.equals(this.accountingByRow, purchaseOrder.accountingByRow) &&
        Objects.equals(this.bankAccount, purchaseOrder.bankAccount) &&
        Objects.equals(this.channel, purchaseOrder.channel) &&
        Objects.equals(this.createdAt, purchaseOrder.createdAt) &&
        Objects.equals(this.createdBy, purchaseOrder.createdBy) &&
        Objects.equals(this.currency, purchaseOrder.currency) &&
        Objects.equals(this.currencyRate, purchaseOrder.currencyRate) &&
        Objects.equals(this.customMappings, purchaseOrder.customMappings) &&
        Objects.equals(this.deliveryDate, purchaseOrder.deliveryDate) &&
        Objects.equals(this.discountPercentage, purchaseOrder.discountPercentage) &&
        Objects.equals(this.downstreamId, purchaseOrder.downstreamId) &&
        Objects.equals(this.dueDate, purchaseOrder.dueDate) &&
        Objects.equals(this.expectedArrivalDate, purchaseOrder.expectedArrivalDate) &&
        Objects.equals(this.id, purchaseOrder.id) &&
        Objects.equals(this.issuedDate, purchaseOrder.issuedDate) &&
        Objects.equals(this.ledgerAccount, purchaseOrder.ledgerAccount) &&
        Objects.equals(this.lineItems, purchaseOrder.lineItems) &&
        Objects.equals(this.memo, purchaseOrder.memo) &&
        Objects.equals(this.paymentMethod, purchaseOrder.paymentMethod) &&
        Objects.equals(this.poNumber, purchaseOrder.poNumber) &&
        Objects.equals(this.reference, purchaseOrder.reference) &&
        Objects.equals(this.rowVersion, purchaseOrder.rowVersion) &&
        Objects.equals(this.shippingAddress, purchaseOrder.shippingAddress) &&
        Objects.equals(this.status, purchaseOrder.status) &&
        Objects.equals(this.subTotal, purchaseOrder.subTotal) &&
        Objects.equals(this.supplier, purchaseOrder.supplier) &&
        Objects.equals(this.taxCode, purchaseOrder.taxCode) &&
        Objects.equals(this.taxInclusive, purchaseOrder.taxInclusive) &&
        Objects.equals(this.templateId, purchaseOrder.templateId) &&
        Objects.equals(this.total, purchaseOrder.total) &&
        Objects.equals(this.totalTax, purchaseOrder.totalTax) &&
        Objects.equals(this.updatedAt, purchaseOrder.updatedAt) &&
        Objects.equals(this.updatedBy, purchaseOrder.updatedBy);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountingByRow, bankAccount, channel, createdAt, createdBy, currency, currencyRate, customMappings, deliveryDate, discountPercentage, downstreamId, dueDate, expectedArrivalDate, id, issuedDate, ledgerAccount, lineItems, memo, paymentMethod, poNumber, reference, rowVersion, shippingAddress, status, subTotal, supplier, taxCode, taxInclusive, templateId, total, totalTax, updatedAt, updatedBy);
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
    sb.append("class PurchaseOrder {\n");
    sb.append("    accountingByRow: ").append(toIndentedString(accountingByRow)).append("\n");
    sb.append("    bankAccount: ").append(toIndentedString(bankAccount)).append("\n");
    sb.append("    channel: ").append(toIndentedString(channel)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    currencyRate: ").append(toIndentedString(currencyRate)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    deliveryDate: ").append(toIndentedString(deliveryDate)).append("\n");
    sb.append("    discountPercentage: ").append(toIndentedString(discountPercentage)).append("\n");
    sb.append("    downstreamId: ").append(toIndentedString(downstreamId)).append("\n");
    sb.append("    dueDate: ").append(toIndentedString(dueDate)).append("\n");
    sb.append("    expectedArrivalDate: ").append(toIndentedString(expectedArrivalDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    issuedDate: ").append(toIndentedString(issuedDate)).append("\n");
    sb.append("    ledgerAccount: ").append(toIndentedString(ledgerAccount)).append("\n");
    sb.append("    lineItems: ").append(toIndentedString(lineItems)).append("\n");
    sb.append("    memo: ").append(toIndentedString(memo)).append("\n");
    sb.append("    paymentMethod: ").append(toIndentedString(paymentMethod)).append("\n");
    sb.append("    poNumber: ").append(toIndentedString(poNumber)).append("\n");
    sb.append("    reference: ").append(toIndentedString(reference)).append("\n");
    sb.append("    rowVersion: ").append(toIndentedString(rowVersion)).append("\n");
    sb.append("    shippingAddress: ").append(toIndentedString(shippingAddress)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subTotal: ").append(toIndentedString(subTotal)).append("\n");
    sb.append("    supplier: ").append(toIndentedString(supplier)).append("\n");
    sb.append("    taxCode: ").append(toIndentedString(taxCode)).append("\n");
    sb.append("    taxInclusive: ").append(toIndentedString(taxInclusive)).append("\n");
    sb.append("    templateId: ").append(toIndentedString(templateId)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    totalTax: ").append(toIndentedString(totalTax)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
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
    openapiFields.add("accounting_by_row");
    openapiFields.add("bank_account");
    openapiFields.add("channel");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("currency");
    openapiFields.add("currency_rate");
    openapiFields.add("custom_mappings");
    openapiFields.add("delivery_date");
    openapiFields.add("discount_percentage");
    openapiFields.add("downstream_id");
    openapiFields.add("due_date");
    openapiFields.add("expected_arrival_date");
    openapiFields.add("id");
    openapiFields.add("issued_date");
    openapiFields.add("ledger_account");
    openapiFields.add("line_items");
    openapiFields.add("memo");
    openapiFields.add("payment_method");
    openapiFields.add("po_number");
    openapiFields.add("reference");
    openapiFields.add("row_version");
    openapiFields.add("shipping_address");
    openapiFields.add("status");
    openapiFields.add("sub_total");
    openapiFields.add("supplier");
    openapiFields.add("tax_code");
    openapiFields.add("tax_inclusive");
    openapiFields.add("template_id");
    openapiFields.add("total");
    openapiFields.add("total_tax");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PurchaseOrder
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PurchaseOrder.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PurchaseOrder is not found in the empty JSON string", PurchaseOrder.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PurchaseOrder.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PurchaseOrder` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `bank_account`
      if (jsonObj.get("bank_account") != null && !jsonObj.get("bank_account").isJsonNull()) {
        BankAccount.validateJsonElement(jsonObj.get("bank_account"));
      }
      if ((jsonObj.get("channel") != null && !jsonObj.get("channel").isJsonNull()) && !jsonObj.get("channel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `channel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("channel").toString()));
      }
      if ((jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) && !jsonObj.get("created_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by").toString()));
      }
      // validate the optional field `currency`
      if (jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("currency"));
      }
      if ((jsonObj.get("downstream_id") != null && !jsonObj.get("downstream_id").isJsonNull()) && !jsonObj.get("downstream_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `downstream_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("downstream_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `ledger_account`
      if (jsonObj.get("ledger_account") != null && !jsonObj.get("ledger_account").isJsonNull()) {
        LinkedLedgerAccount.validateJsonElement(jsonObj.get("ledger_account"));
      }
      if (jsonObj.get("line_items") != null && !jsonObj.get("line_items").isJsonNull()) {
        JsonArray jsonArraylineItems = jsonObj.getAsJsonArray("line_items");
        if (jsonArraylineItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("line_items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `line_items` to be an array in the JSON string but got `%s`", jsonObj.get("line_items").toString()));
          }

          // validate the optional field `line_items` (array)
          for (int i = 0; i < jsonArraylineItems.size(); i++) {
            InvoiceLineItem.validateJsonElement(jsonArraylineItems.get(i));
          };
        }
      }
      if ((jsonObj.get("memo") != null && !jsonObj.get("memo").isJsonNull()) && !jsonObj.get("memo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `memo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("memo").toString()));
      }
      if ((jsonObj.get("payment_method") != null && !jsonObj.get("payment_method").isJsonNull()) && !jsonObj.get("payment_method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_method").toString()));
      }
      if ((jsonObj.get("po_number") != null && !jsonObj.get("po_number").isJsonNull()) && !jsonObj.get("po_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `po_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("po_number").toString()));
      }
      if ((jsonObj.get("reference") != null && !jsonObj.get("reference").isJsonNull()) && !jsonObj.get("reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference").toString()));
      }
      if ((jsonObj.get("row_version") != null && !jsonObj.get("row_version").isJsonNull()) && !jsonObj.get("row_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `row_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("row_version").toString()));
      }
      // validate the optional field `shipping_address`
      if (jsonObj.get("shipping_address") != null && !jsonObj.get("shipping_address").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("shipping_address"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      // validate the optional field `supplier`
      if (jsonObj.get("supplier") != null && !jsonObj.get("supplier").isJsonNull()) {
        LinkedSupplier.validateJsonElement(jsonObj.get("supplier"));
      }
      if ((jsonObj.get("tax_code") != null && !jsonObj.get("tax_code").isJsonNull()) && !jsonObj.get("tax_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_code").toString()));
      }
      if ((jsonObj.get("template_id") != null && !jsonObj.get("template_id").isJsonNull()) && !jsonObj.get("template_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `template_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("template_id").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PurchaseOrder.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PurchaseOrder' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PurchaseOrder> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PurchaseOrder.class));

       return (TypeAdapter<T>) new TypeAdapter<PurchaseOrder>() {
           @Override
           public void write(JsonWriter out, PurchaseOrder value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PurchaseOrder read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PurchaseOrder given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PurchaseOrder
   * @throws IOException if the JSON string is invalid with respect to PurchaseOrder
   */
  public static PurchaseOrder fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PurchaseOrder.class);
  }

  /**
   * Convert an instance of PurchaseOrder to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

