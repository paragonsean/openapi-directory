/**
 * FabricAdminClient
 * Volume operation endpoints and objects.
 *
 * The version of the OpenAPI document: 2018-10-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Volume from '../model/Volume';
import VolumeList from '../model/VolumeList';

/**
* Volumes service.
* @module api/VolumesApi
* @version 2018-10-01
*/
export default class VolumesApi {

    /**
    * Constructs a new VolumesApi. 
    * @alias module:api/VolumesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the volumesGet operation.
     * @callback module:api/VolumesApi~volumesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Volume} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the requested a storage volume.
     * @param {String} subscriptionId Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} resourceGroupName Name of the resource group.
     * @param {String} location Location of the resource.
     * @param {String} scaleUnit Name of the scale units.
     * @param {String} storageSubSystem Name of the storage system.
     * @param {String} volume Name of the storage volume.
     * @param {String} apiVersion Client API Version.
     * @param {module:api/VolumesApi~volumesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Volume}
     */
    volumesGet(subscriptionId, resourceGroupName, location, scaleUnit, storageSubSystem, volume, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling volumesGet");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling volumesGet");
      }
      // verify the required parameter 'location' is set
      if (location === undefined || location === null) {
        throw new Error("Missing the required parameter 'location' when calling volumesGet");
      }
      // verify the required parameter 'scaleUnit' is set
      if (scaleUnit === undefined || scaleUnit === null) {
        throw new Error("Missing the required parameter 'scaleUnit' when calling volumesGet");
      }
      // verify the required parameter 'storageSubSystem' is set
      if (storageSubSystem === undefined || storageSubSystem === null) {
        throw new Error("Missing the required parameter 'storageSubSystem' when calling volumesGet");
      }
      // verify the required parameter 'volume' is set
      if (volume === undefined || volume === null) {
        throw new Error("Missing the required parameter 'volume' when calling volumesGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling volumesGet");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'location': location,
        'scaleUnit': scaleUnit,
        'storageSubSystem': storageSubSystem,
        'volume': volume
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
      let returnType = Volume;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/storageSubSystems/{storageSubSystem}/volumes/{volume}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the volumesList operation.
     * @callback module:api/VolumesApi~volumesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VolumeList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a list of all storage volumes at a location.
     * @param {String} subscriptionId Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} resourceGroupName Name of the resource group.
     * @param {String} location Location of the resource.
     * @param {String} scaleUnit Name of the scale units.
     * @param {String} storageSubSystem Name of the storage system.
     * @param {String} apiVersion Client API Version.
     * @param {Object} opts Optional parameters
     * @param {String} [filter] OData filter parameter.
     * @param {module:api/VolumesApi~volumesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VolumeList}
     */
    volumesList(subscriptionId, resourceGroupName, location, scaleUnit, storageSubSystem, apiVersion, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling volumesList");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling volumesList");
      }
      // verify the required parameter 'location' is set
      if (location === undefined || location === null) {
        throw new Error("Missing the required parameter 'location' when calling volumesList");
      }
      // verify the required parameter 'scaleUnit' is set
      if (scaleUnit === undefined || scaleUnit === null) {
        throw new Error("Missing the required parameter 'scaleUnit' when calling volumesList");
      }
      // verify the required parameter 'storageSubSystem' is set
      if (storageSubSystem === undefined || storageSubSystem === null) {
        throw new Error("Missing the required parameter 'storageSubSystem' when calling volumesList");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling volumesList");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'location': location,
        'scaleUnit': scaleUnit,
        'storageSubSystem': storageSubSystem
      };
      let queryParams = {
        'api-version': apiVersion,
        '$filter': opts['filter']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VolumeList;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/storageSubSystems/{storageSubSystem}/volumes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
