/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ComponentRepresentation from '../model/ComponentRepresentation';
import ComponentTypeRepresentation from '../model/ComponentTypeRepresentation';

/**
* Component service.
* @module api/ComponentApi
* @version 1
*/
export default class ComponentApi {

    /**
    * Constructs a new ComponentApi. 
    * @alias module:api/ComponentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the realmComponentsGet operation.
     * @callback module:api/ComponentApi~realmComponentsGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ComponentRepresentation>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} realm realm name (not id!)
     * @param {Object} opts Optional parameters
     * @param {String} [name] 
     * @param {String} [parent] 
     * @param {String} [type] 
     * @param {module:api/ComponentApi~realmComponentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ComponentRepresentation>}
     */
    realmComponentsGet(realm, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'realm' is set
      if (realm === undefined || realm === null) {
        throw new Error("Missing the required parameter 'realm' when calling realmComponentsGet");
      }

      let pathParams = {
        'realm': realm
      };
      let queryParams = {
        'name': opts['name'],
        'parent': opts['parent'],
        'type': opts['type']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['access_token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [ComponentRepresentation];
      return this.apiClient.callApi(
        '/{realm}/components', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the realmComponentsIdDelete operation.
     * @callback module:api/ComponentApi~realmComponentsIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} realm realm name (not id!)
     * @param {String} id 
     * @param {module:api/ComponentApi~realmComponentsIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    realmComponentsIdDelete(realm, id, callback) {
      let postBody = null;
      // verify the required parameter 'realm' is set
      if (realm === undefined || realm === null) {
        throw new Error("Missing the required parameter 'realm' when calling realmComponentsIdDelete");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling realmComponentsIdDelete");
      }

      let pathParams = {
        'realm': realm,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['access_token'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/{realm}/components/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the realmComponentsIdGet operation.
     * @callback module:api/ComponentApi~realmComponentsIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ComponentRepresentation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} realm realm name (not id!)
     * @param {String} id 
     * @param {module:api/ComponentApi~realmComponentsIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ComponentRepresentation}
     */
    realmComponentsIdGet(realm, id, callback) {
      let postBody = null;
      // verify the required parameter 'realm' is set
      if (realm === undefined || realm === null) {
        throw new Error("Missing the required parameter 'realm' when calling realmComponentsIdGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling realmComponentsIdGet");
      }

      let pathParams = {
        'realm': realm,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['access_token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ComponentRepresentation;
      return this.apiClient.callApi(
        '/{realm}/components/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the realmComponentsIdPut operation.
     * @callback module:api/ComponentApi~realmComponentsIdPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} realm realm name (not id!)
     * @param {String} id 
     * @param {module:model/ComponentRepresentation} componentRepresentation 
     * @param {module:api/ComponentApi~realmComponentsIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    realmComponentsIdPut(realm, id, componentRepresentation, callback) {
      let postBody = componentRepresentation;
      // verify the required parameter 'realm' is set
      if (realm === undefined || realm === null) {
        throw new Error("Missing the required parameter 'realm' when calling realmComponentsIdPut");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling realmComponentsIdPut");
      }
      // verify the required parameter 'componentRepresentation' is set
      if (componentRepresentation === undefined || componentRepresentation === null) {
        throw new Error("Missing the required parameter 'componentRepresentation' when calling realmComponentsIdPut");
      }

      let pathParams = {
        'realm': realm,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['access_token'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/{realm}/components/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the realmComponentsIdSubComponentTypesGet operation.
     * @callback module:api/ComponentApi~realmComponentsIdSubComponentTypesGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ComponentTypeRepresentation>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List of subcomponent types that are available to configure for a particular parent component.
     * @param {String} realm realm name (not id!)
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [type] 
     * @param {module:api/ComponentApi~realmComponentsIdSubComponentTypesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ComponentTypeRepresentation>}
     */
    realmComponentsIdSubComponentTypesGet(realm, id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'realm' is set
      if (realm === undefined || realm === null) {
        throw new Error("Missing the required parameter 'realm' when calling realmComponentsIdSubComponentTypesGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling realmComponentsIdSubComponentTypesGet");
      }

      let pathParams = {
        'realm': realm,
        'id': id
      };
      let queryParams = {
        'type': opts['type']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['access_token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [ComponentTypeRepresentation];
      return this.apiClient.callApi(
        '/{realm}/components/{id}/sub-component-types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the realmComponentsPost operation.
     * @callback module:api/ComponentApi~realmComponentsPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} realm realm name (not id!)
     * @param {module:model/ComponentRepresentation} componentRepresentation 
     * @param {module:api/ComponentApi~realmComponentsPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    realmComponentsPost(realm, componentRepresentation, callback) {
      let postBody = componentRepresentation;
      // verify the required parameter 'realm' is set
      if (realm === undefined || realm === null) {
        throw new Error("Missing the required parameter 'realm' when calling realmComponentsPost");
      }
      // verify the required parameter 'componentRepresentation' is set
      if (componentRepresentation === undefined || componentRepresentation === null) {
        throw new Error("Missing the required parameter 'componentRepresentation' when calling realmComponentsPost");
      }

      let pathParams = {
        'realm': realm
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['access_token'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/{realm}/components', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
