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
import HoldingCompaniesModel from '../model/HoldingCompaniesModel';
import HoldingCompanyModel from '../model/HoldingCompanyModel';

/**
* HoldingCompanies service.
* @module api/HoldingCompaniesApi
* @version v1
*/
export default class HoldingCompaniesApi {

    /**
    * Constructs a new HoldingCompaniesApi. 
    * @alias module:api/HoldingCompaniesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the holdingCompaniesGetByIdPlanid operation.
     * @callback module:api/HoldingCompaniesApi~holdingCompaniesGetByIdPlanidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/HoldingCompanyModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a holding company
     * This operation retrieves a holding company from the plan.
     * @param {Number} id ID of holding company to retrieve
     * @param {String} planId Id of the plan to retrieve data from (e.g. 1001-11-3).
     * @param {module:api/HoldingCompaniesApi~holdingCompaniesGetByIdPlanidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/HoldingCompanyModel}
     */
    holdingCompaniesGetByIdPlanid(id, planId, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling holdingCompaniesGetByIdPlanid");
      }
      // verify the required parameter 'planId' is set
      if (planId === undefined || planId === null) {
        throw new Error("Missing the required parameter 'planId' when calling holdingCompaniesGetByIdPlanid");
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
      let returnType = HoldingCompanyModel;
      return this.apiClient.callApi(
        '/api/HoldingCompanies/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the holdingCompaniesGetByPlanid operation.
     * @callback module:api/HoldingCompaniesApi~holdingCompaniesGetByPlanidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/HoldingCompaniesModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve holding companies
     * This operation retrieves a list of all of the holding companies in the plan.
     * @param {String} planId Id of the plan to retrieve data from (e.g. 1001-11-3).
     * @param {module:api/HoldingCompaniesApi~holdingCompaniesGetByPlanidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/HoldingCompaniesModel}
     */
    holdingCompaniesGetByPlanid(planId, callback) {
      let postBody = null;
      // verify the required parameter 'planId' is set
      if (planId === undefined || planId === null) {
        throw new Error("Missing the required parameter 'planId' when calling holdingCompaniesGetByPlanid");
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
      let returnType = HoldingCompaniesModel;
      return this.apiClient.callApi(
        '/api/HoldingCompanies', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
