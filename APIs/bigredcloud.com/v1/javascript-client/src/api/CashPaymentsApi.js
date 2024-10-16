/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import BatchItemCashPaymentDto from '../model/BatchItemCashPaymentDto';
import CashPaymentDto from '../model/CashPaymentDto';
import PageResultCashPaymentQueryDto from '../model/PageResultCashPaymentQueryDto';

/**
* CashPayments service.
* @module api/CashPaymentsApi
* @version v1
*/
export default class CashPaymentsApi {

    /**
    * Constructs a new CashPaymentsApi. 
    * @alias module:api/CashPaymentsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the cashPaymentsDelete operation.
     * @callback module:api/CashPaymentsApi~cashPaymentsDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes an existing Cash Payment.
     * @param {Number} id Id of Cash Receipt to remove.
     * @param {String} timestamp Timestamp of Cash Receipt to remove. Should be encoded in Base64.
     * @param {module:api/CashPaymentsApi~cashPaymentsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cashPaymentsDelete(id, timestamp, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling cashPaymentsDelete");
      }
      // verify the required parameter 'timestamp' is set
      if (timestamp === undefined || timestamp === null) {
        throw new Error("Missing the required parameter 'timestamp' when calling cashPaymentsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'timestamp': timestamp
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v1/cashPayments/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cashPaymentsGet operation.
     * @callback module:api/CashPaymentsApi~cashPaymentsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PageResultCashPaymentQueryDto} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a list of company's Cash Payments. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
     * @param {module:api/CashPaymentsApi~cashPaymentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PageResultCashPaymentQueryDto}
     */
    cashPaymentsGet(callback) {
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
      let accepts = ['application/json'];
      let returnType = PageResultCashPaymentQueryDto;
      return this.apiClient.callApi(
        '/v1/cashPayments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cashPaymentsPost operation.
     * @callback module:api/CashPaymentsApi~cashPaymentsPostCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new Cash Payment.
     * @param {module:model/CashPaymentDto} cashPaymentDto Information of Cash Receipt to create.
     * @param {module:api/CashPaymentsApi~cashPaymentsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cashPaymentsPost(cashPaymentDto, callback) {
      let postBody = cashPaymentDto;
      // verify the required parameter 'cashPaymentDto' is set
      if (cashPaymentDto === undefined || cashPaymentDto === null) {
        throw new Error("Missing the required parameter 'cashPaymentDto' when calling cashPaymentsPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v1/cashPayments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cashPaymentsProcessBatch operation.
     * @callback module:api/CashPaymentsApi~cashPaymentsProcessBatchCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Processes a batch of Cash Payments.
     * @param {Array.<module:model/BatchItemCashPaymentDto>} batchItemCashPaymentDto Batch of Cash Receipts to process.
     * @param {module:api/CashPaymentsApi~cashPaymentsProcessBatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cashPaymentsProcessBatch(batchItemCashPaymentDto, callback) {
      let postBody = batchItemCashPaymentDto;
      // verify the required parameter 'batchItemCashPaymentDto' is set
      if (batchItemCashPaymentDto === undefined || batchItemCashPaymentDto === null) {
        throw new Error("Missing the required parameter 'batchItemCashPaymentDto' when calling cashPaymentsProcessBatch");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v1/cashPayments/batch', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cashPaymentsPut operation.
     * @callback module:api/CashPaymentsApi~cashPaymentsPutCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates an existing Cash Payment.
     * @param {Number} id Id of Cash Receipt to update.
     * @param {module:model/CashPaymentDto} cashPaymentDto Information of Cash Receipt to update.
     * @param {module:api/CashPaymentsApi~cashPaymentsPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cashPaymentsPut(id, cashPaymentDto, callback) {
      let postBody = cashPaymentDto;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling cashPaymentsPut");
      }
      // verify the required parameter 'cashPaymentDto' is set
      if (cashPaymentDto === undefined || cashPaymentDto === null) {
        throw new Error("Missing the required parameter 'cashPaymentDto' when calling cashPaymentsPut");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v1/cashPayments/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v1CashPaymentsIdGet operation.
     * @callback module:api/CashPaymentsApi~v1CashPaymentsIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CashPaymentDto} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about a single Cash Payment.
     * @param {Number} id Id of Cash Receipt to return.
     * @param {module:api/CashPaymentsApi~v1CashPaymentsIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CashPaymentDto}
     */
    v1CashPaymentsIdGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling v1CashPaymentsIdGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CashPaymentDto;
      return this.apiClient.callApi(
        '/v1/cashPayments/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
