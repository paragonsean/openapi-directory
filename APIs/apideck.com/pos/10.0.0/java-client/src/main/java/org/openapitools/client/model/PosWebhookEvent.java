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
import java.util.Arrays;

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
 * PosWebhookEvent
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:35.267625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PosWebhookEvent {
  public static final String SERIALIZED_NAME_CONSUMER_ID = "consumer_id";
  @SerializedName(SERIALIZED_NAME_CONSUMER_ID)
  private String consumerId;

  public static final String SERIALIZED_NAME_ENTITY_ID = "entity_id";
  @SerializedName(SERIALIZED_NAME_ENTITY_ID)
  private String entityId;

  public static final String SERIALIZED_NAME_ENTITY_TYPE = "entity_type";
  @SerializedName(SERIALIZED_NAME_ENTITY_TYPE)
  private String entityType;

  public static final String SERIALIZED_NAME_ENTITY_URL = "entity_url";
  @SerializedName(SERIALIZED_NAME_ENTITY_URL)
  private String entityUrl;

  public static final String SERIALIZED_NAME_EVENT_ID = "event_id";
  @SerializedName(SERIALIZED_NAME_EVENT_ID)
  private String eventId;

  public static final String SERIALIZED_NAME_EXECUTION_ATTEMPT = "execution_attempt";
  @SerializedName(SERIALIZED_NAME_EXECUTION_ATTEMPT)
  private BigDecimal executionAttempt;

  public static final String SERIALIZED_NAME_OCCURRED_AT = "occurred_at";
  @SerializedName(SERIALIZED_NAME_OCCURRED_AT)
  private String occurredAt;

  public static final String SERIALIZED_NAME_SERVICE_ID = "service_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_ID)
  private String serviceId;

  /**
   * Name of Apideck Unified API
   */
  @JsonAdapter(UnifiedApiEnum.Adapter.class)
  public enum UnifiedApiEnum {
    ACCOUNTING("accounting"),
    
    ATS("ats"),
    
    CALENDAR("calendar"),
    
    CRM("crm"),
    
    CSP("csp"),
    
    CUSTOMER_SUPPORT("customer-support"),
    
    ECOMMERCE("ecommerce"),
    
    EMAIL("email"),
    
    EMAIL_MARKETING("email-marketing"),
    
    EXPENSE_MANAGEMENT("expense-management"),
    
    FILE_STORAGE("file-storage"),
    
    FORM("form"),
    
    HRIS("hris"),
    
    LEAD("lead"),
    
    PAYROLL("payroll"),
    
    POS("pos"),
    
    PROCUREMENT("procurement"),
    
    PROJECT_MANAGEMENT("project-management"),
    
    SCRIPT("script"),
    
    SMS("sms"),
    
    SPREADSHEET("spreadsheet"),
    
    TEAM_MESSAGING("team-messaging"),
    
    ISSUE_TRACKING("issue-tracking"),
    
    TIME_REGISTRATION("time-registration"),
    
    TRANSACTIONAL_EMAIL("transactional-email"),
    
    VAULT("vault"),
    
    DATA_WAREHOUSE("data-warehouse");

    private String value;

    UnifiedApiEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static UnifiedApiEnum fromValue(String value) {
      for (UnifiedApiEnum b : UnifiedApiEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<UnifiedApiEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final UnifiedApiEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public UnifiedApiEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return UnifiedApiEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      UnifiedApiEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_UNIFIED_API = "unified_api";
  @SerializedName(SERIALIZED_NAME_UNIFIED_API)
  private UnifiedApiEnum unifiedApi;

  /**
   * Gets or Sets eventType
   */
  @JsonAdapter(EventTypeEnum.Adapter.class)
  public enum EventTypeEnum {
    ORDER_CREATED("pos.order.created"),
    
    ORDER_UPDATED("pos.order.updated"),
    
    ORDER_DELETED("pos.order.deleted"),
    
    PAYMENT_CREATED("pos.payment.created"),
    
    PAYMENT_UPDATED("pos.payment.updated"),
    
    PAYMENT_DELETED("pos.payment.deleted"),
    
    MERCHANT_CREATED("pos.merchant.created"),
    
    MERCHANT_UPDATED("pos.merchant.updated"),
    
    MERCHANT_DELETED("pos.merchant.deleted"),
    
    LOCATION_CREATED("pos.location.created"),
    
    LOCATION_UPDATED("pos.location.updated"),
    
    LOCATION_DELETED("pos.location.deleted"),
    
    ITEM_CREATED("pos.item.created"),
    
    ITEM_UPDATED("pos.item.updated"),
    
    ITEM_DELETED("pos.item.deleted"),
    
    MODIFIER_CREATED("pos.modifier.created"),
    
    MODIFIER_UPDATED("pos.modifier.updated"),
    
    MODIFIER_DELETED("pos.modifier.deleted"),
    
    MODIFIER_GROUP_CREATED("pos.modifier-group.created"),
    
    MODIFIER_GROUP_UPDATED("pos.modifier-group.updated"),
    
    MODIFIER_GROUP_DELETED("pos.modifier-group.deleted");

    private String value;

    EventTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EventTypeEnum fromValue(String value) {
      for (EventTypeEnum b : EventTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EventTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EventTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EventTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EventTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EventTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EVENT_TYPE = "event_type";
  @SerializedName(SERIALIZED_NAME_EVENT_TYPE)
  private EventTypeEnum eventType;

  public PosWebhookEvent() {
  }

  public PosWebhookEvent consumerId(String consumerId) {
    this.consumerId = consumerId;
    return this;
  }

  /**
   * Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn&#39;t exist yet, Vault will upsert a consumer based on your ID.
   * @return consumerId
   */
  @javax.annotation.Nullable
  public String getConsumerId() {
    return consumerId;
  }

  public void setConsumerId(String consumerId) {
    this.consumerId = consumerId;
  }


  public PosWebhookEvent entityId(String entityId) {
    this.entityId = entityId;
    return this;
  }

  /**
   * The service provider&#39;s ID of the entity that triggered this event
   * @return entityId
   */
  @javax.annotation.Nullable
  public String getEntityId() {
    return entityId;
  }

  public void setEntityId(String entityId) {
    this.entityId = entityId;
  }


  public PosWebhookEvent entityType(String entityType) {
    this.entityType = entityType;
    return this;
  }

  /**
   * The type entity that triggered this event
   * @return entityType
   */
  @javax.annotation.Nullable
  public String getEntityType() {
    return entityType;
  }

  public void setEntityType(String entityType) {
    this.entityType = entityType;
  }


  public PosWebhookEvent entityUrl(String entityUrl) {
    this.entityUrl = entityUrl;
    return this;
  }

  /**
   * The url to retrieve entity detail.
   * @return entityUrl
   */
  @javax.annotation.Nullable
  public String getEntityUrl() {
    return entityUrl;
  }

  public void setEntityUrl(String entityUrl) {
    this.entityUrl = entityUrl;
  }


  public PosWebhookEvent eventId(String eventId) {
    this.eventId = eventId;
    return this;
  }

  /**
   * Unique reference to this request event
   * @return eventId
   */
  @javax.annotation.Nullable
  public String getEventId() {
    return eventId;
  }

  public void setEventId(String eventId) {
    this.eventId = eventId;
  }


  public PosWebhookEvent executionAttempt(BigDecimal executionAttempt) {
    this.executionAttempt = executionAttempt;
    return this;
  }

  /**
   * The current count this request event has been attempted
   * @return executionAttempt
   */
  @javax.annotation.Nullable
  public BigDecimal getExecutionAttempt() {
    return executionAttempt;
  }

  public void setExecutionAttempt(BigDecimal executionAttempt) {
    this.executionAttempt = executionAttempt;
  }


  public PosWebhookEvent occurredAt(String occurredAt) {
    this.occurredAt = occurredAt;
    return this;
  }

  /**
   * ISO Datetime for when the original event occurred
   * @return occurredAt
   */
  @javax.annotation.Nullable
  public String getOccurredAt() {
    return occurredAt;
  }

  public void setOccurredAt(String occurredAt) {
    this.occurredAt = occurredAt;
  }


  public PosWebhookEvent serviceId(String serviceId) {
    this.serviceId = serviceId;
    return this;
  }

  /**
   * Service provider identifier
   * @return serviceId
   */
  @javax.annotation.Nullable
  public String getServiceId() {
    return serviceId;
  }

  public void setServiceId(String serviceId) {
    this.serviceId = serviceId;
  }


  public PosWebhookEvent unifiedApi(UnifiedApiEnum unifiedApi) {
    this.unifiedApi = unifiedApi;
    return this;
  }

  /**
   * Name of Apideck Unified API
   * @return unifiedApi
   */
  @javax.annotation.Nullable
  public UnifiedApiEnum getUnifiedApi() {
    return unifiedApi;
  }

  public void setUnifiedApi(UnifiedApiEnum unifiedApi) {
    this.unifiedApi = unifiedApi;
  }


  public PosWebhookEvent eventType(EventTypeEnum eventType) {
    this.eventType = eventType;
    return this;
  }

  /**
   * Get eventType
   * @return eventType
   */
  @javax.annotation.Nullable
  public EventTypeEnum getEventType() {
    return eventType;
  }

  public void setEventType(EventTypeEnum eventType) {
    this.eventType = eventType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PosWebhookEvent posWebhookEvent = (PosWebhookEvent) o;
    return Objects.equals(this.consumerId, posWebhookEvent.consumerId) &&
        Objects.equals(this.entityId, posWebhookEvent.entityId) &&
        Objects.equals(this.entityType, posWebhookEvent.entityType) &&
        Objects.equals(this.entityUrl, posWebhookEvent.entityUrl) &&
        Objects.equals(this.eventId, posWebhookEvent.eventId) &&
        Objects.equals(this.executionAttempt, posWebhookEvent.executionAttempt) &&
        Objects.equals(this.occurredAt, posWebhookEvent.occurredAt) &&
        Objects.equals(this.serviceId, posWebhookEvent.serviceId) &&
        Objects.equals(this.unifiedApi, posWebhookEvent.unifiedApi) &&
        Objects.equals(this.eventType, posWebhookEvent.eventType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consumerId, entityId, entityType, entityUrl, eventId, executionAttempt, occurredAt, serviceId, unifiedApi, eventType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PosWebhookEvent {\n");
    sb.append("    consumerId: ").append(toIndentedString(consumerId)).append("\n");
    sb.append("    entityId: ").append(toIndentedString(entityId)).append("\n");
    sb.append("    entityType: ").append(toIndentedString(entityType)).append("\n");
    sb.append("    entityUrl: ").append(toIndentedString(entityUrl)).append("\n");
    sb.append("    eventId: ").append(toIndentedString(eventId)).append("\n");
    sb.append("    executionAttempt: ").append(toIndentedString(executionAttempt)).append("\n");
    sb.append("    occurredAt: ").append(toIndentedString(occurredAt)).append("\n");
    sb.append("    serviceId: ").append(toIndentedString(serviceId)).append("\n");
    sb.append("    unifiedApi: ").append(toIndentedString(unifiedApi)).append("\n");
    sb.append("    eventType: ").append(toIndentedString(eventType)).append("\n");
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
    openapiFields.add("consumer_id");
    openapiFields.add("entity_id");
    openapiFields.add("entity_type");
    openapiFields.add("entity_url");
    openapiFields.add("event_id");
    openapiFields.add("execution_attempt");
    openapiFields.add("occurred_at");
    openapiFields.add("service_id");
    openapiFields.add("unified_api");
    openapiFields.add("event_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PosWebhookEvent
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PosWebhookEvent.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PosWebhookEvent is not found in the empty JSON string", PosWebhookEvent.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PosWebhookEvent.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PosWebhookEvent` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("consumer_id") != null && !jsonObj.get("consumer_id").isJsonNull()) && !jsonObj.get("consumer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consumer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consumer_id").toString()));
      }
      if ((jsonObj.get("entity_id") != null && !jsonObj.get("entity_id").isJsonNull()) && !jsonObj.get("entity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entity_id").toString()));
      }
      if ((jsonObj.get("entity_type") != null && !jsonObj.get("entity_type").isJsonNull()) && !jsonObj.get("entity_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entity_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entity_type").toString()));
      }
      if ((jsonObj.get("entity_url") != null && !jsonObj.get("entity_url").isJsonNull()) && !jsonObj.get("entity_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entity_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entity_url").toString()));
      }
      if ((jsonObj.get("event_id") != null && !jsonObj.get("event_id").isJsonNull()) && !jsonObj.get("event_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `event_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("event_id").toString()));
      }
      if ((jsonObj.get("occurred_at") != null && !jsonObj.get("occurred_at").isJsonNull()) && !jsonObj.get("occurred_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `occurred_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("occurred_at").toString()));
      }
      if ((jsonObj.get("service_id") != null && !jsonObj.get("service_id").isJsonNull()) && !jsonObj.get("service_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_id").toString()));
      }
      if ((jsonObj.get("unified_api") != null && !jsonObj.get("unified_api").isJsonNull()) && !jsonObj.get("unified_api").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unified_api` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unified_api").toString()));
      }
      // validate the optional field `unified_api`
      if (jsonObj.get("unified_api") != null && !jsonObj.get("unified_api").isJsonNull()) {
        UnifiedApiEnum.validateJsonElement(jsonObj.get("unified_api"));
      }
      if ((jsonObj.get("event_type") != null && !jsonObj.get("event_type").isJsonNull()) && !jsonObj.get("event_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `event_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("event_type").toString()));
      }
      // validate the optional field `event_type`
      if (jsonObj.get("event_type") != null && !jsonObj.get("event_type").isJsonNull()) {
        EventTypeEnum.validateJsonElement(jsonObj.get("event_type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PosWebhookEvent.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PosWebhookEvent' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PosWebhookEvent> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PosWebhookEvent.class));

       return (TypeAdapter<T>) new TypeAdapter<PosWebhookEvent>() {
           @Override
           public void write(JsonWriter out, PosWebhookEvent value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PosWebhookEvent read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PosWebhookEvent given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PosWebhookEvent
   * @throws IOException if the JSON string is invalid with respect to PosWebhookEvent
   */
  public static PosWebhookEvent fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PosWebhookEvent.class);
  }

  /**
   * Convert an instance of PosWebhookEvent to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

