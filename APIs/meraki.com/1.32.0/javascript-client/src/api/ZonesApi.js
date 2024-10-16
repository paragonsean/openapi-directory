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
* Zones service.
* @module api/ZonesApi
* @version 1.32.0
*/
export default class ZonesApi {

    /**
    * Constructs a new ZonesApi. 
    * @alias module:api/ZonesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getDeviceCameraAnalyticsZoneHistory_2 operation.
     * @callback module:api/ZonesApi~getDeviceCameraAnalyticsZoneHistory_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return historical records for analytic zones
     * Return historical records for analytic zones
     * @param {String} serial 
     * @param {String} zoneId 
     * @param {Object} opts Optional parameters
     * @param {String} [t0] The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
     * @param {String} [t1] The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
     * @param {Number} [timespan] The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
     * @param {Number} [resolution] The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
     * @param {module:model/String} [objectType] [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
     * @param {module:api/ZonesApi~getDeviceCameraAnalyticsZoneHistory_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getDeviceCameraAnalyticsZoneHistory_2(serial, zoneId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceCameraAnalyticsZoneHistory_2");
      }
      // verify the required parameter 'zoneId' is set
      if (zoneId === undefined || zoneId === null) {
        throw new Error("Missing the required parameter 'zoneId' when calling getDeviceCameraAnalyticsZoneHistory_2");
      }

      let pathParams = {
        'serial': serial,
        'zoneId': zoneId
      };
      let queryParams = {
        't0': opts['t0'],
        't1': opts['t1'],
        'timespan': opts['timespan'],
        'resolution': opts['resolution'],
        'objectType': opts['objectType']
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
        '/devices/{serial}/camera/analytics/zones/{zoneId}/history', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDeviceCameraAnalyticsZones_2 operation.
     * @callback module:api/ZonesApi~getDeviceCameraAnalyticsZones_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns all configured analytic zones for this camera
     * Returns all configured analytic zones for this camera
     * @param {String} serial 
     * @param {module:api/ZonesApi~getDeviceCameraAnalyticsZones_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getDeviceCameraAnalyticsZones_2(serial, callback) {
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceCameraAnalyticsZones_2");
      }

      let pathParams = {
        'serial': serial
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
      let returnType = [Object];
      return this.apiClient.callApi(
        '/devices/{serial}/camera/analytics/zones', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
