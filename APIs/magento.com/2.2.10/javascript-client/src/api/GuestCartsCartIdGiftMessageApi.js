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
import GiftMessageCartRepositoryV1SavePostRequest from '../model/GiftMessageCartRepositoryV1SavePostRequest';
import GiftMessageDataMessageInterface from '../model/GiftMessageDataMessageInterface';

/**
* GuestCartsCartIdGiftMessage service.
* @module api/GuestCartsCartIdGiftMessageApi
* @version 2.2.10
*/
export default class GuestCartsCartIdGiftMessageApi {

    /**
    * Constructs a new GuestCartsCartIdGiftMessageApi. 
    * @alias module:api/GuestCartsCartIdGiftMessageApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the giftMessageGuestCartRepositoryV1GetGet operation.
     * @callback module:api/GuestCartsCartIdGiftMessageApi~giftMessageGuestCartRepositoryV1GetGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GiftMessageDataMessageInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * guest-carts/{cartId}/gift-message
     * Return the gift message for a specified order.
     * @param {String} cartId The shopping cart ID.
     * @param {module:api/GuestCartsCartIdGiftMessageApi~giftMessageGuestCartRepositoryV1GetGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GiftMessageDataMessageInterface}
     */
    giftMessageGuestCartRepositoryV1GetGet(cartId, callback) {
      let postBody = null;
      // verify the required parameter 'cartId' is set
      if (cartId === undefined || cartId === null) {
        throw new Error("Missing the required parameter 'cartId' when calling giftMessageGuestCartRepositoryV1GetGet");
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
      let returnType = GiftMessageDataMessageInterface;
      return this.apiClient.callApi(
        '/V1/guest-carts/{cartId}/gift-message', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the giftMessageGuestCartRepositoryV1SavePost operation.
     * @callback module:api/GuestCartsCartIdGiftMessageApi~giftMessageGuestCartRepositoryV1SavePostCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * guest-carts/{cartId}/gift-message
     * Set the gift message for an entire order.
     * @param {String} cartId The cart ID.
     * @param {Object} opts Optional parameters
     * @param {module:model/GiftMessageCartRepositoryV1SavePostRequest} [giftMessageCartRepositoryV1SavePostRequest] 
     * @param {module:api/GuestCartsCartIdGiftMessageApi~giftMessageGuestCartRepositoryV1SavePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    giftMessageGuestCartRepositoryV1SavePost(cartId, opts, callback) {
      opts = opts || {};
      let postBody = opts['giftMessageCartRepositoryV1SavePostRequest'];
      // verify the required parameter 'cartId' is set
      if (cartId === undefined || cartId === null) {
        throw new Error("Missing the required parameter 'cartId' when calling giftMessageGuestCartRepositoryV1SavePost");
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
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/V1/guest-carts/{cartId}/gift-message', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
