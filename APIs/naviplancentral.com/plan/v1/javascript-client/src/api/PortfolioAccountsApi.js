/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
import PortfolioAccountModel from '../model/PortfolioAccountModel';
import PortfolioAccountsModel from '../model/PortfolioAccountsModel';

/**
* PortfolioAccounts service.
* @module api/PortfolioAccountsApi
* @version v1
*/
export default class PortfolioAccountsApi {

    /**
    * Constructs a new PortfolioAccountsApi. 
    * @alias module:api/PortfolioAccountsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the portfolioAccountsGetByIdPlanid operation.
     * @callback module:api/PortfolioAccountsApi~portfolioAccountsGetByIdPlanidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PortfolioAccountModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a portfolio account
     * This operation retrieves a portfolio account from the plan.
     * @param {Number} id ID of portfolio account to retrieve
     * @param {String} planId Id of the plan to retrieve data from (e.g. 1001-11-3).
     * @param {module:api/PortfolioAccountsApi~portfolioAccountsGetByIdPlanidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PortfolioAccountModel}
     */
    portfolioAccountsGetByIdPlanid(id, planId, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling portfolioAccountsGetByIdPlanid");
      }
      // verify the required parameter 'planId' is set
      if (planId === undefined || planId === null) {
        throw new Error("Missing the required parameter 'planId' when calling portfolioAccountsGetByIdPlanid");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'planId': planId
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = PortfolioAccountModel;
      return this.apiClient.callApi(
        '/api/PortfolioAccounts/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the portfolioAccountsGetByPlanid operation.
     * @callback module:api/PortfolioAccountsApi~portfolioAccountsGetByPlanidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PortfolioAccountsModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve portfolio accounts
     * This operation retrieves a list of all of the portfolio accounts in the plan.
     * @param {String} planId Id of the plan to retrieve data from (e.g. 1001-11-3).
     * @param {module:api/PortfolioAccountsApi~portfolioAccountsGetByPlanidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PortfolioAccountsModel}
     */
    portfolioAccountsGetByPlanid(planId, callback) {
      let postBody = null;
      // verify the required parameter 'planId' is set
      if (planId === undefined || planId === null) {
        throw new Error("Missing the required parameter 'planId' when calling portfolioAccountsGetByPlanid");
      }

      let pathParams = {
      };
      let queryParams = {
        'planId': planId
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = PortfolioAccountsModel;
      return this.apiClient.callApi(
        '/api/PortfolioAccounts', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
