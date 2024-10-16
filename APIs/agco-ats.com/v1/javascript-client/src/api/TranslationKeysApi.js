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
import APIIPagedResponseOASSupportSharedModelsTranslationKey from '../model/APIIPagedResponseOASSupportSharedModelsTranslationKey';
import APIModelsApiError from '../model/APIModelsApiError';
import OASSupportSharedModelsTranslationKey from '../model/OASSupportSharedModelsTranslationKey';

/**
* TranslationKeys service.
* @module api/TranslationKeysApi
* @version v1
*/
export default class TranslationKeysApi {

    /**
    * Constructs a new TranslationKeysApi. 
    * @alias module:api/TranslationKeysApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the translationKeysCreateTranslationKey operation.
     * @callback module:api/TranslationKeysApi~translationKeysCreateTranslationKeyCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a translationKey object.
     * No Documentation Found.
     * @param {module:model/OASSupportSharedModelsTranslationKey} oASSupportSharedModelsTranslationKey 
     * @param {module:api/TranslationKeysApi~translationKeysCreateTranslationKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    translationKeysCreateTranslationKey(oASSupportSharedModelsTranslationKey, callback) {
      let postBody = oASSupportSharedModelsTranslationKey;
      // verify the required parameter 'oASSupportSharedModelsTranslationKey' is set
      if (oASSupportSharedModelsTranslationKey === undefined || oASSupportSharedModelsTranslationKey === null) {
        throw new Error("Missing the required parameter 'oASSupportSharedModelsTranslationKey' when calling translationKeysCreateTranslationKey");
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
        '/api/v2/TranslationKeys', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the translationKeysGet operation.
     * @callback module:api/TranslationKeysApi~translationKeysGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/APIIPagedResponseOASSupportSharedModelsTranslationKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a paged response of TranslationKeys.
     * 
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] 
     * @param {Number} [offset] 
     * @param {String} [keyNames] Can filter by keyNames, a comma deliminated list.
     * @param {module:api/TranslationKeysApi~translationKeysGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/APIIPagedResponseOASSupportSharedModelsTranslationKey}
     */
    translationKeysGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'keyNames': opts['keyNames']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = APIIPagedResponseOASSupportSharedModelsTranslationKey;
      return this.apiClient.callApi(
        '/api/v2/TranslationKeys', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the translationKeysGetTranslationKey operation.
     * @callback module:api/TranslationKeysApi~translationKeysGetTranslationKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OASSupportSharedModelsTranslationKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get TranslationKey by ID
     * No Documentation Found.
     * @param {Number} ID 
     * @param {module:api/TranslationKeysApi~translationKeysGetTranslationKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OASSupportSharedModelsTranslationKey}
     */
    translationKeysGetTranslationKey(ID, callback) {
      let postBody = null;
      // verify the required parameter 'ID' is set
      if (ID === undefined || ID === null) {
        throw new Error("Missing the required parameter 'ID' when calling translationKeysGetTranslationKey");
      }

      let pathParams = {
        'ID': ID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = OASSupportSharedModelsTranslationKey;
      return this.apiClient.callApi(
        '/api/v2/TranslationKeys/{ID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the translationKeysUpdateTranslationKey operation.
     * @callback module:api/TranslationKeysApi~translationKeysUpdateTranslationKeyCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the StringID of the translationKey object.
     * No Documentation Found.
     * @param {Number} ID 
     * @param {module:model/OASSupportSharedModelsTranslationKey} oASSupportSharedModelsTranslationKey 
     * @param {module:api/TranslationKeysApi~translationKeysUpdateTranslationKeyCallback} callback The callback function, accepting three arguments: error, data, response
     */
    translationKeysUpdateTranslationKey(ID, oASSupportSharedModelsTranslationKey, callback) {
      let postBody = oASSupportSharedModelsTranslationKey;
      // verify the required parameter 'ID' is set
      if (ID === undefined || ID === null) {
        throw new Error("Missing the required parameter 'ID' when calling translationKeysUpdateTranslationKey");
      }
      // verify the required parameter 'oASSupportSharedModelsTranslationKey' is set
      if (oASSupportSharedModelsTranslationKey === undefined || oASSupportSharedModelsTranslationKey === null) {
        throw new Error("Missing the required parameter 'oASSupportSharedModelsTranslationKey' when calling translationKeysUpdateTranslationKey");
      }

      let pathParams = {
        'ID': ID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/TranslationKeys/{ID}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
