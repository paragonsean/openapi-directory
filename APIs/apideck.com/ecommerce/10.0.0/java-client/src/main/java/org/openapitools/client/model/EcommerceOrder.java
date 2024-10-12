/*
 * Ecommerce API
 * Welcome to the Ecommerce API.  You can use this API to access all Ecommerce API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.EcommerceAddress;
import org.openapitools.client.model.EcommerceDiscount;
import org.openapitools.client.model.EcommerceOrderLineItem;
import org.openapitools.client.model.EcommerceOrderStatus;
import org.openapitools.client.model.LinkedEcommerceCustomer;
import org.openapitools.client.model.TrackingItem;
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
 * EcommerceOrder
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:59.974616-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EcommerceOrder {
  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billing_address";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private EcommerceAddress billingAddress;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private Currency currency;

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_CUSTOMER = "customer";
  @SerializedName(SERIALIZED_NAME_CUSTOMER)
  private LinkedEcommerceCustomer customer;

  public static final String SERIALIZED_NAME_DISCOUNTS = "discounts";
  @SerializedName(SERIALIZED_NAME_DISCOUNTS)
  private List<EcommerceDiscount> discounts = new ArrayList<>();

  /**
   * Current fulfillment status of the order.
   */
  @JsonAdapter(FulfillmentStatusEnum.Adapter.class)
  public enum FulfillmentStatusEnum {
    PENDING("pending"),
    
    SHIPPED("shipped"),
    
    PARTIAL("partial"),
    
    DELIVERED("delivered"),
    
    CANCELLED("cancelled"),
    
    RETURNED("returned"),
    
    UNKNOWN("unknown");

    private String value;

    FulfillmentStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static FulfillmentStatusEnum fromValue(String value) {
      for (FulfillmentStatusEnum b : FulfillmentStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<FulfillmentStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final FulfillmentStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public FulfillmentStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return FulfillmentStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      FulfillmentStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_FULFILLMENT_STATUS = "fulfillment_status";
  @SerializedName(SERIALIZED_NAME_FULFILLMENT_STATUS)
  private FulfillmentStatusEnum fulfillmentStatus;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LINE_ITEMS = "line_items";
  @SerializedName(SERIALIZED_NAME_LINE_ITEMS)
  private List<EcommerceOrderLineItem> lineItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_ORDER_NUMBER = "order_number";
  @SerializedName(SERIALIZED_NAME_ORDER_NUMBER)
  private String orderNumber;

  public static final String SERIALIZED_NAME_PAYMENT_METHOD = "payment_method";
  @SerializedName(SERIALIZED_NAME_PAYMENT_METHOD)
  private String paymentMethod;

  /**
   * Current payment status of the order.
   */
  @JsonAdapter(PaymentStatusEnum.Adapter.class)
  public enum PaymentStatusEnum {
    PENDING("pending"),
    
    AUTHORIZED("authorized"),
    
    PAID("paid"),
    
    PARTIAL("partial"),
    
    REFUNDED("refunded"),
    
    VOIDED("voided"),
    
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
      return null;
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

  public static final String SERIALIZED_NAME_SHIPPING_ADDRESS = "shipping_address";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ADDRESS)
  private EcommerceAddress shippingAddress;

  public static final String SERIALIZED_NAME_SHIPPING_COST = "shipping_cost";
  @SerializedName(SERIALIZED_NAME_SHIPPING_COST)
  private String shippingCost;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private EcommerceOrderStatus status;

  public static final String SERIALIZED_NAME_SUB_TOTAL = "sub_total";
  @SerializedName(SERIALIZED_NAME_SUB_TOTAL)
  private String subTotal;

  public static final String SERIALIZED_NAME_TOTAL_AMOUNT = "total_amount";
  @SerializedName(SERIALIZED_NAME_TOTAL_AMOUNT)
  private String totalAmount;

  public static final String SERIALIZED_NAME_TOTAL_DISCOUNT = "total_discount";
  @SerializedName(SERIALIZED_NAME_TOTAL_DISCOUNT)
  private String totalDiscount;

  public static final String SERIALIZED_NAME_TOTAL_TAX = "total_tax";
  @SerializedName(SERIALIZED_NAME_TOTAL_TAX)
  private String totalTax;

  public static final String SERIALIZED_NAME_TRACKING = "tracking";
  @SerializedName(SERIALIZED_NAME_TRACKING)
  private List<TrackingItem> tracking = new ArrayList<>();

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public EcommerceOrder() {
  }

  public EcommerceOrder(
     OffsetDateTime createdAt, 
     String id, 
     OffsetDateTime updatedAt
  ) {
    this();
    this.createdAt = createdAt;
    this.id = id;
    this.updatedAt = updatedAt;
  }

  public EcommerceOrder billingAddress(EcommerceAddress billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Get billingAddress
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public EcommerceAddress getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(EcommerceAddress billingAddress) {
    this.billingAddress = billingAddress;
  }


  /**
   * The date and time when the object was created.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



  public EcommerceOrder currency(Currency currency) {
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


  public EcommerceOrder customMappings(Object customMappings) {
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


  public EcommerceOrder customer(LinkedEcommerceCustomer customer) {
    this.customer = customer;
    return this;
  }

  /**
   * Get customer
   * @return customer
   */
  @javax.annotation.Nullable
  public LinkedEcommerceCustomer getCustomer() {
    return customer;
  }

  public void setCustomer(LinkedEcommerceCustomer customer) {
    this.customer = customer;
  }


  public EcommerceOrder discounts(List<EcommerceDiscount> discounts) {
    this.discounts = discounts;
    return this;
  }

  public EcommerceOrder addDiscountsItem(EcommerceDiscount discountsItem) {
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
  public List<EcommerceDiscount> getDiscounts() {
    return discounts;
  }

  public void setDiscounts(List<EcommerceDiscount> discounts) {
    this.discounts = discounts;
  }


  public EcommerceOrder fulfillmentStatus(FulfillmentStatusEnum fulfillmentStatus) {
    this.fulfillmentStatus = fulfillmentStatus;
    return this;
  }

  /**
   * Current fulfillment status of the order.
   * @return fulfillmentStatus
   */
  @javax.annotation.Nullable
  public FulfillmentStatusEnum getFulfillmentStatus() {
    return fulfillmentStatus;
  }

  public void setFulfillmentStatus(FulfillmentStatusEnum fulfillmentStatus) {
    this.fulfillmentStatus = fulfillmentStatus;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }



  public EcommerceOrder lineItems(List<EcommerceOrderLineItem> lineItems) {
    this.lineItems = lineItems;
    return this;
  }

  public EcommerceOrder addLineItemsItem(EcommerceOrderLineItem lineItemsItem) {
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
  public List<EcommerceOrderLineItem> getLineItems() {
    return lineItems;
  }

  public void setLineItems(List<EcommerceOrderLineItem> lineItems) {
    this.lineItems = lineItems;
  }


  public EcommerceOrder note(String note) {
    this.note = note;
    return this;
  }

  /**
   * Note for the order.
   * @return note
   */
  @javax.annotation.Nullable
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }


  public EcommerceOrder orderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
    return this;
  }

  /**
   * Order number, if any.
   * @return orderNumber
   */
  @javax.annotation.Nullable
  public String getOrderNumber() {
    return orderNumber;
  }

  public void setOrderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
  }


  public EcommerceOrder paymentMethod(String paymentMethod) {
    this.paymentMethod = paymentMethod;
    return this;
  }

  /**
   * Payment method used for this order.
   * @return paymentMethod
   */
  @javax.annotation.Nullable
  public String getPaymentMethod() {
    return paymentMethod;
  }

  public void setPaymentMethod(String paymentMethod) {
    this.paymentMethod = paymentMethod;
  }


  public EcommerceOrder paymentStatus(PaymentStatusEnum paymentStatus) {
    this.paymentStatus = paymentStatus;
    return this;
  }

  /**
   * Current payment status of the order.
   * @return paymentStatus
   */
  @javax.annotation.Nullable
  public PaymentStatusEnum getPaymentStatus() {
    return paymentStatus;
  }

  public void setPaymentStatus(PaymentStatusEnum paymentStatus) {
    this.paymentStatus = paymentStatus;
  }


  public EcommerceOrder shippingAddress(EcommerceAddress shippingAddress) {
    this.shippingAddress = shippingAddress;
    return this;
  }

  /**
   * Get shippingAddress
   * @return shippingAddress
   */
  @javax.annotation.Nullable
  public EcommerceAddress getShippingAddress() {
    return shippingAddress;
  }

  public void setShippingAddress(EcommerceAddress shippingAddress) {
    this.shippingAddress = shippingAddress;
  }


  public EcommerceOrder shippingCost(String shippingCost) {
    this.shippingCost = shippingCost;
    return this;
  }

  /**
   * Shipping cost, if any.
   * @return shippingCost
   */
  @javax.annotation.Nullable
  public String getShippingCost() {
    return shippingCost;
  }

  public void setShippingCost(String shippingCost) {
    this.shippingCost = shippingCost;
  }


  public EcommerceOrder status(EcommerceOrderStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public EcommerceOrderStatus getStatus() {
    return status;
  }

  public void setStatus(EcommerceOrderStatus status) {
    this.status = status;
  }


  public EcommerceOrder subTotal(String subTotal) {
    this.subTotal = subTotal;
    return this;
  }

  /**
   * Sub-total amount, normally before tax.
   * @return subTotal
   */
  @javax.annotation.Nullable
  public String getSubTotal() {
    return subTotal;
  }

  public void setSubTotal(String subTotal) {
    this.subTotal = subTotal;
  }


  public EcommerceOrder totalAmount(String totalAmount) {
    this.totalAmount = totalAmount;
    return this;
  }

  /**
   * Total amount due.
   * @return totalAmount
   */
  @javax.annotation.Nullable
  public String getTotalAmount() {
    return totalAmount;
  }

  public void setTotalAmount(String totalAmount) {
    this.totalAmount = totalAmount;
  }


  public EcommerceOrder totalDiscount(String totalDiscount) {
    this.totalDiscount = totalDiscount;
    return this;
  }

  /**
   * Total discount, if any.
   * @return totalDiscount
   */
  @javax.annotation.Nullable
  public String getTotalDiscount() {
    return totalDiscount;
  }

  public void setTotalDiscount(String totalDiscount) {
    this.totalDiscount = totalDiscount;
  }


  public EcommerceOrder totalTax(String totalTax) {
    this.totalTax = totalTax;
    return this;
  }

  /**
   * Total tax, if any.
   * @return totalTax
   */
  @javax.annotation.Nullable
  public String getTotalTax() {
    return totalTax;
  }

  public void setTotalTax(String totalTax) {
    this.totalTax = totalTax;
  }


  public EcommerceOrder tracking(List<TrackingItem> tracking) {
    this.tracking = tracking;
    return this;
  }

  public EcommerceOrder addTrackingItem(TrackingItem trackingItem) {
    if (this.tracking == null) {
      this.tracking = new ArrayList<>();
    }
    this.tracking.add(trackingItem);
    return this;
  }

  /**
   * Get tracking
   * @return tracking
   */
  @javax.annotation.Nullable
  public List<TrackingItem> getTracking() {
    return tracking;
  }

  public void setTracking(List<TrackingItem> tracking) {
    this.tracking = tracking;
  }


  /**
   * The date and time when the object was last updated.
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EcommerceOrder ecommerceOrder = (EcommerceOrder) o;
    return Objects.equals(this.billingAddress, ecommerceOrder.billingAddress) &&
        Objects.equals(this.createdAt, ecommerceOrder.createdAt) &&
        Objects.equals(this.currency, ecommerceOrder.currency) &&
        Objects.equals(this.customMappings, ecommerceOrder.customMappings) &&
        Objects.equals(this.customer, ecommerceOrder.customer) &&
        Objects.equals(this.discounts, ecommerceOrder.discounts) &&
        Objects.equals(this.fulfillmentStatus, ecommerceOrder.fulfillmentStatus) &&
        Objects.equals(this.id, ecommerceOrder.id) &&
        Objects.equals(this.lineItems, ecommerceOrder.lineItems) &&
        Objects.equals(this.note, ecommerceOrder.note) &&
        Objects.equals(this.orderNumber, ecommerceOrder.orderNumber) &&
        Objects.equals(this.paymentMethod, ecommerceOrder.paymentMethod) &&
        Objects.equals(this.paymentStatus, ecommerceOrder.paymentStatus) &&
        Objects.equals(this.shippingAddress, ecommerceOrder.shippingAddress) &&
        Objects.equals(this.shippingCost, ecommerceOrder.shippingCost) &&
        Objects.equals(this.status, ecommerceOrder.status) &&
        Objects.equals(this.subTotal, ecommerceOrder.subTotal) &&
        Objects.equals(this.totalAmount, ecommerceOrder.totalAmount) &&
        Objects.equals(this.totalDiscount, ecommerceOrder.totalDiscount) &&
        Objects.equals(this.totalTax, ecommerceOrder.totalTax) &&
        Objects.equals(this.tracking, ecommerceOrder.tracking) &&
        Objects.equals(this.updatedAt, ecommerceOrder.updatedAt);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(billingAddress, createdAt, currency, customMappings, customer, discounts, fulfillmentStatus, id, lineItems, note, orderNumber, paymentMethod, paymentStatus, shippingAddress, shippingCost, status, subTotal, totalAmount, totalDiscount, totalTax, tracking, updatedAt);
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
    sb.append("class EcommerceOrder {\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    customer: ").append(toIndentedString(customer)).append("\n");
    sb.append("    discounts: ").append(toIndentedString(discounts)).append("\n");
    sb.append("    fulfillmentStatus: ").append(toIndentedString(fulfillmentStatus)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lineItems: ").append(toIndentedString(lineItems)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    orderNumber: ").append(toIndentedString(orderNumber)).append("\n");
    sb.append("    paymentMethod: ").append(toIndentedString(paymentMethod)).append("\n");
    sb.append("    paymentStatus: ").append(toIndentedString(paymentStatus)).append("\n");
    sb.append("    shippingAddress: ").append(toIndentedString(shippingAddress)).append("\n");
    sb.append("    shippingCost: ").append(toIndentedString(shippingCost)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subTotal: ").append(toIndentedString(subTotal)).append("\n");
    sb.append("    totalAmount: ").append(toIndentedString(totalAmount)).append("\n");
    sb.append("    totalDiscount: ").append(toIndentedString(totalDiscount)).append("\n");
    sb.append("    totalTax: ").append(toIndentedString(totalTax)).append("\n");
    sb.append("    tracking: ").append(toIndentedString(tracking)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("billing_address");
    openapiFields.add("created_at");
    openapiFields.add("currency");
    openapiFields.add("custom_mappings");
    openapiFields.add("customer");
    openapiFields.add("discounts");
    openapiFields.add("fulfillment_status");
    openapiFields.add("id");
    openapiFields.add("line_items");
    openapiFields.add("note");
    openapiFields.add("order_number");
    openapiFields.add("payment_method");
    openapiFields.add("payment_status");
    openapiFields.add("shipping_address");
    openapiFields.add("shipping_cost");
    openapiFields.add("status");
    openapiFields.add("sub_total");
    openapiFields.add("total_amount");
    openapiFields.add("total_discount");
    openapiFields.add("total_tax");
    openapiFields.add("tracking");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EcommerceOrder
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EcommerceOrder.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EcommerceOrder is not found in the empty JSON string", EcommerceOrder.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EcommerceOrder.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EcommerceOrder` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EcommerceOrder.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `billing_address`
      if (jsonObj.get("billing_address") != null && !jsonObj.get("billing_address").isJsonNull()) {
        EcommerceAddress.validateJsonElement(jsonObj.get("billing_address"));
      }
      // validate the optional field `currency`
      if (jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("currency"));
      }
      // validate the optional field `customer`
      if (jsonObj.get("customer") != null && !jsonObj.get("customer").isJsonNull()) {
        LinkedEcommerceCustomer.validateJsonElement(jsonObj.get("customer"));
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
            EcommerceDiscount.validateJsonElement(jsonArraydiscounts.get(i));
          };
        }
      }
      if ((jsonObj.get("fulfillment_status") != null && !jsonObj.get("fulfillment_status").isJsonNull()) && !jsonObj.get("fulfillment_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fulfillment_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fulfillment_status").toString()));
      }
      // validate the optional field `fulfillment_status`
      if (jsonObj.get("fulfillment_status") != null && !jsonObj.get("fulfillment_status").isJsonNull()) {
        FulfillmentStatusEnum.validateJsonElement(jsonObj.get("fulfillment_status"));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
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
            EcommerceOrderLineItem.validateJsonElement(jsonArraylineItems.get(i));
          };
        }
      }
      if ((jsonObj.get("note") != null && !jsonObj.get("note").isJsonNull()) && !jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
      if ((jsonObj.get("order_number") != null && !jsonObj.get("order_number").isJsonNull()) && !jsonObj.get("order_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_number").toString()));
      }
      if ((jsonObj.get("payment_method") != null && !jsonObj.get("payment_method").isJsonNull()) && !jsonObj.get("payment_method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_method").toString()));
      }
      if ((jsonObj.get("payment_status") != null && !jsonObj.get("payment_status").isJsonNull()) && !jsonObj.get("payment_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_status").toString()));
      }
      // validate the optional field `payment_status`
      if (jsonObj.get("payment_status") != null && !jsonObj.get("payment_status").isJsonNull()) {
        PaymentStatusEnum.validateJsonElement(jsonObj.get("payment_status"));
      }
      // validate the optional field `shipping_address`
      if (jsonObj.get("shipping_address") != null && !jsonObj.get("shipping_address").isJsonNull()) {
        EcommerceAddress.validateJsonElement(jsonObj.get("shipping_address"));
      }
      if ((jsonObj.get("shipping_cost") != null && !jsonObj.get("shipping_cost").isJsonNull()) && !jsonObj.get("shipping_cost").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipping_cost` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipping_cost").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        EcommerceOrderStatus.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("sub_total") != null && !jsonObj.get("sub_total").isJsonNull()) && !jsonObj.get("sub_total").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sub_total` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sub_total").toString()));
      }
      if ((jsonObj.get("total_amount") != null && !jsonObj.get("total_amount").isJsonNull()) && !jsonObj.get("total_amount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_amount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_amount").toString()));
      }
      if ((jsonObj.get("total_discount") != null && !jsonObj.get("total_discount").isJsonNull()) && !jsonObj.get("total_discount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_discount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_discount").toString()));
      }
      if ((jsonObj.get("total_tax") != null && !jsonObj.get("total_tax").isJsonNull()) && !jsonObj.get("total_tax").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_tax` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_tax").toString()));
      }
      if (jsonObj.get("tracking") != null && !jsonObj.get("tracking").isJsonNull()) {
        JsonArray jsonArraytracking = jsonObj.getAsJsonArray("tracking");
        if (jsonArraytracking != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tracking").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tracking` to be an array in the JSON string but got `%s`", jsonObj.get("tracking").toString()));
          }

          // validate the optional field `tracking` (array)
          for (int i = 0; i < jsonArraytracking.size(); i++) {
            TrackingItem.validateJsonElement(jsonArraytracking.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EcommerceOrder.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EcommerceOrder' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EcommerceOrder> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EcommerceOrder.class));

       return (TypeAdapter<T>) new TypeAdapter<EcommerceOrder>() {
           @Override
           public void write(JsonWriter out, EcommerceOrder value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EcommerceOrder read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EcommerceOrder given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EcommerceOrder
   * @throws IOException if the JSON string is invalid with respect to EcommerceOrder
   */
  public static EcommerceOrder fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EcommerceOrder.class);
  }

  /**
   * Convert an instance of EcommerceOrder to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

