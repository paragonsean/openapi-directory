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

/**
* SmDevicesForKey service.
* @module api/SmDevicesForKeyApi
* @version 1.32.0
*/
export default class SmDevicesForKeyApi {

    /**
    * Constructs a new SmDevicesForKeyApi. 
    * @alias module:api/SmDevicesForKeyApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getNetworkPiiSmDevicesForKey_2 operation.
     * @callback module:api/SmDevicesForKeyApi~getNetworkPiiSmDevicesForKey_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier
     * Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/smDevicesForKey ```
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {String} [username] The username of a Systems Manager user
     * @param {String} [email] The email of a network user account or a Systems Manager device
     * @param {String} [mac] The MAC of a network client device or a Systems Manager device
     * @param {String} [serial] The serial of a Systems Manager device
     * @param {String} [imei] The IMEI of a Systems Manager device
     * @param {String} [bluetoothMac] The MAC of a Bluetooth client
     * @param {module:api/SmDevicesForKeyApi~getNetworkPiiSmDevicesForKey_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkPiiSmDevicesForKey_2(networkId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkPiiSmDevicesForKey_2");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
        'username': opts['username'],
        'email': opts['email'],
        'mac': opts['mac'],
        'serial': opts['serial'],
        'imei': opts['imei'],
        'bluetoothMac': opts['bluetoothMac']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/pii/smDevicesForKey', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
