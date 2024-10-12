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
import Deleted from '../model/Deleted';
import PatchInner from '../model/PatchInner';
import ValidationAuthority from '../model/ValidationAuthority';

/**
* ValidationAuthorities service.
* @module api/ValidationAuthoritiesApi
* @version 1.5.0-dev
*/
export default class ValidationAuthoritiesApi {

    /**
    * Constructs a new ValidationAuthoritiesApi. 
    * @alias module:api/ValidationAuthoritiesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createClientValidator operation.
     * @callback module:api/ValidationAuthoritiesApi~createClientValidatorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ValidationAuthority} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create one validation authorities
     * Create one validation authorities
     * @param {Object} opts Optional parameters
     * @param {module:model/ValidationAuthority} [validationAuthority] 
     * @param {module:api/ValidationAuthoritiesApi~createClientValidatorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ValidationAuthority}
     */
    createClientValidator(opts, callback) {
      opts = opts || {};
      let postBody = opts['validationAuthority'];

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
      let returnType = ValidationAuthority;
      return this.apiClient.callApi(
        '/api/client-validators', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteClientValidator operation.
     * @callback module:api/ValidationAuthoritiesApi~deleteClientValidatorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Deleted} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete one validation authorities by id
     * Delete one validation authorities by id
     * @param {String} id The validation authorities id
     * @param {module:api/ValidationAuthoritiesApi~deleteClientValidatorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Deleted}
     */
    deleteClientValidator(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteClientValidator");
      }

      let pathParams = {
        'id': id
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
      let returnType = Deleted;
      return this.apiClient.callApi(
        '/api/client-validators/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the findAllClientValidators operation.
     * @callback module:api/ValidationAuthoritiesApi~findAllClientValidatorsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ValidationAuthority>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all validation authoritiess
     * Get all validation authoritiess
     * @param {module:api/ValidationAuthoritiesApi~findAllClientValidatorsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ValidationAuthority>}
     */
    findAllClientValidators(callback) {
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
      let returnType = [ValidationAuthority];
      return this.apiClient.callApi(
        '/api/client-validators', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the findClientValidatorById operation.
     * @callback module:api/ValidationAuthoritiesApi~findClientValidatorByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ValidationAuthority} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get one validation authorities by id
     * Get one validation authorities by id
     * @param {String} id The auth. config id
     * @param {module:api/ValidationAuthoritiesApi~findClientValidatorByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ValidationAuthority}
     */
    findClientValidatorById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling findClientValidatorById");
      }

      let pathParams = {
        'id': id
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
      let returnType = ValidationAuthority;
      return this.apiClient.callApi(
        '/api/client-validators/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchClientValidator operation.
     * @callback module:api/ValidationAuthoritiesApi~patchClientValidatorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ValidationAuthority} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update one validation authorities by id
     * Update one validation authorities by id
     * @param {String} id The validation authorities id
     * @param {Object} opts Optional parameters
     * @param {Array.<module:model/PatchInner>} [patchInner] 
     * @param {module:api/ValidationAuthoritiesApi~patchClientValidatorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ValidationAuthority}
     */
    patchClientValidator(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['patchInner'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patchClientValidator");
      }

      let pathParams = {
        'id': id
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
      let returnType = ValidationAuthority;
      return this.apiClient.callApi(
        '/api/client-validators/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateClientValidator operation.
     * @callback module:api/ValidationAuthoritiesApi~updateClientValidatorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ValidationAuthority} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update one validation authorities by id
     * Update one validation authorities by id
     * @param {String} id The validation authorities id
     * @param {Object} opts Optional parameters
     * @param {module:model/ValidationAuthority} [validationAuthority] 
     * @param {module:api/ValidationAuthoritiesApi~updateClientValidatorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ValidationAuthority}
     */
    updateClientValidator(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['validationAuthority'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateClientValidator");
      }

      let pathParams = {
        'id': id
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
      let returnType = ValidationAuthority;
      return this.apiClient.callApi(
        '/api/client-validators/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
