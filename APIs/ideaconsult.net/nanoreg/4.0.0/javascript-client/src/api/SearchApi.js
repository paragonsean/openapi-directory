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
import SolrResponse from '../model/SolrResponse';
import SolrqueryPostRequest from '../model/SolrqueryPostRequest';

/**
* Search service.
* @module api/SearchApi
* @version 4.0.0
*/
export default class SearchApi {

    /**
    * Constructs a new SearchApi. 
    * @alias module:api/SearchApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the solrqueryGet operation.
     * @callback module:api/SearchApi~solrqueryGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SolrResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Apache Solr powered search
     * GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.
     * @param {Object} opts Optional parameters
     * @param {String} [q] The query
     * @param {Number} [start] Starting page
     * @param {Number} [rows] Page size
     * @param {module:model/String} [wt = 'xml')] Response format
     * @param {module:api/SearchApi~solrqueryGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SolrResponse}
     */
    solrqueryGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'q': opts['q'],
        'start': opts['start'],
        'rows': opts['rows'],
        'wt': opts['wt']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = SolrResponse;
      return this.apiClient.callApi(
        '/select', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the solrqueryPost operation.
     * @callback module:api/SearchApi~solrqueryPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SolrResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Apache Solr powered search
     * POST is more complex to use, but also allows for much for complex and lengthy queries.
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [wt = 'xml')] Response format
     * @param {module:model/SolrqueryPostRequest} [solrqueryPostRequest] a JSON object with Solr query parameters
     * @param {module:api/SearchApi~solrqueryPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SolrResponse}
     */
    solrqueryPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['solrqueryPostRequest'];

      let pathParams = {
      };
      let queryParams = {
        'wt': opts['wt']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = SolrResponse;
      return this.apiClient.callApi(
        '/select', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
