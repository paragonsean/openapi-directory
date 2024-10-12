/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
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
import GetTransactionResponse from '../model/GetTransactionResponse';
import ListTransactionsResponse from '../model/ListTransactionsResponse';
import TransactionStatusEnum from '../model/TransactionStatusEnum';

/**
* Transactions service.
* @module api/TransactionsApi
* @version v1
*/
export default class TransactionsApi {

    /**
    * Constructs a new TransactionsApi. 
    * @alias module:api/TransactionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the accountsAccountIdTransactionsGet operation.
     * @callback module:api/TransactionsApi~accountsAccountIdTransactionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListTransactionsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List transactions by account
     * Retrieve a list of all transactions for a specific account. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. To narrow the results to a specific date range pass one or both of `filter[since]` and `filter[until]` in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 
     * @param {String} accountId The unique identifier for the account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [pageSize] The number of records to return in each page. 
     * @param {module:model/TransactionStatusEnum} [filterStatus] The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`. 
     * @param {Date} [filterSince] The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
     * @param {Date} [filterUntil] The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
     * @param {String} [filterCategory] The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response. 
     * @param {String} [filterTag] A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
     * @param {module:api/TransactionsApi~accountsAccountIdTransactionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListTransactionsResponse}
     */
    accountsAccountIdTransactionsGet(accountId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accountId' is set
      if (accountId === undefined || accountId === null) {
        throw new Error("Missing the required parameter 'accountId' when calling accountsAccountIdTransactionsGet");
      }

      let pathParams = {
        'accountId': accountId
      };
      let queryParams = {
        'page[size]': opts['pageSize'],
        'filter[status]': opts['filterStatus'],
        'filter[since]': opts['filterSince'],
        'filter[until]': opts['filterUntil'],
        'filter[category]': opts['filterCategory'],
        'filter[tag]': opts['filterTag']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearer_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListTransactionsResponse;
      return this.apiClient.callApi(
        '/accounts/{accountId}/transactions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the transactionsGet operation.
     * @callback module:api/TransactionsApi~transactionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListTransactionsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List transactions
     * Retrieve a list of all transactions across all accounts for the currently authenticated user. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. To narrow the results to a specific date range pass one or both of `filter[since]` and `filter[until]` in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 
     * @param {Object} opts Optional parameters
     * @param {Number} [pageSize] The number of records to return in each page. 
     * @param {module:model/TransactionStatusEnum} [filterStatus] The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`. 
     * @param {Date} [filterSince] The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
     * @param {Date} [filterUntil] The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
     * @param {String} [filterCategory] The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response. 
     * @param {String} [filterTag] A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
     * @param {module:api/TransactionsApi~transactionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListTransactionsResponse}
     */
    transactionsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page[size]': opts['pageSize'],
        'filter[status]': opts['filterStatus'],
        'filter[since]': opts['filterSince'],
        'filter[until]': opts['filterUntil'],
        'filter[category]': opts['filterCategory'],
        'filter[tag]': opts['filterTag']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearer_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListTransactionsResponse;
      return this.apiClient.callApi(
        '/transactions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the transactionsIdGet operation.
     * @callback module:api/TransactionsApi~transactionsIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetTransactionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve transaction
     * Retrieve a specific transaction by providing its unique identifier. 
     * @param {String} id The unique identifier for the transaction. 
     * @param {module:api/TransactionsApi~transactionsIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetTransactionResponse}
     */
    transactionsIdGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling transactionsIdGet");
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

      let authNames = ['bearer_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetTransactionResponse;
      return this.apiClient.callApi(
        '/transactions/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
