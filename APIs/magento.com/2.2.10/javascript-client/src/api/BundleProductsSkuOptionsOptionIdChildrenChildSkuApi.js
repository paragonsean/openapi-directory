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
* BundleProductsSkuOptionsOptionIdChildrenChildSku service.
* @module api/BundleProductsSkuOptionsOptionIdChildrenChildSkuApi
* @version 2.2.10
*/
export default class BundleProductsSkuOptionsOptionIdChildrenChildSkuApi {

    /**
    * Constructs a new BundleProductsSkuOptionsOptionIdChildrenChildSkuApi. 
    * @alias module:api/BundleProductsSkuOptionsOptionIdChildrenChildSkuApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the bundleProductLinkManagementV1RemoveChildDelete operation.
     * @callback module:api/BundleProductsSkuOptionsOptionIdChildrenChildSkuApi~bundleProductLinkManagementV1RemoveChildDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * bundle-products/{sku}/options/{optionId}/children/{childSku}
     * Remove product from Bundle product option
     * @param {String} sku 
     * @param {Number} optionId 
     * @param {String} childSku 
     * @param {module:api/BundleProductsSkuOptionsOptionIdChildrenChildSkuApi~bundleProductLinkManagementV1RemoveChildDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    bundleProductLinkManagementV1RemoveChildDelete(sku, optionId, childSku, callback) {
      let postBody = null;
      // verify the required parameter 'sku' is set
      if (sku === undefined || sku === null) {
        throw new Error("Missing the required parameter 'sku' when calling bundleProductLinkManagementV1RemoveChildDelete");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling bundleProductLinkManagementV1RemoveChildDelete");
      }
      // verify the required parameter 'childSku' is set
      if (childSku === undefined || childSku === null) {
        throw new Error("Missing the required parameter 'childSku' when calling bundleProductLinkManagementV1RemoveChildDelete");
      }

      let pathParams = {
        'sku': sku,
        'optionId': optionId,
        'childSku': childSku
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
        '/V1/bundle-products/{sku}/options/{optionId}/children/{childSku}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
