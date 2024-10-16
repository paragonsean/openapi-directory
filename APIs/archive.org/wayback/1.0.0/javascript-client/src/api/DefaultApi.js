/**
 * Wayback API
 * API for Internet Archive's Wayback Machine
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AvailabilityRequest from '../model/AvailabilityRequest';
import AvailabilityResults from '../model/AvailabilityResults';
import Error from '../model/Error';

/**
* Default service.
* @module api/DefaultApi
* @version 1.0.0
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the waybackV1AvailableGet operation.
     * @callback module:api/DefaultApi~waybackV1AvailableGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} url A single URL to query.
     * @param {Object} opts Optional parameters
     * @param {String} [timestamp] Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
     * @param {String} [callback] Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
     * @param {Number} [timeout = 5)] Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
     * @param {module:model/String} [closest = 'either')] The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
     * @param {module:model/Number} [statusCode] HTTP status codes to filter by. Only results with these codes will be returned 
     * @param {String} [tag] The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
     * @param {module:api/DefaultApi~waybackV1AvailableGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    waybackV1AvailableGet(url, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'url' is set
      if (url === undefined || url === null) {
        throw new Error("Missing the required parameter 'url' when calling waybackV1AvailableGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'url': url,
        'timestamp': opts['timestamp'],
        'callback': opts['callback'],
        'timeout': opts['timeout'],
        'closest': opts['closest'],
        'status_code': opts['statusCode'],
        'tag': opts['tag']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['applcation/json', 'application/javascript', 'application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/wayback/v1/available', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the waybackV1AvailablePost operation.
     * @callback module:api/DefaultApi~waybackV1AvailablePostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} url A single URL to query.
     * @param {Object} opts Optional parameters
     * @param {String} [timestamp] Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
     * @param {String} [callback] Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
     * @param {Number} [timeout = 5)] Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
     * @param {module:model/String} [closest = 'either')] The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
     * @param {module:model/Number} [statusCode] HTTP status codes to filter by. Only results with these codes will be returned 
     * @param {String} [tag] The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
     * @param {Array.<module:model/AvailabilityRequest>} [availabilityRequest] 
     * @param {module:api/DefaultApi~waybackV1AvailablePostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    waybackV1AvailablePost(url, opts, callback) {
      opts = opts || {};
      let postBody = opts['availabilityRequest'];
      // verify the required parameter 'url' is set
      if (url === undefined || url === null) {
        throw new Error("Missing the required parameter 'url' when calling waybackV1AvailablePost");
      }

      let pathParams = {
      };
      let queryParams = {
        'url': url,
        'timestamp': opts['timestamp'],
        'callback': opts['callback'],
        'timeout': opts['timeout'],
        'closest': opts['closest'],
        'status_code': opts['statusCode'],
        'tag': opts['tag']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'text/csv'];
      let accepts = ['applcation/json', 'application/javascript', 'application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/wayback/v1/available', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
