/**
 * CORE API v2
 * <p style=\"text-align: justify;\">You can use the CORE API to access the      resources harvested and enriched by CORE. If you encounter any problems with the API, please <a href=\"/contact\">report them to us</a>.</p>  <h2>Overview</h2> <p style=\"text-align: justify;\">The API is organised by resource type. The resources are <b>articles</b>,      <b>journals</b> and <b>repositories</b> and are represented using JSON data format. Furthermore,      each resource has a list of methods. The API also provides two global methods for accessing all resources at once.</p>  <h2>Response format</h2> <p style=\"text-align: justify;\">Response for each query contains two fields: <b>status</b> and <b>data</b>.     In case of an error status, the data field is empty. The data field contains a single object     in case the request is for a specific identifier (e.g. CORE ID, CORE repository ID, etc.), or       contains a list of objects, for example for search queries. In case of batch requests, the response     is an array of objects, each of which contains its own <b>status</b> and <b>data</b> fields.     For search queries the response contains an additional field <b>totalHits</b>, which is the      total number of items which match the search criteria.</p>  <h2>Search query syntax</h2>  <p style=\"text-align: justify\">Complex search queries can be used in all of the API search methods.     The query can be a simple string or it can be built using terms and operators described in Elasticsearch     <a href=\"http://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-query-string-query.html#query-string-syntax\">documentation</a>.     The usable field names are <strong>title</strong>, <strong>description</strong>, <strong>fullText</strong>,      <strong>authors</strong>, <strong>publisher</strong>, <strong>repositories.id</strong>, <strong>repositories.name</strong>,      <strong>doi</strong>, <strong>oai</strong>, <strong>identifiers</strong> (which is a list of article identifiers including OAI, URL, etc.), <strong>language.name</strong>      and <strong>year</strong>. Some example queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>title:psychology and language.name:English</p></li>     <li><p>repositories.id:86 AND year:2014</p></li>     <li><p>identifiers:\"oai:aura.abdn.ac.uk:2164/3837\" OR identifiers:\"oai:aura.abdn.ac.uk:2164/3843\"</p></li>     <li><p>doi:\"10.1186/1471-2458-6-309\"</p></li> </ul>  <h3>Retrieving the latest Articles</h3> <p style=\"text-align: justify\">     You can retrieve the harvested items since specific dates using the following queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>repositoryDocument.metadataUpdated:>2017-02-10</p></li>     <li><p>repositoryDocument.metadataUpdated:>2017-03-01 AND repositoryDocument.metadataUpdated:<2017-03-31</p></li>     </ul>  <h2>Sort order</h2>  <p style=\"text-align: justify;\">For search queries, the results are ordered by relevance score. For batch      requests, the results are retrieved in the order of the requests.</p>  <h2>Parameters</h2> <p style=\"text-align: justify;\">The API methods allow different parameters to be passed. Additionally, there is an API key parameter which is common to all API methods. For all API methods      the API key can be provided either as a query parameter or in the request header. If the API key      is not provided, the API will return HTTP 401 error. You can register for an API key <a href=\"/services#api\">here</a>.</p>  <h2>API methods</h2>
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import JournalResponse from '../model/JournalResponse';
import JournalSearchResponse from '../model/JournalSearchResponse';
import SearchRequest from '../model/SearchRequest';

/**
* Journals service.
* @module api/JournalsApi
* @version 2.0
*/
export default class JournalsApi {

    /**
    * Constructs a new JournalsApi. 
    * @alias module:api/JournalsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getJournalByIssn operation.
     * @callback module:api/JournalsApi~getJournalByIssnCallback
     * @param {String} error Error message, if any.
     * @param {module:model/JournalResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find journal by ISSN
     * Returns a journal with given ISSN identifier.
     * @param {String} issn ISSN identifier of journal that needs to be fetched.
     * @param {module:api/JournalsApi~getJournalByIssnCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/JournalResponse}
     */
    getJournalByIssn(issn, callback) {
      let postBody = null;
      // verify the required parameter 'issn' is set
      if (issn === undefined || issn === null) {
        throw new Error("Missing the required parameter 'issn' when calling getJournalByIssn");
      }

      let pathParams = {
        'issn': issn
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = JournalResponse;
      return this.apiClient.callApi(
        '/journals/get/{issn}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getJournalByIssnBatch operation.
     * @callback module:api/JournalsApi~getJournalByIssnBatchCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/JournalResponse>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Batch operation for retrieving journals by ISSN
     * Method accepts a JSON array of ISSNs and retrieves a list of journals.
     * @param {Array.<String>} body JSON array with ISSNs of journals that need to be fetched
     * @param {module:api/JournalsApi~getJournalByIssnBatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/JournalResponse>}
     */
    getJournalByIssnBatch(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling getJournalByIssnBatch");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [JournalResponse];
      return this.apiClient.callApi(
        '/journals/get', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the journalsSearchPost operation.
     * @callback module:api/JournalsApi~journalsSearchPostCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/JournalResponse>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Batch operation for search through journals
     * Method accepts a JSON array of search queries and parameters. It then searches through all journals and returns a JSON array of search results for each of the queries. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).
     * @param {Array.<module:model/SearchRequest>} body JSON array with search queries and parameters. One request can contain up to 100 queries.
     * @param {module:api/JournalsApi~journalsSearchPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/JournalResponse>}
     */
    journalsSearchPost(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling journalsSearchPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [JournalResponse];
      return this.apiClient.callApi(
        '/journals/search', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the journalsSearchQueryGet operation.
     * @callback module:api/JournalsApi~journalsSearchQueryGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/JournalSearchResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search through journals
     * Searches through all journals and returns a JSON array of search results. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).
     * @param {String} query Search query
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
     * @param {Number} [pageSize = 10)] The number of results to return per page. Can be any number between 10 and 100, default is 10.
     * @param {module:api/JournalsApi~journalsSearchQueryGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/JournalSearchResponse}
     */
    journalsSearchQueryGet(query, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'query' is set
      if (query === undefined || query === null) {
        throw new Error("Missing the required parameter 'query' when calling journalsSearchQueryGet");
      }

      let pathParams = {
        'query': query
      };
      let queryParams = {
        'page': opts['page'],
        'pageSize': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = JournalSearchResponse;
      return this.apiClient.callApi(
        '/journals/search/{query}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
