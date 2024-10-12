/*
 * ATS API
 * Welcome to the ATS API.  You can use this API to access all ATS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import org.openapitools.client.model.Address;
import org.openapitools.client.model.Branch;
import org.openapitools.client.model.CustomField;
import org.openapitools.client.model.Department;
import org.openapitools.client.model.JobBlocksInner;
import org.openapitools.client.model.JobLinksInner;
import org.openapitools.client.model.JobSalary;
import org.openapitools.client.model.JobStatus;
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
 * Job
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:53.902874-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Job {
  public static final String SERIALIZED_NAME_ADDRESSES = "addresses";
  @SerializedName(SERIALIZED_NAME_ADDRESSES)
  private List<Address> addresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_AVAILABLE_TO_EMPLOYEES = "available_to_employees";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_TO_EMPLOYEES)
  private Boolean availableToEmployees;

  public static final String SERIALIZED_NAME_BLOCKS = "blocks";
  @SerializedName(SERIALIZED_NAME_BLOCKS)
  private List<JobBlocksInner> blocks = new ArrayList<>();

  public static final String SERIALIZED_NAME_BRANCH = "branch";
  @SerializedName(SERIALIZED_NAME_BRANCH)
  private Branch branch;

  public static final String SERIALIZED_NAME_CLOSING = "closing";
  @SerializedName(SERIALIZED_NAME_CLOSING)
  private String closing;

  public static final String SERIALIZED_NAME_CLOSING_DATE = "closing_date";
  @SerializedName(SERIALIZED_NAME_CLOSING_DATE)
  private LocalDate closingDate;

  public static final String SERIALIZED_NAME_CLOSING_HTML = "closing_html";
  @SerializedName(SERIALIZED_NAME_CLOSING_HTML)
  private String closingHtml;

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_CONFIDENTIAL = "confidential";
  @SerializedName(SERIALIZED_NAME_CONFIDENTIAL)
  private Boolean confidential;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<CustomField> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_DEPARTMENT = "department";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT)
  private Department department;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DESCRIPTION_HTML = "description_html";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION_HTML)
  private String descriptionHtml;

  /**
   * Gets or Sets employmentTerms
   */
  @JsonAdapter(EmploymentTermsEnum.Adapter.class)
  public enum EmploymentTermsEnum {
    FULL_TIME("full-time"),
    
    PART_TIME("part-time"),
    
    INTERNSHIP("internship"),
    
    CONTRACTOR("contractor"),
    
    EMPLOYEE("employee"),
    
    FREELANCE("freelance"),
    
    TEMP("temp"),
    
    SEASONAL("seasonal"),
    
    VOLUNTEER("volunteer"),
    
    OTHER("other");

    private String value;

    EmploymentTermsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EmploymentTermsEnum fromValue(String value) {
      for (EmploymentTermsEnum b : EmploymentTermsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<EmploymentTermsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EmploymentTermsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EmploymentTermsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EmploymentTermsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EmploymentTermsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EMPLOYMENT_TERMS = "employment_terms";
  @SerializedName(SERIALIZED_NAME_EMPLOYMENT_TERMS)
  private EmploymentTermsEnum employmentTerms;

  public static final String SERIALIZED_NAME_EXPERIENCE = "experience";
  @SerializedName(SERIALIZED_NAME_EXPERIENCE)
  private String experience;

  public static final String SERIALIZED_NAME_FOLLOWERS = "followers";
  @SerializedName(SERIALIZED_NAME_FOLLOWERS)
  private List<String> followers;

  public static final String SERIALIZED_NAME_HIRING_MANAGERS = "hiring_managers";
  @SerializedName(SERIALIZED_NAME_HIRING_MANAGERS)
  private List<String> hiringManagers = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_JOB_PORTAL_URL = "job_portal_url";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_JOB_PORTAL_URL)
  private String jobPortalUrl;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<JobLinksInner> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private String location;

  public static final String SERIALIZED_NAME_OWNER_ID = "owner_id";
  @SerializedName(SERIALIZED_NAME_OWNER_ID)
  private String ownerId;

  public static final String SERIALIZED_NAME_PUBLISHED_AT = "published_at";
  @SerializedName(SERIALIZED_NAME_PUBLISHED_AT)
  private OffsetDateTime publishedAt;

  public static final String SERIALIZED_NAME_RECORD_URL = "record_url";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_RECORD_URL)
  private String recordUrl;

  public static final String SERIALIZED_NAME_RECRUITERS = "recruiters";
  @SerializedName(SERIALIZED_NAME_RECRUITERS)
  private List<String> recruiters;

  public static final String SERIALIZED_NAME_REMOTE = "remote";
  @SerializedName(SERIALIZED_NAME_REMOTE)
  private Boolean remote;

  public static final String SERIALIZED_NAME_REQUISITION_ID = "requisition_id";
  @SerializedName(SERIALIZED_NAME_REQUISITION_ID)
  private String requisitionId;

  public static final String SERIALIZED_NAME_SALARY = "salary";
  @SerializedName(SERIALIZED_NAME_SALARY)
  private JobSalary salary;

  public static final String SERIALIZED_NAME_SEQUENCE = "sequence";
  @SerializedName(SERIALIZED_NAME_SEQUENCE)
  private Integer sequence;

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private String slug;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private JobStatus status;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_URL = "url";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  /**
   * The visibility of the job
   */
  @JsonAdapter(VisibilityEnum.Adapter.class)
  public enum VisibilityEnum {
    DRAFT("draft"),
    
    PUBLIC("public"),
    
    INTERNAL("internal");

    private String value;

    VisibilityEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static VisibilityEnum fromValue(String value) {
      for (VisibilityEnum b : VisibilityEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<VisibilityEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final VisibilityEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public VisibilityEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return VisibilityEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      VisibilityEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VISIBILITY = "visibility";
  @SerializedName(SERIALIZED_NAME_VISIBILITY)
  private VisibilityEnum visibility;

  public Job() {
  }

  public Job(
     OffsetDateTime createdAt, 
     String createdBy, 
     String id, 
     OffsetDateTime publishedAt, 
     OffsetDateTime updatedAt, 
     String updatedBy
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.id = id;
    this.publishedAt = publishedAt;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
  }

  public Job addresses(List<Address> addresses) {
    this.addresses = addresses;
    return this;
  }

  public Job addAddressesItem(Address addressesItem) {
    if (this.addresses == null) {
      this.addresses = new ArrayList<>();
    }
    this.addresses.add(addressesItem);
    return this;
  }

  /**
   * Get addresses
   * @return addresses
   */
  @javax.annotation.Nullable
  public List<Address> getAddresses() {
    return addresses;
  }

  public void setAddresses(List<Address> addresses) {
    this.addresses = addresses;
  }


  public Job availableToEmployees(Boolean availableToEmployees) {
    this.availableToEmployees = availableToEmployees;
    return this;
  }

  /**
   * Specifies whether an employee of the organization can apply for the job.
   * @return availableToEmployees
   */
  @javax.annotation.Nullable
  public Boolean getAvailableToEmployees() {
    return availableToEmployees;
  }

  public void setAvailableToEmployees(Boolean availableToEmployees) {
    this.availableToEmployees = availableToEmployees;
  }


  public Job blocks(List<JobBlocksInner> blocks) {
    this.blocks = blocks;
    return this;
  }

  public Job addBlocksItem(JobBlocksInner blocksItem) {
    if (this.blocks == null) {
      this.blocks = new ArrayList<>();
    }
    this.blocks.add(blocksItem);
    return this;
  }

  /**
   * Get blocks
   * @return blocks
   */
  @javax.annotation.Nullable
  public List<JobBlocksInner> getBlocks() {
    return blocks;
  }

  public void setBlocks(List<JobBlocksInner> blocks) {
    this.blocks = blocks;
  }


  public Job branch(Branch branch) {
    this.branch = branch;
    return this;
  }

  /**
   * Get branch
   * @return branch
   */
  @javax.annotation.Nullable
  public Branch getBranch() {
    return branch;
  }

  public void setBranch(Branch branch) {
    this.branch = branch;
  }


  public Job closing(String closing) {
    this.closing = closing;
    return this;
  }

  /**
   * Get closing
   * @return closing
   */
  @javax.annotation.Nullable
  public String getClosing() {
    return closing;
  }

  public void setClosing(String closing) {
    this.closing = closing;
  }


  public Job closingDate(LocalDate closingDate) {
    this.closingDate = closingDate;
    return this;
  }

  /**
   * Get closingDate
   * @return closingDate
   */
  @javax.annotation.Nullable
  public LocalDate getClosingDate() {
    return closingDate;
  }

  public void setClosingDate(LocalDate closingDate) {
    this.closingDate = closingDate;
  }


  public Job closingHtml(String closingHtml) {
    this.closingHtml = closingHtml;
    return this;
  }

  /**
   * The closing section of the job description in HTML format
   * @return closingHtml
   */
  @javax.annotation.Nullable
  public String getClosingHtml() {
    return closingHtml;
  }

  public void setClosingHtml(String closingHtml) {
    this.closingHtml = closingHtml;
  }


  public Job code(String code) {
    this.code = code;
    return this;
  }

  /**
   * The code of the job.
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public Job confidential(Boolean confidential) {
    this.confidential = confidential;
    return this;
  }

  /**
   * Get confidential
   * @return confidential
   */
  @javax.annotation.Nullable
  public Boolean getConfidential() {
    return confidential;
  }

  public void setConfidential(Boolean confidential) {
    this.confidential = confidential;
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



  public Job customFields(List<CustomField> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Job addCustomFieldsItem(CustomField customFieldsItem) {
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


  public Job customMappings(Object customMappings) {
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


  public Job deleted(Boolean deleted) {
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


  public Job department(Department department) {
    this.department = department;
    return this;
  }

  /**
   * Get department
   * @return department
   */
  @javax.annotation.Nullable
  public Department getDepartment() {
    return department;
  }

  public void setDepartment(Department department) {
    this.department = department;
  }


  public Job description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A description of the object.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Job descriptionHtml(String descriptionHtml) {
    this.descriptionHtml = descriptionHtml;
    return this;
  }

  /**
   * The job description in HTML format
   * @return descriptionHtml
   */
  @javax.annotation.Nullable
  public String getDescriptionHtml() {
    return descriptionHtml;
  }

  public void setDescriptionHtml(String descriptionHtml) {
    this.descriptionHtml = descriptionHtml;
  }


  public Job employmentTerms(EmploymentTermsEnum employmentTerms) {
    this.employmentTerms = employmentTerms;
    return this;
  }

  /**
   * Get employmentTerms
   * @return employmentTerms
   */
  @javax.annotation.Nullable
  public EmploymentTermsEnum getEmploymentTerms() {
    return employmentTerms;
  }

  public void setEmploymentTerms(EmploymentTermsEnum employmentTerms) {
    this.employmentTerms = employmentTerms;
  }


  public Job experience(String experience) {
    this.experience = experience;
    return this;
  }

  /**
   * Level of experience required for the job role.
   * @return experience
   */
  @javax.annotation.Nullable
  public String getExperience() {
    return experience;
  }

  public void setExperience(String experience) {
    this.experience = experience;
  }


  public Job followers(List<String> followers) {
    this.followers = followers;
    return this;
  }

  public Job addFollowersItem(String followersItem) {
    if (this.followers == null) {
      this.followers = new ArrayList<>();
    }
    this.followers.add(followersItem);
    return this;
  }

  /**
   * Get followers
   * @return followers
   */
  @javax.annotation.Nullable
  public List<String> getFollowers() {
    return followers;
  }

  public void setFollowers(List<String> followers) {
    this.followers = followers;
  }


  public Job hiringManagers(List<String> hiringManagers) {
    this.hiringManagers = hiringManagers;
    return this;
  }

  public Job addHiringManagersItem(String hiringManagersItem) {
    if (this.hiringManagers == null) {
      this.hiringManagers = new ArrayList<>();
    }
    this.hiringManagers.add(hiringManagersItem);
    return this;
  }

  /**
   * Get hiringManagers
   * @return hiringManagers
   */
  @javax.annotation.Nullable
  public List<String> getHiringManagers() {
    return hiringManagers;
  }

  public void setHiringManagers(List<String> hiringManagers) {
    this.hiringManagers = hiringManagers;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  @Deprecated
  public Job jobPortalUrl(String jobPortalUrl) {
    this.jobPortalUrl = jobPortalUrl;
    return this;
  }

  /**
   * URL of the job portal
   * @return jobPortalUrl
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getJobPortalUrl() {
    return jobPortalUrl;
  }

  @Deprecated
  public void setJobPortalUrl(String jobPortalUrl) {
    this.jobPortalUrl = jobPortalUrl;
  }


  public Job language(String language) {
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


  public Job links(List<JobLinksInner> links) {
    this.links = links;
    return this;
  }

  public Job addLinksItem(JobLinksInner linksItem) {
    if (this.links == null) {
      this.links = new ArrayList<>();
    }
    this.links.add(linksItem);
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nullable
  public List<JobLinksInner> getLinks() {
    return links;
  }

  public void setLinks(List<JobLinksInner> links) {
    this.links = links;
  }


  public Job location(String location) {
    this.location = location;
    return this;
  }

  /**
   * Specifies the location for the job posting.
   * @return location
   */
  @javax.annotation.Nullable
  public String getLocation() {
    return location;
  }

  public void setLocation(String location) {
    this.location = location;
  }


  public Job ownerId(String ownerId) {
    this.ownerId = ownerId;
    return this;
  }

  /**
   * Get ownerId
   * @return ownerId
   */
  @javax.annotation.Nullable
  public String getOwnerId() {
    return ownerId;
  }

  public void setOwnerId(String ownerId) {
    this.ownerId = ownerId;
  }


  /**
   * Get publishedAt
   * @return publishedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPublishedAt() {
    return publishedAt;
  }



  @Deprecated
  public Job recordUrl(String recordUrl) {
    this.recordUrl = recordUrl;
    return this;
  }

  /**
   * Get recordUrl
   * @return recordUrl
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getRecordUrl() {
    return recordUrl;
  }

  @Deprecated
  public void setRecordUrl(String recordUrl) {
    this.recordUrl = recordUrl;
  }


  public Job recruiters(List<String> recruiters) {
    this.recruiters = recruiters;
    return this;
  }

  public Job addRecruitersItem(String recruitersItem) {
    if (this.recruiters == null) {
      this.recruiters = new ArrayList<>();
    }
    this.recruiters.add(recruitersItem);
    return this;
  }

  /**
   * The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant
   * @return recruiters
   */
  @javax.annotation.Nullable
  public List<String> getRecruiters() {
    return recruiters;
  }

  public void setRecruiters(List<String> recruiters) {
    this.recruiters = recruiters;
  }


  public Job remote(Boolean remote) {
    this.remote = remote;
    return this;
  }

  /**
   * Specifies whether the posting is for a remote job.
   * @return remote
   */
  @javax.annotation.Nullable
  public Boolean getRemote() {
    return remote;
  }

  public void setRemote(Boolean remote) {
    this.remote = remote;
  }


  public Job requisitionId(String requisitionId) {
    this.requisitionId = requisitionId;
    return this;
  }

  /**
   * A job&#39;s Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company&#39;s internal processes.
   * @return requisitionId
   */
  @javax.annotation.Nullable
  public String getRequisitionId() {
    return requisitionId;
  }

  public void setRequisitionId(String requisitionId) {
    this.requisitionId = requisitionId;
  }


  public Job salary(JobSalary salary) {
    this.salary = salary;
    return this;
  }

  /**
   * Get salary
   * @return salary
   */
  @javax.annotation.Nullable
  public JobSalary getSalary() {
    return salary;
  }

  public void setSalary(JobSalary salary) {
    this.salary = salary;
  }


  public Job sequence(Integer sequence) {
    this.sequence = sequence;
    return this;
  }

  /**
   * Sequence in relation to other jobs.
   * @return sequence
   */
  @javax.annotation.Nullable
  public Integer getSequence() {
    return sequence;
  }

  public void setSequence(Integer sequence) {
    this.sequence = sequence;
  }


  public Job slug(String slug) {
    this.slug = slug;
    return this;
  }

  /**
   * Get slug
   * @return slug
   */
  @javax.annotation.Nullable
  public String getSlug() {
    return slug;
  }

  public void setSlug(String slug) {
    this.slug = slug;
  }


  public Job status(JobStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public JobStatus getStatus() {
    return status;
  }

  public void setStatus(JobStatus status) {
    this.status = status;
  }


  public Job tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public Job addTagsItem(String tagsItem) {
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


  public Job title(String title) {
    this.title = title;
    return this;
  }

  /**
   * The job title of the person.
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
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



  @Deprecated
  public Job url(String url) {
    this.url = url;
    return this;
  }

  /**
   * URL of the job description
   * @return url
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getUrl() {
    return url;
  }

  @Deprecated
  public void setUrl(String url) {
    this.url = url;
  }


  public Job visibility(VisibilityEnum visibility) {
    this.visibility = visibility;
    return this;
  }

  /**
   * The visibility of the job
   * @return visibility
   */
  @javax.annotation.Nullable
  public VisibilityEnum getVisibility() {
    return visibility;
  }

  public void setVisibility(VisibilityEnum visibility) {
    this.visibility = visibility;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Job job = (Job) o;
    return Objects.equals(this.addresses, job.addresses) &&
        Objects.equals(this.availableToEmployees, job.availableToEmployees) &&
        Objects.equals(this.blocks, job.blocks) &&
        Objects.equals(this.branch, job.branch) &&
        Objects.equals(this.closing, job.closing) &&
        Objects.equals(this.closingDate, job.closingDate) &&
        Objects.equals(this.closingHtml, job.closingHtml) &&
        Objects.equals(this.code, job.code) &&
        Objects.equals(this.confidential, job.confidential) &&
        Objects.equals(this.createdAt, job.createdAt) &&
        Objects.equals(this.createdBy, job.createdBy) &&
        Objects.equals(this.customFields, job.customFields) &&
        Objects.equals(this.customMappings, job.customMappings) &&
        Objects.equals(this.deleted, job.deleted) &&
        Objects.equals(this.department, job.department) &&
        Objects.equals(this.description, job.description) &&
        Objects.equals(this.descriptionHtml, job.descriptionHtml) &&
        Objects.equals(this.employmentTerms, job.employmentTerms) &&
        Objects.equals(this.experience, job.experience) &&
        Objects.equals(this.followers, job.followers) &&
        Objects.equals(this.hiringManagers, job.hiringManagers) &&
        Objects.equals(this.id, job.id) &&
        Objects.equals(this.jobPortalUrl, job.jobPortalUrl) &&
        Objects.equals(this.language, job.language) &&
        Objects.equals(this.links, job.links) &&
        Objects.equals(this.location, job.location) &&
        Objects.equals(this.ownerId, job.ownerId) &&
        Objects.equals(this.publishedAt, job.publishedAt) &&
        Objects.equals(this.recordUrl, job.recordUrl) &&
        Objects.equals(this.recruiters, job.recruiters) &&
        Objects.equals(this.remote, job.remote) &&
        Objects.equals(this.requisitionId, job.requisitionId) &&
        Objects.equals(this.salary, job.salary) &&
        Objects.equals(this.sequence, job.sequence) &&
        Objects.equals(this.slug, job.slug) &&
        Objects.equals(this.status, job.status) &&
        Objects.equals(this.tags, job.tags) &&
        Objects.equals(this.title, job.title) &&
        Objects.equals(this.updatedAt, job.updatedAt) &&
        Objects.equals(this.updatedBy, job.updatedBy) &&
        Objects.equals(this.url, job.url) &&
        Objects.equals(this.visibility, job.visibility);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(addresses, availableToEmployees, blocks, branch, closing, closingDate, closingHtml, code, confidential, createdAt, createdBy, customFields, customMappings, deleted, department, description, descriptionHtml, employmentTerms, experience, followers, hiringManagers, id, jobPortalUrl, language, links, location, ownerId, publishedAt, recordUrl, recruiters, remote, requisitionId, salary, sequence, slug, status, tags, title, updatedAt, updatedBy, url, visibility);
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
    sb.append("class Job {\n");
    sb.append("    addresses: ").append(toIndentedString(addresses)).append("\n");
    sb.append("    availableToEmployees: ").append(toIndentedString(availableToEmployees)).append("\n");
    sb.append("    blocks: ").append(toIndentedString(blocks)).append("\n");
    sb.append("    branch: ").append(toIndentedString(branch)).append("\n");
    sb.append("    closing: ").append(toIndentedString(closing)).append("\n");
    sb.append("    closingDate: ").append(toIndentedString(closingDate)).append("\n");
    sb.append("    closingHtml: ").append(toIndentedString(closingHtml)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    confidential: ").append(toIndentedString(confidential)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    department: ").append(toIndentedString(department)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    descriptionHtml: ").append(toIndentedString(descriptionHtml)).append("\n");
    sb.append("    employmentTerms: ").append(toIndentedString(employmentTerms)).append("\n");
    sb.append("    experience: ").append(toIndentedString(experience)).append("\n");
    sb.append("    followers: ").append(toIndentedString(followers)).append("\n");
    sb.append("    hiringManagers: ").append(toIndentedString(hiringManagers)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    jobPortalUrl: ").append(toIndentedString(jobPortalUrl)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    ownerId: ").append(toIndentedString(ownerId)).append("\n");
    sb.append("    publishedAt: ").append(toIndentedString(publishedAt)).append("\n");
    sb.append("    recordUrl: ").append(toIndentedString(recordUrl)).append("\n");
    sb.append("    recruiters: ").append(toIndentedString(recruiters)).append("\n");
    sb.append("    remote: ").append(toIndentedString(remote)).append("\n");
    sb.append("    requisitionId: ").append(toIndentedString(requisitionId)).append("\n");
    sb.append("    salary: ").append(toIndentedString(salary)).append("\n");
    sb.append("    sequence: ").append(toIndentedString(sequence)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    visibility: ").append(toIndentedString(visibility)).append("\n");
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
    openapiFields.add("addresses");
    openapiFields.add("available_to_employees");
    openapiFields.add("blocks");
    openapiFields.add("branch");
    openapiFields.add("closing");
    openapiFields.add("closing_date");
    openapiFields.add("closing_html");
    openapiFields.add("code");
    openapiFields.add("confidential");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("custom_fields");
    openapiFields.add("custom_mappings");
    openapiFields.add("deleted");
    openapiFields.add("department");
    openapiFields.add("description");
    openapiFields.add("description_html");
    openapiFields.add("employment_terms");
    openapiFields.add("experience");
    openapiFields.add("followers");
    openapiFields.add("hiring_managers");
    openapiFields.add("id");
    openapiFields.add("job_portal_url");
    openapiFields.add("language");
    openapiFields.add("links");
    openapiFields.add("location");
    openapiFields.add("owner_id");
    openapiFields.add("published_at");
    openapiFields.add("record_url");
    openapiFields.add("recruiters");
    openapiFields.add("remote");
    openapiFields.add("requisition_id");
    openapiFields.add("salary");
    openapiFields.add("sequence");
    openapiFields.add("slug");
    openapiFields.add("status");
    openapiFields.add("tags");
    openapiFields.add("title");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("url");
    openapiFields.add("visibility");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Job
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Job.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Job is not found in the empty JSON string", Job.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Job.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Job` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("addresses") != null && !jsonObj.get("addresses").isJsonNull()) {
        JsonArray jsonArrayaddresses = jsonObj.getAsJsonArray("addresses");
        if (jsonArrayaddresses != null) {
          // ensure the json data is an array
          if (!jsonObj.get("addresses").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `addresses` to be an array in the JSON string but got `%s`", jsonObj.get("addresses").toString()));
          }

          // validate the optional field `addresses` (array)
          for (int i = 0; i < jsonArrayaddresses.size(); i++) {
            Address.validateJsonElement(jsonArrayaddresses.get(i));
          };
        }
      }
      if (jsonObj.get("blocks") != null && !jsonObj.get("blocks").isJsonNull()) {
        JsonArray jsonArrayblocks = jsonObj.getAsJsonArray("blocks");
        if (jsonArrayblocks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("blocks").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `blocks` to be an array in the JSON string but got `%s`", jsonObj.get("blocks").toString()));
          }

          // validate the optional field `blocks` (array)
          for (int i = 0; i < jsonArrayblocks.size(); i++) {
            JobBlocksInner.validateJsonElement(jsonArrayblocks.get(i));
          };
        }
      }
      // validate the optional field `branch`
      if (jsonObj.get("branch") != null && !jsonObj.get("branch").isJsonNull()) {
        Branch.validateJsonElement(jsonObj.get("branch"));
      }
      if ((jsonObj.get("closing") != null && !jsonObj.get("closing").isJsonNull()) && !jsonObj.get("closing").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `closing` to be a primitive type in the JSON string but got `%s`", jsonObj.get("closing").toString()));
      }
      if ((jsonObj.get("closing_html") != null && !jsonObj.get("closing_html").isJsonNull()) && !jsonObj.get("closing_html").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `closing_html` to be a primitive type in the JSON string but got `%s`", jsonObj.get("closing_html").toString()));
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
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
      // validate the optional field `department`
      if (jsonObj.get("department") != null && !jsonObj.get("department").isJsonNull()) {
        Department.validateJsonElement(jsonObj.get("department"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("description_html") != null && !jsonObj.get("description_html").isJsonNull()) && !jsonObj.get("description_html").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description_html` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description_html").toString()));
      }
      if ((jsonObj.get("employment_terms") != null && !jsonObj.get("employment_terms").isJsonNull()) && !jsonObj.get("employment_terms").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employment_terms` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employment_terms").toString()));
      }
      // validate the optional field `employment_terms`
      if (jsonObj.get("employment_terms") != null && !jsonObj.get("employment_terms").isJsonNull()) {
        EmploymentTermsEnum.validateJsonElement(jsonObj.get("employment_terms"));
      }
      if ((jsonObj.get("experience") != null && !jsonObj.get("experience").isJsonNull()) && !jsonObj.get("experience").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `experience` to be a primitive type in the JSON string but got `%s`", jsonObj.get("experience").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("followers") != null && !jsonObj.get("followers").isJsonNull() && !jsonObj.get("followers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `followers` to be an array in the JSON string but got `%s`", jsonObj.get("followers").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("hiring_managers") != null && !jsonObj.get("hiring_managers").isJsonNull() && !jsonObj.get("hiring_managers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `hiring_managers` to be an array in the JSON string but got `%s`", jsonObj.get("hiring_managers").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("job_portal_url") != null && !jsonObj.get("job_portal_url").isJsonNull()) && !jsonObj.get("job_portal_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `job_portal_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("job_portal_url").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if (jsonObj.get("links") != null && !jsonObj.get("links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `links` to be an array in the JSON string but got `%s`", jsonObj.get("links").toString()));
          }

          // validate the optional field `links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            JobLinksInner.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if ((jsonObj.get("location") != null && !jsonObj.get("location").isJsonNull()) && !jsonObj.get("location").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location").toString()));
      }
      if ((jsonObj.get("owner_id") != null && !jsonObj.get("owner_id").isJsonNull()) && !jsonObj.get("owner_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner_id").toString()));
      }
      if ((jsonObj.get("record_url") != null && !jsonObj.get("record_url").isJsonNull()) && !jsonObj.get("record_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `record_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("record_url").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("recruiters") != null && !jsonObj.get("recruiters").isJsonNull() && !jsonObj.get("recruiters").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `recruiters` to be an array in the JSON string but got `%s`", jsonObj.get("recruiters").toString()));
      }
      if ((jsonObj.get("requisition_id") != null && !jsonObj.get("requisition_id").isJsonNull()) && !jsonObj.get("requisition_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requisition_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requisition_id").toString()));
      }
      // validate the optional field `salary`
      if (jsonObj.get("salary") != null && !jsonObj.get("salary").isJsonNull()) {
        JobSalary.validateJsonElement(jsonObj.get("salary"));
      }
      if ((jsonObj.get("slug") != null && !jsonObj.get("slug").isJsonNull()) && !jsonObj.get("slug").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be a primitive type in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        JobStatus.validateJsonElement(jsonObj.get("status"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
      if ((jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) && !jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
      if ((jsonObj.get("visibility") != null && !jsonObj.get("visibility").isJsonNull()) && !jsonObj.get("visibility").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `visibility` to be a primitive type in the JSON string but got `%s`", jsonObj.get("visibility").toString()));
      }
      // validate the optional field `visibility`
      if (jsonObj.get("visibility") != null && !jsonObj.get("visibility").isJsonNull()) {
        VisibilityEnum.validateJsonElement(jsonObj.get("visibility"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Job.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Job' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Job> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Job.class));

       return (TypeAdapter<T>) new TypeAdapter<Job>() {
           @Override
           public void write(JsonWriter out, Job value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Job read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Job given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Job
   * @throws IOException if the JSON string is invalid with respect to Job
   */
  public static Job fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Job.class);
  }

  /**
   * Convert an instance of Job to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

