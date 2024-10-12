/*
 * Connector API
 * Welcome to the Connector API.  You can use this API to access all Connector API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import java.net.URI;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ConnectorDoc;
import org.openapitools.client.model.ConnectorEvent;
import org.openapitools.client.model.ConnectorOauthScopesInner;
import org.openapitools.client.model.ConnectorSetting;
import org.openapitools.client.model.ConnectorStatus;
import org.openapitools.client.model.ConnectorTlsSupport;
import org.openapitools.client.model.ConnectorUnifiedApisInner;
import org.openapitools.client.model.LinkedConnectorResource;
import org.openapitools.client.model.SchemaSupport;
import org.openapitools.client.model.WebhookSupport;
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
 * Connector
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:58:14.526870-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Connector {
  public static final String SERIALIZED_NAME_AUTH_ONLY = "auth_only";
  @SerializedName(SERIALIZED_NAME_AUTH_ONLY)
  private Boolean authOnly;

  /**
   * Type of authorization used by the connector
   */
  @JsonAdapter(AuthTypeEnum.Adapter.class)
  public enum AuthTypeEnum {
    OAUTH2("oauth2"),
    
    API_KEY("apiKey"),
    
    BASIC("basic"),
    
    CUSTOM("custom"),
    
    NONE("none");

    private String value;

    AuthTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AuthTypeEnum fromValue(String value) {
      for (AuthTypeEnum b : AuthTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AuthTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AuthTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AuthTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AuthTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AuthTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTH_TYPE = "auth_type";
  @SerializedName(SERIALIZED_NAME_AUTH_TYPE)
  private AuthTypeEnum authType;

  public static final String SERIALIZED_NAME_BLIND_MAPPED = "blind_mapped";
  @SerializedName(SERIALIZED_NAME_BLIND_MAPPED)
  private Boolean blindMapped;

  public static final String SERIALIZED_NAME_CONFIGURABLE_RESOURCES = "configurable_resources";
  @SerializedName(SERIALIZED_NAME_CONFIGURABLE_RESOURCES)
  private List<String> configurableResources = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_SCOPES = "custom_scopes";
  @SerializedName(SERIALIZED_NAME_CUSTOM_SCOPES)
  private Boolean customScopes;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DOCS = "docs";
  @SerializedName(SERIALIZED_NAME_DOCS)
  private List<ConnectorDoc> docs = new ArrayList<>();

  public static final String SERIALIZED_NAME_FREE_TRIAL_AVAILABLE = "free_trial_available";
  @SerializedName(SERIALIZED_NAME_FREE_TRIAL_AVAILABLE)
  private Boolean freeTrialAvailable;

  public static final String SERIALIZED_NAME_HAS_SANDBOX_CREDENTIALS = "has_sandbox_credentials";
  @SerializedName(SERIALIZED_NAME_HAS_SANDBOX_CREDENTIALS)
  private Boolean hasSandboxCredentials;

  public static final String SERIALIZED_NAME_ICON_URL = "icon_url";
  @SerializedName(SERIALIZED_NAME_ICON_URL)
  private URI iconUrl;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LOGO_URL = "logo_url";
  @SerializedName(SERIALIZED_NAME_LOGO_URL)
  private URI logoUrl;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.
   */
  @JsonAdapter(OauthCredentialsSourceEnum.Adapter.class)
  public enum OauthCredentialsSourceEnum {
    INTEGRATION("integration"),
    
    CONNECTION("connection");

    private String value;

    OauthCredentialsSourceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OauthCredentialsSourceEnum fromValue(String value) {
      for (OauthCredentialsSourceEnum b : OauthCredentialsSourceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OauthCredentialsSourceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OauthCredentialsSourceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OauthCredentialsSourceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OauthCredentialsSourceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OauthCredentialsSourceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_OAUTH_CREDENTIALS_SOURCE = "oauth_credentials_source";
  @SerializedName(SERIALIZED_NAME_OAUTH_CREDENTIALS_SOURCE)
  private OauthCredentialsSourceEnum oauthCredentialsSource;

  /**
   * OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types
   */
  @JsonAdapter(OauthGrantTypeEnum.Adapter.class)
  public enum OauthGrantTypeEnum {
    AUTHORIZATION_CODE("authorization_code"),
    
    CLIENT_CREDENTIALS("client_credentials"),
    
    PASSWORD("password");

    private String value;

    OauthGrantTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OauthGrantTypeEnum fromValue(String value) {
      for (OauthGrantTypeEnum b : OauthGrantTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OauthGrantTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OauthGrantTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OauthGrantTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OauthGrantTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OauthGrantTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_OAUTH_GRANT_TYPE = "oauth_grant_type";
  @SerializedName(SERIALIZED_NAME_OAUTH_GRANT_TYPE)
  private OauthGrantTypeEnum oauthGrantType;

  public static final String SERIALIZED_NAME_OAUTH_SCOPES = "oauth_scopes";
  @SerializedName(SERIALIZED_NAME_OAUTH_SCOPES)
  private List<ConnectorOauthScopesInner> oauthScopes = new ArrayList<>();

  public static final String SERIALIZED_NAME_PARTNER_SIGNUP_URL = "partner_signup_url";
  @SerializedName(SERIALIZED_NAME_PARTNER_SIGNUP_URL)
  private URI partnerSignupUrl;

  public static final String SERIALIZED_NAME_SCHEMA_SUPPORT = "schema_support";
  @SerializedName(SERIALIZED_NAME_SCHEMA_SUPPORT)
  private SchemaSupport schemaSupport;

  public static final String SERIALIZED_NAME_SERVICE_ID = "service_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_ID)
  private String serviceId;

  public static final String SERIALIZED_NAME_SETTINGS = "settings";
  @SerializedName(SERIALIZED_NAME_SETTINGS)
  private List<ConnectorSetting> settings = new ArrayList<>();

  public static final String SERIALIZED_NAME_SIGNUP_URL = "signup_url";
  @SerializedName(SERIALIZED_NAME_SIGNUP_URL)
  private URI signupUrl;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private ConnectorStatus status;

  public static final String SERIALIZED_NAME_SUPPORTED_EVENTS = "supported_events";
  @SerializedName(SERIALIZED_NAME_SUPPORTED_EVENTS)
  private List<ConnectorEvent> supportedEvents = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUPPORTED_RESOURCES = "supported_resources";
  @SerializedName(SERIALIZED_NAME_SUPPORTED_RESOURCES)
  private List<LinkedConnectorResource> supportedResources = new ArrayList<>();

  public static final String SERIALIZED_NAME_TLS_SUPPORT = "tls_support";
  @SerializedName(SERIALIZED_NAME_TLS_SUPPORT)
  private ConnectorTlsSupport tlsSupport;

  public static final String SERIALIZED_NAME_UNIFIED_APIS = "unified_apis";
  @SerializedName(SERIALIZED_NAME_UNIFIED_APIS)
  private List<ConnectorUnifiedApisInner> unifiedApis = new ArrayList<>();

  public static final String SERIALIZED_NAME_WEBHOOK_SUPPORT = "webhook_support";
  @SerializedName(SERIALIZED_NAME_WEBHOOK_SUPPORT)
  private WebhookSupport webhookSupport;

  public static final String SERIALIZED_NAME_WEBSITE_URL = "website_url";
  @SerializedName(SERIALIZED_NAME_WEBSITE_URL)
  private URI websiteUrl;

  public Connector() {
  }

  public Connector(
     Boolean authOnly, 
     AuthTypeEnum authType, 
     Boolean blindMapped, 
     Boolean customScopes, 
     String id, 
     OauthCredentialsSourceEnum oauthCredentialsSource, 
     OauthGrantTypeEnum oauthGrantType
  ) {
    this();
    this.authOnly = authOnly;
    this.authType = authType;
    this.blindMapped = blindMapped;
    this.customScopes = customScopes;
    this.id = id;
    this.oauthCredentialsSource = oauthCredentialsSource;
    this.oauthGrantType = oauthGrantType;
  }

  /**
   * Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API
   * @return authOnly
   */
  @javax.annotation.Nullable
  public Boolean getAuthOnly() {
    return authOnly;
  }



  /**
   * Type of authorization used by the connector
   * @return authType
   */
  @javax.annotation.Nullable
  public AuthTypeEnum getAuthType() {
    return authType;
  }



  /**
   * Set to &#x60;true&#x60; when connector was implemented from downstream docs only and without API access. This state indicates that integration will require Apideck support, and access to downstream API to validate mapping quality.
   * @return blindMapped
   */
  @javax.annotation.Nullable
  public Boolean getBlindMapped() {
    return blindMapped;
  }



  public Connector configurableResources(List<String> configurableResources) {
    this.configurableResources = configurableResources;
    return this;
  }

  public Connector addConfigurableResourcesItem(String configurableResourcesItem) {
    if (this.configurableResources == null) {
      this.configurableResources = new ArrayList<>();
    }
    this.configurableResources.add(configurableResourcesItem);
    return this;
  }

  /**
   * List of resources that have settings that can be configured.
   * @return configurableResources
   */
  @javax.annotation.Nullable
  public List<String> getConfigurableResources() {
    return configurableResources;
  }

  public void setConfigurableResources(List<String> configurableResources) {
    this.configurableResources = configurableResources;
  }


  /**
   * Set to &#x60;true&#x60; when connector allows the definition of custom scopes.
   * @return customScopes
   */
  @javax.annotation.Nullable
  public Boolean getCustomScopes() {
    return customScopes;
  }



  public Connector description(String description) {
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


  public Connector docs(List<ConnectorDoc> docs) {
    this.docs = docs;
    return this;
  }

  public Connector addDocsItem(ConnectorDoc docsItem) {
    if (this.docs == null) {
      this.docs = new ArrayList<>();
    }
    this.docs.add(docsItem);
    return this;
  }

  /**
   * Get docs
   * @return docs
   */
  @javax.annotation.Nullable
  public List<ConnectorDoc> getDocs() {
    return docs;
  }

  public void setDocs(List<ConnectorDoc> docs) {
    this.docs = docs;
  }


  public Connector freeTrialAvailable(Boolean freeTrialAvailable) {
    this.freeTrialAvailable = freeTrialAvailable;
    return this;
  }

  /**
   * Set to &#x60;true&#x60; when the connector offers a free trial. Use &#x60;signup_url&#x60; to sign up for a free trial
   * @return freeTrialAvailable
   */
  @javax.annotation.Nullable
  public Boolean getFreeTrialAvailable() {
    return freeTrialAvailable;
  }

  public void setFreeTrialAvailable(Boolean freeTrialAvailable) {
    this.freeTrialAvailable = freeTrialAvailable;
  }


  public Connector hasSandboxCredentials(Boolean hasSandboxCredentials) {
    this.hasSandboxCredentials = hasSandboxCredentials;
    return this;
  }

  /**
   * Indicates whether Apideck Sandbox OAuth credentials are available.
   * @return hasSandboxCredentials
   */
  @javax.annotation.Nullable
  public Boolean getHasSandboxCredentials() {
    return hasSandboxCredentials;
  }

  public void setHasSandboxCredentials(Boolean hasSandboxCredentials) {
    this.hasSandboxCredentials = hasSandboxCredentials;
  }


  public Connector iconUrl(URI iconUrl) {
    this.iconUrl = iconUrl;
    return this;
  }

  /**
   * Link to a small square icon for the connector.
   * @return iconUrl
   */
  @javax.annotation.Nullable
  public URI getIconUrl() {
    return iconUrl;
  }

  public void setIconUrl(URI iconUrl) {
    this.iconUrl = iconUrl;
  }


  /**
   * ID of the connector.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Connector logoUrl(URI logoUrl) {
    this.logoUrl = logoUrl;
    return this;
  }

  /**
   * Link to the full logo for the connector.
   * @return logoUrl
   */
  @javax.annotation.Nullable
  public URI getLogoUrl() {
    return logoUrl;
  }

  public void setLogoUrl(URI logoUrl) {
    this.logoUrl = logoUrl;
  }


  public Connector name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the connector.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  /**
   * Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.
   * @return oauthCredentialsSource
   */
  @javax.annotation.Nullable
  public OauthCredentialsSourceEnum getOauthCredentialsSource() {
    return oauthCredentialsSource;
  }



  /**
   * OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types
   * @return oauthGrantType
   */
  @javax.annotation.Nullable
  public OauthGrantTypeEnum getOauthGrantType() {
    return oauthGrantType;
  }



  public Connector oauthScopes(List<ConnectorOauthScopesInner> oauthScopes) {
    this.oauthScopes = oauthScopes;
    return this;
  }

  public Connector addOauthScopesItem(ConnectorOauthScopesInner oauthScopesItem) {
    if (this.oauthScopes == null) {
      this.oauthScopes = new ArrayList<>();
    }
    this.oauthScopes.add(oauthScopesItem);
    return this;
  }

  /**
   * List of OAuth Scopes available for this connector.
   * @return oauthScopes
   */
  @javax.annotation.Nullable
  public List<ConnectorOauthScopesInner> getOauthScopes() {
    return oauthScopes;
  }

  public void setOauthScopes(List<ConnectorOauthScopesInner> oauthScopes) {
    this.oauthScopes = oauthScopes;
  }


  public Connector partnerSignupUrl(URI partnerSignupUrl) {
    this.partnerSignupUrl = partnerSignupUrl;
    return this;
  }

  /**
   * Link to the connector&#39;s partner program signup page.
   * @return partnerSignupUrl
   */
  @javax.annotation.Nullable
  public URI getPartnerSignupUrl() {
    return partnerSignupUrl;
  }

  public void setPartnerSignupUrl(URI partnerSignupUrl) {
    this.partnerSignupUrl = partnerSignupUrl;
  }


  public Connector schemaSupport(SchemaSupport schemaSupport) {
    this.schemaSupport = schemaSupport;
    return this;
  }

  /**
   * Get schemaSupport
   * @return schemaSupport
   */
  @javax.annotation.Nullable
  public SchemaSupport getSchemaSupport() {
    return schemaSupport;
  }

  public void setSchemaSupport(SchemaSupport schemaSupport) {
    this.schemaSupport = schemaSupport;
  }


  public Connector serviceId(String serviceId) {
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


  public Connector settings(List<ConnectorSetting> settings) {
    this.settings = settings;
    return this;
  }

  public Connector addSettingsItem(ConnectorSetting settingsItem) {
    if (this.settings == null) {
      this.settings = new ArrayList<>();
    }
    this.settings.add(settingsItem);
    return this;
  }

  /**
   * Get settings
   * @return settings
   */
  @javax.annotation.Nullable
  public List<ConnectorSetting> getSettings() {
    return settings;
  }

  public void setSettings(List<ConnectorSetting> settings) {
    this.settings = settings;
  }


  public Connector signupUrl(URI signupUrl) {
    this.signupUrl = signupUrl;
    return this;
  }

  /**
   * Link to the connector&#39;s signup page.
   * @return signupUrl
   */
  @javax.annotation.Nullable
  public URI getSignupUrl() {
    return signupUrl;
  }

  public void setSignupUrl(URI signupUrl) {
    this.signupUrl = signupUrl;
  }


  public Connector status(ConnectorStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public ConnectorStatus getStatus() {
    return status;
  }

  public void setStatus(ConnectorStatus status) {
    this.status = status;
  }


  public Connector supportedEvents(List<ConnectorEvent> supportedEvents) {
    this.supportedEvents = supportedEvents;
    return this;
  }

  public Connector addSupportedEventsItem(ConnectorEvent supportedEventsItem) {
    if (this.supportedEvents == null) {
      this.supportedEvents = new ArrayList<>();
    }
    this.supportedEvents.add(supportedEventsItem);
    return this;
  }

  /**
   * List of events that are supported on the connector across all Unified APIs.
   * @return supportedEvents
   */
  @javax.annotation.Nullable
  public List<ConnectorEvent> getSupportedEvents() {
    return supportedEvents;
  }

  public void setSupportedEvents(List<ConnectorEvent> supportedEvents) {
    this.supportedEvents = supportedEvents;
  }


  public Connector supportedResources(List<LinkedConnectorResource> supportedResources) {
    this.supportedResources = supportedResources;
    return this;
  }

  public Connector addSupportedResourcesItem(LinkedConnectorResource supportedResourcesItem) {
    if (this.supportedResources == null) {
      this.supportedResources = new ArrayList<>();
    }
    this.supportedResources.add(supportedResourcesItem);
    return this;
  }

  /**
   * List of resources that are supported on the connector.
   * @return supportedResources
   */
  @javax.annotation.Nullable
  public List<LinkedConnectorResource> getSupportedResources() {
    return supportedResources;
  }

  public void setSupportedResources(List<LinkedConnectorResource> supportedResources) {
    this.supportedResources = supportedResources;
  }


  public Connector tlsSupport(ConnectorTlsSupport tlsSupport) {
    this.tlsSupport = tlsSupport;
    return this;
  }

  /**
   * Get tlsSupport
   * @return tlsSupport
   */
  @javax.annotation.Nullable
  public ConnectorTlsSupport getTlsSupport() {
    return tlsSupport;
  }

  public void setTlsSupport(ConnectorTlsSupport tlsSupport) {
    this.tlsSupport = tlsSupport;
  }


  public Connector unifiedApis(List<ConnectorUnifiedApisInner> unifiedApis) {
    this.unifiedApis = unifiedApis;
    return this;
  }

  public Connector addUnifiedApisItem(ConnectorUnifiedApisInner unifiedApisItem) {
    if (this.unifiedApis == null) {
      this.unifiedApis = new ArrayList<>();
    }
    this.unifiedApis.add(unifiedApisItem);
    return this;
  }

  /**
   * List of Unified APIs that feature this connector.
   * @return unifiedApis
   */
  @javax.annotation.Nullable
  public List<ConnectorUnifiedApisInner> getUnifiedApis() {
    return unifiedApis;
  }

  public void setUnifiedApis(List<ConnectorUnifiedApisInner> unifiedApis) {
    this.unifiedApis = unifiedApis;
  }


  public Connector webhookSupport(WebhookSupport webhookSupport) {
    this.webhookSupport = webhookSupport;
    return this;
  }

  /**
   * Get webhookSupport
   * @return webhookSupport
   */
  @javax.annotation.Nullable
  public WebhookSupport getWebhookSupport() {
    return webhookSupport;
  }

  public void setWebhookSupport(WebhookSupport webhookSupport) {
    this.webhookSupport = webhookSupport;
  }


  public Connector websiteUrl(URI websiteUrl) {
    this.websiteUrl = websiteUrl;
    return this;
  }

  /**
   * Link to the connector&#39;s website.
   * @return websiteUrl
   */
  @javax.annotation.Nullable
  public URI getWebsiteUrl() {
    return websiteUrl;
  }

  public void setWebsiteUrl(URI websiteUrl) {
    this.websiteUrl = websiteUrl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Connector connector = (Connector) o;
    return Objects.equals(this.authOnly, connector.authOnly) &&
        Objects.equals(this.authType, connector.authType) &&
        Objects.equals(this.blindMapped, connector.blindMapped) &&
        Objects.equals(this.configurableResources, connector.configurableResources) &&
        Objects.equals(this.customScopes, connector.customScopes) &&
        Objects.equals(this.description, connector.description) &&
        Objects.equals(this.docs, connector.docs) &&
        Objects.equals(this.freeTrialAvailable, connector.freeTrialAvailable) &&
        Objects.equals(this.hasSandboxCredentials, connector.hasSandboxCredentials) &&
        Objects.equals(this.iconUrl, connector.iconUrl) &&
        Objects.equals(this.id, connector.id) &&
        Objects.equals(this.logoUrl, connector.logoUrl) &&
        Objects.equals(this.name, connector.name) &&
        Objects.equals(this.oauthCredentialsSource, connector.oauthCredentialsSource) &&
        Objects.equals(this.oauthGrantType, connector.oauthGrantType) &&
        Objects.equals(this.oauthScopes, connector.oauthScopes) &&
        Objects.equals(this.partnerSignupUrl, connector.partnerSignupUrl) &&
        Objects.equals(this.schemaSupport, connector.schemaSupport) &&
        Objects.equals(this.serviceId, connector.serviceId) &&
        Objects.equals(this.settings, connector.settings) &&
        Objects.equals(this.signupUrl, connector.signupUrl) &&
        Objects.equals(this.status, connector.status) &&
        Objects.equals(this.supportedEvents, connector.supportedEvents) &&
        Objects.equals(this.supportedResources, connector.supportedResources) &&
        Objects.equals(this.tlsSupport, connector.tlsSupport) &&
        Objects.equals(this.unifiedApis, connector.unifiedApis) &&
        Objects.equals(this.webhookSupport, connector.webhookSupport) &&
        Objects.equals(this.websiteUrl, connector.websiteUrl);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(authOnly, authType, blindMapped, configurableResources, customScopes, description, docs, freeTrialAvailable, hasSandboxCredentials, iconUrl, id, logoUrl, name, oauthCredentialsSource, oauthGrantType, oauthScopes, partnerSignupUrl, schemaSupport, serviceId, settings, signupUrl, status, supportedEvents, supportedResources, tlsSupport, unifiedApis, webhookSupport, websiteUrl);
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
    sb.append("class Connector {\n");
    sb.append("    authOnly: ").append(toIndentedString(authOnly)).append("\n");
    sb.append("    authType: ").append(toIndentedString(authType)).append("\n");
    sb.append("    blindMapped: ").append(toIndentedString(blindMapped)).append("\n");
    sb.append("    configurableResources: ").append(toIndentedString(configurableResources)).append("\n");
    sb.append("    customScopes: ").append(toIndentedString(customScopes)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    docs: ").append(toIndentedString(docs)).append("\n");
    sb.append("    freeTrialAvailable: ").append(toIndentedString(freeTrialAvailable)).append("\n");
    sb.append("    hasSandboxCredentials: ").append(toIndentedString(hasSandboxCredentials)).append("\n");
    sb.append("    iconUrl: ").append(toIndentedString(iconUrl)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    logoUrl: ").append(toIndentedString(logoUrl)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    oauthCredentialsSource: ").append(toIndentedString(oauthCredentialsSource)).append("\n");
    sb.append("    oauthGrantType: ").append(toIndentedString(oauthGrantType)).append("\n");
    sb.append("    oauthScopes: ").append(toIndentedString(oauthScopes)).append("\n");
    sb.append("    partnerSignupUrl: ").append(toIndentedString(partnerSignupUrl)).append("\n");
    sb.append("    schemaSupport: ").append(toIndentedString(schemaSupport)).append("\n");
    sb.append("    serviceId: ").append(toIndentedString(serviceId)).append("\n");
    sb.append("    settings: ").append(toIndentedString(settings)).append("\n");
    sb.append("    signupUrl: ").append(toIndentedString(signupUrl)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    supportedEvents: ").append(toIndentedString(supportedEvents)).append("\n");
    sb.append("    supportedResources: ").append(toIndentedString(supportedResources)).append("\n");
    sb.append("    tlsSupport: ").append(toIndentedString(tlsSupport)).append("\n");
    sb.append("    unifiedApis: ").append(toIndentedString(unifiedApis)).append("\n");
    sb.append("    webhookSupport: ").append(toIndentedString(webhookSupport)).append("\n");
    sb.append("    websiteUrl: ").append(toIndentedString(websiteUrl)).append("\n");
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
    openapiFields.add("auth_only");
    openapiFields.add("auth_type");
    openapiFields.add("blind_mapped");
    openapiFields.add("configurable_resources");
    openapiFields.add("custom_scopes");
    openapiFields.add("description");
    openapiFields.add("docs");
    openapiFields.add("free_trial_available");
    openapiFields.add("has_sandbox_credentials");
    openapiFields.add("icon_url");
    openapiFields.add("id");
    openapiFields.add("logo_url");
    openapiFields.add("name");
    openapiFields.add("oauth_credentials_source");
    openapiFields.add("oauth_grant_type");
    openapiFields.add("oauth_scopes");
    openapiFields.add("partner_signup_url");
    openapiFields.add("schema_support");
    openapiFields.add("service_id");
    openapiFields.add("settings");
    openapiFields.add("signup_url");
    openapiFields.add("status");
    openapiFields.add("supported_events");
    openapiFields.add("supported_resources");
    openapiFields.add("tls_support");
    openapiFields.add("unified_apis");
    openapiFields.add("webhook_support");
    openapiFields.add("website_url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Connector
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Connector.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Connector is not found in the empty JSON string", Connector.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Connector.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Connector` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("auth_type") != null && !jsonObj.get("auth_type").isJsonNull()) && !jsonObj.get("auth_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auth_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auth_type").toString()));
      }
      // validate the optional field `auth_type`
      if (jsonObj.get("auth_type") != null && !jsonObj.get("auth_type").isJsonNull()) {
        AuthTypeEnum.validateJsonElement(jsonObj.get("auth_type"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("configurable_resources") != null && !jsonObj.get("configurable_resources").isJsonNull() && !jsonObj.get("configurable_resources").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `configurable_resources` to be an array in the JSON string but got `%s`", jsonObj.get("configurable_resources").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("docs") != null && !jsonObj.get("docs").isJsonNull()) {
        JsonArray jsonArraydocs = jsonObj.getAsJsonArray("docs");
        if (jsonArraydocs != null) {
          // ensure the json data is an array
          if (!jsonObj.get("docs").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `docs` to be an array in the JSON string but got `%s`", jsonObj.get("docs").toString()));
          }

          // validate the optional field `docs` (array)
          for (int i = 0; i < jsonArraydocs.size(); i++) {
            ConnectorDoc.validateJsonElement(jsonArraydocs.get(i));
          };
        }
      }
      if ((jsonObj.get("icon_url") != null && !jsonObj.get("icon_url").isJsonNull()) && !jsonObj.get("icon_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon_url").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("logo_url") != null && !jsonObj.get("logo_url").isJsonNull()) && !jsonObj.get("logo_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `logo_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("logo_url").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("oauth_credentials_source") != null && !jsonObj.get("oauth_credentials_source").isJsonNull()) && !jsonObj.get("oauth_credentials_source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `oauth_credentials_source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("oauth_credentials_source").toString()));
      }
      // validate the optional field `oauth_credentials_source`
      if (jsonObj.get("oauth_credentials_source") != null && !jsonObj.get("oauth_credentials_source").isJsonNull()) {
        OauthCredentialsSourceEnum.validateJsonElement(jsonObj.get("oauth_credentials_source"));
      }
      if ((jsonObj.get("oauth_grant_type") != null && !jsonObj.get("oauth_grant_type").isJsonNull()) && !jsonObj.get("oauth_grant_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `oauth_grant_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("oauth_grant_type").toString()));
      }
      // validate the optional field `oauth_grant_type`
      if (jsonObj.get("oauth_grant_type") != null && !jsonObj.get("oauth_grant_type").isJsonNull()) {
        OauthGrantTypeEnum.validateJsonElement(jsonObj.get("oauth_grant_type"));
      }
      if (jsonObj.get("oauth_scopes") != null && !jsonObj.get("oauth_scopes").isJsonNull()) {
        JsonArray jsonArrayoauthScopes = jsonObj.getAsJsonArray("oauth_scopes");
        if (jsonArrayoauthScopes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("oauth_scopes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `oauth_scopes` to be an array in the JSON string but got `%s`", jsonObj.get("oauth_scopes").toString()));
          }

          // validate the optional field `oauth_scopes` (array)
          for (int i = 0; i < jsonArrayoauthScopes.size(); i++) {
            ConnectorOauthScopesInner.validateJsonElement(jsonArrayoauthScopes.get(i));
          };
        }
      }
      if ((jsonObj.get("partner_signup_url") != null && !jsonObj.get("partner_signup_url").isJsonNull()) && !jsonObj.get("partner_signup_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `partner_signup_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("partner_signup_url").toString()));
      }
      // validate the optional field `schema_support`
      if (jsonObj.get("schema_support") != null && !jsonObj.get("schema_support").isJsonNull()) {
        SchemaSupport.validateJsonElement(jsonObj.get("schema_support"));
      }
      if ((jsonObj.get("service_id") != null && !jsonObj.get("service_id").isJsonNull()) && !jsonObj.get("service_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_id").toString()));
      }
      if (jsonObj.get("settings") != null && !jsonObj.get("settings").isJsonNull()) {
        JsonArray jsonArraysettings = jsonObj.getAsJsonArray("settings");
        if (jsonArraysettings != null) {
          // ensure the json data is an array
          if (!jsonObj.get("settings").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `settings` to be an array in the JSON string but got `%s`", jsonObj.get("settings").toString()));
          }

          // validate the optional field `settings` (array)
          for (int i = 0; i < jsonArraysettings.size(); i++) {
            ConnectorSetting.validateJsonElement(jsonArraysettings.get(i));
          };
        }
      }
      if ((jsonObj.get("signup_url") != null && !jsonObj.get("signup_url").isJsonNull()) && !jsonObj.get("signup_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `signup_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("signup_url").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        ConnectorStatus.validateJsonElement(jsonObj.get("status"));
      }
      if (jsonObj.get("supported_events") != null && !jsonObj.get("supported_events").isJsonNull()) {
        JsonArray jsonArraysupportedEvents = jsonObj.getAsJsonArray("supported_events");
        if (jsonArraysupportedEvents != null) {
          // ensure the json data is an array
          if (!jsonObj.get("supported_events").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `supported_events` to be an array in the JSON string but got `%s`", jsonObj.get("supported_events").toString()));
          }

          // validate the optional field `supported_events` (array)
          for (int i = 0; i < jsonArraysupportedEvents.size(); i++) {
            ConnectorEvent.validateJsonElement(jsonArraysupportedEvents.get(i));
          };
        }
      }
      if (jsonObj.get("supported_resources") != null && !jsonObj.get("supported_resources").isJsonNull()) {
        JsonArray jsonArraysupportedResources = jsonObj.getAsJsonArray("supported_resources");
        if (jsonArraysupportedResources != null) {
          // ensure the json data is an array
          if (!jsonObj.get("supported_resources").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `supported_resources` to be an array in the JSON string but got `%s`", jsonObj.get("supported_resources").toString()));
          }

          // validate the optional field `supported_resources` (array)
          for (int i = 0; i < jsonArraysupportedResources.size(); i++) {
            LinkedConnectorResource.validateJsonElement(jsonArraysupportedResources.get(i));
          };
        }
      }
      // validate the optional field `tls_support`
      if (jsonObj.get("tls_support") != null && !jsonObj.get("tls_support").isJsonNull()) {
        ConnectorTlsSupport.validateJsonElement(jsonObj.get("tls_support"));
      }
      if (jsonObj.get("unified_apis") != null && !jsonObj.get("unified_apis").isJsonNull()) {
        JsonArray jsonArrayunifiedApis = jsonObj.getAsJsonArray("unified_apis");
        if (jsonArrayunifiedApis != null) {
          // ensure the json data is an array
          if (!jsonObj.get("unified_apis").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `unified_apis` to be an array in the JSON string but got `%s`", jsonObj.get("unified_apis").toString()));
          }

          // validate the optional field `unified_apis` (array)
          for (int i = 0; i < jsonArrayunifiedApis.size(); i++) {
            ConnectorUnifiedApisInner.validateJsonElement(jsonArrayunifiedApis.get(i));
          };
        }
      }
      // validate the optional field `webhook_support`
      if (jsonObj.get("webhook_support") != null && !jsonObj.get("webhook_support").isJsonNull()) {
        WebhookSupport.validateJsonElement(jsonObj.get("webhook_support"));
      }
      if ((jsonObj.get("website_url") != null && !jsonObj.get("website_url").isJsonNull()) && !jsonObj.get("website_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `website_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("website_url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Connector.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Connector' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Connector> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Connector.class));

       return (TypeAdapter<T>) new TypeAdapter<Connector>() {
           @Override
           public void write(JsonWriter out, Connector value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Connector read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Connector given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Connector
   * @throws IOException if the JSON string is invalid with respect to Connector
   */
  public static Connector fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Connector.class);
  }

  /**
   * Convert an instance of Connector to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

