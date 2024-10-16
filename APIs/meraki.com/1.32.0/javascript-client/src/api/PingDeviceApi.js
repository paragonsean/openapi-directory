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
import CreateDeviceLiveToolsPing201Response from '../model/CreateDeviceLiveToolsPing201Response';
import CreateDeviceLiveToolsPingDeviceRequest from '../model/CreateDeviceLiveToolsPingDeviceRequest';
import GetDeviceLiveToolsPing200Response from '../model/GetDeviceLiveToolsPing200Response';

/**
* PingDevice service.
* @module api/PingDeviceApi
* @version 1.32.0
*/
export default class PingDeviceApi {

    /**
    * Constructs a new PingDeviceApi. 
    * @alias module:api/PingDeviceApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createDeviceLiveToolsPingDevice_1 operation.
     * @callback module:api/PingDeviceApi~createDeviceLiveToolsPingDevice_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateDeviceLiveToolsPing201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Enqueue a job to check connectivity status to the device
     * Enqueue a job to check connectivity status to the device
     * @param {String} serial 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateDeviceLiveToolsPingDeviceRequest} [createDeviceLiveToolsPingDeviceRequest] 
     * @param {module:api/PingDeviceApi~createDeviceLiveToolsPingDevice_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateDeviceLiveToolsPing201Response}
     */
    createDeviceLiveToolsPingDevice_1(serial, opts, callback) {
      opts = opts || {};
      let postBody = opts['createDeviceLiveToolsPingDeviceRequest'];
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling createDeviceLiveToolsPingDevice_1");
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
      let returnType = CreateDeviceLiveToolsPing201Response;
      return this.apiClient.callApi(
        '/devices/{serial}/liveTools/pingDevice', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDeviceLiveToolsPingDevice_1 operation.
     * @callback module:api/PingDeviceApi~getDeviceLiveToolsPingDevice_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDeviceLiveToolsPing200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return a ping device job
     * Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.
     * @param {String} serial 
     * @param {String} id 
     * @param {module:api/PingDeviceApi~getDeviceLiveToolsPingDevice_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDeviceLiveToolsPing200Response}
     */
    getDeviceLiveToolsPingDevice_1(serial, id, callback) {
      let postBody = null;
      // verify the required parameter 'serial' is set
      if (serial === undefined || serial === null) {
        throw new Error("Missing the required parameter 'serial' when calling getDeviceLiveToolsPingDevice_1");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getDeviceLiveToolsPingDevice_1");
      }

      let pathParams = {
        'serial': serial,
        'id': id
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
      let returnType = GetDeviceLiveToolsPing200Response;
      return this.apiClient.callApi(
        '/devices/{serial}/liveTools/pingDevice/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
