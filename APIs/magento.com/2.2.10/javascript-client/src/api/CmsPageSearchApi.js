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
import CmsDataPageSearchResultsInterface from '../model/CmsDataPageSearchResultsInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* CmsPageSearch service.
* @module api/CmsPageSearchApi
* @version 2.2.10
*/
export default class CmsPageSearchApi {

    /**
    * Constructs a new CmsPageSearchApi. 
    * @alias module:api/CmsPageSearchApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the cmsPageRepositoryV1GetListGet operation.
     * @callback module:api/CmsPageSearchApi~cmsPageRepositoryV1GetListGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CmsDataPageSearchResultsInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * cmsPage/search
     * Retrieve pages matching the specified criteria.
     * @param {Object} opts Optional parameters
     * @param {String} [searchCriteriaFilterGroups0Filters0Field] Field
     * @param {String} [searchCriteriaFilterGroups0Filters0Value] Value
     * @param {String} [searchCriteriaFilterGroups0Filters0ConditionType] Condition type
     * @param {String} [searchCriteriaSortOrders0Field] Sorting field.
     * @param {String} [searchCriteriaSortOrders0Direction] Sorting direction.
     * @param {Number} [searchCriteriaPageSize] Page size.
     * @param {Number} [searchCriteriaCurrentPage] Current page.
     * @param {module:api/CmsPageSearchApi~cmsPageRepositoryV1GetListGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CmsDataPageSearchResultsInterface}
     */
    cmsPageRepositoryV1GetListGet(opts, callback) {
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
      let returnType = CmsDataPageSearchResultsInterface;
      return this.apiClient.callApi(
        '/V1/cmsPage/search', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
