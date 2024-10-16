/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ExtendedSubscriptionResponseModel from '../model/ExtendedSubscriptionResponseModel';
import HTTPValidationError from '../model/HTTPValidationError';
import UserResponseModel from '../model/UserResponseModel';

/**
* User service.
* @module api/UserApi
* @version 1.0
*/
export default class UserApi {

    /**
    * Constructs a new UserApi. 
    * @alias module:api/UserApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getUserInfoV1UserGet operation.
     * @callback module:api/UserApi~getUserInfoV1UserGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserResponseModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get User Info
     * Gets information about the user
     * @param {Object} opts Optional parameters
     * @param {String} [xiApiKey] Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
     * @param {module:api/UserApi~getUserInfoV1UserGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserResponseModel}
     */
    getUserInfoV1UserGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'xi-api-key': opts['xiApiKey']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UserResponseModel;
      return this.apiClient.callApi(
        '/v1/user', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUserSubscriptionInfoV1UserSubscriptionGet operation.
     * @callback module:api/UserApi~getUserSubscriptionInfoV1UserSubscriptionGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExtendedSubscriptionResponseModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get User Subscription Info
     * Gets extended information about the users subscription
     * @param {Object} opts Optional parameters
     * @param {String} [xiApiKey] Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
     * @param {module:api/UserApi~getUserSubscriptionInfoV1UserSubscriptionGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExtendedSubscriptionResponseModel}
     */
    getUserSubscriptionInfoV1UserSubscriptionGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'xi-api-key': opts['xiApiKey']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExtendedSubscriptionResponseModel;
      return this.apiClient.callApi(
        '/v1/user/subscription', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
