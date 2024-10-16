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
import UpdateNetworkClientSplashAuthorizationStatusRequest from '../model/UpdateNetworkClientSplashAuthorizationStatusRequest';

/**
* SplashAuthorizationStatus service.
* @module api/SplashAuthorizationStatusApi
* @version 1.32.0
*/
export default class SplashAuthorizationStatusApi {

    /**
    * Constructs a new SplashAuthorizationStatusApi. 
    * @alias module:api/SplashAuthorizationStatusApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getNetworkClientSplashAuthorizationStatus_2 operation.
     * @callback module:api/SplashAuthorizationStatusApi~getNetworkClientSplashAuthorizationStatus_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the splash authorization for a client, for each SSID they've associated with through splash
     * Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param {String} networkId 
     * @param {String} clientId 
     * @param {module:api/SplashAuthorizationStatusApi~getNetworkClientSplashAuthorizationStatus_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkClientSplashAuthorizationStatus_2(networkId, clientId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkClientSplashAuthorizationStatus_2");
      }
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling getNetworkClientSplashAuthorizationStatus_2");
      }

      let pathParams = {
        'networkId': networkId,
        'clientId': clientId
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
        '/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkClientSplashAuthorizationStatus_2 operation.
     * @callback module:api/SplashAuthorizationStatusApi~updateNetworkClientSplashAuthorizationStatus_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a client's splash authorization
     * Update a client's splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param {String} networkId 
     * @param {String} clientId 
     * @param {module:model/UpdateNetworkClientSplashAuthorizationStatusRequest} updateNetworkClientSplashAuthorizationStatusRequest 
     * @param {module:api/SplashAuthorizationStatusApi~updateNetworkClientSplashAuthorizationStatus_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkClientSplashAuthorizationStatus_2(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest, callback) {
      let postBody = updateNetworkClientSplashAuthorizationStatusRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkClientSplashAuthorizationStatus_2");
      }
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling updateNetworkClientSplashAuthorizationStatus_2");
      }
      // verify the required parameter 'updateNetworkClientSplashAuthorizationStatusRequest' is set
      if (updateNetworkClientSplashAuthorizationStatusRequest === undefined || updateNetworkClientSplashAuthorizationStatusRequest === null) {
        throw new Error("Missing the required parameter 'updateNetworkClientSplashAuthorizationStatusRequest' when calling updateNetworkClientSplashAuthorizationStatus_2");
      }

      let pathParams = {
        'networkId': networkId,
        'clientId': clientId
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
        '/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
