/*
 * Vault API
 * Welcome to the Vault API 👋  When you're looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  ``` curl -X POST https://unify.apideck.com/vault/sessions     -H \"Content-Type: application/json\"     -H \"Authorization: Bearer <your-api-key>\"     -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"     -H \"X-APIDECK-APP-ID: <application-id>\"     -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}' ```  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.  This is being handled by the `/authorize` endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  
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
import org.openapitools.client.model.LogOperation;
import org.openapitools.client.model.LogService;
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
 * Log
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:50.743494-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Log {
  public static final String SERIALIZED_NAME_API_STYLE = "api_style";
  @SerializedName(SERIALIZED_NAME_API_STYLE)
  private String apiStyle;

  public static final String SERIALIZED_NAME_BASE_URL = "base_url";
  @SerializedName(SERIALIZED_NAME_BASE_URL)
  private String baseUrl;

  public static final String SERIALIZED_NAME_CHILD_REQUEST = "child_request";
  @SerializedName(SERIALIZED_NAME_CHILD_REQUEST)
  private Boolean childRequest;

  public static final String SERIALIZED_NAME_CONSUMER_ID = "consumer_id";
  @SerializedName(SERIALIZED_NAME_CONSUMER_ID)
  private String consumerId;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private BigDecimal duration;

  public static final String SERIALIZED_NAME_ERROR_MESSAGE = "error_message";
  @SerializedName(SERIALIZED_NAME_ERROR_MESSAGE)
  private String errorMessage;

  public static final String SERIALIZED_NAME_EXECUTION = "execution";
  @SerializedName(SERIALIZED_NAME_EXECUTION)
  private Integer execution;

  public static final String SERIALIZED_NAME_HAS_CHILDREN = "has_children";
  @SerializedName(SERIALIZED_NAME_HAS_CHILDREN)
  private Boolean hasChildren;

  public static final String SERIALIZED_NAME_HTTP_METHOD = "http_method";
  @SerializedName(SERIALIZED_NAME_HTTP_METHOD)
  private String httpMethod;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LATENCY = "latency";
  @SerializedName(SERIALIZED_NAME_LATENCY)
  private BigDecimal latency;

  public static final String SERIALIZED_NAME_OPERATION = "operation";
  @SerializedName(SERIALIZED_NAME_OPERATION)
  private LogOperation operation;

  public static final String SERIALIZED_NAME_PARENT_ID = "parent_id";
  @SerializedName(SERIALIZED_NAME_PARENT_ID)
  private String parentId;

  public static final String SERIALIZED_NAME_PATH = "path";
  @SerializedName(SERIALIZED_NAME_PATH)
  private String path;

  public static final String SERIALIZED_NAME_SANDBOX = "sandbox";
  @SerializedName(SERIALIZED_NAME_SANDBOX)
  private Boolean sandbox;

  public static final String SERIALIZED_NAME_SERVICE = "service";
  @SerializedName(SERIALIZED_NAME_SERVICE)
  private LogService service;

  public static final String SERIALIZED_NAME_SOURCE_IP = "source_ip";
  @SerializedName(SERIALIZED_NAME_SOURCE_IP)
  private String sourceIp;

  public static final String SERIALIZED_NAME_STATUS_CODE = "status_code";
  @SerializedName(SERIALIZED_NAME_STATUS_CODE)
  private Integer statusCode;

  public static final String SERIALIZED_NAME_SUCCESS = "success";
  @SerializedName(SERIALIZED_NAME_SUCCESS)
  private Boolean success;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private String timestamp;

  /**
   * Which Unified Api request was made to.
   */
  @JsonAdapter(UnifiedApiEnum.Adapter.class)
  public enum UnifiedApiEnum {
    CRM("crm"),
    
    LEAD("lead"),
    
    PROXY("proxy"),
    
    VAULT("vault"),
    
    ACCOUNTING("accounting"),
    
    HRIS("hris"),
    
    ATS("ats"),
    
    ECOMMERCE("ecommerce"),
    
    ISSUE_TRACKING("issue-tracking"),
    
    POS("pos"),
    
    FILE_STORAGE("file-storage"),
    
    SMS("sms");

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

  public Log() {
  }

  public Log apiStyle(String apiStyle) {
    this.apiStyle = apiStyle;
    return this;
  }

  /**
   * Indicates if the request was made via REST or Graphql endpoint.
   * @return apiStyle
   */
  @javax.annotation.Nonnull
  public String getApiStyle() {
    return apiStyle;
  }

  public void setApiStyle(String apiStyle) {
    this.apiStyle = apiStyle;
  }


  public Log baseUrl(String baseUrl) {
    this.baseUrl = baseUrl;
    return this;
  }

  /**
   * The Apideck base URL the request was made to.
   * @return baseUrl
   */
  @javax.annotation.Nonnull
  public String getBaseUrl() {
    return baseUrl;
  }

  public void setBaseUrl(String baseUrl) {
    this.baseUrl = baseUrl;
  }


  public Log childRequest(Boolean childRequest) {
    this.childRequest = childRequest;
    return this;
  }

  /**
   * Indicates whether or not this is a child or parent request.
   * @return childRequest
   */
  @javax.annotation.Nonnull
  public Boolean getChildRequest() {
    return childRequest;
  }

  public void setChildRequest(Boolean childRequest) {
    this.childRequest = childRequest;
  }


  public Log consumerId(String consumerId) {
    this.consumerId = consumerId;
    return this;
  }

  /**
   * The consumer Id associated with the request.
   * @return consumerId
   */
  @javax.annotation.Nonnull
  public String getConsumerId() {
    return consumerId;
  }

  public void setConsumerId(String consumerId) {
    this.consumerId = consumerId;
  }


  public Log duration(BigDecimal duration) {
    this.duration = duration;
    return this;
  }

  /**
   * The entire execution time in milliseconds it took to call the Apideck service provider.
   * @return duration
   */
  @javax.annotation.Nonnull
  public BigDecimal getDuration() {
    return duration;
  }

  public void setDuration(BigDecimal duration) {
    this.duration = duration;
  }


  public Log errorMessage(String errorMessage) {
    this.errorMessage = errorMessage;
    return this;
  }

  /**
   * If error occurred, this is brief explanation
   * @return errorMessage
   */
  @javax.annotation.Nullable
  public String getErrorMessage() {
    return errorMessage;
  }

  public void setErrorMessage(String errorMessage) {
    this.errorMessage = errorMessage;
  }


  public Log execution(Integer execution) {
    this.execution = execution;
    return this;
  }

  /**
   * The entire execution time in milliseconds it took to make the request.
   * @return execution
   */
  @javax.annotation.Nonnull
  public Integer getExecution() {
    return execution;
  }

  public void setExecution(Integer execution) {
    this.execution = execution;
  }


  public Log hasChildren(Boolean hasChildren) {
    this.hasChildren = hasChildren;
    return this;
  }

  /**
   * When request is a parent request, this indicates if there are child requests associated.
   * @return hasChildren
   */
  @javax.annotation.Nonnull
  public Boolean getHasChildren() {
    return hasChildren;
  }

  public void setHasChildren(Boolean hasChildren) {
    this.hasChildren = hasChildren;
  }


  public Log httpMethod(String httpMethod) {
    this.httpMethod = httpMethod;
    return this;
  }

  /**
   * HTTP Method of request.
   * @return httpMethod
   */
  @javax.annotation.Nonnull
  public String getHttpMethod() {
    return httpMethod;
  }

  public void setHttpMethod(String httpMethod) {
    this.httpMethod = httpMethod;
  }


  public Log id(String id) {
    this.id = id;
    return this;
  }

  /**
   * UUID acting as Request Identifier.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Log latency(BigDecimal latency) {
    this.latency = latency;
    return this;
  }

  /**
   * Latency added by making this request via Unified Api.
   * @return latency
   */
  @javax.annotation.Nonnull
  public BigDecimal getLatency() {
    return latency;
  }

  public void setLatency(BigDecimal latency) {
    this.latency = latency;
  }


  public Log operation(LogOperation operation) {
    this.operation = operation;
    return this;
  }

  /**
   * Get operation
   * @return operation
   */
  @javax.annotation.Nonnull
  public LogOperation getOperation() {
    return operation;
  }

  public void setOperation(LogOperation operation) {
    this.operation = operation;
  }


  public Log parentId(String parentId) {
    this.parentId = parentId;
    return this;
  }

  /**
   * When request is a child request, this UUID indicates it&#39;s parent request.
   * @return parentId
   */
  @javax.annotation.Nullable
  public String getParentId() {
    return parentId;
  }

  public void setParentId(String parentId) {
    this.parentId = parentId;
  }


  public Log path(String path) {
    this.path = path;
    return this;
  }

  /**
   * The path component of the URI the request was made to.
   * @return path
   */
  @javax.annotation.Nonnull
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  public Log sandbox(Boolean sandbox) {
    this.sandbox = sandbox;
    return this;
  }

  /**
   * Indicates whether the request was made using Apidecks sandbox credentials or not.
   * @return sandbox
   */
  @javax.annotation.Nonnull
  public Boolean getSandbox() {
    return sandbox;
  }

  public void setSandbox(Boolean sandbox) {
    this.sandbox = sandbox;
  }


  public Log service(LogService service) {
    this.service = service;
    return this;
  }

  /**
   * Get service
   * @return service
   */
  @javax.annotation.Nonnull
  public LogService getService() {
    return service;
  }

  public void setService(LogService service) {
    this.service = service;
  }


  public Log sourceIp(String sourceIp) {
    this.sourceIp = sourceIp;
    return this;
  }

  /**
   * The IP address of the source of the request.
   * @return sourceIp
   */
  @javax.annotation.Nullable
  public String getSourceIp() {
    return sourceIp;
  }

  public void setSourceIp(String sourceIp) {
    this.sourceIp = sourceIp;
  }


  public Log statusCode(Integer statusCode) {
    this.statusCode = statusCode;
    return this;
  }

  /**
   * HTTP Status code that was returned.
   * @return statusCode
   */
  @javax.annotation.Nonnull
  public Integer getStatusCode() {
    return statusCode;
  }

  public void setStatusCode(Integer statusCode) {
    this.statusCode = statusCode;
  }


  public Log success(Boolean success) {
    this.success = success;
    return this;
  }

  /**
   * Whether or not the request was successful.
   * @return success
   */
  @javax.annotation.Nonnull
  public Boolean getSuccess() {
    return success;
  }

  public void setSuccess(Boolean success) {
    this.success = success;
  }


  public Log timestamp(String timestamp) {
    this.timestamp = timestamp;
    return this;
  }

  /**
   * ISO Date and time when the request was made.
   * @return timestamp
   */
  @javax.annotation.Nonnull
  public String getTimestamp() {
    return timestamp;
  }

  public void setTimestamp(String timestamp) {
    this.timestamp = timestamp;
  }


  public Log unifiedApi(UnifiedApiEnum unifiedApi) {
    this.unifiedApi = unifiedApi;
    return this;
  }

  /**
   * Which Unified Api request was made to.
   * @return unifiedApi
   */
  @javax.annotation.Nonnull
  public UnifiedApiEnum getUnifiedApi() {
    return unifiedApi;
  }

  public void setUnifiedApi(UnifiedApiEnum unifiedApi) {
    this.unifiedApi = unifiedApi;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Log log = (Log) o;
    return Objects.equals(this.apiStyle, log.apiStyle) &&
        Objects.equals(this.baseUrl, log.baseUrl) &&
        Objects.equals(this.childRequest, log.childRequest) &&
        Objects.equals(this.consumerId, log.consumerId) &&
        Objects.equals(this.duration, log.duration) &&
        Objects.equals(this.errorMessage, log.errorMessage) &&
        Objects.equals(this.execution, log.execution) &&
        Objects.equals(this.hasChildren, log.hasChildren) &&
        Objects.equals(this.httpMethod, log.httpMethod) &&
        Objects.equals(this.id, log.id) &&
        Objects.equals(this.latency, log.latency) &&
        Objects.equals(this.operation, log.operation) &&
        Objects.equals(this.parentId, log.parentId) &&
        Objects.equals(this.path, log.path) &&
        Objects.equals(this.sandbox, log.sandbox) &&
        Objects.equals(this.service, log.service) &&
        Objects.equals(this.sourceIp, log.sourceIp) &&
        Objects.equals(this.statusCode, log.statusCode) &&
        Objects.equals(this.success, log.success) &&
        Objects.equals(this.timestamp, log.timestamp) &&
        Objects.equals(this.unifiedApi, log.unifiedApi);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(apiStyle, baseUrl, childRequest, consumerId, duration, errorMessage, execution, hasChildren, httpMethod, id, latency, operation, parentId, path, sandbox, service, sourceIp, statusCode, success, timestamp, unifiedApi);
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
    sb.append("class Log {\n");
    sb.append("    apiStyle: ").append(toIndentedString(apiStyle)).append("\n");
    sb.append("    baseUrl: ").append(toIndentedString(baseUrl)).append("\n");
    sb.append("    childRequest: ").append(toIndentedString(childRequest)).append("\n");
    sb.append("    consumerId: ").append(toIndentedString(consumerId)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    errorMessage: ").append(toIndentedString(errorMessage)).append("\n");
    sb.append("    execution: ").append(toIndentedString(execution)).append("\n");
    sb.append("    hasChildren: ").append(toIndentedString(hasChildren)).append("\n");
    sb.append("    httpMethod: ").append(toIndentedString(httpMethod)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    latency: ").append(toIndentedString(latency)).append("\n");
    sb.append("    operation: ").append(toIndentedString(operation)).append("\n");
    sb.append("    parentId: ").append(toIndentedString(parentId)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    sandbox: ").append(toIndentedString(sandbox)).append("\n");
    sb.append("    service: ").append(toIndentedString(service)).append("\n");
    sb.append("    sourceIp: ").append(toIndentedString(sourceIp)).append("\n");
    sb.append("    statusCode: ").append(toIndentedString(statusCode)).append("\n");
    sb.append("    success: ").append(toIndentedString(success)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
    sb.append("    unifiedApi: ").append(toIndentedString(unifiedApi)).append("\n");
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
    openapiFields.add("api_style");
    openapiFields.add("base_url");
    openapiFields.add("child_request");
    openapiFields.add("consumer_id");
    openapiFields.add("duration");
    openapiFields.add("error_message");
    openapiFields.add("execution");
    openapiFields.add("has_children");
    openapiFields.add("http_method");
    openapiFields.add("id");
    openapiFields.add("latency");
    openapiFields.add("operation");
    openapiFields.add("parent_id");
    openapiFields.add("path");
    openapiFields.add("sandbox");
    openapiFields.add("service");
    openapiFields.add("source_ip");
    openapiFields.add("status_code");
    openapiFields.add("success");
    openapiFields.add("timestamp");
    openapiFields.add("unified_api");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("api_style");
    openapiRequiredFields.add("base_url");
    openapiRequiredFields.add("child_request");
    openapiRequiredFields.add("consumer_id");
    openapiRequiredFields.add("duration");
    openapiRequiredFields.add("execution");
    openapiRequiredFields.add("has_children");
    openapiRequiredFields.add("http_method");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("latency");
    openapiRequiredFields.add("operation");
    openapiRequiredFields.add("parent_id");
    openapiRequiredFields.add("path");
    openapiRequiredFields.add("sandbox");
    openapiRequiredFields.add("service");
    openapiRequiredFields.add("status_code");
    openapiRequiredFields.add("success");
    openapiRequiredFields.add("timestamp");
    openapiRequiredFields.add("unified_api");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Log
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Log.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Log is not found in the empty JSON string", Log.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Log.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Log` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Log.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("api_style").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `api_style` to be a primitive type in the JSON string but got `%s`", jsonObj.get("api_style").toString()));
      }
      if (!jsonObj.get("base_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `base_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("base_url").toString()));
      }
      if (!jsonObj.get("consumer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consumer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consumer_id").toString()));
      }
      if ((jsonObj.get("error_message") != null && !jsonObj.get("error_message").isJsonNull()) && !jsonObj.get("error_message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `error_message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("error_message").toString()));
      }
      if (!jsonObj.get("http_method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `http_method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("http_method").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the required field `operation`
      LogOperation.validateJsonElement(jsonObj.get("operation"));
      if ((jsonObj.get("parent_id") != null && !jsonObj.get("parent_id").isJsonNull()) && !jsonObj.get("parent_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parent_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parent_id").toString()));
      }
      if (!jsonObj.get("path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("path").toString()));
      }
      // validate the required field `service`
      LogService.validateJsonElement(jsonObj.get("service"));
      if ((jsonObj.get("source_ip") != null && !jsonObj.get("source_ip").isJsonNull()) && !jsonObj.get("source_ip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_ip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_ip").toString()));
      }
      if (!jsonObj.get("timestamp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timestamp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timestamp").toString()));
      }
      if (!jsonObj.get("unified_api").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unified_api` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unified_api").toString()));
      }
      // validate the required field `unified_api`
      UnifiedApiEnum.validateJsonElement(jsonObj.get("unified_api"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Log.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Log' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Log> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Log.class));

       return (TypeAdapter<T>) new TypeAdapter<Log>() {
           @Override
           public void write(JsonWriter out, Log value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Log read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Log given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Log
   * @throws IOException if the JSON string is invalid with respect to Log
   */
  public static Log fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Log.class);
  }

  /**
   * Convert an instance of Log to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

