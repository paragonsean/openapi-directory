/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Statistic from '../model/Statistic';

/**
* Statistics service.
* @module api/StatisticsApi
* @version 4.0
*/
export default class StatisticsApi {

    /**
    * Constructs a new StatisticsApi. 
    * @alias module:api/StatisticsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getStatistic operation.
     * @callback module:api/StatisticsApi~getStatisticCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Statistic} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve usage statistics
     * This method retrieves overall and per configuration usage statistics for specific timeframe. Statistics ordered per available configurations. Available interval values are current <b>hour</b>, <b>day</b>, <b>week</b>, <b>month</b> and <b>year</b>.
     * @param {String} contentType 
     * @param {Object} opts Optional parameters
     * @param {String} [configId] Configuration identifier for usage statistics retrieving.
     * @param {String} [interval] Hour, Day, Week, Month, Year values are supported.
     * @param {module:api/StatisticsApi~getStatisticCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Statistic}
     */
    getStatistic(contentType, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getStatistic");
      }

      let pathParams = {
        'content_type': contentType
      };
      let queryParams = {
        'config_id': opts['configId'],
        'interval': opts['interval']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = Statistic;
      return this.apiClient.callApi(
        '/statistics.{content_type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
