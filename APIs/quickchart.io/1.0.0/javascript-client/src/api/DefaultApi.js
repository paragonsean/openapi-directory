/**
 * QuickChart API
 * An API to generate charts and QR codes using QuickChart services.
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
import ChartPostRequest from '../model/ChartPostRequest';
import QrPostRequest from '../model/QrPostRequest';

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
     * Callback function to receive the result of the chartGet operation.
     * @callback module:api/DefaultApi~chartGetCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a chart (GET)
     * Generate a chart based on the provided parameters.
     * @param {Object} opts Optional parameters
     * @param {String} [chart] The chart configuration in Chart.js format (JSON or Javascript).
     * @param {Number} [width] The width of the chart in pixels.
     * @param {Number} [height] The height of the chart in pixels.
     * @param {String} [format] The output format of the chart, 'png', 'jpg', 'svg', or 'webp'.
     * @param {String} [backgroundColor] The background color of the chart.
     * @param {module:api/DefaultApi~chartGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    chartGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'chart': opts['chart'],
        'width': opts['width'],
        'height': opts['height'],
        'format': opts['format'],
        'backgroundColor': opts['backgroundColor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['image/jpeg', 'image/png', 'image/svg+xml', 'image/webp'];
      let returnType = File;
      return this.apiClient.callApi(
        '/chart', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the chartPost operation.
     * @callback module:api/DefaultApi~chartPostCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a chart (POST)
     * Generate a chart based on the provided configuration in the request body.
     * @param {module:model/ChartPostRequest} chartPostRequest 
     * @param {module:api/DefaultApi~chartPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    chartPost(chartPostRequest, callback) {
      let postBody = chartPostRequest;
      // verify the required parameter 'chartPostRequest' is set
      if (chartPostRequest === undefined || chartPostRequest === null) {
        throw new Error("Missing the required parameter 'chartPostRequest' when calling chartPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['image/jpeg', 'image/png', 'image/svg+xml', 'image/webp'];
      let returnType = File;
      return this.apiClient.callApi(
        '/chart', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the qrGet operation.
     * @callback module:api/DefaultApi~qrGetCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a QR code (GET)
     * Generate a QR code based on the provided parameters.
     * @param {Object} opts Optional parameters
     * @param {String} [text] The text to be encoded in the QR code.
     * @param {Number} [width] The width of the QR code in pixels.
     * @param {Number} [height] The height of the QR code in pixels.
     * @param {String} [format] The output format of the QR code, e.g., 'png' or 'svg'.
     * @param {Number} [margin] The margin around the QR code in pixels.
     * @param {module:api/DefaultApi~qrGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    qrGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'text': opts['text'],
        'width': opts['width'],
        'height': opts['height'],
        'format': opts['format'],
        'margin': opts['margin']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['image/png', 'image/svg+xml'];
      let returnType = File;
      return this.apiClient.callApi(
        '/qr', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the qrPost operation.
     * @callback module:api/DefaultApi~qrPostCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a QR code (POST)
     * Generate a QR code based on the provided configuration in the request body.
     * @param {module:model/QrPostRequest} qrPostRequest 
     * @param {module:api/DefaultApi~qrPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    qrPost(qrPostRequest, callback) {
      let postBody = qrPostRequest;
      // verify the required parameter 'qrPostRequest' is set
      if (qrPostRequest === undefined || qrPostRequest === null) {
        throw new Error("Missing the required parameter 'qrPostRequest' when calling qrPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['image/png', 'image/svg+xml'];
      let returnType = File;
      return this.apiClient.callApi(
        '/qr', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
