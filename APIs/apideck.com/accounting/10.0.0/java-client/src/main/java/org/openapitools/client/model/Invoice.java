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
import org.openapitools.client.model.LinkedCustomer;
import org.openapitools.client.model.LinkedLedgerAccount;
import org.openapitools.client.model.LinkedTrackingCategory;
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:31.900974-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Invoice {
  public static final String SERIALIZED_NAME_ACCOUNTING_BY_ROW = "accounting_by_row";
  @SerializedName(SERIALIZED_NAME_ACCOUNTING_BY_ROW)
  private Boolean accountingByRow;

  public static final String SERIALIZED_NAME_BALANCE = "balance";
  @SerializedName(SERIALIZED_NAME_BALANCE)
  private BigDecimal balance;

  public static final String SERIALIZED_NAME_BANK_ACCOUNT = "bank_account";
  @SerializedName(SERIALIZED_NAME_BANK_ACCOUNT)
  private BankAccount bankAccount;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billing_address";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private Address billingAddress;

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

  public static final String SERIALIZED_NAME_CUSTOMER = "customer";
  @SerializedName(SERIALIZED_NAME_CUSTOMER)
  private LinkedCustomer customer;

  public static final String SERIALIZED_NAME_CUSTOMER_MEMO = "customer_memo";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_MEMO)
  private String customerMemo;

  public static final String SERIALIZED_NAME_DEPOSIT = "deposit";
  @SerializedName(SERIALIZED_NAME_DEPOSIT)
  private BigDecimal deposit;

  public static final String SERIALIZED_NAME_DISCOUNT_AMOUNT = "discount_amount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_AMOUNT)
  private BigDecimal discountAmount;

  public static final String SERIALIZED_NAME_DISCOUNT_PERCENTAGE = "discount_percentage";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_PERCENTAGE)
  private BigDecimal discountPercentage;

  public static final String SERIALIZED_NAME_DOWNSTREAM_ID = "downstream_id";
  @SerializedName(SERIALIZED_NAME_DOWNSTREAM_ID)
  private String downstreamId;

  public static final String SERIALIZED_NAME_DUE_DATE = "due_date";
  @SerializedName(SERIALIZED_NAME_DUE_DATE)
  private LocalDate dueDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INVOICE_DATE = "invoice_date";
  @SerializedName(SERIALIZED_NAME_INVOICE_DATE)
  private LocalDate invoiceDate;

  public static final String SERIALIZED_NAME_INVOICE_SENT = "invoice_sent";
  @SerializedName(SERIALIZED_NAME_INVOICE_SENT)
  private Boolean invoiceSent;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_LEDGER_ACCOUNT = "ledger_account";
  @SerializedName(SERIALIZED_NAME_LEDGER_ACCOUNT)
  private LinkedLedgerAccount ledgerAccount;

  public static final String SERIALIZED_NAME_LINE_ITEMS = "line_items";
  @SerializedName(SERIALIZED_NAME_LINE_ITEMS)
  private List<InvoiceLineItem> lineItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_NUMBER = "number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private String number;

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

  public static final String SERIALIZED_NAME_SOURCE_DOCUMENT_URL = "source_document_url";
  @SerializedName(SERIALIZED_NAME_SOURCE_DOCUMENT_URL)
  private String sourceDocumentUrl;

  /**
   * Invoice status
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    DRAFT("draft"),
    
    SUBMITTED("submitted"),
    
    AUTHORISED("authorised"),
    
    PARTIALLY_PAID("partially_paid"),
    
    PAID("paid"),
    
    VOID("void"),
    
    CREDIT("credit"),
    
    DELETED("deleted");

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

  public static final String SERIALIZED_NAME_TAX_CODE = "tax_code";
  @SerializedName(SERIALIZED_NAME_TAX_CODE)
  private String taxCode;

  public static final String SERIALIZED_NAME_TAX_INCLUSIVE = "tax_inclusive";
  @SerializedName(SERIALIZED_NAME_TAX_INCLUSIVE)
  private Boolean taxInclusive;

  public static final String SERIALIZED_NAME_TEMPLATE_ID = "template_id";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_ID)
  private String templateId;

  public static final String SERIALIZED_NAME_TERMS = "terms";
  @SerializedName(SERIALIZED_NAME_TERMS)
  private String terms;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private BigDecimal total;

  public static final String SERIALIZED_NAME_TOTAL_TAX = "total_tax";
  @SerializedName(SERIALIZED_NAME_TOTAL_TAX)
  private BigDecimal totalTax;

  public static final String SERIALIZED_NAME_TRACKING_CATEGORY = "tracking_category";
  @SerializedName(SERIALIZED_NAME_TRACKING_CATEGORY)
  private LinkedTrackingCategory trackingCategory;

  /**
   * Invoice type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    STANDARD("standard"),
    
    CREDIT("credit"),
    
    SERVICE("service"),
    
    PRODUCT("product"),
    
    SUPPLIER("supplier"),
    
    OTHER("other");

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
      return null;
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

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public Invoice() {
  }

  public Invoice(
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

  public Invoice accountingByRow(Boolean accountingByRow) {
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


  public Invoice balance(BigDecimal balance) {
    this.balance = balance;
    return this;
  }

  /**
   * Balance of invoice due.
   * @return balance
   */
  @javax.annotation.Nullable
  public BigDecimal getBalance() {
    return balance;
  }

  public void setBalance(BigDecimal balance) {
    this.balance = balance;
  }


  public Invoice bankAccount(BankAccount bankAccount) {
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


  public Invoice billingAddress(Address billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Get billingAddress
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public Address getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(Address billingAddress) {
    this.billingAddress = billingAddress;
  }


  public Invoice channel(String channel) {
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



  public Invoice currency(Currency currency) {
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


  public Invoice currencyRate(BigDecimal currencyRate) {
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


  public Invoice customMappings(Object customMappings) {
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


  public Invoice customer(LinkedCustomer customer) {
    this.customer = customer;
    return this;
  }

  /**
   * Get customer
   * @return customer
   */
  @javax.annotation.Nullable
  public LinkedCustomer getCustomer() {
    return customer;
  }

  public void setCustomer(LinkedCustomer customer) {
    this.customer = customer;
  }


  public Invoice customerMemo(String customerMemo) {
    this.customerMemo = customerMemo;
    return this;
  }

  /**
   * Customer memo
   * @return customerMemo
   */
  @javax.annotation.Nullable
  public String getCustomerMemo() {
    return customerMemo;
  }

  public void setCustomerMemo(String customerMemo) {
    this.customerMemo = customerMemo;
  }


  public Invoice deposit(BigDecimal deposit) {
    this.deposit = deposit;
    return this;
  }

  /**
   * Amount of deposit made to this invoice.
   * @return deposit
   */
  @javax.annotation.Nullable
  public BigDecimal getDeposit() {
    return deposit;
  }

  public void setDeposit(BigDecimal deposit) {
    this.deposit = deposit;
  }


  public Invoice discountAmount(BigDecimal discountAmount) {
    this.discountAmount = discountAmount;
    return this;
  }

  /**
   * Discount amount applied to this invoice.
   * @return discountAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getDiscountAmount() {
    return discountAmount;
  }

  public void setDiscountAmount(BigDecimal discountAmount) {
    this.discountAmount = discountAmount;
  }


  public Invoice discountPercentage(BigDecimal discountPercentage) {
    this.discountPercentage = discountPercentage;
    return this;
  }

  /**
   * Discount percentage applied to this invoice.
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



  public Invoice dueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
    return this;
  }

  /**
   * The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.
   * @return dueDate
   */
  @javax.annotation.Nullable
  public LocalDate getDueDate() {
    return dueDate;
  }

  public void setDueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Invoice invoiceDate(LocalDate invoiceDate) {
    this.invoiceDate = invoiceDate;
    return this;
  }

  /**
   * Date invoice was issued - YYYY-MM-DD.
   * @return invoiceDate
   */
  @javax.annotation.Nullable
  public LocalDate getInvoiceDate() {
    return invoiceDate;
  }

  public void setInvoiceDate(LocalDate invoiceDate) {
    this.invoiceDate = invoiceDate;
  }


  public Invoice invoiceSent(Boolean invoiceSent) {
    this.invoiceSent = invoiceSent;
    return this;
  }

  /**
   * Invoice sent to contact/customer.
   * @return invoiceSent
   */
  @javax.annotation.Nullable
  public Boolean getInvoiceSent() {
    return invoiceSent;
  }

  public void setInvoiceSent(Boolean invoiceSent) {
    this.invoiceSent = invoiceSent;
  }


  public Invoice language(String language) {
    this.language = language;
    return this;
  }

  /**
   * language code according to ISO 639-1. For the United States - EN
   * @return language
   */
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public Invoice ledgerAccount(LinkedLedgerAccount ledgerAccount) {
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


  public Invoice lineItems(List<InvoiceLineItem> lineItems) {
    this.lineItems = lineItems;
    return this;
  }

  public Invoice addLineItemsItem(InvoiceLineItem lineItemsItem) {
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


  public Invoice number(String number) {
    this.number = number;
    return this;
  }

  /**
   * Invoice number.
   * @return number
   */
  @javax.annotation.Nullable
  public String getNumber() {
    return number;
  }

  public void setNumber(String number) {
    this.number = number;
  }


  public Invoice paymentMethod(String paymentMethod) {
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


  public Invoice poNumber(String poNumber) {
    this.poNumber = poNumber;
    return this;
  }

  /**
   * A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.
   * @return poNumber
   */
  @javax.annotation.Nullable
  public String getPoNumber() {
    return poNumber;
  }

  public void setPoNumber(String poNumber) {
    this.poNumber = poNumber;
  }


  public Invoice reference(String reference) {
    this.reference = reference;
    return this;
  }

  /**
   * Optional invoice reference.
   * @return reference
   */
  @javax.annotation.Nullable
  public String getReference() {
    return reference;
  }

  public void setReference(String reference) {
    this.reference = reference;
  }


  public Invoice rowVersion(String rowVersion) {
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


  public Invoice shippingAddress(Address shippingAddress) {
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


  public Invoice sourceDocumentUrl(String sourceDocumentUrl) {
    this.sourceDocumentUrl = sourceDocumentUrl;
    return this;
  }

  /**
   * URL link to a source document - shown as &#39;Go to [appName]&#39; in the downstream app. Currently only supported for Xero.
   * @return sourceDocumentUrl
   */
  @javax.annotation.Nullable
  public String getSourceDocumentUrl() {
    return sourceDocumentUrl;
  }

  public void setSourceDocumentUrl(String sourceDocumentUrl) {
    this.sourceDocumentUrl = sourceDocumentUrl;
  }


  public Invoice status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Invoice status
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public Invoice subTotal(BigDecimal subTotal) {
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


  public Invoice taxCode(String taxCode) {
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


  public Invoice taxInclusive(Boolean taxInclusive) {
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


  public Invoice templateId(String templateId) {
    this.templateId = templateId;
    return this;
  }

  /**
   * Optional invoice template
   * @return templateId
   */
  @javax.annotation.Nullable
  public String getTemplateId() {
    return templateId;
  }

  public void setTemplateId(String templateId) {
    this.templateId = templateId;
  }


  public Invoice terms(String terms) {
    this.terms = terms;
    return this;
  }

  /**
   * Terms of payment.
   * @return terms
   */
  @javax.annotation.Nullable
  public String getTerms() {
    return terms;
  }

  public void setTerms(String terms) {
    this.terms = terms;
  }


  public Invoice total(BigDecimal total) {
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


  public Invoice totalTax(BigDecimal totalTax) {
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


  public Invoice trackingCategory(LinkedTrackingCategory trackingCategory) {
    this.trackingCategory = trackingCategory;
    return this;
  }

  /**
   * Get trackingCategory
   * @return trackingCategory
   */
  @javax.annotation.Nullable
  public LinkedTrackingCategory getTrackingCategory() {
    return trackingCategory;
  }

  public void setTrackingCategory(LinkedTrackingCategory trackingCategory) {
    this.trackingCategory = trackingCategory;
  }


  public Invoice type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Invoice type
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
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
    Invoice invoice = (Invoice) o;
    return Objects.equals(this.accountingByRow, invoice.accountingByRow) &&
        Objects.equals(this.balance, invoice.balance) &&
        Objects.equals(this.bankAccount, invoice.bankAccount) &&
        Objects.equals(this.billingAddress, invoice.billingAddress) &&
        Objects.equals(this.channel, invoice.channel) &&
        Objects.equals(this.createdAt, invoice.createdAt) &&
        Objects.equals(this.createdBy, invoice.createdBy) &&
        Objects.equals(this.currency, invoice.currency) &&
        Objects.equals(this.currencyRate, invoice.currencyRate) &&
        Objects.equals(this.customMappings, invoice.customMappings) &&
        Objects.equals(this.customer, invoice.customer) &&
        Objects.equals(this.customerMemo, invoice.customerMemo) &&
        Objects.equals(this.deposit, invoice.deposit) &&
        Objects.equals(this.discountAmount, invoice.discountAmount) &&
        Objects.equals(this.discountPercentage, invoice.discountPercentage) &&
        Objects.equals(this.downstreamId, invoice.downstreamId) &&
        Objects.equals(this.dueDate, invoice.dueDate) &&
        Objects.equals(this.id, invoice.id) &&
        Objects.equals(this.invoiceDate, invoice.invoiceDate) &&
        Objects.equals(this.invoiceSent, invoice.invoiceSent) &&
        Objects.equals(this.language, invoice.language) &&
        Objects.equals(this.ledgerAccount, invoice.ledgerAccount) &&
        Objects.equals(this.lineItems, invoice.lineItems) &&
        Objects.equals(this.number, invoice.number) &&
        Objects.equals(this.paymentMethod, invoice.paymentMethod) &&
        Objects.equals(this.poNumber, invoice.poNumber) &&
        Objects.equals(this.reference, invoice.reference) &&
        Objects.equals(this.rowVersion, invoice.rowVersion) &&
        Objects.equals(this.shippingAddress, invoice.shippingAddress) &&
        Objects.equals(this.sourceDocumentUrl, invoice.sourceDocumentUrl) &&
        Objects.equals(this.status, invoice.status) &&
        Objects.equals(this.subTotal, invoice.subTotal) &&
        Objects.equals(this.taxCode, invoice.taxCode) &&
        Objects.equals(this.taxInclusive, invoice.taxInclusive) &&
        Objects.equals(this.templateId, invoice.templateId) &&
        Objects.equals(this.terms, invoice.terms) &&
        Objects.equals(this.total, invoice.total) &&
        Objects.equals(this.totalTax, invoice.totalTax) &&
        Objects.equals(this.trackingCategory, invoice.trackingCategory) &&
        Objects.equals(this.type, invoice.type) &&
        Objects.equals(this.updatedAt, invoice.updatedAt) &&
        Objects.equals(this.updatedBy, invoice.updatedBy);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountingByRow, balance, bankAccount, billingAddress, channel, createdAt, createdBy, currency, currencyRate, customMappings, customer, customerMemo, deposit, discountAmount, discountPercentage, downstreamId, dueDate, id, invoiceDate, invoiceSent, language, ledgerAccount, lineItems, number, paymentMethod, poNumber, reference, rowVersion, shippingAddress, sourceDocumentUrl, status, subTotal, taxCode, taxInclusive, templateId, terms, total, totalTax, trackingCategory, type, updatedAt, updatedBy);
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
    sb.append("    accountingByRow: ").append(toIndentedString(accountingByRow)).append("\n");
    sb.append("    balance: ").append(toIndentedString(balance)).append("\n");
    sb.append("    bankAccount: ").append(toIndentedString(bankAccount)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    channel: ").append(toIndentedString(channel)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    currencyRate: ").append(toIndentedString(currencyRate)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    customer: ").append(toIndentedString(customer)).append("\n");
    sb.append("    customerMemo: ").append(toIndentedString(customerMemo)).append("\n");
    sb.append("    deposit: ").append(toIndentedString(deposit)).append("\n");
    sb.append("    discountAmount: ").append(toIndentedString(discountAmount)).append("\n");
    sb.append("    discountPercentage: ").append(toIndentedString(discountPercentage)).append("\n");
    sb.append("    downstreamId: ").append(toIndentedString(downstreamId)).append("\n");
    sb.append("    dueDate: ").append(toIndentedString(dueDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invoiceDate: ").append(toIndentedString(invoiceDate)).append("\n");
    sb.append("    invoiceSent: ").append(toIndentedString(invoiceSent)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    ledgerAccount: ").append(toIndentedString(ledgerAccount)).append("\n");
    sb.append("    lineItems: ").append(toIndentedString(lineItems)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    paymentMethod: ").append(toIndentedString(paymentMethod)).append("\n");
    sb.append("    poNumber: ").append(toIndentedString(poNumber)).append("\n");
    sb.append("    reference: ").append(toIndentedString(reference)).append("\n");
    sb.append("    rowVersion: ").append(toIndentedString(rowVersion)).append("\n");
    sb.append("    shippingAddress: ").append(toIndentedString(shippingAddress)).append("\n");
    sb.append("    sourceDocumentUrl: ").append(toIndentedString(sourceDocumentUrl)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subTotal: ").append(toIndentedString(subTotal)).append("\n");
    sb.append("    taxCode: ").append(toIndentedString(taxCode)).append("\n");
    sb.append("    taxInclusive: ").append(toIndentedString(taxInclusive)).append("\n");
    sb.append("    templateId: ").append(toIndentedString(templateId)).append("\n");
    sb.append("    terms: ").append(toIndentedString(terms)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    totalTax: ").append(toIndentedString(totalTax)).append("\n");
    sb.append("    trackingCategory: ").append(toIndentedString(trackingCategory)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("balance");
    openapiFields.add("bank_account");
    openapiFields.add("billing_address");
    openapiFields.add("channel");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("currency");
    openapiFields.add("currency_rate");
    openapiFields.add("custom_mappings");
    openapiFields.add("customer");
    openapiFields.add("customer_memo");
    openapiFields.add("deposit");
    openapiFields.add("discount_amount");
    openapiFields.add("discount_percentage");
    openapiFields.add("downstream_id");
    openapiFields.add("due_date");
    openapiFields.add("id");
    openapiFields.add("invoice_date");
    openapiFields.add("invoice_sent");
    openapiFields.add("language");
    openapiFields.add("ledger_account");
    openapiFields.add("line_items");
    openapiFields.add("number");
    openapiFields.add("payment_method");
    openapiFields.add("po_number");
    openapiFields.add("reference");
    openapiFields.add("row_version");
    openapiFields.add("shipping_address");
    openapiFields.add("source_document_url");
    openapiFields.add("status");
    openapiFields.add("sub_total");
    openapiFields.add("tax_code");
    openapiFields.add("tax_inclusive");
    openapiFields.add("template_id");
    openapiFields.add("terms");
    openapiFields.add("total");
    openapiFields.add("total_tax");
    openapiFields.add("tracking_category");
    openapiFields.add("type");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
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
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `bank_account`
      if (jsonObj.get("bank_account") != null && !jsonObj.get("bank_account").isJsonNull()) {
        BankAccount.validateJsonElement(jsonObj.get("bank_account"));
      }
      // validate the optional field `billing_address`
      if (jsonObj.get("billing_address") != null && !jsonObj.get("billing_address").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("billing_address"));
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
      // validate the optional field `customer`
      if (jsonObj.get("customer") != null && !jsonObj.get("customer").isJsonNull()) {
        LinkedCustomer.validateJsonElement(jsonObj.get("customer"));
      }
      if ((jsonObj.get("customer_memo") != null && !jsonObj.get("customer_memo").isJsonNull()) && !jsonObj.get("customer_memo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customer_memo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customer_memo").toString()));
      }
      if ((jsonObj.get("downstream_id") != null && !jsonObj.get("downstream_id").isJsonNull()) && !jsonObj.get("downstream_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `downstream_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("downstream_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
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
      if ((jsonObj.get("number") != null && !jsonObj.get("number").isJsonNull()) && !jsonObj.get("number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number").toString()));
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
      if ((jsonObj.get("source_document_url") != null && !jsonObj.get("source_document_url").isJsonNull()) && !jsonObj.get("source_document_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_document_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_document_url").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("tax_code") != null && !jsonObj.get("tax_code").isJsonNull()) && !jsonObj.get("tax_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_code").toString()));
      }
      if ((jsonObj.get("template_id") != null && !jsonObj.get("template_id").isJsonNull()) && !jsonObj.get("template_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `template_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("template_id").toString()));
      }
      if ((jsonObj.get("terms") != null && !jsonObj.get("terms").isJsonNull()) && !jsonObj.get("terms").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `terms` to be a primitive type in the JSON string but got `%s`", jsonObj.get("terms").toString()));
      }
      // validate the optional field `tracking_category`
      if (jsonObj.get("tracking_category") != null && !jsonObj.get("tracking_category").isJsonNull()) {
        LinkedTrackingCategory.validateJsonElement(jsonObj.get("tracking_category"));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
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

