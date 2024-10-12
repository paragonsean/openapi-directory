/*
 * CRM API
 * Welcome to the CRM API.  You can use this API to access all CRM API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ActivityAttendee;
import org.openapitools.client.model.Address;
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
 * Activity
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:49.113586-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Activity {
  public static final String SERIALIZED_NAME_ACCOUNT_ID = "account_id";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_ID)
  private String accountId;

  public static final String SERIALIZED_NAME_ACTIVITY_DATE = "activity_date";
  @SerializedName(SERIALIZED_NAME_ACTIVITY_DATE)
  private String activityDate;

  public static final String SERIALIZED_NAME_ACTIVITY_DATETIME = "activity_datetime";
  @SerializedName(SERIALIZED_NAME_ACTIVITY_DATETIME)
  private String activityDatetime;

  public static final String SERIALIZED_NAME_ALL_DAY_EVENT = "all_day_event";
  @SerializedName(SERIALIZED_NAME_ALL_DAY_EVENT)
  private Boolean allDayEvent;

  public static final String SERIALIZED_NAME_ARCHIVED = "archived";
  @SerializedName(SERIALIZED_NAME_ARCHIVED)
  private Boolean archived;

  public static final String SERIALIZED_NAME_ASSET_ID = "asset_id";
  @SerializedName(SERIALIZED_NAME_ASSET_ID)
  private String assetId;

  public static final String SERIALIZED_NAME_ATTENDEES = "attendees";
  @SerializedName(SERIALIZED_NAME_ATTENDEES)
  private List<ActivityAttendee> attendees = new ArrayList<>();

  public static final String SERIALIZED_NAME_CAMPAIGN_ID = "campaign_id";
  @SerializedName(SERIALIZED_NAME_CAMPAIGN_ID)
  private String campaignId;

  public static final String SERIALIZED_NAME_CASE_ID = "case_id";
  @SerializedName(SERIALIZED_NAME_CASE_ID)
  private String caseId;

  public static final String SERIALIZED_NAME_CHILD = "child";
  @SerializedName(SERIALIZED_NAME_CHILD)
  private Boolean child;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private String companyId;

  public static final String SERIALIZED_NAME_CONTACT_ID = "contact_id";
  @SerializedName(SERIALIZED_NAME_CONTACT_ID)
  private String contactId;

  public static final String SERIALIZED_NAME_CONTRACT_ID = "contract_id";
  @SerializedName(SERIALIZED_NAME_CONTRACT_ID)
  private String contractId;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<CustomField> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_CUSTOM_OBJECT_ID = "custom_object_id";
  @SerializedName(SERIALIZED_NAME_CUSTOM_OBJECT_ID)
  private String customObjectId;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DONE = "done";
  @SerializedName(SERIALIZED_NAME_DONE)
  private Boolean done;

  public static final String SERIALIZED_NAME_DOWNSTREAM_ID = "downstream_id";
  @SerializedName(SERIALIZED_NAME_DOWNSTREAM_ID)
  private String downstreamId;

  public static final String SERIALIZED_NAME_DURATION_MINUTES = "duration_minutes";
  @SerializedName(SERIALIZED_NAME_DURATION_MINUTES)
  private Integer durationMinutes;

  public static final String SERIALIZED_NAME_DURATION_SECONDS = "duration_seconds";
  @SerializedName(SERIALIZED_NAME_DURATION_SECONDS)
  private Integer durationSeconds;

  public static final String SERIALIZED_NAME_END_DATE = "end_date";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private String endDate;

  public static final String SERIALIZED_NAME_END_DATETIME = "end_datetime";
  @SerializedName(SERIALIZED_NAME_END_DATETIME)
  private String endDatetime;

  public static final String SERIALIZED_NAME_EVENT_SUB_TYPE = "event_sub_type";
  @SerializedName(SERIALIZED_NAME_EVENT_SUB_TYPE)
  private String eventSubType;

  public static final String SERIALIZED_NAME_GROUP_EVENT = "group_event";
  @SerializedName(SERIALIZED_NAME_GROUP_EVENT)
  private Boolean groupEvent;

  public static final String SERIALIZED_NAME_GROUP_EVENT_TYPE = "group_event_type";
  @SerializedName(SERIALIZED_NAME_GROUP_EVENT_TYPE)
  private String groupEventType;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LEAD_ID = "lead_id";
  @SerializedName(SERIALIZED_NAME_LEAD_ID)
  private String leadId;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private String location;

  public static final String SERIALIZED_NAME_LOCATION_ADDRESS = "location_address";
  @SerializedName(SERIALIZED_NAME_LOCATION_ADDRESS)
  private Address locationAddress;

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_OPPORTUNITY_ID = "opportunity_id";
  @SerializedName(SERIALIZED_NAME_OPPORTUNITY_ID)
  private String opportunityId;

  public static final String SERIALIZED_NAME_OWNER_ID = "owner_id";
  @SerializedName(SERIALIZED_NAME_OWNER_ID)
  private String ownerId;

  public static final String SERIALIZED_NAME_PRIVATE = "private";
  @SerializedName(SERIALIZED_NAME_PRIVATE)
  private Boolean _private;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "product_id";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private String productId;

  public static final String SERIALIZED_NAME_RECURRENT = "recurrent";
  @SerializedName(SERIALIZED_NAME_RECURRENT)
  private Boolean recurrent;

  public static final String SERIALIZED_NAME_REMINDER_DATETIME = "reminder_datetime";
  @SerializedName(SERIALIZED_NAME_REMINDER_DATETIME)
  private String reminderDatetime;

  public static final String SERIALIZED_NAME_REMINDER_SET = "reminder_set";
  @SerializedName(SERIALIZED_NAME_REMINDER_SET)
  private Boolean reminderSet;

  /**
   * Gets or Sets showAs
   */
  @JsonAdapter(ShowAsEnum.Adapter.class)
  public enum ShowAsEnum {
    FREE("free"),
    
    BUSY("busy");

    private String value;

    ShowAsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ShowAsEnum fromValue(String value) {
      for (ShowAsEnum b : ShowAsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<ShowAsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ShowAsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ShowAsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ShowAsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ShowAsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SHOW_AS = "show_as";
  @SerializedName(SERIALIZED_NAME_SHOW_AS)
  private ShowAsEnum showAs;

  public static final String SERIALIZED_NAME_SOLUTION_ID = "solution_id";
  @SerializedName(SERIALIZED_NAME_SOLUTION_ID)
  private String solutionId;

  public static final String SERIALIZED_NAME_START_DATETIME = "start_datetime";
  @SerializedName(SERIALIZED_NAME_START_DATETIME)
  private String startDatetime;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  /**
   * The type of the activity
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    CALL("call"),
    
    MEETING("meeting"),
    
    EMAIL("email"),
    
    NOTE("note"),
    
    TASK("task"),
    
    DEADLINE("deadline"),
    
    SEND_LETTER("send-letter"),
    
    SEND_QUOTE("send-quote"),
    
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
  private String updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public static final String SERIALIZED_NAME_VIDEO_CONFERENCE_ID = "video_conference_id";
  @SerializedName(SERIALIZED_NAME_VIDEO_CONFERENCE_ID)
  private String videoConferenceId;

  public static final String SERIALIZED_NAME_VIDEO_CONFERENCE_URL = "video_conference_url";
  @SerializedName(SERIALIZED_NAME_VIDEO_CONFERENCE_URL)
  private String videoConferenceUrl;

  public Activity() {
  }

  public Activity(
     String createdAt, 
     String createdBy, 
     String downstreamId, 
     Integer durationMinutes, 
     String id, 
     String updatedAt, 
     String updatedBy
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.downstreamId = downstreamId;
    this.durationMinutes = durationMinutes;
    this.id = id;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
  }

  public Activity accountId(String accountId) {
    this.accountId = accountId;
    return this;
  }

  /**
   * The account related to the activity
   * @return accountId
   */
  @javax.annotation.Nullable
  public String getAccountId() {
    return accountId;
  }

  public void setAccountId(String accountId) {
    this.accountId = accountId;
  }


  public Activity activityDate(String activityDate) {
    this.activityDate = activityDate;
    return this;
  }

  /**
   * The date of the activity
   * @return activityDate
   */
  @javax.annotation.Nullable
  public String getActivityDate() {
    return activityDate;
  }

  public void setActivityDate(String activityDate) {
    this.activityDate = activityDate;
  }


  public Activity activityDatetime(String activityDatetime) {
    this.activityDatetime = activityDatetime;
    return this;
  }

  /**
   * The date and time of the activity
   * @return activityDatetime
   */
  @javax.annotation.Nullable
  public String getActivityDatetime() {
    return activityDatetime;
  }

  public void setActivityDatetime(String activityDatetime) {
    this.activityDatetime = activityDatetime;
  }


  public Activity allDayEvent(Boolean allDayEvent) {
    this.allDayEvent = allDayEvent;
    return this;
  }

  /**
   * Whether the Activity is an all day event or not
   * @return allDayEvent
   */
  @javax.annotation.Nullable
  public Boolean getAllDayEvent() {
    return allDayEvent;
  }

  public void setAllDayEvent(Boolean allDayEvent) {
    this.allDayEvent = allDayEvent;
  }


  public Activity archived(Boolean archived) {
    this.archived = archived;
    return this;
  }

  /**
   * Whether the activity is archived or not
   * @return archived
   */
  @javax.annotation.Nullable
  public Boolean getArchived() {
    return archived;
  }

  public void setArchived(Boolean archived) {
    this.archived = archived;
  }


  public Activity assetId(String assetId) {
    this.assetId = assetId;
    return this;
  }

  /**
   * The asset related to the activity
   * @return assetId
   */
  @javax.annotation.Nullable
  public String getAssetId() {
    return assetId;
  }

  public void setAssetId(String assetId) {
    this.assetId = assetId;
  }


  public Activity attendees(List<ActivityAttendee> attendees) {
    this.attendees = attendees;
    return this;
  }

  public Activity addAttendeesItem(ActivityAttendee attendeesItem) {
    if (this.attendees == null) {
      this.attendees = new ArrayList<>();
    }
    this.attendees.add(attendeesItem);
    return this;
  }

  /**
   * Get attendees
   * @return attendees
   */
  @javax.annotation.Nullable
  public List<ActivityAttendee> getAttendees() {
    return attendees;
  }

  public void setAttendees(List<ActivityAttendee> attendees) {
    this.attendees = attendees;
  }


  public Activity campaignId(String campaignId) {
    this.campaignId = campaignId;
    return this;
  }

  /**
   * The campaign related to the activity
   * @return campaignId
   */
  @javax.annotation.Nullable
  public String getCampaignId() {
    return campaignId;
  }

  public void setCampaignId(String campaignId) {
    this.campaignId = campaignId;
  }


  public Activity caseId(String caseId) {
    this.caseId = caseId;
    return this;
  }

  /**
   * The case related to the activity
   * @return caseId
   */
  @javax.annotation.Nullable
  public String getCaseId() {
    return caseId;
  }

  public void setCaseId(String caseId) {
    this.caseId = caseId;
  }


  public Activity child(Boolean child) {
    this.child = child;
    return this;
  }

  /**
   * Whether the activity is a child of another activity or not
   * @return child
   */
  @javax.annotation.Nullable
  public Boolean getChild() {
    return child;
  }

  public void setChild(Boolean child) {
    this.child = child;
  }


  public Activity companyId(String companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * The company related to the activity
   * @return companyId
   */
  @javax.annotation.Nullable
  public String getCompanyId() {
    return companyId;
  }

  public void setCompanyId(String companyId) {
    this.companyId = companyId;
  }


  public Activity contactId(String contactId) {
    this.contactId = contactId;
    return this;
  }

  /**
   * The contact related to the activity
   * @return contactId
   */
  @javax.annotation.Nullable
  public String getContactId() {
    return contactId;
  }

  public void setContactId(String contactId) {
    this.contactId = contactId;
  }


  public Activity contractId(String contractId) {
    this.contractId = contractId;
    return this;
  }

  /**
   * The contract related to the activity
   * @return contractId
   */
  @javax.annotation.Nullable
  public String getContractId() {
    return contractId;
  }

  public void setContractId(String contractId) {
    this.contractId = contractId;
  }


  /**
   * The date and time when the activity was created
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }



  /**
   * The user who created the activity
   * @return createdBy
   */
  @javax.annotation.Nullable
  public String getCreatedBy() {
    return createdBy;
  }



  public Activity customFields(List<CustomField> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Activity addCustomFieldsItem(CustomField customFieldsItem) {
    if (this.customFields == null) {
      this.customFields = new ArrayList<>();
    }
    this.customFields.add(customFieldsItem);
    return this;
  }

  /**
   * Custom fields of the activity
   * @return customFields
   */
  @javax.annotation.Nullable
  public List<CustomField> getCustomFields() {
    return customFields;
  }

  public void setCustomFields(List<CustomField> customFields) {
    this.customFields = customFields;
  }


  public Activity customMappings(Object customMappings) {
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


  public Activity customObjectId(String customObjectId) {
    this.customObjectId = customObjectId;
    return this;
  }

  /**
   * The custom object related to the activity
   * @return customObjectId
   */
  @javax.annotation.Nullable
  public String getCustomObjectId() {
    return customObjectId;
  }

  public void setCustomObjectId(String customObjectId) {
    this.customObjectId = customObjectId;
  }


  public Activity deleted(Boolean deleted) {
    this.deleted = deleted;
    return this;
  }

  /**
   * Whether the activity is deleted or not
   * @return deleted
   */
  @javax.annotation.Nullable
  public Boolean getDeleted() {
    return deleted;
  }

  public void setDeleted(Boolean deleted) {
    this.deleted = deleted;
  }


  public Activity description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A description of the activity
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Activity done(Boolean done) {
    this.done = done;
    return this;
  }

  /**
   * Whether the Activity is done or not
   * @return done
   */
  @javax.annotation.Nullable
  public Boolean getDone() {
    return done;
  }

  public void setDone(Boolean done) {
    this.done = done;
  }


  /**
   * The third-party API ID of original entity
   * @return downstreamId
   */
  @javax.annotation.Nullable
  public String getDownstreamId() {
    return downstreamId;
  }



  /**
   * The duration of the activity in minutes
   * @return durationMinutes
   */
  @javax.annotation.Nullable
  public Integer getDurationMinutes() {
    return durationMinutes;
  }



  public Activity durationSeconds(Integer durationSeconds) {
    this.durationSeconds = durationSeconds;
    return this;
  }

  /**
   * The duration of the activity in seconds
   * minimum: 0
   * @return durationSeconds
   */
  @javax.annotation.Nullable
  public Integer getDurationSeconds() {
    return durationSeconds;
  }

  public void setDurationSeconds(Integer durationSeconds) {
    this.durationSeconds = durationSeconds;
  }


  public Activity endDate(String endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * The end date of the activity
   * @return endDate
   */
  @javax.annotation.Nullable
  public String getEndDate() {
    return endDate;
  }

  public void setEndDate(String endDate) {
    this.endDate = endDate;
  }


  public Activity endDatetime(String endDatetime) {
    this.endDatetime = endDatetime;
    return this;
  }

  /**
   * The end date and time of the activity
   * @return endDatetime
   */
  @javax.annotation.Nullable
  public String getEndDatetime() {
    return endDatetime;
  }

  public void setEndDatetime(String endDatetime) {
    this.endDatetime = endDatetime;
  }


  public Activity eventSubType(String eventSubType) {
    this.eventSubType = eventSubType;
    return this;
  }

  /**
   * The sub type of the group event
   * @return eventSubType
   */
  @javax.annotation.Nullable
  public String getEventSubType() {
    return eventSubType;
  }

  public void setEventSubType(String eventSubType) {
    this.eventSubType = eventSubType;
  }


  public Activity groupEvent(Boolean groupEvent) {
    this.groupEvent = groupEvent;
    return this;
  }

  /**
   * Whether the Activity is a group event or not
   * @return groupEvent
   */
  @javax.annotation.Nullable
  public Boolean getGroupEvent() {
    return groupEvent;
  }

  public void setGroupEvent(Boolean groupEvent) {
    this.groupEvent = groupEvent;
  }


  public Activity groupEventType(String groupEventType) {
    this.groupEventType = groupEventType;
    return this;
  }

  /**
   * The type of the group event
   * @return groupEventType
   */
  @javax.annotation.Nullable
  public String getGroupEventType() {
    return groupEventType;
  }

  public void setGroupEventType(String groupEventType) {
    this.groupEventType = groupEventType;
  }


  /**
   * The unique identifier of the activity
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Activity leadId(String leadId) {
    this.leadId = leadId;
    return this;
  }

  /**
   * The lead related to the activity
   * @return leadId
   */
  @javax.annotation.Nullable
  public String getLeadId() {
    return leadId;
  }

  public void setLeadId(String leadId) {
    this.leadId = leadId;
  }


  public Activity location(String location) {
    this.location = location;
    return this;
  }

  /**
   * The location of the activity
   * @return location
   */
  @javax.annotation.Nullable
  public String getLocation() {
    return location;
  }

  public void setLocation(String location) {
    this.location = location;
  }


  public Activity locationAddress(Address locationAddress) {
    this.locationAddress = locationAddress;
    return this;
  }

  /**
   * Get locationAddress
   * @return locationAddress
   */
  @javax.annotation.Nullable
  public Address getLocationAddress() {
    return locationAddress;
  }

  public void setLocationAddress(Address locationAddress) {
    this.locationAddress = locationAddress;
  }


  public Activity note(String note) {
    this.note = note;
    return this;
  }

  /**
   * An internal note about the activity
   * @return note
   */
  @javax.annotation.Nullable
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }


  public Activity opportunityId(String opportunityId) {
    this.opportunityId = opportunityId;
    return this;
  }

  /**
   * The opportunity related to the activity
   * @return opportunityId
   */
  @javax.annotation.Nullable
  public String getOpportunityId() {
    return opportunityId;
  }

  public void setOpportunityId(String opportunityId) {
    this.opportunityId = opportunityId;
  }


  public Activity ownerId(String ownerId) {
    this.ownerId = ownerId;
    return this;
  }

  /**
   * The owner of the activity
   * @return ownerId
   */
  @javax.annotation.Nullable
  public String getOwnerId() {
    return ownerId;
  }

  public void setOwnerId(String ownerId) {
    this.ownerId = ownerId;
  }


  public Activity _private(Boolean _private) {
    this._private = _private;
    return this;
  }

  /**
   * Whether the Activity is private or not
   * @return _private
   */
  @javax.annotation.Nullable
  public Boolean getPrivate() {
    return _private;
  }

  public void setPrivate(Boolean _private) {
    this._private = _private;
  }


  public Activity productId(String productId) {
    this.productId = productId;
    return this;
  }

  /**
   * The product related to the activity
   * @return productId
   */
  @javax.annotation.Nullable
  public String getProductId() {
    return productId;
  }

  public void setProductId(String productId) {
    this.productId = productId;
  }


  public Activity recurrent(Boolean recurrent) {
    this.recurrent = recurrent;
    return this;
  }

  /**
   * Whether the activity is recurrent or not
   * @return recurrent
   */
  @javax.annotation.Nullable
  public Boolean getRecurrent() {
    return recurrent;
  }

  public void setRecurrent(Boolean recurrent) {
    this.recurrent = recurrent;
  }


  public Activity reminderDatetime(String reminderDatetime) {
    this.reminderDatetime = reminderDatetime;
    return this;
  }

  /**
   * The date and time of the reminder
   * @return reminderDatetime
   */
  @javax.annotation.Nullable
  public String getReminderDatetime() {
    return reminderDatetime;
  }

  public void setReminderDatetime(String reminderDatetime) {
    this.reminderDatetime = reminderDatetime;
  }


  public Activity reminderSet(Boolean reminderSet) {
    this.reminderSet = reminderSet;
    return this;
  }

  /**
   * Whether the reminder is set or not
   * @return reminderSet
   */
  @javax.annotation.Nullable
  public Boolean getReminderSet() {
    return reminderSet;
  }

  public void setReminderSet(Boolean reminderSet) {
    this.reminderSet = reminderSet;
  }


  public Activity showAs(ShowAsEnum showAs) {
    this.showAs = showAs;
    return this;
  }

  /**
   * Get showAs
   * @return showAs
   */
  @javax.annotation.Nullable
  public ShowAsEnum getShowAs() {
    return showAs;
  }

  public void setShowAs(ShowAsEnum showAs) {
    this.showAs = showAs;
  }


  public Activity solutionId(String solutionId) {
    this.solutionId = solutionId;
    return this;
  }

  /**
   * The solution related to the activity
   * @return solutionId
   */
  @javax.annotation.Nullable
  public String getSolutionId() {
    return solutionId;
  }

  public void setSolutionId(String solutionId) {
    this.solutionId = solutionId;
  }


  public Activity startDatetime(String startDatetime) {
    this.startDatetime = startDatetime;
    return this;
  }

  /**
   * The start date and time of the activity
   * @return startDatetime
   */
  @javax.annotation.Nullable
  public String getStartDatetime() {
    return startDatetime;
  }

  public void setStartDatetime(String startDatetime) {
    this.startDatetime = startDatetime;
  }


  public Activity title(String title) {
    this.title = title;
    return this;
  }

  /**
   * The title of the activity
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Activity type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The type of the activity
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
   * The date and time when the activity was last updated
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }



  /**
   * The user who last updated the activity
   * @return updatedBy
   */
  @javax.annotation.Nullable
  public String getUpdatedBy() {
    return updatedBy;
  }



  public Activity userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * The user related to the activity
   * @return userId
   */
  @javax.annotation.Nullable
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }


  public Activity videoConferenceId(String videoConferenceId) {
    this.videoConferenceId = videoConferenceId;
    return this;
  }

  /**
   * The ID of the video conference
   * @return videoConferenceId
   */
  @javax.annotation.Nullable
  public String getVideoConferenceId() {
    return videoConferenceId;
  }

  public void setVideoConferenceId(String videoConferenceId) {
    this.videoConferenceId = videoConferenceId;
  }


  public Activity videoConferenceUrl(String videoConferenceUrl) {
    this.videoConferenceUrl = videoConferenceUrl;
    return this;
  }

  /**
   * The URL of the video conference
   * @return videoConferenceUrl
   */
  @javax.annotation.Nullable
  public String getVideoConferenceUrl() {
    return videoConferenceUrl;
  }

  public void setVideoConferenceUrl(String videoConferenceUrl) {
    this.videoConferenceUrl = videoConferenceUrl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Activity activity = (Activity) o;
    return Objects.equals(this.accountId, activity.accountId) &&
        Objects.equals(this.activityDate, activity.activityDate) &&
        Objects.equals(this.activityDatetime, activity.activityDatetime) &&
        Objects.equals(this.allDayEvent, activity.allDayEvent) &&
        Objects.equals(this.archived, activity.archived) &&
        Objects.equals(this.assetId, activity.assetId) &&
        Objects.equals(this.attendees, activity.attendees) &&
        Objects.equals(this.campaignId, activity.campaignId) &&
        Objects.equals(this.caseId, activity.caseId) &&
        Objects.equals(this.child, activity.child) &&
        Objects.equals(this.companyId, activity.companyId) &&
        Objects.equals(this.contactId, activity.contactId) &&
        Objects.equals(this.contractId, activity.contractId) &&
        Objects.equals(this.createdAt, activity.createdAt) &&
        Objects.equals(this.createdBy, activity.createdBy) &&
        Objects.equals(this.customFields, activity.customFields) &&
        Objects.equals(this.customMappings, activity.customMappings) &&
        Objects.equals(this.customObjectId, activity.customObjectId) &&
        Objects.equals(this.deleted, activity.deleted) &&
        Objects.equals(this.description, activity.description) &&
        Objects.equals(this.done, activity.done) &&
        Objects.equals(this.downstreamId, activity.downstreamId) &&
        Objects.equals(this.durationMinutes, activity.durationMinutes) &&
        Objects.equals(this.durationSeconds, activity.durationSeconds) &&
        Objects.equals(this.endDate, activity.endDate) &&
        Objects.equals(this.endDatetime, activity.endDatetime) &&
        Objects.equals(this.eventSubType, activity.eventSubType) &&
        Objects.equals(this.groupEvent, activity.groupEvent) &&
        Objects.equals(this.groupEventType, activity.groupEventType) &&
        Objects.equals(this.id, activity.id) &&
        Objects.equals(this.leadId, activity.leadId) &&
        Objects.equals(this.location, activity.location) &&
        Objects.equals(this.locationAddress, activity.locationAddress) &&
        Objects.equals(this.note, activity.note) &&
        Objects.equals(this.opportunityId, activity.opportunityId) &&
        Objects.equals(this.ownerId, activity.ownerId) &&
        Objects.equals(this._private, activity._private) &&
        Objects.equals(this.productId, activity.productId) &&
        Objects.equals(this.recurrent, activity.recurrent) &&
        Objects.equals(this.reminderDatetime, activity.reminderDatetime) &&
        Objects.equals(this.reminderSet, activity.reminderSet) &&
        Objects.equals(this.showAs, activity.showAs) &&
        Objects.equals(this.solutionId, activity.solutionId) &&
        Objects.equals(this.startDatetime, activity.startDatetime) &&
        Objects.equals(this.title, activity.title) &&
        Objects.equals(this.type, activity.type) &&
        Objects.equals(this.updatedAt, activity.updatedAt) &&
        Objects.equals(this.updatedBy, activity.updatedBy) &&
        Objects.equals(this.userId, activity.userId) &&
        Objects.equals(this.videoConferenceId, activity.videoConferenceId) &&
        Objects.equals(this.videoConferenceUrl, activity.videoConferenceUrl);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountId, activityDate, activityDatetime, allDayEvent, archived, assetId, attendees, campaignId, caseId, child, companyId, contactId, contractId, createdAt, createdBy, customFields, customMappings, customObjectId, deleted, description, done, downstreamId, durationMinutes, durationSeconds, endDate, endDatetime, eventSubType, groupEvent, groupEventType, id, leadId, location, locationAddress, note, opportunityId, ownerId, _private, productId, recurrent, reminderDatetime, reminderSet, showAs, solutionId, startDatetime, title, type, updatedAt, updatedBy, userId, videoConferenceId, videoConferenceUrl);
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
    sb.append("class Activity {\n");
    sb.append("    accountId: ").append(toIndentedString(accountId)).append("\n");
    sb.append("    activityDate: ").append(toIndentedString(activityDate)).append("\n");
    sb.append("    activityDatetime: ").append(toIndentedString(activityDatetime)).append("\n");
    sb.append("    allDayEvent: ").append(toIndentedString(allDayEvent)).append("\n");
    sb.append("    archived: ").append(toIndentedString(archived)).append("\n");
    sb.append("    assetId: ").append(toIndentedString(assetId)).append("\n");
    sb.append("    attendees: ").append(toIndentedString(attendees)).append("\n");
    sb.append("    campaignId: ").append(toIndentedString(campaignId)).append("\n");
    sb.append("    caseId: ").append(toIndentedString(caseId)).append("\n");
    sb.append("    child: ").append(toIndentedString(child)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    contactId: ").append(toIndentedString(contactId)).append("\n");
    sb.append("    contractId: ").append(toIndentedString(contractId)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    customObjectId: ").append(toIndentedString(customObjectId)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    done: ").append(toIndentedString(done)).append("\n");
    sb.append("    downstreamId: ").append(toIndentedString(downstreamId)).append("\n");
    sb.append("    durationMinutes: ").append(toIndentedString(durationMinutes)).append("\n");
    sb.append("    durationSeconds: ").append(toIndentedString(durationSeconds)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    endDatetime: ").append(toIndentedString(endDatetime)).append("\n");
    sb.append("    eventSubType: ").append(toIndentedString(eventSubType)).append("\n");
    sb.append("    groupEvent: ").append(toIndentedString(groupEvent)).append("\n");
    sb.append("    groupEventType: ").append(toIndentedString(groupEventType)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    leadId: ").append(toIndentedString(leadId)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    locationAddress: ").append(toIndentedString(locationAddress)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    opportunityId: ").append(toIndentedString(opportunityId)).append("\n");
    sb.append("    ownerId: ").append(toIndentedString(ownerId)).append("\n");
    sb.append("    _private: ").append(toIndentedString(_private)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    recurrent: ").append(toIndentedString(recurrent)).append("\n");
    sb.append("    reminderDatetime: ").append(toIndentedString(reminderDatetime)).append("\n");
    sb.append("    reminderSet: ").append(toIndentedString(reminderSet)).append("\n");
    sb.append("    showAs: ").append(toIndentedString(showAs)).append("\n");
    sb.append("    solutionId: ").append(toIndentedString(solutionId)).append("\n");
    sb.append("    startDatetime: ").append(toIndentedString(startDatetime)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    videoConferenceId: ").append(toIndentedString(videoConferenceId)).append("\n");
    sb.append("    videoConferenceUrl: ").append(toIndentedString(videoConferenceUrl)).append("\n");
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
    openapiFields.add("account_id");
    openapiFields.add("activity_date");
    openapiFields.add("activity_datetime");
    openapiFields.add("all_day_event");
    openapiFields.add("archived");
    openapiFields.add("asset_id");
    openapiFields.add("attendees");
    openapiFields.add("campaign_id");
    openapiFields.add("case_id");
    openapiFields.add("child");
    openapiFields.add("company_id");
    openapiFields.add("contact_id");
    openapiFields.add("contract_id");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("custom_fields");
    openapiFields.add("custom_mappings");
    openapiFields.add("custom_object_id");
    openapiFields.add("deleted");
    openapiFields.add("description");
    openapiFields.add("done");
    openapiFields.add("downstream_id");
    openapiFields.add("duration_minutes");
    openapiFields.add("duration_seconds");
    openapiFields.add("end_date");
    openapiFields.add("end_datetime");
    openapiFields.add("event_sub_type");
    openapiFields.add("group_event");
    openapiFields.add("group_event_type");
    openapiFields.add("id");
    openapiFields.add("lead_id");
    openapiFields.add("location");
    openapiFields.add("location_address");
    openapiFields.add("note");
    openapiFields.add("opportunity_id");
    openapiFields.add("owner_id");
    openapiFields.add("private");
    openapiFields.add("product_id");
    openapiFields.add("recurrent");
    openapiFields.add("reminder_datetime");
    openapiFields.add("reminder_set");
    openapiFields.add("show_as");
    openapiFields.add("solution_id");
    openapiFields.add("start_datetime");
    openapiFields.add("title");
    openapiFields.add("type");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("user_id");
    openapiFields.add("video_conference_id");
    openapiFields.add("video_conference_url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Activity
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Activity.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Activity is not found in the empty JSON string", Activity.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Activity.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Activity` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Activity.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("account_id") != null && !jsonObj.get("account_id").isJsonNull()) && !jsonObj.get("account_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `account_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("account_id").toString()));
      }
      if ((jsonObj.get("activity_date") != null && !jsonObj.get("activity_date").isJsonNull()) && !jsonObj.get("activity_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `activity_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("activity_date").toString()));
      }
      if ((jsonObj.get("activity_datetime") != null && !jsonObj.get("activity_datetime").isJsonNull()) && !jsonObj.get("activity_datetime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `activity_datetime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("activity_datetime").toString()));
      }
      if ((jsonObj.get("asset_id") != null && !jsonObj.get("asset_id").isJsonNull()) && !jsonObj.get("asset_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `asset_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("asset_id").toString()));
      }
      if (jsonObj.get("attendees") != null && !jsonObj.get("attendees").isJsonNull()) {
        JsonArray jsonArrayattendees = jsonObj.getAsJsonArray("attendees");
        if (jsonArrayattendees != null) {
          // ensure the json data is an array
          if (!jsonObj.get("attendees").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `attendees` to be an array in the JSON string but got `%s`", jsonObj.get("attendees").toString()));
          }

          // validate the optional field `attendees` (array)
          for (int i = 0; i < jsonArrayattendees.size(); i++) {
            ActivityAttendee.validateJsonElement(jsonArrayattendees.get(i));
          };
        }
      }
      if ((jsonObj.get("campaign_id") != null && !jsonObj.get("campaign_id").isJsonNull()) && !jsonObj.get("campaign_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `campaign_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("campaign_id").toString()));
      }
      if ((jsonObj.get("case_id") != null && !jsonObj.get("case_id").isJsonNull()) && !jsonObj.get("case_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `case_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("case_id").toString()));
      }
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("contact_id") != null && !jsonObj.get("contact_id").isJsonNull()) && !jsonObj.get("contact_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact_id").toString()));
      }
      if ((jsonObj.get("contract_id") != null && !jsonObj.get("contract_id").isJsonNull()) && !jsonObj.get("contract_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contract_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contract_id").toString()));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) && !jsonObj.get("created_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by").toString()));
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
      if ((jsonObj.get("custom_object_id") != null && !jsonObj.get("custom_object_id").isJsonNull()) && !jsonObj.get("custom_object_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `custom_object_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("custom_object_id").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("downstream_id") != null && !jsonObj.get("downstream_id").isJsonNull()) && !jsonObj.get("downstream_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `downstream_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("downstream_id").toString()));
      }
      if ((jsonObj.get("end_date") != null && !jsonObj.get("end_date").isJsonNull()) && !jsonObj.get("end_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("end_date").toString()));
      }
      if ((jsonObj.get("end_datetime") != null && !jsonObj.get("end_datetime").isJsonNull()) && !jsonObj.get("end_datetime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_datetime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("end_datetime").toString()));
      }
      if ((jsonObj.get("event_sub_type") != null && !jsonObj.get("event_sub_type").isJsonNull()) && !jsonObj.get("event_sub_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `event_sub_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("event_sub_type").toString()));
      }
      if ((jsonObj.get("group_event_type") != null && !jsonObj.get("group_event_type").isJsonNull()) && !jsonObj.get("group_event_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group_event_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group_event_type").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("lead_id") != null && !jsonObj.get("lead_id").isJsonNull()) && !jsonObj.get("lead_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lead_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lead_id").toString()));
      }
      if ((jsonObj.get("location") != null && !jsonObj.get("location").isJsonNull()) && !jsonObj.get("location").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location").toString()));
      }
      // validate the optional field `location_address`
      if (jsonObj.get("location_address") != null && !jsonObj.get("location_address").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("location_address"));
      }
      if ((jsonObj.get("note") != null && !jsonObj.get("note").isJsonNull()) && !jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
      if ((jsonObj.get("opportunity_id") != null && !jsonObj.get("opportunity_id").isJsonNull()) && !jsonObj.get("opportunity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `opportunity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("opportunity_id").toString()));
      }
      if ((jsonObj.get("owner_id") != null && !jsonObj.get("owner_id").isJsonNull()) && !jsonObj.get("owner_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner_id").toString()));
      }
      if ((jsonObj.get("product_id") != null && !jsonObj.get("product_id").isJsonNull()) && !jsonObj.get("product_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `product_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("product_id").toString()));
      }
      if ((jsonObj.get("reminder_datetime") != null && !jsonObj.get("reminder_datetime").isJsonNull()) && !jsonObj.get("reminder_datetime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reminder_datetime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reminder_datetime").toString()));
      }
      if ((jsonObj.get("show_as") != null && !jsonObj.get("show_as").isJsonNull()) && !jsonObj.get("show_as").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `show_as` to be a primitive type in the JSON string but got `%s`", jsonObj.get("show_as").toString()));
      }
      // validate the optional field `show_as`
      if (jsonObj.get("show_as") != null && !jsonObj.get("show_as").isJsonNull()) {
        ShowAsEnum.validateJsonElement(jsonObj.get("show_as"));
      }
      if ((jsonObj.get("solution_id") != null && !jsonObj.get("solution_id").isJsonNull()) && !jsonObj.get("solution_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `solution_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("solution_id").toString()));
      }
      if ((jsonObj.get("start_datetime") != null && !jsonObj.get("start_datetime").isJsonNull()) && !jsonObj.get("start_datetime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `start_datetime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("start_datetime").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
      if ((jsonObj.get("user_id") != null && !jsonObj.get("user_id").isJsonNull()) && !jsonObj.get("user_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_id").toString()));
      }
      if ((jsonObj.get("video_conference_id") != null && !jsonObj.get("video_conference_id").isJsonNull()) && !jsonObj.get("video_conference_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `video_conference_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("video_conference_id").toString()));
      }
      if ((jsonObj.get("video_conference_url") != null && !jsonObj.get("video_conference_url").isJsonNull()) && !jsonObj.get("video_conference_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `video_conference_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("video_conference_url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Activity.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Activity' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Activity> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Activity.class));

       return (TypeAdapter<T>) new TypeAdapter<Activity>() {
           @Override
           public void write(JsonWriter out, Activity value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Activity read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Activity given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Activity
   * @throws IOException if the JSON string is invalid with respect to Activity
   */
  public static Activity fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Activity.class);
  }

  /**
   * Convert an instance of Activity to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

