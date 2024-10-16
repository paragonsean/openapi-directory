/**
 * Mon-voyage-pas-cher.com Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import PongResponse from '../model/PongResponse';

/**
* UtilitiesAPIs service.
* @module api/UtilitiesAPIsApi
* @version 0.0.1
*/
export default class UtilitiesAPIsApi {

    /**
    * Constructs a new UtilitiesAPIsApi. 
    * @alias module:api/UtilitiesAPIsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getPing operation.
     * @callback module:api/UtilitiesAPIsApi~getPingCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PongResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a ping. In case you need a health check in your system. Cannot be called /ping as AWS is using this route for their health check. This webservice doesn't have CORS enable, as it's supposed to be call server to server and not from a webpage ( it won't work over the tester)
     * @param {module:api/UtilitiesAPIsApi~getPingCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PongResponse}
     */
    getPing(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['x-api-key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PongResponse;
      return this.apiClient.callApi(
        '/pong', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
