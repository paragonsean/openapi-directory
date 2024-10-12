# openapi-java-client

Vault API
- API version: 10.0.0
  - Build date: 2024-10-12T11:57:50.743494-04:00[America/New_York]
  - Generator version: 7.9.0

Welcome to the Vault API 👋

When you're looking to connect to an API, the first step is authentication.

Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).

## Base URL

The base URL for all API requests is `https://unify.apideck.com`

## Get Started

To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.

- [Create a free account.](https://app.apideck.com/signup)
- Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard).
- Get your API key and the application ID.
- Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations.
- Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations).
- Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming)
- Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings
- Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.

### Hosted Vault

Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.

![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)

Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:

- Add a connection
- Handle the OAuth flow
- Configure connection settings per integration
- Manage connections
- Discover and propose integration options
- Search for integrations (upcoming)
- Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)

To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.

Example using curl:

```
curl -X POST https://unify.apideck.com/vault/sessions
    -H \"Content-Type: application/json\"
    -H \"Authorization: Bearer <your-api-key>\"
    -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"
    -H \"X-APIDECK-APP-ID: <application-id>\"
    -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}'
```

### Vault API

_Beware, this is strategy takes more time to implement in comparison to Hosted Vault._

If you are building your integration settings UI manually, you can call the Vault API directly.

The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.

Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.

If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).

## Domain model

At its core, a domain model creates a web of interconnected entities.

Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.

## Connection state

The connection state is computed based on the connection flow below.

![](https://developers.apideck.com/api-references/vault/connection-flow.png)

More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.

## Unify and Proxy integration

The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).

## Headers

Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.

| Name                  | Type    | Required | Description |
| --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. |
| x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. |
| x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |

## Guides

