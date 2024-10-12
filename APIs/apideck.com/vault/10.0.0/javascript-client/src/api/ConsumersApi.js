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
import Consumer from '../model/Consumer';
import ConsumerRequestCountsInDateRangeResponse from '../model/ConsumerRequestCountsInDateRangeResponse';
import CreateConsumerResponse from '../model/CreateConsumerResponse';
import DeleteConsumerResponse from '../model/DeleteConsumerResponse';
import GetConsumerResponse from '../model/GetConsumerResponse';
import GetConsumersResponse from '../model/GetConsumersResponse';
import NotFoundResponse from '../model/NotFoundResponse';
import PaymentRequiredResponse from '../model/PaymentRequiredResponse';
import UnauthorizedResponse from '../model/UnauthorizedResponse';
import UnexpectedErrorResponse from '../model/UnexpectedErrorResponse';
import UnprocessableResponse from '../model/UnprocessableResponse';
import UpdateConsumerRequest from '../model/UpdateConsumerRequest';
import UpdateConsumerResponse from '../model/UpdateConsumerResponse';

/**
* Consumers service.
* @module api/ConsumersApi
* @version 10.0.0
*/
export default class ConsumersApi {

    /**
    * Constructs a new ConsumersApi. 
    * @alias module:api/ConsumersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the consumerRequestCountsAll operation.
     * @callback module:api/ConsumersApi~consumerRequestCountsAllCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConsumerRequestCountsInDateRangeResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Consumer request counts
     * Get consumer request counts within a given datetime range. 
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} consumerId ID of the consumer to return
     * @param {String} startDatetime Scopes results to requests that happened after datetime
     * @param {String} endDatetime Scopes results to requests that happened before datetime
     * @param {module:api/ConsumersApi~consumerRequestCountsAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConsumerRequestCountsInDateRangeResponse}
     */
    consumerRequestCountsAll(xApideckAppId, consumerId, startDatetime, endDatetime, callback) {
      let postBody = null;
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling consumerRequestCountsAll");
      }
      // verify the required parameter 'consumerId' is set
      if (consumerId === undefined || consumerId === null) {
        throw new Error("Missing the required parameter 'consumerId' when calling consumerRequestCountsAll");
      }
      // verify the required parameter 'startDatetime' is set
      if (startDatetime === undefined || startDatetime === null) {
        throw new Error("Missing the required parameter 'startDatetime' when calling consumerRequestCountsAll");
      }
      // verify the required parameter 'endDatetime' is set
      if (endDatetime === undefined || endDatetime === null) {
        throw new Error("Missing the required parameter 'endDatetime' when calling consumerRequestCountsAll");
      }

      let pathParams = {
        'consumer_id': consumerId
      };
      let queryParams = {
        'start_datetime': startDatetime,
        'end_datetime': endDatetime
      };
      let headerParams = {
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ConsumerRequestCountsInDateRangeResponse;
      return this.apiClient.callApi(
        '/vault/consumers/{consumer_id}/stats', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumersAdd operation.
     * @callback module:api/ConsumersApi~consumersAddCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateConsumerResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create consumer
     * Create a consumer
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {module:model/Consumer} consumer 
     * @param {module:api/ConsumersApi~consumersAddCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateConsumerResponse}
     */
    consumersAdd(xApideckAppId, consumer, callback) {
      let postBody = consumer;
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling consumersAdd");
      }
      // verify the required parameter 'consumer' is set
      if (consumer === undefined || consumer === null) {
        throw new Error("Missing the required parameter 'consumer' when calling consumersAdd");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateConsumerResponse;
      return this.apiClient.callApi(
        '/vault/consumers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumersAll operation.
     * @callback module:api/ConsumersApi~consumersAllCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetConsumersResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all consumers
     * This endpoint includes all application consumers, along with an aggregated count of requests made. 
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
     * @param {Number} [limit = 20)] Number of results to return. Minimum 1, Maximum 200, Default 20
     * @param {module:api/ConsumersApi~consumersAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetConsumersResponse}
     */
    consumersAll(xApideckAppId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling consumersAll");
      }

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'limit': opts['limit']
      };
      let headerParams = {
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetConsumersResponse;
      return this.apiClient.callApi(
        '/vault/consumers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumersDelete operation.
     * @callback module:api/ConsumersApi~consumersDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteConsumerResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete consumer
     * Delete consumer and all their connections, including credentials.
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} consumerId ID of the consumer to return
     * @param {module:api/ConsumersApi~consumersDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteConsumerResponse}
     */
    consumersDelete(xApideckAppId, consumerId, callback) {
      let postBody = null;
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling consumersDelete");
      }
      // verify the required parameter 'consumerId' is set
      if (consumerId === undefined || consumerId === null) {
        throw new Error("Missing the required parameter 'consumerId' when calling consumersDelete");
      }

      let pathParams = {
        'consumer_id': consumerId
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteConsumerResponse;
      return this.apiClient.callApi(
        '/vault/consumers/{consumer_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumersOne operation.
     * @callback module:api/ConsumersApi~consumersOneCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetConsumerResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get consumer
     * Consumer detail including their aggregated counts with the connections they have authorized. 
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} consumerId ID of the consumer to return
     * @param {module:api/ConsumersApi~consumersOneCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetConsumerResponse}
     */
    consumersOne(xApideckAppId, consumerId, callback) {
      let postBody = null;
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling consumersOne");
      }
      // verify the required parameter 'consumerId' is set
      if (consumerId === undefined || consumerId === null) {
        throw new Error("Missing the required parameter 'consumerId' when calling consumersOne");
      }

      let pathParams = {
        'consumer_id': consumerId
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetConsumerResponse;
      return this.apiClient.callApi(
        '/vault/consumers/{consumer_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumersUpdate operation.
     * @callback module:api/ConsumersApi~consumersUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateConsumerResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update consumer
     * Update consumer metadata such as name and email.
     * @param {String} xApideckAppId The ID of your Unify application
     * @param {String} consumerId ID of the consumer to return
     * @param {module:model/UpdateConsumerRequest} updateConsumerRequest 
     * @param {module:api/ConsumersApi~consumersUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateConsumerResponse}
     */
    consumersUpdate(xApideckAppId, consumerId, updateConsumerRequest, callback) {
      let postBody = updateConsumerRequest;
      // verify the required parameter 'xApideckAppId' is set
      if (xApideckAppId === undefined || xApideckAppId === null) {
        throw new Error("Missing the required parameter 'xApideckAppId' when calling consumersUpdate");
      }
      // verify the required parameter 'consumerId' is set
      if (consumerId === undefined || consumerId === null) {
        throw new Error("Missing the required parameter 'consumerId' when calling consumersUpdate");
      }
      // verify the required parameter 'updateConsumerRequest' is set
      if (updateConsumerRequest === undefined || updateConsumerRequest === null) {
        throw new Error("Missing the required parameter 'updateConsumerRequest' when calling consumersUpdate");
      }

      let pathParams = {
        'consumer_id': consumerId
      };
      let queryParams = {
      };
      let headerParams = {
        'x-apideck-app-id': xApideckAppId
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateConsumerResponse;
      return this.apiClient.callApi(
        '/vault/consumers/{consumer_id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
