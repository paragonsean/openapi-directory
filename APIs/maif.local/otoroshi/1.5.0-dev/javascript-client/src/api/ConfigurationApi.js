/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import GlobalConfig from '../model/GlobalConfig';
import PatchInner from '../model/PatchInner';

/**
* Configuration service.
* @module api/ConfigurationApi
* @version 1.5.0-dev
*/
export default class ConfigurationApi {

    /**
    * Constructs a new ConfigurationApi. 
    * @alias module:api/ConfigurationApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the globalConfig operation.
     * @callback module:api/ConfigurationApi~globalConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GlobalConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the full configuration of Otoroshi
     * Get the full configuration of Otoroshi
     * @param {module:api/ConfigurationApi~globalConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GlobalConfig}
     */
    globalConfig(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['otoroshi_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GlobalConfig;
      return this.apiClient.callApi(
        '/api/globalconfig', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchGlobalConfig operation.
     * @callback module:api/ConfigurationApi~patchGlobalConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GlobalConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the global configuration with a diff
     * Update the global configuration with a diff
     * @param {Object} opts Optional parameters
     * @param {Array.<module:model/PatchInner>} [patchInner] 
     * @param {module:api/ConfigurationApi~patchGlobalConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GlobalConfig}
     */
    patchGlobalConfig(opts, callback) {
      opts = opts || {};
      let postBody = opts['patchInner'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['otoroshi_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GlobalConfig;
      return this.apiClient.callApi(
        '/api/globalconfig', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putGlobalConfig operation.
     * @callback module:api/ConfigurationApi~putGlobalConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GlobalConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the global configuration
     * Update the global configuration
     * @param {Object} opts Optional parameters
     * @param {module:model/GlobalConfig} [globalConfig] 
     * @param {module:api/ConfigurationApi~putGlobalConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GlobalConfig}
     */
    putGlobalConfig(opts, callback) {
      opts = opts || {};
      let postBody = opts['globalConfig'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['otoroshi_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GlobalConfig;
      return this.apiClient.callApi(
        '/api/globalconfig', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
