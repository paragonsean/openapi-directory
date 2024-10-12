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
import CatalogDataProductAttributeInterface from '../model/CatalogDataProductAttributeInterface';
import CatalogDataProductAttributeSearchResultsInterface from '../model/CatalogDataProductAttributeSearchResultsInterface';
import CatalogProductAttributeRepositoryV1SavePostRequest from '../model/CatalogProductAttributeRepositoryV1SavePostRequest';
import ErrorResponse from '../model/ErrorResponse';

/**
* ProductsAttributes service.
* @module api/ProductsAttributesApi
* @version 2.2.10
*/
export default class ProductsAttributesApi {

    /**
    * Constructs a new ProductsAttributesApi. 
    * @alias module:api/ProductsAttributesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the catalogProductAttributeRepositoryV1GetListGet operation.
     * @callback module:api/ProductsAttributesApi~catalogProductAttributeRepositoryV1GetListGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CatalogDataProductAttributeSearchResultsInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/attributes
     * Retrieve all attributes for entity type
     * @param {Object} opts Optional parameters
     * @param {String} [searchCriteriaFilterGroups0Filters0Field] Field
     * @param {String} [searchCriteriaFilterGroups0Filters0Value] Value
     * @param {String} [searchCriteriaFilterGroups0Filters0ConditionType] Condition type
     * @param {String} [searchCriteriaSortOrders0Field] Sorting field.
     * @param {String} [searchCriteriaSortOrders0Direction] Sorting direction.
     * @param {Number} [searchCriteriaPageSize] Page size.
     * @param {Number} [searchCriteriaCurrentPage] Current page.
     * @param {module:api/ProductsAttributesApi~catalogProductAttributeRepositoryV1GetListGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CatalogDataProductAttributeSearchResultsInterface}
     */
    catalogProductAttributeRepositoryV1GetListGet(opts, callback) {
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
      let returnType = CatalogDataProductAttributeSearchResultsInterface;
      return this.apiClient.callApi(
        '/V1/products/attributes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the catalogProductAttributeRepositoryV1SavePost operation.
     * @callback module:api/ProductsAttributesApi~catalogProductAttributeRepositoryV1SavePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CatalogDataProductAttributeInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/attributes
     * Save attribute data
     * @param {Object} opts Optional parameters
     * @param {module:model/CatalogProductAttributeRepositoryV1SavePostRequest} [catalogProductAttributeRepositoryV1SavePostRequest] 
     * @param {module:api/ProductsAttributesApi~catalogProductAttributeRepositoryV1SavePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CatalogDataProductAttributeInterface}
     */
    catalogProductAttributeRepositoryV1SavePost(opts, callback) {
      opts = opts || {};
      let postBody = opts['catalogProductAttributeRepositoryV1SavePostRequest'];

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
      let returnType = CatalogDataProductAttributeInterface;
      return this.apiClient.callApi(
        '/V1/products/attributes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
