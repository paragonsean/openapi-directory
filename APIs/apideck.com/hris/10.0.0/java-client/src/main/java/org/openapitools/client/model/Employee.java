/*
 * HRIS API
 * Welcome to the HRIS API.  You can use this API to access all HRIS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import org.openapitools.client.model.BankAccount;
import org.openapitools.client.model.CustomField;
import org.openapitools.client.model.Email;
import org.openapitools.client.model.EmployeeCompensation;
import org.openapitools.client.model.EmployeeEmploymentRole;
import org.openapitools.client.model.EmployeeJob;
import org.openapitools.client.model.EmployeeManager;
import org.openapitools.client.model.EmploymentStatus;
import org.openapitools.client.model.Gender;
import org.openapitools.client.model.Person;
import org.openapitools.client.model.PhoneNumber;
import org.openapitools.client.model.ProbationPeriod;
import org.openapitools.client.model.SocialLink;
import org.openapitools.client.model.Team;
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
 * Employee
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:31.431787-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Employee {
  public static final String SERIALIZED_NAME_ADDRESSES = "addresses";
  @SerializedName(SERIALIZED_NAME_ADDRESSES)
  private List<Address> addresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_BANK_ACCOUNTS = "bank_accounts";
  @SerializedName(SERIALIZED_NAME_BANK_ACCOUNTS)
  private List<BankAccount> bankAccounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_BIRTHDAY = "birthday";
  @SerializedName(SERIALIZED_NAME_BIRTHDAY)
  private LocalDate birthday;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private String companyId;

  public static final String SERIALIZED_NAME_COMPANY_NAME = "company_name";
  @SerializedName(SERIALIZED_NAME_COMPANY_NAME)
  private String companyName;

  public static final String SERIALIZED_NAME_COMPENSATIONS = "compensations";
  @SerializedName(SERIALIZED_NAME_COMPENSATIONS)
  private List<EmployeeCompensation> compensations;

  public static final String SERIALIZED_NAME_COUNTRY_OF_BIRTH = "country_of_birth";
  @SerializedName(SERIALIZED_NAME_COUNTRY_OF_BIRTH)
  private String countryOfBirth;

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

  public static final String SERIALIZED_NAME_DECEASED_ON = "deceased_on";
  @SerializedName(SERIALIZED_NAME_DECEASED_ON)
  private LocalDate deceasedOn;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_DEPARTMENT = "department";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_DEPARTMENT)
  private String department;

  public static final String SERIALIZED_NAME_DEPARTMENT_ID = "department_id";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT_ID)
  private String departmentId;

  public static final String SERIALIZED_NAME_DEPARTMENT_NAME = "department_name";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT_NAME)
  private String departmentName;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DIETARY_PREFERENCE = "dietary_preference";
  @SerializedName(SERIALIZED_NAME_DIETARY_PREFERENCE)
  private String dietaryPreference;

  public static final String SERIALIZED_NAME_DIRECT_REPORTS = "direct_reports";
  @SerializedName(SERIALIZED_NAME_DIRECT_REPORTS)
  private List<String> directReports;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "display_name";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_DIVISION = "division";
  @SerializedName(SERIALIZED_NAME_DIVISION)
  private String division;

  public static final String SERIALIZED_NAME_DIVISION_ID = "division_id";
  @SerializedName(SERIALIZED_NAME_DIVISION_ID)
  private String divisionId;

  public static final String SERIALIZED_NAME_EMAILS = "emails";
  @SerializedName(SERIALIZED_NAME_EMAILS)
  private List<Email> emails = new ArrayList<>();

  public static final String SERIALIZED_NAME_EMPLOYEE_NUMBER = "employee_number";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE_NUMBER)
  private String employeeNumber;

  public static final String SERIALIZED_NAME_EMPLOYMENT_END_DATE = "employment_end_date";
  @SerializedName(SERIALIZED_NAME_EMPLOYMENT_END_DATE)
  private String employmentEndDate;

  public static final String SERIALIZED_NAME_EMPLOYMENT_ROLE = "employment_role";
  @SerializedName(SERIALIZED_NAME_EMPLOYMENT_ROLE)
  private EmployeeEmploymentRole employmentRole;

  public static final String SERIALIZED_NAME_EMPLOYMENT_START_DATE = "employment_start_date";
  @SerializedName(SERIALIZED_NAME_EMPLOYMENT_START_DATE)
  private String employmentStartDate;

  public static final String SERIALIZED_NAME_EMPLOYMENT_STATUS = "employment_status";
  @SerializedName(SERIALIZED_NAME_EMPLOYMENT_STATUS)
  private EmploymentStatus employmentStatus;

  public static final String SERIALIZED_NAME_ETHNICITY = "ethnicity";
  @SerializedName(SERIALIZED_NAME_ETHNICITY)
  private String ethnicity;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_FOOD_ALLERGIES = "food_allergies";
  @SerializedName(SERIALIZED_NAME_FOOD_ALLERGIES)
  private List<String> foodAllergies;

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private Gender gender;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INITIALS = "initials";
  @SerializedName(SERIALIZED_NAME_INITIALS)
  private String initials;

  public static final String SERIALIZED_NAME_JOBS = "jobs";
  @SerializedName(SERIALIZED_NAME_JOBS)
  private List<EmployeeJob> jobs;

  public static final String SERIALIZED_NAME_LANGUAGES = "languages";
  @SerializedName(SERIALIZED_NAME_LANGUAGES)
  private List<String> languages = new ArrayList<>();

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  /**
   * The reason because the employment ended.
   */
  @JsonAdapter(LeavingReasonEnum.Adapter.class)
  public enum LeavingReasonEnum {
    DISMISSED("dismissed"),
    
    RESIGNED("resigned"),
    
    REDUNDANCY("redundancy"),
    
    OTHER("other");

    private String value;

    LeavingReasonEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static LeavingReasonEnum fromValue(String value) {
      for (LeavingReasonEnum b : LeavingReasonEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<LeavingReasonEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final LeavingReasonEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public LeavingReasonEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return LeavingReasonEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      LeavingReasonEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_LEAVING_REASON = "leaving_reason";
  @SerializedName(SERIALIZED_NAME_LEAVING_REASON)
  private LeavingReasonEnum leavingReason;

  public static final String SERIALIZED_NAME_MANAGER = "manager";
  @SerializedName(SERIALIZED_NAME_MANAGER)
  private EmployeeManager manager;

  public static final String SERIALIZED_NAME_MARITAL_STATUS = "marital_status";
  @SerializedName(SERIALIZED_NAME_MARITAL_STATUS)
  private String maritalStatus;

  public static final String SERIALIZED_NAME_MIDDLE_NAME = "middle_name";
  @SerializedName(SERIALIZED_NAME_MIDDLE_NAME)
  private String middleName;

  public static final String SERIALIZED_NAME_NATIONALITIES = "nationalities";
  @SerializedName(SERIALIZED_NAME_NATIONALITIES)
  private List<String> nationalities = new ArrayList<>();

  public static final String SERIALIZED_NAME_PARTNER = "partner";
  @SerializedName(SERIALIZED_NAME_PARTNER)
  private Person partner;

  public static final String SERIALIZED_NAME_PHONE_NUMBERS = "phone_numbers";
  @SerializedName(SERIALIZED_NAME_PHONE_NUMBERS)
  private List<PhoneNumber> phoneNumbers = new ArrayList<>();

  public static final String SERIALIZED_NAME_PHOTO_URL = "photo_url";
  @SerializedName(SERIALIZED_NAME_PHOTO_URL)
  private String photoUrl;

  public static final String SERIALIZED_NAME_PREFERRED_LANGUAGE = "preferred_language";
  @SerializedName(SERIALIZED_NAME_PREFERRED_LANGUAGE)
  private String preferredLanguage;

  public static final String SERIALIZED_NAME_PREFERRED_NAME = "preferred_name";
  @SerializedName(SERIALIZED_NAME_PREFERRED_NAME)
  private String preferredName;

  public static final String SERIALIZED_NAME_PROBATION_PERIOD = "probation_period";
  @SerializedName(SERIALIZED_NAME_PROBATION_PERIOD)
  private ProbationPeriod probationPeriod;

  public static final String SERIALIZED_NAME_PRONOUNS = "pronouns";
  @SerializedName(SERIALIZED_NAME_PRONOUNS)
  private String pronouns;

  public static final String SERIALIZED_NAME_RECORD_URL = "record_url";
  @SerializedName(SERIALIZED_NAME_RECORD_URL)
  private String recordUrl;

  public static final String SERIALIZED_NAME_ROW_VERSION = "row_version";
  @SerializedName(SERIALIZED_NAME_ROW_VERSION)
  private String rowVersion;

  public static final String SERIALIZED_NAME_SALUTATION = "salutation";
  @SerializedName(SERIALIZED_NAME_SALUTATION)
  private String salutation;

  public static final String SERIALIZED_NAME_SOCIAL_LINKS = "social_links";
  @SerializedName(SERIALIZED_NAME_SOCIAL_LINKS)
  private List<SocialLink> socialLinks = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOCIAL_SECURITY_NUMBER = "social_security_number";
  @SerializedName(SERIALIZED_NAME_SOCIAL_SECURITY_NUMBER)
  private String socialSecurityNumber;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public static final String SERIALIZED_NAME_SOURCE_ID = "source_id";
  @SerializedName(SERIALIZED_NAME_SOURCE_ID)
  private String sourceId;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags;

  public static final String SERIALIZED_NAME_TAX_CODE = "tax_code";
  @SerializedName(SERIALIZED_NAME_TAX_CODE)
  private String taxCode;

  public static final String SERIALIZED_NAME_TAX_ID = "tax_id";
  @SerializedName(SERIALIZED_NAME_TAX_ID)
  private String taxId;

  public static final String SERIALIZED_NAME_TEAM = "team";
  @SerializedName(SERIALIZED_NAME_TEAM)
  private Team team;

  public static final String SERIALIZED_NAME_TIMEZONE = "timezone";
  @SerializedName(SERIALIZED_NAME_TIMEZONE)
  private String timezone;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_WORKS_REMOTE = "works_remote";
  @SerializedName(SERIALIZED_NAME_WORKS_REMOTE)
  private Boolean worksRemote;

  public Employee() {
  }

  public Employee(
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

  public Employee addresses(List<Address> addresses) {
    this.addresses = addresses;
    return this;
  }

  public Employee addAddressesItem(Address addressesItem) {
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


  public Employee bankAccounts(List<BankAccount> bankAccounts) {
    this.bankAccounts = bankAccounts;
    return this;
  }

  public Employee addBankAccountsItem(BankAccount bankAccountsItem) {
    if (this.bankAccounts == null) {
      this.bankAccounts = new ArrayList<>();
    }
    this.bankAccounts.add(bankAccountsItem);
    return this;
  }

  /**
   * Get bankAccounts
   * @return bankAccounts
   */
  @javax.annotation.Nullable
  public List<BankAccount> getBankAccounts() {
    return bankAccounts;
  }

  public void setBankAccounts(List<BankAccount> bankAccounts) {
    this.bankAccounts = bankAccounts;
  }


  public Employee birthday(LocalDate birthday) {
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


  public Employee companyId(String companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * The unique identifier of the company.
   * @return companyId
   */
  @javax.annotation.Nullable
  public String getCompanyId() {
    return companyId;
  }

  public void setCompanyId(String companyId) {
    this.companyId = companyId;
  }


  public Employee companyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  /**
   * The name of the company.
   * @return companyName
   */
  @javax.annotation.Nullable
  public String getCompanyName() {
    return companyName;
  }

  public void setCompanyName(String companyName) {
    this.companyName = companyName;
  }


  public Employee compensations(List<EmployeeCompensation> compensations) {
    this.compensations = compensations;
    return this;
  }

  public Employee addCompensationsItem(EmployeeCompensation compensationsItem) {
    if (this.compensations == null) {
      this.compensations = new ArrayList<>();
    }
    this.compensations.add(compensationsItem);
    return this;
  }

  /**
   * Get compensations
   * @return compensations
   */
  @javax.annotation.Nullable
  public List<EmployeeCompensation> getCompensations() {
    return compensations;
  }

  public void setCompensations(List<EmployeeCompensation> compensations) {
    this.compensations = compensations;
  }


  public Employee countryOfBirth(String countryOfBirth) {
    this.countryOfBirth = countryOfBirth;
    return this;
  }

  /**
   * Country code according to ISO 3166-1 alpha-2.
   * @return countryOfBirth
   */
  @javax.annotation.Nullable
  public String getCountryOfBirth() {
    return countryOfBirth;
  }

  public void setCountryOfBirth(String countryOfBirth) {
    this.countryOfBirth = countryOfBirth;
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



  public Employee customFields(List<CustomField> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Employee addCustomFieldsItem(CustomField customFieldsItem) {
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


  public Employee customMappings(Object customMappings) {
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


  public Employee deceasedOn(LocalDate deceasedOn) {
    this.deceasedOn = deceasedOn;
    return this;
  }

  /**
   * The date the person deceased.
   * @return deceasedOn
   */
  @javax.annotation.Nullable
  public LocalDate getDeceasedOn() {
    return deceasedOn;
  }

  public void setDeceasedOn(LocalDate deceasedOn) {
    this.deceasedOn = deceasedOn;
  }


  public Employee deleted(Boolean deleted) {
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


  @Deprecated
  public Employee department(String department) {
    this.department = department;
    return this;
  }

  /**
   * The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.
   * @return department
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getDepartment() {
    return department;
  }

  @Deprecated
  public void setDepartment(String department) {
    this.department = department;
  }


  public Employee departmentId(String departmentId) {
    this.departmentId = departmentId;
    return this;
  }

  /**
   * Unique identifier of the department ID this employee belongs to.
   * @return departmentId
   */
  @javax.annotation.Nullable
  public String getDepartmentId() {
    return departmentId;
  }

  public void setDepartmentId(String departmentId) {
    this.departmentId = departmentId;
  }


  public Employee departmentName(String departmentName) {
    this.departmentName = departmentName;
    return this;
  }

  /**
   * Name of the department this employee belongs to.
   * @return departmentName
   */
  @javax.annotation.Nullable
  public String getDepartmentName() {
    return departmentName;
  }

  public void setDepartmentName(String departmentName) {
    this.departmentName = departmentName;
  }


  public Employee description(String description) {
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


  public Employee dietaryPreference(String dietaryPreference) {
    this.dietaryPreference = dietaryPreference;
    return this;
  }

  /**
   * Indicate the employee&#39;s dietary preference.
   * @return dietaryPreference
   */
  @javax.annotation.Nullable
  public String getDietaryPreference() {
    return dietaryPreference;
  }

  public void setDietaryPreference(String dietaryPreference) {
    this.dietaryPreference = dietaryPreference;
  }


  public Employee directReports(List<String> directReports) {
    this.directReports = directReports;
    return this;
  }

  public Employee addDirectReportsItem(String directReportsItem) {
    if (this.directReports == null) {
      this.directReports = new ArrayList<>();
    }
    this.directReports.add(directReportsItem);
    return this;
  }

  /**
   * Direct reports is an array of ids that reflect the individuals in an organizational hierarchy who are directly supervised by this specific employee.
   * @return directReports
   */
  @javax.annotation.Nullable
  public List<String> getDirectReports() {
    return directReports;
  }

  public void setDirectReports(List<String> directReports) {
    this.directReports = directReports;
  }


  public Employee displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * The name used to display the employee, often a combination of their first and last names.
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public Employee division(String division) {
    this.division = division;
    return this;
  }

  /**
   * The division the person is currently in. Usually a collection of departments or teams or regions.
   * @return division
   */
  @javax.annotation.Nullable
  public String getDivision() {
    return division;
  }

  public void setDivision(String division) {
    this.division = division;
  }


  public Employee divisionId(String divisionId) {
    this.divisionId = divisionId;
    return this;
  }

  /**
   * Unique identifier of the division this employee belongs to.
   * @return divisionId
   */
  @javax.annotation.Nullable
  public String getDivisionId() {
    return divisionId;
  }

  public void setDivisionId(String divisionId) {
    this.divisionId = divisionId;
  }


  public Employee emails(List<Email> emails) {
    this.emails = emails;
    return this;
  }

  public Employee addEmailsItem(Email emailsItem) {
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


  public Employee employeeNumber(String employeeNumber) {
    this.employeeNumber = employeeNumber;
    return this;
  }

  /**
   * An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.
   * @return employeeNumber
   */
  @javax.annotation.Nullable
  public String getEmployeeNumber() {
    return employeeNumber;
  }

  public void setEmployeeNumber(String employeeNumber) {
    this.employeeNumber = employeeNumber;
  }


  public Employee employmentEndDate(String employmentEndDate) {
    this.employmentEndDate = employmentEndDate;
    return this;
  }

  /**
   * An End Date is the date that the employee ended working at the company
   * @return employmentEndDate
   */
  @javax.annotation.Nullable
  public String getEmploymentEndDate() {
    return employmentEndDate;
  }

  public void setEmploymentEndDate(String employmentEndDate) {
    this.employmentEndDate = employmentEndDate;
  }


  public Employee employmentRole(EmployeeEmploymentRole employmentRole) {
    this.employmentRole = employmentRole;
    return this;
  }

  /**
   * Get employmentRole
   * @return employmentRole
   */
  @javax.annotation.Nullable
  public EmployeeEmploymentRole getEmploymentRole() {
    return employmentRole;
  }

  public void setEmploymentRole(EmployeeEmploymentRole employmentRole) {
    this.employmentRole = employmentRole;
  }


  public Employee employmentStartDate(String employmentStartDate) {
    this.employmentStartDate = employmentStartDate;
    return this;
  }

  /**
   * A Start Date is the date that the employee started working at the company
   * @return employmentStartDate
   */
  @javax.annotation.Nullable
  public String getEmploymentStartDate() {
    return employmentStartDate;
  }

  public void setEmploymentStartDate(String employmentStartDate) {
    this.employmentStartDate = employmentStartDate;
  }


  public Employee employmentStatus(EmploymentStatus employmentStatus) {
    this.employmentStatus = employmentStatus;
    return this;
  }

  /**
   * Get employmentStatus
   * @return employmentStatus
   */
  @javax.annotation.Nullable
  public EmploymentStatus getEmploymentStatus() {
    return employmentStatus;
  }

  public void setEmploymentStatus(EmploymentStatus employmentStatus) {
    this.employmentStatus = employmentStatus;
  }


  public Employee ethnicity(String ethnicity) {
    this.ethnicity = ethnicity;
    return this;
  }

  /**
   * The ethnicity of the employee
   * @return ethnicity
   */
  @javax.annotation.Nullable
  public String getEthnicity() {
    return ethnicity;
  }

  public void setEthnicity(String ethnicity) {
    this.ethnicity = ethnicity;
  }


  public Employee firstName(String firstName) {
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


  public Employee foodAllergies(List<String> foodAllergies) {
    this.foodAllergies = foodAllergies;
    return this;
  }

  public Employee addFoodAllergiesItem(String foodAllergiesItem) {
    if (this.foodAllergies == null) {
      this.foodAllergies = new ArrayList<>();
    }
    this.foodAllergies.add(foodAllergiesItem);
    return this;
  }

  /**
   * Indicate the employee&#39;s food allergies.
   * @return foodAllergies
   */
  @javax.annotation.Nullable
  public List<String> getFoodAllergies() {
    return foodAllergies;
  }

  public void setFoodAllergies(List<String> foodAllergies) {
    this.foodAllergies = foodAllergies;
  }


  public Employee gender(Gender gender) {
    this.gender = gender;
    return this;
  }

  /**
   * Get gender
   * @return gender
   */
  @javax.annotation.Nullable
  public Gender getGender() {
    return gender;
  }

  public void setGender(Gender gender) {
    this.gender = gender;
  }


  /**
   * A unique identifier for an object.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }



  public Employee initials(String initials) {
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


  public Employee jobs(List<EmployeeJob> jobs) {
    this.jobs = jobs;
    return this;
  }

  public Employee addJobsItem(EmployeeJob jobsItem) {
    if (this.jobs == null) {
      this.jobs = new ArrayList<>();
    }
    this.jobs.add(jobsItem);
    return this;
  }

  /**
   * Get jobs
   * @return jobs
   */
  @javax.annotation.Nullable
  public List<EmployeeJob> getJobs() {
    return jobs;
  }

  public void setJobs(List<EmployeeJob> jobs) {
    this.jobs = jobs;
  }


  public Employee languages(List<String> languages) {
    this.languages = languages;
    return this;
  }

  public Employee addLanguagesItem(String languagesItem) {
    if (this.languages == null) {
      this.languages = new ArrayList<>();
    }
    this.languages.add(languagesItem);
    return this;
  }

  /**
   * Get languages
   * @return languages
   */
  @javax.annotation.Nullable
  public List<String> getLanguages() {
    return languages;
  }

  public void setLanguages(List<String> languages) {
    this.languages = languages;
  }


  public Employee lastName(String lastName) {
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


  public Employee leavingReason(LeavingReasonEnum leavingReason) {
    this.leavingReason = leavingReason;
    return this;
  }

  /**
   * The reason because the employment ended.
   * @return leavingReason
   */
  @javax.annotation.Nullable
  public LeavingReasonEnum getLeavingReason() {
    return leavingReason;
  }

  public void setLeavingReason(LeavingReasonEnum leavingReason) {
    this.leavingReason = leavingReason;
  }


  public Employee manager(EmployeeManager manager) {
    this.manager = manager;
    return this;
  }

  /**
   * Get manager
   * @return manager
   */
  @javax.annotation.Nullable
  public EmployeeManager getManager() {
    return manager;
  }

  public void setManager(EmployeeManager manager) {
    this.manager = manager;
  }


  public Employee maritalStatus(String maritalStatus) {
    this.maritalStatus = maritalStatus;
    return this;
  }

  /**
   * The marital status of the employee.
   * @return maritalStatus
   */
  @javax.annotation.Nullable
  public String getMaritalStatus() {
    return maritalStatus;
  }

  public void setMaritalStatus(String maritalStatus) {
    this.maritalStatus = maritalStatus;
  }


  public Employee middleName(String middleName) {
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


  public Employee nationalities(List<String> nationalities) {
    this.nationalities = nationalities;
    return this;
  }

  public Employee addNationalitiesItem(String nationalitiesItem) {
    if (this.nationalities == null) {
      this.nationalities = new ArrayList<>();
    }
    this.nationalities.add(nationalitiesItem);
    return this;
  }

  /**
   * Get nationalities
   * @return nationalities
   */
  @javax.annotation.Nullable
  public List<String> getNationalities() {
    return nationalities;
  }

  public void setNationalities(List<String> nationalities) {
    this.nationalities = nationalities;
  }


  public Employee partner(Person partner) {
    this.partner = partner;
    return this;
  }

  /**
   * Get partner
   * @return partner
   */
  @javax.annotation.Nullable
  public Person getPartner() {
    return partner;
  }

  public void setPartner(Person partner) {
    this.partner = partner;
  }


  public Employee phoneNumbers(List<PhoneNumber> phoneNumbers) {
    this.phoneNumbers = phoneNumbers;
    return this;
  }

  public Employee addPhoneNumbersItem(PhoneNumber phoneNumbersItem) {
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


  public Employee photoUrl(String photoUrl) {
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


  public Employee preferredLanguage(String preferredLanguage) {
    this.preferredLanguage = preferredLanguage;
    return this;
  }

  /**
   * language code according to ISO 639-1. For the United States - EN
   * @return preferredLanguage
   */
  @javax.annotation.Nullable
  public String getPreferredLanguage() {
    return preferredLanguage;
  }

  public void setPreferredLanguage(String preferredLanguage) {
    this.preferredLanguage = preferredLanguage;
  }


  public Employee preferredName(String preferredName) {
    this.preferredName = preferredName;
    return this;
  }

  /**
   * The name the employee prefers to be addressed by, which may be different from their legal name.
   * @return preferredName
   */
  @javax.annotation.Nullable
  public String getPreferredName() {
    return preferredName;
  }

  public void setPreferredName(String preferredName) {
    this.preferredName = preferredName;
  }


  public Employee probationPeriod(ProbationPeriod probationPeriod) {
    this.probationPeriod = probationPeriod;
    return this;
  }

  /**
   * Get probationPeriod
   * @return probationPeriod
   */
  @javax.annotation.Nullable
  public ProbationPeriod getProbationPeriod() {
    return probationPeriod;
  }

  public void setProbationPeriod(ProbationPeriod probationPeriod) {
    this.probationPeriod = probationPeriod;
  }


  public Employee pronouns(String pronouns) {
    this.pronouns = pronouns;
    return this;
  }

  /**
   * The preferred pronouns of the person.
   * @return pronouns
   */
  @javax.annotation.Nullable
  public String getPronouns() {
    return pronouns;
  }

  public void setPronouns(String pronouns) {
    this.pronouns = pronouns;
  }


  public Employee recordUrl(String recordUrl) {
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


  public Employee rowVersion(String rowVersion) {
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


  public Employee salutation(String salutation) {
    this.salutation = salutation;
    return this;
  }

  /**
   * A formal salutation for the person. For example, &#39;Mr&#39;, &#39;Mrs&#39;
   * @return salutation
   */
  @javax.annotation.Nullable
  public String getSalutation() {
    return salutation;
  }

  public void setSalutation(String salutation) {
    this.salutation = salutation;
  }


  public Employee socialLinks(List<SocialLink> socialLinks) {
    this.socialLinks = socialLinks;
    return this;
  }

  public Employee addSocialLinksItem(SocialLink socialLinksItem) {
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
  public List<SocialLink> getSocialLinks() {
    return socialLinks;
  }

  public void setSocialLinks(List<SocialLink> socialLinks) {
    this.socialLinks = socialLinks;
  }


  public Employee socialSecurityNumber(String socialSecurityNumber) {
    this.socialSecurityNumber = socialSecurityNumber;
    return this;
  }

  /**
   * A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.
   * @return socialSecurityNumber
   */
  @javax.annotation.Nullable
  public String getSocialSecurityNumber() {
    return socialSecurityNumber;
  }

  public void setSocialSecurityNumber(String socialSecurityNumber) {
    this.socialSecurityNumber = socialSecurityNumber;
  }


  public Employee source(String source) {
    this.source = source;
    return this;
  }

  /**
   * When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.
   * @return source
   */
  @javax.annotation.Nullable
  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }


  public Employee sourceId(String sourceId) {
    this.sourceId = sourceId;
    return this;
  }

  /**
   * Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).
   * @return sourceId
   */
  @javax.annotation.Nullable
  public String getSourceId() {
    return sourceId;
  }

  public void setSourceId(String sourceId) {
    this.sourceId = sourceId;
  }


  public Employee tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public Employee addTagsItem(String tagsItem) {
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


  public Employee taxCode(String taxCode) {
    this.taxCode = taxCode;
    return this;
  }

  /**
   * Get taxCode
   * @return taxCode
   */
  @javax.annotation.Nullable
  public String getTaxCode() {
    return taxCode;
  }

  public void setTaxCode(String taxCode) {
    this.taxCode = taxCode;
  }


  public Employee taxId(String taxId) {
    this.taxId = taxId;
    return this;
  }

  /**
   * Get taxId
   * @return taxId
   */
  @javax.annotation.Nullable
  public String getTaxId() {
    return taxId;
  }

  public void setTaxId(String taxId) {
    this.taxId = taxId;
  }


  public Employee team(Team team) {
    this.team = team;
    return this;
  }

  /**
   * Get team
   * @return team
   */
  @javax.annotation.Nullable
  public Team getTeam() {
    return team;
  }

  public void setTeam(Team team) {
    this.team = team;
  }


  public Employee timezone(String timezone) {
    this.timezone = timezone;
    return this;
  }

  /**
   * The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.
   * @return timezone
   */
  @javax.annotation.Nullable
  public String getTimezone() {
    return timezone;
  }

  public void setTimezone(String timezone) {
    this.timezone = timezone;
  }


  public Employee title(String title) {
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



  public Employee worksRemote(Boolean worksRemote) {
    this.worksRemote = worksRemote;
    return this;
  }

  /**
   * Indicates if the employee works from a remote location.
   * @return worksRemote
   */
  @javax.annotation.Nullable
  public Boolean getWorksRemote() {
    return worksRemote;
  }

  public void setWorksRemote(Boolean worksRemote) {
    this.worksRemote = worksRemote;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Employee employee = (Employee) o;
    return Objects.equals(this.addresses, employee.addresses) &&
        Objects.equals(this.bankAccounts, employee.bankAccounts) &&
        Objects.equals(this.birthday, employee.birthday) &&
        Objects.equals(this.companyId, employee.companyId) &&
        Objects.equals(this.companyName, employee.companyName) &&
        Objects.equals(this.compensations, employee.compensations) &&
        Objects.equals(this.countryOfBirth, employee.countryOfBirth) &&
        Objects.equals(this.createdAt, employee.createdAt) &&
        Objects.equals(this.createdBy, employee.createdBy) &&
        Objects.equals(this.customFields, employee.customFields) &&
        Objects.equals(this.customMappings, employee.customMappings) &&
        Objects.equals(this.deceasedOn, employee.deceasedOn) &&
        Objects.equals(this.deleted, employee.deleted) &&
        Objects.equals(this.department, employee.department) &&
        Objects.equals(this.departmentId, employee.departmentId) &&
        Objects.equals(this.departmentName, employee.departmentName) &&
        Objects.equals(this.description, employee.description) &&
        Objects.equals(this.dietaryPreference, employee.dietaryPreference) &&
        Objects.equals(this.directReports, employee.directReports) &&
        Objects.equals(this.displayName, employee.displayName) &&
        Objects.equals(this.division, employee.division) &&
        Objects.equals(this.divisionId, employee.divisionId) &&
        Objects.equals(this.emails, employee.emails) &&
        Objects.equals(this.employeeNumber, employee.employeeNumber) &&
        Objects.equals(this.employmentEndDate, employee.employmentEndDate) &&
        Objects.equals(this.employmentRole, employee.employmentRole) &&
        Objects.equals(this.employmentStartDate, employee.employmentStartDate) &&
        Objects.equals(this.employmentStatus, employee.employmentStatus) &&
        Objects.equals(this.ethnicity, employee.ethnicity) &&
        Objects.equals(this.firstName, employee.firstName) &&
        Objects.equals(this.foodAllergies, employee.foodAllergies) &&
        Objects.equals(this.gender, employee.gender) &&
        Objects.equals(this.id, employee.id) &&
        Objects.equals(this.initials, employee.initials) &&
        Objects.equals(this.jobs, employee.jobs) &&
        Objects.equals(this.languages, employee.languages) &&
        Objects.equals(this.lastName, employee.lastName) &&
        Objects.equals(this.leavingReason, employee.leavingReason) &&
        Objects.equals(this.manager, employee.manager) &&
        Objects.equals(this.maritalStatus, employee.maritalStatus) &&
        Objects.equals(this.middleName, employee.middleName) &&
        Objects.equals(this.nationalities, employee.nationalities) &&
        Objects.equals(this.partner, employee.partner) &&
        Objects.equals(this.phoneNumbers, employee.phoneNumbers) &&
        Objects.equals(this.photoUrl, employee.photoUrl) &&
        Objects.equals(this.preferredLanguage, employee.preferredLanguage) &&
        Objects.equals(this.preferredName, employee.preferredName) &&
        Objects.equals(this.probationPeriod, employee.probationPeriod) &&
        Objects.equals(this.pronouns, employee.pronouns) &&
        Objects.equals(this.recordUrl, employee.recordUrl) &&
        Objects.equals(this.rowVersion, employee.rowVersion) &&
        Objects.equals(this.salutation, employee.salutation) &&
        Objects.equals(this.socialLinks, employee.socialLinks) &&
        Objects.equals(this.socialSecurityNumber, employee.socialSecurityNumber) &&
        Objects.equals(this.source, employee.source) &&
        Objects.equals(this.sourceId, employee.sourceId) &&
        Objects.equals(this.tags, employee.tags) &&
        Objects.equals(this.taxCode, employee.taxCode) &&
        Objects.equals(this.taxId, employee.taxId) &&
        Objects.equals(this.team, employee.team) &&
        Objects.equals(this.timezone, employee.timezone) &&
        Objects.equals(this.title, employee.title) &&
        Objects.equals(this.updatedAt, employee.updatedAt) &&
        Objects.equals(this.updatedBy, employee.updatedBy) &&
        Objects.equals(this.worksRemote, employee.worksRemote);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(addresses, bankAccounts, birthday, companyId, companyName, compensations, countryOfBirth, createdAt, createdBy, customFields, customMappings, deceasedOn, deleted, department, departmentId, departmentName, description, dietaryPreference, directReports, displayName, division, divisionId, emails, employeeNumber, employmentEndDate, employmentRole, employmentStartDate, employmentStatus, ethnicity, firstName, foodAllergies, gender, id, initials, jobs, languages, lastName, leavingReason, manager, maritalStatus, middleName, nationalities, partner, phoneNumbers, photoUrl, preferredLanguage, preferredName, probationPeriod, pronouns, recordUrl, rowVersion, salutation, socialLinks, socialSecurityNumber, source, sourceId, tags, taxCode, taxId, team, timezone, title, updatedAt, updatedBy, worksRemote);
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
    sb.append("class Employee {\n");
    sb.append("    addresses: ").append(toIndentedString(addresses)).append("\n");
    sb.append("    bankAccounts: ").append(toIndentedString(bankAccounts)).append("\n");
    sb.append("    birthday: ").append(toIndentedString(birthday)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    companyName: ").append(toIndentedString(companyName)).append("\n");
    sb.append("    compensations: ").append(toIndentedString(compensations)).append("\n");
    sb.append("    countryOfBirth: ").append(toIndentedString(countryOfBirth)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    deceasedOn: ").append(toIndentedString(deceasedOn)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    department: ").append(toIndentedString(department)).append("\n");
    sb.append("    departmentId: ").append(toIndentedString(departmentId)).append("\n");
    sb.append("    departmentName: ").append(toIndentedString(departmentName)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    dietaryPreference: ").append(toIndentedString(dietaryPreference)).append("\n");
    sb.append("    directReports: ").append(toIndentedString(directReports)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    division: ").append(toIndentedString(division)).append("\n");
    sb.append("    divisionId: ").append(toIndentedString(divisionId)).append("\n");
    sb.append("    emails: ").append(toIndentedString(emails)).append("\n");
    sb.append("    employeeNumber: ").append(toIndentedString(employeeNumber)).append("\n");
    sb.append("    employmentEndDate: ").append(toIndentedString(employmentEndDate)).append("\n");
    sb.append("    employmentRole: ").append(toIndentedString(employmentRole)).append("\n");
    sb.append("    employmentStartDate: ").append(toIndentedString(employmentStartDate)).append("\n");
    sb.append("    employmentStatus: ").append(toIndentedString(employmentStatus)).append("\n");
    sb.append("    ethnicity: ").append(toIndentedString(ethnicity)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    foodAllergies: ").append(toIndentedString(foodAllergies)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    initials: ").append(toIndentedString(initials)).append("\n");
    sb.append("    jobs: ").append(toIndentedString(jobs)).append("\n");
    sb.append("    languages: ").append(toIndentedString(languages)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    leavingReason: ").append(toIndentedString(leavingReason)).append("\n");
    sb.append("    manager: ").append(toIndentedString(manager)).append("\n");
    sb.append("    maritalStatus: ").append(toIndentedString(maritalStatus)).append("\n");
    sb.append("    middleName: ").append(toIndentedString(middleName)).append("\n");
    sb.append("    nationalities: ").append(toIndentedString(nationalities)).append("\n");
    sb.append("    partner: ").append(toIndentedString(partner)).append("\n");
    sb.append("    phoneNumbers: ").append(toIndentedString(phoneNumbers)).append("\n");
    sb.append("    photoUrl: ").append(toIndentedString(photoUrl)).append("\n");
    sb.append("    preferredLanguage: ").append(toIndentedString(preferredLanguage)).append("\n");
    sb.append("    preferredName: ").append(toIndentedString(preferredName)).append("\n");
    sb.append("    probationPeriod: ").append(toIndentedString(probationPeriod)).append("\n");
    sb.append("    pronouns: ").append(toIndentedString(pronouns)).append("\n");
    sb.append("    recordUrl: ").append(toIndentedString(recordUrl)).append("\n");
    sb.append("    rowVersion: ").append(toIndentedString(rowVersion)).append("\n");
    sb.append("    salutation: ").append(toIndentedString(salutation)).append("\n");
    sb.append("    socialLinks: ").append(toIndentedString(socialLinks)).append("\n");
    sb.append("    socialSecurityNumber: ").append(toIndentedString(socialSecurityNumber)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    sourceId: ").append(toIndentedString(sourceId)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    taxCode: ").append(toIndentedString(taxCode)).append("\n");
    sb.append("    taxId: ").append(toIndentedString(taxId)).append("\n");
    sb.append("    team: ").append(toIndentedString(team)).append("\n");
    sb.append("    timezone: ").append(toIndentedString(timezone)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    worksRemote: ").append(toIndentedString(worksRemote)).append("\n");
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
    openapiFields.add("bank_accounts");
    openapiFields.add("birthday");
    openapiFields.add("company_id");
    openapiFields.add("company_name");
    openapiFields.add("compensations");
    openapiFields.add("country_of_birth");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("custom_fields");
    openapiFields.add("custom_mappings");
    openapiFields.add("deceased_on");
    openapiFields.add("deleted");
    openapiFields.add("department");
    openapiFields.add("department_id");
    openapiFields.add("department_name");
    openapiFields.add("description");
    openapiFields.add("dietary_preference");
    openapiFields.add("direct_reports");
    openapiFields.add("display_name");
    openapiFields.add("division");
    openapiFields.add("division_id");
    openapiFields.add("emails");
    openapiFields.add("employee_number");
    openapiFields.add("employment_end_date");
    openapiFields.add("employment_role");
    openapiFields.add("employment_start_date");
    openapiFields.add("employment_status");
    openapiFields.add("ethnicity");
    openapiFields.add("first_name");
    openapiFields.add("food_allergies");
    openapiFields.add("gender");
    openapiFields.add("id");
    openapiFields.add("initials");
    openapiFields.add("jobs");
    openapiFields.add("languages");
    openapiFields.add("last_name");
    openapiFields.add("leaving_reason");
    openapiFields.add("manager");
    openapiFields.add("marital_status");
    openapiFields.add("middle_name");
    openapiFields.add("nationalities");
    openapiFields.add("partner");
    openapiFields.add("phone_numbers");
    openapiFields.add("photo_url");
    openapiFields.add("preferred_language");
    openapiFields.add("preferred_name");
    openapiFields.add("probation_period");
    openapiFields.add("pronouns");
    openapiFields.add("record_url");
    openapiFields.add("row_version");
    openapiFields.add("salutation");
    openapiFields.add("social_links");
    openapiFields.add("social_security_number");
    openapiFields.add("source");
    openapiFields.add("source_id");
    openapiFields.add("tags");
    openapiFields.add("tax_code");
    openapiFields.add("tax_id");
    openapiFields.add("team");
    openapiFields.add("timezone");
    openapiFields.add("title");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("works_remote");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Employee
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Employee.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Employee is not found in the empty JSON string", Employee.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Employee.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Employee` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Employee.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
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
      if (jsonObj.get("bank_accounts") != null && !jsonObj.get("bank_accounts").isJsonNull()) {
        JsonArray jsonArraybankAccounts = jsonObj.getAsJsonArray("bank_accounts");
        if (jsonArraybankAccounts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("bank_accounts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `bank_accounts` to be an array in the JSON string but got `%s`", jsonObj.get("bank_accounts").toString()));
          }

          // validate the optional field `bank_accounts` (array)
          for (int i = 0; i < jsonArraybankAccounts.size(); i++) {
            BankAccount.validateJsonElement(jsonArraybankAccounts.get(i));
          };
        }
      }
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("company_name") != null && !jsonObj.get("company_name").isJsonNull()) && !jsonObj.get("company_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_name").toString()));
      }
      if (jsonObj.get("compensations") != null && !jsonObj.get("compensations").isJsonNull()) {
        JsonArray jsonArraycompensations = jsonObj.getAsJsonArray("compensations");
        if (jsonArraycompensations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("compensations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `compensations` to be an array in the JSON string but got `%s`", jsonObj.get("compensations").toString()));
          }

          // validate the optional field `compensations` (array)
          for (int i = 0; i < jsonArraycompensations.size(); i++) {
            EmployeeCompensation.validateJsonElement(jsonArraycompensations.get(i));
          };
        }
      }
      if ((jsonObj.get("country_of_birth") != null && !jsonObj.get("country_of_birth").isJsonNull()) && !jsonObj.get("country_of_birth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country_of_birth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country_of_birth").toString()));
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
      if ((jsonObj.get("department") != null && !jsonObj.get("department").isJsonNull()) && !jsonObj.get("department").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `department` to be a primitive type in the JSON string but got `%s`", jsonObj.get("department").toString()));
      }
      if ((jsonObj.get("department_id") != null && !jsonObj.get("department_id").isJsonNull()) && !jsonObj.get("department_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `department_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("department_id").toString()));
      }
      if ((jsonObj.get("department_name") != null && !jsonObj.get("department_name").isJsonNull()) && !jsonObj.get("department_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `department_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("department_name").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("dietary_preference") != null && !jsonObj.get("dietary_preference").isJsonNull()) && !jsonObj.get("dietary_preference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dietary_preference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dietary_preference").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("direct_reports") != null && !jsonObj.get("direct_reports").isJsonNull() && !jsonObj.get("direct_reports").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `direct_reports` to be an array in the JSON string but got `%s`", jsonObj.get("direct_reports").toString()));
      }
      if ((jsonObj.get("display_name") != null && !jsonObj.get("display_name").isJsonNull()) && !jsonObj.get("display_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_name").toString()));
      }
      if ((jsonObj.get("division") != null && !jsonObj.get("division").isJsonNull()) && !jsonObj.get("division").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `division` to be a primitive type in the JSON string but got `%s`", jsonObj.get("division").toString()));
      }
      if ((jsonObj.get("division_id") != null && !jsonObj.get("division_id").isJsonNull()) && !jsonObj.get("division_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `division_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("division_id").toString()));
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
      if ((jsonObj.get("employee_number") != null && !jsonObj.get("employee_number").isJsonNull()) && !jsonObj.get("employee_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employee_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employee_number").toString()));
      }
      if ((jsonObj.get("employment_end_date") != null && !jsonObj.get("employment_end_date").isJsonNull()) && !jsonObj.get("employment_end_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employment_end_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employment_end_date").toString()));
      }
      // validate the optional field `employment_role`
      if (jsonObj.get("employment_role") != null && !jsonObj.get("employment_role").isJsonNull()) {
        EmployeeEmploymentRole.validateJsonElement(jsonObj.get("employment_role"));
      }
      if ((jsonObj.get("employment_start_date") != null && !jsonObj.get("employment_start_date").isJsonNull()) && !jsonObj.get("employment_start_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employment_start_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employment_start_date").toString()));
      }
      // validate the optional field `employment_status`
      if (jsonObj.get("employment_status") != null && !jsonObj.get("employment_status").isJsonNull()) {
        EmploymentStatus.validateJsonElement(jsonObj.get("employment_status"));
      }
      if ((jsonObj.get("ethnicity") != null && !jsonObj.get("ethnicity").isJsonNull()) && !jsonObj.get("ethnicity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ethnicity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ethnicity").toString()));
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("food_allergies") != null && !jsonObj.get("food_allergies").isJsonNull() && !jsonObj.get("food_allergies").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `food_allergies` to be an array in the JSON string but got `%s`", jsonObj.get("food_allergies").toString()));
      }
      // validate the optional field `gender`
      if (jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) {
        Gender.validateJsonElement(jsonObj.get("gender"));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("initials") != null && !jsonObj.get("initials").isJsonNull()) && !jsonObj.get("initials").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `initials` to be a primitive type in the JSON string but got `%s`", jsonObj.get("initials").toString()));
      }
      if (jsonObj.get("jobs") != null && !jsonObj.get("jobs").isJsonNull()) {
        JsonArray jsonArrayjobs = jsonObj.getAsJsonArray("jobs");
        if (jsonArrayjobs != null) {
          // ensure the json data is an array
          if (!jsonObj.get("jobs").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `jobs` to be an array in the JSON string but got `%s`", jsonObj.get("jobs").toString()));
          }

          // validate the optional field `jobs` (array)
          for (int i = 0; i < jsonArrayjobs.size(); i++) {
            EmployeeJob.validateJsonElement(jsonArrayjobs.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("languages") != null && !jsonObj.get("languages").isJsonNull() && !jsonObj.get("languages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `languages` to be an array in the JSON string but got `%s`", jsonObj.get("languages").toString()));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("leaving_reason") != null && !jsonObj.get("leaving_reason").isJsonNull()) && !jsonObj.get("leaving_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `leaving_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("leaving_reason").toString()));
      }
      // validate the optional field `leaving_reason`
      if (jsonObj.get("leaving_reason") != null && !jsonObj.get("leaving_reason").isJsonNull()) {
        LeavingReasonEnum.validateJsonElement(jsonObj.get("leaving_reason"));
      }
      // validate the optional field `manager`
      if (jsonObj.get("manager") != null && !jsonObj.get("manager").isJsonNull()) {
        EmployeeManager.validateJsonElement(jsonObj.get("manager"));
      }
      if ((jsonObj.get("marital_status") != null && !jsonObj.get("marital_status").isJsonNull()) && !jsonObj.get("marital_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `marital_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("marital_status").toString()));
      }
      if ((jsonObj.get("middle_name") != null && !jsonObj.get("middle_name").isJsonNull()) && !jsonObj.get("middle_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `middle_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("middle_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("nationalities") != null && !jsonObj.get("nationalities").isJsonNull() && !jsonObj.get("nationalities").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `nationalities` to be an array in the JSON string but got `%s`", jsonObj.get("nationalities").toString()));
      }
      // validate the optional field `partner`
      if (jsonObj.get("partner") != null && !jsonObj.get("partner").isJsonNull()) {
        Person.validateJsonElement(jsonObj.get("partner"));
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
      if ((jsonObj.get("preferred_language") != null && !jsonObj.get("preferred_language").isJsonNull()) && !jsonObj.get("preferred_language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preferred_language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preferred_language").toString()));
      }
      if ((jsonObj.get("preferred_name") != null && !jsonObj.get("preferred_name").isJsonNull()) && !jsonObj.get("preferred_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preferred_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preferred_name").toString()));
      }
      // validate the optional field `probation_period`
      if (jsonObj.get("probation_period") != null && !jsonObj.get("probation_period").isJsonNull()) {
        ProbationPeriod.validateJsonElement(jsonObj.get("probation_period"));
      }
      if ((jsonObj.get("pronouns") != null && !jsonObj.get("pronouns").isJsonNull()) && !jsonObj.get("pronouns").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pronouns` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pronouns").toString()));
      }
      if ((jsonObj.get("record_url") != null && !jsonObj.get("record_url").isJsonNull()) && !jsonObj.get("record_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `record_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("record_url").toString()));
      }
      if ((jsonObj.get("row_version") != null && !jsonObj.get("row_version").isJsonNull()) && !jsonObj.get("row_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `row_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("row_version").toString()));
      }
      if ((jsonObj.get("salutation") != null && !jsonObj.get("salutation").isJsonNull()) && !jsonObj.get("salutation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `salutation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("salutation").toString()));
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
            SocialLink.validateJsonElement(jsonArraysocialLinks.get(i));
          };
        }
      }
      if ((jsonObj.get("social_security_number") != null && !jsonObj.get("social_security_number").isJsonNull()) && !jsonObj.get("social_security_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `social_security_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("social_security_number").toString()));
      }
      if ((jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) && !jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      if ((jsonObj.get("source_id") != null && !jsonObj.get("source_id").isJsonNull()) && !jsonObj.get("source_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if ((jsonObj.get("tax_code") != null && !jsonObj.get("tax_code").isJsonNull()) && !jsonObj.get("tax_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_code").toString()));
      }
      if ((jsonObj.get("tax_id") != null && !jsonObj.get("tax_id").isJsonNull()) && !jsonObj.get("tax_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_id").toString()));
      }
      // validate the optional field `team`
      if (jsonObj.get("team") != null && !jsonObj.get("team").isJsonNull()) {
        Team.validateJsonElement(jsonObj.get("team"));
      }
      if ((jsonObj.get("timezone") != null && !jsonObj.get("timezone").isJsonNull()) && !jsonObj.get("timezone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timezone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timezone").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Employee.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Employee' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Employee> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Employee.class));

       return (TypeAdapter<T>) new TypeAdapter<Employee>() {
           @Override
           public void write(JsonWriter out, Employee value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Employee read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Employee given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Employee
   * @throws IOException if the JSON string is invalid with respect to Employee
   */
  public static Employee fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Employee.class);
  }

  /**
   * Convert an instance of Employee to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

