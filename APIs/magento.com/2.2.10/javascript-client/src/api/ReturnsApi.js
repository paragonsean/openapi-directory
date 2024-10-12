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
import RmaDataRmaSearchResultInterface from '../model/RmaDataRmaSearchResultInterface';
import RmaRmaManagementV1SaveRmaPostRequest from '../model/RmaRmaManagementV1SaveRmaPostRequest';

/**
* Returns service.
* @module api/ReturnsApi
* @version 2.2.10
*/
export default class ReturnsApi {

    /**
    * Constructs a new ReturnsApi. 
    * @alias module:api/ReturnsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the rmaRmaManagementV1SaveRmaPost operation.
     * @callback module:api/ReturnsApi~rmaRmaManagementV1SaveRmaPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RmaDataRmaInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns
     * Save RMA
     * @param {Object} opts Optional parameters
     * @param {module:model/RmaRmaManagementV1SaveRmaPostRequest} [rmaRmaManagementV1SaveRmaPostRequest] 
     * @param {module:api/ReturnsApi~rmaRmaManagementV1SaveRmaPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RmaDataRmaInterface}
     */
    rmaRmaManagementV1SaveRmaPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['rmaRmaManagementV1SaveRmaPostRequest'];

      let pathParams = {
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
        '/V1/returns', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rmaRmaManagementV1SearchGet operation.
     * @callback module:api/ReturnsApi~rmaRmaManagementV1SearchGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RmaDataRmaSearchResultInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * returns
     * Return list of rma data objects based on search criteria
     * @param {Object} opts Optional parameters
     * @param {String} [searchCriteriaFilterGroups0Filters0Field] Field
     * @param {String} [searchCriteriaFilterGroups0Filters0Value] Value
     * @param {String} [searchCriteriaFilterGroups0Filters0ConditionType] Condition type
     * @param {String} [searchCriteriaSortOrders0Field] Sorting field.
     * @param {String} [searchCriteriaSortOrders0Direction] Sorting direction.
     * @param {Number} [searchCriteriaPageSize] Page size.
     * @param {Number} [searchCriteriaCurrentPage] Current page.
     * @param {module:api/ReturnsApi~rmaRmaManagementV1SearchGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RmaDataRmaSearchResultInterface}
     */
    rmaRmaManagementV1SearchGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'searchCriteria[filterGroups][0][filters][0][field]': opts['searchCriteriaFilterGroups0Filters0Field'],
        'searchCriteria[filterGroups][0][filters][0][value]': opts['searchCriteriaFilterGroups0Filters0Value'],
        'searchCriteria[filterGroups][0][filters][0][conditionType]': opts['searchCriteriaFilterGroups0Filters0ConditionType'],
        'searchCriteria[sortOrders][0][field]': opts['searchCriteriaSortOrders0Field'],
        'searchCriteria[sortOrders][0][direction]': opts['searchCriteriaSortOrders0Direction'],
        'searchCriteria[pageSize]': opts['searchCriteriaPageSize'],
        'searchCriteria[currentPage]': opts['searchCriteriaCurrentPage']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = RmaDataRmaSearchResultInterface;
      return this.apiClient.callApi(
        '/V1/returns', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
