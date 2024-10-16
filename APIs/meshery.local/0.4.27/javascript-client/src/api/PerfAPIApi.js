/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import PerformanceResultsAPIResponse from '../model/PerformanceResultsAPIResponse';
import PerformanceSpec from '../model/PerformanceSpec';
import PerformanceTestConfig from '../model/PerformanceTestConfig';

/**
* PerfAPI service.
* @module api/PerfAPIApi
* @version 0.4.27
*/
export default class PerfAPIApi {

    /**
    * Constructs a new PerfAPIApi. 
    * @alias module:api/PerfAPIApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the idGetAllPerfResults operation.
     * @callback module:api/PerfAPIApi~idGetAllPerfResultsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PerformanceResultsAPIResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Handles GET requests for perf results
     * Returns pages of all the perf results from Remote Provider
     * @param {module:api/PerfAPIApi~idGetAllPerfResultsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PerformanceResultsAPIResponse}
     */
    idGetAllPerfResults(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PerformanceResultsAPIResponse;
      return this.apiClient.callApi(
        '/api/perf/profile/result', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the idGetSinglePerfResult operation.
     * @callback module:api/PerfAPIApi~idGetSinglePerfResultCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PerformanceSpec} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Handles GET requests for perf result
     * Returns an individual result from provider
     * @param {String} id Automatically added
     * @param {module:api/PerfAPIApi~idGetSinglePerfResultCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PerformanceSpec}
     */
    idGetSinglePerfResult(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling idGetSinglePerfResult");
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

      let authNames = ['token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PerformanceSpec;
      return this.apiClient.callApi(
        '/api/perf/profile/result/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the idRunPerfTest operation.
     * @callback module:api/PerfAPIApi~idRunPerfTestCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Handle GET request to run a test
     * Runs the load test with the given parameters
     * @param {Object} opts Optional parameters
     * @param {module:model/PerformanceTestConfig} [performanceTestConfig] 
     * @param {module:api/PerfAPIApi~idRunPerfTestCallback} callback The callback function, accepting three arguments: error, data, response
     */
    idRunPerfTest(opts, callback) {
      opts = opts || {};
      let postBody = opts['performanceTestConfig'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['token'];
      let contentTypes = ['application/json', 'multipart/form-data'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/perf/profile', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
