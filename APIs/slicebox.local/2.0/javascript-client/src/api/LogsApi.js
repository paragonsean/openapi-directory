/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import LogEntry from '../model/LogEntry';

/**
* Logs service.
* @module api/LogsApi
* @version 2.0
*/
export default class LogsApi {

    /**
    * Constructs a new LogsApi. 
    * @alias module:api/LogsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the logDelete operation.
     * @callback module:api/LogsApi~logDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * delete all log messages
     * @param {module:api/LogsApi~logDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    logDelete(callback) {
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
        '/log', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the logGet operation.
     * @callback module:api/LogsApi~logGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/LogEntry>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get a list of slicebox log messages
     * @param {Object} opts Optional parameters
     * @param {Number} [startindex = 0)] start index of returned slice of log messages
     * @param {Number} [count = 20)] size of returned slice of log messages
     * @param {String} [subject] log subject to filter results by
     * @param {String} [type] log type (DEFAULT, INFO, WARN, ERROR) to filter results by
     * @param {module:api/LogsApi~logGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/LogEntry>}
     */
    logGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'startindex': opts['startindex'],
        'count': opts['count'],
        'subject': opts['subject'],
        'type': opts['type']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/octet-stream'];
      let returnType = [LogEntry];
      return this.apiClient.callApi(
        '/log', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the logIdDelete operation.
     * @callback module:api/LogsApi~logIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete the log entry with the supplied ID
     * @param {Number} id ID of log entry
     * @param {module:api/LogsApi~logIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    logIdDelete(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling logIdDelete");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/log/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
