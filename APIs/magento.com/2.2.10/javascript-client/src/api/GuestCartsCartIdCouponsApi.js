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
* GuestCartsCartIdCoupons service.
* @module api/GuestCartsCartIdCouponsApi
* @version 2.2.10
*/
export default class GuestCartsCartIdCouponsApi {

    /**
    * Constructs a new GuestCartsCartIdCouponsApi. 
    * @alias module:api/GuestCartsCartIdCouponsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the quoteGuestCouponManagementV1GetGet operation.
     * @callback module:api/GuestCartsCartIdCouponsApi~quoteGuestCouponManagementV1GetGetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * guest-carts/{cartId}/coupons
     * Return information for a coupon in a specified cart.
     * @param {String} cartId The cart ID.
     * @param {module:api/GuestCartsCartIdCouponsApi~quoteGuestCouponManagementV1GetGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    quoteGuestCouponManagementV1GetGet(cartId, callback) {
      let postBody = null;
      // verify the required parameter 'cartId' is set
      if (cartId === undefined || cartId === null) {
        throw new Error("Missing the required parameter 'cartId' when calling quoteGuestCouponManagementV1GetGet");
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
      let returnType = 'String';
      return this.apiClient.callApi(
        '/V1/guest-carts/{cartId}/coupons', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the quoteGuestCouponManagementV1RemoveDelete operation.
     * @callback module:api/GuestCartsCartIdCouponsApi~quoteGuestCouponManagementV1RemoveDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * guest-carts/{cartId}/coupons
     * Delete a coupon from a specified cart.
     * @param {String} cartId The cart ID.
     * @param {module:api/GuestCartsCartIdCouponsApi~quoteGuestCouponManagementV1RemoveDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    quoteGuestCouponManagementV1RemoveDelete(cartId, callback) {
      let postBody = null;
      // verify the required parameter 'cartId' is set
      if (cartId === undefined || cartId === null) {
        throw new Error("Missing the required parameter 'cartId' when calling quoteGuestCouponManagementV1RemoveDelete");
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
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/V1/guest-carts/{cartId}/coupons', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
