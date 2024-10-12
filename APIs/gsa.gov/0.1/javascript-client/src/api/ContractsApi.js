/**
 * Discovery Market Research
 * <p>This API drives the <a href=\"https://discovery.gsa.gov\">Discovery Market Research Tool</a>. It contains information on the vendors that are part of the OASIS and OASIS Small Business contracting vehicles, such as their contracting history, their elligibility for contract awards, and their small business designations. To learn more about the tool, please visit <a href=\"https://discovery.gsa.gov\">Discovery</a> or see the README on our <a href=\"https://github.com/PSHCDevOps/discovery\">GitHub repository</a>.</p> <p><strong>Please note that the base path for this API is <code>https://api.data.gov/gsa/discovery/</code></strong></p> <p>It requires an API key, obtainable at <a href=\"http://api.data.gov/\">api.data.gov</a>. It must be passed in the <code>api_key</code> parameter with each request.</p>
 *
 * The version of the OpenAPI document: 0.1
 * Contact: discovery-18f@gsa.gov
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Contracts service.
* @module api/ContractsApi
* @version 0.1
*/
export default class ContractsApi {

    /**
    * Constructs a new ContractsApi. 
    * @alias module:api/ContractsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the listContractsGET operation.
     * @callback module:api/ContractsApi~listContractsGETCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * This endpoint returns contract history from FPDS for a specific vendor
     * <p>This endpoint returns contract history from FPDS for a specific vendor. The vendor's DUNS number is a required parameter. You can also filter contracts by their NAICS code to find contracts relevant to a particular category.</p>
     * @param {String} duns A 9-digit DUNS number that uniquely identifies a vendor (required).
     * @param {Object} opts Optional parameters
     * @param {String} [naics] a six digit NAICS code used to filter by contracts with a certain NAICS
     * @param {String} [sort] a field to sort on. Choices are date, status, agency, and amount
     * @param {String} [direction] The sort direction of the results. Choices are asc or desc.
     * @param {String} [page] the page to start on. Results are paginated in increments of 100. Begins at page=1.
     * @param {module:api/ContractsApi~listContractsGETCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    listContractsGET(duns, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'duns' is set
      if (duns === undefined || duns === null) {
        throw new Error("Missing the required parameter 'duns' when calling listContractsGET");
      }

      let pathParams = {
      };
      let queryParams = {
        'duns': duns,
        'naics': opts['naics'],
        'sort': opts['sort'],
        'direction': opts['direction'],
        'page': opts['page']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/api/contracts/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
