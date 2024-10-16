/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* PasswordForgotten service.
* @module api/PasswordForgottenApi
* @version 1.0.0
*/
export default class PasswordForgottenApi {

    /**
    * Constructs a new PasswordForgottenApi. 
    * @alias module:api/PasswordForgottenApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getPasswordForgottenKey_0 operation.
     * @callback module:api/PasswordForgottenApi~getPasswordForgottenKey_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} key 
     * @param {module:api/PasswordForgottenApi~getPasswordForgottenKey_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    getPasswordForgottenKey_0(key, callback) {
      let postBody = null;
      // verify the required parameter 'key' is set
      if (key === undefined || key === null) {
        throw new Error("Missing the required parameter 'key' when calling getPasswordForgottenKey_0");
      }

      let pathParams = {
        'key': key
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/password_forgotten/{key}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPasswordForgotten_0 operation.
     * @callback module:api/PasswordForgottenApi~getPasswordForgotten_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/PasswordForgottenApi~getPasswordForgotten_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    getPasswordForgotten_0(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/password_forgotten', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postPasswordForgottenKey_0 operation.
     * @callback module:api/PasswordForgottenApi~postPasswordForgottenKey_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} key 
     * @param {Object} opts Optional parameters
     * @param {String} [pass] 
     * @param {String} [pass2] 
     * @param {module:api/PasswordForgottenApi~postPasswordForgottenKey_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    postPasswordForgottenKey_0(key, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'key' is set
      if (key === undefined || key === null) {
        throw new Error("Missing the required parameter 'key' when calling postPasswordForgottenKey_0");
      }

      let pathParams = {
        'key': key
      };
      let queryParams = {
        'pass': opts['pass'],
        'pass2': opts['pass2']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/password_forgotten/{key}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postPasswordForgotten_0 operation.
     * @callback module:api/PasswordForgottenApi~postPasswordForgotten_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [login] 
     * @param {String} [dropTokens] 
     * @param {String} [testerPass] 
     * @param {module:api/PasswordForgottenApi~postPasswordForgotten_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    postPasswordForgotten_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'login': opts['login'],
        'drop_tokens': opts['dropTokens']
      };
      let headerParams = {
        'TesterPass': opts['testerPass']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/password_forgotten', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
