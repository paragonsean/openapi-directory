/**
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Server from '../model/Server';
import Servers from '../model/Servers';

/**
* Servers service.
* @module api/ServersApi
* @version 2.2
*/
export default class ServersApi {

    /**
    * Constructs a new ServersApi. 
    * @alias module:api/ServersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createServer operation.
     * @callback module:api/ServersApi~createServerCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Server} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new server
     * Create a new server. Required permission: global 'createserver'.
     * @param {module:model/Server} createServerBody Server data (note that serverid, serverpk and validtime are generated by the server)
     * @param {module:api/ServersApi~createServerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Server}
     */
    createServer(createServerBody, callback) {
      let postBody = createServerBody;
      // verify the required parameter 'createServerBody' is set
      if (createServerBody === undefined || createServerBody === null) {
        throw new Error("Missing the required parameter 'createServerBody' when calling createServer");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = ['application/json'];
      let accepts = ['application/octet-stream'];
      let returnType = Server;
      return this.apiClient.callApi(
        '/servers/', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteServerAttribute operation.
     * @callback module:api/ServersApi~deleteServerAttributeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete specific attribute of a specific server
     * Delete attribute with the specified key of a specific server. Required permission: 'servers'.
     * @param {String} serverid Base64 encoded server id
     * @param {String} attributekey Key of the attribute
     * @param {module:api/ServersApi~deleteServerAttributeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteServerAttribute(serverid, attributekey, callback) {
      let postBody = null;
      // verify the required parameter 'serverid' is set
      if (serverid === undefined || serverid === null) {
        throw new Error("Missing the required parameter 'serverid' when calling deleteServerAttribute");
      }
      // verify the required parameter 'attributekey' is set
      if (attributekey === undefined || attributekey === null) {
        throw new Error("Missing the required parameter 'attributekey' when calling deleteServerAttribute");
      }

      let pathParams = {
        'serverid': serverid,
        'attributekey': attributekey
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/servers/{serverid}/attributes/{attributekey}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteServerAttributes operation.
     * @callback module:api/ServersApi~deleteServerAttributesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete all attributes of a specific server
     * Delete all attributes of a specific server. Required permission: 'servers'.
     * @param {String} serverid Base64 encoded server id
     * @param {module:api/ServersApi~deleteServerAttributesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteServerAttributes(serverid, callback) {
      let postBody = null;
      // verify the required parameter 'serverid' is set
      if (serverid === undefined || serverid === null) {
        throw new Error("Missing the required parameter 'serverid' when calling deleteServerAttributes");
      }

      let pathParams = {
        'serverid': serverid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/servers/{serverid}/attributes/', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServer operation.
     * @callback module:api/ServersApi~getServerCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Server} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configuration of a specific server
     * Returns the configuration of a specific server. Required permission: 'servers' or 'createserver'.
     * @param {String} serverid Base64 encoded server id
     * @param {module:api/ServersApi~getServerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Server}
     */
    getServer(serverid, callback) {
      let postBody = null;
      // verify the required parameter 'serverid' is set
      if (serverid === undefined || serverid === null) {
        throw new Error("Missing the required parameter 'serverid' when calling getServer");
      }

      let pathParams = {
        'serverid': serverid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Server;
      return this.apiClient.callApi(
        '/servers/{serverid}/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServerAttributes operation.
     * @callback module:api/ServersApi~getServerAttributesCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all attributes of a specific server
     * Returns an array containing all attributes corresponding to this server. Required permission: 'servers'.
     * @param {String} serverid Base64 encoded server id
     * @param {module:api/ServersApi~getServerAttributesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    getServerAttributes(serverid, callback) {
      let postBody = null;
      // verify the required parameter 'serverid' is set
      if (serverid === undefined || serverid === null) {
        throw new Error("Missing the required parameter 'serverid' when calling getServerAttributes");
      }

      let pathParams = {
        'serverid': serverid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = [];
      let accepts = ['text/plain'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/servers/{serverid}/attributes/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServers operation.
     * @callback module:api/ServersApi~getServersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Servers} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all your servers
     * List all the servers you have the permissions for. Required permission: 'servers'.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Limit the number of results
     * @param {Number} [marker] Offset in the result list
     * @param {module:api/ServersApi~getServersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Servers}
     */
    getServers(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'marker': opts['marker']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Servers;
      return this.apiClient.callApi(
        '/servers/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setServerAttributes operation.
     * @callback module:api/ServersApi~setServerAttributesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set all attributes of a specific server
     * Set the attributes of a specific server. Prior attributes with keys that are not provided in the body of the request will be deleted. Required permission: 'servers'.
     * @param {String} serverid Base64 encoded server id
     * @param {Object.<String, Object>} attributes Array of attributes
     * @param {module:api/ServersApi~setServerAttributesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    setServerAttributes(serverid, attributes, callback) {
      let postBody = attributes;
      // verify the required parameter 'serverid' is set
      if (serverid === undefined || serverid === null) {
        throw new Error("Missing the required parameter 'serverid' when calling setServerAttributes");
      }
      // verify the required parameter 'attributes' is set
      if (attributes === undefined || attributes === null) {
        throw new Error("Missing the required parameter 'attributes' when calling setServerAttributes");
      }

      let pathParams = {
        'serverid': serverid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/servers/{serverid}/attributes/', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServer operation.
     * @callback module:api/ServersApi~updateServerCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Server} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update configuration of a specific server
     * Update the configuration of a specific server. Required permission: 'createserver'.
     * @param {String} serverid Base64 encoded server id
     * @param {module:model/Server} server Server data (note that serverid and serverpk cannot be changed)
     * @param {module:api/ServersApi~updateServerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Server}
     */
    updateServer(serverid, server, callback) {
      let postBody = server;
      // verify the required parameter 'serverid' is set
      if (serverid === undefined || serverid === null) {
        throw new Error("Missing the required parameter 'serverid' when calling updateServer");
      }
      // verify the required parameter 'server' is set
      if (server === undefined || server === null) {
        throw new Error("Missing the required parameter 'server' when calling updateServer");
      }

      let pathParams = {
        'serverid': serverid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Server;
      return this.apiClient.callApi(
        '/servers/{serverid}/', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateServerAttributes operation.
     * @callback module:api/ServersApi~updateServerAttributesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update specified attributes of a specific server
     * Update the specified attributes of a specific server. Prior attributes with keys that are not provided in the body of the request will not be deleted. Required permission: 'servers'.
     * @param {String} serverid Base64 encoded server id
     * @param {Object.<String, Object>} attributes Array of attributes
     * @param {module:api/ServersApi~updateServerAttributesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateServerAttributes(serverid, attributes, callback) {
      let postBody = attributes;
      // verify the required parameter 'serverid' is set
      if (serverid === undefined || serverid === null) {
        throw new Error("Missing the required parameter 'serverid' when calling updateServerAttributes");
      }
      // verify the required parameter 'attributes' is set
      if (attributes === undefined || attributes === null) {
        throw new Error("Missing the required parameter 'attributes' when calling updateServerAttributes");
      }

      let pathParams = {
        'serverid': serverid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'role_id'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/servers/{serverid}/attributes/', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
