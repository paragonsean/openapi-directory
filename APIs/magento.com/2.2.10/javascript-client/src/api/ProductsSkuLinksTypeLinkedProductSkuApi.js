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

/**
* ProductsSkuLinksTypeLinkedProductSku service.
* @module api/ProductsSkuLinksTypeLinkedProductSkuApi
* @version 2.2.10
*/
export default class ProductsSkuLinksTypeLinkedProductSkuApi {

    /**
    * Constructs a new ProductsSkuLinksTypeLinkedProductSkuApi. 
    * @alias module:api/ProductsSkuLinksTypeLinkedProductSkuApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the catalogProductLinkRepositoryV1DeleteByIdDelete operation.
     * @callback module:api/ProductsSkuLinksTypeLinkedProductSkuApi~catalogProductLinkRepositoryV1DeleteByIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/{sku}/links/{type}/{linkedProductSku}
     * 
     * @param {String} sku 
     * @param {String} type 
     * @param {String} linkedProductSku 
     * @param {module:api/ProductsSkuLinksTypeLinkedProductSkuApi~catalogProductLinkRepositoryV1DeleteByIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    catalogProductLinkRepositoryV1DeleteByIdDelete(sku, type, linkedProductSku, callback) {
      let postBody = null;
      // verify the required parameter 'sku' is set
      if (sku === undefined || sku === null) {
        throw new Error("Missing the required parameter 'sku' when calling catalogProductLinkRepositoryV1DeleteByIdDelete");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling catalogProductLinkRepositoryV1DeleteByIdDelete");
      }
      // verify the required parameter 'linkedProductSku' is set
      if (linkedProductSku === undefined || linkedProductSku === null) {
        throw new Error("Missing the required parameter 'linkedProductSku' when calling catalogProductLinkRepositoryV1DeleteByIdDelete");
      }

      let pathParams = {
        'sku': sku,
        'type': type,
        'linkedProductSku': linkedProductSku
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
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/V1/products/{sku}/links/{type}/{linkedProductSku}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
