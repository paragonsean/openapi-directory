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
import CatalogCostStorageV1UpdatePostRequest from '../model/CatalogCostStorageV1UpdatePostRequest';
import CatalogDataPriceUpdateResultInterface from '../model/CatalogDataPriceUpdateResultInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* ProductsCost service.
* @module api/ProductsCostApi
* @version 2.2.10
*/
export default class ProductsCostApi {

    /**
    * Constructs a new ProductsCostApi. 
    * @alias module:api/ProductsCostApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the catalogCostStorageV1UpdatePost operation.
     * @callback module:api/ProductsCostApi~catalogCostStorageV1UpdatePostCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/CatalogDataPriceUpdateResultInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/cost
     * Add or update product cost. Input item should correspond to \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid cost, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.
     * @param {Object} opts Optional parameters
     * @param {module:model/CatalogCostStorageV1UpdatePostRequest} [catalogCostStorageV1UpdatePostRequest] 
     * @param {module:api/ProductsCostApi~catalogCostStorageV1UpdatePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/CatalogDataPriceUpdateResultInterface>}
     */
    catalogCostStorageV1UpdatePost(opts, callback) {
      opts = opts || {};
      let postBody = opts['catalogCostStorageV1UpdatePostRequest'];

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
      let returnType = [CatalogDataPriceUpdateResultInterface];
      return this.apiClient.callApi(
        '/V1/products/cost', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
