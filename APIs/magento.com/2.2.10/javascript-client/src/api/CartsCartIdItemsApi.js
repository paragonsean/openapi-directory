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
import QuoteDataCartItemInterface from '../model/QuoteDataCartItemInterface';

/**
* CartsCartIdItems service.
* @module api/CartsCartIdItemsApi
* @version 2.2.10
*/
export default class CartsCartIdItemsApi {

    /**
    * Constructs a new CartsCartIdItemsApi. 
    * @alias module:api/CartsCartIdItemsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v1CartsCartIdItemsGet operation.
     * @callback module:api/CartsCartIdItemsApi~v1CartsCartIdItemsGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/QuoteDataCartItemInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * carts/{cartId}/items
     * Lists items that are assigned to a specified cart.
     * @param {Number} cartId The cart ID.
     * @param {module:api/CartsCartIdItemsApi~v1CartsCartIdItemsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/QuoteDataCartItemInterface>}
     */
    v1CartsCartIdItemsGet(cartId, callback) {
      let postBody = null;
      // verify the required parameter 'cartId' is set
      if (cartId === undefined || cartId === null) {
        throw new Error("Missing the required parameter 'cartId' when calling v1CartsCartIdItemsGet");
      }

      let pathParams = {
        'cartId': cartId
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
      let returnType = [QuoteDataCartItemInterface];
      return this.apiClient.callApi(
        '/V1/carts/{cartId}/items', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
