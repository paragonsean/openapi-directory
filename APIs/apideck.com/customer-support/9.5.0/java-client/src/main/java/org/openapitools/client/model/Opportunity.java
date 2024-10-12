/*
 * Customer Support
 * Welcome to the Customer Support API.  You can use this API to access all Customer Support API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  We also provide a [Mock API](https://developers.apideck.com/mock-api) that can be used for testing purposes: `https://mock-api.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 9.5.0
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
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.CustomField;
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
 * Opportunity
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:58:11.025450-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Opportunity {
  public static final String SERIALIZED_NAME_CLOSE_DATE = "close_date";
  @SerializedName(SERIALIZED_NAME_CLOSE_DATE)
  private LocalDate closeDate;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private String companyId;

  public static final String SERIALIZED_NAME_COMPANY_NAME = "company_name";
  @SerializedName(SERIALIZED_NAME_COMPANY_NAME)
  private String companyName;

  public static final String SERIALIZED_NAME_CONTACT_ID = "contact_id";
  @SerializedName(SERIALIZED_NAME_CONTACT_ID)
  private String contactId;

  public static final String SERIALIZED_NAME_CONTACT_IDS = "contact_ids";
  @SerializedName(SERIALIZED_NAME_CONTACT_IDS)
  private List<String> contactIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private Currency currency;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<CustomField> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_DATE_LAST_CONTACTED = "date_last_contacted";
  @SerializedName(SERIALIZED_NAME_DATE_LAST_CONTACTED)
  private OffsetDateTime dateLastContacted;

  public static final String SERIALIZED_NAME_DATE_LEAD_CREATED = "date_lead_created";
  @SerializedName(SERIALIZED_NAME_DATE_LEAD_CREATED)
  private OffsetDateTime dateLeadCreated;

  public static final String SERIALIZED_NAME_DATE_STAGE_CHANGED = "date_stage_changed";
  @SerializedName(SERIALIZED_NAME_DATE_STAGE_CHANGED)
  private OffsetDateTime dateStageChanged;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXPECTED_REVENUE = "expected_revenue";
  @SerializedName(SERIALIZED_NAME_EXPECTED_REVENUE)
  private BigDecimal expectedRevenue;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INTERACTION_COUNT = "interaction_count";
  @SerializedName(SERIALIZED_NAME_INTERACTION_COUNT)
  private BigDecimal interactionCount;

  public static final String SERIALIZED_NAME_LAST_ACTIVITY_AT = "last_activity_at";
  @SerializedName(SERIALIZED_NAME_LAST_ACTIVITY_AT)
  private String lastActivityAt;

  public static final String SERIALIZED_NAME_LEAD_ID = "lead_id";
  @SerializedName(SERIALIZED_NAME_LEAD_ID)
  private String leadId;

  public static final String SERIALIZED_NAME_LEAD_SOURCE = "lead_source";
  @SerializedName(SERIALIZED_NAME_LEAD_SOURCE)
  private String leadSource;

  public static final String SERIALIZED_NAME_LOSS_REASON = "loss_reason";
  @SerializedName(SERIALIZED_NAME_LOSS_REASON)
  private String lossReason;

  public static final String SERIALIZED_NAME_LOSS_REASON_ID = "loss_reason_id";
  @SerializedName(SERIALIZED_NAME_LOSS_REASON_ID)
  private String lossReasonId;

  public static final String SERIALIZED_NAME_MONETARY_AMOUNT = "monetary_amount";
  @SerializedName(SERIALIZED_NAME_MONETARY_AMOUNT)
  private BigDecimal monetaryAmount;

  public static final String SERIALIZED_NAME_OWNER_ID = "owner_id";
  @SerializedName(SERIALIZED_NAME_OWNER_ID)
  private String ownerId;

  public static final String SERIALIZED_NAME_PIPELINE_ID = "pipeline_id";
  @SerializedName(SERIALIZED_NAME_PIPELINE_ID)
  private String pipelineId;

  public static final String SERIALIZED_NAME_PIPELINE_STAGE_ID = "pipeline_stage_id";
  @SerializedName(SERIALIZED_NAME_PIPELINE_STAGE_ID)
  private String pipelineStageId;

  public static final String SERIALIZED_NAME_PRIMARY_CONTACT_ID = "primary_contact_id";
  @SerializedName(SERIALIZED_NAME_PRIMARY_CONTACT_ID)
  private String primaryContactId;

  public static final String SERIALIZED_NAME_PRIORITY = "priority";
  @SerializedName(SERIALIZED_NAME_PRIORITY)
  private String priority;

  public static final String SERIALIZED_NAME_SOURCE_ID = "source_id";
  @SerializedName(SERIALIZED_NAME_SOURCE_ID)
  private String sourceId;

  public static final String SERIALIZED_NAME_STAGE_LAST_CHANGED_AT = "stage_last_changed_at";
  @SerializedName(SERIALIZED_NAME_STAGE_LAST_CHANGED_AT)
  private OffsetDateTime stageLastChangedAt;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_STATUS_ID = "status_id";
  @SerializedName(SERIALIZED_NAME_STATUS_ID)
  private String statusId;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags = new ArrayList<>();

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_WIN_PROBABILITY = "win_probability";
  @SerializedName(SERIALIZED_NAME_WIN_PROBABILITY)
  private BigDecimal winProbability;

  public static final String SERIALIZED_NAME_WON_REASON = "won_reason";
  @SerializedName(SERIALIZED_NAME_WON_REASON)
  private String wonReason;

  public static final String SERIALIZED_NAME_WON_REASON_ID = "won_reason_id";
  @SerializedName(SERIALIZED_NAME_WON_REASON_ID)
  private String wonReasonId;

  public Opportunity() {
  }

  public Opportunity(
     OffsetDateTime createdAt, 
     String createdBy, 
     OffsetDateTime dateLastContacted, 
     OffsetDateTime dateLeadCreated, 
     OffsetDateTime dateStageChanged, 
     Boolean deleted, 
     BigDecimal expectedRevenue, 
     String id, 
     BigDecimal interactionCount, 
     String lastActivityAt, 
     OffsetDateTime updatedAt, 
     String updatedBy
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.dateLastContacted = dateLastContacted;
    this.dateLeadCreated = dateLeadCreated;
    this.dateStageChanged = dateStageChanged;
    this.deleted = deleted;
    this.expectedRevenue = expectedRevenue;
    this.id = id;
    this.interactionCount = interactionCount;
    this.lastActivityAt = lastActivityAt;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
  }

  public Opportunity closeDate(LocalDate closeDate) {
    this.closeDate = closeDate;
    return this;
  }

  /**
   * The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.
   * @return closeDate
   */
  @javax.annotation.Nullable
  public LocalDate getCloseDate() {
    return closeDate;
  }

  public void setCloseDate(LocalDate closeDate) {
    this.closeDate = closeDate;
  }


  public Opportunity companyId(String companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * The unique identifier of the company associated with the opportunity.
   * @return companyId
   */
  @javax.annotation.Nullable
  public String getCompanyId() {
    return companyId;
  }

  public void setCompanyId(String companyId) {
    this.companyId = companyId;
  }


  public Opportunity companyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  /**
   * The name of the company associated with the opportunity.
   * @return companyName
   */
  @javax.annotation.Nullable
  public String getCompanyName() {
    return companyName;
  }

  public void setCompanyName(String companyName) {
    this.companyName = companyName;
  }


  public Opportunity contactId(String contactId) {
    this.contactId = contactId;
    return this;
  }

  /**
   * The unique identifier of the contact associated with the opportunity.
   * @return contactId
   */
  @javax.annotation.Nullable
  public String getContactId() {
    return contactId;
  }

  public void setContactId(String contactId) {
    this.contactId = contactId;
  }


  public Opportunity contactIds(List<String> contactIds) {
    this.contactIds = contactIds;
    return this;
  }

  public Opportunity addContactIdsItem(String contactIdsItem) {
    if (this.contactIds == null) {
      this.contactIds = new ArrayList<>();
    }
    this.contactIds.add(contactIdsItem);
    return this;
  }

  /**
   * An array of unique identifiers of all contacts associated with the opportunity.
   * @return contactIds
   */
  @javax.annotation.Nullable
  public List<String> getContactIds() {
    return contactIds;
  }

  public void setContactIds(List<String> contactIds) {
    this.contactIds = contactIds;
  }


  /**
   * The date and time when the opportunity was created.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



  /**
   * The unique identifier of the user who created the opportunity.
   * @return createdBy
   */
  @javax.annotation.Nullable
  public String getCreatedBy() {
    return createdBy;
  }



  public Opportunity currency(Currency currency) {
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


  public Opportunity customFields(List<CustomField> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Opportunity addCustomFieldsItem(CustomField customFieldsItem) {
    if (this.customFields == null) {
      this.customFields = new ArrayList<>();
    }
    this.customFields.add(customFieldsItem);
    return this;
  }

  /**
   * Get customFields
   * @return customFields
   */
  @javax.annotation.Nullable
  public List<CustomField> getCustomFields() {
    return customFields;
  }

  public void setCustomFields(List<CustomField> customFields) {
    this.customFields = customFields;
  }


  /**
   * The date and time when the opportunity was last contacted.
   * @return dateLastContacted
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateLastContacted() {
    return dateLastContacted;
  }



  /**
   * The date and time when the lead associated with the opportunity was created.
   * @return dateLeadCreated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateLeadCreated() {
    return dateLeadCreated;
  }



  /**
   * The date and time when the stage of the opportunity was last changed.
   * @return dateStageChanged
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateStageChanged() {
    return dateStageChanged;
  }



  /**
   * Indicates whether the opportunity has been deleted.
   * @return deleted
   */
  @javax.annotation.Nullable
  public Boolean getDeleted() {
    return deleted;
  }



  public Opportunity description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A description of the opportunity.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  /**
   * The expected revenue from the opportunity
   * @return expectedRevenue
   */
  @javax.annotation.Nullable
  public BigDecimal getExpectedRevenue() {
    return expectedRevenue;
  }



  /**
   * A unique identifier for the opportunity.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * The number of interactions with the opportunity.
   * @return interactionCount
   */
  @javax.annotation.Nullable
  public BigDecimal getInteractionCount() {
    return interactionCount;
  }



  /**
   * The date and time of the last activity associated with the opportunity.
   * @return lastActivityAt
   */
  @javax.annotation.Nullable
  public String getLastActivityAt() {
    return lastActivityAt;
  }



  public Opportunity leadId(String leadId) {
    this.leadId = leadId;
    return this;
  }

  /**
   * The unique identifier of the lead associated with the opportunity.
   * @return leadId
   */
  @javax.annotation.Nullable
  public String getLeadId() {
    return leadId;
  }

  public void setLeadId(String leadId) {
    this.leadId = leadId;
  }


  public Opportunity leadSource(String leadSource) {
    this.leadSource = leadSource;
    return this;
  }

  /**
   * The source of the lead associated with the opportunity.
   * @return leadSource
   */
  @javax.annotation.Nullable
  public String getLeadSource() {
    return leadSource;
  }

  public void setLeadSource(String leadSource) {
    this.leadSource = leadSource;
  }


  public Opportunity lossReason(String lossReason) {
    this.lossReason = lossReason;
    return this;
  }

  /**
   * The reason why the opportunity was lost.
   * @return lossReason
   */
  @javax.annotation.Nullable
  public String getLossReason() {
    return lossReason;
  }

  public void setLossReason(String lossReason) {
    this.lossReason = lossReason;
  }


  public Opportunity lossReasonId(String lossReasonId) {
    this.lossReasonId = lossReasonId;
    return this;
  }

  /**
   * The unique identifier of the reason why the opportunity was lost.
   * @return lossReasonId
   */
  @javax.annotation.Nullable
  public String getLossReasonId() {
    return lossReasonId;
  }

  public void setLossReasonId(String lossReasonId) {
    this.lossReasonId = lossReasonId;
  }


  public Opportunity monetaryAmount(BigDecimal monetaryAmount) {
    this.monetaryAmount = monetaryAmount;
    return this;
  }

  /**
   * The monetary value associated with the opportunity
   * @return monetaryAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getMonetaryAmount() {
    return monetaryAmount;
  }

  public void setMonetaryAmount(BigDecimal monetaryAmount) {
    this.monetaryAmount = monetaryAmount;
  }


  public Opportunity ownerId(String ownerId) {
    this.ownerId = ownerId;
    return this;
  }

  /**
   * The unique identifier of the user who owns the opportunity.
   * @return ownerId
   */
  @javax.annotation.Nullable
  public String getOwnerId() {
    return ownerId;
  }

  public void setOwnerId(String ownerId) {
    this.ownerId = ownerId;
  }


  public Opportunity pipelineId(String pipelineId) {
    this.pipelineId = pipelineId;
    return this;
  }

  /**
   * The unique identifier of the pipeline associated with the opportunity
   * @return pipelineId
   */
  @javax.annotation.Nullable
  public String getPipelineId() {
    return pipelineId;
  }

  public void setPipelineId(String pipelineId) {
    this.pipelineId = pipelineId;
  }


  public Opportunity pipelineStageId(String pipelineStageId) {
    this.pipelineStageId = pipelineStageId;
    return this;
  }

  /**
   * The unique identifier of the stage in the pipeline associated with the opportunity.
   * @return pipelineStageId
   */
  @javax.annotation.Nullable
  public String getPipelineStageId() {
    return pipelineStageId;
  }

  public void setPipelineStageId(String pipelineStageId) {
    this.pipelineStageId = pipelineStageId;
  }


  public Opportunity primaryContactId(String primaryContactId) {
    this.primaryContactId = primaryContactId;
    return this;
  }

  /**
   * The unique identifier of the primary contact associated with the opportunity.
   * @return primaryContactId
   */
  @javax.annotation.Nullable
  public String getPrimaryContactId() {
    return primaryContactId;
  }

  public void setPrimaryContactId(String primaryContactId) {
    this.primaryContactId = primaryContactId;
  }


  public Opportunity priority(String priority) {
    this.priority = priority;
    return this;
  }

  /**
   * The priority level of the opportunity.
   * @return priority
   */
  @javax.annotation.Nullable
  public String getPriority() {
    return priority;
  }

  public void setPriority(String priority) {
    this.priority = priority;
  }


  public Opportunity sourceId(String sourceId) {
    this.sourceId = sourceId;
    return this;
  }

  /**
   * The unique identifier of the source of the opportunity.
   * @return sourceId
   */
  @javax.annotation.Nullable
  public String getSourceId() {
    return sourceId;
  }

  public void setSourceId(String sourceId) {
    this.sourceId = sourceId;
  }


  public Opportunity stageLastChangedAt(OffsetDateTime stageLastChangedAt) {
    this.stageLastChangedAt = stageLastChangedAt;
    return this;
  }

  /**
   * The date and time when the stage of the opportunity was last changed.
   * @return stageLastChangedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStageLastChangedAt() {
    return stageLastChangedAt;
  }

  public void setStageLastChangedAt(OffsetDateTime stageLastChangedAt) {
    this.stageLastChangedAt = stageLastChangedAt;
  }


  public Opportunity status(String status) {
    this.status = status;
    return this;
  }

  /**
   * The current status of the opportunity.
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public Opportunity statusId(String statusId) {
    this.statusId = statusId;
    return this;
  }

  /**
   * The unique identifier of the current status of the opportunity.
   * @return statusId
   */
  @javax.annotation.Nullable
  public String getStatusId() {
    return statusId;
  }

  public void setStatusId(String statusId) {
    this.statusId = statusId;
  }


  public Opportunity tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public Opportunity addTagsItem(String tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * Get tags
   * @return tags
   */
  @javax.annotation.Nullable
  public List<String> getTags() {
    return tags;
  }

  public void setTags(List<String> tags) {
    this.tags = tags;
  }


  public Opportunity title(String title) {
    this.title = title;
    return this;
  }

  /**
   * The title or name of the opportunity.
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Opportunity type(String type) {
    this.type = type;
    return this;
  }

  /**
   * The type of the opportunity
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  /**
   * The date and time when the opportunity was last updated.
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }



  /**
   * The unique identifier of the user who last updated the opportunity.
   * @return updatedBy
   */
  @javax.annotation.Nullable
  public String getUpdatedBy() {
    return updatedBy;
  }



  public Opportunity winProbability(BigDecimal winProbability) {
    this.winProbability = winProbability;
    return this;
  }

  /**
   * The probability of winning the opportunity, expressed as a percentage.
   * @return winProbability
   */
  @javax.annotation.Nullable
  public BigDecimal getWinProbability() {
    return winProbability;
  }

  public void setWinProbability(BigDecimal winProbability) {
    this.winProbability = winProbability;
  }


  public Opportunity wonReason(String wonReason) {
    this.wonReason = wonReason;
    return this;
  }

  /**
   * The reason why the opportunity was won.
   * @return wonReason
   */
  @javax.annotation.Nullable
  public String getWonReason() {
    return wonReason;
  }

  public void setWonReason(String wonReason) {
    this.wonReason = wonReason;
  }


  public Opportunity wonReasonId(String wonReasonId) {
    this.wonReasonId = wonReasonId;
    return this;
  }

  /**
   * The unique identifier of the reason why the opportunity was won.
   * @return wonReasonId
   */
  @javax.annotation.Nullable
  public String getWonReasonId() {
    return wonReasonId;
  }

  public void setWonReasonId(String wonReasonId) {
    this.wonReasonId = wonReasonId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Opportunity opportunity = (Opportunity) o;
    return Objects.equals(this.closeDate, opportunity.closeDate) &&
        Objects.equals(this.companyId, opportunity.companyId) &&
        Objects.equals(this.companyName, opportunity.companyName) &&
        Objects.equals(this.contactId, opportunity.contactId) &&
        Objects.equals(this.contactIds, opportunity.contactIds) &&
        Objects.equals(this.createdAt, opportunity.createdAt) &&
        Objects.equals(this.createdBy, opportunity.createdBy) &&
        Objects.equals(this.currency, opportunity.currency) &&
        Objects.equals(this.customFields, opportunity.customFields) &&
        Objects.equals(this.dateLastContacted, opportunity.dateLastContacted) &&
        Objects.equals(this.dateLeadCreated, opportunity.dateLeadCreated) &&
        Objects.equals(this.dateStageChanged, opportunity.dateStageChanged) &&
        Objects.equals(this.deleted, opportunity.deleted) &&
        Objects.equals(this.description, opportunity.description) &&
        Objects.equals(this.expectedRevenue, opportunity.expectedRevenue) &&
        Objects.equals(this.id, opportunity.id) &&
        Objects.equals(this.interactionCount, opportunity.interactionCount) &&
        Objects.equals(this.lastActivityAt, opportunity.lastActivityAt) &&
        Objects.equals(this.leadId, opportunity.leadId) &&
        Objects.equals(this.leadSource, opportunity.leadSource) &&
        Objects.equals(this.lossReason, opportunity.lossReason) &&
        Objects.equals(this.lossReasonId, opportunity.lossReasonId) &&
        Objects.equals(this.monetaryAmount, opportunity.monetaryAmount) &&
        Objects.equals(this.ownerId, opportunity.ownerId) &&
        Objects.equals(this.pipelineId, opportunity.pipelineId) &&
        Objects.equals(this.pipelineStageId, opportunity.pipelineStageId) &&
        Objects.equals(this.primaryContactId, opportunity.primaryContactId) &&
        Objects.equals(this.priority, opportunity.priority) &&
        Objects.equals(this.sourceId, opportunity.sourceId) &&
        Objects.equals(this.stageLastChangedAt, opportunity.stageLastChangedAt) &&
        Objects.equals(this.status, opportunity.status) &&
        Objects.equals(this.statusId, opportunity.statusId) &&
        Objects.equals(this.tags, opportunity.tags) &&
        Objects.equals(this.title, opportunity.title) &&
        Objects.equals(this.type, opportunity.type) &&
        Objects.equals(this.updatedAt, opportunity.updatedAt) &&
        Objects.equals(this.updatedBy, opportunity.updatedBy) &&
        Objects.equals(this.winProbability, opportunity.winProbability) &&
        Objects.equals(this.wonReason, opportunity.wonReason) &&
        Objects.equals(this.wonReasonId, opportunity.wonReasonId);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(closeDate, companyId, companyName, contactId, contactIds, createdAt, createdBy, currency, customFields, dateLastContacted, dateLeadCreated, dateStageChanged, deleted, description, expectedRevenue, id, interactionCount, lastActivityAt, leadId, leadSource, lossReason, lossReasonId, monetaryAmount, ownerId, pipelineId, pipelineStageId, primaryContactId, priority, sourceId, stageLastChangedAt, status, statusId, tags, title, type, updatedAt, updatedBy, winProbability, wonReason, wonReasonId);
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
    sb.append("class Opportunity {\n");
    sb.append("    closeDate: ").append(toIndentedString(closeDate)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    companyName: ").append(toIndentedString(companyName)).append("\n");
    sb.append("    contactId: ").append(toIndentedString(contactId)).append("\n");
    sb.append("    contactIds: ").append(toIndentedString(contactIds)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    dateLastContacted: ").append(toIndentedString(dateLastContacted)).append("\n");
    sb.append("    dateLeadCreated: ").append(toIndentedString(dateLeadCreated)).append("\n");
    sb.append("    dateStageChanged: ").append(toIndentedString(dateStageChanged)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    expectedRevenue: ").append(toIndentedString(expectedRevenue)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    interactionCount: ").append(toIndentedString(interactionCount)).append("\n");
    sb.append("    lastActivityAt: ").append(toIndentedString(lastActivityAt)).append("\n");
    sb.append("    leadId: ").append(toIndentedString(leadId)).append("\n");
    sb.append("    leadSource: ").append(toIndentedString(leadSource)).append("\n");
    sb.append("    lossReason: ").append(toIndentedString(lossReason)).append("\n");
    sb.append("    lossReasonId: ").append(toIndentedString(lossReasonId)).append("\n");
    sb.append("    monetaryAmount: ").append(toIndentedString(monetaryAmount)).append("\n");
    sb.append("    ownerId: ").append(toIndentedString(ownerId)).append("\n");
    sb.append("    pipelineId: ").append(toIndentedString(pipelineId)).append("\n");
    sb.append("    pipelineStageId: ").append(toIndentedString(pipelineStageId)).append("\n");
    sb.append("    primaryContactId: ").append(toIndentedString(primaryContactId)).append("\n");
    sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
    sb.append("    sourceId: ").append(toIndentedString(sourceId)).append("\n");
    sb.append("    stageLastChangedAt: ").append(toIndentedString(stageLastChangedAt)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statusId: ").append(toIndentedString(statusId)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    winProbability: ").append(toIndentedString(winProbability)).append("\n");
    sb.append("    wonReason: ").append(toIndentedString(wonReason)).append("\n");
    sb.append("    wonReasonId: ").append(toIndentedString(wonReasonId)).append("\n");
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
    openapiFields.add("close_date");
    openapiFields.add("company_id");
    openapiFields.add("company_name");
    openapiFields.add("contact_id");
    openapiFields.add("contact_ids");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("currency");
    openapiFields.add("custom_fields");
    openapiFields.add("date_last_contacted");
    openapiFields.add("date_lead_created");
    openapiFields.add("date_stage_changed");
    openapiFields.add("deleted");
    openapiFields.add("description");
    openapiFields.add("expected_revenue");
    openapiFields.add("id");
    openapiFields.add("interaction_count");
    openapiFields.add("last_activity_at");
    openapiFields.add("lead_id");
    openapiFields.add("lead_source");
    openapiFields.add("loss_reason");
    openapiFields.add("loss_reason_id");
    openapiFields.add("monetary_amount");
    openapiFields.add("owner_id");
    openapiFields.add("pipeline_id");
    openapiFields.add("pipeline_stage_id");
    openapiFields.add("primary_contact_id");
    openapiFields.add("priority");
    openapiFields.add("source_id");
    openapiFields.add("stage_last_changed_at");
    openapiFields.add("status");
    openapiFields.add("status_id");
    openapiFields.add("tags");
    openapiFields.add("title");
    openapiFields.add("type");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("win_probability");
    openapiFields.add("won_reason");
    openapiFields.add("won_reason_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("primary_contact_id");
    openapiRequiredFields.add("title");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Opportunity
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Opportunity.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Opportunity is not found in the empty JSON string", Opportunity.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Opportunity.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Opportunity` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Opportunity.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("company_name") != null && !jsonObj.get("company_name").isJsonNull()) && !jsonObj.get("company_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_name").toString()));
      }
      if ((jsonObj.get("contact_id") != null && !jsonObj.get("contact_id").isJsonNull()) && !jsonObj.get("contact_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("contact_ids") != null && !jsonObj.get("contact_ids").isJsonNull() && !jsonObj.get("contact_ids").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_ids` to be an array in the JSON string but got `%s`", jsonObj.get("contact_ids").toString()));
      }
      if ((jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) && !jsonObj.get("created_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by").toString()));
      }
      // validate the optional field `currency`
      if (jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("currency"));
      }
      if (jsonObj.get("custom_fields") != null && !jsonObj.get("custom_fields").isJsonNull()) {
        JsonArray jsonArraycustomFields = jsonObj.getAsJsonArray("custom_fields");
        if (jsonArraycustomFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_fields` to be an array in the JSON string but got `%s`", jsonObj.get("custom_fields").toString()));
          }

          // validate the optional field `custom_fields` (array)
          for (int i = 0; i < jsonArraycustomFields.size(); i++) {
            CustomField.validateJsonElement(jsonArraycustomFields.get(i));
          };
        }
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("last_activity_at") != null && !jsonObj.get("last_activity_at").isJsonNull()) && !jsonObj.get("last_activity_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_activity_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_activity_at").toString()));
      }
      if ((jsonObj.get("lead_id") != null && !jsonObj.get("lead_id").isJsonNull()) && !jsonObj.get("lead_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lead_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lead_id").toString()));
      }
      if ((jsonObj.get("lead_source") != null && !jsonObj.get("lead_source").isJsonNull()) && !jsonObj.get("lead_source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lead_source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lead_source").toString()));
      }
      if ((jsonObj.get("loss_reason") != null && !jsonObj.get("loss_reason").isJsonNull()) && !jsonObj.get("loss_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `loss_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("loss_reason").toString()));
      }
      if ((jsonObj.get("loss_reason_id") != null && !jsonObj.get("loss_reason_id").isJsonNull()) && !jsonObj.get("loss_reason_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `loss_reason_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("loss_reason_id").toString()));
      }
      if ((jsonObj.get("owner_id") != null && !jsonObj.get("owner_id").isJsonNull()) && !jsonObj.get("owner_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner_id").toString()));
      }
      if ((jsonObj.get("pipeline_id") != null && !jsonObj.get("pipeline_id").isJsonNull()) && !jsonObj.get("pipeline_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pipeline_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pipeline_id").toString()));
      }
      if ((jsonObj.get("pipeline_stage_id") != null && !jsonObj.get("pipeline_stage_id").isJsonNull()) && !jsonObj.get("pipeline_stage_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pipeline_stage_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pipeline_stage_id").toString()));
      }
      if ((jsonObj.get("primary_contact_id") != null && !jsonObj.get("primary_contact_id").isJsonNull()) && !jsonObj.get("primary_contact_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primary_contact_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primary_contact_id").toString()));
      }
      if ((jsonObj.get("priority") != null && !jsonObj.get("priority").isJsonNull()) && !jsonObj.get("priority").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `priority` to be a primitive type in the JSON string but got `%s`", jsonObj.get("priority").toString()));
      }
      if ((jsonObj.get("source_id") != null && !jsonObj.get("source_id").isJsonNull()) && !jsonObj.get("source_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_id").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("status_id") != null && !jsonObj.get("status_id").isJsonNull()) && !jsonObj.get("status_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
      if ((jsonObj.get("won_reason") != null && !jsonObj.get("won_reason").isJsonNull()) && !jsonObj.get("won_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `won_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("won_reason").toString()));
      }
      if ((jsonObj.get("won_reason_id") != null && !jsonObj.get("won_reason_id").isJsonNull()) && !jsonObj.get("won_reason_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `won_reason_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("won_reason_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Opportunity.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Opportunity' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Opportunity> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Opportunity.class));

       return (TypeAdapter<T>) new TypeAdapter<Opportunity>() {
           @Override
           public void write(JsonWriter out, Opportunity value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Opportunity read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Opportunity given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Opportunity
   * @throws IOException if the JSON string is invalid with respect to Opportunity
   */
  public static Opportunity fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Opportunity.class);
  }

  /**
   * Convert an instance of Opportunity to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

