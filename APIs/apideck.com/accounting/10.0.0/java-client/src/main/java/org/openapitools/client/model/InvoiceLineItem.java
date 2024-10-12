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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.LinkedInvoiceItem;
import org.openapitools.client.model.LinkedLedgerAccount;
import org.openapitools.client.model.LinkedTaxRate;
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
 * InvoiceLineItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:31.900974-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InvoiceLineItem {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_DEPARTMENT_ID = "department_id";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT_ID)
  private String departmentId;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISCOUNT_AMOUNT = "discount_amount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_AMOUNT)
  private BigDecimal discountAmount;

  public static final String SERIALIZED_NAME_DISCOUNT_PERCENTAGE = "discount_percentage";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_PERCENTAGE)
  private BigDecimal discountPercentage;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_ITEM = "item";
  @SerializedName(SERIALIZED_NAME_ITEM)
  private LinkedInvoiceItem item;

  public static final String SERIALIZED_NAME_LEDGER_ACCOUNT = "ledger_account";
  @SerializedName(SERIALIZED_NAME_LEDGER_ACCOUNT)
  private LinkedLedgerAccount ledgerAccount;

  public static final String SERIALIZED_NAME_LINE_NUMBER = "line_number";
  @SerializedName(SERIALIZED_NAME_LINE_NUMBER)
  private Integer lineNumber;

  public static final String SERIALIZED_NAME_LOCATION_ID = "location_id";
  @SerializedName(SERIALIZED_NAME_LOCATION_ID)
  private String locationId;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private BigDecimal quantity;

  public static final String SERIALIZED_NAME_ROW_ID = "row_id";
  @SerializedName(SERIALIZED_NAME_ROW_ID)
  private String rowId;

  public static final String SERIALIZED_NAME_ROW_VERSION = "row_version";
  @SerializedName(SERIALIZED_NAME_ROW_VERSION)
  private String rowVersion;

  public static final String SERIALIZED_NAME_TAX_AMOUNT = "tax_amount";
  @SerializedName(SERIALIZED_NAME_TAX_AMOUNT)
  private BigDecimal taxAmount;

  public static final String SERIALIZED_NAME_TAX_RATE = "tax_rate";
  @SerializedName(SERIALIZED_NAME_TAX_RATE)
  private LinkedTaxRate taxRate;

  public static final String SERIALIZED_NAME_TOTAL_AMOUNT = "total_amount";
  @SerializedName(SERIALIZED_NAME_TOTAL_AMOUNT)
  private BigDecimal totalAmount;

  /**
   * Item type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    SALES_ITEM("sales_item"),
    
    DISCOUNT("discount"),
    
    INFO("info"),
    
    SUB_TOTAL("sub_total");

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

  public static final String SERIALIZED_NAME_UNIT_OF_MEASURE = "unit_of_measure";
  @SerializedName(SERIALIZED_NAME_UNIT_OF_MEASURE)
  private String unitOfMeasure;

  public static final String SERIALIZED_NAME_UNIT_PRICE = "unit_price";
  @SerializedName(SERIALIZED_NAME_UNIT_PRICE)
  private BigDecimal unitPrice;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public InvoiceLineItem() {
  }

  public InvoiceLineItem(
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

  public InvoiceLineItem code(String code) {
    this.code = code;
    return this;
  }

  /**
   * User defined item code
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
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



  public InvoiceLineItem customMappings(Object customMappings) {
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


  public InvoiceLineItem departmentId(String departmentId) {
    this.departmentId = departmentId;
    return this;
  }

  /**
   * Department id
   * @return departmentId
   */
  @javax.annotation.Nullable
  public String getDepartmentId() {
    return departmentId;
  }

  public void setDepartmentId(String departmentId) {
    this.departmentId = departmentId;
  }


  public InvoiceLineItem description(String description) {
    this.description = description;
    return this;
  }

  /**
   * User defined description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public InvoiceLineItem discountAmount(BigDecimal discountAmount) {
    this.discountAmount = discountAmount;
    return this;
  }

  /**
   * Discount amount applied to the line item when supported downstream.
   * @return discountAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getDiscountAmount() {
    return discountAmount;
  }

  public void setDiscountAmount(BigDecimal discountAmount) {
    this.discountAmount = discountAmount;
  }


  public InvoiceLineItem discountPercentage(BigDecimal discountPercentage) {
    this.discountPercentage = discountPercentage;
    return this;
  }

  /**
   * Discount percentage applied to the line item when supported downstream.
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
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public InvoiceLineItem item(LinkedInvoiceItem item) {
    this.item = item;
    return this;
  }

  /**
   * Get item
   * @return item
   */
  @javax.annotation.Nullable
  public LinkedInvoiceItem getItem() {
    return item;
  }

  public void setItem(LinkedInvoiceItem item) {
    this.item = item;
  }


  public InvoiceLineItem ledgerAccount(LinkedLedgerAccount ledgerAccount) {
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


  public InvoiceLineItem lineNumber(Integer lineNumber) {
    this.lineNumber = lineNumber;
    return this;
  }

  /**
   * Line number in the invoice
   * @return lineNumber
   */
  @javax.annotation.Nullable
  public Integer getLineNumber() {
    return lineNumber;
  }

  public void setLineNumber(Integer lineNumber) {
    this.lineNumber = lineNumber;
  }


  public InvoiceLineItem locationId(String locationId) {
    this.locationId = locationId;
    return this;
  }

  /**
   * Location id
   * @return locationId
   */
  @javax.annotation.Nullable
  public String getLocationId() {
    return locationId;
  }

  public void setLocationId(String locationId) {
    this.locationId = locationId;
  }


  public InvoiceLineItem quantity(BigDecimal quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * Get quantity
   * @return quantity
   */
  @javax.annotation.Nullable
  public BigDecimal getQuantity() {
    return quantity;
  }

  public void setQuantity(BigDecimal quantity) {
    this.quantity = quantity;
  }


  public InvoiceLineItem rowId(String rowId) {
    this.rowId = rowId;
    return this;
  }

  /**
   * Row ID
   * @return rowId
   */
  @javax.annotation.Nullable
  public String getRowId() {
    return rowId;
  }

  public void setRowId(String rowId) {
    this.rowId = rowId;
  }


  public InvoiceLineItem rowVersion(String rowVersion) {
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


  public InvoiceLineItem taxAmount(BigDecimal taxAmount) {
    this.taxAmount = taxAmount;
    return this;
  }

  /**
   * Tax amount
   * @return taxAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getTaxAmount() {
    return taxAmount;
  }

  public void setTaxAmount(BigDecimal taxAmount) {
    this.taxAmount = taxAmount;
  }


  public InvoiceLineItem taxRate(LinkedTaxRate taxRate) {
    this.taxRate = taxRate;
    return this;
  }

  /**
   * Get taxRate
   * @return taxRate
   */
  @javax.annotation.Nullable
  public LinkedTaxRate getTaxRate() {
    return taxRate;
  }

  public void setTaxRate(LinkedTaxRate taxRate) {
    this.taxRate = taxRate;
  }


  public InvoiceLineItem totalAmount(BigDecimal totalAmount) {
    this.totalAmount = totalAmount;
    return this;
  }

  /**
   * Total amount of the line item
   * @return totalAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalAmount() {
    return totalAmount;
  }

  public void setTotalAmount(BigDecimal totalAmount) {
    this.totalAmount = totalAmount;
  }


  public InvoiceLineItem type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Item type
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public InvoiceLineItem unitOfMeasure(String unitOfMeasure) {
    this.unitOfMeasure = unitOfMeasure;
    return this;
  }

  /**
   * Description of the unit type the item is sold as, ie: kg, hour.
   * @return unitOfMeasure
   */
  @javax.annotation.Nullable
  public String getUnitOfMeasure() {
    return unitOfMeasure;
  }

  public void setUnitOfMeasure(String unitOfMeasure) {
    this.unitOfMeasure = unitOfMeasure;
  }


  public InvoiceLineItem unitPrice(BigDecimal unitPrice) {
    this.unitPrice = unitPrice;
    return this;
  }

  /**
   * Get unitPrice
   * @return unitPrice
   */
  @javax.annotation.Nullable
  public BigDecimal getUnitPrice() {
    return unitPrice;
  }

  public void setUnitPrice(BigDecimal unitPrice) {
    this.unitPrice = unitPrice;
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
    InvoiceLineItem invoiceLineItem = (InvoiceLineItem) o;
    return Objects.equals(this.code, invoiceLineItem.code) &&
        Objects.equals(this.createdAt, invoiceLineItem.createdAt) &&
        Objects.equals(this.createdBy, invoiceLineItem.createdBy) &&
        Objects.equals(this.customMappings, invoiceLineItem.customMappings) &&
        Objects.equals(this.departmentId, invoiceLineItem.departmentId) &&
        Objects.equals(this.description, invoiceLineItem.description) &&
        Objects.equals(this.discountAmount, invoiceLineItem.discountAmount) &&
        Objects.equals(this.discountPercentage, invoiceLineItem.discountPercentage) &&
        Objects.equals(this.id, invoiceLineItem.id) &&
        Objects.equals(this.item, invoiceLineItem.item) &&
        Objects.equals(this.ledgerAccount, invoiceLineItem.ledgerAccount) &&
        Objects.equals(this.lineNumber, invoiceLineItem.lineNumber) &&
        Objects.equals(this.locationId, invoiceLineItem.locationId) &&
        Objects.equals(this.quantity, invoiceLineItem.quantity) &&
        Objects.equals(this.rowId, invoiceLineItem.rowId) &&
        Objects.equals(this.rowVersion, invoiceLineItem.rowVersion) &&
        Objects.equals(this.taxAmount, invoiceLineItem.taxAmount) &&
        Objects.equals(this.taxRate, invoiceLineItem.taxRate) &&
        Objects.equals(this.totalAmount, invoiceLineItem.totalAmount) &&
        Objects.equals(this.type, invoiceLineItem.type) &&
        Objects.equals(this.unitOfMeasure, invoiceLineItem.unitOfMeasure) &&
        Objects.equals(this.unitPrice, invoiceLineItem.unitPrice) &&
        Objects.equals(this.updatedAt, invoiceLineItem.updatedAt) &&
        Objects.equals(this.updatedBy, invoiceLineItem.updatedBy);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, createdAt, createdBy, customMappings, departmentId, description, discountAmount, discountPercentage, id, item, ledgerAccount, lineNumber, locationId, quantity, rowId, rowVersion, taxAmount, taxRate, totalAmount, type, unitOfMeasure, unitPrice, updatedAt, updatedBy);
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
    sb.append("class InvoiceLineItem {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    departmentId: ").append(toIndentedString(departmentId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    discountAmount: ").append(toIndentedString(discountAmount)).append("\n");
    sb.append("    discountPercentage: ").append(toIndentedString(discountPercentage)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    item: ").append(toIndentedString(item)).append("\n");
    sb.append("    ledgerAccount: ").append(toIndentedString(ledgerAccount)).append("\n");
    sb.append("    lineNumber: ").append(toIndentedString(lineNumber)).append("\n");
    sb.append("    locationId: ").append(toIndentedString(locationId)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    rowId: ").append(toIndentedString(rowId)).append("\n");
    sb.append("    rowVersion: ").append(toIndentedString(rowVersion)).append("\n");
    sb.append("    taxAmount: ").append(toIndentedString(taxAmount)).append("\n");
    sb.append("    taxRate: ").append(toIndentedString(taxRate)).append("\n");
    sb.append("    totalAmount: ").append(toIndentedString(totalAmount)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    unitOfMeasure: ").append(toIndentedString(unitOfMeasure)).append("\n");
    sb.append("    unitPrice: ").append(toIndentedString(unitPrice)).append("\n");
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
    openapiFields.add("code");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("custom_mappings");
    openapiFields.add("department_id");
    openapiFields.add("description");
    openapiFields.add("discount_amount");
    openapiFields.add("discount_percentage");
    openapiFields.add("id");
    openapiFields.add("item");
    openapiFields.add("ledger_account");
    openapiFields.add("line_number");
    openapiFields.add("location_id");
    openapiFields.add("quantity");
    openapiFields.add("row_id");
    openapiFields.add("row_version");
    openapiFields.add("tax_amount");
    openapiFields.add("tax_rate");
    openapiFields.add("total_amount");
    openapiFields.add("type");
    openapiFields.add("unit_of_measure");
    openapiFields.add("unit_price");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InvoiceLineItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InvoiceLineItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InvoiceLineItem is not found in the empty JSON string", InvoiceLineItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InvoiceLineItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InvoiceLineItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) && !jsonObj.get("created_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by").toString()));
      }
      if ((jsonObj.get("department_id") != null && !jsonObj.get("department_id").isJsonNull()) && !jsonObj.get("department_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `department_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("department_id").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `item`
      if (jsonObj.get("item") != null && !jsonObj.get("item").isJsonNull()) {
        LinkedInvoiceItem.validateJsonElement(jsonObj.get("item"));
      }
      // validate the optional field `ledger_account`
      if (jsonObj.get("ledger_account") != null && !jsonObj.get("ledger_account").isJsonNull()) {
        LinkedLedgerAccount.validateJsonElement(jsonObj.get("ledger_account"));
      }
      if ((jsonObj.get("location_id") != null && !jsonObj.get("location_id").isJsonNull()) && !jsonObj.get("location_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location_id").toString()));
      }
      if ((jsonObj.get("row_id") != null && !jsonObj.get("row_id").isJsonNull()) && !jsonObj.get("row_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `row_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("row_id").toString()));
      }
      if ((jsonObj.get("row_version") != null && !jsonObj.get("row_version").isJsonNull()) && !jsonObj.get("row_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `row_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("row_version").toString()));
      }
      // validate the optional field `tax_rate`
      if (jsonObj.get("tax_rate") != null && !jsonObj.get("tax_rate").isJsonNull()) {
        LinkedTaxRate.validateJsonElement(jsonObj.get("tax_rate"));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
      if ((jsonObj.get("unit_of_measure") != null && !jsonObj.get("unit_of_measure").isJsonNull()) && !jsonObj.get("unit_of_measure").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unit_of_measure` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unit_of_measure").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InvoiceLineItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InvoiceLineItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InvoiceLineItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InvoiceLineItem.class));

       return (TypeAdapter<T>) new TypeAdapter<InvoiceLineItem>() {
           @Override
           public void write(JsonWriter out, InvoiceLineItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InvoiceLineItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InvoiceLineItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InvoiceLineItem
   * @throws IOException if the JSON string is invalid with respect to InvoiceLineItem
   */
  public static InvoiceLineItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InvoiceLineItem.class);
  }

  /**
   * Convert an instance of InvoiceLineItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

