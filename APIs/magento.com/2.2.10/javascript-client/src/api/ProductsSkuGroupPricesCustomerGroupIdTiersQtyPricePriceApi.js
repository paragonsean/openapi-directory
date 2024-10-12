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
* ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePrice service.
* @module api/ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi
* @version 2.2.10
*/
export default class ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi {

    /**
    * Constructs a new ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi. 
    * @alias module:api/ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the catalogProductTierPriceManagementV1AddPost operation.
     * @callback module:api/ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi~catalogProductTierPriceManagementV1AddPostCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price}
     * Create tier price for product
     * @param {String} sku 
     * @param {String} customerGroupId 'all' can be used to specify 'ALL GROUPS'
     * @param {Number} price 
     * @param {Number} qty 
     * @param {module:api/ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi~catalogProductTierPriceManagementV1AddPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    catalogProductTierPriceManagementV1AddPost(sku, customerGroupId, price, qty, callback) {
      let postBody = null;
      // verify the required parameter 'sku' is set
      if (sku === undefined || sku === null) {
        throw new Error("Missing the required parameter 'sku' when calling catalogProductTierPriceManagementV1AddPost");
      }
      // verify the required parameter 'customerGroupId' is set
      if (customerGroupId === undefined || customerGroupId === null) {
        throw new Error("Missing the required parameter 'customerGroupId' when calling catalogProductTierPriceManagementV1AddPost");
      }
      // verify the required parameter 'price' is set
      if (price === undefined || price === null) {
        throw new Error("Missing the required parameter 'price' when calling catalogProductTierPriceManagementV1AddPost");
      }
      // verify the required parameter 'qty' is set
      if (qty === undefined || qty === null) {
        throw new Error("Missing the required parameter 'qty' when calling catalogProductTierPriceManagementV1AddPost");
      }

      let pathParams = {
        'sku': sku,
        'customerGroupId': customerGroupId,
        'price': price,
        'qty': qty
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
        '/V1/products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
