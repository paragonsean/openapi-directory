/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import HTTPStatusVO from '../model/HTTPStatusVO';
import RfeExpandVO from '../model/RfeExpandVO';
import RfeListVO from '../model/RfeListVO';
import RfePO from '../model/RfePO';
import RfqVO from '../model/RfqVO';

/**
* RFE service.
* @module api/RFEApi
* @version 1.0
*/
export default class RFEApi {

    /**
    * Constructs a new RFEApi. 
    * @alias module:api/RFEApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getRfe operation.
     * @callback module:api/RFEApi~getRfeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RfeExpandVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a specific Rfe
     * Get a specific Rfe
     * @param {String} workgroupId 
     * @param {String} projectId 
     * @param {String} rfeId 
     * @param {module:api/RFEApi~getRfeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RfeExpandVO}
     */
    getRfe(workgroupId, projectId, rfeId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getRfe");
      }
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getRfe");
      }
      // verify the required parameter 'rfeId' is set
      if (rfeId === undefined || rfeId === null) {
        throw new Error("Missing the required parameter 'rfeId' when calling getRfe");
      }

      let pathParams = {
        'workgroup_id': workgroupId,
        'project_id': projectId,
        'rfe_id': rfeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*', 'application/json', 'application/x-json-smile', 'application/x-yaml', 'application/xml', 'text/csv', 'text/x-yaml', 'text/xml'];
      let returnType = RfeExpandVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/projects/{project_id}/rfes/{rfe_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRfeList operation.
     * @callback module:api/RFEApi~getRfeListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RfeListVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the RFES
     * List the RFES
     * @param {String} workgroupId 
     * @param {String} projectId 
     * @param {module:api/RFEApi~getRfeListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RfeListVO}
     */
    getRfeList(workgroupId, projectId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getRfeList");
      }
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getRfeList");
      }

      let pathParams = {
        'workgroup_id': workgroupId,
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*', 'application/json', 'application/x-json-smile', 'application/x-yaml', 'application/xml', 'text/csv', 'text/x-yaml', 'text/xml'];
      let returnType = RfeListVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/projects/{project_id}/rfes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postRfe operation.
     * @callback module:api/RFEApi~postRfeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RfqVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a RFE
     * Create a RFE
     * @param {String} workgroupId 
     * @param {String} projectId 
     * @param {Object} opts Optional parameters
     * @param {module:model/RfePO} [rfePO] 
     * @param {module:api/RFEApi~postRfeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RfqVO}
     */
    postRfe(workgroupId, projectId, opts, callback) {
      opts = opts || {};
      let postBody = opts['rfePO'];
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling postRfe");
      }
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling postRfe");
      }

      let pathParams = {
        'workgroup_id': workgroupId,
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-json-smile', 'application/x-yaml', 'application/xml', 'text/csv', 'text/x-yaml', 'text/xml'];
      let accepts = ['*/*', 'application/json', 'application/x-json-smile', 'application/x-yaml', 'application/xml', 'text/csv', 'text/x-yaml', 'text/xml'];
      let returnType = RfqVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/projects/{project_id}/rfes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
