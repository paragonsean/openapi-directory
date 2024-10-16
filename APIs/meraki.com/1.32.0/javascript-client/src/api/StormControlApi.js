/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import GetNetworkSwitchStormControl200Response from '../model/GetNetworkSwitchStormControl200Response';
import UpdateNetworkSwitchStormControlRequest from '../model/UpdateNetworkSwitchStormControlRequest';

/**
* StormControl service.
* @module api/StormControlApi
* @version 1.32.0
*/
export default class StormControlApi {

    /**
    * Constructs a new StormControlApi. 
    * @alias module:api/StormControlApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getNetworkSwitchStormControl_1 operation.
     * @callback module:api/StormControlApi~getNetworkSwitchStormControl_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkSwitchStormControl200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the storm control configuration for a switch network
     * Return the storm control configuration for a switch network
     * @param {String} networkId 
     * @param {module:api/StormControlApi~getNetworkSwitchStormControl_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkSwitchStormControl200Response}
     */
    getNetworkSwitchStormControl_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkSwitchStormControl_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetNetworkSwitchStormControl200Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/switch/stormControl', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkSwitchStormControl_1 operation.
     * @callback module:api/StormControlApi~updateNetworkSwitchStormControl_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the storm control configuration for a switch network
     * Update the storm control configuration for a switch network
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkSwitchStormControlRequest} [updateNetworkSwitchStormControlRequest] 
     * @param {module:api/StormControlApi~updateNetworkSwitchStormControl_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkSwitchStormControl_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkSwitchStormControlRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkSwitchStormControl_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/switch/stormControl', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
