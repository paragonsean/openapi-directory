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
import GetDeviceApplianceUplinksSettings200Response from '../model/GetDeviceApplianceUplinksSettings200Response';
import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner from '../model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner';
import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner from '../model/GetOrganizationDevicesUplinksLossAndLatency200ResponseInner';
import GetOrganizationUplinksStatuses200ResponseInner from '../model/GetOrganizationUplinksStatuses200ResponseInner';
import UpdateDeviceApplianceUplinksSettingsRequest from '../model/UpdateDeviceApplianceUplinksSettingsRequest';

/**
* Uplinks service.
* @module api/UplinksApi
* @version 1.32.0
*/
export default class UplinksApi {

    /**
    * Constructs a new UplinksApi. 
    * @alias module:api/UplinksApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getDeviceApplianceUplinksSettings_1 operation.
     * @callback module:api/UplinksApi~getDeviceApplianceUplinksSettings_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDeviceApplianceUplinksSettings200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the uplink settings for an MX appliance
     * Return the uplink settings for an MX appliance
     * @param {String} serial 
     * @param {module:api/UplinksApi~getDeviceApplianceUplinksSettings_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDeviceApplianceUplinksSettings200Response}
     */
    getDeviceApplianceUplinksSettings_1(serial, callback) {
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceApplianceUplinksSettings_1");
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
      let returnType = GetDeviceApplianceUplinksSettings200Response;
      return this.apiClient.callApi(
        '/devices/{serial}/appliance/uplinks/settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDeviceLossAndLatencyHistory_1 operation.
     * @callback module:api/UplinksApi~getDeviceLossAndLatencyHistory_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
     * Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
     * @param {String} serial 
     * @param {String} ip The destination IP used to obtain the requested stats. This is required.
     * @param {Object} opts Optional parameters
     * @param {String} [t0] The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
     * @param {String} [t1] The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
     * @param {Number} [timespan] The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
     * @param {Number} [resolution] The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
     * @param {module:model/String} [uplink] The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
     * @param {module:api/UplinksApi~getDeviceLossAndLatencyHistory_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getDeviceLossAndLatencyHistory_1(serial, ip, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceLossAndLatencyHistory_1");
      }
      // verify the required parameter 'ip' is set
      if (ip === undefined || ip === null) {
        throw new Error("Missing the required parameter 'ip' when calling getDeviceLossAndLatencyHistory_1");
      }

      let pathParams = {
        'serial': serial
      };
      let queryParams = {
        't0': opts['t0'],
        't1': opts['t1'],
        'timespan': opts['timespan'],
        'resolution': opts['resolution'],
        'uplink': opts['uplink'],
        'ip': ip
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
        '/devices/{serial}/lossAndLatencyHistory', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkApplianceUplinksUsageHistory_1 operation.
     * @callback module:api/UplinksApi~getNetworkApplianceUplinksUsageHistory_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the sent and received bytes for each uplink of a network.
     * Get the sent and received bytes for each uplink of a network.
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {String} [t0] The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
     * @param {String} [t1] The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
     * @param {Number} [timespan] The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
     * @param {Number} [resolution] The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
     * @param {module:api/UplinksApi~getNetworkApplianceUplinksUsageHistory_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getNetworkApplianceUplinksUsageHistory_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceUplinksUsageHistory_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
        't0': opts['t0'],
        't1': opts['t1'],
        'timespan': opts['timespan'],
        'resolution': opts['resolution']
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
        '/networks/{networkId}/appliance/uplinks/usageHistory', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationApplianceUplinkStatuses_1 operation.
     * @callback module:api/UplinksApi~getOrganizationApplianceUplinkStatuses_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the uplink status of every Meraki MX and Z series appliances in the organization
     * List the uplink status of every Meraki MX and Z series appliances in the organization
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {Array.<String>} [networkIds] A list of network IDs. The returned devices will be filtered to only include these networks.
     * @param {Array.<String>} [serials] A list of serial numbers. The returned devices will be filtered to only include these serials.
     * @param {Array.<String>} [iccids] A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
     * @param {module:api/UplinksApi~getOrganizationApplianceUplinkStatuses_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationApplianceUplinkStatuses_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationApplianceUplinkStatuses_1");
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
        'iccids': this.apiClient.buildCollectionParam(opts['iccids'], 'csv')
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
        '/organizations/{organizationId}/appliance/uplink/statuses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationDevicesUplinksAddressesByDevice_2 operation.
     * @callback module:api/UplinksApi~getOrganizationDevicesUplinksAddressesByDevice_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the current uplink addresses for devices in an organization.
     * List the current uplink addresses for devices in an organization.
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {Array.<String>} [networkIds] Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
     * @param {Array.<String>} [productTypes] Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
     * @param {Array.<String>} [serials] Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
     * @param {Array.<String>} [tags] An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
     * @param {module:model/String} [tagsFilterType] An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
     * @param {module:api/UplinksApi~getOrganizationDevicesUplinksAddressesByDevice_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner>}
     */
    getOrganizationDevicesUplinksAddressesByDevice_2(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationDevicesUplinksAddressesByDevice_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        'perPage': opts['perPage'],
        'startingAfter': opts['startingAfter'],
        'endingBefore': opts['endingBefore'],
        'networkIds': this.apiClient.buildCollectionParam(opts['networkIds'], 'csv'),
        'productTypes': this.apiClient.buildCollectionParam(opts['productTypes'], 'csv'),
        'serials': this.apiClient.buildCollectionParam(opts['serials'], 'csv'),
        'tags': this.apiClient.buildCollectionParam(opts['tags'], 'csv'),
        'tagsFilterType': opts['tagsFilterType']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/devices/uplinks/addresses/byDevice', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationDevicesUplinksLossAndLatency_2 operation.
     * @callback module:api/UplinksApi~getOrganizationDevicesUplinksLossAndLatency_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationDevicesUplinksLossAndLatency200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
     * Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {String} [t0] The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
     * @param {String} [t1] The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
     * @param {Number} [timespan] The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
     * @param {module:model/String} [uplink] Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
     * @param {String} [ip] Optional filter for a specific destination IP. Default will return all destination IPs.
     * @param {module:api/UplinksApi~getOrganizationDevicesUplinksLossAndLatency_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationDevicesUplinksLossAndLatency200ResponseInner>}
     */
    getOrganizationDevicesUplinksLossAndLatency_2(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationDevicesUplinksLossAndLatency_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        't0': opts['t0'],
        't1': opts['t1'],
        'timespan': opts['timespan'],
        'uplink': opts['uplink'],
        'ip': opts['ip']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationDevicesUplinksLossAndLatency200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/devices/uplinksLossAndLatency', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationUplinksStatuses_1 operation.
     * @callback module:api/UplinksApi~getOrganizationUplinksStatuses_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationUplinksStatuses200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the uplink status of every Meraki MX, MG and Z series devices in the organization
     * List the uplink status of every Meraki MX, MG and Z series devices in the organization
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {Array.<String>} [networkIds] A list of network IDs. The returned devices will be filtered to only include these networks.
     * @param {Array.<String>} [serials] A list of serial numbers. The returned devices will be filtered to only include these serials.
     * @param {Array.<String>} [iccids] A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
     * @param {module:api/UplinksApi~getOrganizationUplinksStatuses_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationUplinksStatuses200ResponseInner>}
     */
    getOrganizationUplinksStatuses_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationUplinksStatuses_1");
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
        'iccids': this.apiClient.buildCollectionParam(opts['iccids'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationUplinksStatuses200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/uplinks/statuses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateDeviceApplianceUplinksSettings_1 operation.
     * @callback module:api/UplinksApi~updateDeviceApplianceUplinksSettings_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDeviceApplianceUplinksSettings200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the uplink settings for an MX appliance
     * Update the uplink settings for an MX appliance
     * @param {String} serial 
     * @param {module:model/UpdateDeviceApplianceUplinksSettingsRequest} updateDeviceApplianceUplinksSettingsRequest 
     * @param {module:api/UplinksApi~updateDeviceApplianceUplinksSettings_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDeviceApplianceUplinksSettings200Response}
     */
    updateDeviceApplianceUplinksSettings_1(serial, updateDeviceApplianceUplinksSettingsRequest, callback) {
      let postBody = updateDeviceApplianceUplinksSettingsRequest;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling updateDeviceApplianceUplinksSettings_1");
      }
      // verify the required parameter 'updateDeviceApplianceUplinksSettingsRequest' is set
      if (updateDeviceApplianceUplinksSettingsRequest === undefined || updateDeviceApplianceUplinksSettingsRequest === null) {
        throw new Error("Missing the required parameter 'updateDeviceApplianceUplinksSettingsRequest' when calling updateDeviceApplianceUplinksSettings_1");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetDeviceApplianceUplinksSettings200Response;
      return this.apiClient.callApi(
        '/devices/{serial}/appliance/uplinks/settings', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
