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
import TaxDataTaxClassSearchResultsInterface from '../model/TaxDataTaxClassSearchResultsInterface';

/**
* TaxClassesSearch service.
* @module api/TaxClassesSearchApi
* @version 2.2.10
*/
export default class TaxClassesSearchApi {

    /**
    * Constructs a new TaxClassesSearchApi. 
    * @alias module:api/TaxClassesSearchApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the taxTaxClassRepositoryV1GetListGet operation.
     * @callback module:api/TaxClassesSearchApi~taxTaxClassRepositoryV1GetListGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaxDataTaxClassSearchResultsInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * taxClasses/search
     * Retrieve tax classes which match a specific criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxClassRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
     * @param {Object} opts Optional parameters
     * @param {String} [searchCriteriaFilterGroups0Filters0Field] Field
     * @param {String} [searchCriteriaFilterGroups0Filters0Value] Value
     * @param {String} [searchCriteriaFilterGroups0Filters0ConditionType] Condition type
     * @param {String} [searchCriteriaSortOrders0Field] Sorting field.
     * @param {String} [searchCriteriaSortOrders0Direction] Sorting direction.
     * @param {Number} [searchCriteriaPageSize] Page size.
     * @param {Number} [searchCriteriaCurrentPage] Current page.
     * @param {module:api/TaxClassesSearchApi~taxTaxClassRepositoryV1GetListGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaxDataTaxClassSearchResultsInterface}
     */
    taxTaxClassRepositoryV1GetListGet(opts, callback) {
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
      let returnType = TaxDataTaxClassSearchResultsInterface;
      return this.apiClient.callApi(
        '/V1/taxClasses/search', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
