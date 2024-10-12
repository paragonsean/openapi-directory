/**
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Analytics200Response from '../model/Analytics200Response';

/**
* Analytics service.
* @module api/AnalyticsApi
* @version 1.0.0
*/
export default class AnalyticsApi {

    /**
    * Constructs a new AnalyticsApi. 
    * @alias module:api/AnalyticsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the analytics operation.
     * @callback module:api/AnalyticsApi~analyticsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Analytics200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [start] Start date of the statistics in the format YYYY-MM-DD. By default, the date of 30 days ago is set.
     * @param {String} [end] End date of the statistics in the format YYYY-MM-DD. By default, the current day.
     * @param {String} [label] Shows only data of a specific label.
     * @param {String} [subaccounts] Receive the data only for the main account, all your (sub-)accounts or only for specific subaccounts.
     * @param {module:model/String} [groupBy] Defines the grouping of the data.
     * @param {module:api/AnalyticsApi~analyticsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Analytics200Response}
     */
    analytics(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'start': opts['start'],
        'end': opts['end'],
        'label': opts['label'],
        'subaccounts': opts['subaccounts'],
        'group_by': opts['groupBy']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Analytics200Response;
      return this.apiClient.callApi(
        '/analytics', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
