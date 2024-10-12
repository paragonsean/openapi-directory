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
import CatalogDataProductInterface from '../model/CatalogDataProductInterface';
import ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest from '../model/ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest';
import ErrorResponse from '../model/ErrorResponse';

/**
* ConfigurableProductsVariation service.
* @module api/ConfigurableProductsVariationApi
* @version 2.2.10
*/
export default class ConfigurableProductsVariationApi {

    /**
    * Constructs a new ConfigurableProductsVariationApi. 
    * @alias module:api/ConfigurableProductsVariationApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the configurableProductConfigurableProductManagementV1GenerateVariationPut operation.
     * @callback module:api/ConfigurableProductsVariationApi~configurableProductConfigurableProductManagementV1GenerateVariationPutCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/CatalogDataProductInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * configurable-products/variation
     * Generate variation based on same product
     * @param {Object} opts Optional parameters
     * @param {module:model/ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest} [configurableProductConfigurableProductManagementV1GenerateVariationPutRequest] 
     * @param {module:api/ConfigurableProductsVariationApi~configurableProductConfigurableProductManagementV1GenerateVariationPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/CatalogDataProductInterface>}
     */
    configurableProductConfigurableProductManagementV1GenerateVariationPut(opts, callback) {
      opts = opts || {};
      let postBody = opts['configurableProductConfigurableProductManagementV1GenerateVariationPutRequest'];

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
      let returnType = [CatalogDataProductInterface];
      return this.apiClient.callApi(
        '/V1/configurable-products/variation', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
