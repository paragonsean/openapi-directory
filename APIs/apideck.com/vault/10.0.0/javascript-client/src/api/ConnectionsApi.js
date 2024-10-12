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


import ApiClient from "../ApiClient";
import BadRequestResponse from '../model/BadRequestResponse';
import Connection from '../model/Connection';
import ConnectionImportData from '../model/ConnectionImportData';
import CreateConnectionResponse from '../model/CreateConnectionResponse';
import GetConnectionResponse from '../model/GetConnectionResponse';
import GetConnectionsResponse from '../model/GetConnectionsResponse';
import GetCustomFieldsResponse from '../model/GetCustomFieldsResponse';
import NotFoundResponse from '../model/NotFoundResponse';
import PaymentRequiredResponse from '../model/PaymentRequiredResponse';
import UnauthorizedResponse from '../model/UnauthorizedResponse';
import UnexpectedErrorResponse from '../model/UnexpectedErrorResponse';
import UnprocessableResponse from '../model/UnprocessableResponse';
import UpdateConnectionResponse from '../model/UpdateConnectionResponse';

/**
* Connections service.
* @module api/ConnectionsApi
* @version 10.0.0
*/
export default class ConnectionsApi {

    /**
    * Constructs a new ConnectionsApi. 
    * @alias module:api/ConnectionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the connectionSettingsAll operation.
     * @callback module:api/ConnectionsApi~connectionSettingsAllCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetConnectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get resource settings
     * This endpoint returns custom settings and their defaults required by connection for a given resource. 
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} unifiedApi Unified API
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} resource Name of the resource (plural)
     * @param {module:api/ConnectionsApi~connectionSettingsAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetConnectionResponse}
     */
    connectionSettingsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, callback) {
      let postBody = null;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionSettingsAll");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionSettingsAll");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionSettingsAll");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionSettingsAll");
      }
      // verify the required parameter 'resource' is set
      if (resource === undefined || resource === null) {
        throw new Error("Missing the required parameter 'resource' when calling connectionSettingsAll");
      }

      let pathParams = {
        'unified_api': unifiedApi,
        'service_id': serviceId,
        'resource': resource
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetConnectionResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}/{resource}/config', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionSettingsUpdate operation.
     * @callback module:api/ConnectionsApi~connectionSettingsUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateConnectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update settings
     * Update default values for a connection's resource settings
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} unifiedApi Unified API
     * @param {String} resource Name of the resource (plural)
     * @param {module:model/Connection} connection Fields that need to be updated on the resource
     * @param {module:api/ConnectionsApi~connectionSettingsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateConnectionResponse}
     */
    connectionSettingsUpdate(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, resource, connection, callback) {
      let postBody = connection;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionSettingsUpdate");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionSettingsUpdate");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionSettingsUpdate");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionSettingsUpdate");
      }
      // verify the required parameter 'resource' is set
      if (resource === undefined || resource === null) {
        throw new Error("Missing the required parameter 'resource' when calling connectionSettingsUpdate");
      }
      // verify the required parameter 'connection' is set
      if (connection === undefined || connection === null) {
        throw new Error("Missing the required parameter 'connection' when calling connectionSettingsUpdate");
      }

      let pathParams = {
        'service_id': serviceId,
        'unified_api': unifiedApi,
        'resource': resource
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateConnectionResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}/{resource}/config', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsAdd operation.
     * @callback module:api/ConnectionsApi~connectionsAddCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateConnectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create connection
     * Create an authorized connection 
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} unifiedApi Unified API
     * @param {module:model/Connection} connection Fields that need to be persisted on the resource
     * @param {module:api/ConnectionsApi~connectionsAddCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateConnectionResponse}
     */
    connectionsAdd(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, callback) {
      let postBody = connection;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionsAdd");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionsAdd");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsAdd");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionsAdd");
      }
      // verify the required parameter 'connection' is set
      if (connection === undefined || connection === null) {
        throw new Error("Missing the required parameter 'connection' when calling connectionsAdd");
      }

      let pathParams = {
        'service_id': serviceId,
        'unified_api': unifiedApi
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateConnectionResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsAll operation.
     * @callback module:api/ConnectionsApi~connectionsAllCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetConnectionsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all connections
     * This endpoint includes all the configured integrations and contains the required assets to build an integrations page where your users can install integrations. OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows. 
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {Object} opts Optional parameters
     * @param {String} [api] Scope results to Unified API
     * @param {Boolean} [configured] Scopes results to connections that have been configured or not
     * @param {module:api/ConnectionsApi~connectionsAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetConnectionsResponse}
     */
    connectionsAll(xApideckConsumerId, xApideckAppId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionsAll");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionsAll");
      }

      let pathParams = {
      };
      let queryParams = {
        'api': opts['api'],
        'configured': opts['configured']
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetConnectionsResponse;
      return this.apiClient.callApi(
        '/vault/connections', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsAuthorize operation.
     * @callback module:api/ConnectionsApi~connectionsAuthorizeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UnexpectedErrorResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Authorize
     * __In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__  Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} applicationId Application ID of the resource to return
     * @param {String} state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
     * @param {String} redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [scope] One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector's documentation for the available scopes.
     * @param {module:api/ConnectionsApi~connectionsAuthorizeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UnexpectedErrorResponse}
     */
    connectionsAuthorize(serviceId, applicationId, state, redirectUri, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsAuthorize");
      }
      // verify the required parameter 'applicationId' is set
      if (applicationId === undefined || applicationId === null) {
        throw new Error("Missing the required parameter 'applicationId' when calling connectionsAuthorize");
      }
      // verify the required parameter 'state' is set
      if (state === undefined || state === null) {
        throw new Error("Missing the required parameter 'state' when calling connectionsAuthorize");
      }
      // verify the required parameter 'redirectUri' is set
      if (redirectUri === undefined || redirectUri === null) {
        throw new Error("Missing the required parameter 'redirectUri' when calling connectionsAuthorize");
      }

      let pathParams = {
        'service_id': serviceId,
        'application_id': applicationId
      };
      let queryParams = {
        'state': state,
        'redirect_uri': redirectUri,
        'scope': this.apiClient.buildCollectionParam(opts['scope'], 'ssv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UnexpectedErrorResponse;
      return this.apiClient.callApi(
        '/vault/authorize/{service_id}/{application_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsCallback operation.
     * @callback module:api/ConnectionsApi~connectionsCallbackCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UnexpectedErrorResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Callback
     * This endpoint gets called after the triggering the authorize flow.  Callback links need a state and code parameter to verify the validity of the request. 
     * @param {String} state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
     * @param {String} code An authorization code from the connector which Apideck Vault will later exchange for an access token.
     * @param {module:api/ConnectionsApi~connectionsCallbackCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UnexpectedErrorResponse}
     */
    connectionsCallback(state, code, callback) {
      let postBody = null;
      // verify the required parameter 'state' is set
      if (state === undefined || state === null) {
        throw new Error("Missing the required parameter 'state' when calling connectionsCallback");
      }
      // verify the required parameter 'code' is set
      if (code === undefined || code === null) {
        throw new Error("Missing the required parameter 'code' when calling connectionsCallback");
      }

      let pathParams = {
      };
      let queryParams = {
        'state': state,
        'code': code
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UnexpectedErrorResponse;
      return this.apiClient.callApi(
        '/vault/callback', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsDelete operation.
     * @callback module:api/ConnectionsApi~connectionsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a connection
     * Deletes a connection
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} unifiedApi Unified API
     * @param {module:api/ConnectionsApi~connectionsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    connectionsDelete(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, callback) {
      let postBody = null;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionsDelete");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionsDelete");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsDelete");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionsDelete");
      }

      let pathParams = {
        'service_id': serviceId,
        'unified_api': unifiedApi
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsImport operation.
     * @callback module:api/ConnectionsApi~connectionsImportCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateConnectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Import connection
     * Import an authorized connection. 
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} unifiedApi Unified API
     * @param {module:model/ConnectionImportData} connectionImportData Fields that need to be persisted on the resource
     * @param {module:api/ConnectionsApi~connectionsImportCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateConnectionResponse}
     */
    connectionsImport(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connectionImportData, callback) {
      let postBody = connectionImportData;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionsImport");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionsImport");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsImport");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionsImport");
      }
      // verify the required parameter 'connectionImportData' is set
      if (connectionImportData === undefined || connectionImportData === null) {
        throw new Error("Missing the required parameter 'connectionImportData' when calling connectionsImport");
      }

      let pathParams = {
        'service_id': serviceId,
        'unified_api': unifiedApi
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateConnectionResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}/import', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsOne operation.
     * @callback module:api/ConnectionsApi~connectionsOneCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetConnectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get connection
     * Get a connection
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} unifiedApi Unified API
     * @param {module:api/ConnectionsApi~connectionsOneCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetConnectionResponse}
     */
    connectionsOne(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, callback) {
      let postBody = null;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionsOne");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionsOne");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsOne");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionsOne");
      }

      let pathParams = {
        'service_id': serviceId,
        'unified_api': unifiedApi
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetConnectionResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsRevoke operation.
     * @callback module:api/ConnectionsApi~connectionsRevokeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UnexpectedErrorResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Revoke connection
     * __In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__  Use this endpoint to revoke an existing OAuth connector.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} applicationId Application ID of the resource to return
     * @param {String} state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
     * @param {String} redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
     * @param {module:api/ConnectionsApi~connectionsRevokeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UnexpectedErrorResponse}
     */
    connectionsRevoke(serviceId, applicationId, state, redirectUri, callback) {
      let postBody = null;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsRevoke");
      }
      // verify the required parameter 'applicationId' is set
      if (applicationId === undefined || applicationId === null) {
        throw new Error("Missing the required parameter 'applicationId' when calling connectionsRevoke");
      }
      // verify the required parameter 'state' is set
      if (state === undefined || state === null) {
        throw new Error("Missing the required parameter 'state' when calling connectionsRevoke");
      }
      // verify the required parameter 'redirectUri' is set
      if (redirectUri === undefined || redirectUri === null) {
        throw new Error("Missing the required parameter 'redirectUri' when calling connectionsRevoke");
      }

      let pathParams = {
        'service_id': serviceId,
        'application_id': applicationId
      };
      let queryParams = {
        'state': state,
        'redirect_uri': redirectUri
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UnexpectedErrorResponse;
      return this.apiClient.callApi(
        '/vault/revoke/{service_id}/{application_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsToken operation.
     * @callback module:api/ConnectionsApi~connectionsTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetConnectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Access Token
     * Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.  Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection. 
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} unifiedApi Unified API
     * @param {Object} opts Optional parameters
     * @param {Object.<String, Object>} [body] 
     * @param {module:api/ConnectionsApi~connectionsTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetConnectionResponse}
     */
    connectionsToken(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, opts, callback) {
      opts = opts || {};
      let postBody = opts['body'];
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionsToken");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionsToken");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsToken");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionsToken");
      }

      let pathParams = {
        'service_id': serviceId,
        'unified_api': unifiedApi
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetConnectionResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}/token', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the connectionsUpdate operation.
     * @callback module:api/ConnectionsApi~connectionsUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateConnectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update connection
     * Update a connection
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} unifiedApi Unified API
     * @param {module:model/Connection} connection Fields that need to be updated on the resource
     * @param {module:api/ConnectionsApi~connectionsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateConnectionResponse}
     */
    connectionsUpdate(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, callback) {
      let postBody = connection;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling connectionsUpdate");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling connectionsUpdate");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling connectionsUpdate");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling connectionsUpdate");
      }
      // verify the required parameter 'connection' is set
      if (connection === undefined || connection === null) {
        throw new Error("Missing the required parameter 'connection' when calling connectionsUpdate");
      }

      let pathParams = {
        'service_id': serviceId,
        'unified_api': unifiedApi
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateConnectionResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customFieldsAll operation.
     * @callback module:api/ConnectionsApi~customFieldsAllCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCustomFieldsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get resource custom fields
     * This endpoint returns an custom fields on a connection resource. 
     * @param {String} xApideckConsumerId ID of the consumer which you want to get or push data from
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} unifiedApi Unified API
     * @param {String} serviceId Service ID of the resource to return
     * @param {String} resource Name of the resource (plural)
     * @param {module:api/ConnectionsApi~customFieldsAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCustomFieldsResponse}
     */
    customFieldsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, callback) {
      let postBody = null;
      // verify the required parameter 'xApideckConsumerId' is set
      if (xApideckConsumerId === undefined || xApideckConsumerId === null) {
        throw new Error("Missing the required parameter 'xApideckConsumerId' when calling customFieldsAll");
      }
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling customFieldsAll");
      }
      // verify the required parameter 'unifiedApi' is set
      if (unifiedApi === undefined || unifiedApi === null) {
        throw new Error("Missing the required parameter 'unifiedApi' when calling customFieldsAll");
      }
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling customFieldsAll");
      }
      // verify the required parameter 'resource' is set
      if (resource === undefined || resource === null) {
        throw new Error("Missing the required parameter 'resource' when calling customFieldsAll");
      }

      let pathParams = {
        'unified_api': unifiedApi,
        'service_id': serviceId,
        'resource': resource
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-consumer-id': xApideckConsumerId,
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetCustomFieldsResponse;
      return this.apiClient.callApi(
        '/vault/connections/{unified_api}/{service_id}/{resource}/custom-fields', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
