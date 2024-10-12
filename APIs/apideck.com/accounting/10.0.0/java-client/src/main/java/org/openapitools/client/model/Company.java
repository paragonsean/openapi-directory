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
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Address;
import org.openapitools.client.model.BankAccount;
import org.openapitools.client.model.CompanyRowType;
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.CustomField;
import org.openapitools.client.model.Email;
import org.openapitools.client.model.PhoneNumber;
import org.openapitools.client.model.SocialLink;
import org.openapitools.client.model.Website;
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
 * Company
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:31.900974-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Company {
  public static final String SERIALIZED_NAME_ABN_BRANCH = "abn_branch";
  @SerializedName(SERIALIZED_NAME_ABN_BRANCH)
  private String abnBranch;

  public static final String SERIALIZED_NAME_ABN_OR_TFN = "abn_or_tfn";
  @SerializedName(SERIALIZED_NAME_ABN_OR_TFN)
  private String abnOrTfn;

  public static final String SERIALIZED_NAME_ACN = "acn";
  @SerializedName(SERIALIZED_NAME_ACN)
  private String acn;

  public static final String SERIALIZED_NAME_ADDRESSES = "addresses";
  @SerializedName(SERIALIZED_NAME_ADDRESSES)
  private List<Address> addresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_ANNUAL_REVENUE = "annual_revenue";
  @SerializedName(SERIALIZED_NAME_ANNUAL_REVENUE)
  private String annualRevenue;

  public static final String SERIALIZED_NAME_BANK_ACCOUNTS = "bank_accounts";
  @SerializedName(SERIALIZED_NAME_BANK_ACCOUNTS)
  private List<BankAccount> bankAccounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_BIRTHDAY = "birthday";
  @SerializedName(SERIALIZED_NAME_BIRTHDAY)
  private LocalDate birthday;

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

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EMAILS = "emails";
  @SerializedName(SERIALIZED_NAME_EMAILS)
  private List<Email> emails = new ArrayList<>();

  public static final String SERIALIZED_NAME_FAX = "fax";
  @SerializedName(SERIALIZED_NAME_FAX)
  private String fax;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_INDUSTRY = "industry";
  @SerializedName(SERIALIZED_NAME_INDUSTRY)
  private String industry;

  public static final String SERIALIZED_NAME_INTERACTION_COUNT = "interaction_count";
  @SerializedName(SERIALIZED_NAME_INTERACTION_COUNT)
  private Integer interactionCount;

  public static final String SERIALIZED_NAME_LAST_ACTIVITY_AT = "last_activity_at";
  @SerializedName(SERIALIZED_NAME_LAST_ACTIVITY_AT)
  private OffsetDateTime lastActivityAt;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NUMBER_OF_EMPLOYEES = "number_of_employees";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_EMPLOYEES)
  private String numberOfEmployees;

  public static final String SERIALIZED_NAME_OWNER_ID = "owner_id";
  @SerializedName(SERIALIZED_NAME_OWNER_ID)
  private String ownerId;

  public static final String SERIALIZED_NAME_OWNERSHIP = "ownership";
  @SerializedName(SERIALIZED_NAME_OWNERSHIP)
  private String ownership;

  public static final String SERIALIZED_NAME_PARENT_ID = "parent_id";
  @SerializedName(SERIALIZED_NAME_PARENT_ID)
  private String parentId;

  public static final String SERIALIZED_NAME_PAYEE_NUMBER = "payee_number";
  @SerializedName(SERIALIZED_NAME_PAYEE_NUMBER)
  private String payeeNumber;

  public static final String SERIALIZED_NAME_PHONE_NUMBERS = "phone_numbers";
  @SerializedName(SERIALIZED_NAME_PHONE_NUMBERS)
  private List<PhoneNumber> phoneNumbers = new ArrayList<>();

  public static final String SERIALIZED_NAME_READ_ONLY = "read_only";
  @SerializedName(SERIALIZED_NAME_READ_ONLY)
  private Boolean readOnly;

  public static final String SERIALIZED_NAME_ROW_TYPE = "row_type";
  @SerializedName(SERIALIZED_NAME_ROW_TYPE)
  private CompanyRowType rowType;

  public static final String SERIALIZED_NAME_SALES_TAX_NUMBER = "sales_tax_number";
  @SerializedName(SERIALIZED_NAME_SALES_TAX_NUMBER)
  private String salesTaxNumber;

  public static final String SERIALIZED_NAME_SALUTATION = "salutation";
  @SerializedName(SERIALIZED_NAME_SALUTATION)
  private String salutation;

  public static final String SERIALIZED_NAME_SOCIAL_LINKS = "social_links";
  @SerializedName(SERIALIZED_NAME_SOCIAL_LINKS)
  private List<SocialLink> socialLinks = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updated_by";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private String updatedBy;

  public static final String SERIALIZED_NAME_VAT_NUMBER = "vat_number";
  @SerializedName(SERIALIZED_NAME_VAT_NUMBER)
  private String vatNumber;

  public static final String SERIALIZED_NAME_WEBSITES = "websites";
  @SerializedName(SERIALIZED_NAME_WEBSITES)
  private List<Website> websites = new ArrayList<>();

  public Company() {
  }

  public Company(
     OffsetDateTime createdAt, 
     String createdBy, 
     Boolean deleted, 
     String id, 
     Integer interactionCount, 
     OffsetDateTime lastActivityAt, 
     String parentId, 
     OffsetDateTime updatedAt, 
     String updatedBy
  ) {
    this();
    this.createdAt = createdAt;
    this.createdBy = createdBy;
    this.deleted = deleted;
    this.id = id;
    this.interactionCount = interactionCount;
    this.lastActivityAt = lastActivityAt;
    this.parentId = parentId;
    this.updatedAt = updatedAt;
    this.updatedBy = updatedBy;
  }

  public Company abnBranch(String abnBranch) {
    this.abnBranch = abnBranch;
    return this;
  }

  /**
   * An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.
   * @return abnBranch
   */
  @javax.annotation.Nullable
  public String getAbnBranch() {
    return abnBranch;
  }

  public void setAbnBranch(String abnBranch) {
    this.abnBranch = abnBranch;
  }


  public Company abnOrTfn(String abnOrTfn) {
    this.abnOrTfn = abnOrTfn;
    return this;
  }

  /**
   * An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.
   * @return abnOrTfn
   */
  @javax.annotation.Nullable
  public String getAbnOrTfn() {
    return abnOrTfn;
  }

  public void setAbnOrTfn(String abnOrTfn) {
    this.abnOrTfn = abnOrTfn;
  }


  public Company acn(String acn) {
    this.acn = acn;
    return this;
  }

  /**
   * The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.
   * @return acn
   */
  @javax.annotation.Nullable
  public String getAcn() {
    return acn;
  }

  public void setAcn(String acn) {
    this.acn = acn;
  }


  public Company addresses(List<Address> addresses) {
    this.addresses = addresses;
    return this;
  }

  public Company addAddressesItem(Address addressesItem) {
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


  public Company annualRevenue(String annualRevenue) {
    this.annualRevenue = annualRevenue;
    return this;
  }

  /**
   * The annual revenue of the company
   * @return annualRevenue
   */
  @javax.annotation.Nullable
  public String getAnnualRevenue() {
    return annualRevenue;
  }

  public void setAnnualRevenue(String annualRevenue) {
    this.annualRevenue = annualRevenue;
  }


  public Company bankAccounts(List<BankAccount> bankAccounts) {
    this.bankAccounts = bankAccounts;
    return this;
  }

  public Company addBankAccountsItem(BankAccount bankAccountsItem) {
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


  public Company birthday(LocalDate birthday) {
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


  /**
   * Creation date
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



  /**
   * Created by user ID
   * @return createdBy
   */
  @javax.annotation.Nullable
  public String getCreatedBy() {
    return createdBy;
  }



  public Company currency(Currency currency) {
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


  public Company customFields(List<CustomField> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Company addCustomFieldsItem(CustomField customFieldsItem) {
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


  public Company customMappings(Object customMappings) {
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
   * Whether the company is deleted or not
   * @return deleted
   */
  @javax.annotation.Nullable
  public Boolean getDeleted() {
    return deleted;
  }



  public Company description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A description of the company
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Company emails(List<Email> emails) {
    this.emails = emails;
    return this;
  }

  public Company addEmailsItem(Email emailsItem) {
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


  public Company fax(String fax) {
    this.fax = fax;
    return this;
  }

  /**
   * The fax number of the company
   * @return fax
   */
  @javax.annotation.Nullable
  public String getFax() {
    return fax;
  }

  public void setFax(String fax) {
    this.fax = fax;
  }


  public Company firstName(String firstName) {
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


  /**
   * Unique identifier for the company
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Company image(String image) {
    this.image = image;
    return this;
  }

  /**
   * The Image URL of the company
   * @return image
   */
  @javax.annotation.Nullable
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public Company industry(String industry) {
    this.industry = industry;
    return this;
  }

  /**
   * The industry represents the type of business the company is in.
   * @return industry
   */
  @javax.annotation.Nullable
  public String getIndustry() {
    return industry;
  }

  public void setIndustry(String industry) {
    this.industry = industry;
  }


  /**
   * Number of interactions
   * @return interactionCount
   */
  @javax.annotation.Nullable
  public Integer getInteractionCount() {
    return interactionCount;
  }



  /**
   * Last activity date
   * @return lastActivityAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastActivityAt() {
    return lastActivityAt;
  }



  public Company lastName(String lastName) {
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


  public Company name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the company
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Company numberOfEmployees(String numberOfEmployees) {
    this.numberOfEmployees = numberOfEmployees;
    return this;
  }

  /**
   * Number of employees
   * @return numberOfEmployees
   */
  @javax.annotation.Nullable
  public String getNumberOfEmployees() {
    return numberOfEmployees;
  }

  public void setNumberOfEmployees(String numberOfEmployees) {
    this.numberOfEmployees = numberOfEmployees;
  }


  public Company ownerId(String ownerId) {
    this.ownerId = ownerId;
    return this;
  }

  /**
   * Owner ID
   * @return ownerId
   */
  @javax.annotation.Nullable
  public String getOwnerId() {
    return ownerId;
  }

  public void setOwnerId(String ownerId) {
    this.ownerId = ownerId;
  }


  public Company ownership(String ownership) {
    this.ownership = ownership;
    return this;
  }

  /**
   * The ownership indicates the type of ownership of the company.
   * @return ownership
   */
  @javax.annotation.Nullable
  public String getOwnership() {
    return ownership;
  }

  public void setOwnership(String ownership) {
    this.ownership = ownership;
  }


  /**
   * Parent ID
   * @return parentId
   */
  @javax.annotation.Nullable
  public String getParentId() {
    return parentId;
  }



  public Company payeeNumber(String payeeNumber) {
    this.payeeNumber = payeeNumber;
    return this;
  }

  /**
   * A payee number is a unique number that identifies a payee for tax purposes.
   * @return payeeNumber
   */
  @javax.annotation.Nullable
  public String getPayeeNumber() {
    return payeeNumber;
  }

  public void setPayeeNumber(String payeeNumber) {
    this.payeeNumber = payeeNumber;
  }


  public Company phoneNumbers(List<PhoneNumber> phoneNumbers) {
    this.phoneNumbers = phoneNumbers;
    return this;
  }

  public Company addPhoneNumbersItem(PhoneNumber phoneNumbersItem) {
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


  public Company readOnly(Boolean readOnly) {
    this.readOnly = readOnly;
    return this;
  }

  /**
   * Whether the company is read-only or not
   * @return readOnly
   */
  @javax.annotation.Nullable
  public Boolean getReadOnly() {
    return readOnly;
  }

  public void setReadOnly(Boolean readOnly) {
    this.readOnly = readOnly;
  }


  public Company rowType(CompanyRowType rowType) {
    this.rowType = rowType;
    return this;
  }

  /**
   * Get rowType
   * @return rowType
   */
  @javax.annotation.Nullable
  public CompanyRowType getRowType() {
    return rowType;
  }

  public void setRowType(CompanyRowType rowType) {
    this.rowType = rowType;
  }


  public Company salesTaxNumber(String salesTaxNumber) {
    this.salesTaxNumber = salesTaxNumber;
    return this;
  }

  /**
   * A sales tax number is a unique number that identifies a company for tax purposes.
   * @return salesTaxNumber
   */
  @javax.annotation.Nullable
  public String getSalesTaxNumber() {
    return salesTaxNumber;
  }

  public void setSalesTaxNumber(String salesTaxNumber) {
    this.salesTaxNumber = salesTaxNumber;
  }


  public Company salutation(String salutation) {
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


  public Company socialLinks(List<SocialLink> socialLinks) {
    this.socialLinks = socialLinks;
    return this;
  }

  public Company addSocialLinksItem(SocialLink socialLinksItem) {
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


  public Company status(String status) {
    this.status = status;
    return this;
  }

  /**
   * The status of the company
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public Company tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public Company addTagsItem(String tagsItem) {
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


  /**
   * Last updated date
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }



  /**
   * Updated by user ID
   * @return updatedBy
   */
  @javax.annotation.Nullable
  public String getUpdatedBy() {
    return updatedBy;
  }



  public Company vatNumber(String vatNumber) {
    this.vatNumber = vatNumber;
    return this;
  }

  /**
   * The VAT number of the company
   * @return vatNumber
   */
  @javax.annotation.Nullable
  public String getVatNumber() {
    return vatNumber;
  }

  public void setVatNumber(String vatNumber) {
    this.vatNumber = vatNumber;
  }


  public Company websites(List<Website> websites) {
    this.websites = websites;
    return this;
  }

  public Company addWebsitesItem(Website websitesItem) {
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
  public List<Website> getWebsites() {
    return websites;
  }

  public void setWebsites(List<Website> websites) {
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
    Company company = (Company) o;
    return Objects.equals(this.abnBranch, company.abnBranch) &&
        Objects.equals(this.abnOrTfn, company.abnOrTfn) &&
        Objects.equals(this.acn, company.acn) &&
        Objects.equals(this.addresses, company.addresses) &&
        Objects.equals(this.annualRevenue, company.annualRevenue) &&
        Objects.equals(this.bankAccounts, company.bankAccounts) &&
        Objects.equals(this.birthday, company.birthday) &&
        Objects.equals(this.createdAt, company.createdAt) &&
        Objects.equals(this.createdBy, company.createdBy) &&
        Objects.equals(this.currency, company.currency) &&
        Objects.equals(this.customFields, company.customFields) &&
        Objects.equals(this.customMappings, company.customMappings) &&
        Objects.equals(this.deleted, company.deleted) &&
        Objects.equals(this.description, company.description) &&
        Objects.equals(this.emails, company.emails) &&
        Objects.equals(this.fax, company.fax) &&
        Objects.equals(this.firstName, company.firstName) &&
        Objects.equals(this.id, company.id) &&
        Objects.equals(this.image, company.image) &&
        Objects.equals(this.industry, company.industry) &&
        Objects.equals(this.interactionCount, company.interactionCount) &&
        Objects.equals(this.lastActivityAt, company.lastActivityAt) &&
        Objects.equals(this.lastName, company.lastName) &&
        Objects.equals(this.name, company.name) &&
        Objects.equals(this.numberOfEmployees, company.numberOfEmployees) &&
        Objects.equals(this.ownerId, company.ownerId) &&
        Objects.equals(this.ownership, company.ownership) &&
        Objects.equals(this.parentId, company.parentId) &&
        Objects.equals(this.payeeNumber, company.payeeNumber) &&
        Objects.equals(this.phoneNumbers, company.phoneNumbers) &&
        Objects.equals(this.readOnly, company.readOnly) &&
        Objects.equals(this.rowType, company.rowType) &&
        Objects.equals(this.salesTaxNumber, company.salesTaxNumber) &&
        Objects.equals(this.salutation, company.salutation) &&
        Objects.equals(this.socialLinks, company.socialLinks) &&
        Objects.equals(this.status, company.status) &&
        Objects.equals(this.tags, company.tags) &&
        Objects.equals(this.updatedAt, company.updatedAt) &&
        Objects.equals(this.updatedBy, company.updatedBy) &&
        Objects.equals(this.vatNumber, company.vatNumber) &&
        Objects.equals(this.websites, company.websites);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(abnBranch, abnOrTfn, acn, addresses, annualRevenue, bankAccounts, birthday, createdAt, createdBy, currency, customFields, customMappings, deleted, description, emails, fax, firstName, id, image, industry, interactionCount, lastActivityAt, lastName, name, numberOfEmployees, ownerId, ownership, parentId, payeeNumber, phoneNumbers, readOnly, rowType, salesTaxNumber, salutation, socialLinks, status, tags, updatedAt, updatedBy, vatNumber, websites);
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
    sb.append("class Company {\n");
    sb.append("    abnBranch: ").append(toIndentedString(abnBranch)).append("\n");
    sb.append("    abnOrTfn: ").append(toIndentedString(abnOrTfn)).append("\n");
    sb.append("    acn: ").append(toIndentedString(acn)).append("\n");
    sb.append("    addresses: ").append(toIndentedString(addresses)).append("\n");
    sb.append("    annualRevenue: ").append(toIndentedString(annualRevenue)).append("\n");
    sb.append("    bankAccounts: ").append(toIndentedString(bankAccounts)).append("\n");
    sb.append("    birthday: ").append(toIndentedString(birthday)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    emails: ").append(toIndentedString(emails)).append("\n");
    sb.append("    fax: ").append(toIndentedString(fax)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    industry: ").append(toIndentedString(industry)).append("\n");
    sb.append("    interactionCount: ").append(toIndentedString(interactionCount)).append("\n");
    sb.append("    lastActivityAt: ").append(toIndentedString(lastActivityAt)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    numberOfEmployees: ").append(toIndentedString(numberOfEmployees)).append("\n");
    sb.append("    ownerId: ").append(toIndentedString(ownerId)).append("\n");
    sb.append("    ownership: ").append(toIndentedString(ownership)).append("\n");
    sb.append("    parentId: ").append(toIndentedString(parentId)).append("\n");
    sb.append("    payeeNumber: ").append(toIndentedString(payeeNumber)).append("\n");
    sb.append("    phoneNumbers: ").append(toIndentedString(phoneNumbers)).append("\n");
    sb.append("    readOnly: ").append(toIndentedString(readOnly)).append("\n");
    sb.append("    rowType: ").append(toIndentedString(rowType)).append("\n");
    sb.append("    salesTaxNumber: ").append(toIndentedString(salesTaxNumber)).append("\n");
    sb.append("    salutation: ").append(toIndentedString(salutation)).append("\n");
    sb.append("    socialLinks: ").append(toIndentedString(socialLinks)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    vatNumber: ").append(toIndentedString(vatNumber)).append("\n");
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
    openapiFields.add("abn_branch");
    openapiFields.add("abn_or_tfn");
    openapiFields.add("acn");
    openapiFields.add("addresses");
    openapiFields.add("annual_revenue");
    openapiFields.add("bank_accounts");
    openapiFields.add("birthday");
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("currency");
    openapiFields.add("custom_fields");
    openapiFields.add("custom_mappings");
    openapiFields.add("deleted");
    openapiFields.add("description");
    openapiFields.add("emails");
    openapiFields.add("fax");
    openapiFields.add("first_name");
    openapiFields.add("id");
    openapiFields.add("image");
    openapiFields.add("industry");
    openapiFields.add("interaction_count");
    openapiFields.add("last_activity_at");
    openapiFields.add("last_name");
    openapiFields.add("name");
    openapiFields.add("number_of_employees");
    openapiFields.add("owner_id");
    openapiFields.add("ownership");
    openapiFields.add("parent_id");
    openapiFields.add("payee_number");
    openapiFields.add("phone_numbers");
    openapiFields.add("read_only");
    openapiFields.add("row_type");
    openapiFields.add("sales_tax_number");
    openapiFields.add("salutation");
    openapiFields.add("social_links");
    openapiFields.add("status");
    openapiFields.add("tags");
    openapiFields.add("updated_at");
    openapiFields.add("updated_by");
    openapiFields.add("vat_number");
    openapiFields.add("websites");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Company
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Company.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Company is not found in the empty JSON string", Company.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Company.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Company` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Company.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("abn_branch") != null && !jsonObj.get("abn_branch").isJsonNull()) && !jsonObj.get("abn_branch").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `abn_branch` to be a primitive type in the JSON string but got `%s`", jsonObj.get("abn_branch").toString()));
      }
      if ((jsonObj.get("abn_or_tfn") != null && !jsonObj.get("abn_or_tfn").isJsonNull()) && !jsonObj.get("abn_or_tfn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `abn_or_tfn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("abn_or_tfn").toString()));
      }
      if ((jsonObj.get("acn") != null && !jsonObj.get("acn").isJsonNull()) && !jsonObj.get("acn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `acn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("acn").toString()));
      }
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
      if ((jsonObj.get("annual_revenue") != null && !jsonObj.get("annual_revenue").isJsonNull()) && !jsonObj.get("annual_revenue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `annual_revenue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("annual_revenue").toString()));
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
      if ((jsonObj.get("fax") != null && !jsonObj.get("fax").isJsonNull()) && !jsonObj.get("fax").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fax` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fax").toString()));
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) && !jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if ((jsonObj.get("industry") != null && !jsonObj.get("industry").isJsonNull()) && !jsonObj.get("industry").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `industry` to be a primitive type in the JSON string but got `%s`", jsonObj.get("industry").toString()));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("number_of_employees") != null && !jsonObj.get("number_of_employees").isJsonNull()) && !jsonObj.get("number_of_employees").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number_of_employees` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number_of_employees").toString()));
      }
      if ((jsonObj.get("owner_id") != null && !jsonObj.get("owner_id").isJsonNull()) && !jsonObj.get("owner_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner_id").toString()));
      }
      if ((jsonObj.get("ownership") != null && !jsonObj.get("ownership").isJsonNull()) && !jsonObj.get("ownership").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ownership` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ownership").toString()));
      }
      if ((jsonObj.get("parent_id") != null && !jsonObj.get("parent_id").isJsonNull()) && !jsonObj.get("parent_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parent_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parent_id").toString()));
      }
      if ((jsonObj.get("payee_number") != null && !jsonObj.get("payee_number").isJsonNull()) && !jsonObj.get("payee_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payee_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payee_number").toString()));
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
      // validate the optional field `row_type`
      if (jsonObj.get("row_type") != null && !jsonObj.get("row_type").isJsonNull()) {
        CompanyRowType.validateJsonElement(jsonObj.get("row_type"));
      }
      if ((jsonObj.get("sales_tax_number") != null && !jsonObj.get("sales_tax_number").isJsonNull()) && !jsonObj.get("sales_tax_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sales_tax_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sales_tax_number").toString()));
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
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if ((jsonObj.get("updated_by") != null && !jsonObj.get("updated_by").isJsonNull()) && !jsonObj.get("updated_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_by").toString()));
      }
      if ((jsonObj.get("vat_number") != null && !jsonObj.get("vat_number").isJsonNull()) && !jsonObj.get("vat_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vat_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vat_number").toString()));
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
            Website.validateJsonElement(jsonArraywebsites.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Company.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Company' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Company> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Company.class));

       return (TypeAdapter<T>) new TypeAdapter<Company>() {
           @Override
           public void write(JsonWriter out, Company value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Company read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Company given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Company
   * @throws IOException if the JSON string is invalid with respect to Company
   */
  public static Company fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Company.class);
  }

  /**
   * Convert an instance of Company to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

