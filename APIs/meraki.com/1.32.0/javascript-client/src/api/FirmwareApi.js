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
import GetOrganizationFirmwareUpgrades200ResponseInner from '../model/GetOrganizationFirmwareUpgrades200ResponseInner';
import GetOrganizationFirmwareUpgradesByDevice200ResponseInner from '../model/GetOrganizationFirmwareUpgradesByDevice200ResponseInner';

/**
* Firmware service.
* @module api/FirmwareApi
* @version 1.32.0
*/
export default class FirmwareApi {

    /**
    * Constructs a new FirmwareApi. 
    * @alias module:api/FirmwareApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getOrganizationFirmwareUpgradesByDevice_1 operation.
     * @callback module:api/FirmwareApi~getOrganizationFirmwareUpgradesByDevice_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationFirmwareUpgradesByDevice200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get firmware upgrade status for the filtered devices
     * Get firmware upgrade status for the filtered devices
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {Array.<String>} [networkIds] Optional parameter to filter by network
     * @param {Array.<String>} [serials] Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
     * @param {Array.<String>} [macs] Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
     * @param {Array.<String>} [firmwareUpgradeIds] Optional parameter to filter by firmware upgrade ids.
     * @param {Array.<String>} [firmwareUpgradeBatchIds] Optional parameter to filter by firmware upgrade batch ids.
     * @param {module:api/FirmwareApi~getOrganizationFirmwareUpgradesByDevice_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationFirmwareUpgradesByDevice200ResponseInner>}
     */
    getOrganizationFirmwareUpgradesByDevice_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationFirmwareUpgradesByDevice_1");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        'perPage': opts['perPage'],
        'startingAfter': opts['startingAfter'],
        'endingBefore': opts['endingBefore'],
        'networkIds': this.apiClient.buildCollectionParam(opts['networkIds'], 'csv'),
        'serials': this.apiClient.buildCollectionParam(opts['serials'], 'csv'),
        'macs': this.apiClient.buildCollectionParam(opts['macs'], 'csv'),
        'firmwareUpgradeIds': this.apiClient.buildCollectionParam(opts['firmwareUpgradeIds'], 'csv'),
        'firmwareUpgradeBatchIds': this.apiClient.buildCollectionParam(opts['firmwareUpgradeBatchIds'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationFirmwareUpgradesByDevice200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/firmware/upgrades/byDevice', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationFirmwareUpgrades_1 operation.
     * @callback module:api/FirmwareApi~getOrganizationFirmwareUpgrades_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationFirmwareUpgrades200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get firmware upgrade information for an organization
     * Get firmware upgrade information for an organization
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [status] The status of an upgrade 
     * @param {Array.<String>} [productType] The product type in a given upgrade ID
     * @param {module:api/FirmwareApi~getOrganizationFirmwareUpgrades_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationFirmwareUpgrades200ResponseInner>}
     */
    getOrganizationFirmwareUpgrades_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationFirmwareUpgrades_1");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        'status': this.apiClient.buildCollectionParam(opts['status'], 'csv'),
        'productType': this.apiClient.buildCollectionParam(opts['productType'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationFirmwareUpgrades200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/firmware/upgrades', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
