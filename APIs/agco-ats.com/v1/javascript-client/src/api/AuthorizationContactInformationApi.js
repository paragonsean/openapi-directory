/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation from '../model/APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation';
import APIModelsApiError from '../model/APIModelsApiError';
import AuthorizationCodesSharedModelsAuthorizationContactInformation from '../model/AuthorizationCodesSharedModelsAuthorizationContactInformation';

/**
* AuthorizationContactInformation service.
* @module api/AuthorizationContactInformationApi
* @version v1
*/
export default class AuthorizationContactInformationApi {

    /**
    * Constructs a new AuthorizationContactInformationApi. 
    * @alias module:api/AuthorizationContactInformationApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the authorizationContactInformationGet operation.
     * @callback module:api/AuthorizationContactInformationApi~authorizationContactInformationGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get contact information for authorization codes.
     * No Documentation Found.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Optional. The page limit.  If not specified, the default page limit is 10.
     * @param {Number} [offset] Optional. The page offset.  If not specified, the default page offset is 0.
     * @param {String} [authorizationCode] Optional. Search by authorization code.
     * @param {Date} [afterDate] Optional. Include only data for authorization codes created after a provided date.
     * @param {Date} [beforeDate] Optional. Include only data for authorization codes created before a provided date.
     * @param {String} [dealerCode] Optional. Search by dealer code.
     * @param {module:api/AuthorizationContactInformationApi~authorizationContactInformationGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation}
     */
    authorizationContactInformationGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'authorizationCode': opts['authorizationCode'],
        'afterDate': opts['afterDate'],
        'beforeDate': opts['beforeDate'],
        'dealerCode': opts['dealerCode']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation;
      return this.apiClient.callApi(
        '/api/v2/AuthorizationContactInformation', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the authorizationContactInformationPost operation.
     * @callback module:api/AuthorizationContactInformationApi~authorizationContactInformationPostCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add contact information for authorization code.
     * No Documentation Found.
     * @param {module:model/AuthorizationCodesSharedModelsAuthorizationContactInformation} authorizationCodesSharedModelsAuthorizationContactInformation A contact information.
     * @param {module:api/AuthorizationContactInformationApi~authorizationContactInformationPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    authorizationContactInformationPost(authorizationCodesSharedModelsAuthorizationContactInformation, callback) {
      let postBody = authorizationCodesSharedModelsAuthorizationContactInformation;
      // verify the required parameter 'authorizationCodesSharedModelsAuthorizationContactInformation' is set
      if (authorizationCodesSharedModelsAuthorizationContactInformation === undefined || authorizationCodesSharedModelsAuthorizationContactInformation === null) {
        throw new Error("Missing the required parameter 'authorizationCodesSharedModelsAuthorizationContactInformation' when calling authorizationContactInformationPost");
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
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/api/v2/AuthorizationContactInformation', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
