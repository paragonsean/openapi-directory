/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import APIModelsApiError from '../model/APIModelsApiError';
import APIPagedResponseUpdateSystemModelsPackage from '../model/APIPagedResponseUpdateSystemModelsPackage';
import UpdateSystemModelsPackage from '../model/UpdateSystemModelsPackage';

/**
* Packages service.
* @module api/PackagesApi
* @version v1
*/
export default class PackagesApi {

    /**
    * Constructs a new PackagesApi. 
    * @alias module:api/PackagesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the packagesDeletePackage operation.
     * @callback module:api/PackagesApi~packagesDeletePackageCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Package.
     * No Documentation Found.
     * @param {String} ID The Package ID to Delete
     * @param {module:api/PackagesApi~packagesDeletePackageCallback} callback The callback function, accepting three arguments: error, data, response
     */
    packagesDeletePackage(ID, callback) {
      let postBody = null;
      // verify the required parameter 'ID' is set
      if (ID === undefined || ID === null) {
        throw new Error("Missing the required parameter 'ID' when calling packagesDeletePackage");
      }

      let pathParams = {
        'ID': ID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/Packages/{ID}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the packagesGetPackage operation.
     * @callback module:api/PackagesApi~packagesGetPackageCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateSystemModelsPackage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find a Package.
     * No Documentation Found.
     * @param {String} ID The Package ID to Search for
     * @param {module:api/PackagesApi~packagesGetPackageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateSystemModelsPackage}
     */
    packagesGetPackage(ID, callback) {
      let postBody = null;
      // verify the required parameter 'ID' is set
      if (ID === undefined || ID === null) {
        throw new Error("Missing the required parameter 'ID' when calling packagesGetPackage");
      }

      let pathParams = {
        'ID': ID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = UpdateSystemModelsPackage;
      return this.apiClient.callApi(
        '/api/v2/Packages/{ID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the packagesGetPackages operation.
     * @callback module:api/PackagesApi~packagesGetPackagesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/APIPagedResponseUpdateSystemModelsPackage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Packages.
     * No Documentation Found.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Optional. The page limit. The default page limit is 10.
     * @param {Number} [offset] Optional. The page offset. The default page offset is 0.
     * @param {String} [packageTypeID] Optional. If provided, filters by PackageTypeID.
     * @param {Number} [version] Optional. If provided, filters by Version.
     * @param {Boolean} [released] Optional. If provided, filters by Released.
     * @param {module:api/PackagesApi~packagesGetPackagesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/APIPagedResponseUpdateSystemModelsPackage}
     */
    packagesGetPackages(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'PackageTypeID': opts['packageTypeID'],
        'Version': opts['version'],
        'Released': opts['released']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = APIPagedResponseUpdateSystemModelsPackage;
      return this.apiClient.callApi(
        '/api/v2/Packages', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the packagesPostPackage operation.
     * @callback module:api/PackagesApi~packagesPostPackageCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a Package to the Update System.
     * No Documentation Found.
     * @param {module:model/UpdateSystemModelsPackage} updateSystemModelsPackage The package to add.
     * @param {module:api/PackagesApi~packagesPostPackageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    packagesPostPackage(updateSystemModelsPackage, callback) {
      let postBody = updateSystemModelsPackage;
      // verify the required parameter 'updateSystemModelsPackage' is set
      if (updateSystemModelsPackage === undefined || updateSystemModelsPackage === null) {
        throw new Error("Missing the required parameter 'updateSystemModelsPackage' when calling packagesPostPackage");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/api/v2/Packages', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the packagesPutPackage operation.
     * @callback module:api/PackagesApi~packagesPutPackageCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify a Packge to the Update System.
     * No Documentation Found.
     * @param {String} ID The unique ID of the Package
     * @param {module:model/UpdateSystemModelsPackage} updateSystemModelsPackage The package to update.
     * @param {module:api/PackagesApi~packagesPutPackageCallback} callback The callback function, accepting three arguments: error, data, response
     */
    packagesPutPackage(ID, updateSystemModelsPackage, callback) {
      let postBody = updateSystemModelsPackage;
      // verify the required parameter 'ID' is set
      if (ID === undefined || ID === null) {
        throw new Error("Missing the required parameter 'ID' when calling packagesPutPackage");
      }
      // verify the required parameter 'updateSystemModelsPackage' is set
      if (updateSystemModelsPackage === undefined || updateSystemModelsPackage === null) {
        throw new Error("Missing the required parameter 'updateSystemModelsPackage' when calling packagesPutPackage");
      }

      let pathParams = {
        'ID': ID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/Packages/{ID}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
