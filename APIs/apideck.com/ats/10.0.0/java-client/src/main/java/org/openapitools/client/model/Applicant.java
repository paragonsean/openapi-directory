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
import org.openapitools.client.model.ApplicantSocialLinksInner;
import org.openapitools.client.model.ApplicantWebsitesInner;
import org.openapitools.client.model.CustomField;
import org.openapitools.client.model.Email;
import org.openapitools.client.model.PhoneNumber;
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
 * Applicant
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:53.902874-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Applicant {
  public static final String SERIALIZED_NAME_ADDRESSES = "addresses";
  @SerializedName(SERIALIZED_NAME_ADDRESSES)
  private List<Address> addresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_ANONYMIZED = "anonymized";
  @SerializedName(SERIALIZED_NAME_ANONYMIZED)
  private Boolean anonymized;

  public static final String SERIALIZED_NAME_APPLICATION_IDS = "application_ids";
  @SerializedName(SERIALIZED_NAME_APPLICATION_IDS)
  private List<String> applicationIds;

  public static final String SERIALIZED_NAME_APPLICATIONS = "applications";
  @SerializedName(SERIALIZED_NAME_APPLICATIONS)
  private List<String> applications;

  public static final String SERIALIZED_NAME_ARCHIVED = "archived";
  @SerializedName(SERIALIZED_NAME_ARCHIVED)
  private Boolean archived;

  public static final String SERIALIZED_NAME_BIRTHDAY = "birthday";
  @SerializedName(SERIALIZED_NAME_BIRTHDAY)
  private LocalDate birthday;

  public static final String SERIALIZED_NAME_CONFIDENTIAL = "confidential";
  @SerializedName(SERIALIZED_NAME_CONFIDENTIAL)
  private Boolean confidential;

  public static final String SERIALIZED_NAME_COORDINATOR_ID = "coordinator_id";
  @SerializedName(SERIALIZED_NAME_COORDINATOR_ID)
  private String coordinatorId;

  public static final String SERIALIZED_NAME_COVER_LETTER = "cover_letter";
  @SerializedName(SERIALIZED_NAME_COVER_LETTER)
  private String coverLetter;

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

  public static final String SERIALIZED_NAME_CV_URL = "cv_url";
  @SerializedName(SERIALIZED_NAME_CV_URL)
  private String cvUrl;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_DELETED_AT = "deleted_at";
  @SerializedName(SERIALIZED_NAME_DELETED_AT)
  private OffsetDateTime deletedAt;

  public static final String SERIALIZED_NAME_DELETED_BY = "deleted_by";
  @SerializedName(SERIALIZED_NAME_DELETED_BY)
  private String deletedBy;

  public static final String SERIALIZED_NAME_EMAILS = "emails";
  @SerializedName(SERIALIZED_NAME_EMAILS)
  private List<Email> emails = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_FOLLOWERS = "followers";
  @SerializedName(SERIALIZED_NAME_FOLLOWERS)
  private List<String> followers;

  public static final String SERIALIZED_NAME_HEADLINE = "headline";
  @SerializedName(SERIALIZED_NAME_HEADLINE)
  private String headline;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INITIALS = "initials";
  @SerializedName(SERIALIZED_NAME_INITIALS)
  private String initials;

  public static final String SERIALIZED_NAME_JOB_URL = "job_url";
  @SerializedName(SERIALIZED_NAME_JOB_URL)
  private String jobUrl;

  public static final String SERIALIZED_NAME_LAST_INTERACTION_AT = "last_interaction_at";
  @SerializedName(SERIALIZED_NAME_LAST_INTERACTION_AT)
  private OffsetDateTime lastInteractionAt;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_MIDDLE_NAME = "middle_name";
  @SerializedName(SERIALIZED_NAME_MIDDLE_NAME)
  private String middleName;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OWNER_ID = "owner_id";
  @SerializedName(SERIALIZED_NAME_OWNER_ID)
  private String ownerId;

  public static final String SERIALIZED_NAME_PHONE_NUMBERS = "phone_numbers";
  @SerializedName(SERIALIZED_NAME_PHONE_NUMBERS)
  private List<PhoneNumber> phoneNumbers = new ArrayList<>();

  public static final String SERIALIZED_NAME_PHOTO_URL = "photo_url";
  @SerializedName(SERIALIZED_NAME_PHOTO_URL)
  private String photoUrl;

  public static final String SERIALIZED_NAME_POSITION_ID = "position_id";
  @SerializedName(SERIALIZED_NAME_POSITION_ID)
  private String positionId;

  public static final String SERIALIZED_NAME_RECORD_URL = "record_url";
  @SerializedName(SERIALIZED_NAME_RECORD_URL)
  private String recordUrl;

  public static final String SERIALIZED_NAME_RECRUITER_ID = "recruiter_id";
  @SerializedName(SERIALIZED_NAME_RECRUITER_ID)
  private String recruiterId;

  public static final String SERIALIZED_NAME_REJECTED_AT = "rejected_at";
  @SerializedName(SERIALIZED_NAME_REJECTED_AT)
  private OffsetDateTime rejectedAt;

  public static final String SERIALIZED_NAME_SOCIAL_LINKS = "social_links";
  @SerializedName(SERIALIZED_NAME_SOCIAL_LINKS)
  private List<ApplicantSocialLinksInner> socialLinks = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOURCE_ID = "source_id";
  @SerializedName(SERIALIZED_NAME_SOURCE_ID)
  private String sourceId;

  public static final String SERIALIZED_NAME_SOURCED_BY = "sourced_by";
  @SerializedName(SERIALIZED_NAME_SOURCED_BY)
  private String sourcedBy;

  public static final String SERIALIZED_NAME_SOURCES = "sources";
  @SerializedName(SERIALIZED_NAME_SOURCES)
  private List<String> sources;

  public static final String SERIALIZED_NAME_STAGE_ID = "stage_id";
  @SerializedName(SERIALIZED_NAME_STAGE_ID)
  private String stageId;

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

  public static final String SERIALIZED_NAME_WEBSITES = "websites";
  @SerializedName(SERIALIZED_NAME_WEBSITES)
  private List<ApplicantWebsitesInner> websites = new ArrayList<>();

  public Applicant() {
  }

  public Applicant(
     OffsetDateTime createdAt, 
     String createdBy, 
     String cvUrl, 
     OffsetDateTime deletedAt, 
     String deletedBy, 
     String id, 
     String jobUrl, 
     OffsetDateTime lastInteractionAt, 
     OffsetDateTime rejectedAt, 
     String sourceId, 
     String sourcedBy, 
     OffsetDateTime updatedAt, 
     String updatedBy
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.cvUrl = cvUrl;
    this.deletedAt = deletedAt;
    this.deletedBy = deletedBy;
    this.id = id;
    this.jobUrl = jobUrl;
    this.lastInteractionAt = lastInteractionAt;
    this.rejectedAt = rejectedAt;
    this.sourceId = sourceId;
    this.sourcedBy = sourcedBy;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
  }

  public Applicant addresses(List<Address> addresses) {
    this.addresses = addresses;
    return this;
  }

  public Applicant addAddressesItem(Address addressesItem) {
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


  public Applicant anonymized(Boolean anonymized) {
    this.anonymized = anonymized;
    return this;
  }

  /**
   * Get anonymized
   * @return anonymized
   */
  @javax.annotation.Nullable
  public Boolean getAnonymized() {
    return anonymized;
  }

  public void setAnonymized(Boolean anonymized) {
    this.anonymized = anonymized;
  }


  public Applicant applicationIds(List<String> applicationIds) {
    this.applicationIds = applicationIds;
    return this;
  }

  public Applicant addApplicationIdsItem(String applicationIdsItem) {
    if (this.applicationIds == null) {
      this.applicationIds = new ArrayList<>();
    }
    this.applicationIds.add(applicationIdsItem);
    return this;
  }

  /**
   * Get applicationIds
   * @return applicationIds
   */
  @javax.annotation.Nullable
  public List<String> getApplicationIds() {
    return applicationIds;
  }

  public void setApplicationIds(List<String> applicationIds) {
    this.applicationIds = applicationIds;
  }


  public Applicant applications(List<String> applications) {
    this.applications = applications;
    return this;
  }

  public Applicant addApplicationsItem(String applicationsItem) {
    if (this.applications == null) {
      this.applications = new ArrayList<>();
    }
    this.applications.add(applicationsItem);
    return this;
  }

  /**
   * Get applications
   * @return applications
   */
  @javax.annotation.Nullable
  public List<String> getApplications() {
    return applications;
  }

  public void setApplications(List<String> applications) {
    this.applications = applications;
  }


  public Applicant archived(Boolean archived) {
    this.archived = archived;
    return this;
  }

  /**
   * Get archived
   * @return archived
   */
  @javax.annotation.Nullable
  public Boolean getArchived() {
    return archived;
  }

  public void setArchived(Boolean archived) {
    this.archived = archived;
  }


  public Applicant birthday(LocalDate birthday) {
    this.birthday = birthday;
    return this;
  }

  /**
   * The date of birth of the person.
   * @return birthday
   */
  @javax.annotation.Nullable
  public LocalDate getBirthday() {
    return birthday;
  }

  public void setBirthday(LocalDate birthday) {
    this.birthday = birthday;
  }


  public Applicant confidential(Boolean confidential) {
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


  public Applicant coordinatorId(String coordinatorId) {
    this.coordinatorId = coordinatorId;
    return this;
  }

  /**
   * Get coordinatorId
   * @return coordinatorId
   */
  @javax.annotation.Nullable
  public String getCoordinatorId() {
    return coordinatorId;
  }

  public void setCoordinatorId(String coordinatorId) {
    this.coordinatorId = coordinatorId;
  }


  public Applicant coverLetter(String coverLetter) {
    this.coverLetter = coverLetter;
    return this;
  }

  /**
   * Get coverLetter
   * @return coverLetter
   */
  @javax.annotation.Nullable
  public String getCoverLetter() {
    return coverLetter;
  }

  public void setCoverLetter(String coverLetter) {
    this.coverLetter = coverLetter;
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



  public Applicant customFields(List<CustomField> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Applicant addCustomFieldsItem(CustomField customFieldsItem) {
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


  public Applicant customMappings(Object customMappings) {
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


  /**
   * Get cvUrl
   * @return cvUrl
   */
  @javax.annotation.Nullable
  public String getCvUrl() {
    return cvUrl;
  }



  public Applicant deleted(Boolean deleted) {
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


  /**
   * The time at which the object was deleted.
   * @return deletedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDeletedAt() {
    return deletedAt;
  }



  /**
   * The user who deleted the object.
   * @return deletedBy
   */
  @javax.annotation.Nullable
  public String getDeletedBy() {
    return deletedBy;
  }



  public Applicant emails(List<Email> emails) {
    this.emails = emails;
    return this;
  }

  public Applicant addEmailsItem(Email emailsItem) {
    if (this.emails == null) {
      this.emails = new ArrayList<>();
    }
    this.emails.add(emailsItem);
    return this;
  }

  /**
   * Get emails
   * @return emails
   */
  @javax.annotation.Nullable
  public List<Email> getEmails() {
    return emails;
  }

  public void setEmails(List<Email> emails) {
    this.emails = emails;
  }


  public Applicant firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * The first name of the person.
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public Applicant followers(List<String> followers) {
    this.followers = followers;
    return this;
  }

  public Applicant addFollowersItem(String followersItem) {
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


  public Applicant headline(String headline) {
    this.headline = headline;
    return this;
  }

  /**
   * Typically a list of previous companies where the contact has worked or schools that the contact has attended
   * @return headline
   */
  @javax.annotation.Nullable
  public String getHeadline() {
    return headline;
  }

  public void setHeadline(String headline) {
    this.headline = headline;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Applicant initials(String initials) {
    this.initials = initials;
    return this;
  }

  /**
   * The initials of the person, usually derived from their first, middle, and last names.
   * @return initials
   */
  @javax.annotation.Nullable
  public String getInitials() {
    return initials;
  }

  public void setInitials(String initials) {
    this.initials = initials;
  }


  /**
   * Get jobUrl
   * @return jobUrl
   */
  @javax.annotation.Nullable
  public String getJobUrl() {
    return jobUrl;
  }



  /**
   * Get lastInteractionAt
   * @return lastInteractionAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastInteractionAt() {
    return lastInteractionAt;
  }



  public Applicant lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * The last name of the person.
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public Applicant middleName(String middleName) {
    this.middleName = middleName;
    return this;
  }

  /**
   * Middle name of the person.
   * @return middleName
   */
  @javax.annotation.Nullable
  public String getMiddleName() {
    return middleName;
  }

  public void setMiddleName(String middleName) {
    this.middleName = middleName;
  }


  public Applicant name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of an applicant.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Applicant ownerId(String ownerId) {
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


  public Applicant phoneNumbers(List<PhoneNumber> phoneNumbers) {
    this.phoneNumbers = phoneNumbers;
    return this;
  }

  public Applicant addPhoneNumbersItem(PhoneNumber phoneNumbersItem) {
    if (this.phoneNumbers == null) {
      this.phoneNumbers = new ArrayList<>();
    }
    this.phoneNumbers.add(phoneNumbersItem);
    return this;
  }

  /**
   * Get phoneNumbers
   * @return phoneNumbers
   */
  @javax.annotation.Nullable
  public List<PhoneNumber> getPhoneNumbers() {
    return phoneNumbers;
  }

  public void setPhoneNumbers(List<PhoneNumber> phoneNumbers) {
    this.phoneNumbers = phoneNumbers;
  }


  public Applicant photoUrl(String photoUrl) {
    this.photoUrl = photoUrl;
    return this;
  }

  /**
   * The URL of the photo of a person.
   * @return photoUrl
   */
  @javax.annotation.Nullable
  public String getPhotoUrl() {
    return photoUrl;
  }

  public void setPhotoUrl(String photoUrl) {
    this.photoUrl = photoUrl;
  }


  public Applicant positionId(String positionId) {
    this.positionId = positionId;
    return this;
  }

  /**
   * The PositionId the applicant applied for.
   * @return positionId
   */
  @javax.annotation.Nullable
  public String getPositionId() {
    return positionId;
  }

  public void setPositionId(String positionId) {
    this.positionId = positionId;
  }


  public Applicant recordUrl(String recordUrl) {
    this.recordUrl = recordUrl;
    return this;
  }

  /**
   * Get recordUrl
   * @return recordUrl
   */
  @javax.annotation.Nullable
  public String getRecordUrl() {
    return recordUrl;
  }

  public void setRecordUrl(String recordUrl) {
    this.recordUrl = recordUrl;
  }


  public Applicant recruiterId(String recruiterId) {
    this.recruiterId = recruiterId;
    return this;
  }

  /**
   * Get recruiterId
   * @return recruiterId
   */
  @javax.annotation.Nullable
  public String getRecruiterId() {
    return recruiterId;
  }

  public void setRecruiterId(String recruiterId) {
    this.recruiterId = recruiterId;
  }


  /**
   * Get rejectedAt
   * @return rejectedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getRejectedAt() {
    return rejectedAt;
  }



  public Applicant socialLinks(List<ApplicantSocialLinksInner> socialLinks) {
    this.socialLinks = socialLinks;
    return this;
  }

  public Applicant addSocialLinksItem(ApplicantSocialLinksInner socialLinksItem) {
    if (this.socialLinks == null) {
      this.socialLinks = new ArrayList<>();
    }
    this.socialLinks.add(socialLinksItem);
    return this;
  }

  /**
   * Get socialLinks
   * @return socialLinks
   */
  @javax.annotation.Nullable
  public List<ApplicantSocialLinksInner> getSocialLinks() {
    return socialLinks;
  }

  public void setSocialLinks(List<ApplicantSocialLinksInner> socialLinks) {
    this.socialLinks = socialLinks;
  }


  /**
   * Get sourceId
   * @return sourceId
   */
  @javax.annotation.Nullable
  public String getSourceId() {
    return sourceId;
  }



  /**
   * Get sourcedBy
   * @return sourcedBy
   */
  @javax.annotation.Nullable
  public String getSourcedBy() {
    return sourcedBy;
  }



  public Applicant sources(List<String> sources) {
    this.sources = sources;
    return this;
  }

  public Applicant addSourcesItem(String sourcesItem) {
    if (this.sources == null) {
      this.sources = new ArrayList<>();
    }
    this.sources.add(sourcesItem);
    return this;
  }

  /**
   * Get sources
   * @return sources
   */
  @javax.annotation.Nullable
  public List<String> getSources() {
    return sources;
  }

  public void setSources(List<String> sources) {
    this.sources = sources;
  }


  public Applicant stageId(String stageId) {
    this.stageId = stageId;
    return this;
  }

  /**
   * Get stageId
   * @return stageId
   */
  @javax.annotation.Nullable
  public String getStageId() {
    return stageId;
  }

  public void setStageId(String stageId) {
    this.stageId = stageId;
  }


  public Applicant tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public Applicant addTagsItem(String tagsItem) {
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


  public Applicant title(String title) {
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



  public Applicant websites(List<ApplicantWebsitesInner> websites) {
    this.websites = websites;
    return this;
  }

  public Applicant addWebsitesItem(ApplicantWebsitesInner websitesItem) {
    if (this.websites == null) {
      this.websites = new ArrayList<>();
    }
    this.websites.add(websitesItem);
    return this;
  }

  /**
   * Get websites
   * @return websites
   */
  @javax.annotation.Nullable
  public List<ApplicantWebsitesInner> getWebsites() {
    return websites;
  }

  public void setWebsites(List<ApplicantWebsitesInner> websites) {
    this.websites = websites;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Applicant applicant = (Applicant) o;
    return Objects.equals(this.addresses, applicant.addresses) &&
        Objects.equals(this.anonymized, applicant.anonymized) &&
        Objects.equals(this.applicationIds, applicant.applicationIds) &&
        Objects.equals(this.applications, applicant.applications) &&
        Objects.equals(this.archived, applicant.archived) &&
        Objects.equals(this.birthday, applicant.birthday) &&
        Objects.equals(this.confidential, applicant.confidential) &&
        Objects.equals(this.coordinatorId, applicant.coordinatorId) &&
        Objects.equals(this.coverLetter, applicant.coverLetter) &&
        Objects.equals(this.createdAt, applicant.createdAt) &&
        Objects.equals(this.createdBy, applicant.createdBy) &&
        Objects.equals(this.customFields, applicant.customFields) &&
        Objects.equals(this.customMappings, applicant.customMappings) &&
        Objects.equals(this.cvUrl, applicant.cvUrl) &&
        Objects.equals(this.deleted, applicant.deleted) &&
        Objects.equals(this.deletedAt, applicant.deletedAt) &&
        Objects.equals(this.deletedBy, applicant.deletedBy) &&
        Objects.equals(this.emails, applicant.emails) &&
        Objects.equals(this.firstName, applicant.firstName) &&
        Objects.equals(this.followers, applicant.followers) &&
        Objects.equals(this.headline, applicant.headline) &&
        Objects.equals(this.id, applicant.id) &&
        Objects.equals(this.initials, applicant.initials) &&
        Objects.equals(this.jobUrl, applicant.jobUrl) &&
        Objects.equals(this.lastInteractionAt, applicant.lastInteractionAt) &&
        Objects.equals(this.lastName, applicant.lastName) &&
        Objects.equals(this.middleName, applicant.middleName) &&
        Objects.equals(this.name, applicant.name) &&
        Objects.equals(this.ownerId, applicant.ownerId) &&
        Objects.equals(this.phoneNumbers, applicant.phoneNumbers) &&
        Objects.equals(this.photoUrl, applicant.photoUrl) &&
        Objects.equals(this.positionId, applicant.positionId) &&
        Objects.equals(this.recordUrl, applicant.recordUrl) &&
        Objects.equals(this.recruiterId, applicant.recruiterId) &&
        Objects.equals(this.rejectedAt, applicant.rejectedAt) &&
        Objects.equals(this.socialLinks, applicant.socialLinks) &&
        Objects.equals(this.sourceId, applicant.sourceId) &&
        Objects.equals(this.sourcedBy, applicant.sourcedBy) &&
        Objects.equals(this.sources, applicant.sources) &&
        Objects.equals(this.stageId, applicant.stageId) &&
        Objects.equals(this.tags, applicant.tags) &&
        Objects.equals(this.title, applicant.title) &&
        Objects.equals(this.updatedAt, applicant.updatedAt) &&
        Objects.equals(this.updatedBy, applicant.updatedBy) &&
        Objects.equals(this.websites, applicant.websites);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(addresses, anonymized, applicationIds, applications, archived, birthday, confidential, coordinatorId, coverLetter, createdAt, createdBy, customFields, customMappings, cvUrl, deleted, deletedAt, deletedBy, emails, firstName, followers, headline, id, initials, jobUrl, lastInteractionAt, lastName, middleName, name, ownerId, phoneNumbers, photoUrl, positionId, recordUrl, recruiterId, rejectedAt, socialLinks, sourceId, sourcedBy, sources, stageId, tags, title, updatedAt, updatedBy, websites);
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
    sb.append("class Applicant {\n");
    sb.append("    addresses: ").append(toIndentedString(addresses)).append("\n");
    sb.append("    anonymized: ").append(toIndentedString(anonymized)).append("\n");
    sb.append("    applicationIds: ").append(toIndentedString(applicationIds)).append("\n");
    sb.append("    applications: ").append(toIndentedString(applications)).append("\n");
    sb.append("    archived: ").append(toIndentedString(archived)).append("\n");
    sb.append("    birthday: ").append(toIndentedString(birthday)).append("\n");
    sb.append("    confidential: ").append(toIndentedString(confidential)).append("\n");
    sb.append("    coordinatorId: ").append(toIndentedString(coordinatorId)).append("\n");
    sb.append("    coverLetter: ").append(toIndentedString(coverLetter)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    cvUrl: ").append(toIndentedString(cvUrl)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    deletedAt: ").append(toIndentedString(deletedAt)).append("\n");
    sb.append("    deletedBy: ").append(toIndentedString(deletedBy)).append("\n");
    sb.append("    emails: ").append(toIndentedString(emails)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    followers: ").append(toIndentedString(followers)).append("\n");
    sb.append("    headline: ").append(toIndentedString(headline)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    initials: ").append(toIndentedString(initials)).append("\n");
    sb.append("    jobUrl: ").append(toIndentedString(jobUrl)).append("\n");
    sb.append("    lastInteractionAt: ").append(toIndentedString(lastInteractionAt)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    middleName: ").append(toIndentedString(middleName)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ownerId: ").append(toIndentedString(ownerId)).append("\n");
    sb.append("    phoneNumbers: ").append(toIndentedString(phoneNumbers)).append("\n");
    sb.append("    photoUrl: ").append(toIndentedString(photoUrl)).append("\n");
    sb.append("    positionId: ").append(toIndentedString(positionId)).append("\n");
    sb.append("    recordUrl: ").append(toIndentedString(recordUrl)).append("\n");
    sb.append("    recruiterId: ").append(toIndentedString(recruiterId)).append("\n");
    sb.append("    rejectedAt: ").append(toIndentedString(rejectedAt)).append("\n");
    sb.append("    socialLinks: ").append(toIndentedString(socialLinks)).append("\n");
    sb.append("    sourceId: ").append(toIndentedString(sourceId)).append("\n");
    sb.append("    sourcedBy: ").append(toIndentedString(sourcedBy)).append("\n");
    sb.append("    sources: ").append(toIndentedString(sources)).append("\n");
    sb.append("    stageId: ").append(toIndentedString(stageId)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    websites: ").append(toIndentedString(websites)).append("\n");
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
    openapiFields.add("anonymized");
    openapiFields.add("application_ids");
    openapiFields.add("applications");
    openapiFields.add("archived");
    openapiFields.add("birthday");
    openapiFields.add("confidential");
    openapiFields.add("coordinator_id");
    openapiFields.add("cover_letter");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("custom_fields");
    openapiFields.add("custom_mappings");
    openapiFields.add("cv_url");
    openapiFields.add("deleted");
    openapiFields.add("deleted_at");
    openapiFields.add("deleted_by");
    openapiFields.add("emails");
    openapiFields.add("first_name");
    openapiFields.add("followers");
    openapiFields.add("headline");
    openapiFields.add("id");
    openapiFields.add("initials");
    openapiFields.add("job_url");
    openapiFields.add("last_interaction_at");
    openapiFields.add("last_name");
    openapiFields.add("middle_name");
    openapiFields.add("name");
    openapiFields.add("owner_id");
    openapiFields.add("phone_numbers");
    openapiFields.add("photo_url");
    openapiFields.add("position_id");
    openapiFields.add("record_url");
    openapiFields.add("recruiter_id");
    openapiFields.add("rejected_at");
    openapiFields.add("social_links");
    openapiFields.add("source_id");
    openapiFields.add("sourced_by");
    openapiFields.add("sources");
    openapiFields.add("stage_id");
    openapiFields.add("tags");
    openapiFields.add("title");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("websites");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Applicant
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Applicant.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Applicant is not found in the empty JSON string", Applicant.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Applicant.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Applicant` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      // ensure the optional json data is an array if present
      if (jsonObj.get("application_ids") != null && !jsonObj.get("application_ids").isJsonNull() && !jsonObj.get("application_ids").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `application_ids` to be an array in the JSON string but got `%s`", jsonObj.get("application_ids").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("applications") != null && !jsonObj.get("applications").isJsonNull() && !jsonObj.get("applications").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `applications` to be an array in the JSON string but got `%s`", jsonObj.get("applications").toString()));
      }
      if ((jsonObj.get("coordinator_id") != null && !jsonObj.get("coordinator_id").isJsonNull()) && !jsonObj.get("coordinator_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `coordinator_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("coordinator_id").toString()));
      }
      if ((jsonObj.get("cover_letter") != null && !jsonObj.get("cover_letter").isJsonNull()) && !jsonObj.get("cover_letter").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cover_letter` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cover_letter").toString()));
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
      if ((jsonObj.get("cv_url") != null && !jsonObj.get("cv_url").isJsonNull()) && !jsonObj.get("cv_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cv_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cv_url").toString()));
      }
      if ((jsonObj.get("deleted_by") != null && !jsonObj.get("deleted_by").isJsonNull()) && !jsonObj.get("deleted_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted_by").toString()));
      }
      if (jsonObj.get("emails") != null && !jsonObj.get("emails").isJsonNull()) {
        JsonArray jsonArrayemails = jsonObj.getAsJsonArray("emails");
        if (jsonArrayemails != null) {
          // ensure the json data is an array
          if (!jsonObj.get("emails").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `emails` to be an array in the JSON string but got `%s`", jsonObj.get("emails").toString()));
          }

          // validate the optional field `emails` (array)
          for (int i = 0; i < jsonArrayemails.size(); i++) {
            Email.validateJsonElement(jsonArrayemails.get(i));
          };
        }
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("followers") != null && !jsonObj.get("followers").isJsonNull() && !jsonObj.get("followers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `followers` to be an array in the JSON string but got `%s`", jsonObj.get("followers").toString()));
      }
      if ((jsonObj.get("headline") != null && !jsonObj.get("headline").isJsonNull()) && !jsonObj.get("headline").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `headline` to be a primitive type in the JSON string but got `%s`", jsonObj.get("headline").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("initials") != null && !jsonObj.get("initials").isJsonNull()) && !jsonObj.get("initials").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `initials` to be a primitive type in the JSON string but got `%s`", jsonObj.get("initials").toString()));
      }
      if ((jsonObj.get("job_url") != null && !jsonObj.get("job_url").isJsonNull()) && !jsonObj.get("job_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `job_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("job_url").toString()));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("middle_name") != null && !jsonObj.get("middle_name").isJsonNull()) && !jsonObj.get("middle_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `middle_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("middle_name").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("owner_id") != null && !jsonObj.get("owner_id").isJsonNull()) && !jsonObj.get("owner_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner_id").toString()));
      }
      if (jsonObj.get("phone_numbers") != null && !jsonObj.get("phone_numbers").isJsonNull()) {
        JsonArray jsonArrayphoneNumbers = jsonObj.getAsJsonArray("phone_numbers");
        if (jsonArrayphoneNumbers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("phone_numbers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `phone_numbers` to be an array in the JSON string but got `%s`", jsonObj.get("phone_numbers").toString()));
          }

          // validate the optional field `phone_numbers` (array)
          for (int i = 0; i < jsonArrayphoneNumbers.size(); i++) {
            PhoneNumber.validateJsonElement(jsonArrayphoneNumbers.get(i));
          };
        }
      }
      if ((jsonObj.get("photo_url") != null && !jsonObj.get("photo_url").isJsonNull()) && !jsonObj.get("photo_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `photo_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("photo_url").toString()));
      }
      if ((jsonObj.get("position_id") != null && !jsonObj.get("position_id").isJsonNull()) && !jsonObj.get("position_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `position_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("position_id").toString()));
      }
      if ((jsonObj.get("record_url") != null && !jsonObj.get("record_url").isJsonNull()) && !jsonObj.get("record_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `record_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("record_url").toString()));
      }
      if ((jsonObj.get("recruiter_id") != null && !jsonObj.get("recruiter_id").isJsonNull()) && !jsonObj.get("recruiter_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `recruiter_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("recruiter_id").toString()));
      }
      if (jsonObj.get("social_links") != null && !jsonObj.get("social_links").isJsonNull()) {
        JsonArray jsonArraysocialLinks = jsonObj.getAsJsonArray("social_links");
        if (jsonArraysocialLinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("social_links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `social_links` to be an array in the JSON string but got `%s`", jsonObj.get("social_links").toString()));
          }

          // validate the optional field `social_links` (array)
          for (int i = 0; i < jsonArraysocialLinks.size(); i++) {
            ApplicantSocialLinksInner.validateJsonElement(jsonArraysocialLinks.get(i));
          };
        }
      }
      if ((jsonObj.get("source_id") != null && !jsonObj.get("source_id").isJsonNull()) && !jsonObj.get("source_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_id").toString()));
      }
      if ((jsonObj.get("sourced_by") != null && !jsonObj.get("sourced_by").isJsonNull()) && !jsonObj.get("sourced_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourced_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourced_by").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("sources") != null && !jsonObj.get("sources").isJsonNull() && !jsonObj.get("sources").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `sources` to be an array in the JSON string but got `%s`", jsonObj.get("sources").toString()));
      }
      if ((jsonObj.get("stage_id") != null && !jsonObj.get("stage_id").isJsonNull()) && !jsonObj.get("stage_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `stage_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("stage_id").toString()));
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
      if (jsonObj.get("websites") != null && !jsonObj.get("websites").isJsonNull()) {
        JsonArray jsonArraywebsites = jsonObj.getAsJsonArray("websites");
        if (jsonArraywebsites != null) {
          // ensure the json data is an array
          if (!jsonObj.get("websites").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `websites` to be an array in the JSON string but got `%s`", jsonObj.get("websites").toString()));
          }

          // validate the optional field `websites` (array)
          for (int i = 0; i < jsonArraywebsites.size(); i++) {
            ApplicantWebsitesInner.validateJsonElement(jsonArraywebsites.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Applicant.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Applicant' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Applicant> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Applicant.class));

       return (TypeAdapter<T>) new TypeAdapter<Applicant>() {
           @Override
           public void write(JsonWriter out, Applicant value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Applicant read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Applicant given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Applicant
   * @throws IOException if the JSON string is invalid with respect to Applicant
   */
  public static Applicant fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Applicant.class);
  }

  /**
   * Convert an instance of Applicant to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

