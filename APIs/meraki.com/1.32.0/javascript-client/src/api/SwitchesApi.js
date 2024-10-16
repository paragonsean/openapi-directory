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
import GetOrganizationSummaryTopSwitchesByEnergyUsage200ResponseInner from '../model/GetOrganizationSummaryTopSwitchesByEnergyUsage200ResponseInner';

/**
* Switches service.
* @module api/SwitchesApi
* @version 1.32.0
*/
export default class SwitchesApi {

    /**
    * Constructs a new SwitchesApi. 
    * @alias module:api/SwitchesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getOrganizationSummaryTopSwitchesByEnergyUsage_3 operation.
     * @callback module:api/SwitchesApi~getOrganizationSummaryTopSwitchesByEnergyUsage_3Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationSummaryTopSwitchesByEnergyUsage200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return metrics for organization's top 10 switches by energy usage over given time range
     * Return metrics for organization's top 10 switches by energy usage over given time range. Default unit is joules.
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {String} [t0] The beginning of the timespan for the data.
     * @param {String} [t1] The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
     * @param {Number} [timespan] The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
     * @param {module:api/SwitchesApi~getOrganizationSummaryTopSwitchesByEnergyUsage_3Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationSummaryTopSwitchesByEnergyUsage200ResponseInner>}
     */
    getOrganizationSummaryTopSwitchesByEnergyUsage_3(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationSummaryTopSwitchesByEnergyUsage_3");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        't0': opts['t0'],
        't1': opts['t1'],
        'timespan': opts['timespan']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationSummaryTopSwitchesByEnergyUsage200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/summary/top/switches/byEnergyUsage', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
