/**
 * OnSched API Utility
 * Endpoints for system utilities. e.g.Health
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ThreadPoolInfo from '../model/ThreadPoolInfo';

/**
* Health service.
* @module api/HealthApi
* @version v1
*/
export default class HealthApi {

    /**
    * Constructs a new HealthApi. 
    * @alias module:api/HealthApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the utilityV1HealthHeartbeatGet operation.
     * @callback module:api/HealthApi~utilityV1HealthHeartbeatGetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/HealthApi~utilityV1HealthHeartbeatGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    utilityV1HealthHeartbeatGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/utility/v1/health/heartbeat', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the utilityV1HealthThreadinfoGet operation.
     * @callback module:api/HealthApi~utilityV1HealthThreadinfoGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ThreadPoolInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/HealthApi~utilityV1HealthThreadinfoGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ThreadPoolInfo}
     */
    utilityV1HealthThreadinfoGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ThreadPoolInfo;
      return this.apiClient.callApi(
        '/utility/v1/health/threadinfo', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
