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
import GetNetworkWirelessSsidEapOverride200Response from '../model/GetNetworkWirelessSsidEapOverride200Response';
import UpdateNetworkWirelessSsidEapOverrideRequest from '../model/UpdateNetworkWirelessSsidEapOverrideRequest';

/**
* EapOverride service.
* @module api/EapOverrideApi
* @version 1.32.0
*/
export default class EapOverrideApi {

    /**
    * Constructs a new EapOverrideApi. 
    * @alias module:api/EapOverrideApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getNetworkWirelessSsidEapOverride_2 operation.
     * @callback module:api/EapOverrideApi~getNetworkWirelessSsidEapOverride_2Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWirelessSsidEapOverride200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the EAP overridden parameters for an SSID
     * Return the EAP overridden parameters for an SSID
     * @param {String} networkId 
     * @param {String} number 
     * @param {module:api/EapOverrideApi~getNetworkWirelessSsidEapOverride_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWirelessSsidEapOverride200Response}
     */
    getNetworkWirelessSsidEapOverride_2(networkId, number, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkWirelessSsidEapOverride_2");
      }
      // verify the required parameter 'number' is set
      if (number === undefined || number === null) {
        throw new Error("Missing the required parameter 'number' when calling getNetworkWirelessSsidEapOverride_2");
      }

      let pathParams = {
        'networkId': networkId,
        'number': number
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
      let returnType = GetNetworkWirelessSsidEapOverride200Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/wireless/ssids/{number}/eapOverride', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkWirelessSsidEapOverride_2 operation.
     * @callback module:api/EapOverrideApi~updateNetworkWirelessSsidEapOverride_2Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWirelessSsidEapOverride200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the EAP overridden parameters for an SSID.
     * Update the EAP overridden parameters for an SSID.
     * @param {String} networkId 
     * @param {String} number 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkWirelessSsidEapOverrideRequest} [updateNetworkWirelessSsidEapOverrideRequest] 
     * @param {module:api/EapOverrideApi~updateNetworkWirelessSsidEapOverride_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWirelessSsidEapOverride200Response}
     */
    updateNetworkWirelessSsidEapOverride_2(networkId, number, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkWirelessSsidEapOverrideRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkWirelessSsidEapOverride_2");
      }
      // verify the required parameter 'number' is set
      if (number === undefined || number === null) {
        throw new Error("Missing the required parameter 'number' when calling updateNetworkWirelessSsidEapOverride_2");
      }

      let pathParams = {
        'networkId': networkId,
        'number': number
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
      let returnType = GetNetworkWirelessSsidEapOverride200Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/wireless/ssids/{number}/eapOverride', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
