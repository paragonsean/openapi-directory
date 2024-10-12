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
import org.openapitools.client.model.ConsumerConnection;
import org.openapitools.client.model.VaultEventType;

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
 * ConnectionEvent
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:50.743494-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ConnectionEvent {
  public static final String SERIALIZED_NAME_ENTITY = "entity";
  @SerializedName(SERIALIZED_NAME_ENTITY)
  private ConsumerConnection entity;

  public static final String SERIALIZED_NAME_ENTITY_ID = "entity_id";
  @SerializedName(SERIALIZED_NAME_ENTITY_ID)
  private String entityId;

  public static final String SERIALIZED_NAME_ENTITY_TYPE = "entity_type";
  @SerializedName(SERIALIZED_NAME_ENTITY_TYPE)
  private String entityType;

  public static final String SERIALIZED_NAME_EVENT_ID = "event_id";
  @SerializedName(SERIALIZED_NAME_EVENT_ID)
  private String eventId;

  public static final String SERIALIZED_NAME_EVENT_TYPE = "event_type";
  @SerializedName(SERIALIZED_NAME_EVENT_TYPE)
  private VaultEventType eventType;

  public static final String SERIALIZED_NAME_EXECUTION_ATTEMPT = "execution_attempt";
  @SerializedName(SERIALIZED_NAME_EXECUTION_ATTEMPT)
  private BigDecimal executionAttempt;

  public static final String SERIALIZED_NAME_OCCURRED_AT = "occurred_at";
  @SerializedName(SERIALIZED_NAME_OCCURRED_AT)
  private String occurredAt;

  public static final String SERIALIZED_NAME_SERVICE_ID = "service_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_ID)
  private String serviceId;

  public ConnectionEvent() {
  }

  public ConnectionEvent entity(ConsumerConnection entity) {
    this.entity = entity;
    return this;
  }

  /**
   * Get entity
   * @return entity
   */
  @javax.annotation.Nullable
  public ConsumerConnection getEntity() {
    return entity;
  }

  public void setEntity(ConsumerConnection entity) {
    this.entity = entity;
  }


  public ConnectionEvent entityId(String entityId) {
    this.entityId = entityId;
    return this;
  }

  /**
   * The service provider&#39;s ID of the entity that triggered this event
   * @return entityId
   */
  @javax.annotation.Nullable
  public String getEntityId() {
    return entityId;
  }

  public void setEntityId(String entityId) {
    this.entityId = entityId;
  }


  public ConnectionEvent entityType(String entityType) {
    this.entityType = entityType;
    return this;
  }

  /**
   * The type entity that triggered this event
   * @return entityType
   */
  @javax.annotation.Nullable
  public String getEntityType() {
    return entityType;
  }

  public void setEntityType(String entityType) {
    this.entityType = entityType;
  }


  public ConnectionEvent eventId(String eventId) {
    this.eventId = eventId;
    return this;
  }

  /**
   * Unique reference to this request event
   * @return eventId
   */
  @javax.annotation.Nullable
  public String getEventId() {
    return eventId;
  }

  public void setEventId(String eventId) {
    this.eventId = eventId;
  }


  public ConnectionEvent eventType(VaultEventType eventType) {
    this.eventType = eventType;
    return this;
  }

  /**
   * Get eventType
   * @return eventType
   */
  @javax.annotation.Nullable
  public VaultEventType getEventType() {
    return eventType;
  }

  public void setEventType(VaultEventType eventType) {
    this.eventType = eventType;
  }


  public ConnectionEvent executionAttempt(BigDecimal executionAttempt) {
    this.executionAttempt = executionAttempt;
    return this;
  }

  /**
   * The current count this request event has been attempted
   * @return executionAttempt
   */
  @javax.annotation.Nullable
  public BigDecimal getExecutionAttempt() {
    return executionAttempt;
  }

  public void setExecutionAttempt(BigDecimal executionAttempt) {
    this.executionAttempt = executionAttempt;
  }


  public ConnectionEvent occurredAt(String occurredAt) {
    this.occurredAt = occurredAt;
    return this;
  }

  /**
   * ISO Datetime for when the original event occurred
   * @return occurredAt
   */
  @javax.annotation.Nullable
  public String getOccurredAt() {
    return occurredAt;
  }

  public void setOccurredAt(String occurredAt) {
    this.occurredAt = occurredAt;
  }


  public ConnectionEvent serviceId(String serviceId) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ConnectionEvent connectionEvent = (ConnectionEvent) o;
    return Objects.equals(this.entity, connectionEvent.entity) &&
        Objects.equals(this.entityId, connectionEvent.entityId) &&
        Objects.equals(this.entityType, connectionEvent.entityType) &&
        Objects.equals(this.eventId, connectionEvent.eventId) &&
        Objects.equals(this.eventType, connectionEvent.eventType) &&
        Objects.equals(this.executionAttempt, connectionEvent.executionAttempt) &&
        Objects.equals(this.occurredAt, connectionEvent.occurredAt) &&
        Objects.equals(this.serviceId, connectionEvent.serviceId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(entity, entityId, entityType, eventId, eventType, executionAttempt, occurredAt, serviceId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ConnectionEvent {\n");
    sb.append("    entity: ").append(toIndentedString(entity)).append("\n");
    sb.append("    entityId: ").append(toIndentedString(entityId)).append("\n");
    sb.append("    entityType: ").append(toIndentedString(entityType)).append("\n");
    sb.append("    eventId: ").append(toIndentedString(eventId)).append("\n");
    sb.append("    eventType: ").append(toIndentedString(eventType)).append("\n");
    sb.append("    executionAttempt: ").append(toIndentedString(executionAttempt)).append("\n");
    sb.append("    occurredAt: ").append(toIndentedString(occurredAt)).append("\n");
    sb.append("    serviceId: ").append(toIndentedString(serviceId)).append("\n");
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
    openapiFields.add("entity");
    openapiFields.add("entity_id");
    openapiFields.add("entity_type");
    openapiFields.add("event_id");
    openapiFields.add("event_type");
    openapiFields.add("execution_attempt");
    openapiFields.add("occurred_at");
    openapiFields.add("service_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ConnectionEvent
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ConnectionEvent.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ConnectionEvent is not found in the empty JSON string", ConnectionEvent.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ConnectionEvent.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ConnectionEvent` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `entity`
      if (jsonObj.get("entity") != null && !jsonObj.get("entity").isJsonNull()) {
        ConsumerConnection.validateJsonElement(jsonObj.get("entity"));
      }
      if ((jsonObj.get("entity_id") != null && !jsonObj.get("entity_id").isJsonNull()) && !jsonObj.get("entity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entity_id").toString()));
      }
      if ((jsonObj.get("entity_type") != null && !jsonObj.get("entity_type").isJsonNull()) && !jsonObj.get("entity_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entity_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entity_type").toString()));
      }
      if ((jsonObj.get("event_id") != null && !jsonObj.get("event_id").isJsonNull()) && !jsonObj.get("event_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `event_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("event_id").toString()));
      }
      // validate the optional field `event_type`
      if (jsonObj.get("event_type") != null && !jsonObj.get("event_type").isJsonNull()) {
        VaultEventType.validateJsonElement(jsonObj.get("event_type"));
      }
      if ((jsonObj.get("occurred_at") != null && !jsonObj.get("occurred_at").isJsonNull()) && !jsonObj.get("occurred_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `occurred_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("occurred_at").toString()));
      }
      if ((jsonObj.get("service_id") != null && !jsonObj.get("service_id").isJsonNull()) && !jsonObj.get("service_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ConnectionEvent.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ConnectionEvent' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ConnectionEvent> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ConnectionEvent.class));

       return (TypeAdapter<T>) new TypeAdapter<ConnectionEvent>() {
           @Override
           public void write(JsonWriter out, ConnectionEvent value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ConnectionEvent read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ConnectionEvent given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ConnectionEvent
   * @throws IOException if the JSON string is invalid with respect to ConnectionEvent
   */
  public static ConnectionEvent fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ConnectionEvent.class);
  }

  /**
   * Convert an instance of ConnectionEvent to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

