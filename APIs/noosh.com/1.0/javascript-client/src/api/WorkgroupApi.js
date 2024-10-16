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
import ClientWorkgroupExpandVO from '../model/ClientWorkgroupExpandVO';
import ClientWorkgroupListVO from '../model/ClientWorkgroupListVO';
import HTTPStatusVO from '../model/HTTPStatusVO';
import SupplierWorkgroupExpandVO from '../model/SupplierWorkgroupExpandVO';
import SupplierWorkgroupListVO from '../model/SupplierWorkgroupListVO';
import WorkgroupExpandVO from '../model/WorkgroupExpandVO';
import WorkgroupHTTPStatusVO from '../model/WorkgroupHTTPStatusVO';
import WorkgroupListVO from '../model/WorkgroupListVO';
import WorkgroupUpdPersistVO from '../model/WorkgroupUpdPersistVO';

/**
* Workgroup service.
* @module api/WorkgroupApi
* @version 1.0
*/
export default class WorkgroupApi {

    /**
    * Constructs a new WorkgroupApi. 
    * @alias module:api/WorkgroupApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getClientWorkgroupList operation.
     * @callback module:api/WorkgroupApi~getClientWorkgroupListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClientWorkgroupListVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List client workgroups
     * List client workgroups
     * @param {String} workgroupId 
     * @param {module:api/WorkgroupApi~getClientWorkgroupListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClientWorkgroupListVO}
     */
    getClientWorkgroupList(workgroupId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getClientWorkgroupList");
      }

      let pathParams = {
        'workgroup_id': workgroupId
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
      let returnType = ClientWorkgroupListVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/clientWorkgroups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSpecificClientWorkgroup operation.
     * @callback module:api/WorkgroupApi~getSpecificClientWorkgroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClientWorkgroupExpandVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a specific client workgroups
     * Get a specific client workgroups
     * @param {String} workgroupId 
     * @param {String} clientWorkgroupId 
     * @param {module:api/WorkgroupApi~getSpecificClientWorkgroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClientWorkgroupExpandVO}
     */
    getSpecificClientWorkgroup(workgroupId, clientWorkgroupId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getSpecificClientWorkgroup");
      }
      // verify the required parameter 'clientWorkgroupId' is set
      if (clientWorkgroupId === undefined || clientWorkgroupId === null) {
        throw new Error("Missing the required parameter 'clientWorkgroupId' when calling getSpecificClientWorkgroup");
      }

      let pathParams = {
        'workgroup_id': workgroupId,
        'client_workgroup_id': clientWorkgroupId
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
      let returnType = ClientWorkgroupExpandVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSupplierWorkgroupDetail operation.
     * @callback module:api/WorkgroupApi~getSupplierWorkgroupDetailCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SupplierWorkgroupExpandVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the specific supplier of My Group
     * Get the specific supplier of My Group
     * @param {String} workgroupId 
     * @param {String} buSupplierWorkgroupId 
     * @param {module:api/WorkgroupApi~getSupplierWorkgroupDetailCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SupplierWorkgroupExpandVO}
     */
    getSupplierWorkgroupDetail(workgroupId, buSupplierWorkgroupId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getSupplierWorkgroupDetail");
      }
      // verify the required parameter 'buSupplierWorkgroupId' is set
      if (buSupplierWorkgroupId === undefined || buSupplierWorkgroupId === null) {
        throw new Error("Missing the required parameter 'buSupplierWorkgroupId' when calling getSupplierWorkgroupDetail");
      }

      let pathParams = {
        'workgroup_id': workgroupId,
        'bu_supplier_workgroup_id': buSupplierWorkgroupId
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
      let returnType = SupplierWorkgroupExpandVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/supplierWorkgroups/{bu_supplier_workgroup_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSupplierWorkgroupList operation.
     * @callback module:api/WorkgroupApi~getSupplierWorkgroupListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SupplierWorkgroupListVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List supplier workgroups
     * List supplier workgroups
     * @param {String} workgroupId 
     * @param {module:api/WorkgroupApi~getSupplierWorkgroupListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SupplierWorkgroupListVO}
     */
    getSupplierWorkgroupList(workgroupId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getSupplierWorkgroupList");
      }

      let pathParams = {
        'workgroup_id': workgroupId
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
      let returnType = SupplierWorkgroupListVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/supplierWorkgroups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWorkgroupDetail operation.
     * @callback module:api/WorkgroupApi~getWorkgroupDetailCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WorkgroupExpandVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Detail workgroup info
     * Detail workgroup info
     * @param {String} workgroupId 
     * @param {module:api/WorkgroupApi~getWorkgroupDetailCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WorkgroupExpandVO}
     */
    getWorkgroupDetail(workgroupId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getWorkgroupDetail");
      }

      let pathParams = {
        'workgroup_id': workgroupId
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
      let returnType = WorkgroupExpandVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/detail', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWorkgroupList operation.
     * @callback module:api/WorkgroupApi~getWorkgroupListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WorkgroupListVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the workgroups
     * List the workgroups
     * @param {Object} opts Optional parameters
     * @param {String} [workgroupName] Workgroup Name
     * @param {Array.<String>} [workgroupTypes] 1000001 for Buyer, 1000002 for supplier, 1000003 for agent, 1000004 for Broker/Outsourcer and 1000005 for Partner
     * @param {module:api/WorkgroupApi~getWorkgroupListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WorkgroupListVO}
     */
    getWorkgroupList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'workgroup_name': opts['workgroupName'],
        'workgroup_types': this.apiClient.buildCollectionParam(opts['workgroupTypes'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*', 'application/json', 'application/x-json-smile', 'application/x-yaml', 'application/xml', 'text/csv', 'text/x-yaml', 'text/xml'];
      let returnType = WorkgroupListVO;
      return this.apiClient.callApi(
        '/v1/workgroups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putWorkgroup operation.
     * @callback module:api/WorkgroupApi~putWorkgroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WorkgroupHTTPStatusVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a specific Workgroup
     * Update a specific Workgroup
     * @param {String} workgroupId 
     * @param {Object} opts Optional parameters
     * @param {module:model/WorkgroupUpdPersistVO} [workgroupUpdPersistVO] 
     * @param {module:api/WorkgroupApi~putWorkgroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WorkgroupHTTPStatusVO}
     */
    putWorkgroup(workgroupId, opts, callback) {
      opts = opts || {};
      let postBody = opts['workgroupUpdPersistVO'];
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling putWorkgroup");
      }

      let pathParams = {
        'workgroup_id': workgroupId
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
      let returnType = WorkgroupHTTPStatusVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/detail', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
