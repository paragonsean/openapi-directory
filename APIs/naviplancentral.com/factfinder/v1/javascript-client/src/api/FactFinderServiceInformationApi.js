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
import ServiceInformationModel from '../model/ServiceInformationModel';

/**
* FactFinderServiceInformation service.
* @module api/FactFinderServiceInformationApi
* @version v1
*/
export default class FactFinderServiceInformationApi {

    /**
    * Constructs a new FactFinderServiceInformationApi. 
    * @alias module:api/FactFinderServiceInformationApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the factFinderServiceInformationGet operation.
     * @callback module:api/FactFinderServiceInformationApi~factFinderServiceInformationGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceInformationModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Description: This operation retrieves information statistics for the current service.<br />                Purpose: Provides access to Service Information.
     * @param {module:api/FactFinderServiceInformationApi~factFinderServiceInformationGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceInformationModel}
     */
    factFinderServiceInformationGet(callback) {
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
      let returnType = ServiceInformationModel;
      return this.apiClient.callApi(
        '/api/ServiceInformation', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
