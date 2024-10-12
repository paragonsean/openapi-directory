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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails;
import org.openapitools.client.model.OrderFulfillmentsInnerPickupDetailsRecipient;
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
 * OrderFulfillmentsInnerPickupDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:35.267625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderFulfillmentsInnerPickupDetails {
  public static final String SERIALIZED_NAME_ACCEPTED_AT = "accepted_at";
  @SerializedName(SERIALIZED_NAME_ACCEPTED_AT)
  private OffsetDateTime acceptedAt;

  public static final String SERIALIZED_NAME_AUTO_COMPLETE_DURATION = "auto_complete_duration";
  @SerializedName(SERIALIZED_NAME_AUTO_COMPLETE_DURATION)
  private String autoCompleteDuration;

  public static final String SERIALIZED_NAME_CANCEL_REASON = "cancel_reason";
  @SerializedName(SERIALIZED_NAME_CANCEL_REASON)
  private String cancelReason;

  public static final String SERIALIZED_NAME_CANCELED_AT = "canceled_at";
  @SerializedName(SERIALIZED_NAME_CANCELED_AT)
  private OffsetDateTime canceledAt;

  public static final String SERIALIZED_NAME_CURBSIDE_PICKUP_DETAILS = "curbside_pickup_details";
  @SerializedName(SERIALIZED_NAME_CURBSIDE_PICKUP_DETAILS)
  private OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails curbsidePickupDetails;

  public static final String SERIALIZED_NAME_EXPIRED_AT = "expired_at";
  @SerializedName(SERIALIZED_NAME_EXPIRED_AT)
  private OffsetDateTime expiredAt;

  public static final String SERIALIZED_NAME_EXPIRES_AT = "expires_at";
  @SerializedName(SERIALIZED_NAME_EXPIRES_AT)
  private OffsetDateTime expiresAt;

  public static final String SERIALIZED_NAME_IS_CURBSIDE_PICKUP = "is_curbside_pickup";
  @SerializedName(SERIALIZED_NAME_IS_CURBSIDE_PICKUP)
  private Boolean isCurbsidePickup;

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_PICKED_UP_AT = "picked_up_at";
  @SerializedName(SERIALIZED_NAME_PICKED_UP_AT)
  private OffsetDateTime pickedUpAt;

  public static final String SERIALIZED_NAME_PICKUP_AT = "pickup_at";
  @SerializedName(SERIALIZED_NAME_PICKUP_AT)
  private OffsetDateTime pickupAt;

  public static final String SERIALIZED_NAME_PICKUP_WINDOW_DURATION = "pickup_window_duration";
  @SerializedName(SERIALIZED_NAME_PICKUP_WINDOW_DURATION)
  private String pickupWindowDuration;

  public static final String SERIALIZED_NAME_PLACED_AT = "placed_at";
  @SerializedName(SERIALIZED_NAME_PLACED_AT)
  private OffsetDateTime placedAt;

  public static final String SERIALIZED_NAME_PREP_TIME_DURATION = "prep_time_duration";
  @SerializedName(SERIALIZED_NAME_PREP_TIME_DURATION)
  private String prepTimeDuration;

  public static final String SERIALIZED_NAME_READY_AT = "ready_at";
  @SerializedName(SERIALIZED_NAME_READY_AT)
  private OffsetDateTime readyAt;

  public static final String SERIALIZED_NAME_RECIPIENT = "recipient";
  @SerializedName(SERIALIZED_NAME_RECIPIENT)
  private OrderFulfillmentsInnerPickupDetailsRecipient recipient;

  public static final String SERIALIZED_NAME_REJECTED_AT = "rejected_at";
  @SerializedName(SERIALIZED_NAME_REJECTED_AT)
  private OffsetDateTime rejectedAt;

  /**
   * The schedule type of the pickup fulfillment.
   */
  @JsonAdapter(ScheduleTypeEnum.Adapter.class)
  public enum ScheduleTypeEnum {
    SCHEDULED("scheduled");

    private String value;

    ScheduleTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ScheduleTypeEnum fromValue(String value) {
      for (ScheduleTypeEnum b : ScheduleTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ScheduleTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ScheduleTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ScheduleTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ScheduleTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ScheduleTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SCHEDULE_TYPE = "schedule_type";
  @SerializedName(SERIALIZED_NAME_SCHEDULE_TYPE)
  private ScheduleTypeEnum scheduleType;

  public OrderFulfillmentsInnerPickupDetails() {
  }

  public OrderFulfillmentsInnerPickupDetails(
     OffsetDateTime acceptedAt
  ) {
    this();
    this.acceptedAt = acceptedAt;
  }

  /**
   * Get acceptedAt
   * @return acceptedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getAcceptedAt() {
    return acceptedAt;
  }



  public OrderFulfillmentsInnerPickupDetails autoCompleteDuration(String autoCompleteDuration) {
    this.autoCompleteDuration = autoCompleteDuration;
    return this;
  }

  /**
   * The duration of time after which an open and accepted pickup fulfillment is automatically moved to the COMPLETED state. The duration must be in RFC 3339 format (for example, &#39;P1W3D&#39;).
   * @return autoCompleteDuration
   */
  @javax.annotation.Nullable
  public String getAutoCompleteDuration() {
    return autoCompleteDuration;
  }

  public void setAutoCompleteDuration(String autoCompleteDuration) {
    this.autoCompleteDuration = autoCompleteDuration;
  }


  public OrderFulfillmentsInnerPickupDetails cancelReason(String cancelReason) {
    this.cancelReason = cancelReason;
    return this;
  }

  /**
   * A description of why the pickup was canceled.
   * @return cancelReason
   */
  @javax.annotation.Nullable
  public String getCancelReason() {
    return cancelReason;
  }

  public void setCancelReason(String cancelReason) {
    this.cancelReason = cancelReason;
  }


  public OrderFulfillmentsInnerPickupDetails canceledAt(OffsetDateTime canceledAt) {
    this.canceledAt = canceledAt;
    return this;
  }

  /**
   * Indicating when the fulfillment was canceled. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;).
   * @return canceledAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCanceledAt() {
    return canceledAt;
  }

  public void setCanceledAt(OffsetDateTime canceledAt) {
    this.canceledAt = canceledAt;
  }


  public OrderFulfillmentsInnerPickupDetails curbsidePickupDetails(OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails curbsidePickupDetails) {
    this.curbsidePickupDetails = curbsidePickupDetails;
    return this;
  }

  /**
   * Get curbsidePickupDetails
   * @return curbsidePickupDetails
   */
  @javax.annotation.Nullable
  public OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails getCurbsidePickupDetails() {
    return curbsidePickupDetails;
  }

  public void setCurbsidePickupDetails(OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails curbsidePickupDetails) {
    this.curbsidePickupDetails = curbsidePickupDetails;
  }


  public OrderFulfillmentsInnerPickupDetails expiredAt(OffsetDateTime expiredAt) {
    this.expiredAt = expiredAt;
    return this;
  }

  /**
   * Indicating when the fulfillment expired. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;).
   * @return expiredAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiredAt() {
    return expiredAt;
  }

  public void setExpiredAt(OffsetDateTime expiredAt) {
    this.expiredAt = expiredAt;
  }


  public OrderFulfillmentsInnerPickupDetails expiresAt(OffsetDateTime expiresAt) {
    this.expiresAt = expiresAt;
    return this;
  }

  /**
   * Indicating when this fulfillment expires if it is not accepted. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). The expiration time can only be set up to 7 days in the future. If &#x60;expires_at&#x60; is not set, this pickup fulfillment is automatically accepted when  placed.
   * @return expiresAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiresAt() {
    return expiresAt;
  }

  public void setExpiresAt(OffsetDateTime expiresAt) {
    this.expiresAt = expiresAt;
  }


  public OrderFulfillmentsInnerPickupDetails isCurbsidePickup(Boolean isCurbsidePickup) {
    this.isCurbsidePickup = isCurbsidePickup;
    return this;
  }

  /**
   * If set to &#x60;true&#x60;, indicates that this pickup order is for curbside pickup, not in-store pickup.
   * @return isCurbsidePickup
   */
  @javax.annotation.Nullable
  public Boolean getIsCurbsidePickup() {
    return isCurbsidePickup;
  }

  public void setIsCurbsidePickup(Boolean isCurbsidePickup) {
    this.isCurbsidePickup = isCurbsidePickup;
  }


  public OrderFulfillmentsInnerPickupDetails note(String note) {
    this.note = note;
    return this;
  }

  /**
   * A note meant to provide additional instructions about the pickup fulfillment displayed in the Square Point of Sale application and set by the API.
   * @return note
   */
  @javax.annotation.Nullable
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }


  public OrderFulfillmentsInnerPickupDetails pickedUpAt(OffsetDateTime pickedUpAt) {
    this.pickedUpAt = pickedUpAt;
    return this;
  }

  /**
   * Indicating when the fulfillment was picked up by the recipient. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;).
   * @return pickedUpAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPickedUpAt() {
    return pickedUpAt;
  }

  public void setPickedUpAt(OffsetDateTime pickedUpAt) {
    this.pickedUpAt = pickedUpAt;
  }


  public OrderFulfillmentsInnerPickupDetails pickupAt(OffsetDateTime pickupAt) {
    this.pickupAt = pickupAt;
    return this;
  }

  /**
   * The timestamp that represents the start of the pickup window. Must be in RFC 3339 timestamp format, e.g.,  \&quot;2016-09-04T23:59:33.123Z\&quot;.  For fulfillments with the schedule type &#x60;ASAP&#x60;, this is automatically set to the current time plus the expected duration to prepare the fulfillment.
   * @return pickupAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPickupAt() {
    return pickupAt;
  }

  public void setPickupAt(OffsetDateTime pickupAt) {
    this.pickupAt = pickupAt;
  }


  public OrderFulfillmentsInnerPickupDetails pickupWindowDuration(String pickupWindowDuration) {
    this.pickupWindowDuration = pickupWindowDuration;
    return this;
  }

  /**
   * The window of time in which the order should be picked up after the &#x60;pickup_at&#x60; timestamp. Must be in RFC 3339 duration format, e.g., \&quot;P1W3D\&quot;. Can be used as an informational guideline for merchants.
   * @return pickupWindowDuration
   */
  @javax.annotation.Nullable
  public String getPickupWindowDuration() {
    return pickupWindowDuration;
  }

  public void setPickupWindowDuration(String pickupWindowDuration) {
    this.pickupWindowDuration = pickupWindowDuration;
  }


  public OrderFulfillmentsInnerPickupDetails placedAt(OffsetDateTime placedAt) {
    this.placedAt = placedAt;
    return this;
  }

  /**
   * Indicating when the fulfillment was placed. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;).
   * @return placedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPlacedAt() {
    return placedAt;
  }

  public void setPlacedAt(OffsetDateTime placedAt) {
    this.placedAt = placedAt;
  }


  public OrderFulfillmentsInnerPickupDetails prepTimeDuration(String prepTimeDuration) {
    this.prepTimeDuration = prepTimeDuration;
    return this;
  }

  /**
   * The duration of time it takes to prepare this fulfillment. The duration must be in RFC 3339 format (for example, \&quot;P1W3D\&quot;).
   * @return prepTimeDuration
   */
  @javax.annotation.Nullable
  public String getPrepTimeDuration() {
    return prepTimeDuration;
  }

  public void setPrepTimeDuration(String prepTimeDuration) {
    this.prepTimeDuration = prepTimeDuration;
  }


  public OrderFulfillmentsInnerPickupDetails readyAt(OffsetDateTime readyAt) {
    this.readyAt = readyAt;
    return this;
  }

  /**
   * Indicating when the fulfillment is marked as ready for pickup. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;).
   * @return readyAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getReadyAt() {
    return readyAt;
  }

  public void setReadyAt(OffsetDateTime readyAt) {
    this.readyAt = readyAt;
  }


  public OrderFulfillmentsInnerPickupDetails recipient(OrderFulfillmentsInnerPickupDetailsRecipient recipient) {
    this.recipient = recipient;
    return this;
  }

  /**
   * Get recipient
   * @return recipient
   */
  @javax.annotation.Nullable
  public OrderFulfillmentsInnerPickupDetailsRecipient getRecipient() {
    return recipient;
  }

  public void setRecipient(OrderFulfillmentsInnerPickupDetailsRecipient recipient) {
    this.recipient = recipient;
  }


  public OrderFulfillmentsInnerPickupDetails rejectedAt(OffsetDateTime rejectedAt) {
    this.rejectedAt = rejectedAt;
    return this;
  }

  /**
   * Indicating when the fulfillment was rejected. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;).
   * @return rejectedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getRejectedAt() {
    return rejectedAt;
  }

  public void setRejectedAt(OffsetDateTime rejectedAt) {
    this.rejectedAt = rejectedAt;
  }


  public OrderFulfillmentsInnerPickupDetails scheduleType(ScheduleTypeEnum scheduleType) {
    this.scheduleType = scheduleType;
    return this;
  }

  /**
   * The schedule type of the pickup fulfillment.
   * @return scheduleType
   */
  @javax.annotation.Nullable
  public ScheduleTypeEnum getScheduleType() {
    return scheduleType;
  }

  public void setScheduleType(ScheduleTypeEnum scheduleType) {
    this.scheduleType = scheduleType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderFulfillmentsInnerPickupDetails orderFulfillmentsInnerPickupDetails = (OrderFulfillmentsInnerPickupDetails) o;
    return Objects.equals(this.acceptedAt, orderFulfillmentsInnerPickupDetails.acceptedAt) &&
        Objects.equals(this.autoCompleteDuration, orderFulfillmentsInnerPickupDetails.autoCompleteDuration) &&
        Objects.equals(this.cancelReason, orderFulfillmentsInnerPickupDetails.cancelReason) &&
        Objects.equals(this.canceledAt, orderFulfillmentsInnerPickupDetails.canceledAt) &&
        Objects.equals(this.curbsidePickupDetails, orderFulfillmentsInnerPickupDetails.curbsidePickupDetails) &&
        Objects.equals(this.expiredAt, orderFulfillmentsInnerPickupDetails.expiredAt) &&
        Objects.equals(this.expiresAt, orderFulfillmentsInnerPickupDetails.expiresAt) &&
        Objects.equals(this.isCurbsidePickup, orderFulfillmentsInnerPickupDetails.isCurbsidePickup) &&
        Objects.equals(this.note, orderFulfillmentsInnerPickupDetails.note) &&
        Objects.equals(this.pickedUpAt, orderFulfillmentsInnerPickupDetails.pickedUpAt) &&
        Objects.equals(this.pickupAt, orderFulfillmentsInnerPickupDetails.pickupAt) &&
        Objects.equals(this.pickupWindowDuration, orderFulfillmentsInnerPickupDetails.pickupWindowDuration) &&
        Objects.equals(this.placedAt, orderFulfillmentsInnerPickupDetails.placedAt) &&
        Objects.equals(this.prepTimeDuration, orderFulfillmentsInnerPickupDetails.prepTimeDuration) &&
        Objects.equals(this.readyAt, orderFulfillmentsInnerPickupDetails.readyAt) &&
        Objects.equals(this.recipient, orderFulfillmentsInnerPickupDetails.recipient) &&
        Objects.equals(this.rejectedAt, orderFulfillmentsInnerPickupDetails.rejectedAt) &&
        Objects.equals(this.scheduleType, orderFulfillmentsInnerPickupDetails.scheduleType);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(acceptedAt, autoCompleteDuration, cancelReason, canceledAt, curbsidePickupDetails, expiredAt, expiresAt, isCurbsidePickup, note, pickedUpAt, pickupAt, pickupWindowDuration, placedAt, prepTimeDuration, readyAt, recipient, rejectedAt, scheduleType);
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
    sb.append("class OrderFulfillmentsInnerPickupDetails {\n");
    sb.append("    acceptedAt: ").append(toIndentedString(acceptedAt)).append("\n");
    sb.append("    autoCompleteDuration: ").append(toIndentedString(autoCompleteDuration)).append("\n");
    sb.append("    cancelReason: ").append(toIndentedString(cancelReason)).append("\n");
    sb.append("    canceledAt: ").append(toIndentedString(canceledAt)).append("\n");
    sb.append("    curbsidePickupDetails: ").append(toIndentedString(curbsidePickupDetails)).append("\n");
    sb.append("    expiredAt: ").append(toIndentedString(expiredAt)).append("\n");
    sb.append("    expiresAt: ").append(toIndentedString(expiresAt)).append("\n");
    sb.append("    isCurbsidePickup: ").append(toIndentedString(isCurbsidePickup)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    pickedUpAt: ").append(toIndentedString(pickedUpAt)).append("\n");
    sb.append("    pickupAt: ").append(toIndentedString(pickupAt)).append("\n");
    sb.append("    pickupWindowDuration: ").append(toIndentedString(pickupWindowDuration)).append("\n");
    sb.append("    placedAt: ").append(toIndentedString(placedAt)).append("\n");
    sb.append("    prepTimeDuration: ").append(toIndentedString(prepTimeDuration)).append("\n");
    sb.append("    readyAt: ").append(toIndentedString(readyAt)).append("\n");
    sb.append("    recipient: ").append(toIndentedString(recipient)).append("\n");
    sb.append("    rejectedAt: ").append(toIndentedString(rejectedAt)).append("\n");
    sb.append("    scheduleType: ").append(toIndentedString(scheduleType)).append("\n");
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
    openapiFields.add("accepted_at");
    openapiFields.add("auto_complete_duration");
    openapiFields.add("cancel_reason");
    openapiFields.add("canceled_at");
    openapiFields.add("curbside_pickup_details");
    openapiFields.add("expired_at");
    openapiFields.add("expires_at");
    openapiFields.add("is_curbside_pickup");
    openapiFields.add("note");
    openapiFields.add("picked_up_at");
    openapiFields.add("pickup_at");
    openapiFields.add("pickup_window_duration");
    openapiFields.add("placed_at");
    openapiFields.add("prep_time_duration");
    openapiFields.add("ready_at");
    openapiFields.add("recipient");
    openapiFields.add("rejected_at");
    openapiFields.add("schedule_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderFulfillmentsInnerPickupDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderFulfillmentsInnerPickupDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderFulfillmentsInnerPickupDetails is not found in the empty JSON string", OrderFulfillmentsInnerPickupDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderFulfillmentsInnerPickupDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderFulfillmentsInnerPickupDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("auto_complete_duration") != null && !jsonObj.get("auto_complete_duration").isJsonNull()) && !jsonObj.get("auto_complete_duration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_complete_duration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_complete_duration").toString()));
      }
      if ((jsonObj.get("cancel_reason") != null && !jsonObj.get("cancel_reason").isJsonNull()) && !jsonObj.get("cancel_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cancel_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cancel_reason").toString()));
      }
      // validate the optional field `curbside_pickup_details`
      if (jsonObj.get("curbside_pickup_details") != null && !jsonObj.get("curbside_pickup_details").isJsonNull()) {
        OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails.validateJsonElement(jsonObj.get("curbside_pickup_details"));
      }
      if ((jsonObj.get("note") != null && !jsonObj.get("note").isJsonNull()) && !jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
      if ((jsonObj.get("pickup_window_duration") != null && !jsonObj.get("pickup_window_duration").isJsonNull()) && !jsonObj.get("pickup_window_duration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pickup_window_duration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pickup_window_duration").toString()));
      }
      if ((jsonObj.get("prep_time_duration") != null && !jsonObj.get("prep_time_duration").isJsonNull()) && !jsonObj.get("prep_time_duration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `prep_time_duration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("prep_time_duration").toString()));
      }
      // validate the optional field `recipient`
      if (jsonObj.get("recipient") != null && !jsonObj.get("recipient").isJsonNull()) {
        OrderFulfillmentsInnerPickupDetailsRecipient.validateJsonElement(jsonObj.get("recipient"));
      }
      if ((jsonObj.get("schedule_type") != null && !jsonObj.get("schedule_type").isJsonNull()) && !jsonObj.get("schedule_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `schedule_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("schedule_type").toString()));
      }
      // validate the optional field `schedule_type`
      if (jsonObj.get("schedule_type") != null && !jsonObj.get("schedule_type").isJsonNull()) {
        ScheduleTypeEnum.validateJsonElement(jsonObj.get("schedule_type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrderFulfillmentsInnerPickupDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderFulfillmentsInnerPickupDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderFulfillmentsInnerPickupDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderFulfillmentsInnerPickupDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderFulfillmentsInnerPickupDetails>() {
           @Override
           public void write(JsonWriter out, OrderFulfillmentsInnerPickupDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderFulfillmentsInnerPickupDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderFulfillmentsInnerPickupDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderFulfillmentsInnerPickupDetails
   * @throws IOException if the JSON string is invalid with respect to OrderFulfillmentsInnerPickupDetails
   */
  public static OrderFulfillmentsInnerPickupDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderFulfillmentsInnerPickupDetails.class);
  }

  /**
   * Convert an instance of OrderFulfillmentsInnerPickupDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

