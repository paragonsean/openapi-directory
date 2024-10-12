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
import DownloadableDataLinkInterface from '../model/DownloadableDataLinkInterface';
import DownloadableLinkRepositoryV1SavePostRequest from '../model/DownloadableLinkRepositoryV1SavePostRequest';
import ErrorResponse from '../model/ErrorResponse';

/**
* ProductsSkuDownloadableLinks service.
* @module api/ProductsSkuDownloadableLinksApi
* @version 2.2.10
*/
export default class ProductsSkuDownloadableLinksApi {

    /**
    * Constructs a new ProductsSkuDownloadableLinksApi. 
    * @alias module:api/ProductsSkuDownloadableLinksApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the downloadableLinkRepositoryV1GetListGet operation.
     * @callback module:api/ProductsSkuDownloadableLinksApi~downloadableLinkRepositoryV1GetListGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/DownloadableDataLinkInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/{sku}/downloadable-links
     * List of links with associated samples
     * @param {String} sku 
     * @param {module:api/ProductsSkuDownloadableLinksApi~downloadableLinkRepositoryV1GetListGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/DownloadableDataLinkInterface>}
     */
    downloadableLinkRepositoryV1GetListGet(sku, callback) {
      let postBody = null;
      // verify the required parameter 'sku' is set
      if (sku === undefined || sku === null) {
        throw new Error("Missing the required parameter 'sku' when calling downloadableLinkRepositoryV1GetListGet");
      }

      let pathParams = {
        'sku': sku
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
      let returnType = [DownloadableDataLinkInterface];
      return this.apiClient.callApi(
        '/V1/products/{sku}/downloadable-links', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the downloadableLinkRepositoryV1SavePost operation.
     * @callback module:api/ProductsSkuDownloadableLinksApi~downloadableLinkRepositoryV1SavePostCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/{sku}/downloadable-links
     * Update downloadable link of the given product (link type and its resources cannot be changed)
     * @param {String} sku 
     * @param {Object} opts Optional parameters
     * @param {module:model/DownloadableLinkRepositoryV1SavePostRequest} [downloadableLinkRepositoryV1SavePostRequest] 
     * @param {module:api/ProductsSkuDownloadableLinksApi~downloadableLinkRepositoryV1SavePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    downloadableLinkRepositoryV1SavePost(sku, opts, callback) {
      opts = opts || {};
      let postBody = opts['downloadableLinkRepositoryV1SavePostRequest'];
      // verify the required parameter 'sku' is set
      if (sku === undefined || sku === null) {
        throw new Error("Missing the required parameter 'sku' when calling downloadableLinkRepositoryV1SavePost");
      }

      let pathParams = {
        'sku': sku
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
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/V1/products/{sku}/downloadable-links', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
