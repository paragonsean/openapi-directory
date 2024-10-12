/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Stats from '../model/Stats';

/**
* Stats service.
* @module api/StatsApi
* @version 1.5.0-dev
*/
export default class StatsApi {

    /**
    * Constructs a new StatsApi. 
    * @alias module:api/StatsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the globalLiveStats operation.
     * @callback module:api/StatsApi~globalLiveStatsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Stats} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get global otoroshi stats
     * Get global otoroshi stats
     * @param {module:api/StatsApi~globalLiveStatsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Stats}
     */
    globalLiveStats(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['otoroshi_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Stats;
      return this.apiClient.callApi(
        '/api/live', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serviceLiveStats operation.
     * @callback module:api/StatsApi~serviceLiveStatsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Stats} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get live feed of otoroshi stats
     * Get live feed of global otoroshi stats (global) or for a service {id}
     * @param {String} id The service id or global for otoroshi stats
     * @param {module:api/StatsApi~serviceLiveStatsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Stats}
     */
    serviceLiveStats(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serviceLiveStats");
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

      let authNames = ['otoroshi_auth'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/event-stream'];
      let returnType = Stats;
      return this.apiClient.callApi(
        '/api/live/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
