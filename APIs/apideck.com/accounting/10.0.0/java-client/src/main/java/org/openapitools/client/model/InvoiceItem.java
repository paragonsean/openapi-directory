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
import java.util.Arrays;
import org.openapitools.client.model.InvoiceItemPurchaseDetails;
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
 * InvoiceItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:31.900974-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InvoiceItem {
  public static final String SERIALIZED_NAME_ACTIVE = "active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_ASSET_ACCOUNT = "asset_account";
  @SerializedName(SERIALIZED_NAME_ASSET_ACCOUNT)
  private LinkedLedgerAccount assetAccount;

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

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXPENSE_ACCOUNT = "expense_account";
  @SerializedName(SERIALIZED_NAME_EXPENSE_ACCOUNT)
  private LinkedLedgerAccount expenseAccount;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INCOME_ACCOUNT = "income_account";
  @SerializedName(SERIALIZED_NAME_INCOME_ACCOUNT)
  private LinkedLedgerAccount incomeAccount;

  public static final String SERIALIZED_NAME_INVENTORY_DATE = "inventory_date";
  @SerializedName(SERIALIZED_NAME_INVENTORY_DATE)
  private LocalDate inventoryDate;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PURCHASE_DETAILS = "purchase_details";
  @SerializedName(SERIALIZED_NAME_PURCHASE_DETAILS)
  private InvoiceItemPurchaseDetails purchaseDetails;

  public static final String SERIALIZED_NAME_PURCHASED = "purchased";
  @SerializedName(SERIALIZED_NAME_PURCHASED)
  private Boolean purchased;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private BigDecimal quantity;

  public static final String SERIALIZED_NAME_ROW_VERSION = "row_version";
  @SerializedName(SERIALIZED_NAME_ROW_VERSION)
  private String rowVersion;

  public static final String SERIALIZED_NAME_SALES_DETAILS = "sales_details";
  @SerializedName(SERIALIZED_NAME_SALES_DETAILS)
  private InvoiceItemPurchaseDetails salesDetails;

  public static final String SERIALIZED_NAME_SOLD = "sold";
  @SerializedName(SERIALIZED_NAME_SOLD)
  private Boolean sold;

  public static final String SERIALIZED_NAME_TAXABLE = "taxable";
  @SerializedName(SERIALIZED_NAME_TAXABLE)
  private Boolean taxable;

  public static final String SERIALIZED_NAME_TRACKED = "tracked";
  @SerializedName(SERIALIZED_NAME_TRACKED)
  private Boolean tracked;

  public static final String SERIALIZED_NAME_TRACKING_CATEGORY = "tracking_category";
  @SerializedName(SERIALIZED_NAME_TRACKING_CATEGORY)
  private LinkedTrackingCategory trackingCategory;

  /**
   * Item type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    INVENTORY("inventory"),
    
    SERVICE("service"),
    
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

  public static final String SERIALIZED_NAME_UNIT_PRICE = "unit_price";
  @SerializedName(SERIALIZED_NAME_UNIT_PRICE)
  private BigDecimal unitPrice;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public InvoiceItem() {
  }

  public InvoiceItem(
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

  public InvoiceItem active(Boolean active) {
    this.active = active;
    return this;
  }

  /**
   * Get active
   * @return active
   */
  @javax.annotation.Nullable
  public Boolean getActive() {
    return active;
  }

  public void setActive(Boolean active) {
    this.active = active;
  }


  public InvoiceItem assetAccount(LinkedLedgerAccount assetAccount) {
    this.assetAccount = assetAccount;
    return this;
  }

  /**
   * Get assetAccount
   * @return assetAccount
   */
  @javax.annotation.Nullable
  public LinkedLedgerAccount getAssetAccount() {
    return assetAccount;
  }

  public void setAssetAccount(LinkedLedgerAccount assetAccount) {
    this.assetAccount = assetAccount;
  }


  public InvoiceItem code(String code) {
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



  public InvoiceItem customMappings(Object customMappings) {
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


  public InvoiceItem description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A short description of the item
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public InvoiceItem expenseAccount(LinkedLedgerAccount expenseAccount) {
    this.expenseAccount = expenseAccount;
    return this;
  }

  /**
   * Get expenseAccount
   * @return expenseAccount
   */
  @javax.annotation.Nullable
  public LinkedLedgerAccount getExpenseAccount() {
    return expenseAccount;
  }

  public void setExpenseAccount(LinkedLedgerAccount expenseAccount) {
    this.expenseAccount = expenseAccount;
  }


  /**
   * The ID of the item.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public InvoiceItem incomeAccount(LinkedLedgerAccount incomeAccount) {
    this.incomeAccount = incomeAccount;
    return this;
  }

  /**
   * Get incomeAccount
   * @return incomeAccount
   */
  @javax.annotation.Nullable
  public LinkedLedgerAccount getIncomeAccount() {
    return incomeAccount;
  }

  public void setIncomeAccount(LinkedLedgerAccount incomeAccount) {
    this.incomeAccount = incomeAccount;
  }


  public InvoiceItem inventoryDate(LocalDate inventoryDate) {
    this.inventoryDate = inventoryDate;
    return this;
  }

  /**
   * The date of opening balance if inventory item is tracked - YYYY-MM-DD.
   * @return inventoryDate
   */
  @javax.annotation.Nullable
  public LocalDate getInventoryDate() {
    return inventoryDate;
  }

  public void setInventoryDate(LocalDate inventoryDate) {
    this.inventoryDate = inventoryDate;
  }


  public InvoiceItem name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Item name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public InvoiceItem purchaseDetails(InvoiceItemPurchaseDetails purchaseDetails) {
    this.purchaseDetails = purchaseDetails;
    return this;
  }

  /**
   * Get purchaseDetails
   * @return purchaseDetails
   */
  @javax.annotation.Nullable
  public InvoiceItemPurchaseDetails getPurchaseDetails() {
    return purchaseDetails;
  }

  public void setPurchaseDetails(InvoiceItemPurchaseDetails purchaseDetails) {
    this.purchaseDetails = purchaseDetails;
  }


  public InvoiceItem purchased(Boolean purchased) {
    this.purchased = purchased;
    return this;
  }

  /**
   * Item is available for purchase transactions
   * @return purchased
   */
  @javax.annotation.Nullable
  public Boolean getPurchased() {
    return purchased;
  }

  public void setPurchased(Boolean purchased) {
    this.purchased = purchased;
  }


  public InvoiceItem quantity(BigDecimal quantity) {
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


  public InvoiceItem rowVersion(String rowVersion) {
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


  public InvoiceItem salesDetails(InvoiceItemPurchaseDetails salesDetails) {
    this.salesDetails = salesDetails;
    return this;
  }

  /**
   * Get salesDetails
   * @return salesDetails
   */
  @javax.annotation.Nullable
  public InvoiceItemPurchaseDetails getSalesDetails() {
    return salesDetails;
  }

  public void setSalesDetails(InvoiceItemPurchaseDetails salesDetails) {
    this.salesDetails = salesDetails;
  }


  public InvoiceItem sold(Boolean sold) {
    this.sold = sold;
    return this;
  }

  /**
   * Item will be available on sales transactions
   * @return sold
   */
  @javax.annotation.Nullable
  public Boolean getSold() {
    return sold;
  }

  public void setSold(Boolean sold) {
    this.sold = sold;
  }


  public InvoiceItem taxable(Boolean taxable) {
    this.taxable = taxable;
    return this;
  }

  /**
   * If true, transactions for this item are taxable
   * @return taxable
   */
  @javax.annotation.Nullable
  public Boolean getTaxable() {
    return taxable;
  }

  public void setTaxable(Boolean taxable) {
    this.taxable = taxable;
  }


  public InvoiceItem tracked(Boolean tracked) {
    this.tracked = tracked;
    return this;
  }

  /**
   * Item is inventoried
   * @return tracked
   */
  @javax.annotation.Nullable
  public Boolean getTracked() {
    return tracked;
  }

  public void setTracked(Boolean tracked) {
    this.tracked = tracked;
  }


  public InvoiceItem trackingCategory(LinkedTrackingCategory trackingCategory) {
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


  public InvoiceItem type(TypeEnum type) {
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


  public InvoiceItem unitPrice(BigDecimal unitPrice) {
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
    InvoiceItem invoiceItem = (InvoiceItem) o;
    return Objects.equals(this.active, invoiceItem.active) &&
        Objects.equals(this.assetAccount, invoiceItem.assetAccount) &&
        Objects.equals(this.code, invoiceItem.code) &&
        Objects.equals(this.createdAt, invoiceItem.createdAt) &&
        Objects.equals(this.createdBy, invoiceItem.createdBy) &&
        Objects.equals(this.customMappings, invoiceItem.customMappings) &&
        Objects.equals(this.description, invoiceItem.description) &&
        Objects.equals(this.expenseAccount, invoiceItem.expenseAccount) &&
        Objects.equals(this.id, invoiceItem.id) &&
        Objects.equals(this.incomeAccount, invoiceItem.incomeAccount) &&
        Objects.equals(this.inventoryDate, invoiceItem.inventoryDate) &&
        Objects.equals(this.name, invoiceItem.name) &&
        Objects.equals(this.purchaseDetails, invoiceItem.purchaseDetails) &&
        Objects.equals(this.purchased, invoiceItem.purchased) &&
        Objects.equals(this.quantity, invoiceItem.quantity) &&
        Objects.equals(this.rowVersion, invoiceItem.rowVersion) &&
        Objects.equals(this.salesDetails, invoiceItem.salesDetails) &&
        Objects.equals(this.sold, invoiceItem.sold) &&
        Objects.equals(this.taxable, invoiceItem.taxable) &&
        Objects.equals(this.tracked, invoiceItem.tracked) &&
        Objects.equals(this.trackingCategory, invoiceItem.trackingCategory) &&
        Objects.equals(this.type, invoiceItem.type) &&
        Objects.equals(this.unitPrice, invoiceItem.unitPrice) &&
        Objects.equals(this.updatedAt, invoiceItem.updatedAt) &&
        Objects.equals(this.updatedBy, invoiceItem.updatedBy);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, assetAccount, code, createdAt, createdBy, customMappings, description, expenseAccount, id, incomeAccount, inventoryDate, name, purchaseDetails, purchased, quantity, rowVersion, salesDetails, sold, taxable, tracked, trackingCategory, type, unitPrice, updatedAt, updatedBy);
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
    sb.append("class InvoiceItem {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    assetAccount: ").append(toIndentedString(assetAccount)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    expenseAccount: ").append(toIndentedString(expenseAccount)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    incomeAccount: ").append(toIndentedString(incomeAccount)).append("\n");
    sb.append("    inventoryDate: ").append(toIndentedString(inventoryDate)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    purchaseDetails: ").append(toIndentedString(purchaseDetails)).append("\n");
    sb.append("    purchased: ").append(toIndentedString(purchased)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    rowVersion: ").append(toIndentedString(rowVersion)).append("\n");
    sb.append("    salesDetails: ").append(toIndentedString(salesDetails)).append("\n");
    sb.append("    sold: ").append(toIndentedString(sold)).append("\n");
    sb.append("    taxable: ").append(toIndentedString(taxable)).append("\n");
    sb.append("    tracked: ").append(toIndentedString(tracked)).append("\n");
    sb.append("    trackingCategory: ").append(toIndentedString(trackingCategory)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("active");
    openapiFields.add("asset_account");
    openapiFields.add("code");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("custom_mappings");
    openapiFields.add("description");
    openapiFields.add("expense_account");
    openapiFields.add("id");
    openapiFields.add("income_account");
    openapiFields.add("inventory_date");
    openapiFields.add("name");
    openapiFields.add("purchase_details");
    openapiFields.add("purchased");
    openapiFields.add("quantity");
    openapiFields.add("row_version");
    openapiFields.add("sales_details");
    openapiFields.add("sold");
    openapiFields.add("taxable");
    openapiFields.add("tracked");
    openapiFields.add("tracking_category");
    openapiFields.add("type");
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
   * @throws IOException if the JSON Element is invalid with respect to InvoiceItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InvoiceItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InvoiceItem is not found in the empty JSON string", InvoiceItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InvoiceItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InvoiceItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `asset_account`
      if (jsonObj.get("asset_account") != null && !jsonObj.get("asset_account").isJsonNull()) {
        LinkedLedgerAccount.validateJsonElement(jsonObj.get("asset_account"));
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) && !jsonObj.get("created_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `expense_account`
      if (jsonObj.get("expense_account") != null && !jsonObj.get("expense_account").isJsonNull()) {
        LinkedLedgerAccount.validateJsonElement(jsonObj.get("expense_account"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `income_account`
      if (jsonObj.get("income_account") != null && !jsonObj.get("income_account").isJsonNull()) {
        LinkedLedgerAccount.validateJsonElement(jsonObj.get("income_account"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `purchase_details`
      if (jsonObj.get("purchase_details") != null && !jsonObj.get("purchase_details").isJsonNull()) {
        InvoiceItemPurchaseDetails.validateJsonElement(jsonObj.get("purchase_details"));
      }
      if ((jsonObj.get("row_version") != null && !jsonObj.get("row_version").isJsonNull()) && !jsonObj.get("row_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `row_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("row_version").toString()));
      }
      // validate the optional field `sales_details`
      if (jsonObj.get("sales_details") != null && !jsonObj.get("sales_details").isJsonNull()) {
        InvoiceItemPurchaseDetails.validateJsonElement(jsonObj.get("sales_details"));
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
       if (!InvoiceItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InvoiceItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InvoiceItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InvoiceItem.class));

       return (TypeAdapter<T>) new TypeAdapter<InvoiceItem>() {
           @Override
           public void write(JsonWriter out, InvoiceItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InvoiceItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InvoiceItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InvoiceItem
   * @throws IOException if the JSON string is invalid with respect to InvoiceItem
   */
  public static InvoiceItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InvoiceItem.class);
  }

  /**
   * Convert an instance of InvoiceItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

