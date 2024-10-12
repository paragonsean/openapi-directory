/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import BandwidthSchedule from '../model/BandwidthSchedule';
import BandwidthSchedulesList from '../model/BandwidthSchedulesList';
import CloudError from '../model/CloudError';

/**
* BandwidthSchedules service.
* @module api/BandwidthSchedulesApi
* @version 2019-03-01
*/
export default class BandwidthSchedulesApi {

    /**
    * Constructs a new BandwidthSchedulesApi. 
    * @alias module:api/BandwidthSchedulesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the bandwidthSchedulesCreateOrUpdate operation.
     * @callback module:api/BandwidthSchedulesApi~bandwidthSchedulesCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BandwidthSchedule} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates or updates a bandwidth schedule.
     * @param {String} deviceName The device name.
     * @param {String} name The bandwidth schedule name which needs to be added/updated.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The resource group name.
     * @param {String} apiVersion The API version.
     * @param {module:model/BandwidthSchedule} parameters The bandwidth schedule to be added or updated.
     * @param {module:api/BandwidthSchedulesApi~bandwidthSchedulesCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BandwidthSchedule}
     */
    bandwidthSchedulesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, parameters, callback) {
      let postBody = parameters;
      // verify the required parameter 'deviceName' is set
      if (deviceName === undefined || deviceName === null) {
        throw new Error("Missing the required parameter 'deviceName' when calling bandwidthSchedulesCreateOrUpdate");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling bandwidthSchedulesCreateOrUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling bandwidthSchedulesCreateOrUpdate");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling bandwidthSchedulesCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling bandwidthSchedulesCreateOrUpdate");
      }
      // verify the required parameter 'parameters' is set
      if (parameters === undefined || parameters === null) {
        throw new Error("Missing the required parameter 'parameters' when calling bandwidthSchedulesCreateOrUpdate");
      }

      let pathParams = {
        'deviceName': deviceName,
        'name': name,
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = BandwidthSchedule;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules/{name}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the bandwidthSchedulesDelete operation.
     * @callback module:api/BandwidthSchedulesApi~bandwidthSchedulesDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified bandwidth schedule.
     * @param {String} deviceName The device name.
     * @param {String} name The bandwidth schedule name.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The resource group name.
     * @param {String} apiVersion The API version.
     * @param {module:api/BandwidthSchedulesApi~bandwidthSchedulesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    bandwidthSchedulesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'deviceName' is set
      if (deviceName === undefined || deviceName === null) {
        throw new Error("Missing the required parameter 'deviceName' when calling bandwidthSchedulesDelete");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling bandwidthSchedulesDelete");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling bandwidthSchedulesDelete");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling bandwidthSchedulesDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling bandwidthSchedulesDelete");
      }

      let pathParams = {
        'deviceName': deviceName,
        'name': name,
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules/{name}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the bandwidthSchedulesGet operation.
     * @callback module:api/BandwidthSchedulesApi~bandwidthSchedulesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BandwidthSchedule} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the properties of the specified bandwidth schedule.
     * @param {String} deviceName The device name.
     * @param {String} name The bandwidth schedule name.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The resource group name.
     * @param {String} apiVersion The API version.
     * @param {module:api/BandwidthSchedulesApi~bandwidthSchedulesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BandwidthSchedule}
     */
    bandwidthSchedulesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'deviceName' is set
      if (deviceName === undefined || deviceName === null) {
        throw new Error("Missing the required parameter 'deviceName' when calling bandwidthSchedulesGet");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling bandwidthSchedulesGet");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling bandwidthSchedulesGet");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling bandwidthSchedulesGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling bandwidthSchedulesGet");
      }

      let pathParams = {
        'deviceName': deviceName,
        'name': name,
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BandwidthSchedule;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules/{name}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the bandwidthSchedulesListByDataBoxEdgeDevice operation.
     * @callback module:api/BandwidthSchedulesApi~bandwidthSchedulesListByDataBoxEdgeDeviceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BandwidthSchedulesList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets all the bandwidth schedules for a data box edge/gateway device.
     * @param {String} deviceName The device name.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The resource group name.
     * @param {String} apiVersion The API version.
     * @param {module:api/BandwidthSchedulesApi~bandwidthSchedulesListByDataBoxEdgeDeviceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BandwidthSchedulesList}
     */
    bandwidthSchedulesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'deviceName' is set
      if (deviceName === undefined || deviceName === null) {
        throw new Error("Missing the required parameter 'deviceName' when calling bandwidthSchedulesListByDataBoxEdgeDevice");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling bandwidthSchedulesListByDataBoxEdgeDevice");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling bandwidthSchedulesListByDataBoxEdgeDevice");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling bandwidthSchedulesListByDataBoxEdgeDevice");
      }

      let pathParams = {
        'deviceName': deviceName,
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BandwidthSchedulesList;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
