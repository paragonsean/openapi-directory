/**
 * Betriebsstellen
 * This REST-API enables you to query station and stop infos
 *
 * The version of the OpenAPI document: v1
 * Contact: Joachim.Schirrmacher@deutschebahn.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Error from '../model/Error';
import Station from '../model/Station';

/**
* Default service.
* @module api/DefaultApi
* @version v1
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the betriebsstellenAbbrevGet operation.
     * @callback module:api/DefaultApi~betriebsstellenAbbrevGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Station} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get information about a specific station or stop by abbrevation
     * Get information about a specific station or stop by abbrevation
     * @param {String} abbrev Station or stop abbrevation
     * @param {module:api/DefaultApi~betriebsstellenAbbrevGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Station}
     */
    betriebsstellenAbbrevGet(abbrev, callback) {
      let postBody = null;
      // verify the required parameter 'abbrev' is set
      if (abbrev === undefined || abbrev === null) {
        throw new Error("Missing the required parameter 'abbrev' when calling betriebsstellenAbbrevGet");
      }

      let pathParams = {
        'abbrev': abbrev
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = Station;
      return this.apiClient.callApi(
        '/betriebsstellen/{abbrev}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the betriebsstellenGet operation.
     * @callback module:api/DefaultApi~betriebsstellenGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Station>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get information of stations matching a given text
     * Get all station and stop infos
     * @param {Object} opts Optional parameters
     * @param {String} [name] A station name or part of it
     * @param {module:api/DefaultApi~betriebsstellenGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Station>}
     */
    betriebsstellenGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'name': opts['name']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Station];
      return this.apiClient.callApi(
        '/betriebsstellen', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
