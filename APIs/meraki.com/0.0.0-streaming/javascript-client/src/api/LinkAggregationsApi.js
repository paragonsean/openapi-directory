/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CreateNetworkSwitchLinkAggregationRequest from '../model/CreateNetworkSwitchLinkAggregationRequest';
import UpdateNetworkSwitchLinkAggregationRequest from '../model/UpdateNetworkSwitchLinkAggregationRequest';

/**
* LinkAggregations service.
* @module api/LinkAggregationsApi
* @version 0.0.0-streaming
*/
export default class LinkAggregationsApi {

    /**
    * Constructs a new LinkAggregationsApi. 
    * @alias module:api/LinkAggregationsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createNetworkSwitchLinkAggregation operation.
     * @callback module:api/LinkAggregationsApi~createNetworkSwitchLinkAggregationCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a link aggregation group
     * Create a link aggregation group
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateNetworkSwitchLinkAggregationRequest} [createNetworkSwitchLinkAggregationRequest] 
     * @param {module:api/LinkAggregationsApi~createNetworkSwitchLinkAggregationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createNetworkSwitchLinkAggregation(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['createNetworkSwitchLinkAggregationRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkSwitchLinkAggregation");
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
        '/networks/{networkId}/switch/linkAggregations', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetworkSwitchLinkAggregation operation.
     * @callback module:api/LinkAggregationsApi~deleteNetworkSwitchLinkAggregationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Split a link aggregation group into separate ports
     * Split a link aggregation group into separate ports
     * @param {String} networkId 
     * @param {String} linkAggregationId 
     * @param {module:api/LinkAggregationsApi~deleteNetworkSwitchLinkAggregationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetworkSwitchLinkAggregation(networkId, linkAggregationId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling deleteNetworkSwitchLinkAggregation");
      }
      // verify the required parameter 'linkAggregationId' is set
      if (linkAggregationId === undefined || linkAggregationId === null) {
        throw new Error("Missing the required parameter 'linkAggregationId' when calling deleteNetworkSwitchLinkAggregation");
      }

      let pathParams = {
        'networkId': networkId,
        'linkAggregationId': linkAggregationId
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
        '/networks/{networkId}/switch/linkAggregations/{linkAggregationId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkSwitchLinkAggregations operation.
     * @callback module:api/LinkAggregationsApi~getNetworkSwitchLinkAggregationsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List link aggregation groups
     * List link aggregation groups
     * @param {String} networkId 
     * @param {module:api/LinkAggregationsApi~getNetworkSwitchLinkAggregationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getNetworkSwitchLinkAggregations(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkSwitchLinkAggregations");
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
      let returnType = [Object];
      return this.apiClient.callApi(
        '/networks/{networkId}/switch/linkAggregations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkSwitchLinkAggregation operation.
     * @callback module:api/LinkAggregationsApi~updateNetworkSwitchLinkAggregationCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a link aggregation group
     * Update a link aggregation group
     * @param {String} networkId 
     * @param {String} linkAggregationId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkSwitchLinkAggregationRequest} [updateNetworkSwitchLinkAggregationRequest] 
     * @param {module:api/LinkAggregationsApi~updateNetworkSwitchLinkAggregationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkSwitchLinkAggregation(networkId, linkAggregationId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkSwitchLinkAggregationRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkSwitchLinkAggregation");
      }
      // verify the required parameter 'linkAggregationId' is set
      if (linkAggregationId === undefined || linkAggregationId === null) {
        throw new Error("Missing the required parameter 'linkAggregationId' when calling updateNetworkSwitchLinkAggregation");
      }

      let pathParams = {
        'networkId': networkId,
        'linkAggregationId': linkAggregationId
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
        '/networks/{networkId}/switch/linkAggregations/{linkAggregationId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