- [Get started with Apideck](https://developers.apideck.com/getting-started)
- [Get started with Vault](https://developers.apideck.com/guides/vault)
- [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections)
- [Vault connection status](https://developers.apideck.com/guides/connection-states)
- [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)


## FAQ

**What purpose does Vault serve? Can I just handle the authentication and access token myself?**
You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.

### Is my data secure?

Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.

### How do I migrate existing data?

Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.

### Can I use Vault in combination with existing integrations?

Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.

### How does Vault work for Apideck Ecosystem customers?

Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.

### How to integrate Apideck Vault

This section covers everything you need to know to authenticate your customers through Vault.
Vault provides **three auth strategies** to use API tokens from your customers:

- Vault API
- Hosted Vault
- Vault Widget (JS, React, Vue)

You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.

### What auth types does Vault support?

We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.

#### API keys

For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.

#### OAuth 2.0

##### Authorization Code Grant Type Flow

Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.

Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.

This is being handled by the `/authorize` endpoint.

#### Basic auth

Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.



  For more information, please visit [https://developers.apideck.com](https://developers.apideck.com)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>10.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:10.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-10.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String unifiedApi = "crm"; // String | Unified API
    String serviceId = "pipedrive"; // String | Service ID of the resource to return
    String resource = "leads"; // String | Name of the resource (plural)
    try {
      GetConnectionResponse result = apiInstance.connectionSettingsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionSettingsAll");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://unify.apideck.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConnectionsApi* | [**connectionSettingsAll**](docs/ConnectionsApi.md#connectionSettingsAll) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/config | Get resource settings
*ConnectionsApi* | [**connectionSettingsUpdate**](docs/ConnectionsApi.md#connectionSettingsUpdate) | **PATCH** /vault/connections/{unified_api}/{service_id}/{resource}/config | Update settings
*ConnectionsApi* | [**connectionsAdd**](docs/ConnectionsApi.md#connectionsAdd) | **POST** /vault/connections/{unified_api}/{service_id} | Create connection
*ConnectionsApi* | [**connectionsAll**](docs/ConnectionsApi.md#connectionsAll) | **GET** /vault/connections | Get all connections
*ConnectionsApi* | [**connectionsAuthorize**](docs/ConnectionsApi.md#connectionsAuthorize) | **GET** /vault/authorize/{service_id}/{application_id} | Authorize
*ConnectionsApi* | [**connectionsCallback**](docs/ConnectionsApi.md#connectionsCallback) | **GET** /vault/callback | Callback
*ConnectionsApi* | [**connectionsDelete**](docs/ConnectionsApi.md#connectionsDelete) | **DELETE** /vault/connections/{unified_api}/{service_id} | Deletes a connection
*ConnectionsApi* | [**connectionsImport**](docs/ConnectionsApi.md#connectionsImport) | **POST** /vault/connections/{unified_api}/{service_id}/import | Import connection
*ConnectionsApi* | [**connectionsOne**](docs/ConnectionsApi.md#connectionsOne) | **GET** /vault/connections/{unified_api}/{service_id} | Get connection
*ConnectionsApi* | [**connectionsRevoke**](docs/ConnectionsApi.md#connectionsRevoke) | **GET** /vault/revoke/{service_id}/{application_id} | Revoke connection
*ConnectionsApi* | [**connectionsToken**](docs/ConnectionsApi.md#connectionsToken) | **POST** /vault/connections/{unified_api}/{service_id}/token | Get Access Token
*ConnectionsApi* | [**connectionsUpdate**](docs/ConnectionsApi.md#connectionsUpdate) | **PATCH** /vault/connections/{unified_api}/{service_id} | Update connection
*ConnectionsApi* | [**customFieldsAll**](docs/ConnectionsApi.md#customFieldsAll) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/custom-fields | Get resource custom fields
*ConsumersApi* | [**consumerRequestCountsAll**](docs/ConsumersApi.md#consumerRequestCountsAll) | **GET** /vault/consumers/{consumer_id}/stats | Consumer request counts
*ConsumersApi* | [**consumersAdd**](docs/ConsumersApi.md#consumersAdd) | **POST** /vault/consumers | Create consumer
*ConsumersApi* | [**consumersAll**](docs/ConsumersApi.md#consumersAll) | **GET** /vault/consumers | Get all consumers
*ConsumersApi* | [**consumersDelete**](docs/ConsumersApi.md#consumersDelete) | **DELETE** /vault/consumers/{consumer_id} | Delete consumer
*ConsumersApi* | [**consumersOne**](docs/ConsumersApi.md#consumersOne) | **GET** /vault/consumers/{consumer_id} | Get consumer
*ConsumersApi* | [**consumersUpdate**](docs/ConsumersApi.md#consumersUpdate) | **PATCH** /vault/consumers/{consumer_id} | Update consumer
*LogsApi* | [**logsAll**](docs/LogsApi.md#logsAll) | **GET** /vault/logs | Get all consumer request logs
*SessionsApi* | [**sessionsCreate**](docs/SessionsApi.md#sessionsCreate) | **POST** /vault/sessions | Create Session


## Documentation for Models

 - [AuthType](docs/AuthType.md)
 - [BadRequestResponse](docs/BadRequestResponse.md)
 - [BadRequestResponseDetail](docs/BadRequestResponseDetail.md)
 - [Connection](docs/Connection.md)
 - [ConnectionConfigurationInner](docs/ConnectionConfigurationInner.md)
 - [ConnectionConfigurationInnerDefaultsInner](docs/ConnectionConfigurationInnerDefaultsInner.md)
 - [ConnectionConfigurationInnerDefaultsInnerValue](docs/ConnectionConfigurationInnerDefaultsInnerValue.md)
 - [ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner](docs/ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner.md)
 - [ConnectionEvent](docs/ConnectionEvent.md)
 - [ConnectionImportData](docs/ConnectionImportData.md)
 - [ConnectionImportDataCredentials](docs/ConnectionImportDataCredentials.md)
 - [ConnectionMetadata](docs/ConnectionMetadata.md)
 - [ConnectionState](docs/ConnectionState.md)
 - [ConnectionWebhook](docs/ConnectionWebhook.md)
 - [Consumer](docs/Consumer.md)
 - [ConsumerConnection](docs/ConsumerConnection.md)
 - [ConsumerMetadata](docs/ConsumerMetadata.md)
 - [ConsumerRequestCountsInDateRangeResponse](docs/ConsumerRequestCountsInDateRangeResponse.md)
 - [ConsumerRequestCountsInDateRangeResponseData](docs/ConsumerRequestCountsInDateRangeResponseData.md)
 - [CreateConnectionResponse](docs/CreateConnectionResponse.md)
 - [CreateConsumerResponse](docs/CreateConsumerResponse.md)
 - [CreateCustomMappingRequest](docs/CreateCustomMappingRequest.md)
 - [CreateCustomMappingResponse](docs/CreateCustomMappingResponse.md)
 - [CreateSessionResponse](docs/CreateSessionResponse.md)
 - [CreateSessionResponseData](docs/CreateSessionResponseData.md)
 - [CustomFieldFinder](docs/CustomFieldFinder.md)
 - [CustomMapping](docs/CustomMapping.md)
 - [DeleteConsumerResponse](docs/DeleteConsumerResponse.md)
 - [DeleteConsumerResponseData](docs/DeleteConsumerResponseData.md)
 - [FormField](docs/FormField.md)
 - [FormFieldOption](docs/FormFieldOption.md)
 - [FormFieldOptionGroup](docs/FormFieldOptionGroup.md)
 - [GetConnectionResponse](docs/GetConnectionResponse.md)
 - [GetConnectionsResponse](docs/GetConnectionsResponse.md)
 - [GetConsumerResponse](docs/GetConsumerResponse.md)
 - [GetConsumersResponse](docs/GetConsumersResponse.md)
 - [GetConsumersResponseDataInner](docs/GetConsumersResponseDataInner.md)
 - [GetCustomFieldsResponse](docs/GetCustomFieldsResponse.md)
 - [GetCustomMappingResponse](docs/GetCustomMappingResponse.md)
 - [GetLogsResponse](docs/GetLogsResponse.md)
 - [GetResourceExampleResponse](docs/GetResourceExampleResponse.md)
 - [GetResourceSchemaResponse](docs/GetResourceSchemaResponse.md)
 - [IntegrationState](docs/IntegrationState.md)
 - [LinkedConnectorResource](docs/LinkedConnectorResource.md)
 - [Links](docs/Links.md)
 - [Log](docs/Log.md)
 - [LogOperation](docs/LogOperation.md)
 - [LogService](docs/LogService.md)
 - [LogsFilter](docs/LogsFilter.md)
 - [Meta](docs/Meta.md)
 - [MetaCursors](docs/MetaCursors.md)
 - [NotFoundResponse](docs/NotFoundResponse.md)
 - [NotFoundResponseDetail](docs/NotFoundResponseDetail.md)
 - [NotImplementedResponse](docs/NotImplementedResponse.md)
 - [NotImplementedResponseDetail](docs/NotImplementedResponseDetail.md)
 - [OAuthGrantType](docs/OAuthGrantType.md)
 - [PaymentRequiredResponse](docs/PaymentRequiredResponse.md)
 - [RequestCountAllocation](docs/RequestCountAllocation.md)
 - [ResourceExample](docs/ResourceExample.md)
 - [ResourceStatus](docs/ResourceStatus.md)
 - [Session](docs/Session.md)
 - [SessionSettings](docs/SessionSettings.md)
 - [SessionTheme](docs/SessionTheme.md)
 - [SimpleFormFieldOption](docs/SimpleFormFieldOption.md)
 - [SimpleFormFieldOptionValue](docs/SimpleFormFieldOptionValue.md)
 - [SimpleFormFieldOptionValueAnyOfInner](docs/SimpleFormFieldOptionValueAnyOfInner.md)
 - [UnauthorizedResponse](docs/UnauthorizedResponse.md)
 - [UnexpectedErrorResponse](docs/UnexpectedErrorResponse.md)
 - [UnexpectedErrorResponseDetail](docs/UnexpectedErrorResponseDetail.md)
 - [UnifiedApiId](docs/UnifiedApiId.md)
 - [UnprocessableResponse](docs/UnprocessableResponse.md)
 - [UpdateConnectionResponse](docs/UpdateConnectionResponse.md)
 - [UpdateConsumerRequest](docs/UpdateConsumerRequest.md)
 - [UpdateConsumerResponse](docs/UpdateConsumerResponse.md)
 - [UpdateCustomMappingRequest](docs/UpdateCustomMappingRequest.md)
 - [UpdateCustomMappingResponse](docs/UpdateCustomMappingResponse.md)
 - [VaultEventType](docs/VaultEventType.md)
 - [WebhookSubscription](docs/WebhookSubscription.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
### apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="applicationId"></a>
### applicationId

- **Type**: API key
- **API key parameter name**: x-apideck-app-id
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

hello@apideck.com

