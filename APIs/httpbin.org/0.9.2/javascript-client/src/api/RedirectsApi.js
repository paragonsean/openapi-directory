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
* Redirects service.
* @module api/RedirectsApi
* @version 0.9.2
*/
export default class RedirectsApi {

    /**
    * Constructs a new RedirectsApi. 
    * @alias module:api/RedirectsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the absoluteRedirectNGet operation.
     * @callback module:api/RedirectsApi~absoluteRedirectNGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Absolutely 302 Redirects n times.
     * @param {Number} n 
     * @param {module:api/RedirectsApi~absoluteRedirectNGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    absoluteRedirectNGet(n, callback) {
      let postBody = null;
      // verify the required parameter 'n' is set
      if (n === undefined || n === null) {
        throw new Error("Missing the required parameter 'n' when calling absoluteRedirectNGet");
      }

      let pathParams = {
        'n': n
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
        '/absolute-redirect/{n}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the redirectNGet operation.
     * @callback module:api/RedirectsApi~redirectNGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 302 Redirects n times.
     * @param {Number} n 
     * @param {module:api/RedirectsApi~redirectNGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    redirectNGet(n, callback) {
      let postBody = null;
      // verify the required parameter 'n' is set
      if (n === undefined || n === null) {
        throw new Error("Missing the required parameter 'n' when calling redirectNGet");
      }

      let pathParams = {
        'n': n
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
        '/redirect/{n}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the redirectToDelete operation.
     * @callback module:api/RedirectsApi~redirectToDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 302/3XX Redirects to the given URL.
     * @param {module:api/RedirectsApi~redirectToDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    redirectToDelete(callback) {
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/redirect-to', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the redirectToGet operation.
     * @callback module:api/RedirectsApi~redirectToGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 302/3XX Redirects to the given URL.
     * @param {String} url 
     * @param {Object} opts Optional parameters
     * @param {Number} [statusCode] 
     * @param {module:api/RedirectsApi~redirectToGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    redirectToGet(url, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'url' is set
      if (url === undefined || url === null) {
        throw new Error("Missing the required parameter 'url' when calling redirectToGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'url': url,
        'status_code': opts['statusCode']
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
        '/redirect-to', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the redirectToPatch operation.
     * @callback module:api/RedirectsApi~redirectToPatchCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 302/3XX Redirects to the given URL.
     * @param {module:api/RedirectsApi~redirectToPatchCallback} callback The callback function, accepting three arguments: error, data, response
     */
    redirectToPatch(callback) {
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/redirect-to', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the redirectToPost operation.
     * @callback module:api/RedirectsApi~redirectToPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 302/3XX Redirects to the given URL.
     * @param {String} url 
     * @param {Object} opts Optional parameters
     * @param {Number} [statusCode] 
     * @param {module:api/RedirectsApi~redirectToPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    redirectToPost(url, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'url' is set
      if (url === undefined || url === null) {
        throw new Error("Missing the required parameter 'url' when calling redirectToPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'status_code': opts['statusCode'],
        'url': url
      };

      let authNames = [];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/redirect-to', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the redirectToPut operation.
     * @callback module:api/RedirectsApi~redirectToPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 302/3XX Redirects to the given URL.
     * @param {String} url 
     * @param {Object} opts Optional parameters
     * @param {Number} [statusCode] 
     * @param {module:api/RedirectsApi~redirectToPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    redirectToPut(url, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'url' is set
      if (url === undefined || url === null) {
        throw new Error("Missing the required parameter 'url' when calling redirectToPut");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'status_code': opts['statusCode'],
        'url': url
      };

      let authNames = [];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/redirect-to', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the redirectToTrace operation.
     * @callback module:api/RedirectsApi~redirectToTraceCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 302/3XX Redirects to the given URL.
     * @param {module:api/RedirectsApi~redirectToTraceCallback} callback The callback function, accepting three arguments: error, data, response
     */
    redirectToTrace(callback) {
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/redirect-to', 'TRACE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the relativeRedirectNGet operation.
     * @callback module:api/RedirectsApi~relativeRedirectNGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Relatively 302 Redirects n times.
     * @param {Number} n 
     * @param {module:api/RedirectsApi~relativeRedirectNGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    relativeRedirectNGet(n, callback) {
      let postBody = null;
      // verify the required parameter 'n' is set
      if (n === undefined || n === null) {
        throw new Error("Missing the required parameter 'n' when calling relativeRedirectNGet");
      }

      let pathParams = {
        'n': n
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
        '/relative-redirect/{n}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
