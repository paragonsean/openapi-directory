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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.UnifiedApiId;

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
 * Settings to change the way the Vault is displayed.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:50.743494-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SessionSettings {
  /**
   * Gets or Sets allowActions
   */
  @JsonAdapter(AllowActionsEnum.Adapter.class)
  public enum AllowActionsEnum {
    DELETE("delete"),
    
    DISCONNECT("disconnect"),
    
    REAUTHORIZE("reauthorize"),
    
    DISABLE("disable");

    private String value;

    AllowActionsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AllowActionsEnum fromValue(String value) {
      for (AllowActionsEnum b : AllowActionsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AllowActionsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AllowActionsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AllowActionsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AllowActionsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AllowActionsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ALLOW_ACTIONS = "allow_actions";
  @SerializedName(SERIALIZED_NAME_ALLOW_ACTIONS)
  private List<AllowActionsEnum> allowActions = new ArrayList<>();

  public static final String SERIALIZED_NAME_AUTO_REDIRECT = "auto_redirect";
  @SerializedName(SERIALIZED_NAME_AUTO_REDIRECT)
  private Boolean autoRedirect = false;

  public static final String SERIALIZED_NAME_HIDE_GUIDES = "hide_guides";
  @SerializedName(SERIALIZED_NAME_HIDE_GUIDES)
  private Boolean hideGuides = false;

  public static final String SERIALIZED_NAME_HIDE_RESOURCE_SETTINGS = "hide_resource_settings";
  @SerializedName(SERIALIZED_NAME_HIDE_RESOURCE_SETTINGS)
  private Boolean hideResourceSettings = false;

  public static final String SERIALIZED_NAME_ISOLATION_MODE = "isolation_mode";
  @SerializedName(SERIALIZED_NAME_ISOLATION_MODE)
  private Boolean isolationMode = false;

  public static final String SERIALIZED_NAME_SANDBOX_MODE = "sandbox_mode";
  @SerializedName(SERIALIZED_NAME_SANDBOX_MODE)
  private Boolean sandboxMode = false;

  public static final String SERIALIZED_NAME_SESSION_LENGTH = "session_length";
  @SerializedName(SERIALIZED_NAME_SESSION_LENGTH)
  private String sessionLength = "1h";

  public static final String SERIALIZED_NAME_SHOW_LOGS = "show_logs";
  @SerializedName(SERIALIZED_NAME_SHOW_LOGS)
  private Boolean showLogs = true;

  public static final String SERIALIZED_NAME_SHOW_SIDEBAR = "show_sidebar";
  @SerializedName(SERIALIZED_NAME_SHOW_SIDEBAR)
  private Boolean showSidebar = true;

  public static final String SERIALIZED_NAME_SHOW_SUGGESTIONS = "show_suggestions";
  @SerializedName(SERIALIZED_NAME_SHOW_SUGGESTIONS)
  private Boolean showSuggestions = false;

  public static final String SERIALIZED_NAME_UNIFIED_APIS = "unified_apis";
  @SerializedName(SERIALIZED_NAME_UNIFIED_APIS)
  private List<UnifiedApiId> unifiedApis = new ArrayList<>();

  public SessionSettings() {
  }

  public SessionSettings allowActions(List<AllowActionsEnum> allowActions) {
    this.allowActions = allowActions;
    return this;
  }

  public SessionSettings addAllowActionsItem(AllowActionsEnum allowActionsItem) {
    if (this.allowActions == null) {
      this.allowActions = new ArrayList<>();
    }
    this.allowActions.add(allowActionsItem);
    return this;
  }

  /**
   * Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in &#x60;allow_actions&#x60; will be shown on a connection in Vault. Available actions are: &#x60;delete&#x60;, &#x60;disconnect&#x60;, &#x60;reauthorize&#x60; and &#x60;disable&#x60;. Empty array will hide all actions. By default all actions are visible.
   * @return allowActions
   */
  @javax.annotation.Nullable
  public List<AllowActionsEnum> getAllowActions() {
    return allowActions;
  }

  public void setAllowActions(List<AllowActionsEnum> allowActions) {
    this.allowActions = allowActions;
  }


  public SessionSettings autoRedirect(Boolean autoRedirect) {
    this.autoRedirect = autoRedirect;
    return this;
  }

  /**
   * Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to &#x60;false&#x60;.
   * @return autoRedirect
   */
  @javax.annotation.Nullable
  public Boolean getAutoRedirect() {
    return autoRedirect;
  }

  public void setAutoRedirect(Boolean autoRedirect) {
    this.autoRedirect = autoRedirect;
  }


  public SessionSettings hideGuides(Boolean hideGuides) {
    this.hideGuides = hideGuides;
    return this;
  }

  /**
   * Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to &#x60;false&#x60;.
   * @return hideGuides
   */
  @javax.annotation.Nullable
  public Boolean getHideGuides() {
    return hideGuides;
  }

  public void setHideGuides(Boolean hideGuides) {
    this.hideGuides = hideGuides;
  }


  public SessionSettings hideResourceSettings(Boolean hideResourceSettings) {
    this.hideResourceSettings = hideResourceSettings;
    return this;
  }

  /**
   * A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user.
   * @return hideResourceSettings
   */
  @javax.annotation.Nullable
  public Boolean getHideResourceSettings() {
    return hideResourceSettings;
  }

  public void setHideResourceSettings(Boolean hideResourceSettings) {
    this.hideResourceSettings = hideResourceSettings;
  }


  public SessionSettings isolationMode(Boolean isolationMode) {
    this.isolationMode = isolationMode;
    return this;
  }

  /**
   * Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items.
   * @return isolationMode
   */
  @javax.annotation.Nullable
  public Boolean getIsolationMode() {
    return isolationMode;
  }

  public void setIsolationMode(Boolean isolationMode) {
    this.isolationMode = isolationMode;
  }


  public SessionSettings sandboxMode(Boolean sandboxMode) {
    this.sandboxMode = sandboxMode;
    return this;
  }

  /**
   * Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment.
   * @return sandboxMode
   */
  @javax.annotation.Nullable
  public Boolean getSandboxMode() {
    return sandboxMode;
  }

  public void setSandboxMode(Boolean sandboxMode) {
    this.sandboxMode = sandboxMode;
  }


  public SessionSettings sessionLength(String sessionLength) {
    this.sessionLength = sessionLength;
    return this;
  }

  /**
   * The duration of time the session is valid for (maximum 1 week).
   * @return sessionLength
   */
  @javax.annotation.Nullable
  public String getSessionLength() {
    return sessionLength;
  }

  public void setSessionLength(String sessionLength) {
    this.sessionLength = sessionLength;
  }


  public SessionSettings showLogs(Boolean showLogs) {
    this.showLogs = showLogs;
    return this;
  }

  /**
   * Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to &#x60;true&#x60;.
   * @return showLogs
   */
  @javax.annotation.Nullable
  public Boolean getShowLogs() {
    return showLogs;
  }

  public void setShowLogs(Boolean showLogs) {
    this.showLogs = showLogs;
  }


  public SessionSettings showSidebar(Boolean showSidebar) {
    this.showSidebar = showSidebar;
    return this;
  }

  /**
   * Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to &#x60;true&#x60;.
   * @return showSidebar
   */
  @javax.annotation.Nullable
  public Boolean getShowSidebar() {
    return showSidebar;
  }

  public void setShowSidebar(Boolean showSidebar) {
    this.showSidebar = showSidebar;
  }


  public SessionSettings showSuggestions(Boolean showSuggestions) {
    this.showSuggestions = showSuggestions;
    return this;
  }

  /**
   * Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to &#x60;false&#x60;.
   * @return showSuggestions
   */
  @javax.annotation.Nullable
  public Boolean getShowSuggestions() {
    return showSuggestions;
  }

  public void setShowSuggestions(Boolean showSuggestions) {
    this.showSuggestions = showSuggestions;
  }


  public SessionSettings unifiedApis(List<UnifiedApiId> unifiedApis) {
    this.unifiedApis = unifiedApis;
    return this;
  }

  public SessionSettings addUnifiedApisItem(UnifiedApiId unifiedApisItem) {
    if (this.unifiedApis == null) {
      this.unifiedApis = new ArrayList<>();
    }
    this.unifiedApis.add(unifiedApisItem);
    return this;
  }

  /**
   * Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs.
   * @return unifiedApis
   */
  @javax.annotation.Nullable
  public List<UnifiedApiId> getUnifiedApis() {
    return unifiedApis;
  }

  public void setUnifiedApis(List<UnifiedApiId> unifiedApis) {
    this.unifiedApis = unifiedApis;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SessionSettings sessionSettings = (SessionSettings) o;
    return Objects.equals(this.allowActions, sessionSettings.allowActions) &&
        Objects.equals(this.autoRedirect, sessionSettings.autoRedirect) &&
        Objects.equals(this.hideGuides, sessionSettings.hideGuides) &&
        Objects.equals(this.hideResourceSettings, sessionSettings.hideResourceSettings) &&
        Objects.equals(this.isolationMode, sessionSettings.isolationMode) &&
        Objects.equals(this.sandboxMode, sessionSettings.sandboxMode) &&
        Objects.equals(this.sessionLength, sessionSettings.sessionLength) &&
        Objects.equals(this.showLogs, sessionSettings.showLogs) &&
        Objects.equals(this.showSidebar, sessionSettings.showSidebar) &&
        Objects.equals(this.showSuggestions, sessionSettings.showSuggestions) &&
        Objects.equals(this.unifiedApis, sessionSettings.unifiedApis);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowActions, autoRedirect, hideGuides, hideResourceSettings, isolationMode, sandboxMode, sessionLength, showLogs, showSidebar, showSuggestions, unifiedApis);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SessionSettings {\n");
    sb.append("    allowActions: ").append(toIndentedString(allowActions)).append("\n");
    sb.append("    autoRedirect: ").append(toIndentedString(autoRedirect)).append("\n");
    sb.append("    hideGuides: ").append(toIndentedString(hideGuides)).append("\n");
    sb.append("    hideResourceSettings: ").append(toIndentedString(hideResourceSettings)).append("\n");
    sb.append("    isolationMode: ").append(toIndentedString(isolationMode)).append("\n");
    sb.append("    sandboxMode: ").append(toIndentedString(sandboxMode)).append("\n");
    sb.append("    sessionLength: ").append(toIndentedString(sessionLength)).append("\n");
    sb.append("    showLogs: ").append(toIndentedString(showLogs)).append("\n");
    sb.append("    showSidebar: ").append(toIndentedString(showSidebar)).append("\n");
    sb.append("    showSuggestions: ").append(toIndentedString(showSuggestions)).append("\n");
    sb.append("    unifiedApis: ").append(toIndentedString(unifiedApis)).append("\n");
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
    openapiFields.add("allow_actions");
    openapiFields.add("auto_redirect");
    openapiFields.add("hide_guides");
    openapiFields.add("hide_resource_settings");
    openapiFields.add("isolation_mode");
    openapiFields.add("sandbox_mode");
    openapiFields.add("session_length");
    openapiFields.add("show_logs");
    openapiFields.add("show_sidebar");
    openapiFields.add("show_suggestions");
    openapiFields.add("unified_apis");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SessionSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SessionSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SessionSettings is not found in the empty JSON string", SessionSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SessionSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SessionSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("allow_actions") != null && !jsonObj.get("allow_actions").isJsonNull() && !jsonObj.get("allow_actions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `allow_actions` to be an array in the JSON string but got `%s`", jsonObj.get("allow_actions").toString()));
      }
      if ((jsonObj.get("session_length") != null && !jsonObj.get("session_length").isJsonNull()) && !jsonObj.get("session_length").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `session_length` to be a primitive type in the JSON string but got `%s`", jsonObj.get("session_length").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("unified_apis") != null && !jsonObj.get("unified_apis").isJsonNull() && !jsonObj.get("unified_apis").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `unified_apis` to be an array in the JSON string but got `%s`", jsonObj.get("unified_apis").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SessionSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SessionSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SessionSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SessionSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<SessionSettings>() {
           @Override
           public void write(JsonWriter out, SessionSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SessionSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SessionSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SessionSettings
   * @throws IOException if the JSON string is invalid with respect to SessionSettings
   */
  public static SessionSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SessionSettings.class);
  }

  /**
   * Convert an instance of SessionSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

