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
import UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest from '../model/UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest';
import UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest from '../model/UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest';

/**
* ConnectivityMonitoringDestinations service.
* @module api/ConnectivityMonitoringDestinationsApi
* @version 1.32.0
*/
export default class ConnectivityMonitoringDestinationsApi {

    /**
    * Constructs a new ConnectivityMonitoringDestinationsApi. 
    * @alias module:api/ConnectivityMonitoringDestinationsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getNetworkApplianceConnectivityMonitoringDestinations_1 operation.
     * @callback module:api/ConnectivityMonitoringDestinationsApi~getNetworkApplianceConnectivityMonitoringDestinations_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the connectivity testing destinations for an MX network
     * Return the connectivity testing destinations for an MX network
     * @param {String} networkId 
     * @param {module:api/ConnectivityMonitoringDestinationsApi~getNetworkApplianceConnectivityMonitoringDestinations_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkApplianceConnectivityMonitoringDestinations_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceConnectivityMonitoringDestinations_1");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/connectivityMonitoringDestinations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkCellularGatewayConnectivityMonitoringDestinations_1 operation.
     * @callback module:api/ConnectivityMonitoringDestinationsApi~getNetworkCellularGatewayConnectivityMonitoringDestinations_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the connectivity testing destinations for an MG network
     * Return the connectivity testing destinations for an MG network
     * @param {String} networkId 
     * @param {module:api/ConnectivityMonitoringDestinationsApi~getNetworkCellularGatewayConnectivityMonitoringDestinations_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkCellularGatewayConnectivityMonitoringDestinations_1");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkApplianceConnectivityMonitoringDestinations_1 operation.
     * @callback module:api/ConnectivityMonitoringDestinationsApi~updateNetworkApplianceConnectivityMonitoringDestinations_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the connectivity testing destinations for an MX network
     * Update the connectivity testing destinations for an MX network
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest} [updateNetworkApplianceConnectivityMonitoringDestinationsRequest] 
     * @param {module:api/ConnectivityMonitoringDestinationsApi~updateNetworkApplianceConnectivityMonitoringDestinations_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkApplianceConnectivityMonitoringDestinations_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkApplianceConnectivityMonitoringDestinationsRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkApplianceConnectivityMonitoringDestinations_1");
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
        '/networks/{networkId}/appliance/connectivityMonitoringDestinations', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkCellularGatewayConnectivityMonitoringDestinations_1 operation.
     * @callback module:api/ConnectivityMonitoringDestinationsApi~updateNetworkCellularGatewayConnectivityMonitoringDestinations_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the connectivity testing destinations for an MG network
     * Update the connectivity testing destinations for an MG network
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest} [updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest] 
     * @param {module:api/ConnectivityMonitoringDestinationsApi~updateNetworkCellularGatewayConnectivityMonitoringDestinations_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkCellularGatewayConnectivityMonitoringDestinations_1");
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
        '/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
