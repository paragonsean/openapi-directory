/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
import NetworksResponse from '../model/NetworksResponse';
import RadioErrorResponse from '../model/RadioErrorResponse';

/**
* Networks service.
* @module api/NetworksApi
* @version 1.0.0
*/
export default class NetworksApi {

    /**
    * Constructs a new NetworksApi. 
    * @alias module:api/NetworksApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getRadioNetworks operation.
     * @callback module:api/NetworksApi~getRadioNetworksCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NetworksResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Networks
     * All iPlayer Radio networks - contains business logic for masterbrand and service relationships 
     * @param {String} xAPIKey API_KEY
     * @param {Object} opts Optional parameters
     * @param {Boolean} [preset] Returns all networks needed for iPlayer Radio responsive web navigation
     * @param {Boolean} [international] Returns all networks available internationally
     * @param {module:api/NetworksApi~getRadioNetworksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NetworksResponse}
     */
    getRadioNetworks(xAPIKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'xAPIKey' is set
      if (xAPIKey === undefined || xAPIKey === null) {
        throw new Error("Missing the required parameter 'xAPIKey' when calling getRadioNetworks");
      }

      let pathParams = {
      };
      let queryParams = {
        'preset': opts['preset'],
        'international': opts['international']
      };
      let headerParams = {
        'X-API-Key': xAPIKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = NetworksResponse;
      return this.apiClient.callApi(
        '/radio/networks.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
