/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ExpressRouteConnection from '../model/ExpressRouteConnection';
import ExpressRouteConnectionList from '../model/ExpressRouteConnectionList';

/**
* ExpressRouteConnections service.
* @module api/ExpressRouteConnectionsApi
* @version 2019-08-01
*/
export default class ExpressRouteConnectionsApi {

    /**
    * Constructs a new ExpressRouteConnectionsApi. 
    * @alias module:api/ExpressRouteConnectionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the expressRouteConnectionsCreateOrUpdate operation.
     * @callback module:api/ExpressRouteConnectionsApi~expressRouteConnectionsCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpressRouteConnection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} expressRouteGatewayName The name of the ExpressRoute gateway.
     * @param {String} connectionName The name of the connection subresource.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:model/ExpressRouteConnection} putExpressRouteConnectionParameters Parameters required in an ExpressRouteConnection PUT operation.
     * @param {module:api/ExpressRouteConnectionsApi~expressRouteConnectionsCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpressRouteConnection}
     */
    expressRouteConnectionsCreateOrUpdate(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, putExpressRouteConnectionParameters, callback) {
      let postBody = putExpressRouteConnectionParameters;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'expressRouteGatewayName' is set
      if (expressRouteGatewayName === undefined || expressRouteGatewayName === null) {
        throw new Error("Missing the required parameter 'expressRouteGatewayName' when calling expressRouteConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'connectionName' is set
      if (connectionName === undefined || connectionName === null) {
        throw new Error("Missing the required parameter 'connectionName' when calling expressRouteConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteConnectionsCreateOrUpdate");
      }
      // verify the required parameter 'putExpressRouteConnectionParameters' is set
      if (putExpressRouteConnectionParameters === undefined || putExpressRouteConnectionParameters === null) {
        throw new Error("Missing the required parameter 'putExpressRouteConnectionParameters' when calling expressRouteConnectionsCreateOrUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'expressRouteGatewayName': expressRouteGatewayName,
        'connectionName': connectionName,
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
      let returnType = ExpressRouteConnection;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expressRouteConnectionsDelete operation.
     * @callback module:api/ExpressRouteConnectionsApi~expressRouteConnectionsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a connection to a ExpressRoute circuit.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} expressRouteGatewayName The name of the ExpressRoute gateway.
     * @param {String} connectionName The name of the connection subresource.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/ExpressRouteConnectionsApi~expressRouteConnectionsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    expressRouteConnectionsDelete(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteConnectionsDelete");
      }
      // verify the required parameter 'expressRouteGatewayName' is set
      if (expressRouteGatewayName === undefined || expressRouteGatewayName === null) {
        throw new Error("Missing the required parameter 'expressRouteGatewayName' when calling expressRouteConnectionsDelete");
      }
      // verify the required parameter 'connectionName' is set
      if (connectionName === undefined || connectionName === null) {
        throw new Error("Missing the required parameter 'connectionName' when calling expressRouteConnectionsDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteConnectionsDelete");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteConnectionsDelete");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'expressRouteGatewayName': expressRouteGatewayName,
        'connectionName': connectionName,
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expressRouteConnectionsGet operation.
     * @callback module:api/ExpressRouteConnectionsApi~expressRouteConnectionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpressRouteConnection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the specified ExpressRouteConnection.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} expressRouteGatewayName The name of the ExpressRoute gateway.
     * @param {String} connectionName The name of the ExpressRoute connection.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/ExpressRouteConnectionsApi~expressRouteConnectionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpressRouteConnection}
     */
    expressRouteConnectionsGet(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteConnectionsGet");
      }
      // verify the required parameter 'expressRouteGatewayName' is set
      if (expressRouteGatewayName === undefined || expressRouteGatewayName === null) {
        throw new Error("Missing the required parameter 'expressRouteGatewayName' when calling expressRouteConnectionsGet");
      }
      // verify the required parameter 'connectionName' is set
      if (connectionName === undefined || connectionName === null) {
        throw new Error("Missing the required parameter 'connectionName' when calling expressRouteConnectionsGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteConnectionsGet");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteConnectionsGet");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'expressRouteGatewayName': expressRouteGatewayName,
        'connectionName': connectionName,
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
      let returnType = ExpressRouteConnection;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expressRouteConnectionsList operation.
     * @callback module:api/ExpressRouteConnectionsApi~expressRouteConnectionsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpressRouteConnectionList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists ExpressRouteConnections.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} expressRouteGatewayName The name of the ExpressRoute gateway.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/ExpressRouteConnectionsApi~expressRouteConnectionsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpressRouteConnectionList}
     */
    expressRouteConnectionsList(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteConnectionsList");
      }
      // verify the required parameter 'expressRouteGatewayName' is set
      if (expressRouteGatewayName === undefined || expressRouteGatewayName === null) {
        throw new Error("Missing the required parameter 'expressRouteGatewayName' when calling expressRouteConnectionsList");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteConnectionsList");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteConnectionsList");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'expressRouteGatewayName': expressRouteGatewayName,
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
      let returnType = ExpressRouteConnectionList;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
