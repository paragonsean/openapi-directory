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
* Packets service.
* @module api/PacketsApi
* @version 1.32.0
*/
export default class PacketsApi {

    /**
    * Constructs a new PacketsApi. 
    * @alias module:api/PacketsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getDeviceSwitchPortsStatusesPackets_3 operation.
     * @callback module:api/PacketsApi~getDeviceSwitchPortsStatusesPackets_3Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the packet counters for all the ports of a switch
     * Return the packet counters for all the ports of a switch
     * @param {String} serial 
     * @param {Object} opts Optional parameters
     * @param {String} [t0] The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
     * @param {Number} [timespan] The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
     * @param {module:api/PacketsApi~getDeviceSwitchPortsStatusesPackets_3Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getDeviceSwitchPortsStatusesPackets_3(serial, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceSwitchPortsStatusesPackets_3");
      }

      let pathParams = {
        'serial': serial
      };
      let queryParams = {
        't0': opts['t0'],
        'timespan': opts['timespan']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/devices/{serial}/switch/ports/statuses/packets', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
