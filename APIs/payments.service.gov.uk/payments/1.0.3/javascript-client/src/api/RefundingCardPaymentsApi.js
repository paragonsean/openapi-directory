/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import PaymentError from '../model/PaymentError';
import PaymentRefundRequest from '../model/PaymentRefundRequest';
import Refund from '../model/Refund';
import RefundError from '../model/RefundError';
import RefundForSearchResult from '../model/RefundForSearchResult';
import RefundSearchResults from '../model/RefundSearchResults';

/**
* RefundingCardPayments service.
* @module api/RefundingCardPaymentsApi
* @version 1.0.3
*/
export default class RefundingCardPaymentsApi {

    /**
    * Constructs a new RefundingCardPaymentsApi. 
    * @alias module:api/RefundingCardPaymentsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getAPaymentRefund operation.
     * @callback module:api/RefundingCardPaymentsApi~getAPaymentRefundCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Refund} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find payment refund by ID
     * Return payment refund information by Refund ID The Authorisation token needs to be specified in the 'authorization' header as 'authorization: Bearer YOUR_API_KEY_HERE'
     * @param {String} paymentId 
     * @param {String} refundId 
     * @param {module:api/RefundingCardPaymentsApi~getAPaymentRefundCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Refund}
     */
    getAPaymentRefund(paymentId, refundId, callback) {
      let postBody = null;
      // verify the required parameter 'paymentId' is set
      if (paymentId === undefined || paymentId === null) {
        throw new Error("Missing the required parameter 'paymentId' when calling getAPaymentRefund");
      }
      // verify the required parameter 'refundId' is set
      if (refundId === undefined || refundId === null) {
        throw new Error("Missing the required parameter 'refundId' when calling getAPaymentRefund");
      }

      let pathParams = {
        'paymentId': paymentId,
        'refundId': refundId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Authorization'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Refund;
      return this.apiClient.callApi(
        '/v1/payments/{paymentId}/refunds/{refundId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllRefundsForAPayment operation.
     * @callback module:api/RefundingCardPaymentsApi~getAllRefundsForAPaymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RefundForSearchResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all refunds for a payment
     * Return refunds for a payment. The Authorisation token needs to be specified in the 'authorization' header as 'authorization: Bearer YOUR_API_KEY_HERE'
     * @param {String} paymentId 
     * @param {module:api/RefundingCardPaymentsApi~getAllRefundsForAPaymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RefundForSearchResult}
     */
    getAllRefundsForAPayment(paymentId, callback) {
      let postBody = null;
      // verify the required parameter 'paymentId' is set
      if (paymentId === undefined || paymentId === null) {
        throw new Error("Missing the required parameter 'paymentId' when calling getAllRefundsForAPayment");
      }

      let pathParams = {
        'paymentId': paymentId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Authorization'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = RefundForSearchResult;
      return this.apiClient.callApi(
        '/v1/payments/{paymentId}/refunds', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the searchRefunds operation.
     * @callback module:api/RefundingCardPaymentsApi~searchRefundsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RefundSearchResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search refunds
     * Search refunds by 'from' and 'to' date. The Authorisation token needs to be specified in the 'authorization' header as 'authorization: Bearer YOUR_API_KEY_HERE'
     * @param {Object} opts Optional parameters
     * @param {String} [fromDate] From date of refunds to be searched (this date is inclusive). Example=2015-08-13T12:35:00Z
     * @param {String} [toDate] To date of refunds to be searched (this date is exclusive). Example=2015-08-14T12:35:00Z
     * @param {String} [fromSettledDate] From settled date of refund to be searched (this date is inclusive). Example=2015-08-13
     * @param {String} [toSettledDate] To settled date of refund to be searched (this date is inclusive). Example=2015-08-13
     * @param {String} [page] Page number requested for the search, should be a positive integer (optional, defaults to 1)
     * @param {String} [displaySize] Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500)
     * @param {module:api/RefundingCardPaymentsApi~searchRefundsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RefundSearchResults}
     */
    searchRefunds(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'from_date': opts['fromDate'],
        'to_date': opts['toDate'],
        'from_settled_date': opts['fromSettledDate'],
        'to_settled_date': opts['toSettledDate'],
        'page': opts['page'],
        'display_size': opts['displaySize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Authorization'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = RefundSearchResults;
      return this.apiClient.callApi(
        '/v1/refunds', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the submitARefundForAPayment operation.
     * @callback module:api/RefundingCardPaymentsApi~submitARefundForAPaymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Refund} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Submit a refund for a payment
     * Return issued refund information. The Authorisation token needs to be specified in the 'authorization' header as 'authorization: Bearer YOUR_API_KEY_HERE'
     * @param {String} paymentId paymentId
     * @param {module:model/PaymentRefundRequest} body requestPayload
     * @param {module:api/RefundingCardPaymentsApi~submitARefundForAPaymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Refund}
     */
    submitARefundForAPayment(paymentId, body, callback) {
      let postBody = body;
      // verify the required parameter 'paymentId' is set
      if (paymentId === undefined || paymentId === null) {
        throw new Error("Missing the required parameter 'paymentId' when calling submitARefundForAPayment");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling submitARefundForAPayment");
      }

      let pathParams = {
        'paymentId': paymentId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Authorization'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Refund;
      return this.apiClient.callApi(
        '/v1/payments/{paymentId}/refunds', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
