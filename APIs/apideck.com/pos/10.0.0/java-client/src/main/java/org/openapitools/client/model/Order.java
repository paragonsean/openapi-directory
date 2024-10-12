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
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.OrderCustomersInner;
import org.openapitools.client.model.OrderDiscountsInner;
import org.openapitools.client.model.OrderFulfillmentsInner;
import org.openapitools.client.model.OrderLineItemsInner;
import org.openapitools.client.model.OrderPaymentsInner;
import org.openapitools.client.model.OrderRefundsInner;
import org.openapitools.client.model.OrderTaxesInner;
import org.openapitools.client.model.OrderTendersInner;
import org.openapitools.client.model.ServiceCharge;
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
 * Order
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:35.267625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Order {
  public static final String SERIALIZED_NAME_CLOSED_DATE = "closed_date";
  @SerializedName(SERIALIZED_NAME_CLOSED_DATE)
  private LocalDate closedDate;

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

  public static final String SERIALIZED_NAME_CUSTOMERS = "customers";
  @SerializedName(SERIALIZED_NAME_CUSTOMERS)
  private List<OrderCustomersInner> customers = new ArrayList<>();

  public static final String SERIALIZED_NAME_DISCOUNTS = "discounts";
  @SerializedName(SERIALIZED_NAME_DISCOUNTS)
  private List<OrderDiscountsInner> discounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_EMPLOYEE_ID = "employee_id";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE_ID)
  private String employeeId;

  public static final String SERIALIZED_NAME_FULFILLMENTS = "fulfillments";
  @SerializedName(SERIALIZED_NAME_FULFILLMENTS)
  private List<OrderFulfillmentsInner> fulfillments = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IDEMPOTENCY_KEY = "idempotency_key";
  @SerializedName(SERIALIZED_NAME_IDEMPOTENCY_KEY)
  private String idempotencyKey;

  public static final String SERIALIZED_NAME_LINE_ITEMS = "line_items";
  @SerializedName(SERIALIZED_NAME_LINE_ITEMS)
  private List<OrderLineItemsInner> lineItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOCATION_ID = "location_id";
  @SerializedName(SERIALIZED_NAME_LOCATION_ID)
  private String locationId;

  public static final String SERIALIZED_NAME_MERCHANT_ID = "merchant_id";
  @SerializedName(SERIALIZED_NAME_MERCHANT_ID)
  private String merchantId;

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_ORDER_DATE = "order_date";
  @SerializedName(SERIALIZED_NAME_ORDER_DATE)
  private LocalDate orderDate;

  public static final String SERIALIZED_NAME_ORDER_NUMBER = "order_number";
  @SerializedName(SERIALIZED_NAME_ORDER_NUMBER)
  private String orderNumber;

  public static final String SERIALIZED_NAME_ORDER_TYPE_ID = "order_type_id";
  @SerializedName(SERIALIZED_NAME_ORDER_TYPE_ID)
  private String orderTypeId;

  /**
   * Is this order paid or not?
   */
  @JsonAdapter(PaymentStatusEnum.Adapter.class)
  public enum PaymentStatusEnum {
    OPEN("open"),
    
    PAID("paid"),
    
    REFUNDED("refunded"),
    
    CREDITED("credited"),
    
    PARTIALLY_PAID("partially_paid"),
    
    PARTIALLY_REFUNDED("partially_refunded"),
    
    UNKNOWN("unknown");

    private String value;

    PaymentStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PaymentStatusEnum fromValue(String value) {
      for (PaymentStatusEnum b : PaymentStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PaymentStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PaymentStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PaymentStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PaymentStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PaymentStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PAYMENT_STATUS = "payment_status";
  @SerializedName(SERIALIZED_NAME_PAYMENT_STATUS)
  private PaymentStatusEnum paymentStatus;

  public static final String SERIALIZED_NAME_PAYMENTS = "payments";
  @SerializedName(SERIALIZED_NAME_PAYMENTS)
  private List<OrderPaymentsInner> payments = new ArrayList<>();

  public static final String SERIALIZED_NAME_REFERENCE_ID = "reference_id";
  @SerializedName(SERIALIZED_NAME_REFERENCE_ID)
  private String referenceId;

  public static final String SERIALIZED_NAME_REFUNDED = "refunded";
  @SerializedName(SERIALIZED_NAME_REFUNDED)
  private Boolean refunded;

  public static final String SERIALIZED_NAME_REFUNDS = "refunds";
  @SerializedName(SERIALIZED_NAME_REFUNDS)
  private List<OrderRefundsInner> refunds = new ArrayList<>();

  public static final String SERIALIZED_NAME_SEAT = "seat";
  @SerializedName(SERIALIZED_NAME_SEAT)
  private String seat;

  public static final String SERIALIZED_NAME_SERVICE_CHARGES = "service_charges";
  @SerializedName(SERIALIZED_NAME_SERVICE_CHARGES)
  private List<ServiceCharge> serviceCharges = new ArrayList<>();

  /**
   * Source of order. Indicates the way that the order was placed.
   */
  @JsonAdapter(SourceEnum.Adapter.class)
  public enum SourceEnum {
    IN_STORE("in-store"),
    
    ONLINE("online"),
    
    OPT("opt"),
    
    API("api"),
    
    KIOSK("kiosk"),
    
    CALLER_ID("caller-id"),
    
    GOOGLE("google"),
    
    INVOICE("invoice");

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
      return null;
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

  /**
   * Order status. Clover specific: If no value is set, the status defaults to hidden, which indicates a hidden order. A hidden order is not displayed in user interfaces and can only be retrieved by its id. When creating an order via the REST API the value must be manually set to &#39;open&#39;. More info [https://docs.clover.com/reference/orderupdateorder]()
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    OPEN("open"),
    
    DRAFT("draft"),
    
    DELIVERED("delivered"),
    
    DELAYED("delayed"),
    
    VOIDED("voided"),
    
    COMPLETED("completed"),
    
    HIDDEN("hidden");

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

  public static final String SERIALIZED_NAME_TABLE = "table";
  @SerializedName(SERIALIZED_NAME_TABLE)
  private String table;

  public static final String SERIALIZED_NAME_TAXES = "taxes";
  @SerializedName(SERIALIZED_NAME_TAXES)
  private List<OrderTaxesInner> taxes = new ArrayList<>();

  public static final String SERIALIZED_NAME_TENDERS = "tenders";
  @SerializedName(SERIALIZED_NAME_TENDERS)
  private List<OrderTendersInner> tenders = new ArrayList<>();

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TOTAL_AMOUNT = "total_amount";
  @SerializedName(SERIALIZED_NAME_TOTAL_AMOUNT)
  private Integer totalAmount;

  public static final String SERIALIZED_NAME_TOTAL_DISCOUNT = "total_discount";
  @SerializedName(SERIALIZED_NAME_TOTAL_DISCOUNT)
  private Integer totalDiscount;

  public static final String SERIALIZED_NAME_TOTAL_REFUND = "total_refund";
  @SerializedName(SERIALIZED_NAME_TOTAL_REFUND)
  private Integer totalRefund;

  public static final String SERIALIZED_NAME_TOTAL_SERVICE_CHARGE = "total_service_charge";
  @SerializedName(SERIALIZED_NAME_TOTAL_SERVICE_CHARGE)
  private Integer totalServiceCharge;

  public static final String SERIALIZED_NAME_TOTAL_TAX = "total_tax";
  @SerializedName(SERIALIZED_NAME_TOTAL_TAX)
  private Integer totalTax;

  public static final String SERIALIZED_NAME_TOTAL_TIP = "total_tip";
  @SerializedName(SERIALIZED_NAME_TOTAL_TIP)
  private Integer totalTip;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public static final String SERIALIZED_NAME_VOIDED = "voided";
  @SerializedName(SERIALIZED_NAME_VOIDED)
  private Boolean voided;

  public static final String SERIALIZED_NAME_VOIDED_AT = "voided_at";
  @SerializedName(SERIALIZED_NAME_VOIDED_AT)
  private OffsetDateTime voidedAt;

  public Order() {
  }

  public Order(
     OffsetDateTime createdAt, 
     String createdBy, 
     String id, 
     SourceEnum source, 
     OffsetDateTime updatedAt, 
     String updatedBy, 
     OffsetDateTime voidedAt
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.id = id;
    this.source = source;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
    this.voidedAt = voidedAt;
  }

  public Order closedDate(LocalDate closedDate) {
    this.closedDate = closedDate;
    return this;
  }

  /**
   * Get closedDate
   * @return closedDate
   */
  @javax.annotation.Nullable
  public LocalDate getClosedDate() {
    return closedDate;
  }

  public void setClosedDate(LocalDate closedDate) {
    this.closedDate = closedDate;
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



  public Order currency(Currency currency) {
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


  public Order customMappings(Object customMappings) {
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


  public Order customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * Get customerId
   * @return customerId
   */
  @javax.annotation.Nullable
  public String getCustomerId() {
    return customerId;
  }

  public void setCustomerId(String customerId) {
    this.customerId = customerId;
  }


  public Order customers(List<OrderCustomersInner> customers) {
    this.customers = customers;
    return this;
  }

  public Order addCustomersItem(OrderCustomersInner customersItem) {
    if (this.customers == null) {
      this.customers = new ArrayList<>();
    }
    this.customers.add(customersItem);
    return this;
  }

  /**
   * Get customers
   * @return customers
   */
  @javax.annotation.Nullable
  public List<OrderCustomersInner> getCustomers() {
    return customers;
  }

  public void setCustomers(List<OrderCustomersInner> customers) {
    this.customers = customers;
  }


  public Order discounts(List<OrderDiscountsInner> discounts) {
    this.discounts = discounts;
    return this;
  }

  public Order addDiscountsItem(OrderDiscountsInner discountsItem) {
    if (this.discounts == null) {
      this.discounts = new ArrayList<>();
    }
    this.discounts.add(discountsItem);
    return this;
  }

  /**
   * Get discounts
   * @return discounts
   */
  @javax.annotation.Nullable
  public List<OrderDiscountsInner> getDiscounts() {
    return discounts;
  }

  public void setDiscounts(List<OrderDiscountsInner> discounts) {
    this.discounts = discounts;
  }


  public Order employeeId(String employeeId) {
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


  public Order fulfillments(List<OrderFulfillmentsInner> fulfillments) {
    this.fulfillments = fulfillments;
    return this;
  }

  public Order addFulfillmentsItem(OrderFulfillmentsInner fulfillmentsItem) {
    if (this.fulfillments == null) {
      this.fulfillments = new ArrayList<>();
    }
    this.fulfillments.add(fulfillmentsItem);
    return this;
  }

  /**
   * Get fulfillments
   * @return fulfillments
   */
  @javax.annotation.Nullable
  public List<OrderFulfillmentsInner> getFulfillments() {
    return fulfillments;
  }

  public void setFulfillments(List<OrderFulfillmentsInner> fulfillments) {
    this.fulfillments = fulfillments;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Order idempotencyKey(String idempotencyKey) {
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


  public Order lineItems(List<OrderLineItemsInner> lineItems) {
    this.lineItems = lineItems;
    return this;
  }

  public Order addLineItemsItem(OrderLineItemsInner lineItemsItem) {
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
  public List<OrderLineItemsInner> getLineItems() {
    return lineItems;
  }

  public void setLineItems(List<OrderLineItemsInner> lineItems) {
    this.lineItems = lineItems;
  }


  public Order locationId(String locationId) {
    this.locationId = locationId;
    return this;
  }

  /**
   * Get locationId
   * @return locationId
   */
  @javax.annotation.Nonnull
  public String getLocationId() {
    return locationId;
  }

  public void setLocationId(String locationId) {
    this.locationId = locationId;
  }


  public Order merchantId(String merchantId) {
    this.merchantId = merchantId;
    return this;
  }

  /**
   * Get merchantId
   * @return merchantId
   */
  @javax.annotation.Nonnull
  public String getMerchantId() {
    return merchantId;
  }

  public void setMerchantId(String merchantId) {
    this.merchantId = merchantId;
  }


  public Order note(String note) {
    this.note = note;
    return this;
  }

  /**
   * A note with information about this order, may be printed on the order receipt and displayed in apps
   * @return note
   */
  @javax.annotation.Nullable
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }


  public Order orderDate(LocalDate orderDate) {
    this.orderDate = orderDate;
    return this;
  }

  /**
   * Get orderDate
   * @return orderDate
   */
  @javax.annotation.Nullable
  public LocalDate getOrderDate() {
    return orderDate;
  }

  public void setOrderDate(LocalDate orderDate) {
    this.orderDate = orderDate;
  }


  public Order orderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
    return this;
  }

  /**
   * Get orderNumber
   * @return orderNumber
   */
  @javax.annotation.Nullable
  public String getOrderNumber() {
    return orderNumber;
  }

  public void setOrderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
  }


  public Order orderTypeId(String orderTypeId) {
    this.orderTypeId = orderTypeId;
    return this;
  }

  /**
   * Get orderTypeId
   * @return orderTypeId
   */
  @javax.annotation.Nullable
  public String getOrderTypeId() {
    return orderTypeId;
  }

  public void setOrderTypeId(String orderTypeId) {
    this.orderTypeId = orderTypeId;
  }


  public Order paymentStatus(PaymentStatusEnum paymentStatus) {
    this.paymentStatus = paymentStatus;
    return this;
  }

  /**
   * Is this order paid or not?
   * @return paymentStatus
   */
  @javax.annotation.Nullable
  public PaymentStatusEnum getPaymentStatus() {
    return paymentStatus;
  }

  public void setPaymentStatus(PaymentStatusEnum paymentStatus) {
    this.paymentStatus = paymentStatus;
  }


  public Order payments(List<OrderPaymentsInner> payments) {
    this.payments = payments;
    return this;
  }

  public Order addPaymentsItem(OrderPaymentsInner paymentsItem) {
    if (this.payments == null) {
      this.payments = new ArrayList<>();
    }
    this.payments.add(paymentsItem);
    return this;
  }

  /**
   * Get payments
   * @return payments
   */
  @javax.annotation.Nullable
  public List<OrderPaymentsInner> getPayments() {
    return payments;
  }

  public void setPayments(List<OrderPaymentsInner> payments) {
    this.payments = payments;
  }


  public Order referenceId(String referenceId) {
    this.referenceId = referenceId;
    return this;
  }

  /**
   * An optional user-defined reference ID that associates this record with another entity in an external system. For example, a customer ID from an external customer management system.
   * @return referenceId
   */
  @javax.annotation.Nullable
  public String getReferenceId() {
    return referenceId;
  }

  public void setReferenceId(String referenceId) {
    this.referenceId = referenceId;
  }


  public Order refunded(Boolean refunded) {
    this.refunded = refunded;
    return this;
  }

  /**
   * Get refunded
   * @return refunded
   */
  @javax.annotation.Nullable
  public Boolean getRefunded() {
    return refunded;
  }

  public void setRefunded(Boolean refunded) {
    this.refunded = refunded;
  }


  public Order refunds(List<OrderRefundsInner> refunds) {
    this.refunds = refunds;
    return this;
  }

  public Order addRefundsItem(OrderRefundsInner refundsItem) {
    if (this.refunds == null) {
      this.refunds = new ArrayList<>();
    }
    this.refunds.add(refundsItem);
    return this;
  }

  /**
   * Get refunds
   * @return refunds
   */
  @javax.annotation.Nullable
  public List<OrderRefundsInner> getRefunds() {
    return refunds;
  }

  public void setRefunds(List<OrderRefundsInner> refunds) {
    this.refunds = refunds;
  }


  public Order seat(String seat) {
    this.seat = seat;
    return this;
  }

  /**
   * Get seat
   * @return seat
   */
  @javax.annotation.Nullable
  public String getSeat() {
    return seat;
  }

  public void setSeat(String seat) {
    this.seat = seat;
  }


  public Order serviceCharges(List<ServiceCharge> serviceCharges) {
    this.serviceCharges = serviceCharges;
    return this;
  }

  public Order addServiceChargesItem(ServiceCharge serviceChargesItem) {
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


  /**
   * Source of order. Indicates the way that the order was placed.
   * @return source
   */
  @javax.annotation.Nullable
  public SourceEnum getSource() {
    return source;
  }



  public Order status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Order status. Clover specific: If no value is set, the status defaults to hidden, which indicates a hidden order. A hidden order is not displayed in user interfaces and can only be retrieved by its id. When creating an order via the REST API the value must be manually set to &#39;open&#39;. More info [https://docs.clover.com/reference/orderupdateorder]()
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public Order table(String table) {
    this.table = table;
    return this;
  }

  /**
   * Get table
   * @return table
   */
  @javax.annotation.Nullable
  public String getTable() {
    return table;
  }

  public void setTable(String table) {
    this.table = table;
  }


  public Order taxes(List<OrderTaxesInner> taxes) {
    this.taxes = taxes;
    return this;
  }

  public Order addTaxesItem(OrderTaxesInner taxesItem) {
    if (this.taxes == null) {
      this.taxes = new ArrayList<>();
    }
    this.taxes.add(taxesItem);
    return this;
  }

  /**
   * Get taxes
   * @return taxes
   */
  @javax.annotation.Nullable
  public List<OrderTaxesInner> getTaxes() {
    return taxes;
  }

  public void setTaxes(List<OrderTaxesInner> taxes) {
    this.taxes = taxes;
  }


  public Order tenders(List<OrderTendersInner> tenders) {
    this.tenders = tenders;
    return this;
  }

  public Order addTendersItem(OrderTendersInner tendersItem) {
    if (this.tenders == null) {
      this.tenders = new ArrayList<>();
    }
    this.tenders.add(tendersItem);
    return this;
  }

  /**
   * Get tenders
   * @return tenders
   */
  @javax.annotation.Nullable
  public List<OrderTendersInner> getTenders() {
    return tenders;
  }

  public void setTenders(List<OrderTendersInner> tenders) {
    this.tenders = tenders;
  }


  public Order title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Order totalAmount(Integer totalAmount) {
    this.totalAmount = totalAmount;
    return this;
  }

  /**
   * Get totalAmount
   * @return totalAmount
   */
  @javax.annotation.Nullable
  public Integer getTotalAmount() {
    return totalAmount;
  }

  public void setTotalAmount(Integer totalAmount) {
    this.totalAmount = totalAmount;
  }


  public Order totalDiscount(Integer totalDiscount) {
    this.totalDiscount = totalDiscount;
    return this;
  }

  /**
   * Get totalDiscount
   * @return totalDiscount
   */
  @javax.annotation.Nullable
  public Integer getTotalDiscount() {
    return totalDiscount;
  }

  public void setTotalDiscount(Integer totalDiscount) {
    this.totalDiscount = totalDiscount;
  }


  public Order totalRefund(Integer totalRefund) {
    this.totalRefund = totalRefund;
    return this;
  }

  /**
   * Get totalRefund
   * @return totalRefund
   */
  @javax.annotation.Nullable
  public Integer getTotalRefund() {
    return totalRefund;
  }

  public void setTotalRefund(Integer totalRefund) {
    this.totalRefund = totalRefund;
  }


  public Order totalServiceCharge(Integer totalServiceCharge) {
    this.totalServiceCharge = totalServiceCharge;
    return this;
  }

  /**
   * Get totalServiceCharge
   * @return totalServiceCharge
   */
  @javax.annotation.Nullable
  public Integer getTotalServiceCharge() {
    return totalServiceCharge;
  }

  public void setTotalServiceCharge(Integer totalServiceCharge) {
    this.totalServiceCharge = totalServiceCharge;
  }


  public Order totalTax(Integer totalTax) {
    this.totalTax = totalTax;
    return this;
  }

  /**
   * Get totalTax
   * @return totalTax
   */
  @javax.annotation.Nullable
  public Integer getTotalTax() {
    return totalTax;
  }

  public void setTotalTax(Integer totalTax) {
    this.totalTax = totalTax;
  }


  public Order totalTip(Integer totalTip) {
    this.totalTip = totalTip;
    return this;
  }

  /**
   * Get totalTip
   * @return totalTip
   */
  @javax.annotation.Nullable
  public Integer getTotalTip() {
    return totalTip;
  }

  public void setTotalTip(Integer totalTip) {
    this.totalTip = totalTip;
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



  public Order version(String version) {
    this.version = version;
    return this;
  }

  /**
   * Get version
   * @return version
   */
  @javax.annotation.Nullable
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }


  public Order voided(Boolean voided) {
    this.voided = voided;
    return this;
  }

  /**
   * Get voided
   * @return voided
   */
  @javax.annotation.Nullable
  public Boolean getVoided() {
    return voided;
  }

  public void setVoided(Boolean voided) {
    this.voided = voided;
  }


  /**
   * Get voidedAt
   * @return voidedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getVoidedAt() {
    return voidedAt;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Order order = (Order) o;
    return Objects.equals(this.closedDate, order.closedDate) &&
        Objects.equals(this.createdAt, order.createdAt) &&
        Objects.equals(this.createdBy, order.createdBy) &&
        Objects.equals(this.currency, order.currency) &&
        Objects.equals(this.customMappings, order.customMappings) &&
        Objects.equals(this.customerId, order.customerId) &&
        Objects.equals(this.customers, order.customers) &&
        Objects.equals(this.discounts, order.discounts) &&
        Objects.equals(this.employeeId, order.employeeId) &&
        Objects.equals(this.fulfillments, order.fulfillments) &&
        Objects.equals(this.id, order.id) &&
        Objects.equals(this.idempotencyKey, order.idempotencyKey) &&
        Objects.equals(this.lineItems, order.lineItems) &&
        Objects.equals(this.locationId, order.locationId) &&
        Objects.equals(this.merchantId, order.merchantId) &&
        Objects.equals(this.note, order.note) &&
        Objects.equals(this.orderDate, order.orderDate) &&
        Objects.equals(this.orderNumber, order.orderNumber) &&
        Objects.equals(this.orderTypeId, order.orderTypeId) &&
        Objects.equals(this.paymentStatus, order.paymentStatus) &&
        Objects.equals(this.payments, order.payments) &&
        Objects.equals(this.referenceId, order.referenceId) &&
        Objects.equals(this.refunded, order.refunded) &&
        Objects.equals(this.refunds, order.refunds) &&
        Objects.equals(this.seat, order.seat) &&
        Objects.equals(this.serviceCharges, order.serviceCharges) &&
        Objects.equals(this.source, order.source) &&
        Objects.equals(this.status, order.status) &&
        Objects.equals(this.table, order.table) &&
        Objects.equals(this.taxes, order.taxes) &&
        Objects.equals(this.tenders, order.tenders) &&
        Objects.equals(this.title, order.title) &&
        Objects.equals(this.totalAmount, order.totalAmount) &&
        Objects.equals(this.totalDiscount, order.totalDiscount) &&
        Objects.equals(this.totalRefund, order.totalRefund) &&
        Objects.equals(this.totalServiceCharge, order.totalServiceCharge) &&
        Objects.equals(this.totalTax, order.totalTax) &&
        Objects.equals(this.totalTip, order.totalTip) &&
        Objects.equals(this.updatedAt, order.updatedAt) &&
        Objects.equals(this.updatedBy, order.updatedBy) &&
        Objects.equals(this.version, order.version) &&
        Objects.equals(this.voided, order.voided) &&
        Objects.equals(this.voidedAt, order.voidedAt);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(closedDate, createdAt, createdBy, currency, customMappings, customerId, customers, discounts, employeeId, fulfillments, id, idempotencyKey, lineItems, locationId, merchantId, note, orderDate, orderNumber, orderTypeId, paymentStatus, payments, referenceId, refunded, refunds, seat, serviceCharges, source, status, table, taxes, tenders, title, totalAmount, totalDiscount, totalRefund, totalServiceCharge, totalTax, totalTip, updatedAt, updatedBy, version, voided, voidedAt);
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
    sb.append("class Order {\n");
    sb.append("    closedDate: ").append(toIndentedString(closedDate)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    customers: ").append(toIndentedString(customers)).append("\n");
    sb.append("    discounts: ").append(toIndentedString(discounts)).append("\n");
    sb.append("    employeeId: ").append(toIndentedString(employeeId)).append("\n");
    sb.append("    fulfillments: ").append(toIndentedString(fulfillments)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    idempotencyKey: ").append(toIndentedString(idempotencyKey)).append("\n");
    sb.append("    lineItems: ").append(toIndentedString(lineItems)).append("\n");
    sb.append("    locationId: ").append(toIndentedString(locationId)).append("\n");
    sb.append("    merchantId: ").append(toIndentedString(merchantId)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    orderDate: ").append(toIndentedString(orderDate)).append("\n");
    sb.append("    orderNumber: ").append(toIndentedString(orderNumber)).append("\n");
    sb.append("    orderTypeId: ").append(toIndentedString(orderTypeId)).append("\n");
    sb.append("    paymentStatus: ").append(toIndentedString(paymentStatus)).append("\n");
    sb.append("    payments: ").append(toIndentedString(payments)).append("\n");
    sb.append("    referenceId: ").append(toIndentedString(referenceId)).append("\n");
    sb.append("    refunded: ").append(toIndentedString(refunded)).append("\n");
    sb.append("    refunds: ").append(toIndentedString(refunds)).append("\n");
    sb.append("    seat: ").append(toIndentedString(seat)).append("\n");
    sb.append("    serviceCharges: ").append(toIndentedString(serviceCharges)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    table: ").append(toIndentedString(table)).append("\n");
    sb.append("    taxes: ").append(toIndentedString(taxes)).append("\n");
    sb.append("    tenders: ").append(toIndentedString(tenders)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    totalAmount: ").append(toIndentedString(totalAmount)).append("\n");
    sb.append("    totalDiscount: ").append(toIndentedString(totalDiscount)).append("\n");
    sb.append("    totalRefund: ").append(toIndentedString(totalRefund)).append("\n");
    sb.append("    totalServiceCharge: ").append(toIndentedString(totalServiceCharge)).append("\n");
    sb.append("    totalTax: ").append(toIndentedString(totalTax)).append("\n");
    sb.append("    totalTip: ").append(toIndentedString(totalTip)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    voided: ").append(toIndentedString(voided)).append("\n");
    sb.append("    voidedAt: ").append(toIndentedString(voidedAt)).append("\n");
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
    openapiFields.add("closed_date");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("currency");
    openapiFields.add("custom_mappings");
    openapiFields.add("customer_id");
    openapiFields.add("customers");
    openapiFields.add("discounts");
    openapiFields.add("employee_id");
    openapiFields.add("fulfillments");
    openapiFields.add("id");
    openapiFields.add("idempotency_key");
    openapiFields.add("line_items");
    openapiFields.add("location_id");
    openapiFields.add("merchant_id");
    openapiFields.add("note");
    openapiFields.add("order_date");
    openapiFields.add("order_number");
    openapiFields.add("order_type_id");
    openapiFields.add("payment_status");
    openapiFields.add("payments");
    openapiFields.add("reference_id");
    openapiFields.add("refunded");
    openapiFields.add("refunds");
    openapiFields.add("seat");
    openapiFields.add("service_charges");
    openapiFields.add("source");
    openapiFields.add("status");
    openapiFields.add("table");
    openapiFields.add("taxes");
    openapiFields.add("tenders");
    openapiFields.add("title");
    openapiFields.add("total_amount");
    openapiFields.add("total_discount");
    openapiFields.add("total_refund");
    openapiFields.add("total_service_charge");
    openapiFields.add("total_tax");
    openapiFields.add("total_tip");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("version");
    openapiFields.add("voided");
    openapiFields.add("voided_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("location_id");
    openapiRequiredFields.add("merchant_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Order
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Order.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Order is not found in the empty JSON string", Order.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Order.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Order` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Order.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) && !jsonObj.get("created_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by").toString()));
      }
      // validate the optional field `currency`
      if (jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("currency"));
      }
      if ((jsonObj.get("customer_id") != null && !jsonObj.get("customer_id").isJsonNull()) && !jsonObj.get("customer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customer_id").toString()));
      }
      if (jsonObj.get("customers") != null && !jsonObj.get("customers").isJsonNull()) {
        JsonArray jsonArraycustomers = jsonObj.getAsJsonArray("customers");
        if (jsonArraycustomers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customers` to be an array in the JSON string but got `%s`", jsonObj.get("customers").toString()));
          }

          // validate the optional field `customers` (array)
          for (int i = 0; i < jsonArraycustomers.size(); i++) {
            OrderCustomersInner.validateJsonElement(jsonArraycustomers.get(i));
          };
        }
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
            OrderDiscountsInner.validateJsonElement(jsonArraydiscounts.get(i));
          };
        }
      }
      if ((jsonObj.get("employee_id") != null && !jsonObj.get("employee_id").isJsonNull()) && !jsonObj.get("employee_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employee_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employee_id").toString()));
      }
      if (jsonObj.get("fulfillments") != null && !jsonObj.get("fulfillments").isJsonNull()) {
        JsonArray jsonArrayfulfillments = jsonObj.getAsJsonArray("fulfillments");
        if (jsonArrayfulfillments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("fulfillments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `fulfillments` to be an array in the JSON string but got `%s`", jsonObj.get("fulfillments").toString()));
          }

          // validate the optional field `fulfillments` (array)
          for (int i = 0; i < jsonArrayfulfillments.size(); i++) {
            OrderFulfillmentsInner.validateJsonElement(jsonArrayfulfillments.get(i));
          };
        }
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("idempotency_key") != null && !jsonObj.get("idempotency_key").isJsonNull()) && !jsonObj.get("idempotency_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `idempotency_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("idempotency_key").toString()));
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
            OrderLineItemsInner.validateJsonElement(jsonArraylineItems.get(i));
          };
        }
      }
      if (!jsonObj.get("location_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location_id").toString()));
      }
      if (!jsonObj.get("merchant_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchant_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchant_id").toString()));
      }
      if ((jsonObj.get("note") != null && !jsonObj.get("note").isJsonNull()) && !jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
      if ((jsonObj.get("order_number") != null && !jsonObj.get("order_number").isJsonNull()) && !jsonObj.get("order_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_number").toString()));
      }
      if ((jsonObj.get("order_type_id") != null && !jsonObj.get("order_type_id").isJsonNull()) && !jsonObj.get("order_type_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_type_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_type_id").toString()));
      }
      if ((jsonObj.get("payment_status") != null && !jsonObj.get("payment_status").isJsonNull()) && !jsonObj.get("payment_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_status").toString()));
      }
      // validate the optional field `payment_status`
      if (jsonObj.get("payment_status") != null && !jsonObj.get("payment_status").isJsonNull()) {
        PaymentStatusEnum.validateJsonElement(jsonObj.get("payment_status"));
      }
      if (jsonObj.get("payments") != null && !jsonObj.get("payments").isJsonNull()) {
        JsonArray jsonArraypayments = jsonObj.getAsJsonArray("payments");
        if (jsonArraypayments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("payments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `payments` to be an array in the JSON string but got `%s`", jsonObj.get("payments").toString()));
          }

          // validate the optional field `payments` (array)
          for (int i = 0; i < jsonArraypayments.size(); i++) {
            OrderPaymentsInner.validateJsonElement(jsonArraypayments.get(i));
          };
        }
      }
      if ((jsonObj.get("reference_id") != null && !jsonObj.get("reference_id").isJsonNull()) && !jsonObj.get("reference_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference_id").toString()));
      }
      if (jsonObj.get("refunds") != null && !jsonObj.get("refunds").isJsonNull()) {
        JsonArray jsonArrayrefunds = jsonObj.getAsJsonArray("refunds");
        if (jsonArrayrefunds != null) {
          // ensure the json data is an array
          if (!jsonObj.get("refunds").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `refunds` to be an array in the JSON string but got `%s`", jsonObj.get("refunds").toString()));
          }

          // validate the optional field `refunds` (array)
          for (int i = 0; i < jsonArrayrefunds.size(); i++) {
            OrderRefundsInner.validateJsonElement(jsonArrayrefunds.get(i));
          };
        }
      }
      if ((jsonObj.get("seat") != null && !jsonObj.get("seat").isJsonNull()) && !jsonObj.get("seat").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `seat` to be a primitive type in the JSON string but got `%s`", jsonObj.get("seat").toString()));
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
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("table") != null && !jsonObj.get("table").isJsonNull()) && !jsonObj.get("table").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `table` to be a primitive type in the JSON string but got `%s`", jsonObj.get("table").toString()));
      }
      if (jsonObj.get("taxes") != null && !jsonObj.get("taxes").isJsonNull()) {
        JsonArray jsonArraytaxes = jsonObj.getAsJsonArray("taxes");
        if (jsonArraytaxes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("taxes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `taxes` to be an array in the JSON string but got `%s`", jsonObj.get("taxes").toString()));
          }

          // validate the optional field `taxes` (array)
          for (int i = 0; i < jsonArraytaxes.size(); i++) {
            OrderTaxesInner.validateJsonElement(jsonArraytaxes.get(i));
          };
        }
      }
      if (jsonObj.get("tenders") != null && !jsonObj.get("tenders").isJsonNull()) {
        JsonArray jsonArraytenders = jsonObj.getAsJsonArray("tenders");
        if (jsonArraytenders != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tenders").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tenders` to be an array in the JSON string but got `%s`", jsonObj.get("tenders").toString()));
          }

          // validate the optional field `tenders` (array)
          for (int i = 0; i < jsonArraytenders.size(); i++) {
            OrderTendersInner.validateJsonElement(jsonArraytenders.get(i));
          };
        }
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
      if ((jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Order.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Order' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Order> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Order.class));

       return (TypeAdapter<T>) new TypeAdapter<Order>() {
           @Override
           public void write(JsonWriter out, Order value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Order read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Order given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Order
   * @throws IOException if the JSON string is invalid with respect to Order
   */
  public static Order fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Order.class);
  }

  /**
   * Convert an instance of Order to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

