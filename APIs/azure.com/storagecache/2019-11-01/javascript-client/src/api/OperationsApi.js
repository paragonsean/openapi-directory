/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ApiOperationListResult from '../model/ApiOperationListResult';
import CloudError from '../model/CloudError';

/**
* Operations service.
* @module api/OperationsApi
* @version 2019-11-01
*/
export default class OperationsApi {

    /**
    * Constructs a new OperationsApi. 
    * @alias module:api/OperationsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the operationsList operation.
     * @callback module:api/OperationsApi~operationsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiOperationListResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all of the available Resource Provider operations.
     * @param {String} apiVersion Client API version.
     * @param {module:api/OperationsApi~operationsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiOperationListResult}
     */
    operationsList(apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling operationsList");
      }

      let pathParams = {
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
      let returnType = ApiOperationListResult;
      return this.apiClient.callApi(
        '/providers/Microsoft.StorageCache/operations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
