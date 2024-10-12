/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AuthenticationOptions from '../model/AuthenticationOptions';
import AuthenticationToken from '../model/AuthenticationToken';
import Credential from '../model/Credential';
import CustomerJWT from '../model/CustomerJWT';
import Error from '../model/Error';
import InvalidError from '../model/InvalidError';
import ResetPasswordToken from '../model/ResetPasswordToken';

/**
* CustomerAuthentication service.
* @module api/CustomerAuthenticationApi
* @version 2.1
*/
export default class CustomerAuthenticationApi {

    /**
    * Constructs a new CustomerAuthenticationApi. 
    * @alias module:api/CustomerAuthenticationApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteAuthenticationToken operation.
     * @callback module:api/CustomerAuthenticationApi~deleteAuthenticationTokenCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Logout a customer
     * Logout a customer. 
     * @param {String} token The token identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~deleteAuthenticationTokenCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteAuthenticationToken(token, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling deleteAuthenticationToken");
      }

      let pathParams = {
        'token': token
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT', 'PublishableApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/authentication-tokens/{token}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteCredential operation.
     * @callback module:api/CustomerAuthenticationApi~deleteCredentialCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a credential
     * Delete a credential with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~deleteCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteCredential(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteCredential");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/credentials/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePasswordToken operation.
     * @callback module:api/CustomerAuthenticationApi~deletePasswordTokenCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Reset Password Token
     * Delete a Reset Password Token with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~deletePasswordTokenCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deletePasswordToken(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deletePasswordToken");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/password-tokens/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAuthenticationOption operation.
     * @callback module:api/CustomerAuthenticationApi~getAuthenticationOptionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/AuthenticationOptions>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Read current authentication options
     * Read current authentication options. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~getAuthenticationOptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/AuthenticationOptions>}
     */
    getAuthenticationOption(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [AuthenticationOptions];
      return this.apiClient.callApi(
        '/authentication-options', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAuthenticationTokenCollection operation.
     * @callback module:api/CustomerAuthenticationApi~getAuthenticationTokenCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/AuthenticationToken>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of auth tokens
     * Retrieve a list of auth tokens. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {module:api/CustomerAuthenticationApi~getAuthenticationTokenCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/AuthenticationToken>}
     */
    getAuthenticationTokenCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [AuthenticationToken];
      return this.apiClient.callApi(
        '/authentication-tokens', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAuthenticationTokenVerification operation.
     * @callback module:api/CustomerAuthenticationApi~getAuthenticationTokenVerificationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthenticationToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Verify
     * Verify an authentication token. 
     * @param {String} token The token identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~getAuthenticationTokenVerificationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthenticationToken}
     */
    getAuthenticationTokenVerification(token, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling getAuthenticationTokenVerification");
      }

      let pathParams = {
        'token': token
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT', 'PublishableApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AuthenticationToken;
      return this.apiClient.callApi(
        '/authentication-tokens/{token}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCredential operation.
     * @callback module:api/CustomerAuthenticationApi~getCredentialCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Credential} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a credential
     * Retrieve a credential with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~getCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Credential}
     */
    getCredential(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getCredential");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Credential;
      return this.apiClient.callApi(
        '/credentials/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCredentialCollection operation.
     * @callback module:api/CustomerAuthenticationApi~getCredentialCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Credential>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of credentials
     * Retrieve a list of credentials. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {module:api/CustomerAuthenticationApi~getCredentialCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Credential>}
     */
    getCredentialCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Credential];
      return this.apiClient.callApi(
        '/credentials', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPasswordToken operation.
     * @callback module:api/CustomerAuthenticationApi~getPasswordTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ResetPasswordToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a Reset Password Token
     * Retrieve a Reset Password Token with specified identifier string. 
     * @param {String} id The resource identifier string.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~getPasswordTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ResetPasswordToken}
     */
    getPasswordToken(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getPasswordToken");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ResetPasswordToken;
      return this.apiClient.callApi(
        '/password-tokens/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPasswordTokenCollection operation.
     * @callback module:api/CustomerAuthenticationApi~getPasswordTokenCollectionCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ResetPasswordToken>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of tokens
     * Retrieve a list of tokens. 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {Number} [limit] The collection items limit.
     * @param {Number} [offset] The collection items offset.
     * @param {module:api/CustomerAuthenticationApi~getPasswordTokenCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ResetPasswordToken>}
     */
    getPasswordTokenCollection(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [ResetPasswordToken];
      return this.apiClient.callApi(
        '/password-tokens', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postAuthenticationToken operation.
     * @callback module:api/CustomerAuthenticationApi~postAuthenticationTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthenticationToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Login
     * Login a customer. 
     * @param {module:model/AuthenticationToken} authenticationToken AuthenticationToken resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~postAuthenticationTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthenticationToken}
     */
    postAuthenticationToken(authenticationToken, opts, callback) {
      opts = opts || {};
      let postBody = authenticationToken;
      // verify the required parameter 'authenticationToken' is set
      if (authenticationToken === undefined || authenticationToken === null) {
        throw new Error("Missing the required parameter 'authenticationToken' when calling postAuthenticationToken");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT', 'PublishableApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AuthenticationToken;
      return this.apiClient.callApi(
        '/authentication-tokens', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postAuthenticationTokenExchange operation.
     * @callback module:api/CustomerAuthenticationApi~postAuthenticationTokenExchangeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomerJWT} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Exchange
     * Exchange Authentication Token for JWT.  It will also invalidate an Authentication Token by default (so it can only be exchanged once). 
     * @param {String} token The token identifier string.
     * @param {module:model/CustomerJWT} customerJWT 
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~postAuthenticationTokenExchangeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomerJWT}
     */
    postAuthenticationTokenExchange(token, customerJWT, opts, callback) {
      opts = opts || {};
      let postBody = customerJWT;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling postAuthenticationTokenExchange");
      }
      // verify the required parameter 'customerJWT' is set
      if (customerJWT === undefined || customerJWT === null) {
        throw new Error("Missing the required parameter 'customerJWT' when calling postAuthenticationTokenExchange");
      }

      let pathParams = {
        'token': token
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT', 'PublishableApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CustomerJWT;
      return this.apiClient.callApi(
        '/authentication-tokens/{token}/exchange', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postCredential operation.
     * @callback module:api/CustomerAuthenticationApi~postCredentialCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Credential} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a credential
     * Create a credential. 
     * @param {module:model/Credential} credential Credential resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~postCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Credential}
     */
    postCredential(credential, opts, callback) {
      opts = opts || {};
      let postBody = credential;
      // verify the required parameter 'credential' is set
      if (credential === undefined || credential === null) {
        throw new Error("Missing the required parameter 'credential' when calling postCredential");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Credential;
      return this.apiClient.callApi(
        '/credentials', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postPasswordToken operation.
     * @callback module:api/CustomerAuthenticationApi~postPasswordTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ResetPasswordToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a Reset Password Token
     * Create a Reset Password Token. 
     * @param {module:model/ResetPasswordToken} resetPasswordToken ResetPasswordToken resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~postPasswordTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ResetPasswordToken}
     */
    postPasswordToken(resetPasswordToken, opts, callback) {
      opts = opts || {};
      let postBody = resetPasswordToken;
      // verify the required parameter 'resetPasswordToken' is set
      if (resetPasswordToken === undefined || resetPasswordToken === null) {
        throw new Error("Missing the required parameter 'resetPasswordToken' when calling postPasswordToken");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ResetPasswordToken;
      return this.apiClient.callApi(
        '/password-tokens', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putAuthenticationOption operation.
     * @callback module:api/CustomerAuthenticationApi~putAuthenticationOptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthenticationOptions} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change authentication options
     * Change options. 
     * @param {module:model/AuthenticationOptions} authenticationOptions Authentication Options resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~putAuthenticationOptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthenticationOptions}
     */
    putAuthenticationOption(authenticationOptions, opts, callback) {
      opts = opts || {};
      let postBody = authenticationOptions;
      // verify the required parameter 'authenticationOptions' is set
      if (authenticationOptions === undefined || authenticationOptions === null) {
        throw new Error("Missing the required parameter 'authenticationOptions' when calling putAuthenticationOption");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AuthenticationOptions;
      return this.apiClient.callApi(
        '/authentication-options', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putCredential operation.
     * @callback module:api/CustomerAuthenticationApi~putCredentialCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Credential} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create or update a credential with predefined ID
     * Create or update a credential with predefined identifier string. 
     * @param {String} id The resource identifier string.
     * @param {module:model/Credential} credential Credential resource.
     * @param {Object} opts Optional parameters
     * @param {String} [organizationId] Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
     * @param {module:api/CustomerAuthenticationApi~putCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Credential}
     */
    putCredential(id, credential, opts, callback) {
      opts = opts || {};
      let postBody = credential;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putCredential");
      }
      // verify the required parameter 'credential' is set
      if (credential === undefined || credential === null) {
        throw new Error("Missing the required parameter 'credential' when calling putCredential");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'Organization-Id': opts['organizationId']
      };
      let formParams = {
      };

      let authNames = ['SecretApiKey', 'JWT'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Credential;
      return this.apiClient.callApi(
        '/credentials/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
