/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import RmaDataRmaInterface from '../model/RmaDataRmaInterface';
import RmaRmaManagementV1SaveRmaPostRequest from '../model/RmaRmaManagementV1SaveRmaPostRequest';

/**
* ReturnsId service.
* @module api/ReturnsIdApi
* @version 2.2.10
*/
export default class ReturnsIdApi {

    /**
    * Constructs a new ReturnsIdApi. 
    * @alias module:api/ReturnsIdApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the rmaRmaManagementV1SaveRmaPut operation.
     * @callback module:api/ReturnsIdApi~rmaRmaManagementV1SaveRmaPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RmaDataRmaInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns/{id}
     * Save RMA
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {module:model/RmaRmaManagementV1SaveRmaPostRequest} [rmaRmaManagementV1SaveRmaPostRequest] 
     * @param {module:api/ReturnsIdApi~rmaRmaManagementV1SaveRmaPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RmaDataRmaInterface}
     */
    rmaRmaManagementV1SaveRmaPut(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['rmaRmaManagementV1SaveRmaPostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling rmaRmaManagementV1SaveRmaPut");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = RmaDataRmaInterface;
      return this.apiClient.callApi(
        '/V1/returns/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rmaRmaRepositoryV1DeleteDelete operation.
     * @callback module:api/ReturnsIdApi~rmaRmaRepositoryV1DeleteDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns/{id}
     * Delete RMA
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {module:model/RmaRmaManagementV1SaveRmaPostRequest} [rmaRmaManagementV1SaveRmaPostRequest] 
     * @param {module:api/ReturnsIdApi~rmaRmaRepositoryV1DeleteDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    rmaRmaRepositoryV1DeleteDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['rmaRmaManagementV1SaveRmaPostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling rmaRmaRepositoryV1DeleteDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/V1/returns/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rmaRmaRepositoryV1GetGet operation.
     * @callback module:api/ReturnsIdApi~rmaRmaRepositoryV1GetGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RmaDataRmaInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns/{id}
     * Return data object for specified RMA id
     * @param {Number} id 
     * @param {module:api/ReturnsIdApi~rmaRmaRepositoryV1GetGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RmaDataRmaInterface}
     */
    rmaRmaRepositoryV1GetGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling rmaRmaRepositoryV1GetGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = RmaDataRmaInterface;
      return this.apiClient.callApi(
        '/V1/returns/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
