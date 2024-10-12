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
import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Address;
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
 * Contact
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:49.113586-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Contact {
  public static final String SERIALIZED_NAME_ACTIVE = "active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_ADDRESSES = "addresses";
  @SerializedName(SERIALIZED_NAME_ADDRESSES)
  private List<Address> addresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_BIRTHDAY = "birthday";
  @SerializedName(SERIALIZED_NAME_BIRTHDAY)
  private String birthday;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private String companyId;

  public static final String SERIALIZED_NAME_COMPANY_NAME = "company_name";
  @SerializedName(SERIALIZED_NAME_COMPANY_NAME)
  private String companyName;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CURRENT_BALANCE = "current_balance";
  @SerializedName(SERIALIZED_NAME_CURRENT_BALANCE)
  private BigDecimal currentBalance;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<CustomField> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private Object customMappings;

  public static final String SERIALIZED_NAME_DEPARTMENT = "department";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT)
  private String department;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EMAIL_DOMAIN = "email_domain";
  @SerializedName(SERIALIZED_NAME_EMAIL_DOMAIN)
  private String emailDomain;

  public static final String SERIALIZED_NAME_EMAILS = "emails";
  @SerializedName(SERIALIZED_NAME_EMAILS)
  private List<Email> emails = new ArrayList<>();

  public static final String SERIALIZED_NAME_FAX = "fax";
  @SerializedName(SERIALIZED_NAME_FAX)
  private String fax;

  public static final String SERIALIZED_NAME_FIRST_CALL_AT = "first_call_at";
  @SerializedName(SERIALIZED_NAME_FIRST_CALL_AT)
  private OffsetDateTime firstCallAt;

  public static final String SERIALIZED_NAME_FIRST_EMAIL_AT = "first_email_at";
  @SerializedName(SERIALIZED_NAME_FIRST_EMAIL_AT)
  private OffsetDateTime firstEmailAt;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  /**
   * The gender of the contact.
   */
  @JsonAdapter(GenderEnum.Adapter.class)
  public enum GenderEnum {
    MALE("male"),
    
    FEMALE("female"),
    
    UNISEX("unisex");

    private String value;

    GenderEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GenderEnum fromValue(String value) {
      for (GenderEnum b : GenderEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<GenderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GenderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GenderEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GenderEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GenderEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private GenderEnum gender;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_LAST_ACTIVITY_AT = "last_activity_at";
  @SerializedName(SERIALIZED_NAME_LAST_ACTIVITY_AT)
  private OffsetDateTime lastActivityAt;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_LEAD_ID = "lead_id";
  @SerializedName(SERIALIZED_NAME_LEAD_ID)
  private String leadId;

  public static final String SERIALIZED_NAME_LEAD_SOURCE = "lead_source";
  @SerializedName(SERIALIZED_NAME_LEAD_SOURCE)
  private String leadSource;

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

  public static final String SERIALIZED_NAME_PREFIX = "prefix";
  @SerializedName(SERIALIZED_NAME_PREFIX)
  private String prefix;

  public static final String SERIALIZED_NAME_SOCIAL_LINKS = "social_links";
  @SerializedName(SERIALIZED_NAME_SOCIAL_LINKS)
  private List<SocialLink> socialLinks = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_SUFFIX = "suffix";
  @SerializedName(SERIALIZED_NAME_SUFFIX)
  private String suffix;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  /**
   * The type of the contact.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    CUSTOMER("customer"),
    
    SUPPLIER("supplier"),
    
    EMPLOYEE("employee"),
    
    PERSONAL("personal");

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
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_WEBSITES = "websites";
  @SerializedName(SERIALIZED_NAME_WEBSITES)
  private List<Website> websites = new ArrayList<>();

  public Contact() {
  }

  public Contact(
     OffsetDateTime createdAt, 
     OffsetDateTime firstCallAt, 
     OffsetDateTime firstEmailAt, 
     String id, 
     OffsetDateTime lastActivityAt, 
     OffsetDateTime updatedAt
  ) {
    this();
    this.createdAt = createdAt;
    this.firstCallAt = firstCallAt;
    this.firstEmailAt = firstEmailAt;
    this.id = id;
    this.lastActivityAt = lastActivityAt;
    this.updatedAt = updatedAt;
  }

  public Contact active(Boolean active) {
    this.active = active;
    return this;
  }

  /**
   * The active status of the contact.
   * @return active
   */
  @javax.annotation.Nullable
  public Boolean getActive() {
    return active;
  }

  public void setActive(Boolean active) {
    this.active = active;
  }


  public Contact addresses(List<Address> addresses) {
    this.addresses = addresses;
    return this;
  }

  public Contact addAddressesItem(Address addressesItem) {
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


  public Contact birthday(String birthday) {
    this.birthday = birthday;
    return this;
  }

  /**
   * The birthday of the contact.
   * @return birthday
   */
  @javax.annotation.Nullable
  public String getBirthday() {
    return birthday;
  }

  public void setBirthday(String birthday) {
    this.birthday = birthday;
  }


  public Contact companyId(String companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * The company the contact is associated with.
   * @return companyId
   */
  @javax.annotation.Nullable
  public String getCompanyId() {
    return companyId;
  }

  public void setCompanyId(String companyId) {
    this.companyId = companyId;
  }


  public Contact companyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  /**
   * The name of the company the contact is associated with.
   * @return companyName
   */
  @javax.annotation.Nullable
  public String getCompanyName() {
    return companyName;
  }

  public void setCompanyName(String companyName) {
    this.companyName = companyName;
  }


  /**
   * The creation date of the contact.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



  public Contact currentBalance(BigDecimal currentBalance) {
    this.currentBalance = currentBalance;
    return this;
  }

  /**
   * The current balance of the contact.
   * @return currentBalance
   */
  @javax.annotation.Nullable
  public BigDecimal getCurrentBalance() {
    return currentBalance;
  }

  public void setCurrentBalance(BigDecimal currentBalance) {
    this.currentBalance = currentBalance;
  }


  public Contact customFields(List<CustomField> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Contact addCustomFieldsItem(CustomField customFieldsItem) {
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


  public Contact customMappings(Object customMappings) {
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


  public Contact department(String department) {
    this.department = department;
    return this;
  }

  /**
   * The department of the contact.
   * @return department
   */
  @javax.annotation.Nullable
  public String getDepartment() {
    return department;
  }

  public void setDepartment(String department) {
    this.department = department;
  }


  public Contact description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The description of the contact.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Contact emailDomain(String emailDomain) {
    this.emailDomain = emailDomain;
    return this;
  }

  /**
   * Get emailDomain
   * @return emailDomain
   */
  @javax.annotation.Nullable
  public String getEmailDomain() {
    return emailDomain;
  }

  public void setEmailDomain(String emailDomain) {
    this.emailDomain = emailDomain;
  }


  public Contact emails(List<Email> emails) {
    this.emails = emails;
    return this;
  }

  public Contact addEmailsItem(Email emailsItem) {
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


  public Contact fax(String fax) {
    this.fax = fax;
    return this;
  }

  /**
   * The fax number of the contact.
   * @return fax
   */
  @javax.annotation.Nullable
  public String getFax() {
    return fax;
  }

  public void setFax(String fax) {
    this.fax = fax;
  }


  /**
   * The first call date of the contact.
   * @return firstCallAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getFirstCallAt() {
    return firstCallAt;
  }



  /**
   * The first email date of the contact.
   * @return firstEmailAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getFirstEmailAt() {
    return firstEmailAt;
  }



  public Contact firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * The first name of the contact.
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public Contact gender(GenderEnum gender) {
    this.gender = gender;
    return this;
  }

  /**
   * The gender of the contact.
   * @return gender
   */
  @javax.annotation.Nullable
  public GenderEnum getGender() {
    return gender;
  }

  public void setGender(GenderEnum gender) {
    this.gender = gender;
  }


  /**
   * Unique identifier for the contact.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  @Deprecated
  public Contact image(String image) {
    this.image = image;
    return this;
  }

  /**
   * Get image
   * @return image
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getImage() {
    return image;
  }

  @Deprecated
  public void setImage(String image) {
    this.image = image;
  }


  public Contact language(String language) {
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


  /**
   * The last activity date of the contact.
   * @return lastActivityAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastActivityAt() {
    return lastActivityAt;
  }



  public Contact lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * The last name of the contact.
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public Contact leadId(String leadId) {
    this.leadId = leadId;
    return this;
  }

  /**
   * The lead the contact is associated with.
   * @return leadId
   */
  @javax.annotation.Nullable
  public String getLeadId() {
    return leadId;
  }

  public void setLeadId(String leadId) {
    this.leadId = leadId;
  }


  public Contact leadSource(String leadSource) {
    this.leadSource = leadSource;
    return this;
  }

  /**
   * The lead source of the contact.
   * @return leadSource
   */
  @javax.annotation.Nullable
  public String getLeadSource() {
    return leadSource;
  }

  public void setLeadSource(String leadSource) {
    this.leadSource = leadSource;
  }


  public Contact middleName(String middleName) {
    this.middleName = middleName;
    return this;
  }

  /**
   * The middle name of the contact.
   * @return middleName
   */
  @javax.annotation.Nullable
  public String getMiddleName() {
    return middleName;
  }

  public void setMiddleName(String middleName) {
    this.middleName = middleName;
  }


  public Contact name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Full name of the contact.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Contact ownerId(String ownerId) {
    this.ownerId = ownerId;
    return this;
  }

  /**
   * The owner of the contact.
   * @return ownerId
   */
  @javax.annotation.Nullable
  public String getOwnerId() {
    return ownerId;
  }

  public void setOwnerId(String ownerId) {
    this.ownerId = ownerId;
  }


  public Contact phoneNumbers(List<PhoneNumber> phoneNumbers) {
    this.phoneNumbers = phoneNumbers;
    return this;
  }

  public Contact addPhoneNumbersItem(PhoneNumber phoneNumbersItem) {
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


  public Contact photoUrl(String photoUrl) {
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


  public Contact prefix(String prefix) {
    this.prefix = prefix;
    return this;
  }

  /**
   * The prefix of the contact.
   * @return prefix
   */
  @javax.annotation.Nullable
  public String getPrefix() {
    return prefix;
  }

  public void setPrefix(String prefix) {
    this.prefix = prefix;
  }


  public Contact socialLinks(List<SocialLink> socialLinks) {
    this.socialLinks = socialLinks;
    return this;
  }

  public Contact addSocialLinksItem(SocialLink socialLinksItem) {
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


  public Contact status(String status) {
    this.status = status;
    return this;
  }

  /**
   * The status of the contact.
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public Contact suffix(String suffix) {
    this.suffix = suffix;
    return this;
  }

  /**
   * The suffix of the contact.
   * @return suffix
   */
  @javax.annotation.Nullable
  public String getSuffix() {
    return suffix;
  }

  public void setSuffix(String suffix) {
    this.suffix = suffix;
  }


  public Contact tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public Contact addTagsItem(String tagsItem) {
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


  public Contact title(String title) {
    this.title = title;
    return this;
  }

  /**
   * The job title of the contact.
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Contact type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The type of the contact.
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
   * The last update date of the contact.
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }



  public Contact websites(List<Website> websites) {
    this.websites = websites;
    return this;
  }

  public Contact addWebsitesItem(Website websitesItem) {
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
    Contact contact = (Contact) o;
    return Objects.equals(this.active, contact.active) &&
        Objects.equals(this.addresses, contact.addresses) &&
        Objects.equals(this.birthday, contact.birthday) &&
        Objects.equals(this.companyId, contact.companyId) &&
        Objects.equals(this.companyName, contact.companyName) &&
        Objects.equals(this.createdAt, contact.createdAt) &&
        Objects.equals(this.currentBalance, contact.currentBalance) &&
        Objects.equals(this.customFields, contact.customFields) &&
        Objects.equals(this.customMappings, contact.customMappings) &&
        Objects.equals(this.department, contact.department) &&
        Objects.equals(this.description, contact.description) &&
        Objects.equals(this.emailDomain, contact.emailDomain) &&
        Objects.equals(this.emails, contact.emails) &&
        Objects.equals(this.fax, contact.fax) &&
        Objects.equals(this.firstCallAt, contact.firstCallAt) &&
        Objects.equals(this.firstEmailAt, contact.firstEmailAt) &&
        Objects.equals(this.firstName, contact.firstName) &&
        Objects.equals(this.gender, contact.gender) &&
        Objects.equals(this.id, contact.id) &&
        Objects.equals(this.image, contact.image) &&
        Objects.equals(this.language, contact.language) &&
        Objects.equals(this.lastActivityAt, contact.lastActivityAt) &&
        Objects.equals(this.lastName, contact.lastName) &&
        Objects.equals(this.leadId, contact.leadId) &&
        Objects.equals(this.leadSource, contact.leadSource) &&
        Objects.equals(this.middleName, contact.middleName) &&
        Objects.equals(this.name, contact.name) &&
        Objects.equals(this.ownerId, contact.ownerId) &&
        Objects.equals(this.phoneNumbers, contact.phoneNumbers) &&
        Objects.equals(this.photoUrl, contact.photoUrl) &&
        Objects.equals(this.prefix, contact.prefix) &&
        Objects.equals(this.socialLinks, contact.socialLinks) &&
        Objects.equals(this.status, contact.status) &&
        Objects.equals(this.suffix, contact.suffix) &&
        Objects.equals(this.tags, contact.tags) &&
        Objects.equals(this.title, contact.title) &&
        Objects.equals(this.type, contact.type) &&
        Objects.equals(this.updatedAt, contact.updatedAt) &&
        Objects.equals(this.websites, contact.websites);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, addresses, birthday, companyId, companyName, createdAt, currentBalance, customFields, customMappings, department, description, emailDomain, emails, fax, firstCallAt, firstEmailAt, firstName, gender, id, image, language, lastActivityAt, lastName, leadId, leadSource, middleName, name, ownerId, phoneNumbers, photoUrl, prefix, socialLinks, status, suffix, tags, title, type, updatedAt, websites);
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
    sb.append("class Contact {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    addresses: ").append(toIndentedString(addresses)).append("\n");
    sb.append("    birthday: ").append(toIndentedString(birthday)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    companyName: ").append(toIndentedString(companyName)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    currentBalance: ").append(toIndentedString(currentBalance)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    department: ").append(toIndentedString(department)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    emailDomain: ").append(toIndentedString(emailDomain)).append("\n");
    sb.append("    emails: ").append(toIndentedString(emails)).append("\n");
    sb.append("    fax: ").append(toIndentedString(fax)).append("\n");
    sb.append("    firstCallAt: ").append(toIndentedString(firstCallAt)).append("\n");
    sb.append("    firstEmailAt: ").append(toIndentedString(firstEmailAt)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    lastActivityAt: ").append(toIndentedString(lastActivityAt)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    leadId: ").append(toIndentedString(leadId)).append("\n");
    sb.append("    leadSource: ").append(toIndentedString(leadSource)).append("\n");
    sb.append("    middleName: ").append(toIndentedString(middleName)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ownerId: ").append(toIndentedString(ownerId)).append("\n");
    sb.append("    phoneNumbers: ").append(toIndentedString(phoneNumbers)).append("\n");
    sb.append("    photoUrl: ").append(toIndentedString(photoUrl)).append("\n");
    sb.append("    prefix: ").append(toIndentedString(prefix)).append("\n");
    sb.append("    socialLinks: ").append(toIndentedString(socialLinks)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    suffix: ").append(toIndentedString(suffix)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("active");
    openapiFields.add("addresses");
    openapiFields.add("birthday");
    openapiFields.add("company_id");
    openapiFields.add("company_name");
    openapiFields.add("created_at");
    openapiFields.add("current_balance");
    openapiFields.add("custom_fields");
    openapiFields.add("custom_mappings");
    openapiFields.add("department");
    openapiFields.add("description");
    openapiFields.add("email_domain");
    openapiFields.add("emails");
    openapiFields.add("fax");
    openapiFields.add("first_call_at");
    openapiFields.add("first_email_at");
    openapiFields.add("first_name");
    openapiFields.add("gender");
    openapiFields.add("id");
    openapiFields.add("image");
    openapiFields.add("language");
    openapiFields.add("last_activity_at");
    openapiFields.add("last_name");
    openapiFields.add("lead_id");
    openapiFields.add("lead_source");
    openapiFields.add("middle_name");
    openapiFields.add("name");
    openapiFields.add("owner_id");
    openapiFields.add("phone_numbers");
    openapiFields.add("photo_url");
    openapiFields.add("prefix");
    openapiFields.add("social_links");
    openapiFields.add("status");
    openapiFields.add("suffix");
    openapiFields.add("tags");
    openapiFields.add("title");
    openapiFields.add("type");
    openapiFields.add("updated_at");
    openapiFields.add("websites");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Contact
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Contact.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Contact is not found in the empty JSON string", Contact.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Contact.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Contact` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Contact.openapiRequiredFields) {
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
      if ((jsonObj.get("birthday") != null && !jsonObj.get("birthday").isJsonNull()) && !jsonObj.get("birthday").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `birthday` to be a primitive type in the JSON string but got `%s`", jsonObj.get("birthday").toString()));
      }
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("company_name") != null && !jsonObj.get("company_name").isJsonNull()) && !jsonObj.get("company_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_name").toString()));
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
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("email_domain") != null && !jsonObj.get("email_domain").isJsonNull()) && !jsonObj.get("email_domain").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email_domain` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email_domain").toString()));
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
      if ((jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) && !jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      // validate the optional field `gender`
      if (jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) {
        GenderEnum.validateJsonElement(jsonObj.get("gender"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) && !jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("lead_id") != null && !jsonObj.get("lead_id").isJsonNull()) && !jsonObj.get("lead_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lead_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lead_id").toString()));
      }
      if ((jsonObj.get("lead_source") != null && !jsonObj.get("lead_source").isJsonNull()) && !jsonObj.get("lead_source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lead_source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lead_source").toString()));
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
      if ((jsonObj.get("prefix") != null && !jsonObj.get("prefix").isJsonNull()) && !jsonObj.get("prefix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `prefix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("prefix").toString()));
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
      if ((jsonObj.get("suffix") != null && !jsonObj.get("suffix").isJsonNull()) && !jsonObj.get("suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suffix").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
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
       if (!Contact.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Contact' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Contact> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Contact.class));

       return (TypeAdapter<T>) new TypeAdapter<Contact>() {
           @Override
           public void write(JsonWriter out, Contact value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Contact read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Contact given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Contact
   * @throws IOException if the JSON string is invalid with respect to Contact
   */
  public static Contact fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Contact.class);
  }

  /**
   * Convert an instance of Contact to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

