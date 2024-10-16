/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
import ExpenseTypeModel from '../model/ExpenseTypeModel';
import ExpenseTypesModel from '../model/ExpenseTypesModel';

/**
* ExpenseTypes service.
* @module api/ExpenseTypesApi
* @version v1
*/
export default class ExpenseTypesApi {

    /**
    * Constructs a new ExpenseTypesApi. 
    * @alias module:api/ExpenseTypesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the expenseTypesGetByCountry operation.
     * @callback module:api/ExpenseTypesApi~expenseTypesGetByCountryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseTypesModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Description: This operation retrieves all Expense Types for the specified country.<br />                Purpose: Provides access to the Expense Types including id and type description.
     * @param {module:model/String} country The country used to filter Expense Types
     * @param {module:api/ExpenseTypesApi~expenseTypesGetByCountryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseTypesModel}
     */
    expenseTypesGetByCountry(country, callback) {
      let postBody = null;
      // verify the required parameter 'country' is set
      if (country === undefined || country === null) {
        throw new Error("Missing the required parameter 'country' when calling expenseTypesGetByCountry");
      }

      let pathParams = {
      };
      let queryParams = {
        'country': country
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = ExpenseTypesModel;
      return this.apiClient.callApi(
        '/api/ExpenseTypes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expenseTypesGetById operation.
     * @callback module:api/ExpenseTypesApi~expenseTypesGetByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseTypeModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Description: This operation retrieves all Expense Types for the specified country.<br />                Purpose: Provides access to the Expense Types including id and type description.
     * @param {Number} id The ID of Expense Type used to retreive the Expense Type information
     * @param {module:api/ExpenseTypesApi~expenseTypesGetByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseTypeModel}
     */
    expenseTypesGetById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling expenseTypesGetById");
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
      let returnType = ExpenseTypeModel;
      return this.apiClient.callApi(
        '/api/ExpenseTypes/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
