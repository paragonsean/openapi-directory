/**
 * httpbin.org
 * A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>
 *
 * The version of the OpenAPI document: 0.9.2
 * Contact: me@kennethreitz.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* ResponseInspection service.
* @module api/ResponseInspectionApi
* @version 0.9.2
*/
export default class ResponseInspectionApi {

    /**
    * Constructs a new ResponseInspectionApi. 
    * @alias module:api/ResponseInspectionApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the cacheGet operation.
     * @callback module:api/ResponseInspectionApi~cacheGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.
     * @param {Object} opts Optional parameters
     * @param {String} [ifModifiedSince] 
     * @param {String} [ifNoneMatch] 
     * @param {module:api/ResponseInspectionApi~cacheGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    cacheGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'If-Modified-Since': opts['ifModifiedSince'],
        'If-None-Match': opts['ifNoneMatch']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/cache', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cacheValueGet operation.
     * @callback module:api/ResponseInspectionApi~cacheValueGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Sets a Cache-Control header for n seconds.
     * @param {Number} value 
     * @param {module:api/ResponseInspectionApi~cacheValueGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    cacheValueGet(value, callback) {
      let postBody = null;
      // verify the required parameter 'value' is set
      if (value === undefined || value === null) {
        throw new Error("Missing the required parameter 'value' when calling cacheValueGet");
      }

      let pathParams = {
        'value': value
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/cache/{value}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the etagEtagGet operation.
     * @callback module:api/ResponseInspectionApi~etagEtagGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.
     * @param {String} etag Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [ifNoneMatch] 
     * @param {String} [ifMatch] 
     * @param {module:api/ResponseInspectionApi~etagEtagGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    etagEtagGet(etag, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'etag' is set
      if (etag === undefined || etag === null) {
        throw new Error("Missing the required parameter 'etag' when calling etagEtagGet");
      }

      let pathParams = {
        'etag': etag
      };
      let queryParams = {
      };
      let headerParams = {
        'If-None-Match': opts['ifNoneMatch'],
        'If-Match': opts['ifMatch']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/etag/{etag}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the responseHeadersGet operation.
     * @callback module:api/ResponseInspectionApi~responseHeadersGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a set of response headers from the query string.
     * @param {Object} opts Optional parameters
     * @param {Object.<String, {String: String}>} [freeform] 
     * @param {module:api/ResponseInspectionApi~responseHeadersGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    responseHeadersGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'freeform': opts['freeform']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/response-headers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the responseHeadersPost operation.
     * @callback module:api/ResponseInspectionApi~responseHeadersPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a set of response headers from the query string.
     * @param {Object} opts Optional parameters
     * @param {Object.<String, {String: String}>} [freeform] 
     * @param {module:api/ResponseInspectionApi~responseHeadersPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    responseHeadersPost(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'freeform': opts['freeform']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/response-headers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
