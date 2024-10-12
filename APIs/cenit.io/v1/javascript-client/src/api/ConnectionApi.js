/**
 * Cenit IO - REST API Specification
 * Cenit IO is an Open Platform for Data and Business Integration (iPaaS) 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@cenit.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Connection from '../model/Connection';

/**
* Connection service.
* @module api/ConnectionApi
* @version v1
*/
export default class ConnectionApi {

    /**
    * Constructs a new ConnectionApi. 
    * @alias module:api/ConnectionApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the setupConnectionGet operation.
     * @callback module:api/ConnectionApi~setupConnectionGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Connection>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a list of connections
     * Returns a list of connections you've previously created. The connections are returned in sorted order, with the most recent connection appearing first.
     * @param {module:api/ConnectionApi~setupConnectionGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Connection>}
     */
    setupConnectionGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['X-User-Access-Key', 'X-User-Access-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Connection];
      return this.apiClient.callApi(
        '/setup/connection', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setupConnectionIdDelete operation.
     * @callback module:api/ConnectionApi~setupConnectionIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a connection
     * Permanently deletes a connection. It cannot be undone.
     * @param {String} id Connection ID
     * @param {module:api/ConnectionApi~setupConnectionIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    setupConnectionIdDelete(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling setupConnectionIdDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['X-User-Access-Key', 'X-User-Access-Token'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/setup/connection/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setupConnectionIdGet operation.
     * @callback module:api/ConnectionApi~setupConnectionIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Connection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing connection
     * Retrieves the details of an existing connection. You need only supply the unique connection identifier that was returned upon connection creation.
     * @param {String} id Connection ID
     * @param {module:api/ConnectionApi~setupConnectionIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Connection}
     */
    setupConnectionIdGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling setupConnectionIdGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['X-User-Access-Key', 'X-User-Access-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Connection;
      return this.apiClient.callApi(
        '/setup/connection/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setupConnectionPost operation.
     * @callback module:api/ConnectionApi~setupConnectionPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Connection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create or update a connection
     * Creates or updates the specified connection by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
     * @param {module:api/ConnectionApi~setupConnectionPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Connection}
     */
    setupConnectionPost(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['X-User-Access-Key', 'X-User-Access-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Connection;
      return this.apiClient.callApi(
        '/setup/connection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
