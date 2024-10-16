/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import PayeeBankAccounts from '../model/PayeeBankAccounts';

/**
* PayeeBankAccounts service.
* @module api/PayeeBankAccountsApi
* @version 1.0
*/
export default class PayeeBankAccountsApi {

    /**
    * Constructs a new PayeeBankAccountsApi. 
    * @alias module:api/PayeeBankAccountsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getPayees operation.
     * @callback module:api/PayeeBankAccountsApi~getPayeesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PayeeBankAccounts} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all Payee Bank Accounts
     * Returns all your payee bank accounts.   Ordered by payee name ascending.   Can be paginated. 
     * @param {module:api/PayeeBankAccountsApi~getPayeesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PayeeBankAccounts}
     */
    getPayees(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PayeeBankAccounts;
      return this.apiClient.callApi(
        '/v1/payees', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
