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
import java.util.List;
import org.openapitools.client.model.ConsumerMetadata;
import org.openapitools.client.model.RequestCountAllocation;

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
 * GetConsumersResponseDataInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:50.743494-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetConsumersResponseDataInner {
  public static final String SERIALIZED_NAME_AGGREGATED_REQUEST_COUNT = "aggregated_request_count";
  @SerializedName(SERIALIZED_NAME_AGGREGATED_REQUEST_COUNT)
  private BigDecimal aggregatedRequestCount;

  public static final String SERIALIZED_NAME_APPLICATION_ID = "application_id";
  @SerializedName(SERIALIZED_NAME_APPLICATION_ID)
  private String applicationId;

  public static final String SERIALIZED_NAME_CONSUMER_ID = "consumer_id";
  @SerializedName(SERIALIZED_NAME_CONSUMER_ID)
  private String consumerId;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private ConsumerMetadata metadata;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_REQUEST_COUNT_UPDATED = "request_count_updated";
  @SerializedName(SERIALIZED_NAME_REQUEST_COUNT_UPDATED)
  private String requestCountUpdated;

  public static final String SERIALIZED_NAME_REQUEST_COUNTS = "request_counts";
  @SerializedName(SERIALIZED_NAME_REQUEST_COUNTS)
  private RequestCountAllocation requestCounts;

  public static final String SERIALIZED_NAME_SERVICES = "services";
  @SerializedName(SERIALIZED_NAME_SERVICES)
  private List<String> services = new ArrayList<>();

  public GetConsumersResponseDataInner() {
  }

  public GetConsumersResponseDataInner aggregatedRequestCount(BigDecimal aggregatedRequestCount) {
    this.aggregatedRequestCount = aggregatedRequestCount;
    return this;
  }

  /**
   * Get aggregatedRequestCount
   * @return aggregatedRequestCount
   */
  @javax.annotation.Nullable
  public BigDecimal getAggregatedRequestCount() {
    return aggregatedRequestCount;
  }

  public void setAggregatedRequestCount(BigDecimal aggregatedRequestCount) {
    this.aggregatedRequestCount = aggregatedRequestCount;
  }


  public GetConsumersResponseDataInner applicationId(String applicationId) {
    this.applicationId = applicationId;
    return this;
  }

  /**
   * Get applicationId
   * @return applicationId
   */
  @javax.annotation.Nullable
  public String getApplicationId() {
    return applicationId;
  }

  public void setApplicationId(String applicationId) {
    this.applicationId = applicationId;
  }


  public GetConsumersResponseDataInner consumerId(String consumerId) {
    this.consumerId = consumerId;
    return this;
  }

  /**
   * Get consumerId
   * @return consumerId
   */
  @javax.annotation.Nullable
  public String getConsumerId() {
    return consumerId;
  }

  public void setConsumerId(String consumerId) {
    this.consumerId = consumerId;
  }


  public GetConsumersResponseDataInner created(String created) {
    this.created = created;
    return this;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }

  public void setCreated(String created) {
    this.created = created;
  }


  public GetConsumersResponseDataInner metadata(ConsumerMetadata metadata) {
    this.metadata = metadata;
    return this;
  }

  /**
   * Get metadata
   * @return metadata
   */
  @javax.annotation.Nullable
  public ConsumerMetadata getMetadata() {
    return metadata;
  }

  public void setMetadata(ConsumerMetadata metadata) {
    this.metadata = metadata;
  }


  public GetConsumersResponseDataInner modified(String modified) {
    this.modified = modified;
    return this;
  }

  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }

  public void setModified(String modified) {
    this.modified = modified;
  }


  public GetConsumersResponseDataInner requestCountUpdated(String requestCountUpdated) {
    this.requestCountUpdated = requestCountUpdated;
    return this;
  }

  /**
   * Get requestCountUpdated
   * @return requestCountUpdated
   */
  @javax.annotation.Nullable
  public String getRequestCountUpdated() {
    return requestCountUpdated;
  }

  public void setRequestCountUpdated(String requestCountUpdated) {
    this.requestCountUpdated = requestCountUpdated;
  }


  public GetConsumersResponseDataInner requestCounts(RequestCountAllocation requestCounts) {
    this.requestCounts = requestCounts;
    return this;
  }

  /**
   * Get requestCounts
   * @return requestCounts
   */
  @javax.annotation.Nullable
  public RequestCountAllocation getRequestCounts() {
    return requestCounts;
  }

  public void setRequestCounts(RequestCountAllocation requestCounts) {
    this.requestCounts = requestCounts;
  }


  public GetConsumersResponseDataInner services(List<String> services) {
    this.services = services;
    return this;
  }

  public GetConsumersResponseDataInner addServicesItem(String servicesItem) {
    if (this.services == null) {
      this.services = new ArrayList<>();
    }
    this.services.add(servicesItem);
    return this;
  }

  /**
   * Get services
   * @return services
   */
  @javax.annotation.Nullable
  public List<String> getServices() {
    return services;
  }

  public void setServices(List<String> services) {
    this.services = services;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetConsumersResponseDataInner getConsumersResponseDataInner = (GetConsumersResponseDataInner) o;
    return Objects.equals(this.aggregatedRequestCount, getConsumersResponseDataInner.aggregatedRequestCount) &&
        Objects.equals(this.applicationId, getConsumersResponseDataInner.applicationId) &&
        Objects.equals(this.consumerId, getConsumersResponseDataInner.consumerId) &&
        Objects.equals(this.created, getConsumersResponseDataInner.created) &&
        Objects.equals(this.metadata, getConsumersResponseDataInner.metadata) &&
        Objects.equals(this.modified, getConsumersResponseDataInner.modified) &&
        Objects.equals(this.requestCountUpdated, getConsumersResponseDataInner.requestCountUpdated) &&
        Objects.equals(this.requestCounts, getConsumersResponseDataInner.requestCounts) &&
        Objects.equals(this.services, getConsumersResponseDataInner.services);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aggregatedRequestCount, applicationId, consumerId, created, metadata, modified, requestCountUpdated, requestCounts, services);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetConsumersResponseDataInner {\n");
    sb.append("    aggregatedRequestCount: ").append(toIndentedString(aggregatedRequestCount)).append("\n");
    sb.append("    applicationId: ").append(toIndentedString(applicationId)).append("\n");
    sb.append("    consumerId: ").append(toIndentedString(consumerId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    requestCountUpdated: ").append(toIndentedString(requestCountUpdated)).append("\n");
    sb.append("    requestCounts: ").append(toIndentedString(requestCounts)).append("\n");
    sb.append("    services: ").append(toIndentedString(services)).append("\n");
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
    openapiFields.add("aggregated_request_count");
    openapiFields.add("application_id");
    openapiFields.add("consumer_id");
    openapiFields.add("created");
    openapiFields.add("metadata");
    openapiFields.add("modified");
    openapiFields.add("request_count_updated");
    openapiFields.add("request_counts");
    openapiFields.add("services");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetConsumersResponseDataInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetConsumersResponseDataInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetConsumersResponseDataInner is not found in the empty JSON string", GetConsumersResponseDataInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetConsumersResponseDataInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetConsumersResponseDataInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("application_id") != null && !jsonObj.get("application_id").isJsonNull()) && !jsonObj.get("application_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `application_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("application_id").toString()));
      }
      if ((jsonObj.get("consumer_id") != null && !jsonObj.get("consumer_id").isJsonNull()) && !jsonObj.get("consumer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consumer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consumer_id").toString()));
      }
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      // validate the optional field `metadata`
      if (jsonObj.get("metadata") != null && !jsonObj.get("metadata").isJsonNull()) {
        ConsumerMetadata.validateJsonElement(jsonObj.get("metadata"));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("request_count_updated") != null && !jsonObj.get("request_count_updated").isJsonNull()) && !jsonObj.get("request_count_updated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `request_count_updated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("request_count_updated").toString()));
      }
      // validate the optional field `request_counts`
      if (jsonObj.get("request_counts") != null && !jsonObj.get("request_counts").isJsonNull()) {
        RequestCountAllocation.validateJsonElement(jsonObj.get("request_counts"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("services") != null && !jsonObj.get("services").isJsonNull() && !jsonObj.get("services").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `services` to be an array in the JSON string but got `%s`", jsonObj.get("services").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetConsumersResponseDataInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetConsumersResponseDataInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetConsumersResponseDataInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetConsumersResponseDataInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetConsumersResponseDataInner>() {
           @Override
           public void write(JsonWriter out, GetConsumersResponseDataInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetConsumersResponseDataInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetConsumersResponseDataInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetConsumersResponseDataInner
   * @throws IOException if the JSON string is invalid with respect to GetConsumersResponseDataInner
   */
  public static GetConsumersResponseDataInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetConsumersResponseDataInner.class);
  }

  /**
   * Convert an instance of GetConsumersResponseDataInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

