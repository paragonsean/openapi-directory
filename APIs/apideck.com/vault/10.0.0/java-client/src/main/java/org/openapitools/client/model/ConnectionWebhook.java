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
import java.net.URI;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.UnifiedApiId;
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
 * ConnectionWebhook
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:50.743494-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ConnectionWebhook {
  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DELIVERY_URL = "delivery_url";
  @SerializedName(SERIALIZED_NAME_DELIVERY_URL)
  private URI deliveryUrl;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  /**
   * Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it&#39;s plan.
   */
  @JsonAdapter(DisabledReasonEnum.Adapter.class)
  public enum DisabledReasonEnum {
    NONE("none"),
    
    RETRY_LIMIT("retry_limit"),
    
    USAGE_LIMIT("usage_limit");

    private String value;

    DisabledReasonEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DisabledReasonEnum fromValue(String value) {
      for (DisabledReasonEnum b : DisabledReasonEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DisabledReasonEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DisabledReasonEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DisabledReasonEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DisabledReasonEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DisabledReasonEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DISABLED_REASON = "disabled_reason";
  @SerializedName(SERIALIZED_NAME_DISABLED_REASON)
  private DisabledReasonEnum disabledReason;

  /**
   * Gets or Sets events
   */
  @JsonAdapter(EventsEnum.Adapter.class)
  public enum EventsEnum {
    STAR("*"),
    
    CRM_ACTIVITY_CREATED("crm.activity.created"),
    
    CRM_ACTIVITY_UPDATED("crm.activity.updated"),
    
    CRM_ACTIVITY_DELETED("crm.activity.deleted"),
    
    CRM_COMPANY_CREATED("crm.company.created"),
    
    CRM_COMPANY_UPDATED("crm.company.updated"),
    
    CRM_COMPANY_DELETED("crm.company.deleted"),
    
    CRM_CONTACT_CREATED("crm.contact.created"),
    
    CRM_CONTACT_UPDATED("crm.contact.updated"),
    
    CRM_CONTACT_DELETED("crm.contact.deleted"),
    
    CRM_LEAD_CREATED("crm.lead.created"),
    
    CRM_LEAD_UPDATED("crm.lead.updated"),
    
    CRM_LEAD_DELETED("crm.lead.deleted"),
    
    CRM_NOTE_CREATED("crm.note.created"),
    
    CRM_NOTES_UPDATED("crm.notes.updated"),
    
    CRM_NOTES_DELETED("crm.notes.deleted"),
    
    CRM_OPPORTUNITY_CREATED("crm.opportunity.created"),
    
    CRM_OPPORTUNITY_UPDATED("crm.opportunity.updated"),
    
    CRM_OPPORTUNITY_DELETED("crm.opportunity.deleted"),
    
    LEAD_LEAD_CREATED("lead.lead.created"),
    
    LEAD_LEAD_UPDATED("lead.lead.updated"),
    
    LEAD_LEAD_DELETED("lead.lead.deleted"),
    
    VAULT_CONNECTION_CREATED("vault.connection.created"),
    
    VAULT_CONNECTION_UPDATED("vault.connection.updated"),
    
    VAULT_CONNECTION_DISABLED("vault.connection.disabled"),
    
    VAULT_CONNECTION_DELETED("vault.connection.deleted"),
    
    VAULT_CONNECTION_CALLABLE("vault.connection.callable"),
    
    VAULT_CONNECTION_REVOKED("vault.connection.revoked"),
    
    VAULT_CONNECTION_TOKEN_REFRESH_FAILED("vault.connection.token_refresh.failed"),
    
    ATS_JOB_CREATED("ats.job.created"),
    
    ATS_JOB_UPDATED("ats.job.updated"),
    
    ATS_JOB_DELETED("ats.job.deleted"),
    
    ATS_APPLICANT_CREATED("ats.applicant.created"),
    
    ATS_APPLICANT_UPDATED("ats.applicant.updated"),
    
    ATS_APPLICANT_DELETED("ats.applicant.deleted"),
    
    ACCOUNTING_CUSTOMER_CREATED("accounting.customer.created"),
    
    ACCOUNTING_CUSTOMER_UPDATED("accounting.customer.updated"),
    
    ACCOUNTING_CUSTOMER_DELETED("accounting.customer.deleted"),
    
    ACCOUNTING_INVOICE_CREATED("accounting.invoice.created"),
    
    ACCOUNTING_INVOICE_UPDATED("accounting.invoice.updated"),
    
    ACCOUNTING_INVOICE_DELETED("accounting.invoice.deleted"),
    
    ACCOUNTING_INVOICE_ITEM_CREATED("accounting.invoice_item.created"),
    
    ACCOUNTING_INVOICE_ITEM_UPDATED("accounting.invoice_item.updated"),
    
    ACCOUNTING_INVOICE_ITEM_DELETED("accounting.invoice_item.deleted"),
    
    ACCOUNTING_LEDGER_ACCOUNT_CREATED("accounting.ledger_account.created"),
    
    ACCOUNTING_LEDGER_ACCOUNT_UPDATED("accounting.ledger_account.updated"),
    
    ACCOUNTING_LEDGER_ACCOUNT_DELETED("accounting.ledger_account.deleted"),
    
    ACCOUNTING_TAX_RATE_CREATED("accounting.tax_rate.created"),
    
    ACCOUNTING_TAX_RATE_UPDATED("accounting.tax_rate.updated"),
    
    ACCOUNTING_TAX_RATE_DELETED("accounting.tax_rate.deleted"),
    
    ACCOUNTING_BILL_CREATED("accounting.bill.created"),
    
    ACCOUNTING_BILL_UPDATED("accounting.bill.updated"),
    
    ACCOUNTING_BILL_DELETED("accounting.bill.deleted"),
    
    ACCOUNTING_PAYMENT_CREATED("accounting.payment.created"),
    
    ACCOUNTING_PAYMENT_UPDATED("accounting.payment.updated"),
    
    ACCOUNTING_PAYMENT_DELETED("accounting.payment.deleted"),
    
    ACCOUNTING_SUPPLIER_CREATED("accounting.supplier.created"),
    
    ACCOUNTING_SUPPLIER_UPDATED("accounting.supplier.updated"),
    
    ACCOUNTING_SUPPLIER_DELETED("accounting.supplier.deleted"),
    
    ACCOUNTING_PURCHASE_ORDER_CREATED("accounting.purchase-order.created"),
    
    ACCOUNTING_PURCHASE_ORDER_UPDATED("accounting.purchase-order.updated"),
    
    ACCOUNTING_PURCHASE_ORDER_DELETED("accounting.purchase-order.deleted"),
    
    POS_ORDER_CREATED("pos.order.created"),
    
    POS_ORDER_UPDATED("pos.order.updated"),
    
    POS_ORDER_DELETED("pos.order.deleted"),
    
    POS_PRODUCT_CREATED("pos.product.created"),
    
    POS_PRODUCT_UPDATED("pos.product.updated"),
    
    POS_PRODUCT_DELETED("pos.product.deleted"),
    
    POS_PAYMENT_CREATED("pos.payment.created"),
    
    POS_PAYMENT_UPDATED("pos.payment.updated"),
    
    POS_PAYMENT_DELETED("pos.payment.deleted"),
    
    POS_MERCHANT_CREATED("pos.merchant.created"),
    
    POS_MERCHANT_UPDATED("pos.merchant.updated"),
    
    POS_MERCHANT_DELETED("pos.merchant.deleted"),
    
    POS_LOCATION_CREATED("pos.location.created"),
    
    POS_LOCATION_UPDATED("pos.location.updated"),
    
    POS_LOCATION_DELETED("pos.location.deleted"),
    
    POS_ITEM_CREATED("pos.item.created"),
    
    POS_ITEM_UPDATED("pos.item.updated"),
    
    POS_ITEM_DELETED("pos.item.deleted"),
    
    POS_MODIFIER_CREATED("pos.modifier.created"),
    
    POS_MODIFIER_UPDATED("pos.modifier.updated"),
    
    POS_MODIFIER_DELETED("pos.modifier.deleted"),
    
    POS_MODIFIER_GROUP_CREATED("pos.modifier-group.created"),
    
    POS_MODIFIER_GROUP_UPDATED("pos.modifier-group.updated"),
    
    POS_MODIFIER_GROUP_DELETED("pos.modifier-group.deleted"),
    
    HRIS_EMPLOYEE_CREATED("hris.employee.created"),
    
    HRIS_EMPLOYEE_UPDATED("hris.employee.updated"),
    
    HRIS_EMPLOYEE_DELETED("hris.employee.deleted"),
    
    HRIS_EMPLOYEE_TERMINATED("hris.employee.terminated"),
    
    HRIS_COMPANY_CREATED("hris.company.created"),
    
    HRIS_COMPANY_UPDATED("hris.company.updated"),
    
    HRIS_COMPANY_DELETED("hris.company.deleted"),
    
    FILE_STORAGE_FILE_CREATED("file-storage.file.created"),
    
    FILE_STORAGE_FILE_UPDATED("file-storage.file.updated"),
    
    FILE_STORAGE_FILE_DELETED("file-storage.file.deleted"),
    
    ISSUE_TRACKING_TICKET_CREATED("issue-tracking.ticket.created"),
    
    ISSUE_TRACKING_TICKET_UPDATED("issue-tracking.ticket.updated"),
    
    ISSUE_TRACKING_TICKET_DELETED("issue-tracking.ticket.deleted"),
    
    ATS_APPLICATION_CREATED("ats.application.created"),
    
    ATS_APPLICATION_UPDATED("ats.application.updated"),
    
    ATS_APPLICATION_DELETED("ats.application.deleted");

    private String value;

    EventsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EventsEnum fromValue(String value) {
      for (EventsEnum b : EventsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EventsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EventsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EventsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EventsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EventsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EVENTS = "events";
  @SerializedName(SERIALIZED_NAME_EVENTS)
  private List<EventsEnum> events = new ArrayList<>();

  public static final String SERIALIZED_NAME_EXECUTE_BASE_URL = "execute_base_url";
  @SerializedName(SERIALIZED_NAME_EXECUTE_BASE_URL)
  private URI executeBaseUrl;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  /**
   * The status of the webhook.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    ENABLED("enabled"),
    
    DISABLED("disabled");

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

  public static final String SERIALIZED_NAME_UNIFIED_API = "unified_api";
  @SerializedName(SERIALIZED_NAME_UNIFIED_API)
  private UnifiedApiId unifiedApi;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public ConnectionWebhook() {
  }

  public ConnectionWebhook(
     OffsetDateTime createdAt, 
     URI executeBaseUrl, 
     String id, 
     OffsetDateTime updatedAt
  ) {
    this();
    this.createdAt = createdAt;
    this.executeBaseUrl = executeBaseUrl;
    this.id = id;
    this.updatedAt = updatedAt;
  }

  /**
   * The date and time when the object was created.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }



  public ConnectionWebhook deliveryUrl(URI deliveryUrl) {
    this.deliveryUrl = deliveryUrl;
    return this;
  }

  /**
   * The delivery url of the webhook endpoint.
   * @return deliveryUrl
   */
  @javax.annotation.Nonnull
  public URI getDeliveryUrl() {
    return deliveryUrl;
  }

  public void setDeliveryUrl(URI deliveryUrl) {
    this.deliveryUrl = deliveryUrl;
  }


  public ConnectionWebhook description(String description) {
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


  public ConnectionWebhook disabledReason(DisabledReasonEnum disabledReason) {
    this.disabledReason = disabledReason;
    return this;
  }

  /**
   * Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it&#39;s plan.
   * @return disabledReason
   */
  @javax.annotation.Nullable
  public DisabledReasonEnum getDisabledReason() {
    return disabledReason;
  }

  public void setDisabledReason(DisabledReasonEnum disabledReason) {
    this.disabledReason = disabledReason;
  }


  public ConnectionWebhook events(List<EventsEnum> events) {
    this.events = events;
    return this;
  }

  public ConnectionWebhook addEventsItem(EventsEnum eventsItem) {
    if (this.events == null) {
      this.events = new ArrayList<>();
    }
    this.events.add(eventsItem);
    return this;
  }

  /**
   * The list of subscribed events for this webhook. [&#x60;*&#x60;] indicates that all events are enabled.
   * @return events
   */
  @javax.annotation.Nonnull
  public List<EventsEnum> getEvents() {
    return events;
  }

  public void setEvents(List<EventsEnum> events) {
    this.events = events;
  }


  /**
   * The Unify Base URL events from connectors will be sent to after service id is appended.
   * @return executeBaseUrl
   */
  @javax.annotation.Nonnull
  public URI getExecuteBaseUrl() {
    return executeBaseUrl;
  }



  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public ConnectionWebhook status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * The status of the webhook.
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public ConnectionWebhook unifiedApi(UnifiedApiId unifiedApi) {
    this.unifiedApi = unifiedApi;
    return this;
  }

  /**
   * Get unifiedApi
   * @return unifiedApi
   */
  @javax.annotation.Nonnull
  public UnifiedApiId getUnifiedApi() {
    return unifiedApi;
  }

  public void setUnifiedApi(UnifiedApiId unifiedApi) {
    this.unifiedApi = unifiedApi;
  }


  /**
   * The date and time when the object was last updated.
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ConnectionWebhook connectionWebhook = (ConnectionWebhook) o;
    return Objects.equals(this.createdAt, connectionWebhook.createdAt) &&
        Objects.equals(this.deliveryUrl, connectionWebhook.deliveryUrl) &&
        Objects.equals(this.description, connectionWebhook.description) &&
        Objects.equals(this.disabledReason, connectionWebhook.disabledReason) &&
        Objects.equals(this.events, connectionWebhook.events) &&
        Objects.equals(this.executeBaseUrl, connectionWebhook.executeBaseUrl) &&
        Objects.equals(this.id, connectionWebhook.id) &&
        Objects.equals(this.status, connectionWebhook.status) &&
        Objects.equals(this.unifiedApi, connectionWebhook.unifiedApi) &&
        Objects.equals(this.updatedAt, connectionWebhook.updatedAt);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, deliveryUrl, description, disabledReason, events, executeBaseUrl, id, status, unifiedApi, updatedAt);
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
    sb.append("class ConnectionWebhook {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    deliveryUrl: ").append(toIndentedString(deliveryUrl)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    disabledReason: ").append(toIndentedString(disabledReason)).append("\n");
    sb.append("    events: ").append(toIndentedString(events)).append("\n");
    sb.append("    executeBaseUrl: ").append(toIndentedString(executeBaseUrl)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    unifiedApi: ").append(toIndentedString(unifiedApi)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("created_at");
    openapiFields.add("delivery_url");
    openapiFields.add("description");
    openapiFields.add("disabled_reason");
    openapiFields.add("events");
    openapiFields.add("execute_base_url");
    openapiFields.add("id");
    openapiFields.add("status");
    openapiFields.add("unified_api");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("delivery_url");
    openapiRequiredFields.add("events");
    openapiRequiredFields.add("execute_base_url");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("unified_api");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ConnectionWebhook
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ConnectionWebhook.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ConnectionWebhook is not found in the empty JSON string", ConnectionWebhook.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ConnectionWebhook.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ConnectionWebhook` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ConnectionWebhook.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("delivery_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `delivery_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("delivery_url").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("disabled_reason") != null && !jsonObj.get("disabled_reason").isJsonNull()) && !jsonObj.get("disabled_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `disabled_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("disabled_reason").toString()));
      }
      // validate the optional field `disabled_reason`
      if (jsonObj.get("disabled_reason") != null && !jsonObj.get("disabled_reason").isJsonNull()) {
        DisabledReasonEnum.validateJsonElement(jsonObj.get("disabled_reason"));
      }
      // ensure the required json array is present
      if (jsonObj.get("events") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("events").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `events` to be an array in the JSON string but got `%s`", jsonObj.get("events").toString()));
      }
      if (!jsonObj.get("execute_base_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `execute_base_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("execute_base_url").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      // validate the required field `unified_api`
      UnifiedApiId.validateJsonElement(jsonObj.get("unified_api"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ConnectionWebhook.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ConnectionWebhook' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ConnectionWebhook> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ConnectionWebhook.class));

       return (TypeAdapter<T>) new TypeAdapter<ConnectionWebhook>() {
           @Override
           public void write(JsonWriter out, ConnectionWebhook value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ConnectionWebhook read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ConnectionWebhook given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ConnectionWebhook
   * @throws IOException if the JSON string is invalid with respect to ConnectionWebhook
   */
  public static ConnectionWebhook fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ConnectionWebhook.class);
  }

  /**
   * Convert an instance of ConnectionWebhook to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

