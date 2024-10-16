/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import HTTPValidationError from '../model/HTTPValidationError';
import TwilioMessageRequest from '../model/TwilioMessageRequest';

/**
* Twilio service.
* @module api/TwilioApi
* @version 0.1.0
*/
export default class TwilioApi {

    /**
    * Constructs a new TwilioApi. 
    * @alias module:api/TwilioApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the twilioMessageGetTwilioGet operation.
     * @callback module:api/TwilioApi~twilioMessageGetTwilioGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Twilio Message Get
     * @param {String} to 
     * @param {Object} opts Optional parameters
     * @param {String} [message] 
     * @param {String} [base64Message] 
     * @param {String} [authorization] 
     * @param {module:api/TwilioApi~twilioMessageGetTwilioGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    twilioMessageGetTwilioGet(to, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'to' is set
      if (to === undefined || to === null) {
        throw new Error("Missing the required parameter 'to' when calling twilioMessageGetTwilioGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'to': to,
        'message': opts['message'],
        'base64_message': opts['base64Message']
      };
      let headerParams = {
        'authorization': opts['authorization']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/twilio', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the twilioMessagePostTwilioPost operation.
     * @callback module:api/TwilioApi~twilioMessagePostTwilioPostCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Twilio Message Post
     * @param {module:model/TwilioMessageRequest} twilioMessageRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [authorization] 
     * @param {module:api/TwilioApi~twilioMessagePostTwilioPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    twilioMessagePostTwilioPost(twilioMessageRequest, opts, callback) {
      opts = opts || {};
      let postBody = twilioMessageRequest;
      // verify the required parameter 'twilioMessageRequest' is set
      if (twilioMessageRequest === undefined || twilioMessageRequest === null) {
        throw new Error("Missing the required parameter 'twilioMessageRequest' when calling twilioMessagePostTwilioPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'authorization': opts['authorization']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/twilio', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
