/**
 * Vault API
 * Welcome to the Vault API 👋  When you're looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  ``` curl -X POST https://unify.apideck.com/vault/sessions     -H \"Content-Type: application/json\"     -H \"Authorization: Bearer <your-api-key>\"     -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"     -H \"X-APIDECK-APP-ID: <application-id>\"     -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}' ```  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.  This is being handled by the `/authorize` endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AuthType from './model/AuthType';
import BadRequestResponse from './model/BadRequestResponse';
import BadRequestResponseDetail from './model/BadRequestResponseDetail';
import Connection from './model/Connection';
import ConnectionConfigurationInner from './model/ConnectionConfigurationInner';
import ConnectionConfigurationInnerDefaultsInner from './model/ConnectionConfigurationInnerDefaultsInner';
import ConnectionConfigurationInnerDefaultsInnerValue from './model/ConnectionConfigurationInnerDefaultsInnerValue';
import ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner from './model/ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner';
import ConnectionEvent from './model/ConnectionEvent';
import ConnectionImportData from './model/ConnectionImportData';
import ConnectionImportDataCredentials from './model/ConnectionImportDataCredentials';
import ConnectionMetadata from './model/ConnectionMetadata';
import ConnectionState from './model/ConnectionState';
import ConnectionWebhook from './model/ConnectionWebhook';
import Consumer from './model/Consumer';
import ConsumerConnection from './model/ConsumerConnection';
import ConsumerMetadata from './model/ConsumerMetadata';
import ConsumerRequestCountsInDateRangeResponse from './model/ConsumerRequestCountsInDateRangeResponse';
import ConsumerRequestCountsInDateRangeResponseData from './model/ConsumerRequestCountsInDateRangeResponseData';
import CreateConnectionResponse from './model/CreateConnectionResponse';
import CreateConsumerResponse from './model/CreateConsumerResponse';
import CreateCustomMappingRequest from './model/CreateCustomMappingRequest';
import CreateCustomMappingResponse from './model/CreateCustomMappingResponse';
import CreateSessionResponse from './model/CreateSessionResponse';
import CreateSessionResponseData from './model/CreateSessionResponseData';
import CustomFieldFinder from './model/CustomFieldFinder';
import CustomMapping from './model/CustomMapping';
import DeleteConsumerResponse from './model/DeleteConsumerResponse';
import DeleteConsumerResponseData from './model/DeleteConsumerResponseData';
import FormField from './model/FormField';
import FormFieldOption from './model/FormFieldOption';
import FormFieldOptionGroup from './model/FormFieldOptionGroup';
import GetConnectionResponse from './model/GetConnectionResponse';
import GetConnectionsResponse from './model/GetConnectionsResponse';
import GetConsumerResponse from './model/GetConsumerResponse';
import GetConsumersResponse from './model/GetConsumersResponse';
import GetConsumersResponseDataInner from './model/GetConsumersResponseDataInner';
import GetCustomFieldsResponse from './model/GetCustomFieldsResponse';
import GetCustomMappingResponse from './model/GetCustomMappingResponse';
import GetLogsResponse from './model/GetLogsResponse';
import GetResourceExampleResponse from './model/GetResourceExampleResponse';
import GetResourceSchemaResponse from './model/GetResourceSchemaResponse';
import IntegrationState from './model/IntegrationState';
import LinkedConnectorResource from './model/LinkedConnectorResource';
import Links from './model/Links';
import Log from './model/Log';
import LogOperation from './model/LogOperation';
import LogService from './model/LogService';
import LogsFilter from './model/LogsFilter';
import Meta from './model/Meta';
import MetaCursors from './model/MetaCursors';
import NotFoundResponse from './model/NotFoundResponse';
import NotFoundResponseDetail from './model/NotFoundResponseDetail';
import NotImplementedResponse from './model/NotImplementedResponse';
import NotImplementedResponseDetail from './model/NotImplementedResponseDetail';
import OAuthGrantType from './model/OAuthGrantType';
import PaymentRequiredResponse from './model/PaymentRequiredResponse';
import RequestCountAllocation from './model/RequestCountAllocation';
import ResourceExample from './model/ResourceExample';
import ResourceStatus from './model/ResourceStatus';
import Session from './model/Session';
import SessionSettings from './model/SessionSettings';
import SessionTheme from './model/SessionTheme';
import SimpleFormFieldOption from './model/SimpleFormFieldOption';
import SimpleFormFieldOptionValue from './model/SimpleFormFieldOptionValue';
import SimpleFormFieldOptionValueAnyOfInner from './model/SimpleFormFieldOptionValueAnyOfInner';
import UnauthorizedResponse from './model/UnauthorizedResponse';
import UnexpectedErrorResponse from './model/UnexpectedErrorResponse';
import UnexpectedErrorResponseDetail from './model/UnexpectedErrorResponseDetail';
import UnifiedApiId from './model/UnifiedApiId';
import UnprocessableResponse from './model/UnprocessableResponse';
import UpdateConnectionResponse from './model/UpdateConnectionResponse';
import UpdateConsumerRequest from './model/UpdateConsumerRequest';
import UpdateConsumerResponse from './model/UpdateConsumerResponse';
import UpdateCustomMappingRequest from './model/UpdateCustomMappingRequest';
import UpdateCustomMappingResponse from './model/UpdateCustomMappingResponse';
import VaultEventType from './model/VaultEventType';
import WebhookSubscription from './model/WebhookSubscription';
import ConnectionsApi from './api/ConnectionsApi';
import ConsumersApi from './api/ConsumersApi';
import LogsApi from './api/LogsApi';
import SessionsApi from './api/SessionsApi';


/**
* Welcome to the Vault API 👋  When you&#39;re looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is &#x60;https://unify.apideck.com&#x60;  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app&#39;s settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don&#39;t need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  &#x60;&#x60;&#x60; curl -X POST https://unify.apideck.com/vault/sessions     -H \&quot;Content-Type: application/json\&quot;     -H \&quot;Authorization: Bearer &lt;your-api-key&gt;\&quot;     -H \&quot;X-APIDECK-CONSUMER-ID: &lt;consumer-id&gt;\&quot;     -H \&quot;X-APIDECK-APP-ID: &lt;application-id&gt;\&quot;     -d &#39;{\&quot;consumer_metadata\&quot;: { \&quot;account_name\&quot; : \&quot;Sample\&quot;, \&quot;user_name\&quot;: \&quot;Sand Box\&quot;, \&quot;email\&quot;: \&quot;sand@box.com\&quot;, \&quot;image\&quot;: \&quot;https://unavatar.now.sh/jake\&quot; }, \&quot;theme\&quot;: { \&quot;vault_name\&quot;: \&quot;Intercom\&quot;, \&quot;primary_color\&quot;: \&quot;#286efa\&quot;, \&quot;sidepanel_background_color\&quot;: \&quot;#286efa\&quot;,\&quot;sidepanel_text_color\&quot;: \&quot;#FFFFFF\&quot;, \&quot;favicon\&quot;: \&quot;https://res.cloudinary.com/apideck/icons/intercom\&quot; }}&#39; &#x60;&#x60;&#x60;  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you&#39;re already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you&#39;ll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers&#39; tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don&#39;t allow entering a username and password to be entered into applications that they don&#39;t own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider&#39;s website or mobile app to authenticate.  This is being handled by the &#x60;/authorize&#x60; endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var VaultApi = require('index'); // See note below*.
* var xxxSvc = new VaultApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new VaultApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new VaultApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new VaultApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 10.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AuthType model constructor.
     * @property {module:model/AuthType}
     */
    AuthType,

    /**
     * The BadRequestResponse model constructor.
     * @property {module:model/BadRequestResponse}
     */
    BadRequestResponse,

    /**
     * The BadRequestResponseDetail model constructor.
     * @property {module:model/BadRequestResponseDetail}
     */
    BadRequestResponseDetail,

    /**
     * The Connection model constructor.
     * @property {module:model/Connection}
     */
    Connection,

    /**
     * The ConnectionConfigurationInner model constructor.
     * @property {module:model/ConnectionConfigurationInner}
     */
    ConnectionConfigurationInner,

    /**
     * The ConnectionConfigurationInnerDefaultsInner model constructor.
     * @property {module:model/ConnectionConfigurationInnerDefaultsInner}
     */
    ConnectionConfigurationInnerDefaultsInner,

    /**
     * The ConnectionConfigurationInnerDefaultsInnerValue model constructor.
     * @property {module:model/ConnectionConfigurationInnerDefaultsInnerValue}
     */
    ConnectionConfigurationInnerDefaultsInnerValue,

    /**
     * The ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner model constructor.
     * @property {module:model/ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner}
     */
    ConnectionConfigurationInnerDefaultsInnerValueAnyOfInner,

    /**
     * The ConnectionEvent model constructor.
     * @property {module:model/ConnectionEvent}
     */
    ConnectionEvent,

    /**
     * The ConnectionImportData model constructor.
     * @property {module:model/ConnectionImportData}
     */
    ConnectionImportData,

    /**
     * The ConnectionImportDataCredentials model constructor.
     * @property {module:model/ConnectionImportDataCredentials}
     */
    ConnectionImportDataCredentials,

    /**
     * The ConnectionMetadata model constructor.
     * @property {module:model/ConnectionMetadata}
     */
    ConnectionMetadata,

    /**
     * The ConnectionState model constructor.
     * @property {module:model/ConnectionState}
     */
    ConnectionState,

    /**
     * The ConnectionWebhook model constructor.
     * @property {module:model/ConnectionWebhook}
     */
    ConnectionWebhook,

    /**
     * The Consumer model constructor.
     * @property {module:model/Consumer}
     */
    Consumer,

    /**
     * The ConsumerConnection model constructor.
     * @property {module:model/ConsumerConnection}
     */
    ConsumerConnection,

    /**
     * The ConsumerMetadata model constructor.
     * @property {module:model/ConsumerMetadata}
     */
    ConsumerMetadata,

    /**
     * The ConsumerRequestCountsInDateRangeResponse model constructor.
     * @property {module:model/ConsumerRequestCountsInDateRangeResponse}
     */
    ConsumerRequestCountsInDateRangeResponse,

    /**
     * The ConsumerRequestCountsInDateRangeResponseData model constructor.
     * @property {module:model/ConsumerRequestCountsInDateRangeResponseData}
     */
    ConsumerRequestCountsInDateRangeResponseData,

    /**
     * The CreateConnectionResponse model constructor.
     * @property {module:model/CreateConnectionResponse}
     */
    CreateConnectionResponse,

    /**
     * The CreateConsumerResponse model constructor.
     * @property {module:model/CreateConsumerResponse}
     */
    CreateConsumerResponse,

    /**
     * The CreateCustomMappingRequest model constructor.
     * @property {module:model/CreateCustomMappingRequest}
     */
    CreateCustomMappingRequest,

    /**
     * The CreateCustomMappingResponse model constructor.
     * @property {module:model/CreateCustomMappingResponse}
     */
    CreateCustomMappingResponse,

    /**
     * The CreateSessionResponse model constructor.
     * @property {module:model/CreateSessionResponse}
     */
    CreateSessionResponse,

    /**
     * The CreateSessionResponseData model constructor.
     * @property {module:model/CreateSessionResponseData}
     */
    CreateSessionResponseData,

    /**
     * The CustomFieldFinder model constructor.
     * @property {module:model/CustomFieldFinder}
     */
    CustomFieldFinder,

    /**
     * The CustomMapping model constructor.
     * @property {module:model/CustomMapping}
     */
    CustomMapping,

    /**
     * The DeleteConsumerResponse model constructor.
     * @property {module:model/DeleteConsumerResponse}
     */
    DeleteConsumerResponse,

    /**
     * The DeleteConsumerResponseData model constructor.
     * @property {module:model/DeleteConsumerResponseData}
     */
    DeleteConsumerResponseData,

    /**
     * The FormField model constructor.
     * @property {module:model/FormField}
     */
    FormField,

    /**
     * The FormFieldOption model constructor.
     * @property {module:model/FormFieldOption}
     */
    FormFieldOption,

    /**
     * The FormFieldOptionGroup model constructor.
     * @property {module:model/FormFieldOptionGroup}
     */
    FormFieldOptionGroup,

    /**
     * The GetConnectionResponse model constructor.
     * @property {module:model/GetConnectionResponse}
     */
    GetConnectionResponse,

    /**
     * The GetConnectionsResponse model constructor.
     * @property {module:model/GetConnectionsResponse}
     */
    GetConnectionsResponse,

    /**
     * The GetConsumerResponse model constructor.
     * @property {module:model/GetConsumerResponse}
     */
    GetConsumerResponse,

    /**
     * The GetConsumersResponse model constructor.
     * @property {module:model/GetConsumersResponse}
     */
    GetConsumersResponse,

    /**
     * The GetConsumersResponseDataInner model constructor.
     * @property {module:model/GetConsumersResponseDataInner}
     */
    GetConsumersResponseDataInner,

    /**
     * The GetCustomFieldsResponse model constructor.
     * @property {module:model/GetCustomFieldsResponse}
     */
    GetCustomFieldsResponse,

    /**
     * The GetCustomMappingResponse model constructor.
     * @property {module:model/GetCustomMappingResponse}
     */
    GetCustomMappingResponse,

    /**
     * The GetLogsResponse model constructor.
     * @property {module:model/GetLogsResponse}
     */
    GetLogsResponse,

    /**
     * The GetResourceExampleResponse model constructor.
     * @property {module:model/GetResourceExampleResponse}
     */
    GetResourceExampleResponse,

    /**
     * The GetResourceSchemaResponse model constructor.
     * @property {module:model/GetResourceSchemaResponse}
     */
    GetResourceSchemaResponse,

    /**
     * The IntegrationState model constructor.
     * @property {module:model/IntegrationState}
     */
    IntegrationState,

    /**
     * The LinkedConnectorResource model constructor.
     * @property {module:model/LinkedConnectorResource}
     */
    LinkedConnectorResource,

    /**
     * The Links model constructor.
     * @property {module:model/Links}
     */
    Links,

    /**
     * The Log model constructor.
     * @property {module:model/Log}
     */
    Log,

    /**
     * The LogOperation model constructor.
     * @property {module:model/LogOperation}
     */
    LogOperation,

    /**
     * The LogService model constructor.
     * @property {module:model/LogService}
     */
    LogService,

    /**
     * The LogsFilter model constructor.
     * @property {module:model/LogsFilter}
     */
    LogsFilter,

    /**
     * The Meta model constructor.
     * @property {module:model/Meta}
     */
    Meta,

    /**
     * The MetaCursors model constructor.
     * @property {module:model/MetaCursors}
     */
    MetaCursors,

    /**
     * The NotFoundResponse model constructor.
     * @property {module:model/NotFoundResponse}
     */
    NotFoundResponse,

    /**
     * The NotFoundResponseDetail model constructor.
     * @property {module:model/NotFoundResponseDetail}
     */
    NotFoundResponseDetail,

    /**
     * The NotImplementedResponse model constructor.
     * @property {module:model/NotImplementedResponse}
     */
    NotImplementedResponse,

    /**
     * The NotImplementedResponseDetail model constructor.
     * @property {module:model/NotImplementedResponseDetail}
     */
    NotImplementedResponseDetail,

    /**
     * The OAuthGrantType model constructor.
     * @property {module:model/OAuthGrantType}
     */
    OAuthGrantType,

    /**
     * The PaymentRequiredResponse model constructor.
     * @property {module:model/PaymentRequiredResponse}
     */
    PaymentRequiredResponse,

    /**
     * The RequestCountAllocation model constructor.
     * @property {module:model/RequestCountAllocation}
     */
    RequestCountAllocation,

    /**
     * The ResourceExample model constructor.
     * @property {module:model/ResourceExample}
     */
    ResourceExample,

    /**
     * The ResourceStatus model constructor.
     * @property {module:model/ResourceStatus}
     */
    ResourceStatus,

    /**
     * The Session model constructor.
     * @property {module:model/Session}
     */
    Session,

    /**
     * The SessionSettings model constructor.
     * @property {module:model/SessionSettings}
     */
    SessionSettings,

    /**
     * The SessionTheme model constructor.
     * @property {module:model/SessionTheme}
     */
    SessionTheme,

    /**
     * The SimpleFormFieldOption model constructor.
     * @property {module:model/SimpleFormFieldOption}
     */
    SimpleFormFieldOption,

    /**
     * The SimpleFormFieldOptionValue model constructor.
     * @property {module:model/SimpleFormFieldOptionValue}
     */
    SimpleFormFieldOptionValue,

    /**
     * The SimpleFormFieldOptionValueAnyOfInner model constructor.
     * @property {module:model/SimpleFormFieldOptionValueAnyOfInner}
     */
    SimpleFormFieldOptionValueAnyOfInner,

    /**
     * The UnauthorizedResponse model constructor.
     * @property {module:model/UnauthorizedResponse}
     */
    UnauthorizedResponse,

    /**
     * The UnexpectedErrorResponse model constructor.
     * @property {module:model/UnexpectedErrorResponse}
     */
    UnexpectedErrorResponse,

    /**
     * The UnexpectedErrorResponseDetail model constructor.
     * @property {module:model/UnexpectedErrorResponseDetail}
     */
    UnexpectedErrorResponseDetail,

    /**
     * The UnifiedApiId model constructor.
     * @property {module:model/UnifiedApiId}
     */
    UnifiedApiId,

    /**
     * The UnprocessableResponse model constructor.
     * @property {module:model/UnprocessableResponse}
     */
    UnprocessableResponse,

    /**
     * The UpdateConnectionResponse model constructor.
     * @property {module:model/UpdateConnectionResponse}
     */
    UpdateConnectionResponse,

    /**
     * The UpdateConsumerRequest model constructor.
     * @property {module:model/UpdateConsumerRequest}
     */
    UpdateConsumerRequest,

    /**
     * The UpdateConsumerResponse model constructor.
     * @property {module:model/UpdateConsumerResponse}
     */
    UpdateConsumerResponse,

    /**
     * The UpdateCustomMappingRequest model constructor.
     * @property {module:model/UpdateCustomMappingRequest}
     */
    UpdateCustomMappingRequest,

    /**
     * The UpdateCustomMappingResponse model constructor.
     * @property {module:model/UpdateCustomMappingResponse}
     */
    UpdateCustomMappingResponse,

    /**
     * The VaultEventType model constructor.
     * @property {module:model/VaultEventType}
     */
    VaultEventType,

    /**
     * The WebhookSubscription model constructor.
     * @property {module:model/WebhookSubscription}
     */
    WebhookSubscription,

    /**
    * The ConnectionsApi service constructor.
    * @property {module:api/ConnectionsApi}
    */
    ConnectionsApi,

    /**
    * The ConsumersApi service constructor.
    * @property {module:api/ConsumersApi}
    */
    ConsumersApi,

    /**
    * The LogsApi service constructor.
    * @property {module:api/LogsApi}
    */
    LogsApi,

    /**
    * The SessionsApi service constructor.
    * @property {module:api/SessionsApi}
    */
    SessionsApi
};
