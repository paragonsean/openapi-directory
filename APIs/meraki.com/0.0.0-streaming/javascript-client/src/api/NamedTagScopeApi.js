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
import CreateNetworkSmTargetGroupRequest from '../model/CreateNetworkSmTargetGroupRequest';

/**
* NamedTagScope service.
* @module api/NamedTagScopeApi
* @version 0.0.0-streaming
*/
export default class NamedTagScopeApi {

    /**
    * Constructs a new NamedTagScopeApi. 
    * @alias module:api/NamedTagScopeApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createNetworkSmTargetGroup operation.
     * @callback module:api/NamedTagScopeApi~createNetworkSmTargetGroupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a target group
     * Add a target group
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateNetworkSmTargetGroupRequest} [createNetworkSmTargetGroupRequest] 
     * @param {module:api/NamedTagScopeApi~createNetworkSmTargetGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createNetworkSmTargetGroup(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['createNetworkSmTargetGroupRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkSmTargetGroup");
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
        '/networks/{networkId}/sm/targetGroups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetworkSmTargetGroup operation.
     * @callback module:api/NamedTagScopeApi~deleteNetworkSmTargetGroupCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a target group from a network
     * Delete a target group from a network
     * @param {String} networkId 
     * @param {String} targetGroupId 
     * @param {module:api/NamedTagScopeApi~deleteNetworkSmTargetGroupCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetworkSmTargetGroup(networkId, targetGroupId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling deleteNetworkSmTargetGroup");
      }
      // verify the required parameter 'targetGroupId' is set
      if (targetGroupId === undefined || targetGroupId === null) {
        throw new Error("Missing the required parameter 'targetGroupId' when calling deleteNetworkSmTargetGroup");
      }

      let pathParams = {
        'networkId': networkId,
        'targetGroupId': targetGroupId
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
        '/networks/{networkId}/sm/targetGroups/{targetGroupId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkSmTargetGroup operation.
     * @callback module:api/NamedTagScopeApi~getNetworkSmTargetGroupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return a target group
     * Return a target group
     * @param {String} networkId 
     * @param {String} targetGroupId 
     * @param {Object} opts Optional parameters
     * @param {Boolean} [withDetails] Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
     * @param {module:api/NamedTagScopeApi~getNetworkSmTargetGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkSmTargetGroup(networkId, targetGroupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkSmTargetGroup");
      }
      // verify the required parameter 'targetGroupId' is set
      if (targetGroupId === undefined || targetGroupId === null) {
        throw new Error("Missing the required parameter 'targetGroupId' when calling getNetworkSmTargetGroup");
      }

      let pathParams = {
        'networkId': networkId,
        'targetGroupId': targetGroupId
      };
      let queryParams = {
        'withDetails': opts['withDetails']
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
        '/networks/{networkId}/sm/targetGroups/{targetGroupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkSmTargetGroups operation.
     * @callback module:api/NamedTagScopeApi~getNetworkSmTargetGroupsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the target groups in this network
     * List the target groups in this network
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {Boolean} [withDetails] Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
     * @param {module:api/NamedTagScopeApi~getNetworkSmTargetGroupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getNetworkSmTargetGroups(networkId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkSmTargetGroups");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
        'withDetails': opts['withDetails']
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
        '/networks/{networkId}/sm/targetGroups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkSmTargetGroup operation.
     * @callback module:api/NamedTagScopeApi~updateNetworkSmTargetGroupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a target group
     * Update a target group
     * @param {String} networkId 
     * @param {String} targetGroupId 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateNetworkSmTargetGroupRequest} [createNetworkSmTargetGroupRequest] 
     * @param {module:api/NamedTagScopeApi~updateNetworkSmTargetGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkSmTargetGroup(networkId, targetGroupId, opts, callback) {
      opts = opts || {};
      let postBody = opts['createNetworkSmTargetGroupRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkSmTargetGroup");
      }
      // verify the required parameter 'targetGroupId' is set
      if (targetGroupId === undefined || targetGroupId === null) {
        throw new Error("Missing the required parameter 'targetGroupId' when calling updateNetworkSmTargetGroup");
      }

      let pathParams = {
        'networkId': networkId,
        'targetGroupId': targetGroupId
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
        '/networks/{networkId}/sm/targetGroups/{targetGroupId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
