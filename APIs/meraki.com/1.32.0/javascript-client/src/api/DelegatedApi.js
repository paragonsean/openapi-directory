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
import CreateNetworkAppliancePrefixesDelegatedStaticRequest from '../model/CreateNetworkAppliancePrefixesDelegatedStaticRequest';
import GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner from '../model/GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner';
import UpdateNetworkAppliancePrefixesDelegatedStaticRequest from '../model/UpdateNetworkAppliancePrefixesDelegatedStaticRequest';

/**
* Delegated service.
* @module api/DelegatedApi
* @version 1.32.0
*/
export default class DelegatedApi {

    /**
    * Constructs a new DelegatedApi. 
    * @alias module:api/DelegatedApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createNetworkAppliancePrefixesDelegatedStatic_2 operation.
     * @callback module:api/DelegatedApi~createNetworkAppliancePrefixesDelegatedStatic_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a static delegated prefix from a network
     * Add a static delegated prefix from a network
     * @param {String} networkId 
     * @param {module:model/CreateNetworkAppliancePrefixesDelegatedStaticRequest} createNetworkAppliancePrefixesDelegatedStaticRequest 
     * @param {module:api/DelegatedApi~createNetworkAppliancePrefixesDelegatedStatic_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createNetworkAppliancePrefixesDelegatedStatic_2(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest, callback) {
      let postBody = createNetworkAppliancePrefixesDelegatedStaticRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkAppliancePrefixesDelegatedStatic_2");
      }
      // verify the required parameter 'createNetworkAppliancePrefixesDelegatedStaticRequest' is set
      if (createNetworkAppliancePrefixesDelegatedStaticRequest === undefined || createNetworkAppliancePrefixesDelegatedStaticRequest === null) {
        throw new Error("Missing the required parameter 'createNetworkAppliancePrefixesDelegatedStaticRequest' when calling createNetworkAppliancePrefixesDelegatedStatic_2");
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
        '/networks/{networkId}/appliance/prefixes/delegated/statics', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetworkAppliancePrefixesDelegatedStatic_2 operation.
     * @callback module:api/DelegatedApi~deleteNetworkAppliancePrefixesDelegatedStatic_2Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a static delegated prefix from a network
     * Delete a static delegated prefix from a network
     * @param {String} networkId 
     * @param {String} staticDelegatedPrefixId 
     * @param {module:api/DelegatedApi~deleteNetworkAppliancePrefixesDelegatedStatic_2Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling deleteNetworkAppliancePrefixesDelegatedStatic_2");
      }
      // verify the required parameter 'staticDelegatedPrefixId' is set
      if (staticDelegatedPrefixId === undefined || staticDelegatedPrefixId === null) {
        throw new Error("Missing the required parameter 'staticDelegatedPrefixId' when calling deleteNetworkAppliancePrefixesDelegatedStatic_2");
      }

      let pathParams = {
        'networkId': networkId,
        'staticDelegatedPrefixId': staticDelegatedPrefixId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDeviceAppliancePrefixesDelegatedVlanAssignments_2 operation.
     * @callback module:api/DelegatedApi~getDeviceAppliancePrefixesDelegatedVlanAssignments_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
     * Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
     * @param {String} serial 
     * @param {module:api/DelegatedApi~getDeviceAppliancePrefixesDelegatedVlanAssignments_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getDeviceAppliancePrefixesDelegatedVlanAssignments_2(serial, callback) {
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceAppliancePrefixesDelegatedVlanAssignments_2");
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
        '/devices/{serial}/appliance/prefixes/delegated/vlanAssignments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDeviceAppliancePrefixesDelegated_2 operation.
     * @callback module:api/DelegatedApi~getDeviceAppliancePrefixesDelegated_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return current delegated IPv6 prefixes on an appliance.
     * Return current delegated IPv6 prefixes on an appliance.
     * @param {String} serial 
     * @param {module:api/DelegatedApi~getDeviceAppliancePrefixesDelegated_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getDeviceAppliancePrefixesDelegated_2(serial, callback) {
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceAppliancePrefixesDelegated_2");
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
        '/devices/{serial}/appliance/prefixes/delegated', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkAppliancePrefixesDelegatedStatic_2 operation.
     * @callback module:api/DelegatedApi~getNetworkAppliancePrefixesDelegatedStatic_2Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return a static delegated prefix from a network
     * Return a static delegated prefix from a network
     * @param {String} networkId 
     * @param {String} staticDelegatedPrefixId 
     * @param {module:api/DelegatedApi~getNetworkAppliancePrefixesDelegatedStatic_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner}
     */
    getNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkAppliancePrefixesDelegatedStatic_2");
      }
      // verify the required parameter 'staticDelegatedPrefixId' is set
      if (staticDelegatedPrefixId === undefined || staticDelegatedPrefixId === null) {
        throw new Error("Missing the required parameter 'staticDelegatedPrefixId' when calling getNetworkAppliancePrefixesDelegatedStatic_2");
      }

      let pathParams = {
        'networkId': networkId,
        'staticDelegatedPrefixId': staticDelegatedPrefixId
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
      let returnType = GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkAppliancePrefixesDelegatedStatics_2 operation.
     * @callback module:api/DelegatedApi~getNetworkAppliancePrefixesDelegatedStatics_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List static delegated prefixes for a network
     * List static delegated prefixes for a network
     * @param {String} networkId 
     * @param {module:api/DelegatedApi~getNetworkAppliancePrefixesDelegatedStatics_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>}
     */
    getNetworkAppliancePrefixesDelegatedStatics_2(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkAppliancePrefixesDelegatedStatics_2");
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
      let returnType = [GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner];
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/prefixes/delegated/statics', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkAppliancePrefixesDelegatedStatic_2 operation.
     * @callback module:api/DelegatedApi~updateNetworkAppliancePrefixesDelegatedStatic_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a static delegated prefix from a network
     * Update a static delegated prefix from a network
     * @param {String} networkId 
     * @param {String} staticDelegatedPrefixId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkAppliancePrefixesDelegatedStaticRequest} [updateNetworkAppliancePrefixesDelegatedStaticRequest] 
     * @param {module:api/DelegatedApi~updateNetworkAppliancePrefixesDelegatedStatic_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkAppliancePrefixesDelegatedStaticRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkAppliancePrefixesDelegatedStatic_2");
      }
      // verify the required parameter 'staticDelegatedPrefixId' is set
      if (staticDelegatedPrefixId === undefined || staticDelegatedPrefixId === null) {
        throw new Error("Missing the required parameter 'staticDelegatedPrefixId' when calling updateNetworkAppliancePrefixesDelegatedStatic_2");
      }

      let pathParams = {
        'networkId': networkId,
        'staticDelegatedPrefixId': staticDelegatedPrefixId
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
        '/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
