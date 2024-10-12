/**
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AddClutterRequest from '../model/AddClutterRequest';

/**
* Manage service.
* @module api/ManageApi
* @version 2.0.0
*/
export default class ManageApi {

    /**
    * Constructs a new ManageApi. 
    * @alias module:api/ManageApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addClutter operation.
     * @callback module:api/ManageApi~addClutterCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upload clutter data as GeoJSON
     * Upload GeoJSON lineString and polygon features to your account. The height property is in metres and the material code / type / attenuation are.. 1 Trees – 0.25,2Trees + 0.5,3 Timber – 1.0,4 Timber + 1.5,5 Brick –  1.5,6 Brick + 2.0,7 Concrete – 3.0,8 Concrete + 4.0,9 Metal 6.0
     * @param {module:model/AddClutterRequest} addClutterRequest 
     * @param {module:api/ManageApi~addClutterCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addClutter(addClutterRequest, callback) {
      let postBody = addClutterRequest;
      // verify the required parameter 'addClutterRequest' is set
      if (addClutterRequest === undefined || addClutterRequest === null) {
        throw new Error("Missing the required parameter 'addClutterRequest' when calling addClutter");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/clutter/add', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the callDelete operation.
     * @callback module:api/ManageApi~callDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a calculation from the database.
     * Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.
     * @param {Number} cid Unique calculation ID number
     * @param {module:api/ManageApi~callDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    callDelete(cid, callback) {
      let postBody = null;
      // verify the required parameter 'cid' is set
      if (cid === undefined || cid === null) {
        throw new Error("Missing the required parameter 'cid' when calling callDelete");
      }

      let pathParams = {
      };
      let queryParams = {
        'cid': cid
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/archive/delete', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the callExport operation.
     * @callback module:api/ManageApi~callExportCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Export a calculation in a GIS file format
     * Download your data in a format suitable for a third party viewer like Google Earth or ESRI Arcmap.
     * @param {String} file Calculation file name
     * @param {module:model/String} fmt Raster/Vector file format: KML, KMZ, SHP, GeoTIFF
     * @param {module:api/ManageApi~callExportCallback} callback The callback function, accepting three arguments: error, data, response
     */
    callExport(file, fmt, callback) {
      let postBody = null;
      // verify the required parameter 'file' is set
      if (file === undefined || file === null) {
        throw new Error("Missing the required parameter 'file' when calling callExport");
      }
      // verify the required parameter 'fmt' is set
      if (fmt === undefined || fmt === null) {
        throw new Error("Missing the required parameter 'fmt' when calling callExport");
      }

      let pathParams = {
      };
      let queryParams = {
        'file': file,
        'fmt': fmt
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/archive/export', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetwork operation.
     * @callback module:api/ManageApi~deleteNetworkCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an entire network
     * Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.
     * @param {String} nid Network name
     * @param {module:api/ManageApi~deleteNetworkCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetwork(nid, callback) {
      let postBody = null;
      // verify the required parameter 'nid' is set
      if (nid === undefined || nid === null) {
        throw new Error("Missing the required parameter 'nid' when calling deleteNetwork");
      }

      let pathParams = {
      };
      let queryParams = {
        'nid': nid
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/archive/delete/network', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the list operation.
     * @callback module:api/ManageApi~listCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List calculations from your archive
     * List your area and path calculations, sorted by time and limited to the last few hundred. To fetch all for a given network append a 'net' filter with the network name.
     * @param {Object} opts Optional parameters
     * @param {Number} [n] North bounding box
     * @param {Number} [e] East bounding box
     * @param {Number} [s] South bounding box
     * @param {Number} [w] West bounding box
     * @param {module:api/ManageApi~listCallback} callback The callback function, accepting three arguments: error, data, response
     */
    list(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'n': opts['n'],
        'e': opts['e'],
        's': opts['s'],
        'w': opts['w']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/archive/list', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
