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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.AuthType;
import org.openapitools.client.model.ConnectionConfigurationInner;
import org.openapitools.client.model.ConnectionState;
import org.openapitools.client.model.CustomMapping;
import org.openapitools.client.model.FormField;
import org.openapitools.client.model.IntegrationState;
import org.openapitools.client.model.OAuthGrantType;
import org.openapitools.client.model.WebhookSubscription;
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
 * Connection
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:50.743494-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Connection {
  public static final String SERIALIZED_NAME_AUTH_TYPE = "auth_type";
  @SerializedName(SERIALIZED_NAME_AUTH_TYPE)
  private AuthType authType;

  public static final String SERIALIZED_NAME_AUTHORIZE_URL = "authorize_url";
  @SerializedName(SERIALIZED_NAME_AUTHORIZE_URL)
  private String authorizeUrl;

  public static final String SERIALIZED_NAME_CONFIGURABLE_RESOURCES = "configurable_resources";
  @SerializedName(SERIALIZED_NAME_CONFIGURABLE_RESOURCES)
  private List<String> configurableResources = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONFIGURATION = "configuration";
  @SerializedName(SERIALIZED_NAME_CONFIGURATION)
  private List<ConnectionConfigurationInner> _configuration = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private BigDecimal createdAt;

  public static final String SERIALIZED_NAME_CUSTOM_MAPPINGS = "custom_mappings";
  @SerializedName(SERIALIZED_NAME_CUSTOM_MAPPINGS)
  private List<CustomMapping> customMappings = new ArrayList<>();

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_FORM_FIELDS = "form_fields";
  @SerializedName(SERIALIZED_NAME_FORM_FIELDS)
  private List<FormField> formFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_HAS_GUIDE = "has_guide";
  @SerializedName(SERIALIZED_NAME_HAS_GUIDE)
  private Boolean hasGuide;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private String icon;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INTEGRATION_STATE = "integration_state";
  @SerializedName(SERIALIZED_NAME_INTEGRATION_STATE)
  private IntegrationState integrationState;

  public static final String SERIALIZED_NAME_LOGO = "logo";
  @SerializedName(SERIALIZED_NAME_LOGO)
  private String logo;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private Map<String, Object> metadata;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OAUTH_GRANT_TYPE = "oauth_grant_type";
  @SerializedName(SERIALIZED_NAME_OAUTH_GRANT_TYPE)
  private OAuthGrantType oauthGrantType;

  public static final String SERIALIZED_NAME_RESOURCE_SCHEMA_SUPPORT = "resource_schema_support";
  @SerializedName(SERIALIZED_NAME_RESOURCE_SCHEMA_SUPPORT)
  private List<String> resourceSchemaSupport = new ArrayList<>();

  public static final String SERIALIZED_NAME_RESOURCE_SETTINGS_SUPPORT = "resource_settings_support";
  @SerializedName(SERIALIZED_NAME_RESOURCE_SETTINGS_SUPPORT)
  private List<String> resourceSettingsSupport = new ArrayList<>();

  public static final String SERIALIZED_NAME_REVOKE_URL = "revoke_url";
  @SerializedName(SERIALIZED_NAME_REVOKE_URL)
  private String revokeUrl;

  public static final String SERIALIZED_NAME_SCHEMA_SUPPORT = "schema_support";
  @SerializedName(SERIALIZED_NAME_SCHEMA_SUPPORT)
  private Boolean schemaSupport;

  public static final String SERIALIZED_NAME_SERVICE_ID = "service_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_ID)
  private String serviceId;

  public static final String SERIALIZED_NAME_SETTINGS = "settings";
  @SerializedName(SERIALIZED_NAME_SETTINGS)
  private Map<String, Object> settings;

  public static final String SERIALIZED_NAME_SETTINGS_REQUIRED_FOR_AUTHORIZATION = "settings_required_for_authorization";
  @SerializedName(SERIALIZED_NAME_SETTINGS_REQUIRED_FOR_AUTHORIZATION)
  private List<String> settingsRequiredForAuthorization = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private ConnectionState state;

  /**
   * Status of the connection.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    LIVE("live"),
    
    UPCOMING("upcoming"),
    
    REQUESTED("requested");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_SUBSCRIPTIONS = "subscriptions";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTIONS)
  private List<WebhookSubscription> subscriptions = new ArrayList<>();

  public static final String SERIALIZED_NAME_TAG_LINE = "tag_line";
  @SerializedName(SERIALIZED_NAME_TAG_LINE)
  private String tagLine;

  public static final String SERIALIZED_NAME_UNIFIED_API = "unified_api";
  @SerializedName(SERIALIZED_NAME_UNIFIED_API)
  private String unifiedApi;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private BigDecimal updatedAt;

  public static final String SERIALIZED_NAME_VALIDATION_SUPPORT = "validation_support";
  @SerializedName(SERIALIZED_NAME_VALIDATION_SUPPORT)
  private Boolean validationSupport;

  public static final String SERIALIZED_NAME_WEBSITE = "website";
  @SerializedName(SERIALIZED_NAME_WEBSITE)
  private String website;

  public Connection() {
  }

  public Connection(
     String authorizeUrl, 
     List<String> configurableResources, 
     BigDecimal createdAt, 
     List<FormField> formFields, 
     Boolean hasGuide, 
     String icon, 
     String id, 
     String logo, 
     String name, 
     List<String> resourceSchemaSupport, 
     List<String> resourceSettingsSupport, 
     String revokeUrl, 
     Boolean schemaSupport, 
     String serviceId, 
     List<String> settingsRequiredForAuthorization, 
     StatusEnum status, 
     List<WebhookSubscription> subscriptions, 
     String tagLine, 
     String unifiedApi, 
     BigDecimal updatedAt, 
     Boolean validationSupport, 
     String website
  ) {
    this();
    this.authorizeUrl = authorizeUrl;
    this.configurableResources = configurableResources;
    this.createdAt = createdAt;
    this.formFields = formFields;
    this.hasGuide = hasGuide;
    this.icon = icon;
    this.id = id;
    this.logo = logo;
    this.name = name;
    this.resourceSchemaSupport = resourceSchemaSupport;
    this.resourceSettingsSupport = resourceSettingsSupport;
    this.revokeUrl = revokeUrl;
    this.schemaSupport = schemaSupport;
    this.serviceId = serviceId;
    this.settingsRequiredForAuthorization = settingsRequiredForAuthorization;
    this.status = status;
    this.subscriptions = subscriptions;
    this.tagLine = tagLine;
    this.unifiedApi = unifiedApi;
    this.updatedAt = updatedAt;
    this.validationSupport = validationSupport;
    this.website = website;
  }

  public Connection authType(AuthType authType) {
    this.authType = authType;
    return this;
  }

  /**
   * Get authType
   * @return authType
   */
  @javax.annotation.Nullable
  public AuthType getAuthType() {
    return authType;
  }

  public void setAuthType(AuthType authType) {
    this.authType = authType;
  }


  /**
   * The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector&#39;s UI. Before you can use this URI, you must add &#x60;redirect_uri&#x60; as a query parameter to the &#x60;authorize_url&#x60;. Be sure to URL encode the &#x60;redirect_uri&#x60; part. Your users will be redirected to this &#x60;redirect_uri&#x60; after they granted access to your app in the connector&#39;s UI.
   * @return authorizeUrl
   */
  @javax.annotation.Nullable
  public String getAuthorizeUrl() {
    return authorizeUrl;
  }



  /**
   * Get configurableResources
   * @return configurableResources
   */
  @javax.annotation.Nullable
  public List<String> getConfigurableResources() {
    return configurableResources;
  }



  public Connection _configuration(List<ConnectionConfigurationInner> _configuration) {
    this._configuration = _configuration;
    return this;
  }

  public Connection addConfigurationItem(ConnectionConfigurationInner _configurationItem) {
    if (this._configuration == null) {
      this._configuration = new ArrayList<>();
    }
    this._configuration.add(_configurationItem);
    return this;
  }

  /**
   * Get _configuration
   * @return _configuration
   */
  @javax.annotation.Nullable
  public List<ConnectionConfigurationInner> getConfiguration() {
    return _configuration;
  }

  public void setConfiguration(List<ConnectionConfigurationInner> _configuration) {
    this._configuration = _configuration;
  }


  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public BigDecimal getCreatedAt() {
    return createdAt;
  }



  public Connection customMappings(List<CustomMapping> customMappings) {
    this.customMappings = customMappings;
    return this;
  }

  public Connection addCustomMappingsItem(CustomMapping customMappingsItem) {
    if (this.customMappings == null) {
      this.customMappings = new ArrayList<>();
    }
    this.customMappings.add(customMappingsItem);
    return this;
  }

  /**
   * List of custom mappings configured for this connection
   * @return customMappings
   */
  @javax.annotation.Nullable
  public List<CustomMapping> getCustomMappings() {
    return customMappings;
  }

  public void setCustomMappings(List<CustomMapping> customMappings) {
    this.customMappings = customMappings;
  }


  public Connection enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  /**
   * The settings that are wanted to create a connection.
   * @return formFields
   */
  @javax.annotation.Nullable
  public List<FormField> getFormFields() {
    return formFields;
  }



  /**
   * Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).
   * @return hasGuide
   */
  @javax.annotation.Nullable
  public Boolean getHasGuide() {
    return hasGuide;
  }



  /**
   * A visual icon of the connection, that will be shown in the Vault
   * @return icon
   */
  @javax.annotation.Nullable
  public String getIcon() {
    return icon;
  }



  /**
   * The unique identifier of the connection.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Connection integrationState(IntegrationState integrationState) {
    this.integrationState = integrationState;
    return this;
  }

  /**
   * Get integrationState
   * @return integrationState
   */
  @javax.annotation.Nullable
  public IntegrationState getIntegrationState() {
    return integrationState;
  }

  public void setIntegrationState(IntegrationState integrationState) {
    this.integrationState = integrationState;
  }


  /**
   * The logo of the connection, that will be shown in the Vault
   * @return logo
   */
  @javax.annotation.Nullable
  public String getLogo() {
    return logo;
  }



  public Connection metadata(Map<String, Object> metadata) {
    this.metadata = metadata;
    return this;
  }

  public Connection putMetadataItem(String key, Object metadataItem) {
    if (this.metadata == null) {
      this.metadata = new HashMap<>();
    }
    this.metadata.put(key, metadataItem);
    return this;
  }

  /**
   * Attach your own consumer specific metadata
   * @return metadata
   */
  @javax.annotation.Nullable
  public Map<String, Object> getMetadata() {
    return metadata;
  }

  public void setMetadata(Map<String, Object> metadata) {
    this.metadata = metadata;
  }


  /**
   * The name of the connection
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }



  public Connection oauthGrantType(OAuthGrantType oauthGrantType) {
    this.oauthGrantType = oauthGrantType;
    return this;
  }

  /**
   * Get oauthGrantType
   * @return oauthGrantType
   */
  @javax.annotation.Nullable
  public OAuthGrantType getOauthGrantType() {
    return oauthGrantType;
  }

  public void setOauthGrantType(OAuthGrantType oauthGrantType) {
    this.oauthGrantType = oauthGrantType;
  }


  /**
   * Get resourceSchemaSupport
   * @return resourceSchemaSupport
   */
  @javax.annotation.Nullable
  public List<String> getResourceSchemaSupport() {
    return resourceSchemaSupport;
  }



  /**
   * Get resourceSettingsSupport
   * @return resourceSettingsSupport
   */
  @javax.annotation.Nullable
  public List<String> getResourceSettingsSupport() {
    return resourceSettingsSupport;
  }



  /**
   * The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add &#x60;redirect_uri&#x60; as a query parameter. Your users will be redirected to this &#x60;redirect_uri&#x60; after they granted access to your app in the connector&#39;s UI.
   * @return revokeUrl
   */
  @javax.annotation.Nullable
  public String getRevokeUrl() {
    return revokeUrl;
  }



  /**
   * Get schemaSupport
   * @return schemaSupport
   */
  @javax.annotation.Nullable
  public Boolean getSchemaSupport() {
    return schemaSupport;
  }



  /**
   * The ID of the service this connection belongs to.
   * @return serviceId
   */
  @javax.annotation.Nullable
  public String getServiceId() {
    return serviceId;
  }



  public Connection settings(Map<String, Object> settings) {
    this.settings = settings;
    return this;
  }

  public Connection putSettingsItem(String key, Object settingsItem) {
    if (this.settings == null) {
      this.settings = new HashMap<>();
    }
    this.settings.put(key, settingsItem);
    return this;
  }

  /**
   * Connection settings. Values will persist to &#x60;form_fields&#x60; with corresponding id
   * @return settings
   */
  @javax.annotation.Nullable
  public Map<String, Object> getSettings() {
    return settings;
  }

  public void setSettings(Map<String, Object> settings) {
    this.settings = settings;
  }


  /**
   * List of settings that are required to be configured on integration before authorization can occur
   * @return settingsRequiredForAuthorization
   */
  @javax.annotation.Nullable
  public List<String> getSettingsRequiredForAuthorization() {
    return settingsRequiredForAuthorization;
  }



  public Connection state(ConnectionState state) {
    this.state = state;
    return this;
  }

  /**
   * Get state
   * @return state
   */
  @javax.annotation.Nullable
  public ConnectionState getState() {
    return state;
  }

  public void setState(ConnectionState state) {
    this.state = state;
  }


  /**
   * Status of the connection.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  /**
   * Get subscriptions
   * @return subscriptions
   */
  @javax.annotation.Nullable
  public List<WebhookSubscription> getSubscriptions() {
    return subscriptions;
  }



  /**
   * Get tagLine
   * @return tagLine
   */
  @javax.annotation.Nullable
  public String getTagLine() {
    return tagLine;
  }



  /**
   * The unified API category where the connection belongs to.
   * @return unifiedApi
   */
  @javax.annotation.Nullable
  public String getUnifiedApi() {
    return unifiedApi;
  }



  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public BigDecimal getUpdatedAt() {
    return updatedAt;
  }



  /**
   * Get validationSupport
   * @return validationSupport
   */
  @javax.annotation.Nullable
  public Boolean getValidationSupport() {
    return validationSupport;
  }



  /**
   * The website URL of the connection
   * @return website
   */
  @javax.annotation.Nullable
  public String getWebsite() {
    return website;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Connection connection = (Connection) o;
    return Objects.equals(this.authType, connection.authType) &&
        Objects.equals(this.authorizeUrl, connection.authorizeUrl) &&
        Objects.equals(this.configurableResources, connection.configurableResources) &&
        Objects.equals(this._configuration, connection._configuration) &&
        Objects.equals(this.createdAt, connection.createdAt) &&
        Objects.equals(this.customMappings, connection.customMappings) &&
        Objects.equals(this.enabled, connection.enabled) &&
        Objects.equals(this.formFields, connection.formFields) &&
        Objects.equals(this.hasGuide, connection.hasGuide) &&
        Objects.equals(this.icon, connection.icon) &&
        Objects.equals(this.id, connection.id) &&
        Objects.equals(this.integrationState, connection.integrationState) &&
        Objects.equals(this.logo, connection.logo) &&
        Objects.equals(this.metadata, connection.metadata) &&
        Objects.equals(this.name, connection.name) &&
        Objects.equals(this.oauthGrantType, connection.oauthGrantType) &&
        Objects.equals(this.resourceSchemaSupport, connection.resourceSchemaSupport) &&
        Objects.equals(this.resourceSettingsSupport, connection.resourceSettingsSupport) &&
        Objects.equals(this.revokeUrl, connection.revokeUrl) &&
        Objects.equals(this.schemaSupport, connection.schemaSupport) &&
        Objects.equals(this.serviceId, connection.serviceId) &&
        Objects.equals(this.settings, connection.settings) &&
        Objects.equals(this.settingsRequiredForAuthorization, connection.settingsRequiredForAuthorization) &&
        Objects.equals(this.state, connection.state) &&
        Objects.equals(this.status, connection.status) &&
        Objects.equals(this.subscriptions, connection.subscriptions) &&
        Objects.equals(this.tagLine, connection.tagLine) &&
        Objects.equals(this.unifiedApi, connection.unifiedApi) &&
        Objects.equals(this.updatedAt, connection.updatedAt) &&
        Objects.equals(this.validationSupport, connection.validationSupport) &&
        Objects.equals(this.website, connection.website);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(authType, authorizeUrl, configurableResources, _configuration, createdAt, customMappings, enabled, formFields, hasGuide, icon, id, integrationState, logo, metadata, name, oauthGrantType, resourceSchemaSupport, resourceSettingsSupport, revokeUrl, schemaSupport, serviceId, settings, settingsRequiredForAuthorization, state, status, subscriptions, tagLine, unifiedApi, updatedAt, validationSupport, website);
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
    sb.append("class Connection {\n");
    sb.append("    authType: ").append(toIndentedString(authType)).append("\n");
    sb.append("    authorizeUrl: ").append(toIndentedString(authorizeUrl)).append("\n");
    sb.append("    configurableResources: ").append(toIndentedString(configurableResources)).append("\n");
    sb.append("    _configuration: ").append(toIndentedString(_configuration)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    customMappings: ").append(toIndentedString(customMappings)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    formFields: ").append(toIndentedString(formFields)).append("\n");
    sb.append("    hasGuide: ").append(toIndentedString(hasGuide)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    integrationState: ").append(toIndentedString(integrationState)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    oauthGrantType: ").append(toIndentedString(oauthGrantType)).append("\n");
    sb.append("    resourceSchemaSupport: ").append(toIndentedString(resourceSchemaSupport)).append("\n");
    sb.append("    resourceSettingsSupport: ").append(toIndentedString(resourceSettingsSupport)).append("\n");
    sb.append("    revokeUrl: ").append(toIndentedString(revokeUrl)).append("\n");
    sb.append("    schemaSupport: ").append(toIndentedString(schemaSupport)).append("\n");
    sb.append("    serviceId: ").append(toIndentedString(serviceId)).append("\n");
    sb.append("    settings: ").append(toIndentedString(settings)).append("\n");
    sb.append("    settingsRequiredForAuthorization: ").append(toIndentedString(settingsRequiredForAuthorization)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subscriptions: ").append(toIndentedString(subscriptions)).append("\n");
    sb.append("    tagLine: ").append(toIndentedString(tagLine)).append("\n");
    sb.append("    unifiedApi: ").append(toIndentedString(unifiedApi)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    validationSupport: ").append(toIndentedString(validationSupport)).append("\n");
    sb.append("    website: ").append(toIndentedString(website)).append("\n");
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
    openapiFields.add("auth_type");
    openapiFields.add("authorize_url");
    openapiFields.add("configurable_resources");
    openapiFields.add("configuration");
    openapiFields.add("created_at");
    openapiFields.add("custom_mappings");
    openapiFields.add("enabled");
    openapiFields.add("form_fields");
    openapiFields.add("has_guide");
    openapiFields.add("icon");
    openapiFields.add("id");
    openapiFields.add("integration_state");
    openapiFields.add("logo");
    openapiFields.add("metadata");
    openapiFields.add("name");
    openapiFields.add("oauth_grant_type");
    openapiFields.add("resource_schema_support");
    openapiFields.add("resource_settings_support");
    openapiFields.add("revoke_url");
    openapiFields.add("schema_support");
    openapiFields.add("service_id");
    openapiFields.add("settings");
    openapiFields.add("settings_required_for_authorization");
    openapiFields.add("state");
    openapiFields.add("status");
    openapiFields.add("subscriptions");
    openapiFields.add("tag_line");
    openapiFields.add("unified_api");
    openapiFields.add("updated_at");
    openapiFields.add("validation_support");
    openapiFields.add("website");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Connection
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Connection.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Connection is not found in the empty JSON string", Connection.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Connection.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Connection` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `auth_type`
      if (jsonObj.get("auth_type") != null && !jsonObj.get("auth_type").isJsonNull()) {
        AuthType.validateJsonElement(jsonObj.get("auth_type"));
      }
      if ((jsonObj.get("authorize_url") != null && !jsonObj.get("authorize_url").isJsonNull()) && !jsonObj.get("authorize_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authorize_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authorize_url").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("configurable_resources") != null && !jsonObj.get("configurable_resources").isJsonNull() && !jsonObj.get("configurable_resources").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `configurable_resources` to be an array in the JSON string but got `%s`", jsonObj.get("configurable_resources").toString()));
      }
      if (jsonObj.get("configuration") != null && !jsonObj.get("configuration").isJsonNull()) {
        JsonArray jsonArray_configuration = jsonObj.getAsJsonArray("configuration");
        if (jsonArray_configuration != null) {
          // ensure the json data is an array
          if (!jsonObj.get("configuration").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `configuration` to be an array in the JSON string but got `%s`", jsonObj.get("configuration").toString()));
          }

          // validate the optional field `configuration` (array)
          for (int i = 0; i < jsonArray_configuration.size(); i++) {
            ConnectionConfigurationInner.validateJsonElement(jsonArray_configuration.get(i));
          };
        }
      }
      if (jsonObj.get("custom_mappings") != null && !jsonObj.get("custom_mappings").isJsonNull()) {
        JsonArray jsonArraycustomMappings = jsonObj.getAsJsonArray("custom_mappings");
        if (jsonArraycustomMappings != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_mappings").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_mappings` to be an array in the JSON string but got `%s`", jsonObj.get("custom_mappings").toString()));
          }

          // validate the optional field `custom_mappings` (array)
          for (int i = 0; i < jsonArraycustomMappings.size(); i++) {
            CustomMapping.validateJsonElement(jsonArraycustomMappings.get(i));
          };
        }
      }
      if (jsonObj.get("form_fields") != null && !jsonObj.get("form_fields").isJsonNull()) {
        JsonArray jsonArrayformFields = jsonObj.getAsJsonArray("form_fields");
        if (jsonArrayformFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("form_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `form_fields` to be an array in the JSON string but got `%s`", jsonObj.get("form_fields").toString()));
          }

          // validate the optional field `form_fields` (array)
          for (int i = 0; i < jsonArrayformFields.size(); i++) {
            FormField.validateJsonElement(jsonArrayformFields.get(i));
          };
        }
      }
      if ((jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) && !jsonObj.get("icon").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `integration_state`
      if (jsonObj.get("integration_state") != null && !jsonObj.get("integration_state").isJsonNull()) {
        IntegrationState.validateJsonElement(jsonObj.get("integration_state"));
      }
      if ((jsonObj.get("logo") != null && !jsonObj.get("logo").isJsonNull()) && !jsonObj.get("logo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `logo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("logo").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `oauth_grant_type`
      if (jsonObj.get("oauth_grant_type") != null && !jsonObj.get("oauth_grant_type").isJsonNull()) {
        OAuthGrantType.validateJsonElement(jsonObj.get("oauth_grant_type"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("resource_schema_support") != null && !jsonObj.get("resource_schema_support").isJsonNull() && !jsonObj.get("resource_schema_support").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `resource_schema_support` to be an array in the JSON string but got `%s`", jsonObj.get("resource_schema_support").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("resource_settings_support") != null && !jsonObj.get("resource_settings_support").isJsonNull() && !jsonObj.get("resource_settings_support").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `resource_settings_support` to be an array in the JSON string but got `%s`", jsonObj.get("resource_settings_support").toString()));
      }
      if ((jsonObj.get("revoke_url") != null && !jsonObj.get("revoke_url").isJsonNull()) && !jsonObj.get("revoke_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `revoke_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("revoke_url").toString()));
      }
      if ((jsonObj.get("service_id") != null && !jsonObj.get("service_id").isJsonNull()) && !jsonObj.get("service_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("settings_required_for_authorization") != null && !jsonObj.get("settings_required_for_authorization").isJsonNull() && !jsonObj.get("settings_required_for_authorization").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `settings_required_for_authorization` to be an array in the JSON string but got `%s`", jsonObj.get("settings_required_for_authorization").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        ConnectionState.validateJsonElement(jsonObj.get("state"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if (jsonObj.get("subscriptions") != null && !jsonObj.get("subscriptions").isJsonNull()) {
        JsonArray jsonArraysubscriptions = jsonObj.getAsJsonArray("subscriptions");
        if (jsonArraysubscriptions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("subscriptions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `subscriptions` to be an array in the JSON string but got `%s`", jsonObj.get("subscriptions").toString()));
          }

          // validate the optional field `subscriptions` (array)
          for (int i = 0; i < jsonArraysubscriptions.size(); i++) {
            WebhookSubscription.validateJsonElement(jsonArraysubscriptions.get(i));
          };
        }
      }
      if ((jsonObj.get("tag_line") != null && !jsonObj.get("tag_line").isJsonNull()) && !jsonObj.get("tag_line").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tag_line` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tag_line").toString()));
      }
      if ((jsonObj.get("unified_api") != null && !jsonObj.get("unified_api").isJsonNull()) && !jsonObj.get("unified_api").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unified_api` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unified_api").toString()));
      }
      if ((jsonObj.get("website") != null && !jsonObj.get("website").isJsonNull()) && !jsonObj.get("website").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `website` to be a primitive type in the JSON string but got `%s`", jsonObj.get("website").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Connection.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Connection' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Connection> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Connection.class));

       return (TypeAdapter<T>) new TypeAdapter<Connection>() {
           @Override
           public void write(JsonWriter out, Connection value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Connection read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Connection given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Connection
   * @throws IOException if the JSON string is invalid with respect to Connection
   */
  public static Connection fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Connection.class);
  }

  /**
   * Convert an instance of Connection to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

