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
import QuoteDataShippingMethodInterface from '../model/QuoteDataShippingMethodInterface';
import QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest from '../model/QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest';

/**
* NegotiableCartsCartIdEstimateShippingMethods service.
* @module api/NegotiableCartsCartIdEstimateShippingMethodsApi
* @version 2.2.10
*/
export default class NegotiableCartsCartIdEstimateShippingMethodsApi {

    /**
    * Constructs a new NegotiableCartsCartIdEstimateShippingMethodsApi. 
    * @alias module:api/NegotiableCartsCartIdEstimateShippingMethodsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost operation.
     * @callback module:api/NegotiableCartsCartIdEstimateShippingMethodsApi~negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPostCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/QuoteDataShippingMethodInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * negotiable-carts/{cartId}/estimate-shipping-methods
     * Estimate shipping by address and return list of available shipping methods
     * @param {String} cartId 
     * @param {Object} opts Optional parameters
     * @param {module:model/QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest} [quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest] 
     * @param {module:api/NegotiableCartsCartIdEstimateShippingMethodsApi~negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/QuoteDataShippingMethodInterface>}
     */
    negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost(cartId, opts, callback) {
      opts = opts || {};
      let postBody = opts['quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest'];
      // verify the required parameter 'cartId' is set
      if (cartId === undefined || cartId === null) {
        throw new Error("Missing the required parameter 'cartId' when calling negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost");
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
      let returnType = [QuoteDataShippingMethodInterface];
      return this.apiClient.callApi(
        '/V1/negotiable-carts/{cartId}/estimate-shipping-methods', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
