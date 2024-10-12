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
import AdvisorModel from '../model/AdvisorModel';
import AdvisorsModel from '../model/AdvisorsModel';

/**
* Advisors service.
* @module api/AdvisorsApi
* @version v1
*/
export default class AdvisorsApi {

    /**
    * Constructs a new AdvisorsApi. 
    * @alias module:api/AdvisorsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the advisorsGet operation.
     * @callback module:api/AdvisorsApi~advisorsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AdvisorsModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve Advisors
     * This operation retrieves a list of all of the Advisors in the plan.
     * @param {module:api/AdvisorsApi~advisorsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AdvisorsModel}
     */
    advisorsGet(callback) {
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
      let accepts = ['application/json', 'text/json'];
      let returnType = AdvisorsModel;
      return this.apiClient.callApi(
        '/api/Advisors', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the advisorsGetByHouseholdidClientid operation.
     * @callback module:api/AdvisorsApi~advisorsGetByHouseholdidClientidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AdvisorsModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve Advisors for a Client
     * This operation retrieves a list of all of the Advisors for the client.
     * @param {Number} householdId Integer id of the household
     * @param {String} clientId Guid id of the client.
     * @param {module:api/AdvisorsApi~advisorsGetByHouseholdidClientidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AdvisorsModel}
     */
    advisorsGetByHouseholdidClientid(householdId, clientId, callback) {
      let postBody = null;
      // verify the required parameter 'householdId' is set
      if (householdId === undefined || householdId === null) {
        throw new Error("Missing the required parameter 'householdId' when calling advisorsGetByHouseholdidClientid");
      }
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling advisorsGetByHouseholdidClientid");
      }

      let pathParams = {
        'householdId': householdId,
        'clientId': clientId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = AdvisorsModel;
      return this.apiClient.callApi(
        '/api/Advisors/{householdId}/{clientId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the advisorsGetById operation.
     * @callback module:api/AdvisorsApi~advisorsGetByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AdvisorModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an Advisor
     * This operation retrieves an Advisor from the plan.
     * @param {String} id Guid id of the advisor
     * @param {module:api/AdvisorsApi~advisorsGetByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AdvisorModel}
     */
    advisorsGetById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling advisorsGetById");
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
      let accepts = ['application/json', 'text/json'];
      let returnType = AdvisorModel;
      return this.apiClient.callApi(
        '/api/Advisors/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
