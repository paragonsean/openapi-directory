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
import org.openapitools.client.model.CategoriesInner;
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.ItemOptionsInner;
import org.openapitools.client.model.VariationsInner;
import org.openapitools.client.model.VariationsInner1;
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
 * Item
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:35.267625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Item {
  public static final String SERIALIZED_NAME_ABBREVIATION = "abbreviation";
  @SerializedName(SERIALIZED_NAME_ABBREVIATION)
  private String abbreviation;

  public static final String SERIALIZED_NAME_ABSENT_AT_LOCATION_IDS = "absent_at_location_ids";
  @SerializedName(SERIALIZED_NAME_ABSENT_AT_LOCATION_IDS)
  private List<String> absentAtLocationIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_AVAILABLE = "available";
  @SerializedName(SERIALIZED_NAME_AVAILABLE)
  private Boolean available;

  public static final String SERIALIZED_NAME_AVAILABLE_FOR_PICKUP = "available_for_pickup";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_FOR_PICKUP)
  private Boolean availableForPickup;

  public static final String SERIALIZED_NAME_AVAILABLE_ONLINE = "available_online";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_ONLINE)
  private Boolean availableOnline;

  public static final String SERIALIZED_NAME_CATEGORIES = "categories";
  @SerializedName(SERIALIZED_NAME_CATEGORIES)
  private List<CategoriesInner> categories = new ArrayList<>();

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_COST = "cost";
  @SerializedName(SERIALIZED_NAME_COST)
  private BigDecimal cost;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_HIDDEN = "hidden";
  @SerializedName(SERIALIZED_NAME_HIDDEN)
  private Boolean hidden;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IDEMPOTENCY_KEY = "idempotency_key";
  @SerializedName(SERIALIZED_NAME_IDEMPOTENCY_KEY)
  private String idempotencyKey;

  public static final String SERIALIZED_NAME_IS_REVENUE = "is_revenue";
  @SerializedName(SERIALIZED_NAME_IS_REVENUE)
  private Boolean isRevenue;

  public static final String SERIALIZED_NAME_MODIFIER_GROUPS = "modifier_groups";
  @SerializedName(SERIALIZED_NAME_MODIFIER_GROUPS)
  private List<VariationsInner> modifierGroups = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OPTIONS = "options";
  @SerializedName(SERIALIZED_NAME_OPTIONS)
  private List<ItemOptionsInner> options = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRESENT_AT_ALL_LOCATIONS = "present_at_all_locations";
  @SerializedName(SERIALIZED_NAME_PRESENT_AT_ALL_LOCATIONS)
  private Boolean presentAtAllLocations;

  public static final String SERIALIZED_NAME_PRICE_AMOUNT = "price_amount";
  @SerializedName(SERIALIZED_NAME_PRICE_AMOUNT)
  private BigDecimal priceAmount;

  public static final String SERIALIZED_NAME_PRICE_CURRENCY = "price_currency";
  @SerializedName(SERIALIZED_NAME_PRICE_CURRENCY)
  private Currency priceCurrency;

  /**
   * Gets or Sets pricingType
   */
  @JsonAdapter(PricingTypeEnum.Adapter.class)
  public enum PricingTypeEnum {
    FIXED("fixed"),
    
    VARIABLE("variable"),
    
    PER_UNIT("per_unit"),
    
    OTHER("other");

    private String value;

    PricingTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PricingTypeEnum fromValue(String value) {
      for (PricingTypeEnum b : PricingTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PricingTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PricingTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PricingTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PricingTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PricingTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PRICING_TYPE = "pricing_type";
  @SerializedName(SERIALIZED_NAME_PRICING_TYPE)
  private PricingTypeEnum pricingType;

  /**
   * Gets or Sets productType
   */
  @JsonAdapter(ProductTypeEnum.Adapter.class)
  public enum ProductTypeEnum {
    REGULAR("regular"),
    
    OTHER("other");

    private String value;

    ProductTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProductTypeEnum fromValue(String value) {
      for (ProductTypeEnum b : ProductTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProductTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProductTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProductTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProductTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProductTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PRODUCT_TYPE = "product_type";
  @SerializedName(SERIALIZED_NAME_PRODUCT_TYPE)
  private ProductTypeEnum productType;

  public static final String SERIALIZED_NAME_SKU = "sku";
  @SerializedName(SERIALIZED_NAME_SKU)
  private String sku;

  public static final String SERIALIZED_NAME_TAX_IDS = "tax_ids";
  @SerializedName(SERIALIZED_NAME_TAX_IDS)
  private List<String> taxIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_USE_DEFAULT_TAX_RATES = "use_default_tax_rates";
  @SerializedName(SERIALIZED_NAME_USE_DEFAULT_TAX_RATES)
  private Boolean useDefaultTaxRates;

  public static final String SERIALIZED_NAME_VARIATIONS = "variations";
  @SerializedName(SERIALIZED_NAME_VARIATIONS)
  private List<VariationsInner1> variations = new ArrayList<>();

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public Item() {
  }

  public Item(
     OffsetDateTime createdAt, 
     String createdBy, 
     OffsetDateTime updatedAt, 
     String updatedBy, 
     String version
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
    this.version = version;
  }

  public Item abbreviation(String abbreviation) {
    this.abbreviation = abbreviation;
    return this;
  }

  /**
   * Get abbreviation
   * @return abbreviation
   */
  @javax.annotation.Nullable
  public String getAbbreviation() {
    return abbreviation;
  }

  public void setAbbreviation(String abbreviation) {
    this.abbreviation = abbreviation;
  }


  public Item absentAtLocationIds(List<String> absentAtLocationIds) {
    this.absentAtLocationIds = absentAtLocationIds;
    return this;
  }

  public Item addAbsentAtLocationIdsItem(String absentAtLocationIdsItem) {
    if (this.absentAtLocationIds == null) {
      this.absentAtLocationIds = new ArrayList<>();
    }
    this.absentAtLocationIds.add(absentAtLocationIdsItem);
    return this;
  }

  /**
   * A list of locations where the object is not present, even if present_at_all_locations is true. This can include locations that are deactivated.
   * @return absentAtLocationIds
   */
  @javax.annotation.Nullable
  public List<String> getAbsentAtLocationIds() {
    return absentAtLocationIds;
  }

  public void setAbsentAtLocationIds(List<String> absentAtLocationIds) {
    this.absentAtLocationIds = absentAtLocationIds;
  }


  public Item available(Boolean available) {
    this.available = available;
    return this;
  }

  /**
   * Get available
   * @return available
   */
  @javax.annotation.Nullable
  public Boolean getAvailable() {
    return available;
  }

  public void setAvailable(Boolean available) {
    this.available = available;
  }


  public Item availableForPickup(Boolean availableForPickup) {
    this.availableForPickup = availableForPickup;
    return this;
  }

  /**
   * Get availableForPickup
   * @return availableForPickup
   */
  @javax.annotation.Nullable
  public Boolean getAvailableForPickup() {
    return availableForPickup;
  }

  public void setAvailableForPickup(Boolean availableForPickup) {
    this.availableForPickup = availableForPickup;
  }


  public Item availableOnline(Boolean availableOnline) {
    this.availableOnline = availableOnline;
    return this;
  }

  /**
   * Get availableOnline
   * @return availableOnline
   */
  @javax.annotation.Nullable
  public Boolean getAvailableOnline() {
    return availableOnline;
  }

  public void setAvailableOnline(Boolean availableOnline) {
    this.availableOnline = availableOnline;
  }


  public Item categories(List<CategoriesInner> categories) {
    this.categories = categories;
    return this;
  }

  public Item addCategoriesItem(CategoriesInner categoriesItem) {
    if (this.categories == null) {
      this.categories = new ArrayList<>();
    }
    this.categories.add(categoriesItem);
    return this;
  }

  /**
   * Get categories
   * @return categories
   */
  @javax.annotation.Nullable
  public List<CategoriesInner> getCategories() {
    return categories;
  }

  public void setCategories(List<CategoriesInner> categories) {
    this.categories = categories;
  }


  public Item code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Product code, e.g. UPC or EAN
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public Item cost(BigDecimal cost) {
    this.cost = cost;
    return this;
  }

  /**
   * Get cost
   * @return cost
   */
  @javax.annotation.Nullable
  public BigDecimal getCost() {
    return cost;
  }

  public void setCost(BigDecimal cost) {
    this.cost = cost;
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



  public Item customMappings(Object customMappings) {
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


  public Item deleted(Boolean deleted) {
    this.deleted = deleted;
    return this;
  }

  /**
   * Flag to indicate if the object is deleted.
   * @return deleted
   */
  @javax.annotation.Nullable
  public Boolean getDeleted() {
    return deleted;
  }

  public void setDeleted(Boolean deleted) {
    this.deleted = deleted;
  }


  public Item description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Item hidden(Boolean hidden) {
    this.hidden = hidden;
    return this;
  }

  /**
   * Get hidden
   * @return hidden
   */
  @javax.annotation.Nullable
  public Boolean getHidden() {
    return hidden;
  }

  public void setHidden(Boolean hidden) {
    this.hidden = hidden;
  }


  public Item id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Item idempotencyKey(String idempotencyKey) {
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


  public Item isRevenue(Boolean isRevenue) {
    this.isRevenue = isRevenue;
    return this;
  }

  /**
   * True if this item should be counted as revenue. For example, gift cards and donations would not be counted as revenue.
   * @return isRevenue
   */
  @javax.annotation.Nullable
  public Boolean getIsRevenue() {
    return isRevenue;
  }

  public void setIsRevenue(Boolean isRevenue) {
    this.isRevenue = isRevenue;
  }


  public Item modifierGroups(List<VariationsInner> modifierGroups) {
    this.modifierGroups = modifierGroups;
    return this;
  }

  public Item addModifierGroupsItem(VariationsInner modifierGroupsItem) {
    if (this.modifierGroups == null) {
      this.modifierGroups = new ArrayList<>();
    }
    this.modifierGroups.add(modifierGroupsItem);
    return this;
  }

  /**
   * Get modifierGroups
   * @return modifierGroups
   */
  @javax.annotation.Nullable
  public List<VariationsInner> getModifierGroups() {
    return modifierGroups;
  }

  public void setModifierGroups(List<VariationsInner> modifierGroups) {
    this.modifierGroups = modifierGroups;
  }


  public Item name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Item options(List<ItemOptionsInner> options) {
    this.options = options;
    return this;
  }

  public Item addOptionsItem(ItemOptionsInner optionsItem) {
    if (this.options == null) {
      this.options = new ArrayList<>();
    }
    this.options.add(optionsItem);
    return this;
  }

  /**
   * List of options pertaining to this item&#39;s attribute variation
   * @return options
   */
  @javax.annotation.Nullable
  public List<ItemOptionsInner> getOptions() {
    return options;
  }

  public void setOptions(List<ItemOptionsInner> options) {
    this.options = options;
  }


  public Item presentAtAllLocations(Boolean presentAtAllLocations) {
    this.presentAtAllLocations = presentAtAllLocations;
    return this;
  }

  /**
   * Get presentAtAllLocations
   * @return presentAtAllLocations
   */
  @javax.annotation.Nullable
  public Boolean getPresentAtAllLocations() {
    return presentAtAllLocations;
  }

  public void setPresentAtAllLocations(Boolean presentAtAllLocations) {
    this.presentAtAllLocations = presentAtAllLocations;
  }


  public Item priceAmount(BigDecimal priceAmount) {
    this.priceAmount = priceAmount;
    return this;
  }

  /**
   * Get priceAmount
   * @return priceAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getPriceAmount() {
    return priceAmount;
  }

  public void setPriceAmount(BigDecimal priceAmount) {
    this.priceAmount = priceAmount;
  }


  public Item priceCurrency(Currency priceCurrency) {
    this.priceCurrency = priceCurrency;
    return this;
  }

  /**
   * Get priceCurrency
   * @return priceCurrency
   */
  @javax.annotation.Nullable
  public Currency getPriceCurrency() {
    return priceCurrency;
  }

  public void setPriceCurrency(Currency priceCurrency) {
    this.priceCurrency = priceCurrency;
  }


  public Item pricingType(PricingTypeEnum pricingType) {
    this.pricingType = pricingType;
    return this;
  }

  /**
   * Get pricingType
   * @return pricingType
   */
  @javax.annotation.Nullable
  public PricingTypeEnum getPricingType() {
    return pricingType;
  }

  public void setPricingType(PricingTypeEnum pricingType) {
    this.pricingType = pricingType;
  }


  public Item productType(ProductTypeEnum productType) {
    this.productType = productType;
    return this;
  }

  /**
   * Get productType
   * @return productType
   */
  @javax.annotation.Nullable
  public ProductTypeEnum getProductType() {
    return productType;
  }

  public void setProductType(ProductTypeEnum productType) {
    this.productType = productType;
  }


  public Item sku(String sku) {
    this.sku = sku;
    return this;
  }

  /**
   * SKU of the item
   * @return sku
   */
  @javax.annotation.Nullable
  public String getSku() {
    return sku;
  }

  public void setSku(String sku) {
    this.sku = sku;
  }


  public Item taxIds(List<String> taxIds) {
    this.taxIds = taxIds;
    return this;
  }

  public Item addTaxIdsItem(String taxIdsItem) {
    if (this.taxIds == null) {
      this.taxIds = new ArrayList<>();
    }
    this.taxIds.add(taxIdsItem);
    return this;
  }

  /**
   * A list of Tax IDs for the product.
   * @return taxIds
   */
  @javax.annotation.Nullable
  public List<String> getTaxIds() {
    return taxIds;
  }

  public void setTaxIds(List<String> taxIds) {
    this.taxIds = taxIds;
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



  public Item useDefaultTaxRates(Boolean useDefaultTaxRates) {
    this.useDefaultTaxRates = useDefaultTaxRates;
    return this;
  }

  /**
   * Get useDefaultTaxRates
   * @return useDefaultTaxRates
   */
  @javax.annotation.Nullable
  public Boolean getUseDefaultTaxRates() {
    return useDefaultTaxRates;
  }

  public void setUseDefaultTaxRates(Boolean useDefaultTaxRates) {
    this.useDefaultTaxRates = useDefaultTaxRates;
  }


  public Item variations(List<VariationsInner1> variations) {
    this.variations = variations;
    return this;
  }

  public Item addVariationsItem(VariationsInner1 variationsItem) {
    if (this.variations == null) {
      this.variations = new ArrayList<>();
    }
    this.variations.add(variationsItem);
    return this;
  }

  /**
   * Get variations
   * @return variations
   */
  @javax.annotation.Nullable
  public List<VariationsInner1> getVariations() {
    return variations;
  }

  public void setVariations(List<VariationsInner1> variations) {
    this.variations = variations;
  }


  /**
   * The user who last updated the object.
   * @return version
   */
  @javax.annotation.Nullable
  public String getVersion() {
    return version;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Item item = (Item) o;
    return Objects.equals(this.abbreviation, item.abbreviation) &&
        Objects.equals(this.absentAtLocationIds, item.absentAtLocationIds) &&
        Objects.equals(this.available, item.available) &&
        Objects.equals(this.availableForPickup, item.availableForPickup) &&
        Objects.equals(this.availableOnline, item.availableOnline) &&
        Objects.equals(this.categories, item.categories) &&
        Objects.equals(this.code, item.code) &&
        Objects.equals(this.cost, item.cost) &&
        Objects.equals(this.createdAt, item.createdAt) &&
        Objects.equals(this.createdBy, item.createdBy) &&
        Objects.equals(this.customMappings, item.customMappings) &&
        Objects.equals(this.deleted, item.deleted) &&
        Objects.equals(this.description, item.description) &&
        Objects.equals(this.hidden, item.hidden) &&
        Objects.equals(this.id, item.id) &&
        Objects.equals(this.idempotencyKey, item.idempotencyKey) &&
        Objects.equals(this.isRevenue, item.isRevenue) &&
        Objects.equals(this.modifierGroups, item.modifierGroups) &&
        Objects.equals(this.name, item.name) &&
        Objects.equals(this.options, item.options) &&
        Objects.equals(this.presentAtAllLocations, item.presentAtAllLocations) &&
        Objects.equals(this.priceAmount, item.priceAmount) &&
        Objects.equals(this.priceCurrency, item.priceCurrency) &&
        Objects.equals(this.pricingType, item.pricingType) &&
        Objects.equals(this.productType, item.productType) &&
        Objects.equals(this.sku, item.sku) &&
        Objects.equals(this.taxIds, item.taxIds) &&
        Objects.equals(this.updatedAt, item.updatedAt) &&
        Objects.equals(this.updatedBy, item.updatedBy) &&
        Objects.equals(this.useDefaultTaxRates, item.useDefaultTaxRates) &&
        Objects.equals(this.variations, item.variations) &&
        Objects.equals(this.version, item.version);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(abbreviation, absentAtLocationIds, available, availableForPickup, availableOnline, categories, code, cost, createdAt, createdBy, customMappings, deleted, description, hidden, id, idempotencyKey, isRevenue, modifierGroups, name, options, presentAtAllLocations, priceAmount, priceCurrency, pricingType, productType, sku, taxIds, updatedAt, updatedBy, useDefaultTaxRates, variations, version);
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
    sb.append("class Item {\n");
    sb.append("    abbreviation: ").append(toIndentedString(abbreviation)).append("\n");
    sb.append("    absentAtLocationIds: ").append(toIndentedString(absentAtLocationIds)).append("\n");
    sb.append("    available: ").append(toIndentedString(available)).append("\n");
    sb.append("    availableForPickup: ").append(toIndentedString(availableForPickup)).append("\n");
    sb.append("    availableOnline: ").append(toIndentedString(availableOnline)).append("\n");
    sb.append("    categories: ").append(toIndentedString(categories)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    cost: ").append(toIndentedString(cost)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    hidden: ").append(toIndentedString(hidden)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    idempotencyKey: ").append(toIndentedString(idempotencyKey)).append("\n");
    sb.append("    isRevenue: ").append(toIndentedString(isRevenue)).append("\n");
    sb.append("    modifierGroups: ").append(toIndentedString(modifierGroups)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    options: ").append(toIndentedString(options)).append("\n");
    sb.append("    presentAtAllLocations: ").append(toIndentedString(presentAtAllLocations)).append("\n");
    sb.append("    priceAmount: ").append(toIndentedString(priceAmount)).append("\n");
    sb.append("    priceCurrency: ").append(toIndentedString(priceCurrency)).append("\n");
    sb.append("    pricingType: ").append(toIndentedString(pricingType)).append("\n");
    sb.append("    productType: ").append(toIndentedString(productType)).append("\n");
    sb.append("    sku: ").append(toIndentedString(sku)).append("\n");
    sb.append("    taxIds: ").append(toIndentedString(taxIds)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    useDefaultTaxRates: ").append(toIndentedString(useDefaultTaxRates)).append("\n");
    sb.append("    variations: ").append(toIndentedString(variations)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("abbreviation");
    openapiFields.add("absent_at_location_ids");
    openapiFields.add("available");
    openapiFields.add("available_for_pickup");
    openapiFields.add("available_online");
    openapiFields.add("categories");
    openapiFields.add("code");
    openapiFields.add("cost");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("custom_mappings");
    openapiFields.add("deleted");
    openapiFields.add("description");
    openapiFields.add("hidden");
    openapiFields.add("id");
    openapiFields.add("idempotency_key");
    openapiFields.add("is_revenue");
    openapiFields.add("modifier_groups");
    openapiFields.add("name");
    openapiFields.add("options");
    openapiFields.add("present_at_all_locations");
    openapiFields.add("price_amount");
    openapiFields.add("price_currency");
    openapiFields.add("pricing_type");
    openapiFields.add("product_type");
    openapiFields.add("sku");
    openapiFields.add("tax_ids");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("use_default_tax_rates");
    openapiFields.add("variations");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Item
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Item.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Item is not found in the empty JSON string", Item.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Item.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Item` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Item.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("abbreviation") != null && !jsonObj.get("abbreviation").isJsonNull()) && !jsonObj.get("abbreviation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `abbreviation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("abbreviation").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("absent_at_location_ids") != null && !jsonObj.get("absent_at_location_ids").isJsonNull() && !jsonObj.get("absent_at_location_ids").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `absent_at_location_ids` to be an array in the JSON string but got `%s`", jsonObj.get("absent_at_location_ids").toString()));
      }
      if (jsonObj.get("categories") != null && !jsonObj.get("categories").isJsonNull()) {
        JsonArray jsonArraycategories = jsonObj.getAsJsonArray("categories");
        if (jsonArraycategories != null) {
          // ensure the json data is an array
          if (!jsonObj.get("categories").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `categories` to be an array in the JSON string but got `%s`", jsonObj.get("categories").toString()));
          }

          // validate the optional field `categories` (array)
          for (int i = 0; i < jsonArraycategories.size(); i++) {
            CategoriesInner.validateJsonElement(jsonArraycategories.get(i));
          };
        }
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
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("idempotency_key") != null && !jsonObj.get("idempotency_key").isJsonNull()) && !jsonObj.get("idempotency_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `idempotency_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("idempotency_key").toString()));
      }
      if (jsonObj.get("modifier_groups") != null && !jsonObj.get("modifier_groups").isJsonNull()) {
        JsonArray jsonArraymodifierGroups = jsonObj.getAsJsonArray("modifier_groups");
        if (jsonArraymodifierGroups != null) {
          // ensure the json data is an array
          if (!jsonObj.get("modifier_groups").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `modifier_groups` to be an array in the JSON string but got `%s`", jsonObj.get("modifier_groups").toString()));
          }

          // validate the optional field `modifier_groups` (array)
          for (int i = 0; i < jsonArraymodifierGroups.size(); i++) {
            VariationsInner.validateJsonElement(jsonArraymodifierGroups.get(i));
          };
        }
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("options") != null && !jsonObj.get("options").isJsonNull()) {
        JsonArray jsonArrayoptions = jsonObj.getAsJsonArray("options");
        if (jsonArrayoptions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("options").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `options` to be an array in the JSON string but got `%s`", jsonObj.get("options").toString()));
          }

          // validate the optional field `options` (array)
          for (int i = 0; i < jsonArrayoptions.size(); i++) {
            ItemOptionsInner.validateJsonElement(jsonArrayoptions.get(i));
          };
        }
      }
      // validate the optional field `price_currency`
      if (jsonObj.get("price_currency") != null && !jsonObj.get("price_currency").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("price_currency"));
      }
      if ((jsonObj.get("pricing_type") != null && !jsonObj.get("pricing_type").isJsonNull()) && !jsonObj.get("pricing_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pricing_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pricing_type").toString()));
      }
      // validate the optional field `pricing_type`
      if (jsonObj.get("pricing_type") != null && !jsonObj.get("pricing_type").isJsonNull()) {
        PricingTypeEnum.validateJsonElement(jsonObj.get("pricing_type"));
      }
      if ((jsonObj.get("product_type") != null && !jsonObj.get("product_type").isJsonNull()) && !jsonObj.get("product_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `product_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("product_type").toString()));
      }
      // validate the optional field `product_type`
      if (jsonObj.get("product_type") != null && !jsonObj.get("product_type").isJsonNull()) {
        ProductTypeEnum.validateJsonElement(jsonObj.get("product_type"));
      }
      if ((jsonObj.get("sku") != null && !jsonObj.get("sku").isJsonNull()) && !jsonObj.get("sku").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sku` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sku").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tax_ids") != null && !jsonObj.get("tax_ids").isJsonNull() && !jsonObj.get("tax_ids").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_ids` to be an array in the JSON string but got `%s`", jsonObj.get("tax_ids").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
      if (jsonObj.get("variations") != null && !jsonObj.get("variations").isJsonNull()) {
        JsonArray jsonArrayvariations = jsonObj.getAsJsonArray("variations");
        if (jsonArrayvariations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("variations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `variations` to be an array in the JSON string but got `%s`", jsonObj.get("variations").toString()));
          }

          // validate the optional field `variations` (array)
          for (int i = 0; i < jsonArrayvariations.size(); i++) {
            VariationsInner1.validateJsonElement(jsonArrayvariations.get(i));
          };
        }
      }
      if ((jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Item.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Item' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Item> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Item.class));

       return (TypeAdapter<T>) new TypeAdapter<Item>() {
           @Override
           public void write(JsonWriter out, Item value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Item read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Item given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Item
   * @throws IOException if the JSON string is invalid with respect to Item
   */
  public static Item fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Item.class);
  }

  /**
   * Convert an instance of Item to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

