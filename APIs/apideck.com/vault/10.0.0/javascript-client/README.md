# vault_api

VaultApi - JavaScript client for vault_api
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


This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 10.0.0
- Package version: 10.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://developers.apideck.com](https://developers.apideck.com)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install vault_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your vault_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var VaultApi = require('vault_api');

var defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
var apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix['Authorization'] = "Token"

var api = new VaultApi.ConnectionsApi()
var xApideckConsumerId = "xApideckConsumerId_example"; // {String} ID of the consumer which you want to get or push data from
var xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // {String} The ID of your Unify application
var unifiedApi = "crm"; // {String} Unified API
var serviceId = "pipedrive"; // {String} Service ID of the resource to return
var resource = "leads"; // {String} Name of the resource (plural)
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.connectionSettingsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://unify.apideck.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*VaultApi.ConnectionsApi* | [**connectionSettingsAll**](docs/ConnectionsApi.md#connectionSettingsAll) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/config | Get resource settings
*VaultApi.ConnectionsApi* | [**connectionSettingsUpdate**](docs/ConnectionsApi.md#connectionSettingsUpdate) | **PATCH** /vault/connections/{unified_api}/{service_id}/{resource}/config | Update settings
*VaultApi.ConnectionsApi* | [**connectionsAdd**](docs/ConnectionsApi.md#connectionsAdd) | **POST** /vault/connections/{unified_api}/{service_id} | Create connection
*VaultApi.ConnectionsApi* | [**connectionsAll**](docs/ConnectionsApi.md#connectionsAll) | **GET** /vault/connections | Get all connections
*VaultApi.ConnectionsApi* | [**connectionsAuthorize**](docs/ConnectionsApi.md#connectionsAuthorize) | **GET** /vault/authorize/{service_id}/{application_id} | Authorize
*VaultApi.ConnectionsApi* | [**connectionsCallback**](docs/ConnectionsApi.md#connectionsCallback) | **GET** /vault/callback | Callback
*VaultApi.ConnectionsApi* | [**connectionsDelete**](docs/ConnectionsApi.md#connectionsDelete) | **DELETE** /vault/connections/{unified_api}/{service_id} | Deletes a connection
*VaultApi.ConnectionsApi* | [**connectionsImport**](docs/ConnectionsApi.md#connectionsImport) | **POST** /vault/connections/{unified_api}/{service_id}/import | Import connection
*VaultApi.ConnectionsApi* | [**connectionsOne**](docs/ConnectionsApi.md#connectionsOne) | **GET** /vault/connections/{unified_api}/{service_id} | Get connection
*VaultApi.ConnectionsApi* | [**connectionsRevoke**](docs/ConnectionsApi.md#connectionsRevoke) | **GET** /vault/revoke/{service_id}/{application_id} | Revoke connection
*VaultApi.ConnectionsApi* | [**connectionsToken**](docs/ConnectionsApi.md#connectionsToken) | **POST** /vault/connections/{unified_api}/{service_id}/token | Get Access Token
*VaultApi.ConnectionsApi* | [**connectionsUpdate**](docs/ConnectionsApi.md#connectionsUpdate) | **PATCH** /vault/connections/{unified_api}/{service_id} | Update connection
*VaultApi.ConnectionsApi* | [**customFieldsAll**](docs/ConnectionsApi.md#customFieldsAll) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/custom-fields | Get resource custom fields
*VaultApi.ConsumersApi* | [**consumerRequestCountsAll**](docs/ConsumersApi.md#consumerRequestCountsAll) | **GET** /vault/consumers/{consumer_id}/stats | Consumer request counts
*VaultApi.ConsumersApi* | [**consumersAdd**](docs/ConsumersApi.md#consumersAdd) | **POST** /vault/consumers | Create consumer
*VaultApi.ConsumersApi* | [**consumersAll**](docs/ConsumersApi.md#consumersAll) | **GET** /vault/consumers | Get all consumers
*VaultApi.ConsumersApi* | [**consumersDelete**](docs/ConsumersApi.md#consumersDelete) | **DELETE** /vault/consumers/{consumer_id} | Delete consumer
*VaultApi.ConsumersApi* | [**consumersOne**](docs/ConsumersApi.md#consumersOne) | **GET** /vault/consumers/{consumer_id} | Get consumer
*VaultApi.ConsumersApi* | [**consumersUpdate**](docs/ConsumersApi.md#consumersUpdate) | **PATCH** /vault/consumers/{consumer_id} | Update consumer
*VaultApi.LogsApi* | [**logsAll**](docs/LogsApi.md#logsAll) | **GET** /vault/logs | Get all consumer request logs
*VaultApi.SessionsApi* | [**sessionsCreate**](docs/SessionsApi.md#sessionsCreate) | **POST** /vault/sessions | Create Session


## Documentation for Models

 - [VaultApi.AuthType](docs/AuthType.md)
 - [VaultApi.BadRequestResponse](docs/BadRequestResponse.md)
 - [VaultApi.BadRequestResponseDetail](docs/BadRequestResponseDetail.md)
 - [VaultApi.Connection](docs/Connection.md)
 - [VaultApi.ConnectionConfigurationInner](docs/ConnectionConfigurationInner.md)
 - [VaultApi.ConnectionConfigurationInnerDefaultsInner](docs/ConnectionConfigurationInnerDefaultsInner.md)
 - [VaultApi.ConnectionConfigurationInnerDefaultsInnerValue](docs/ConnectionConfigurationInnerDefaultsInnerValue.md)
 - [VaultApi.ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner](docs/ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner.md)
 - [VaultApi.ConnectionEvent](docs/ConnectionEvent.md)
 - [VaultApi.ConnectionImportData](docs/ConnectionImportData.md)
 - [VaultApi.ConnectionImportDataCredentials](docs/ConnectionImportDataCredentials.md)
 - [VaultApi.ConnectionMetadata](docs/ConnectionMetadata.md)
 - [VaultApi.ConnectionState](docs/ConnectionState.md)
 - [VaultApi.ConnectionWebhook](docs/ConnectionWebhook.md)
 - [VaultApi.Consumer](docs/Consumer.md)
 - [VaultApi.ConsumerConnection](docs/ConsumerConnection.md)
 - [VaultApi.ConsumerMetadata](docs/ConsumerMetadata.md)
 - [VaultApi.ConsumerRequestCountsInDateRangeResponse](docs/ConsumerRequestCountsInDateRangeResponse.md)
 - [VaultApi.ConsumerRequestCountsInDateRangeResponseData](docs/ConsumerRequestCountsInDateRangeResponseData.md)
 - [VaultApi.CreateConnectionResponse](docs/CreateConnectionResponse.md)
 - [VaultApi.CreateConsumerResponse](docs/CreateConsumerResponse.md)
 - [VaultApi.CreateCustomMappingRequest](docs/CreateCustomMappingRequest.md)
 - [VaultApi.CreateCustomMappingResponse](docs/CreateCustomMappingResponse.md)
 - [VaultApi.CreateSessionResponse](docs/CreateSessionResponse.md)
 - [VaultApi.CreateSessionResponseData](docs/CreateSessionResponseData.md)
 - [VaultApi.CustomFieldFinder](docs/CustomFieldFinder.md)
 - [VaultApi.CustomMapping](docs/CustomMapping.md)
 - [VaultApi.DeleteConsumerResponse](docs/DeleteConsumerResponse.md)
 - [VaultApi.DeleteConsumerResponseData](docs/DeleteConsumerResponseData.md)
 - [VaultApi.FormField](docs/FormField.md)
 - [VaultApi.FormFieldOption](docs/FormFieldOption.md)
 - [VaultApi.FormFieldOptionGroup](docs/FormFieldOptionGroup.md)
 - [VaultApi.GetConnectionResponse](docs/GetConnectionResponse.md)
 - [VaultApi.GetConnectionsResponse](docs/GetConnectionsResponse.md)
 - [VaultApi.GetConsumerResponse](docs/GetConsumerResponse.md)
 - [VaultApi.GetConsumersResponse](docs/GetConsumersResponse.md)
 - [VaultApi.GetConsumersResponseDataInner](docs/GetConsumersResponseDataInner.md)
 - [VaultApi.GetCustomFieldsResponse](docs/GetCustomFieldsResponse.md)
 - [VaultApi.GetCustomMappingResponse](docs/GetCustomMappingResponse.md)
 - [VaultApi.GetLogsResponse](docs/GetLogsResponse.md)
 - [VaultApi.GetResourceExampleResponse](docs/GetResourceExampleResponse.md)
 - [VaultApi.GetResourceSchemaResponse](docs/GetResourceSchemaResponse.md)
 - [VaultApi.IntegrationState](docs/IntegrationState.md)
 - [VaultApi.LinkedConnectorResource](docs/LinkedConnectorResource.md)
 - [VaultApi.Links](docs/Links.md)
 - [VaultApi.Log](docs/Log.md)
 - [VaultApi.LogOperation](docs/LogOperation.md)
 - [VaultApi.LogService](docs/LogService.md)
 - [VaultApi.LogsFilter](docs/LogsFilter.md)
 - [VaultApi.Meta](docs/Meta.md)
 - [VaultApi.MetaCursors](docs/MetaCursors.md)
 - [VaultApi.NotFoundResponse](docs/NotFoundResponse.md)
 - [VaultApi.NotFoundResponseDetail](docs/NotFoundResponseDetail.md)
 - [VaultApi.NotImplementedResponse](docs/NotImplementedResponse.md)
 - [VaultApi.NotImplementedResponseDetail](docs/NotImplementedResponseDetail.md)
 - [VaultApi.OAuthGrantType](docs/OAuthGrantType.md)
 - [VaultApi.PaymentRequiredResponse](docs/PaymentRequiredResponse.md)
 - [VaultApi.RequestCountAllocation](docs/RequestCountAllocation.md)
 - [VaultApi.ResourceExample](docs/ResourceExample.md)
 - [VaultApi.ResourceStatus](docs/ResourceStatus.md)
 - [VaultApi.Session](docs/Session.md)
 - [VaultApi.SessionSettings](docs/SessionSettings.md)
 - [VaultApi.SessionTheme](docs/SessionTheme.md)
 - [VaultApi.SimpleFormFieldOption](docs/SimpleFormFieldOption.md)
 - [VaultApi.SimpleFormFieldOptionValue](docs/SimpleFormFieldOptionValue.md)
 - [VaultApi.SimpleFormFieldOptionValueAnyOfInner](docs/SimpleFormFieldOptionValueAnyOfInner.md)
 - [VaultApi.UnauthorizedResponse](docs/UnauthorizedResponse.md)
 - [VaultApi.UnexpectedErrorResponse](docs/UnexpectedErrorResponse.md)
 - [VaultApi.UnexpectedErrorResponseDetail](docs/UnexpectedErrorResponseDetail.md)
 - [VaultApi.UnifiedApiId](docs/UnifiedApiId.md)
 - [VaultApi.UnprocessableResponse](docs/UnprocessableResponse.md)
 - [VaultApi.UpdateConnectionResponse](docs/UpdateConnectionResponse.md)
 - [VaultApi.UpdateConsumerRequest](docs/UpdateConsumerRequest.md)
 - [VaultApi.UpdateConsumerResponse](docs/UpdateConsumerResponse.md)
 - [VaultApi.UpdateCustomMappingRequest](docs/UpdateCustomMappingRequest.md)
 - [VaultApi.UpdateCustomMappingResponse](docs/UpdateCustomMappingResponse.md)
 - [VaultApi.VaultEventType](docs/VaultEventType.md)
 - [VaultApi.WebhookSubscription](docs/WebhookSubscription.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### apiKey


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

### applicationId


- **Type**: API key
- **API key parameter name**: x-apideck-app-id
- **Location**: HTTP header

