/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01-privatepreview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CloudError from '../model/CloudError';
import PrivateEndpointConnection from '../model/PrivateEndpointConnection';
import PrivateEndpointConnectionListResult from '../model/PrivateEndpointConnectionListResult';
import TagsObject from '../model/TagsObject';

/**
* PrivateEndpointConnections service.
* @module api/PrivateEndpointConnectionsApi
* @version 2018-06-01-privatepreview
*/
export default class PrivateEndpointConnectionsApi {

    /**
    * Constructs a new PrivateEndpointConnectionsApi. 
    * @alias module:api/PrivateEndpointConnectionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the privateEndpointConnectionsCreateOrUpdate operation.
     * @callback module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PrivateEndpointConnection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Approve or reject a private endpoint connection with a given name.
     * @param {String} resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
     * @param {String} serverName The name of the server.
     * @param {String} privateEndpointConnectionName 
     * @param {String} subscriptionId The subscription ID that identifies an Azure subscription.
     * @param {String} apiVersion The API version to use for the request.
     * @param {module:model/PrivateEndpointConnection} parameters 
     * @param {module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PrivateEndpointConnection}
     */
    privateEndpointConnectionsCreateOrUpdate(resourceGroupName, serverName, privateEndpointConnectionName, subscriptionId, apiVersion, parameters, callback) {
      let postBody = parameters;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling privateEndpointConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'serverName' is set
      if (serverName === undefined || serverName === null) {
        throw new Error("Missing the required parameter 'serverName' when calling privateEndpointConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'privateEndpointConnectionName' is set
      if (privateEndpointConnectionName === undefined || privateEndpointConnectionName === null) {
        throw new Error("Missing the required parameter 'privateEndpointConnectionName' when calling privateEndpointConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling privateEndpointConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling privateEndpointConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'parameters' is set
      if (parameters === undefined || parameters === null) {
        throw new Error("Missing the required parameter 'parameters' when calling privateEndpointConnectionsCreateOrUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serverName': serverName,
        'privateEndpointConnectionName': privateEndpointConnectionName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PrivateEndpointConnection;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/privateEndpointConnections/{privateEndpointConnectionName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the privateEndpointConnectionsDelete operation.
     * @callback module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a private endpoint connection with a given name.
     * @param {String} resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
     * @param {String} serverName The name of the server.
     * @param {String} privateEndpointConnectionName 
     * @param {String} subscriptionId The subscription ID that identifies an Azure subscription.
     * @param {String} apiVersion The API version to use for the request.
     * @param {module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    privateEndpointConnectionsDelete(resourceGroupName, serverName, privateEndpointConnectionName, subscriptionId, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling privateEndpointConnectionsDelete");
      }
      // verify the required parameter 'serverName' is set
      if (serverName === undefined || serverName === null) {
        throw new Error("Missing the required parameter 'serverName' when calling privateEndpointConnectionsDelete");
      }
      // verify the required parameter 'privateEndpointConnectionName' is set
      if (privateEndpointConnectionName === undefined || privateEndpointConnectionName === null) {
        throw new Error("Missing the required parameter 'privateEndpointConnectionName' when calling privateEndpointConnectionsDelete");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling privateEndpointConnectionsDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling privateEndpointConnectionsDelete");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serverName': serverName,
        'privateEndpointConnectionName': privateEndpointConnectionName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/privateEndpointConnections/{privateEndpointConnectionName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the privateEndpointConnectionsGet operation.
     * @callback module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PrivateEndpointConnection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a private endpoint connection.
     * @param {String} resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
     * @param {String} serverName The name of the server.
     * @param {String} privateEndpointConnectionName The name of the private endpoint connection.
     * @param {String} subscriptionId The subscription ID that identifies an Azure subscription.
     * @param {String} apiVersion The API version to use for the request.
     * @param {module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PrivateEndpointConnection}
     */
    privateEndpointConnectionsGet(resourceGroupName, serverName, privateEndpointConnectionName, subscriptionId, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling privateEndpointConnectionsGet");
      }
      // verify the required parameter 'serverName' is set
      if (serverName === undefined || serverName === null) {
        throw new Error("Missing the required parameter 'serverName' when calling privateEndpointConnectionsGet");
      }
      // verify the required parameter 'privateEndpointConnectionName' is set
      if (privateEndpointConnectionName === undefined || privateEndpointConnectionName === null) {
        throw new Error("Missing the required parameter 'privateEndpointConnectionName' when calling privateEndpointConnectionsGet");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling privateEndpointConnectionsGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling privateEndpointConnectionsGet");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serverName': serverName,
        'privateEndpointConnectionName': privateEndpointConnectionName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PrivateEndpointConnection;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/privateEndpointConnections/{privateEndpointConnectionName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the privateEndpointConnectionsListByServer operation.
     * @callback module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsListByServerCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PrivateEndpointConnectionListResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets all private endpoint connections on a server.
     * @param {String} resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
     * @param {String} serverName The name of the server.
     * @param {String} subscriptionId The subscription ID that identifies an Azure subscription.
     * @param {String} apiVersion The API version to use for the request.
     * @param {module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsListByServerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PrivateEndpointConnectionListResult}
     */
    privateEndpointConnectionsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling privateEndpointConnectionsListByServer");
      }
      // verify the required parameter 'serverName' is set
      if (serverName === undefined || serverName === null) {
        throw new Error("Missing the required parameter 'serverName' when calling privateEndpointConnectionsListByServer");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling privateEndpointConnectionsListByServer");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling privateEndpointConnectionsListByServer");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serverName': serverName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PrivateEndpointConnectionListResult;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/privateEndpointConnections', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the privateEndpointConnectionsUpdateTags operation.
     * @callback module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsUpdateTagsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PrivateEndpointConnection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates tags on private endpoint connection.
     * Updates private endpoint connection with the specified tags.
     * @param {String} apiVersion The API version to use for the request.
     * @param {String} subscriptionId The subscription ID that identifies an Azure subscription.
     * @param {String} resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
     * @param {String} serverName The name of the server.
     * @param {String} privateEndpointConnectionName 
     * @param {module:model/TagsObject} parameters Parameters supplied to the Update private endpoint connection Tags operation.
     * @param {module:api/PrivateEndpointConnectionsApi~privateEndpointConnectionsUpdateTagsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PrivateEndpointConnection}
     */
    privateEndpointConnectionsUpdateTags(apiVersion, subscriptionId, resourceGroupName, serverName, privateEndpointConnectionName, parameters, callback) {
      let postBody = parameters;
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling privateEndpointConnectionsUpdateTags");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling privateEndpointConnectionsUpdateTags");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling privateEndpointConnectionsUpdateTags");
      }
      // verify the required parameter 'serverName' is set
      if (serverName === undefined || serverName === null) {
        throw new Error("Missing the required parameter 'serverName' when calling privateEndpointConnectionsUpdateTags");
      }
      // verify the required parameter 'privateEndpointConnectionName' is set
      if (privateEndpointConnectionName === undefined || privateEndpointConnectionName === null) {
        throw new Error("Missing the required parameter 'privateEndpointConnectionName' when calling privateEndpointConnectionsUpdateTags");
      }
      // verify the required parameter 'parameters' is set
      if (parameters === undefined || parameters === null) {
        throw new Error("Missing the required parameter 'parameters' when calling privateEndpointConnectionsUpdateTags");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'serverName': serverName,
        'privateEndpointConnectionName': privateEndpointConnectionName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PrivateEndpointConnection;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/privateEndpointConnections/{privateEndpointConnectionName}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
