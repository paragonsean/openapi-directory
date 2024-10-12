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
* CartsMineBalanceUnapply service.
* @module api/CartsMineBalanceUnapplyApi
* @version 2.2.10
*/
export default class CartsMineBalanceUnapplyApi {

    /**
    * Constructs a new CartsMineBalanceUnapplyApi. 
    * @alias module:api/CartsMineBalanceUnapplyApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the customerBalanceBalanceManagementFromQuoteV1UnapplyPost operation.
     * @callback module:api/CartsMineBalanceUnapplyApi~customerBalanceBalanceManagementFromQuoteV1UnapplyPostCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * carts/mine/balance/unapply
     * Unapply store credit.
     * @param {module:api/CartsMineBalanceUnapplyApi~customerBalanceBalanceManagementFromQuoteV1UnapplyPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    customerBalanceBalanceManagementFromQuoteV1UnapplyPost(callback) {
      let postBody = null;

      let pathParams = {
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
        '/V1/carts/mine/balance/unapply', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
