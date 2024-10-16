/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import KeywordConfig from '../model/KeywordConfig';
import KeywordLease from '../model/KeywordLease';
import KeywordLeasePage from '../model/KeywordLeasePage';
import KeywordList from '../model/KeywordList';
import Page from '../model/Page';

/**
* Keywords service.
* @module api/KeywordsApi
* @version V2
*/
export default class KeywordsApi {

    /**
    * Constructs a new KeywordsApi. 
    * @alias module:api/KeywordsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the findKeywordLeaseConfigs operation.
     * @callback module:api/KeywordsApi~findKeywordLeaseConfigsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Page} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find keyword lease configs
     * Searches for all keyword lease configs for the user. Returns a paged list of KeywordConfig
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 20)] To set the maximum number of records to return in a paged list response. The default is 100
     * @param {Number} [offset = 0)] Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
     * @param {String} [filter] Filter by part of Keyword name or Label name of Keyword
     * @param {String} [labelName] An exact label name to search by
     * @param {String} [fields] Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
     * @param {module:api/KeywordsApi~findKeywordLeaseConfigsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Page}
     */
    findKeywordLeaseConfigs(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'labelName': opts['labelName'],
        'fields': opts['fields']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Page;
      return this.apiClient.callApi(
        '/keywords/leases/configs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the findKeywordLeases operation.
     * @callback module:api/KeywordsApi~findKeywordLeasesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KeywordLeasePage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find keyword leases
     * Searches for all keywords owned by user. A keyword lease is the ownership information involving a keyword
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 100)] To set the maximum number of records to return in a paged list response. The default is 100
     * @param {Number} [offset = 0)] Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
     * @param {String} [filter] Filter by part of Keyword name or Label name of Keyword
     * @param {String} [labelName] An exact label name to search by
     * @param {String} [fields] Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
     * @param {module:api/KeywordsApi~findKeywordLeasesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KeywordLeasePage}
     */
    findKeywordLeases(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'filter': opts['filter'],
        'labelName': opts['labelName'],
        'fields': opts['fields']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = KeywordLeasePage;
      return this.apiClient.callApi(
        '/keywords/leases', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the findKeywords operation.
     * @callback module:api/KeywordsApi~findKeywordsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KeywordList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find keywords
     * Searches for all keywords available for purchase on the CallFire platform. If a keyword appears in the response, it is available for purchase. List the 'keywords' in a query parameter to search for multiple keywords (at least one keyword should be sent in request). Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [keywords] A keyword to search for
     * @param {module:api/KeywordsApi~findKeywordsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KeywordList}
     */
    findKeywords(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'keywords': this.apiClient.buildCollectionParam(opts['keywords'], 'multi')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = KeywordList;
      return this.apiClient.callApi(
        '/keywords', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKeywordLease operation.
     * @callback module:api/KeywordsApi~getKeywordLeaseCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KeywordLease} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find a specific lease
     * Searches for all keywords owned by user
     * @param {String} keyword Keyword text that a lease is desired for
     * @param {Object} opts Optional parameters
     * @param {String} [fields] Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
     * @param {module:api/KeywordsApi~getKeywordLeaseCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KeywordLease}
     */
    getKeywordLease(keyword, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'keyword' is set
      if (keyword === undefined || keyword === null) {
        throw new Error("Missing the required parameter 'keyword' when calling getKeywordLease");
      }

      let pathParams = {
        'keyword': keyword
      };
      let queryParams = {
        'fields': opts['fields']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = KeywordLease;
      return this.apiClient.callApi(
        '/keywords/leases/{keyword}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKeywordLeaseById operation.
     * @callback module:api/KeywordsApi~getKeywordLeaseByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KeywordLease} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find a keyword by id
     * Get keyword by id
     * @param {Number} id ~
     * @param {Object} opts Optional parameters
     * @param {String} [fields] Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
     * @param {module:api/KeywordsApi~getKeywordLeaseByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KeywordLease}
     */
    getKeywordLeaseById(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getKeywordLeaseById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'fields': opts['fields']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = KeywordLease;
      return this.apiClient.callApi(
        '/keywords/leases/id/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKeywordLeaseConfig operation.
     * @callback module:api/KeywordsApi~getKeywordLeaseConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/KeywordConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find a specific keyword lease config
     * Returns a single KeywordConfig instance for a given keyword lease
     * @param {String} keyword A Keyword to get KeywordConfig by
     * @param {Object} opts Optional parameters
     * @param {String} [fields] Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
     * @param {module:api/KeywordsApi~getKeywordLeaseConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/KeywordConfig}
     */
    getKeywordLeaseConfig(keyword, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'keyword' is set
      if (keyword === undefined || keyword === null) {
        throw new Error("Missing the required parameter 'keyword' when calling getKeywordLeaseConfig");
      }

      let pathParams = {
        'keyword': keyword
      };
      let queryParams = {
        'fields': opts['fields']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = KeywordConfig;
      return this.apiClient.callApi(
        '/keywords/leases/configs/{keyword}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the isKeywordAvailable operation.
     * @callback module:api/KeywordsApi~isKeywordAvailableCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Check for a specific keyword
     * Searches for the specific keyword to purchase on the CallFire platform. Returns 'true' if keyword is available. Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.
     * @param {String} keyword To specify a keyword to search for. Example: SUN, MOON
     * @param {module:api/KeywordsApi~isKeywordAvailableCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    isKeywordAvailable(keyword, callback) {
      let postBody = null;
      // verify the required parameter 'keyword' is set
      if (keyword === undefined || keyword === null) {
        throw new Error("Missing the required parameter 'keyword' when calling isKeywordAvailable");
      }

      let pathParams = {
        'keyword': keyword
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/keywords/{keyword}/available', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateKeywordLease operation.
     * @callback module:api/KeywordsApi~updateKeywordLeaseCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a lease
     * Updates a keyword lease. Turns the autoRenew on/off. Configure double opt in feature. Add/remove contact list from keyword.
     * @param {String} keyword To update a keyword lease
     * @param {Object} opts Optional parameters
     * @param {module:model/KeywordLease} [keywordLease] A keyword lease object
     * @param {module:api/KeywordsApi~updateKeywordLeaseCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateKeywordLease(keyword, opts, callback) {
      opts = opts || {};
      let postBody = opts['keywordLease'];
      // verify the required parameter 'keyword' is set
      if (keyword === undefined || keyword === null) {
        throw new Error("Missing the required parameter 'keyword' when calling updateKeywordLease");
      }

      let pathParams = {
        'keyword': keyword
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/keywords/leases/{keyword}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateKeywordLeaseConfig operation.
     * @callback module:api/KeywordsApi~updateKeywordLeaseConfigCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a keyword lease config
     * Updates a keyword lease configuration. Use this API endpoint to enable/disable inbound SMS forwarding, set forward number. Forward number must be in E.164 format)
     * @param {String} keyword To update a keyword lease config
     * @param {Object} opts Optional parameters
     * @param {module:model/KeywordConfig} [keywordConfig] The configuration of a keyword lease object.
     * @param {module:api/KeywordsApi~updateKeywordLeaseConfigCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateKeywordLeaseConfig(keyword, opts, callback) {
      opts = opts || {};
      let postBody = opts['keywordConfig'];
      // verify the required parameter 'keyword' is set
      if (keyword === undefined || keyword === null) {
        throw new Error("Missing the required parameter 'keyword' when calling updateKeywordLeaseConfig");
      }

      let pathParams = {
        'keyword': keyword
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/keywords/leases/configs/{keyword}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
