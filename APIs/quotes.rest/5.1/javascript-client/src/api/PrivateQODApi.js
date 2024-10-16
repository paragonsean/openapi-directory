/**
 * They Said So Quotes API
 *  They Said So Quotes API offers a complete feature rich REST API access to its quotes platform.  This is the documentation for the world famous [quotes API](https://theysaidso.com/api).  If you are a subscriber and you are trying this from a console you can use Bearer token with your api key as the token. You can test and play with the API right here on this web page. Please note recently we closed downs public access without api key to prevent abuse. The public routes are still available to use free of charge but requires a api token. You can get one for free at our website. For using the private end points and subscribing to the API please visit [https://theysaidso.com/api](https://theysaidso.com/api).
 *
 * The version of the OpenAPI document: 5.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import QODResponse from '../model/QODResponse';
import QuoteResponse from '../model/QuoteResponse';
import SuccessResponse from '../model/SuccessResponse';

/**
* PrivateQOD service.
* @module api/PrivateQODApi
* @version 5.1
*/
export default class PrivateQODApi {

    /**
    * Constructs a new PrivateQODApi. 
    * @alias module:api/PrivateQODApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the qodGet_0 operation.
     * @callback module:api/PrivateQODApi~qodGet_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/QODResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets `Quote of the Day` (QOD). Optional `category` param determines the category of returned quote of the day 
     * @param {Object} opts Optional parameters
     * @param {String} [category] QOD Category (Used in public QOD only)
     * @param {String} [language = 'en')] Language of the QOD. The language must be supported in our QOD system.
     * @param {String} [id] QOD defition id (Used in private QOD only)
     * @param {module:api/PrivateQODApi~qodGet_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/QODResponse}
     */
    qodGet_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'category': opts['category'],
        'language': opts['language'],
        'id': opts['id']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = QODResponse;
      return this.apiClient.callApi(
        '/qod', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the qodPatch operation.
     * @callback module:api/PrivateQODApi~qodPatchCallback
     * @param {String} error Error message, if any.
     * @param {module:model/QuoteResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing private `Quote of the Day` definition. 
     * @param {String} title Title of the Quote of the day category
     * @param {Object} opts Optional parameters
     * @param {Number} [repeatAfter = 30)] How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
     * @param {Array} [authors] Comma seperated author names. Quotes will be chosen from one of these authors.
     * @param {Boolean} [_private = false)] Should apply the filters to the private collection. Default is public quotes in the platform.
     * @param {String} [language = 'en')] Quotes language.
     * @param {Boolean} [sfw = false)] Consider only quotes marked as \"sfw\" (Safe for work).
     * @param {module:api/PrivateQODApi~qodPatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/QuoteResponse}
     */
    qodPatch(title, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'title' is set
      if (title === undefined || title === null) {
        throw new Error("Missing the required parameter 'title' when calling qodPatch");
      }

      let pathParams = {
      };
      let queryParams = {
        'repeat_after': opts['repeatAfter'],
        'authors': opts['authors'],
        'title': title,
        'private': opts['_private'],
        'language': opts['language'],
        'sfw': opts['sfw']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = QuoteResponse;
      return this.apiClient.callApi(
        '/qod', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the qodPut operation.
     * @callback module:api/PrivateQODApi~qodPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a private `Quote of the Day` service.  
     * @param {String} title Title of the Quote of the day category
     * @param {Object} opts Optional parameters
     * @param {Number} [repeatAfter = 30)] How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
     * @param {Array} [authors] Comma seperated author names. Quotes will be chosen from one of these authors.
     * @param {Boolean} [_private = false)] Should apply the filters to the private collection. Default is public quotes in the platform.
     * @param {String} [language = 'en')] Quotes language.
     * @param {Boolean} [sfw = false)] Consider only quotes marked as \"sfw\" (Safe for work).
     * @param {module:api/PrivateQODApi~qodPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SuccessResponse}
     */
    qodPut(title, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'title' is set
      if (title === undefined || title === null) {
        throw new Error("Missing the required parameter 'title' when calling qodPut");
      }

      let pathParams = {
      };
      let queryParams = {
        'repeat_after': opts['repeatAfter'],
        'authors': opts['authors'],
        'title': title,
        'private': opts['_private'],
        'language': opts['language'],
        'sfw': opts['sfw']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = SuccessResponse;
      return this.apiClient.callApi(
        '/qod', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
