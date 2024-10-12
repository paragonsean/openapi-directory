/**
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Facet from '../model/Facet';

/**
* Facets service.
* @module api/FacetsApi
* @version 4.0.0
*/
export default class FacetsApi {

    /**
    * Constructs a new FacetsApi. 
    * @alias module:api/FacetsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getEndpointSummary_0 operation.
     * @callback module:api/FacetsApi~getEndpointSummary_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/Facet} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search endpoint summary
     * Returns endpoint summary
     * @param {module:model/String} db Database ID
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [top] Top endpoint category
     * @param {String} [category] Endpoint category (The value in the protocol.category.code field)
     * @param {module:api/FacetsApi~getEndpointSummary_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Facet}
     */
    getEndpointSummary_0(db, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'db' is set
      if (db === undefined || db === null) {
        throw new Error("Missing the required parameter 'db' when calling getEndpointSummary_0");
      }

      let pathParams = {
        'db': db
      };
      let queryParams = {
        'top': opts['top'],
        'category': opts['category']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Facet;
      return this.apiClient.callApi(
        '/enm/{db}/query/study', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
